"""
VERSION: 1 (23/08/2026) - script de diagnostico de un solo uso.

POR QUE EXISTE: el 22/08/2026 se descubrio que en candidatos_rankeados.json
las 107 candidatas europeas (de 141 totales) tenian sma50, sma200, rsi_14,
momentum_30d y momentum_5d todos a null, mientras que las 34 de EEUU,
Australia y Canada los tenian correctos. El reparto era perfecto por mercado:
.PA, .MI, .MC, .AS, .HE, .LS, .BR y .L fallaban TODAS; sin sufijo, .AX y .TO
funcionaban TODAS.

Efecto real: 19 de las 30 tarjetas del cuaderno se estaban puntuando sin
ningun dato de precio, y ademas salian etiquetadas como tendencia "mixta"
en vez de "sin datos", porque las comparaciones contra NaN dan siempre False
y el codigo caia en el else.

Este script NO arregla nada. Solo prueba varias formas de pedir el historico
a Yahoo y dice cual funciona, para arreglar la de verdad con datos y no a
ojo. Se ejecuta una vez desde la pestana Actions y se lee la salida.

COMO USARLO: subir al repo, ir a Actions -> "Diagnostico de datos" ->
Run workflow, y mirar el resumen que sale al terminar.
"""

import time
from datetime import date, timedelta

import pandas as pd
import yfinance as yf

# Una muestra de cada mercado: los que fallan y los que funcionan, para poder
# comparar. Si un metodo arregla los europeos pero rompe los americanos, hay
# que verlo aqui antes de tocar fase2.
TICKERS_PRUEBA = [
    ("SCYR.MC", "Espana - Sacyr (operacion real cerrada)"),
    ("ITX.MC", "Espana - Inditex"),
    ("AI.PA", "Francia - Air Liquide"),
    ("LDO.MI", "Italia - Leonardo"),
    ("ASML.AS", "Holanda - ASML"),
    ("ANET", "EEUU - Arista (ESTE FUNCIONA HOY)"),
    ("^STOXX50E", "Indice EuroStoxx50 (lo necesita el regimen de mercado)"),
    ("^GSPC", "Indice S&P500 (lo necesita el regimen de mercado)"),
]


def resumen(hist):
    """Distingue los tres casos que importan, que NO son lo mismo:
    - vacio: Yahoo no devolvio ninguna fila
    - solo NaN: devolvio filas pero sin precios (el fallo que tenemos ahora,
      y el mas traicionero porque el codigo no se entera)
    - ok: filas con precios de verdad"""
    if hist is None or len(hist) == 0:
        return "VACIO (0 filas)"
    if "Close" not in hist.columns:
        return f"SIN COLUMNA Close ({len(hist)} filas)"
    validos = hist["Close"].notna().sum()
    if validos == 0:
        return f"SOLO NaN ({len(hist)} filas, 0 precios) <-- el fallo actual"
    return f"OK ({len(hist)} filas, {validos} precios, ultimo {round(float(hist['Close'].dropna().iloc[-1]), 2)})"


def metodo_actual(ticker):
    return yf.Ticker(ticker).history(period="220d")


def metodo_periodo_estandar(ticker):
    """'1y' es un periodo de los que Yahoo lista como validos; '220d' es un
    formato libre que yfinance acepta pero que Yahoo puede rechazar segun
    el mercado."""
    return yf.Ticker(ticker).history(period="1y")


def metodo_fechas_explicitas(ticker):
    fin = date.today()
    ini = fin - timedelta(days=400)
    return yf.Ticker(ticker).history(start=ini.isoformat(), end=fin.isoformat())


def metodo_download(ticker):
    return yf.download(ticker, period="1y", progress=False, auto_adjust=True)


def metodo_download_sin_ajustar(ticker):
    return yf.download(ticker, period="1y", progress=False, auto_adjust=False)


METODOS = [
    ("1. history(period='220d')  [el actual]", metodo_actual),
    ("2. history(period='1y')", metodo_periodo_estandar),
    ("3. history(start=, end=)", metodo_fechas_explicitas),
    ("4. download(period='1y')", metodo_download),
    ("5. download(auto_adjust=False)", metodo_download_sin_ajustar),
]


def ejecutar():
    print(f"yfinance instalado: {yf.__version__}")
    print(f"pandas instalado:   {pd.__version__}")
    print("=" * 78)

    tabla = {}
    for etiqueta, funcion in METODOS:
        print(f"\n### {etiqueta}")
        tabla[etiqueta] = {}
        for ticker, descripcion in TICKERS_PRUEBA:
            try:
                r = resumen(funcion(ticker))
            except Exception as e:
                r = f"EXCEPCION: {type(e).__name__}: {str(e)[:70]}"
            tabla[etiqueta][ticker] = r
            print(f"  {ticker:12} {descripcion:52} {r}")
            time.sleep(1.5)  # misma pausa que usa fase2, para no falsear el resultado

    print("\n" + "=" * 78)
    print("RESUMEN: cuantos de los 8 devuelven precios de verdad")
    print("=" * 78)
    for etiqueta in tabla:
        buenos = sum(1 for v in tabla[etiqueta].values() if v.startswith("OK"))
        print(f"  {buenos}/8   {etiqueta}")

    print("\nQUE HACER CON ESTO: el metodo con mas OK es el que hay que poner")
    print("en fase2_scoring.py. Si NINGUNO arregla los europeos, el problema no")
    print("es la forma de llamar sino la fuente, y toca buscar otra distinta")
    print("de Yahoo para Europa.")


if __name__ == "__main__":
    ejecutar()
