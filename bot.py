"""
VERSION: 26 (31/08/2026) - fuera el aviso [AMPLIA EL HORARIO]. Estaba roto con
los mercados que cruzan la medianoche (el australiano lo disparaba cada 13
minutos diciendo que el bot "solo corre de 0:00 a 24:00") y era redundante:
el cron ya corre las 24 horas y quien decide es marketState de Yahoo.

VERSION: 25 (27/08/2026) - FRANJA_CRON_UTC pasa a 24 h: el workflow ya no
recorta horas y es este archivo quien decide, preguntando a Yahoo si el
mercado de cada accion esta abierto.

VERSION: 25 (27/08/2026) - avisa si una posicion cotiza en un mercado que el
cron del workflow no cubre. El bot no puede ampliarse el horario solo (GitHub
no deja que el token de Actions toque .github/workflows), pero al menos ya no
se queda vigilando a medias en silencio.

VERSION: 24 (27/08/2026) - el stop inicial usa la comision real de la compra,
no 1 EUR fijo. Y el aviso [CREA EL STOP-LOSS] respeta el horario del mercado:
se detectaba la posicion nueva antes de comprobar si estaba abierto, asi que
podia llegar de noche.

VERSION: 23 (26/08/2026) - cada posicion se vigila en el horario de SU
mercado, leyendo marketState de Yahoo. El workflow pasa a correr todo el dia y
es el bot quien decide si toca mirar.

VERSION: 22 (25/08/2026) - fuera el trailing y los escalones automaticos.
[VENDE] es exclusivo del -8%.

VERSION: 21 (25/08/2026) - dos avisos separados en el equilibrio, margen del
2% (no 0,02%), avisos de perdida rearmables y con el precio y el porcentaje
real dentro, y el stop del -8% ahora descuenta las comisiones como ya hacian
los avisos de -5% y -6,5%.

VERSION: 20 (25/08/2026) - FUERA los suelos automaticos.

Me habia pasado de listo: programe que el bot subiera el stop-loss solo al
tocar el equilibrio y al llegar al 7%. Pero eso no es lo que hace falta. Jose
Manuel mueve el stop A MANO en Trade Republic, apretandolo poco a poco segun
sube el precio, y lo que necesita del bot es que le DIGA LOS NUMEROS en el
momento oportuno. El bot avisa; el decide y ejecuta.

Asi que los avisos ahora traen la cifra concreta que poner en la aplicacion,
y el bot ya no toca nada por su cuenta.

VERSION: 19 (25/08/2026) - tres fallos que salieron al simular el bot entero
con precios inventados, y que no se veian leyendo el codigo:

  1. Si una posicion no tenia stop_loss_inicial, el respaldo usaba el stop
     ACTUAL. Como los escalones multiplican ese valor y el stop actual sube
     con los suelos, se componia sobre si mismo: con el precio en 27,20 el
     stop se puso en 28,24, por ENCIMA del precio, y disparaba un [VENDE]
     falso en cada ronda para siempre. Le pasa a cualquier posicion guardada
     por una version antigua. Ahora se recalcula desde el precio de compra.

  2. Habia DOS puntos de equilibrio distintos en el mismo bot: los escalones
     usaban 24,70 (comision fija de 1 EUR) y los avisos 24,7487 (la comision
     real de 1,39 con la tasa italiana). Ahora comparten el mismo.

  3. Red de seguridad: el stop no puede colocarse nunca igual o por encima
     del precio actual. Un stop asi siempre es un error de calculo, y sin
     esta comprobacion se traduce en una orden de venta inmediata.

VERSION: 18 (25/08/2026) - "[PIENSA]" pasa a "[OJO CUIDADO]"

NOTA sobre el reparto de comisiones, que pregunto Jose Manuel el 25/08:
todo esto se piensa en precio por accion, y las comisiones se reparten entre
5 acciones o entre 17 segun lo que se compre. La formula ya lo tiene en
cuenta, porque divide entre el numero de acciones:

    equilibrio = precio_compra + (comision_compra + comision_venta) / acciones

Y el resultado es menos intuitivo de lo que parece: en PORCENTAJE da
practicamente igual. Con 200 EUR invertidos hay que subir un 1% tanto si son
5 acciones de 40 EUR como si son 100 de 2 EUR. Con pocas acciones la comision
por accion es alta, pero cada accion cuesta mas, y se compensa exacto.

Lo que si cambia el listo es cuanto se invierte en total: 2 EUR de comision
sobre 100 son un 2%, sobre 500 un 0,4%. Y la tasa segun el pais: sin tasa hay
que subir un 1%, en Italia o Espana un 1,20%, en Francia un 1,30%. y el mensaje
dice el porcentaje que se esta perdiendo, igual que el de -5%.

VERSION: 17 (25/08/2026) - tres retoques pedidos el 25/08:
  - "[CUIDADO]" pasa a "[VIGILA] estamos perdiendo un 5%". La palabra cuidado
    no le gustaba y tiene razon: a ese nivel no hay que hacer nada, asi que
    una etiqueta que suena a alarma es enganosa.
  - "[POR DEBAJO]" pasa a "[EQUILIBRIO PERDIDO]", y el texto dice
    explicitamente que la alerta de equilibrio queda rearmada.
  - El aviso del 7% estima ademas lo que quedaria despues de Hacienda.

VERSION: 16 (25/08/2026) - margen del 0,02% a los dos lados del equilibrio,
segun la nota del 25/08. Se comprobo antes de ponerlo si un margen tan fino
daria un goteo de avisos: con la volatilidad real de LTMC.MI (1,58% diario)
salen unos 0,4 al dia, asi que no. Quien evita el goteo es la alternancia, no
el ancho de la banda.

VERSION: 15 (25/08/2026) - el equilibrio es una LINEA que se cruza en los dos
sentidos, no un aviso de una sola vez. Sustituye a la escalera porcentual de
la v14, que no era lo que Jose Manuel habia dibujado.

VERSION: 14 (25/08/2026) - ESCALERA DE AVISOS sobre el punto de ganancia.

Lo que pidio Jose Manuel: una vez que salta el aviso de que ya hay beneficio,
ese aviso no debe repetirse aunque el precio cruce el umbral veinte veces el
mismo dia. En su lugar se arman DOS avisos nuevos referidos a ese punto:
uno si sube un paso, otro si baja un paso. Y al subir, la referencia sube con
el precio, de modo que la escalera lo va siguiendo.

SU DUDA ERA CORRECTA: pregunto si un 10% seria buen paso y la respuesta es
que no. Con la compra de Lottomatica (equilibrio 24,749 y suelo en 24,45),
un paso del 10% pone el aviso de bajada en 22,27, muy por debajo del
stop-loss: saltaria antes el [VENDE] y ese aviso no llegaria jamas. De hecho
justo al cruzar el equilibrio solo hay un 1,21% de margen hasta el suelo.

Por eso el aviso de bajada NO se coloca a ciegas: si el paso lo dejaria por
debajo del stop, se omite y se dice por que. Segun sube el precio y sube el
stop, el margen cambia, asi que se recalcula en cada ronda.

PASO_ALERTA_PCT se puede cambiar sin tocar codigo: basta con crear
config_alertas.json en el repo con {"paso_alerta_pct": 1.5}.

VERSION: 13 (24/08/2026) - SUELOS QUE NO BAJAN. Resuelve el problema que
planteo Jose Manuel: el aviso de [EQUILIBRIO] salta una vez, pero despues el
precio sube y baja varias veces el mismo dia, y hasta ahora eso no cambiaba
nada. Una posicion podia estar en verde por la manana y acabar saltando el
stop del -8% por la tarde: perdiendo dinero en una operacion que YA habia
cubierto las comisiones.

Mas avisos no era la solucion (serian decenas al dia y dejaria de leerlos).
La solucion es que el suelo suba solo y NO VUELVA A BAJAR NUNCA:

  Suelo 1 - se arma cuando el precio alcanza el punto de equilibrio.
            El stop no vuelve a bajar del PRECIO DE COMPRA. Se pone en el
            precio de compra y no en el equilibrio a proposito: deja algo de
            margen para el vaiven normal del dia. Es exactamente lo que hace
            Jose Manuel a mano ("compro a 100, llega a 105, subo el stop a
            100 porque ya no pierdo dinero").

  Suelo 2 - se arma cuando la ganancia neta llega al 7%.
            El stop no vuelve a bajar del punto de EQUILIBRIO. A partir de
            ahi la operacion no puede acabar en perdida pase lo que pase.

Una vez armados, ni el trailing ni nada pueden bajarlos. Y el aviso de

VERSION: 12 (24/08/2026) - dos avisos NUEVOS de ganancia, y un arreglo de
fondo que hacia falta para que sean correctos.

EL ARREGLO: coste_total se calculaba como acciones x precio, SIN las
comisiones. Con la compra de Lottomatica quedo claro por que importa: 8
acciones a 24,45 son 195,60, pero el coste real fue 196,99 porque Trade
Republic cobro 1 EUR de comision MAS 0,39 EUR de tasa a las transacciones
financieras (el 0,2% que aplica Italia, y que tambien aplican Espana al 0,2%
y Francia al 0,3%). Ahora se lee la comision real de cada compra del ledger,
asi que el punto de equilibrio sale exacto.

LOS AVISOS NUEVOS, ambos una sola vez por posicion:

  [EQUILIBRIO]  el precio ha alcanzado el punto a partir del cual la
                operacion ya no pierde dinero, comisiones y tasas incluidas.
                Es el momento de subir el stop-loss al precio de compra:
                a partir de ahi ya no se puede perder.

  [GANANCIA]    la posicion da un 7% neto sobre lo invertido, con todas las
                comisiones ya descontadas.

Con esto no hace falta poner alertas de precio a mano en Trade Republic.

VERSION: 11 (23/08/2026) - baja el riesgo por decision de Jose Manuel: con
poco patrimonio, perder un 12,5% por operacion es demasiado. Nuevos niveles:

  -5,0%  [VIGILA]   aviso informativo, no hay que hacer nada
  -6,5%  [OJO CUIDADO] aviso de decision
  -8,0%  [VENDE]    stop-loss real

Antes eran -7,5% / -10% / -12,5%. El aviso de cierre de mercado (Metodo 4)
baja tambien de -7,5% a -5%, para que acompane al primer nivel.

NOTA sobre el -12,5% anterior: en la practica nunca llego a aplicarse. El
trailing del 8% arranca desde el precio de compra y bot.py se queda siempre
con el stop mas protector, asi que el stop efectivo del dia 1 ya era -8%.
Este cambio no endurece la venta: la deja donde ya estaba de hecho, y lo que
cambia de verdad son los dos avisos, que ahora llegan antes.

AVISO SOBRE EL RUIDO: a -5% un valor de volatilidad normal (2% diario) toca
ese nivel por puro vaiven cada pocas sesiones. El [VIGILA] esta pensado como
informacion, NO como senal de venta. La venta sigue siendo solo el -8%.

VERSION: 10 (20/08/2026) - añade el Método 4: aviso al CIERRE de mercado si
la posición sigue por debajo del -5% (usa el "marketState" de Yahoo, así
no hace falta programar a mano el horario de cada bolsa), y un único
recordatorio a la siguiente APERTURA si cerró en pérdida el día anterior.

VERSION: 9 (11/08/2026) - añade Opción B (Stooq, gratis y sin clave) si
Yahoo Finance falla o no da precio — antes, una caída puntual de Yahoo
dejaba la posición sin vigilar esa pasada sin más remedio. Solo cubre
tickers de EE.UU. sin sufijo (el mapeo a Stooq para otras bolsas no es
fiable). También envuelto en try/except el propio yf.Ticker().info por si
Yahoo cae del todo, no solo si devuelve precio vacío.

VERSION: 8 (06/08/2026) - añade avisos tempranos de pérdida: -7,5%
"[VIGILA]" y -6,5% "[OJO CUIDADO]", antes del stop-loss real (-8%, que ya
existía como "[VENDE]"). Cada nivel avisa una sola vez,
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
import math
import os
from datetime import datetime

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


# Paso de la escalera de avisos, en % sobre el punto de referencia. Se puede
# cambiar creando config_alertas.json en la raiz del repo:
#     {"paso_alerta_pct": 1.5}
# Ojo: un paso grande deja el aviso de bajada por debajo del stop-loss y ese
# aviso no llega nunca. El sistema lo detecta y lo omite, pero conviene
# elegirlo con cabeza.
PASO_ALERTA_PCT = 1.0


def cargar_config_alertas():
    try:
        with open("config_alertas.json", "r", encoding="utf-8") as f:
            cfg = json.load(f)
        valor = float(cfg.get("paso_alerta_pct", PASO_ALERTA_PCT))
        if 0.1 <= valor <= 20:
            return valor
        print(f"paso_alerta_pct fuera de rango ({valor}), se usa {PASO_ALERTA_PCT}")
    except (FileNotFoundError, json.JSONDecodeError, TypeError, ValueError):
        pass
    return PASO_ALERTA_PCT


# Escalones de ganancia sobre lo invertido. Se puede alargar la lista.
NIVELES_GANANCIA = [7, 10, 12.5, 15, 20, 25, 30]


# Horario de cada mercado en UTC, para avisar si el cron del workflow se queda
# corto. Son aproximados y con margen: solo sirven para detectar un descuadre
# grande, no para decidir si mirar o no (eso lo dice marketState de Yahoo).
# NOTA (31/08/2026): aqui vivia una tabla de horarios por mercado y un aviso
# [AMPLIA EL HORARIO] que saltaba cuando una posicion cotizaba fuera de la
# franja del cron. Se ha quitado por dos motivos:
#
#   1. Estaba mal. No sabia tratar los mercados que cruzan la medianoche: el
#      australiano abre a las 23:00 UTC y cierra a las 6:00, y la comprobacion
#      lo daba por descubierto SIEMPRE. Con el cron corriendo las 24 horas
#      mandaba "el bot solo corre de 0:00 a 24:00", que no tiene sentido, y lo
#      repetia cada 13 minutos.
#
#   2. Ya no hace falta. El cron corre las 24 horas y quien decide si toca
#      mirar es marketState de Yahoo, unos renglones mas abajo. La tabla era
#      una duplicacion de esa informacion, y encima peor: hecha a mano, sin
#      cambios de hora y desactualizandose sola.

def cargar_margen_cruce():
    """Margen muerto alrededor del punto de equilibrio, en %.

    Evita que un precio pegado a la linea genere un aviso cada media hora.
    Con 0 se comporta como un cruce puro, que es lo que pidio Jose Manuel;
    el valor por defecto es pequeno a proposito, solo para filtrar el
    temblor de los centimos.
    """
    try:
        with open("config_alertas.json", "r", encoding="utf-8") as f:
            cfg = json.load(f)
        valor = float(cfg.get("margen_cruce_pct", 0.02))
        if 0 <= valor <= 5:
            return valor
    except (FileNotFoundError, json.JSONDecodeError, TypeError, ValueError):
        pass
    return 0.02


def calcular_stop_loss_inicial(precio_compra, acciones, cambio_divisa, pct=8.0,
                               comision_compra=None):
    """Mismo cálculo que el simulador: pérdida máxima X% sobre lo invertido,
    comisiones y coste de cambio de divisa incluidos. Se usa como valor de
    referencia automático al detectar una posición nueva — el usuario puede
    ajustarlo luego editando posiciones.json si no es el preset que quería."""
    # La base del porcentaje es lo INVERTIDO DE VERDAD, comision de compra
    # incluida. Antes se usaba precio x acciones (160 EUR en vez de 161), y por
    # eso un "-8%" acababa siendo un -7,95% real. Sobre poco dinero la
    # diferencia es de centimos, pero es que el numero tiene que ser el que
    # dice que es.
    if comision_compra is None:
        comision_compra = COMISION_COMPRA
    coste_fx = precio_compra * (COSTE_FX_PCT / 100) if cambio_divisa else 0
    invertido = precio_compra * acciones + comision_compra + coste_fx
    perdida_maxima = invertido * (pct / 100)
    return round((invertido + COMISION_VENTA - perdida_maxima) / acciones, 4)


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
            abiertas[t] = {"acciones": 0, "coste_total": 0, "comision_compra": 0,
                           "cambio_divisa": op.get("cambio_divisa", False)}
        abiertas[t]["acciones"] += op["acciones_restantes"]
        abiertas[t]["coste_total"] += op["acciones_restantes"] * op["precio"]
        # La comision real de la compra, tal y como se registro. En las
        # europeas incluye la tasa a las transacciones financieras, que no es
        # despreciable: 0,39 EUR sobre una compra de 195 EUR en Italia.
        # Se prorratea si la compra esta parcialmente vendida.
        com = op.get("comision")
        if com is None:
            com = COMISION_COMPRA
        proporcion = (op["acciones_restantes"] / op["acciones"]) if op.get("acciones") else 1
        abiertas[t]["comision_compra"] += com * proporcion

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
        # Se pasa la comision REAL de la compra. Sin esto usaba 1 EUR fijo, y
        # en Lottomatica (1 EUR + 0,39 de tasa italiana) el stop salia en
        # 22,734 en vez de 22,779: cuatro centimos de mas de perdida antes de
        # que salte. Poco dinero, pero el numero tiene que ser el correcto.
        stop_inicial = calcular_stop_loss_inicial(
            precio_compra, datos["acciones"], datos["cambio_divisa"],
            comision_compra=datos.get("comision_compra", COMISION_COMPRA))
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
            "comision_compra": round(datos.get("comision_compra", COMISION_COMPRA), 4),
            "avisos_perdida_disparados": [],
            "avisos_ganancia_disparados": [],
            "ultimo_cierre_notificado": None,
            "recordatorio_apertura_pendiente": False,
        }
        notificar(
            f"[CREA EL STOP-LOSS] {ticker}",
            f"Pon el stop-loss en {stop_inicial}€, que es un -8% sobre lo invertido "
            f"con las comisiones ya contadas.\n"
            f"Compra registrada: {datos['acciones']} acciones a {precio_compra}€.",
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
    # y los emojis (💰📈🔴🎯) rompían el envío con un UnicodeEncodeError.
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


def obtener_precio_respaldo_stooq(ticker):
    """Opción B si Yahoo Finance falla o no da precio: Stooq, gratis y sin
    clave. Solo se usa para tickers de EE.UU. sin sufijo (ej. "AAPL") —
    para el resto de bolsas (.TO, .AX, .MC...) el mapeo de tickers entre
    Yahoo y Stooq no es lo bastante fiable como para confiar en él a
    ciegas, así que ahí simplemente no hay respaldo por ahora. Devuelve
    (precio, moneda) o (None, None) si falla."""
    if "." in ticker:
        return None, None  # tiene sufijo de bolsa no-US, sin mapeo fiable a Stooq
    try:
        resp = requests.get(
            f"https://stooq.com/q/l/?s={ticker.lower()}.us&f=sd2t2ohlcv&h&e=csv",
            timeout=10,
        )
        resp.raise_for_status()
        lineas = resp.text.strip().splitlines()
        if len(lineas) < 2:
            return None, None
        campos = lineas[1].split(",")
        precio = float(campos[6])  # columna "Close"
        if precio <= 0:
            return None, None
        return precio, "USD"
    except Exception:
        return None, None


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
    try:
        info = yf.Ticker(pos["ticker"]).info
        precio_nativo = info.get("currentPrice")
        moneda = info.get("currency", "EUR")
        estado_mercado = info.get("marketState")
    except Exception:
        precio_nativo, moneda, estado_mercado = None, "EUR", None

    # Cada accion se vigila en el horario de SU mercado, no en el americano.
    # El ticker ya dice donde cotiza (.MI Milan, .MC Madrid, .HK Hong Kong...)
    # y Yahoo devuelve si ese mercado esta abierto ahora mismo, asi que no hace
    # falta mantener una tabla de horarios ni pelearse con los cambios de hora.
    #
    # Esto arregla un agujero de verdad: el workflow corria de 15:00 a 23:00
    # hora espanola, pensado para Wall Street, mientras Lottomatica cotiza en
    # Milan y cierra a las 17:30. De las siete horas y media de sesion italiana
    # solo se vigilaban dos y media. Una caida a las 10 de la manana no la veia
    # nadie.
    if estado_mercado and estado_mercado not in ("REGULAR", "PRE", "POST"):
        print(f"{pos['ticker']}: su mercado está cerrado ({estado_mercado}), no se toca.")
        return pos, False

    if not precio_nativo:
        # Yahoo Finance ha fallado (caída puntual, símbolo no encontrado esa
        # vez...). Antes de rendirnos, probamos la Opción B con Stooq.
        precio_nativo, moneda_respaldo = obtener_precio_respaldo_stooq(pos["ticker"])
        if precio_nativo:
            moneda = moneda_respaldo
            print(f"{pos['ticker']}: Yahoo Finance falló, usado el precio de respaldo de Stooq.")
        else:
            print(f"{pos['ticker']}: no se pudo obtener precio ni de Yahoo ni de Stooq, se salta esta vez.")
            return pos, False

    # CRÍTICO: Yahoo da el precio en la divisa real de cotización (ej. CAD
    # para tickers .TO), no en euros. Compararlo directamente contra un
    # punto de equilibrio en euros sería comparar unidades distintas.
    # Se detecta la divisa real (no solo el checkbox) y se convierte con
    # un tipo de cambio en vivo antes de cualquier cálculo.
    tasa = obtener_tasa_cambio(moneda)
    if tasa is None:
        print(f"No se pudo obtener el tipo de cambio {moneda}->EUR, se salta {pos['ticker']} esta vez")
        return pos, False
    precio_actual = round(precio_nativo * tasa, 4)

    # El respaldo NO puede ser stop_anterior: los escalones multiplican este
    # valor, asi que si se usa el stop actual (que sube con los suelos y el
    # trailing) el resultado se compone sobre si mismo y acaba POR ENCIMA del
    # precio, disparando un [VENDE] falso que ademas no para nunca. Le paso a
    # una posicion sin stop_loss_inicial, que es justo lo que tienen las
    # guardadas por versiones antiguas. Se recalcula desde el precio de compra.
    stop_inicial = pos.get("stop_loss_inicial")
    if not stop_inicial:
        stop_inicial = calcular_stop_loss_inicial(
            pos["precio_compra"], pos["acciones"], pos.get("cambio_divisa", False))
        pos["stop_loss_inicial"] = stop_inicial
    cambio_divisa = pos.get("cambio_divisa", False) or moneda != "EUR"

    _com_compra = pos.get("comision_compra", COMISION_COMPRA)
    _coste_real = pos["precio_compra"] * pos["acciones"] + _com_compra
    precio_equilibrio = round((_coste_real + COMISION_VENTA) / pos["acciones"], 4)
    coste_real = _coste_real
    acciones = pos["acciones"]

    # --- Avisos de perdida. Cada nivel se REARMA: si el precio baja, avisa;
    # si se recupera por encima del nivel, el aviso vuelve a quedar armado.
    # Antes era de una sola vez, y en una sesion con altibajos eso significaba
    # perderse la segunda caida. ---
    avisos_disparados = set(pos.get("avisos_perdida_disparados", []))
    niveles_aviso_perdida = [
        (5.0, "[ATENCIÓN]", "No hay nada que hacer todavía: a este nivel el vaivén normal del día ya llega."),
        (6.5, "[OJO CUIDADO]", "Vende si no ves claro que se recupere. La venta salta en el -8%."),
    ]
    for pct, etiqueta, _texto in niveles_aviso_perdida:
        umbral = calcular_stop_loss_inicial(pos["precio_compra"], pos["acciones"], cambio_divisa, pct, _com_compra)
        if precio_actual <= umbral:
            if pct not in avisos_disparados:
                avisos_disparados.add(pct)
                # Tres lineas y ya. Cuanto mas corto, mas rapido se lee en una
                # notificacion del movil, y aqui no hace falta nada mas.
                # Se da el precio del NIVEL y la perdida EN ese nivel, no los
                # del momento en que se detecto. El aviso puede leerse mucho
                # despues, y entonces un "precio ahora" engaña mas que ayuda;
                # el nivel, en cambio, sigue siendo el mismo mañana.
                perdida_nivel = round(umbral * pos["acciones"] - COMISION_VENTA - coste_real, 2)
                notificar(
                    f"{etiqueta} {pos['ticker']} · -{pct}%",
                    f"Precio: {umbral}€\n"
                    f"Pérdida: {abs(perdida_nivel)}€",
                    urgente=False,
                )
        elif pct in avisos_disparados:
            # Se ha recuperado por encima del nivel: el aviso queda rearmado
            avisos_disparados.discard(pct)
    pos["avisos_perdida_disparados"] = sorted(avisos_disparados)

    # Precios de referencia, calculados aqui porque los usan tanto los avisos
    # de ganancia como los suelos.

    # --- Avisos de GANANCIA (v12). Evitan tener que poner alertas de precio
    # a mano en Trade Republic. Cada uno salta una sola vez. ---
    ganancias_disparadas = set(pos.get("avisos_ganancia_disparados", []))

    # --- DOS avisos separados alrededor del equilibrio (v21) ---
    #
    #   equilibrio          20,25   "has llegado al equilibrio"
    #   equilibrio + 2%     20,655  "comienzan las ganancias, mueve el stop"
    #   equilibrio - 2%     19,845  rearma los dos de arriba
    #
    # El 2% se aclaro el 25/08: en el papel ponia "0'02%" y estuvo programado
    # como 0,02% (medio centimo sobre 20,25), pero al hacer la cuenta a mano
    # -20,25 + 20,25 x 0,02- salia 20,655, o sea el 2%. Cien veces mas.
    #
    # Se rearman al bajar del nivel inferior, asi que una sesion con altibajos
    # los va disparando tantas veces como haga falta.
    margen = cargar_margen_cruce() / 100
    nivel_ganancias = round(precio_equilibrio * (1 + margen), 4)
    nivel_rearme = round(precio_equilibrio * (1 - margen), 4)
    cruzados = set(pos.get("cruces_equilibrio", []))

    if "equilibrio" not in cruzados and precio_actual >= precio_equilibrio:
        cruzados.add("equilibrio")
        notificar(
            f"[PUNTO DE EQUILIBRIO CONSEGUIDO] {pos['ticker']}",
            f"Punto de equilibrio conseguido en {precio_equilibrio}€, a partir de aquí "
            f"serán ganancias reales.",
            urgente=False,
        )

    # Precio al que, si salta el stop, quedaria 1 EUR limpio. Se redondea
    # hacia ARRIBA para que sea 1 EUR o algo mas, nunca menos.
    precio_stop_1eur = math.ceil((coste_real + COMISION_VENTA + 1.0) / acciones * 100) / 100

    if "ganancias" not in cruzados and precio_actual >= nivel_ganancias:
        cruzados.add("ganancias")
        neto = round(precio_actual * acciones - COMISION_VENTA - coste_real, 2)
        notificar(
            f"[COMIENZAN GANANCIAS] {pos['ticker']}",
            f"Empiezan las ganancias en: {nivel_ganancias}€\n"
            f"Pon el stop-loss en {precio_stop_1eur}€ y ganas al menos 1€ pase lo que pase.",
            urgente=False,
        )

    if cruzados and precio_actual <= nivel_rearme:
        if "equilibrio" in cruzados:
            neto = round(precio_actual * acciones - COMISION_VENTA - coste_real, 2)
            notificar(
                f"[PUNTO DE EQUILIBRIO PERDIDO] {pos['ticker']}",
                f"Perdido por debajo de: {nivel_rearme}€\n"
                f"Punto de equilibrio: {precio_equilibrio}€",
                urgente=False,
            )
        cruzados.clear()

    pos["cruces_equilibrio"] = sorted(cruzados)

    # --- Escalera de ganancias: 7%, 10%, 12,5%, 15%, 20%, 25%, 30%.
    # Cada uno avisa una sola vez; no se rearman, porque una vez alcanzado un
    # nivel de ganancia lo que interesa es el siguiente, no volver a oir el
    # mismo. Los porcentajes son sobre lo invertido, comisiones incluidas. ---
    for pct_gan in NIVELES_GANANCIA:
        clave = f"g{pct_gan}"
        if clave in ganancias_disparadas:
            continue
        precio_nivel = round((coste_real * (1 + pct_gan / 100) + COMISION_VENTA) / acciones, 4)
        if precio_actual >= precio_nivel:
            ganancias_disparadas.add(clave)
            # La ganancia se calcula EN EL NIVEL, no al precio del momento: el
            # aviso puede leerse horas despues y entonces "lo que llevas ahora"
            # ya no es cierto, mientras que "en este nivel se ganan X" lo sigue
            # siendo siempre.
            neto = round(precio_nivel * acciones - COMISION_VENTA - coste_real, 2)
            # El stop sugerido asegura 3,5 puntos menos que el nivel
            # alcanzado: al llegar al 7% se asegura el 3,5%, al 10% el 6,5%,
            # y asi. Eran 2 puntos y Jose Manuel prefirio dar mas juego, con
            # buen criterio: las acciones suben y bajan todo el dia, y un stop
            # demasiado pegado salta por puro vaiven y te saca de una posicion
            # que iba bien. Con 3,5 puntos sigues asegurando ganancias y
            # aguantas un retroceso normal.
            pct_asegurado = max(pct_gan - 3.5, 0)
            precio_stop = math.ceil(
                (coste_real * (1 + pct_asegurado / 100) + COMISION_VENTA) / acciones * 100) / 100
            notificar(
                f"[GANANCIAS {pct_gan}%] {pos['ticker']}",
                f"Precio: {precio_nivel}€\n"
                f"Llevas ganados {neto}€\n"
                f"Cambia el stop-loss a {precio_stop}€ (te asegura un {pct_asegurado}%)",
                urgente=False,
            )
    pos["avisos_ganancia_disparados"] = sorted(ganancias_disparadas)

    # --- EL STOP-LOSS ES FIJO EN EL -8% (v22) ---
    #
    # Aqui vivian dos sistemas que movian el stop solos: un trailing continuo
    # al 8% por debajo del maximo, y unos escalones que lo subian cada +5% de
    # beneficio. Los dos disparaban [VENDE] y [SUBE STOP-LOSS] por su cuenta.
    #
    # Fuera. Jose Manuel nunca los pidio: son restos de las primeras versiones,
    # de antes de decidir que el bot AVISA y el decide. El problema practico
    # era que [VENDE] llegaba tambien estando en ganancias, cuando esa etiqueta
    # significa una sola cosa: has tocado el -8% y hay que salir.
    #
    # Ahora el stop del bot es el -8% y no se mueve. Cuando toca apretarlo, se
    # lo dicen los avisos de [COMIENZAN GANANCIAS] y [GANANCIAS X%], que le dan
    # el numero para ponerlo a mano en Trade Republic.
    pos["stop_loss_actual"] = stop_inicial


    salto = precio_actual <= pos.get("stop_loss_actual", 0)
    if salto:
        # Se calcula sobre el nivel del stop, no sobre el precio del momento:
        # el aviso puede leerse mas tarde y el numero tiene que seguir siendo
        # cierto. Y se dice "perdido" o "ganado" segun toque, sin llamar
        # "beneficio" a una perdida.
        stop = pos["stop_loss_actual"]
        _com = pos.get("comision_compra", COMISION_COMPRA)
        _coste = pos["precio_compra"] * pos["acciones"] + _com
        resultado = round(stop * pos["acciones"] - COMISION_VENTA - _coste, 2)
        pct = round(resultado / _coste * 100, 1)
        verbo = "hemos perdido" if resultado < 0 else "hemos ganado"
        notificar(
            f"[VENDE] {pos['ticker']}",
            f"Precio {stop}€, {verbo} un {pct}% en esta operación, "
            f"siendo un total de {resultado}€.",
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
