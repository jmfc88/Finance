"""
VERSION: 3 (28/07/2026) - corregido bug: faltaba la definición de dias_hasta_resultados

FASE 2 - SCORING Y RANKING DE CANDIDATOS
==========================================
Coge candidatos_fase1.json (salida del screening cuantitativo) y les
aplica un score real, no solo "consenso de compra" (que es ruido en
small-caps temáticas). Descarta las que publican resultados pronto
(riesgo de evento binario) y devuelve un ranking ordenado.

Entrada:  candidatos_fase1.json   -> {"TICKER": {...datos fase1...}, ...}
Salida:   candidatos_rankeados.json -> lista ordenada de mejor a peor
"""

import json
import time
from datetime import datetime, timedelta

import yfinance as yf
from deep_translator import GoogleTranslator

ENTRADA = "candidatos_fase1.json"
SALIDA = "candidatos_rankeados.json"
DIAS_MINIMOS_ANTES_DE_RESULTADOS = 5
PRECIO_MAXIMO = 200  # criterio de Jose Manuel: nada de fracciones, nada por encima de ~200€
PAUSA_ENTRE_PETICIONES = 1.5


def traducir(texto):
    if not texto:
        return ""
    try:
        return GoogleTranslator(source="en", target="es").translate(texto[:1000])
    except Exception:
        return texto  # si falla la traducción, mejor mostrar el original en inglés que nada


def dias_hasta_resultados(ticker_obj):
    """Devuelve None si no hay fecha, o número de días naturales hasta la próxima publicación."""
    try:
        cal = ticker_obj.calendar
        if cal is None or len(cal) == 0:
            return None
        fecha = None
        if isinstance(cal, dict) and "Earnings Date" in cal:
            fecha = cal["Earnings Date"][0]
        elif hasattr(cal, "loc") and "Earnings Date" in cal.index:
            fecha = cal.loc["Earnings Date"].iloc[0]
        if fecha is None:
            return None
        if hasattr(fecha, "to_pydatetime"):
            fecha = fecha.to_pydatetime()
        return (fecha.date() - datetime.now().date()).days
    except Exception:
        return None


def calcular_score(info, momentum_30d, dispersion_pct):
    """
    Score de 0 a 100. Pondera:
    - Consenso de analistas (peso bajo, es la señal más ruidosa)
    - Dispersión entre precio objetivo alto/bajo (a MENOS dispersión, más fiable el consenso)
    - Momentum reciente (evita comprar algo que ya se ha desplomado o que está sobrecomprado)
    """
    score = 0

    recomendacion = (info.get("recommendationKey") or "").lower()
    puntos_consenso = {
        "strong_buy": 15,
        "buy": 10,
        "hold": 3,
        "underperform": -10,
        "sell": -20,
    }
    score += puntos_consenso.get(recomendacion, 0)

    # Menos dispersión = consenso más fiable = más puntos
    if dispersion_pct is not None:
        if dispersion_pct < 30:
            score += 25
        elif dispersion_pct < 60:
            score += 15
        elif dispersion_pct < 100:
            score += 5
        else:
            score += 0  # dispersión enorme = el "consenso" no significa nada

    # Momentum: castiga tanto caídas fuertes recientes como subidas parabólicas ya agotadas
    if momentum_30d is not None:
        if -15 <= momentum_30d <= 25:
            score += 20
        elif momentum_30d > 25:
            score += 5  # ya ha subido mucho, entrar ahora es peor punto de entrada
        else:
            score += 0  # cayendo con fuerza, cuchillo cayendo

    # Potencial de subida hasta precio objetivo medio
    target = info.get("targetMeanPrice")
    precio = info.get("currentPrice") or info.get("regularMarketPrice")
    if target and precio and precio > 0:
        potencial = (target - precio) / precio * 100
        score += min(max(potencial / 4, -10), 25)  # tope +25 para no dejar que un dato exagerado domine

    return round(score, 1)


def evaluar(ticker):
    try:
        t = yf.Ticker(ticker)
        info = t.info

        precio = info.get("currentPrice") or info.get("regularMarketPrice")
        if not precio or precio > PRECIO_MAXIMO:
            return None  # fuera de presupuesto para acción entera

        dias_resultados = dias_hasta_resultados(t)
        if dias_resultados is not None and 0 <= dias_resultados <= DIAS_MINIMOS_ANTES_DE_RESULTADOS:
            return {"ticker": ticker, "descartado": True,
                    "motivo": f"Resultados en {dias_resultados} días - evento binario, se evita"}

        hist = t.history(period="35d")
        momentum_30d = None
        if len(hist) > 5:
            momentum_30d = round((hist["Close"].iloc[-1] / hist["Close"].iloc[0] - 1) * 100, 1)

        target_alto = info.get("targetHighPrice")
        target_bajo = info.get("targetLowPrice")
        dispersion_pct = None
        if target_alto and target_bajo and target_bajo > 0:
            dispersion_pct = round((target_alto - target_bajo) / target_bajo * 100, 1)

        score = calcular_score(info, momentum_30d, dispersion_pct)

        return {
            "ticker": ticker,
            "descartado": False,
            "precio_actual": precio,
            "score": score,
            "consenso": info.get("recommendationKey"),
            "precio_objetivo_medio": info.get("targetMeanPrice"),
            "dispersion_pct": dispersion_pct,
            "momentum_30d_pct": momentum_30d,
            "sector": info.get("sector"),
            "resumen_negocio": traducir(info.get("longBusinessSummary") or "")[:280],
        }
    except Exception as e:
        return {"ticker": ticker, "descartado": True, "motivo": f"Error de datos: {e}"}


def ejecutar():
    with open(ENTRADA, "r", encoding="utf-8") as f:
        candidatos_fase1 = json.load(f)

    resultados = []
    for ticker in candidatos_fase1.keys():
        r = evaluar(ticker)
        if r:
            resultados.append(r)
        time.sleep(PAUSA_ENTRE_PETICIONES)

    validos = [r for r in resultados if not r.get("descartado")]
    validos.sort(key=lambda x: x["score"], reverse=True)

    descartados = [r for r in resultados if r.get("descartado")]

    salida = {
        "generado": datetime.now().isoformat(),
        "ranking": validos,
        "descartados": descartados,
    }

    with open(SALIDA, "w", encoding="utf-8") as f:
        json.dump(salida, f, indent=2, ensure_ascii=False)

    print(f"Ranking generado: {len(validos)} candidatas válidas, {len(descartados)} descartadas.")


if __name__ == "__main__":
    ejecutar()
    
