"""
VERSION: 8 (06/08/2026) - añade avisos tempranos de pérdida: -7,5%
"[CUIDADO]" y -10% "[PIENSA]", antes del stop-loss real (normalmente
-12,5%, que ya existía como "[VENDE]"). Cada nivel avisa una sola vez,
misma fórmula que los presets del simulador (comisiones + cambio de
divisa incluidos), para que los tres niveles sean consistentes entre sí.

BOT DE STOP-LOSS DINÁMICO
==========================================
Trade Republic no tiene trailing stop nativo, así que este bot lo
sustituye: vigila tus posiciones abiertas y, en cuanto el precio cae
hasta el nivel de stop-loss (que solo sube, nunca baja, protegiendo
siempre ganancia neta ya conseguida), te avisa por notificación al
móvil vía ntfy.sh.

Es la ÚNICA notificación que Jose Manuel quiere: protege de pérdidas,
no empuja decisiones de compra.

Entrada:  posiciones.json -> lista de posiciones abiertas
Salida:   posiciones.json actualizado (nuevo stop-loss si ha subido)
          + notificación si el stop-loss ha saltado
"""

import json
import os

import requests
import yfinance as yf

POSICIONES_FILE = "posiciones.json"
LEDGER_FILE = "ledger.json"
NTFY_TOPIC = os.environ.get("NTFY_TOPIC")

COMISION_COMPRA = 1.0
COMISION_VENTA = 1.0
TAX_RATE = 0.19
COSTE_FX_PCT = 1.2  # % estimado de coste de cambio de divisa (igual que en el simulador)

# Ejemplo de posiciones.json:
# [
#   {
#     "ticker": "OUST",
#     "precio_compra": 41.30,
#     "acciones": 3,
#     "stop_loss_actual": 39.50,     # se actualiza solo, solo puede subir
#     "stop_loss_inicial": 39.50,    # el que pusiste al abrir la posición, NO se toca nunca
#     "trailing_pct": 8,             # % por debajo del máximo alcanzado (método 1)
#     "maximo_alcanzado": 45.10,
#     "cambio_divisa": false,        # true si la acción no cotiza en euros
#     "escalon_actual": 0            # cuántos escalones de +5% de beneficio ya se han disparado
#   }
# ]


def cargar_posiciones():
    if not os.path.exists(POSICIONES_FILE):
        return []
    with open(POSICIONES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_posiciones(posiciones):
    with open(POSICIONES_FILE, "w", encoding="utf-8") as f:
        json.dump(posiciones, f, indent=2, ensure_ascii=False)


def calcular_stop_loss_inicial(precio_compra, acciones, cambio_divisa, pct=12.5):
    """Mismo cálculo que el simulador: pérdida máxima X% sobre lo invertido,
    comisiones y coste de cambio de divisa incluidos. Se usa como valor de
    referencia automático al detectar una posición nueva — el usuario puede
    ajustarlo luego editando posiciones.json si no es el preset que quería."""
    comisiones = COMISION_COMPRA + COMISION_VENTA
    coste_fx = precio_compra * (COSTE_FX_PCT / 100) if cambio_divisa else 0
    importe_invertido = precio_compra * acciones
    perdida_maxima = importe_invertido * (pct / 100)
    return round(precio_compra - ((perdida_maxima - comisiones - coste_fx) / acciones), 4)


def reconciliar_con_ledger(posiciones):
    """Lee ledger.json (el registro del simulador) y ajusta posiciones.json
    solo, sin que el usuario tenga que editarlo a mano: añade las posiciones
    abiertas nuevas que detecte, y quita las que ya se hayan vendido del
    todo. Si ledger.json no existe o no se puede leer, sigue con lo que
    hubiera en posiciones.json tal cual, sin romper nada."""
    if not os.path.exists(LEDGER_FILE):
        return posiciones

    try:
        with open(LEDGER_FILE, "r", encoding="utf-8") as f:
            ledger = json.load(f)
    except Exception:
        return posiciones

    # Acciones netas abiertas por ticker, según el ledger (FIFO ya resuelto
    # por el simulador: acciones_restantes de cada compra)
    abiertas = {}
    for op in ledger:
        if op.get("tipo") != "compra" or op.get("acciones_restantes", 0) <= 0:
            continue
        t = op["ticker"]
        if t not in abiertas:
            abiertas[t] = {"acciones": 0, "coste_total": 0, "cambio_divisa": op.get("cambio_divisa", False)}
        abiertas[t]["acciones"] += op["acciones_restantes"]
        abiertas[t]["coste_total"] += op["acciones_restantes"] * op["precio"]

    posiciones_por_ticker = {p["ticker"]: p for p in posiciones}

    # Quita del vigilante las que ya no están abiertas en el ledger (vendidas del todo)
    for ticker in list(posiciones_por_ticker):
        if ticker not in abiertas:
            print(f"{ticker}: ya no aparece abierta en el ledger, se quita de la vigilancia.")
            del posiciones_por_ticker[ticker]

    # Añade las que están abiertas en el ledger pero el bot todavía no vigilaba
    for ticker, datos in abiertas.items():
        if ticker in posiciones_por_ticker:
            continue
        precio_compra = round(datos["coste_total"] / datos["acciones"], 4)
        stop_inicial = calcular_stop_loss_inicial(precio_compra, datos["acciones"], datos["cambio_divisa"])
        posiciones_por_ticker[ticker] = {
            "ticker": ticker,
            "precio_compra": precio_compra,
            "acciones": datos["acciones"],
            "cambio_divisa": datos["cambio_divisa"],
            "stop_loss_inicial": stop_inicial,
            "stop_loss_actual": stop_inicial,
            "trailing_pct": 8,
            "maximo_alcanzado": precio_compra,
            "escalon_actual": 0,
            "avisos_perdida_disparados": [],
        }
        notificar(
            f"[NUEVA POSICIÓN] {ticker}",
            f"Detectada en el ledger, no estaba en la vigilancia. Precio de compra: {precio_compra}€, "
            f"{datos['acciones']} acciones. Stop-loss inicial puesto por defecto (preset 12,5%) en "
            f"{stop_inicial}€ — revísalo y ajústalo si querías otro nivel.",
            urgente=False,
        )

    return list(posiciones_por_ticker.values())


def beneficio_neto(precio_compra, precio_venta, acciones):
    bruto = (precio_venta - precio_compra) * acciones
    comisiones = COMISION_COMPRA + COMISION_VENTA
    ganancia_antes_impuesto = bruto - comisiones
    impuesto = max(ganancia_antes_impuesto, 0) * TAX_RATE
    return round(ganancia_antes_impuesto - impuesto, 2)


def notificar(titulo, mensaje, urgente=True):
    if not NTFY_TOPIC:
        print(f"[SIN NTFY_TOPIC] {titulo}: {mensaje}")
        return
    # Se usa el formato JSON de ntfy (no las cabeceras HTTP normales) porque
    # las cabeceras solo admiten un juego de caracteres muy limitado (Latin-1)
    # y los emojis () rompían el envío con un UnicodeEncodeError.
    try:
        requests.post(
            "https://ntfy.sh/",
            json={
                "topic": NTFY_TOPIC,
                "title": titulo,
                "message": mensaje,
                "priority": 5 if urgente else 3,
                "tags": ["warning"] if urgente else ["chart_with_upwards_trend"],
            },
            timeout=10,
        )
    except Exception as e:
        print(f"No se pudo enviar la notificación ({titulo}): {e}")

def obtener_tasa_cambio(moneda_origen):
    """Convierte cualquier divisa a euros con una API gratuita sin clave.
    Si falla, devuelve None — en ese caso NO se procesa la posición esta
    vez (mejor no comparar nada, que comparar mal)."""
    if moneda_origen == "EUR":
        return 1.0
    try:
        resp = requests.get(
            f"https://api.frankfurter.dev/v1/latest?base={moneda_origen}&symbols=EUR",
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json().get("rates", {}).get("EUR")
    except Exception:
        return None


def procesar_posicion(pos):
    """Calcula el stop-loss con DOS métodos que conviven a la vez, y se
    queda siempre con el más protector (el más alto) de los dos — nunca
    con el más bajo, y nunca baja respecto al que ya había:

    Método 1 (el de siempre): trailing continuo, baja del máximo precio
    alcanzado según trailing_pct.

    Método 2 (nuevo): escalones de +5% de beneficio desde el punto de
    equilibrio (precio de compra + comisiones + cambio de divisa si
    aplica). Cada vez que el precio supera un escalón nuevo (5%, 10%,
    15%...), avisa de la ganancia Y sube el stop-loss ORIGINAL (no el
    actual) por ese mismo múltiplo — así, pasados suficientes escalones,
    el peor caso deja de ser perder dinero y pasa a ser ganar algo seguro.
    """
    info = yf.Ticker(pos["ticker"]).info
    precio_nativo = info.get("currentPrice")
    if not precio_nativo:
        return pos, False

    # CRÍTICO: Yahoo da el precio en la divisa real de cotización (ej. CAD
    # para tickers .TO), no en euros. Compararlo directamente contra un
    # punto de equilibrio en euros sería comparar unidades distintas.
    # Se detecta la divisa real (no solo el checkbox) y se convierte con
    # un tipo de cambio en vivo antes de cualquier cálculo.
    moneda = info.get("currency", "EUR")
    tasa = obtener_tasa_cambio(moneda)
    if tasa is None:
        print(f"No se pudo obtener el tipo de cambio {moneda}->EUR, se salta {pos['ticker']} esta vez")
        return pos, False
    precio_actual = round(precio_nativo * tasa, 4)

    stop_anterior = pos.get("stop_loss_actual", 0)
    stop_inicial = pos.get("stop_loss_inicial", stop_anterior)
    cambio_divisa = pos.get("cambio_divisa", False) or moneda != "EUR"

    # --- Método 3: avisos tempranos de pérdida (-7,5% y -10%), antes del
    # stop-loss real (normalmente -12,5%). Cada nivel avisa una sola vez. ---
    avisos_disparados = set(pos.get("avisos_perdida_disparados", []))
    niveles_aviso_perdida = [
        (7.5, "[CUIDADO]", "está bajando. Nada urgente todavía, solo un ojo."),
        (10.0, "[PIENSA]", "ya llevas aproximadamente un -10% sobre lo invertido. Piensa si vender ahora o esperar a ver si se recupera."),
    ]
    for pct, etiqueta, texto in niveles_aviso_perdida:
        if pct in avisos_disparados:
            continue
        umbral = calcular_stop_loss_inicial(pos["precio_compra"], pos["acciones"], cambio_divisa, pct)
        if precio_actual <= umbral:
            avisos_disparados.add(pct)
            notificar(
                f"{etiqueta} {pos['ticker']}",
                f"Precio actual {precio_actual}€. {pos['ticker']} {texto}",
                urgente=False,
            )
    pos["avisos_perdida_disparados"] = sorted(avisos_disparados)

    # --- Método 1: trailing continuo (el de siempre) ---
    if precio_actual > pos.get("maximo_alcanzado", pos["precio_compra"]):
        pos["maximo_alcanzado"] = precio_actual
    stop_trailing = round(pos.get("maximo_alcanzado", pos["precio_compra"]) * (1 - pos["trailing_pct"] / 100), 2)

    # --- Método 2: escalones de beneficio del 5% desde el punto de equilibrio ---
    comisiones = COMISION_COMPRA + COMISION_VENTA
    coste_fx = pos["precio_compra"] * (COSTE_FX_PCT / 100) if cambio_divisa else 0
    precio_ganancia = pos["precio_compra"] + coste_fx + (comisiones / pos["acciones"])

    escalon_anterior = pos.get("escalon_actual", 0)
    escalon_nuevo = escalon_anterior
    stop_escalones = stop_anterior
    aviso_ganancia = None

    if precio_actual > precio_ganancia:
        escalon_calculado = int((precio_actual / precio_ganancia - 1) // 0.05)
        if escalon_calculado > escalon_anterior:
            escalon_nuevo = escalon_calculado
            stop_escalones = round(stop_inicial * (1 + 0.05 * escalon_nuevo), 2)
            aviso_ganancia = (
                f"[GANANCIA] {pos['ticker']}: ganando ~{escalon_nuevo * 5}%",
                f"Precio actual {precio_actual}€, un {escalon_nuevo * 5}% por encima de tu punto de "
                f"equilibrio ({precio_ganancia:.2f}€). Tu stop-loss sube a {stop_escalones}€.",
            )

    pos["escalon_actual"] = escalon_nuevo

    # El stop-loss real es siempre el MÁS PROTECTOR de los dos métodos, y nunca baja
    nuevo_stop = max(stop_anterior, stop_trailing, stop_escalones)

    if nuevo_stop > stop_anterior:
        pos["stop_loss_actual"] = nuevo_stop
        if aviso_ganancia:
            notificar(aviso_ganancia[0], aviso_ganancia[1], urgente=False)
        else:
            notificar(
                f"[SUBE STOP-LOSS] {pos['ticker']}",
                f"Nuevo máximo: {precio_actual}€. Sube tu stop-loss en Trade Republic de "
                f"{stop_anterior}€ a {nuevo_stop}€ (protege más ganancia ya conseguida).",
                urgente=False,
            )

    salto = precio_actual <= pos.get("stop_loss_actual", 0)
    if salto:
        neto = beneficio_neto(pos["precio_compra"], precio_actual, pos["acciones"])
        notificar(
            f"[VENDE] {pos['ticker']} - stop-loss activado",
            f"Precio actual: {precio_actual}€. Stop-loss: {pos['stop_loss_actual']}€. "
            f"Beneficio neto estimado si vendes ahora: {neto}€. Ejecuta la venta en Trade Republic.",
        )
    return pos, salto


def ejecutar():
    posiciones = cargar_posiciones()
    posiciones = reconciliar_con_ledger(posiciones)

    if not posiciones:
        guardar_posiciones(posiciones)  # guarda por si la reconciliación vació la lista (todo vendido)
        print("No hay posiciones abiertas que vigilar.")
        return

    actualizadas = []
    for pos in posiciones:
        pos_actualizada, salto = procesar_posicion(pos)
        actualizadas.append(pos_actualizada)
        if salto:
            print(f"{pos['ticker']}: stop-loss saltado, notificación enviada.")
        else:
            print(f"{pos['ticker']}: sigue en vigilancia, stop-loss en {pos_actualizada.get('stop_loss_actual')}")

    guardar_posiciones(actualizadas)


if __name__ == "__main__":
    ejecutar()

