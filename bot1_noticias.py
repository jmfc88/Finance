"""
VERSION: 1 (28/07/2026) - primera versión

BOT 1 - NOTICIAS (sentimiento)
==========================================
Lee candidatos_fase1.json y para cada ticker consulta sus noticias
recientes (vía yfinance, gratis, sin API de pago), aplicando un
análisis de sentimiento simple por palabras clave. No sustituye tu
criterio, es una capa extra de contexto antes de decidir.

Salida: candidatos_con_noticias.json -> mismo listado + sentimiento y titulares
"""

import json
import time

import yfinance as yf

ENTRADA = "candidatos_fase1.json"
SALIDA = "candidatos_con_noticias.json"
PAUSA_ENTRE_PETICIONES = 1.0
MAX_NOTICIAS_POR_TICKER = 5

PALABRAS_POSITIVAS = [
    "upgrade", "beat", "record", "growth", "contract", "surge", "soar",
    "raises", "buy rating", "strong", "profit", "expand", "win", "partnership",
]
PALABRAS_NEGATIVAS = [
    "downgrade", "miss", "loss", "lawsuit", "investigation", "recall",
    "cuts", "sell rating", "weak", "delay", "dilution", "bankruptcy", "fraud",
]


def sentimiento_titular(titular):
    t = titular.lower()
    puntos = 0
    for palabra in PALABRAS_POSITIVAS:
        if palabra in t:
            puntos += 1
    for palabra in PALABRAS_NEGATIVAS:
        if palabra in t:
            puntos -= 1
    return puntos


def analizar_ticker(ticker):
    try:
        noticias = yf.Ticker(ticker).news[:MAX_NOTICIAS_POR_TICKER]
        titulares = []
        sentimiento_total = 0
        for n in noticias:
            titulo = n.get("title", "")
            if not titulo:
                continue
            puntos = sentimiento_titular(titulo)
            sentimiento_total += puntos
            titulares.append({"titulo": titulo, "sentimiento": puntos})
        return {"sentimiento_total": sentimiento_total, "titulares": titulares}
    except Exception as e:
        return {"sentimiento_total": 0, "titulares": [], "error": str(e)}


def ejecutar():
    with open(ENTRADA, "r", encoding="utf-8") as f:
        candidatos = json.load(f)

    resultado = {}
    for ticker, datos in candidatos.items():
        analisis = analizar_ticker(ticker)
        resultado[ticker] = {**datos, **analisis}
        time.sleep(PAUSA_ENTRE_PETICIONES)

    with open(SALIDA, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)

    print(f"Noticias analizadas para {len(resultado)} candidatas.")


if __name__ == "__main__":
    ejecutar()
