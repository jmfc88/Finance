"""
VERSION: 8 (28/07/2026) - verificación real de las páginas de Wikipedia
añadidas en la v7: corregidas las columnas de TSX60 (Symbol, no Ticker) y
OMXC25 (Ticker symbol); añadida conversión de espacio a guión en tickers
(ej. "MAERSK A" -> "MAERSK-A") para que Yahoo Finance los reconozca.
ASX200, IPC (México) e Ibovespa (Brasil) se mantienen porque no hacen daño
si fallan, pero sus páginas de Wikipedia no parecen tener tabla de tickers
limpia — probablemente no aporten candidatas hasta que se revisen mejor.

FASE 1 - SCREENING CUANTITATIVO
==========================================
Recorre TODO el universo de tickers de los índices principales
(S&P500, DAX, FTSE100, CAC40, IBEX35, Nikkei225, EuroStoxx50, AEX, BEL20,
PSI20, FTSE MIB, DJIA, MDAX, SDAX, TecDAX, SMI, ATX, NASDAQ-100) en una
sola pasada, buscando:
  - Consenso de analistas de compra (buy / strong_buy)
  - Beta alto (movimiento fuerte, criterio agresivo de Jose Manuel)

El universo se reconstruye en cada ejecución leyendo los componentes
actuales de cada índice desde Wikipedia (tablas mantenidas por la
comunidad, se actualizan solas cuando cambia un índice). Así la lista
no se queda vieja en 6 meses o un año.

Si Wikipedia falla para un índice concreto ese día (cambio de formato,
caída temporal...), se mantiene el último listado bueno conocido de ese
índice guardado en universo_por_indice.json, en vez de romper todo el
proceso.

Cada ejecución empieza la lista de candidatos DESDE CERO (no acumula
entre ejecuciones), para que siempre refleje el estado actual del
mercado y no arrastre para siempre nombres que dejaron de cumplir el
criterio.

Solo se ejecuta bajo demanda (workflow_dispatch), nunca en cron.
"""

import json
import io
import os
import re
import time

import pandas as pd
import requests
import yfinance as yf

UNIVERSO_FILE = "universo_tickers.json"
CACHE_INDICES_FILE = "universo_por_indice.json"
CANDIDATOS_FILE = "candidatos_fase1.json"

PAUSA_ENTRE_PETICIONES = 0.3
BETA_MINIMA = 1.5  # movimiento fuerte, coherente con el perfil agresivo

# Fuente: tablas de Wikipedia mantenidas por la comunidad para cada índice.
# "columnas" prueba varios nombres posibles porque no todas las páginas
# usan el mismo encabezado. "sufijo" es el que necesita yfinance para
# identificar la bolsa correcta (Madrid, Fráncfort, Londres, París,
# Ámsterdam, Bruselas, Lisboa, Milán, Zúrich, Viena, Tokio, Toronto,
# Estocolmo, Copenhague, Helsinki, Sídney, Ciudad de México, São Paulo...).
# Esta lista está ajustada al filtro real de índices y países que ofrece
# la app de Trade Republic (capturas de pantalla del usuario, 28/07/2026).
INDICES = {
    "SP500":       {"url": "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies", "columnas": ["Symbol"], "sufijo": ""},
    "NASDAQ100":   {"url": "https://en.wikipedia.org/wiki/Nasdaq-100", "columnas": ["Ticker"], "sufijo": ""},
    "DJIA":        {"url": "https://en.wikipedia.org/wiki/Dow_Jones_Industrial_Average", "columnas": ["Symbol"], "sufijo": ""},
    "TSX60":       {"url": "https://en.wikipedia.org/wiki/S%26P/TSX_60", "columnas": ["Symbol"], "sufijo": ".TO"},
    "IBEX35":      {"url": "https://en.wikipedia.org/wiki/IBEX_35", "columnas": ["Ticker", "Símbolo"], "sufijo": ".MC"},
    "DAX":         {"url": "https://en.wikipedia.org/wiki/DAX", "columnas": ["Ticker symbol", "Ticker"], "sufijo": ""},
    "MDAX":        {"url": "https://en.wikipedia.org/wiki/MDAX", "columnas": ["Ticker symbol", "Ticker"], "sufijo": ""},
    "SDAX":        {"url": "https://en.wikipedia.org/wiki/SDAX", "columnas": ["Ticker symbol", "Ticker"], "sufijo": ""},
    "TECDAX":      {"url": "https://en.wikipedia.org/wiki/TecDAX", "columnas": ["Ticker symbol", "Ticker"], "sufijo": ""},
    "FTSE100":     {"url": "https://en.wikipedia.org/wiki/FTSE_100_Index", "columnas": ["Ticker"], "sufijo": ".L"},
    "CAC40":       {"url": "https://en.wikipedia.org/wiki/CAC_40", "columnas": ["Ticker"], "sufijo": ".PA"},
    "AEX":         {"url": "https://en.wikipedia.org/wiki/AEX_index", "columnas": ["Ticker"], "sufijo": ".AS"},
    "BEL20":       {"url": "https://en.wikipedia.org/wiki/BEL_20", "columnas": ["Ticker"], "sufijo": ".BR"},
    "PSI20":       {"url": "https://en.wikipedia.org/wiki/PSI-20", "columnas": ["Ticker"], "sufijo": ".LS"},
    "FTSEMIB":     {"url": "https://en.wikipedia.org/wiki/FTSE_MIB", "columnas": ["Ticker"], "sufijo": ".MI"},
    "SMI":         {"url": "https://en.wikipedia.org/wiki/Swiss_Market_Index", "columnas": ["Ticker"], "sufijo": ".SW"},
    "ATX":         {"url": "https://en.wikipedia.org/wiki/ATX_(stock_market_index)", "columnas": ["Ticker", "Symbol"], "sufijo": ".VI"},
    "OMXS30":      {"url": "https://en.wikipedia.org/wiki/OMX_Stockholm_30", "columnas": ["Ticker", "Symbol"], "sufijo": ".ST"},
    "OMXC25":      {"url": "https://en.wikipedia.org/wiki/OMX_Copenhagen_25", "columnas": ["Ticker symbol", "Ticker"], "sufijo": ".CO"},
    "OMXH25":      {"url": "https://en.wikipedia.org/wiki/OMX_Helsinki_25", "columnas": ["Ticker", "Symbol"], "sufijo": ".HE"},
    "ASX200":      {"url": "https://en.wikipedia.org/wiki/S%26P/ASX_200", "columnas": ["Code", "Ticker"], "sufijo": ".AX"},
    "IPC_MEXICO":  {"url": "https://en.wikipedia.org/wiki/S%26P/BMV_IPC", "columnas": ["Ticker", "Symbol"], "sufijo": ".MX"},
    "IBOVESPA":    {"url": "https://en.wikipedia.org/wiki/Ibovespa", "columnas": ["Ticker", "Código", "Code"], "sufijo": ".SA"},
    "NIKKEI225":   {"url": "https://en.wikipedia.org/wiki/Nikkei_225", "columnas": ["Code", "Ticker"], "sufijo": ".T"},
    "EUROSTOXX50": {"url": "https://en.wikipedia.org/wiki/EURO_STOXX_50", "columnas": ["Ticker"], "sufijo": ""},
}


def limpiar_ticker(valor, sufijo):
    t = str(valor).strip()
    t = re.sub(r"\[.*?\]", "", t)  # quita notas al pie tipo [1]
    if not t or t.lower() == "nan":
        return None
    t = t.replace(" ", "-")  # ej: "MAERSK A" -> "MAERSK-A" (formato que espera Yahoo Finance)
    if sufijo and not t.endswith(sufijo):
        t = t + sufijo
    return t


CABECERAS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}


def obtener_indice(nombre, cfg):
    resp = requests.get(cfg["url"], headers=CABECERAS, timeout=20)
    resp.raise_for_status()
    tablas = pd.read_html(io.StringIO(resp.text))
    for tabla in tablas:
        for col in cfg["columnas"]:
            if col in tabla.columns:
                tickers = [limpiar_ticker(v, cfg["sufijo"]) for v in tabla[col].tolist()]
                tickers = [t for t in tickers if t]
                if tickers:
                    return tickers
    raise ValueError(f"No se encontró una columna de ticker reconocible para {nombre}")


def construir_universo():
    """Reconstruye el universo desde Wikipedia. Si un índice falla, conserva
    su último listado bueno conocido en vez de dejar el universo vacío."""
    cache = {}
    if os.path.exists(CACHE_INDICES_FILE):
        with open(CACHE_INDICES_FILE, "r", encoding="utf-8") as f:
            cache = json.load(f)

    for nombre, cfg in INDICES.items():
        try:
            cache[nombre] = obtener_indice(nombre, cfg)
            print(f"{nombre}: {len(cache[nombre])} tickers actualizados desde Wikipedia")
        except Exception as e:
            conocidos = len(cache.get(nombre, []))
            print(f"{nombre}: no se pudo actualizar ({e}); se mantiene el último conocido ({conocidos} tickers)")

    with open(CACHE_INDICES_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, indent=2, ensure_ascii=False)

    universo = sorted(set(t for lista in cache.values() for t in lista))
    if not universo:
        # último recurso, solo si Wikipedia falla del todo Y no hay caché previa
        universo = ["OUST", "RDW", "BKSY", "IONQ", "QUBT", "RKLB", "GRF", "ASTS", "PL", "BBAI", "SOUN"]

    with open(UNIVERSO_FILE, "w", encoding="utf-8") as f:
        json.dump(universo, f, indent=2, ensure_ascii=False)

    return universo


def evaluar_ticker(ticker):
    try:
        info = yf.Ticker(ticker).info
        recomendacion = (info.get("recommendationKey") or "").lower()
        beta = info.get("beta") or 0
        candidato_fuerte = recomendacion in ("buy", "strong_buy") and beta >= BETA_MINIMA
        return {
            "candidato_fuerte": candidato_fuerte,
            "recomendacion": recomendacion,
            "beta": beta,
            "precio": info.get("currentPrice") or info.get("regularMarketPrice"),
        }
    except Exception:
        return None


def ejecutar():
    universo = construir_universo()
    total = len(universo)
    print(f"Universo total a analizar: {total} tickers")

    candidatos = {}  # se empieza de cero cada vez, no se arrastran ejecuciones anteriores

    for i, ticker in enumerate(universo, start=1):
        resultado = evaluar_ticker(ticker)
        if resultado and resultado["candidato_fuerte"]:
            candidatos[ticker] = resultado
        if i % 50 == 0:
            print(f"  procesados {i}/{total}...")
        time.sleep(PAUSA_ENTRE_PETICIONES)

    with open(CANDIDATOS_FILE, "w", encoding="utf-8") as f:
        json.dump(candidatos, f, indent=2, ensure_ascii=False)

    print(f"Candidatos fuertes encontrados esta pasada: {len(candidatos)}")


if __name__ == "__main__":
    ejecutar()
