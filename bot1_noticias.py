"""
VERSION: 3 (03/08/2026) - AVISO: esta lógica ya está fusionada dentro de
fase2_scoring.py (v18+), donde corre automáticamente para cada candidata
del ranking. Este archivo suelto ya NO hace falta ejecutarlo aparte — se
deja aquí solo por si algún día quieres consultar noticias de un ticker
que no esté en el ranking actual, fuera del flujo normal.

VERSION: 2 (31/07/2026) - añade búsqueda en Google News (RSS gratis, sin
clave) junto a las de Yahoo Finance, para pillar también prensa como
Expansión, Reuters o Bloomberg cuando cubran alguna candidata. Añadidas
listas de palabras en español, porque Google News en español devuelve
titulares en español, no solo en inglés.

BOT 1 - NOTICIAS (sentimiento)
==========================================
Lee candidatos_fase1.json y para cada ticker consulta sus noticias
recientes (vía yfinance + Google News, ambos gratis, sin API de pago),
aplicando un análisis de sentimiento simple por palabras clave. No
sustituye tu criterio, es una capa extra de contexto antes de decidir.

Salida: candidatos_con_noticias.json -> mismo listado + sentimiento y titulares
"""

import json
import time
import xml.etree.ElementTree as ET
from urllib.parse import quote

import requests
import yfinance as yf

ENTRADA = "candidatos_fase1.json"
SALIDA = "candidatos_con_noticias.json"
PAUSA_ENTRE_PETICIONES = 1.0
MAX_NOTICIAS_POR_TICKER = 5
MAX_NOTICIAS_GOOGLE = 5

CABECERAS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}

PALABRAS_POSITIVAS = [
    "upgrade", "beat", "record", "growth", "contract", "surge", "soar",
    "raises", "buy rating", "strong", "profit", "expand", "win", "partnership",
    # español, porque Google News en español devuelve titulares en español
    "mejora", "sube", "récord", "crecimiento", "contrato", "dispara", "eleva",
    "recomendación de compra", "fuerte", "beneficio", "expande", "gana", "acuerdo",
]
PALABRAS_NEGATIVAS = [
    "downgrade", "miss", "loss", "lawsuit", "investigation", "recall",
    "cuts", "sell rating", "weak", "delay", "dilution", "bankruptcy", "fraud",
    # español
    "rebaja", "cae", "pérdida", "demanda judicial", "investigación", "retirada",
    "recorta", "recomendación de venta", "débil", "retraso", "dilución", "quiebra", "fraude",
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


def buscar_google_news(consulta, maximo=MAX_NOTICIAS_GOOGLE):
    """Busca en el RSS de Google News (gratis, sin clave). Devuelve una
    lista de titulares con su fuente (Expansión, Reuters, Bloomberg...).
    Si falla (sin conexión, cambio de formato, etc.) devuelve vacío,
    sin romper el resto del proceso."""
    try:
        url = f"https://news.google.com/rss/search?q={quote(consulta)}&hl=es-419&gl=ES&ceid=ES:es"
        resp = requests.get(url, headers=CABECERAS, timeout=10)
        resp.raise_for_status()
        raiz = ET.fromstring(resp.content)
        items = raiz.findall(".//item")[:maximo]
        resultado = []
        for item in items:
            titulo = (item.findtext("title") or "").strip()
            fuente = (item.findtext("source") or "").strip()
            if titulo:
                resultado.append({"titulo": titulo, "fuente": fuente})
        return resultado
    except Exception:
        return []


def nombre_empresa(ticker):
    """Nombre real de la empresa, para que la búsqueda en Google News no
    dependa del ticker (que a veces no se reconoce bien fuera de EE.UU.)."""
    try:
        info = yf.Ticker(ticker).info
        return info.get("longName") or info.get("shortName") or ticker
    except Exception:
        return ticker


def analizar_ticker(ticker):
    try:
        noticias_yahoo = yf.Ticker(ticker).news[:MAX_NOTICIAS_POR_TICKER]
        titulares = []
        sentimiento_total = 0

        for n in noticias_yahoo:
            titulo = n.get("title", "")
            if not titulo:
                continue
            puntos = sentimiento_titular(titulo)
            sentimiento_total += puntos
            titulares.append({"titulo": titulo, "fuente": "Yahoo Finance", "sentimiento": puntos})

        nombre = nombre_empresa(ticker)
        for n in buscar_google_news(nombre):
            puntos = sentimiento_titular(n["titulo"])
            sentimiento_total += puntos
            titulares.append({"titulo": n["titulo"], "fuente": n["fuente"] or "Google News", "sentimiento": puntos})

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
