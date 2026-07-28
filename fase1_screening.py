"""
FASE 1 - SCREENING CUANTITATIVO
==========================================
Recorre en lotes el universo de tickers de los índices principales
(S&P500, IBEX35, DAX, FTSE100, CAC40, EuroStoxx50) buscando:
  - Consenso de analistas de compra (buy / strong_buy)
  - Beta alto (movimiento fuerte, criterio agresivo de Jose Manuel)

El universo YA NO es una lista fija: se reconstruye en cada ejecución
leyendo los componentes actuales de cada índice desde Wikipedia (tablas
mantenidas por la comunidad, se actualizan solas cuando cambia un índice).
Así la lista no se queda vieja en 6 meses o un año.

Si Wikipedia falla para un índice concreto ese día (cambio de formato,
caída temporal...), se mantiene el último listado bueno conocido de ese
índice guardado en universo_por_indice.json, en vez de romper todo el
proceso.

Guarda progreso entre ejecuciones (por si el universo es grande y se
corta en varios "Run workflow"), y acumula los candidatos fuertes en
candidatos_fase1.json, que luego consume fase2_scoring.py.

Solo se ejecuta bajo demanda (workflow_dispatch), nunca en cron.
"""

import json
import os
import re
import time

import pandas as pd
import yfinance as yf

UNIVERSO_FILE = "universo_tickers.json"
CACHE_INDICES_FILE = "universo_por_indice.json"
PROGRESO_FILE = "progreso.json"
CANDIDATOS_FILE = "candidatos_fase1.json"

LOTE_TAMANO = 300
PAUSA_ENTRE_PETICIONES = 1.0
BETA_MINIMA = 1.5  # movimiento fuerte, coherente con el perfil agresivo

# Fuente: tablas de Wikipedia mantenidas por la comunidad para cada índice.
# "columnas" prueba varios nombres posibles porque no todas las páginas
# usan el mismo encabezado. "sufijo" es el que necesita yfinance para
# identificar la bolsa correcta (Madrid, Fráncfort, Londres, París...).
INDICES = {
    "SP500":       {"url": "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies", "columnas": ["Symbol"], "sufijo": ""},
    "IBEX35":      {"url": "https://en.wikipedia.org/wiki/IBEX_35", "columnas": ["Ticker", "Símbolo"], "sufijo": ".MC"},
    "DAX":         {"url": "https://en.wikipedia.org/wiki/DAX", "columnas": ["Ticker symbol", "Ticker"], "sufijo": ""},
    "FTSE100":     {"url": "https://en.wikipedia.org/wiki/FTSE_100_Index", "columnas": ["Ticker"], "sufijo": ".L"},
    "CAC40":       {"url": "https://en.wikipedia.org/wiki/CAC_40", "columnas": ["Ticker"], "sufijo": ".PA"},
    "EUROSTOXX50": {"url": "https://en.wikipedia.org/wiki/EURO_STOXX_50", "columnas": ["Ticker"], "sufijo": ""},
}


def limpiar_ticker(valor, sufijo):
    t = str(valor).strip()
    t = re.sub(r"\[.*?\]", "", t)  # quita notas al pie tipo [1]
    if not t or t.lower() == "nan":
        return None
    if sufijo and not t.endswith(sufijo):
        t = t + sufijo
    return t


def obtener_indice(nombre, cfg):
    tablas = pd.read_html(cfg["url"])
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


def cargar_progreso():
    if os.path.exists(PROGRESO_FILE):
        with open(PROGRESO_FILE, "r", encoding="utf-8") as f:
            return json.load(f).get("posicion", 0)
    return 0


def guardar_progreso(posicion):
    with open(PROGRESO_FILE, "w", encoding="utf-8") as f:
        json.dump({"posicion": posicion}, f)


def cargar_candidatos():
    if os.path.exists(CANDIDATOS_FILE):
        with open(CANDIDATOS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


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
    # Solo se reconstruye el universo completo desde Wikipedia al empezar
    # una vuelta nueva (posición 0), no en cada lote, para no repetir
    # peticiones de más si el universo es grande y se corta en varias tandas.
    posicion = cargar_progreso()
    if posicion == 0 or not os.path.exists(UNIVERSO_FILE):
        universo = construir_universo()
    else:
        with open(UNIVERSO_FILE, "r", encoding="utf-8") as f:
            universo = json.load(f)

    total = len(universo)
    candidatos = cargar_candidatos()

    lote = universo[posicion: posicion + LOTE_TAMANO]
    print(f"Procesando {len(lote)} tickers ({posicion} a {posicion + len(lote)} de {total})")

    for ticker in lote:
        resultado = evaluar_ticker(ticker)
        if resultado and resultado["candidato_fuerte"]:
            candidatos[ticker] = resultado
        time.sleep(PAUSA_ENTRE_PETICIONES)

    nueva_posicion = posicion + len(lote)
    if nueva_posicion >= total:
        nueva_posicion = 0  # reinicia el ciclo (y reconstruirá el universo de nuevo la próxima vez)

    guardar_progreso(nueva_posicion)

    with open(CANDIDATOS_FILE, "w", encoding="utf-8") as f:
        json.dump(candidatos, f, indent=2, ensure_ascii=False)

    print(f"Candidatos fuertes acumulados: {len(candidatos)}")


if __name__ == "__main__":
    ejecutar()
