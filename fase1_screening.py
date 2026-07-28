"""
FASE 1 - SCREENING CUANTITATIVO
==========================================
Recorre en lotes el universo de tickers de los índices principales
(S&P500, DAX, FTSE100, CAC40, IBEX35, Nikkei225, EuroStoxx50) buscando:
  - Consenso de analistas de compra (buy / strong_buy)
  - Beta alto (movimiento fuerte, criterio agresivo de Jose Manuel)

Guarda progreso entre ejecuciones (por si el universo es grande y se
corta en varios "Run workflow"), y acumula los candidatos fuertes en
candidatos_fase1.json, que luego consume fase2_scoring.py.

Solo se ejecuta bajo demanda (workflow_dispatch), nunca en cron.
"""

import json
import os
import time

import yfinance as yf

UNIVERSO_FILE = "universo_tickers.json"
PROGRESO_FILE = "progreso.json"
CANDIDATOS_FILE = "candidatos_fase1.json"

LOTE_TAMANO = 300
PAUSA_ENTRE_PETICIONES = 1.0
BETA_MINIMA = 1.5  # movimiento fuerte, coherente con el perfil agresivo


def cargar_universo():
    if os.path.exists(UNIVERSO_FILE):
        with open(UNIVERSO_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    # Semilla mínima de partida si aún no existe el universo completo.
    # Se puede ampliar con listas reales de S&P500/DAX/FTSE100/CAC40/IBEX35/Nikkei225/EuroStoxx50.
    return ["OUST", "RDW", "BKSY", "IONQ", "QUBT", "RKLB", "GRF", "ASTS", "PL", "BBAI", "SOUN"]


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
    universo = cargar_universo()
    total = len(universo)
    posicion = cargar_progreso()
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
        nueva_posicion = 0  # reinicia el ciclo para tener datos siempre frescos

    guardar_progreso(nueva_posicion)

    with open(CANDIDATOS_FILE, "w", encoding="utf-8") as f:
        json.dump(candidatos, f, indent=2, ensure_ascii=False)

    print(f"Candidatos fuertes acumulados: {len(candidatos)}")


if __name__ == "__main__":
    ejecutar()
