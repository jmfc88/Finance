"""
VERSION: 1 (23/08/2026) - diagnostico de FUENTES ALTERNATIVAS.

POR QUE: hoy todo el sistema depende de Yahoo Finance. El 22/08 Yahoo
devolvio precios en blanco para las 107 candidatas europeas y el sistema no
se entero: las etiquetaba "mixta" y competian en el ranking sin datos. Se
arreglo la DETECCION, pero la dependencia sigue siendo total.

QUE PRUEBA ESTE SCRIPT, con tickers reales del universo:
  1. Que cobertura tiene Stooq de las bolsas europeas. Stooq ya se usa como
     respaldo pero SOLO para tickers de EE.UU., porque nunca se comprobo si
     sirve para Madrid, Paris o Milan. Su documentacion menciona Xetra y
     Londres pero no Madrid, asi que hay que verlo.
  2. Que sufijo hay que usar en cada mercado. Yahoo usa .MC .PA .MI .AS;
     Stooq usa otro esquema, y sin el mapeo correcto todo daria vacio
     aunque los datos esten ahi.
  3. Si Stooq y Yahoo COINCIDEN en el precio. Esto es lo mas valioso: dos
     fuentes que coinciden dan confianza, y dos que discrepan un 5% son un
     aviso de que una de las dos esta mal. Hoy no hay forma de saberlo.

QUE NO HACE: no cambia nada del sistema. Solo mide y informa, para decidir
con datos si merece la pena montar la doble fuente y como.

COMO USARLO: subir al repo y lanzar "Diagnostico de fuentes" desde Actions.
"""

import io
import time

import pandas as pd
import requests
import yfinance as yf

# Tickers reales del universo, uno por mercado, con el sufijo de Yahoo y los
# candidatos de sufijo de Stooq que hay que probar.
CASOS = [
    ("SCYR.MC", "Sacyr", "Espana (Madrid)", ["scyr.es", "scyr.mc", "scyr"]),
    ("ITX.MC", "Inditex", "Espana (Madrid)", ["itx.es", "itx.mc", "itx"]),
    ("AI.PA", "Air Liquide", "Francia (Paris)", ["ai.fr", "ai.pa", "ai"]),
    ("LDO.MI", "Leonardo", "Italia (Milan)", ["ldo.it", "ldo.mi", "ldo"]),
    ("ASML.AS", "ASML", "Holanda (Amsterdam)", ["asml.nl", "asml.as", "asml"]),
    ("SAP.DE", "SAP", "Alemania (Xetra)", ["sap.de", "sap"]),
    ("BP.L", "BP", "Reino Unido (Londres)", ["bp.uk", "bp.l", "bp"]),
    ("ANET", "Arista", "EE.UU.", ["anet.us", "anet"]),
]

CABECERAS = {"User-Agent": "Mozilla/5.0 (compatible; jmfc88-Finance/1.0)"}


def precio_yahoo(ticker):
    """Ultimo cierre segun Yahoo, o None."""
    try:
        h = yf.Ticker(ticker).history(period="1mo")
        if h is None or len(h) == 0 or "Close" not in h.columns:
            return None, 0
        cierres = h["Close"].dropna()
        if len(cierres) == 0:
            return None, 0
        return round(float(cierres.iloc[-1]), 4), len(cierres)
    except Exception:
        return None, 0


def precio_stooq(simbolo):
    """Stooq sirve CSV directo, sin clave ni limite documentado. Formato:
    https://stooq.com/q/d/l/?s=SIMBOLO&i=d"""
    url = f"https://stooq.com/q/d/l/?s={simbolo}&i=d"
    try:
        r = requests.get(url, headers=CABECERAS, timeout=20)
        if r.status_code != 200 or len(r.text) < 60:
            return None, 0
        if "No data" in r.text or "Exceeded" in r.text:
            return None, 0
        df = pd.read_csv(io.StringIO(r.text))
        if "Close" not in df.columns or len(df) == 0:
            return None, 0
        return round(float(df["Close"].iloc[-1]), 4), len(df)
    except Exception:
        return None, 0


def ejecutar():
    print("DIAGNOSTICO DE FUENTES ALTERNATIVAS")
    print("=" * 78)
    print()

    resumen = []
    for ticker_yahoo, nombre, mercado, candidatos_stooq in CASOS:
        print(f"### {nombre} ({mercado})")

        py, ny = precio_yahoo(ticker_yahoo)
        print(f"  Yahoo  {ticker_yahoo:12} -> {'%.4f' % py if py else 'SIN DATOS':>12}"
              f"   ({ny} sesiones en el ultimo mes)")
        time.sleep(1.5)

        # Se prueban los sufijos hasta dar con uno que responda
        encontrado = None
        for simbolo in candidatos_stooq:
            ps, ns = precio_stooq(simbolo)
            marca = "OK" if ps else "vacio"
            print(f"  Stooq  {simbolo:12} -> {'%.4f' % ps if ps else 'SIN DATOS':>12}   {marca}")
            time.sleep(1.5)
            if ps and not encontrado:
                encontrado = (simbolo, ps, ns)

        # Lo que de verdad interesa: ¿coinciden?
        if py and encontrado:
            simbolo, ps, ns = encontrado
            dif = abs(ps - py) / py * 100
            if dif <= 1:
                veredicto = f"COINCIDEN (difieren {dif:.2f}%)"
            elif dif <= 5:
                veredicto = f"discrepan {dif:.1f}% - puede ser divisa o desfase de cierre"
            else:
                veredicto = f"DISCREPAN {dif:.1f}% - probablemente NO es el mismo valor"
            print(f"  --> {veredicto}")
            resumen.append((nombre, mercado, simbolo, dif))
        elif py and not encontrado:
            print("  --> Stooq NO tiene este valor con ningun sufijo probado")
            resumen.append((nombre, mercado, None, None))
        elif encontrado and not py:
            print("  --> solo Stooq lo tiene: serviria de respaldo cuando Yahoo falle")
            resumen.append((nombre, mercado, encontrado[0], None))
        else:
            print("  --> ninguna de las dos fuentes lo tiene")
            resumen.append((nombre, mercado, None, None))
        print()

    print("=" * 78)
    print("RESUMEN: mapeo de sufijos que funciona")
    print("=" * 78)
    cubiertos = 0
    for nombre, mercado, simbolo, dif in resumen:
        if simbolo:
            cubiertos += 1
            extra = f", precios difieren {dif:.2f}%" if dif is not None else ""
            print(f"  {mercado:24} -> usar '{simbolo}' en Stooq{extra}")
        else:
            print(f"  {mercado:24} -> SIN COBERTURA en Stooq")

    print()
    print(f"Cobertura de Stooq: {cubiertos} de {len(resumen)} mercados probados.")
    print()
    print("COMO INTERPRETARLO:")
    print("  - Si Stooq cubre los mercados europeos y los precios coinciden, merece")
    print("    la pena montar la doble fuente: Yahoo como principal, Stooq como")
    print("    contraste, y una senal de aviso cuando discrepen mas de un 2%.")
    print("  - Si Stooq solo cubre Alemania, Reino Unido y EE.UU., la doble fuente")
    print("    solo protegeria una parte del universo, y habria que buscar otra")
    print("    fuente para Madrid, Paris, Milan y Amsterdam.")
    print("  - Si los precios discrepan mucho de forma sistematica, cuidado: puede")
    print("    ser que Stooq tenga otra cotizacion del mismo valor en otra bolsa,")
    print("    que es el mismo problema de los ISIN que ya conocemos.")


if __name__ == "__main__":
    ejecutar()
