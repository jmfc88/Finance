"""
VERSION: 2 (23/08/2026) - segunda ronda del diagnostico.

QUE DESCUBRIO LA RONDA 1 (ejecutada el 22/08 a las 23:41 UTC):
las tres formas de pedir el historico funcionan con TODAS las europeas,
8 de 8, incluida SCYR.MC. Asi que la forma de pedirlo NO es el problema.
Tambien salio que yf.download() esta roto entero bajo pandas 3.0.5
("The truth value of a Series is ambiguous"), con europeas y americanas
por igual — no usar download() en este proyecto.

LA PISTA QUE QUEDA: el diagnostico pedia el historico sobre un objeto
Ticker RECIEN CREADO. fase2 no hace eso: sobre el MISMO objeto llama
antes a .info, luego a .calendar, luego a .recommendations, y solo
despues a .history(). Hay un fallo conocido de yfinance por el que unas
llamadas envenenan a las siguientes sobre el mismo objeto.

QUE PRUEBA ESTE SCRIPT: exactamente esa hipotesis. Reproduce el orden de
llamadas de fase2 y lo compara con el objeto limpio. Si la hipotesis es
correcta, la prueba B fallara en las europeas y la A funcionara — y
entonces el arreglo es de una linea.

COMO USARLO: subir al repo y lanzar "Diagnostico de datos" desde Actions.
"""

import time

import yfinance as yf

TICKERS_PRUEBA = [
    ("SCYR.MC", "Espana - Sacyr"),
    ("AI.PA", "Francia - Air Liquide"),
    ("LDO.MI", "Italia - Leonardo"),
    ("ASML.AS", "Holanda - ASML"),
    ("ANET", "EEUU - Arista (control, este funciona)"),
    ("^STOXX50E", "Indice EuroStoxx50"),
]


def resumen(hist):
    if hist is None or len(hist) == 0:
        return "VACIO"
    if "Close" not in hist.columns:
        return "SIN COLUMNA Close"
    validos = hist["Close"].notna().sum()
    if validos == 0:
        return f"SOLO NaN ({len(hist)} filas, 0 precios)  <-- EL FALLO"
    return f"OK ({validos} precios)"


def a_limpio(ticker):
    """Objeto nuevo, el historico es lo primero que se le pide."""
    return yf.Ticker(ticker).history(period="220d")


def b_orden_de_fase2(ticker):
    """El orden EXACTO de evaluar() en fase2_scoring.py."""
    t = yf.Ticker(ticker)
    _ = t.info
    try:
        _ = t.calendar
    except Exception:
        pass
    try:
        _ = t.recommendations
    except Exception:
        pass
    return t.history(period="220d")


def c_solo_info_antes(ticker):
    """Para saber cual de las tres llamadas previas es la culpable."""
    t = yf.Ticker(ticker)
    _ = t.info
    return t.history(period="220d")


def d_solo_calendar_antes(ticker):
    t = yf.Ticker(ticker)
    try:
        _ = t.calendar
    except Exception:
        pass
    return t.history(period="220d")


def e_solo_recomendaciones_antes(ticker):
    t = yf.Ticker(ticker)
    try:
        _ = t.recommendations
    except Exception:
        pass
    return t.history(period="220d")


def f_arreglo_objeto_aparte(ticker):
    """EL ARREGLO PROPUESTO: hacer todo lo de fase2 sobre un objeto y pedir
    el historico sobre OTRO objeto nuevo. Si esto funciona donde falla la
    prueba B, el arreglo en fase2 es cambiar una sola linea."""
    t = yf.Ticker(ticker)
    _ = t.info
    try:
        _ = t.calendar
    except Exception:
        pass
    try:
        _ = t.recommendations
    except Exception:
        pass
    return yf.Ticker(ticker).history(period="220d")  # objeto nuevo solo para el historico


PRUEBAS = [
    ("A. objeto limpio (asi lo pedia el diagnostico 1)", a_limpio),
    ("B. orden de fase2: info + calendar + recomendaciones", b_orden_de_fase2),
    ("C. solo .info antes", c_solo_info_antes),
    ("D. solo .calendar antes", d_solo_calendar_antes),
    ("E. solo .recommendations antes", e_solo_recomendaciones_antes),
    ("F. ARREGLO: objeto aparte solo para el historico", f_arreglo_objeto_aparte),
]


def ejecutar():
    print(f"yfinance {yf.__version__}")
    print("=" * 78)
    resultados = {}

    for etiqueta, funcion in PRUEBAS:
        print(f"\n### {etiqueta}")
        resultados[etiqueta] = {}
        for ticker, descripcion in TICKERS_PRUEBA:
            try:
                r = resumen(funcion(ticker))
            except Exception as e:
                r = f"EXCEPCION: {type(e).__name__}: {str(e)[:60]}"
            resultados[etiqueta][ticker] = r
            print(f"  {ticker:12} {descripcion:40} {r}")
            time.sleep(1.5)

    print("\n" + "=" * 78)
    print("RESUMEN (cuantos de los 6 traen precios)")
    print("=" * 78)
    for etiqueta in resultados:
        buenos = sum(1 for v in resultados[etiqueta].values() if v.startswith("OK"))
        print(f"  {buenos}/6   {etiqueta}")

    print("\nCOMO LEERLO:")
    print("  - Si B falla y A funciona -> confirmado: una llamada previa")
    print("    envenena el historico. C, D y E dicen cual de las tres.")
    print("  - Si F funciona -> el arreglo es pedir el historico sobre un")
    print("    objeto Ticker nuevo, y es un cambio de una linea en fase2.")
    print("  - Si B funciona en todas -> la causa no esta aqui, y hay que")
    print("    mirar la carga total de peticiones de una ejecucion entera.")


if __name__ == "__main__":
    ejecutar()
