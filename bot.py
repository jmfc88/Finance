"""
VERSION: 3 (04/08/2026) - añade el segundo método de stop-loss: escalones de
+5% de beneficio desde el punto de equilibrio (precio compra + comisiones +
cambio de divisa si aplica). Cada escalón nuevo avisa la ganancia Y sube el
stop-loss ORIGINAL por ese mismo múltiplo. Convive con el trailing continuo
de siempre — el stop-loss real es siempre el más protector de los dos.

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
    requests.post(
        f"https://ntfy.sh/{NTFY_TOPIC}",
        data=mensaje.encode("utf-8"),
        headers={
            "Title": titulo,
            "Priority": "urgent" if urgente else "default",
            "Tags": "warning" if urgente else "chart_with_upwards_trend",
        },
    )


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
    precio_actual = yf.Ticker(pos["ticker"]).info.get("currentPrice")
    if not precio_actual:
        return pos, False

    stop_anterior = pos.get("stop_loss_actual", 0)
    stop_inicial = pos.get("stop_loss_inicial", stop_anterior)
    cambio_divisa = pos.get("cambio_divisa", False)

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
                f"💰 {pos['ticker']}: ganando ~{escalon_nuevo * 5}%",
                f"Precio actual {precio_actual}$, un {escalon_nuevo * 5}% por encima de tu punto de "
                f"equilibrio ({precio_ganancia:.2f}$). Tu stop-loss sube a {stop_escalones}$.",
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
                f"📈 {pos['ticker']} sube — sube tu stop-loss",
                f"Nuevo máximo: {precio_actual}$. Sube tu stop-loss en Trade Republic de "
                f"{stop_anterior}$ a {nuevo_stop}$ (protege más ganancia ya conseguida).",
                urgente=False,
            )

    salto = precio_actual <= pos.get("stop_loss_actual", 0)
    if salto:
        neto = beneficio_neto(pos["precio_compra"], precio_actual, pos["acciones"])
        notificar(
            f"🔴 VENDE {pos['ticker']} - stop-loss activado",
            f"Precio actual: {precio_actual}$. Stop-loss: {pos['stop_loss_actual']}$. "
            f"Beneficio neto estimado si vendes ahora: {neto}€. Ejecuta la venta en Trade Republic.",
        )
    return pos, salto


def ejecutar():
    posiciones = cargar_posiciones()
    if not posiciones:
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