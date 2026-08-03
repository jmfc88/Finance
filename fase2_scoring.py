"""
VERSION: 15 (03/08/2026) - CORRECCIÓN CRÍTICA: el total de analistas venía
como numpy.int64 (no int nativo de Python) desde pandas, y json.dump no
sabe serializarlo — rompía el guardado entero (exit code 1). Convertido
a int() nativo.

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
PRECIO_MINIMO = 0.05  # excluye solo penny stocks casi a cero, no acciones baratas en general
PAUSA_ENTRE_PETICIONES = 1.5


def traducir(texto):
    if not texto:
        return ""
    try:
        return GoogleTranslator(source="en", target="es").translate(texto[:1000])
    except Exception:
        return texto  # si falla la traducción, mejor mostrar el original en inglés que nada


def recortar_resumen(texto, minimo=180, maximo=420):
    """Construye el resumen acumulando frases completas hasta tener
    contexto real (mínimo de caracteres orientativo, normalmente 2 frases),
    nunca a medias. El máximo es solo un tope de seguridad para el caso
    raro de una frase kilométrica; se prioriza que el resumen tenga
    sentido por sí mismo antes que ajustarse a un número exacto."""
    if not texto:
        return ""

    frases = [f.strip() for f in texto.split(". ") if f.strip()]
    resultado = ""
    for frase in frases:
        resultado = f"{resultado}{frase}. " if resultado else f"{frase}. "
        if len(resultado) >= minimo:
            break

    resultado = resultado.strip()

    if len(resultado) > maximo:
        # caso raro: ni la primera frase cabe en el tope de seguridad
        resultado = resultado[:maximo].rsplit(" ", 1)[0].rstrip(",;:") + "..."

    return resultado


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


def catalizador_resultados_recientes(ticker_obj, hist):
    """Si la empresa publicó resultados en el último día o dos y fueron
    MUY buenos (sorpresa alta sobre lo esperado), lo marcamos como
    catalizador reciente — a propósito SIN exigir que el precio ya haya
    subido: si esperáramos esa confirmación, avisaríamos justo cuando ya
    se ha inflado, que es lo contrario de lo que se busca (entrar antes
    de que suba, no perseguirlo después). El dato de variación de precio
    se incluye solo como información de contexto, no como filtro."""
    try:
        fechas = ticker_obj.get_earnings_dates(limit=8)
        if fechas is None or fechas.empty:
            return None

        ahora = datetime.now(fechas.index.tz) if fechas.index.tz is not None else datetime.now()
        pasadas = fechas[fechas.index <= ahora]
        if pasadas.empty:
            return None

        fecha_resultado = pasadas.index[0]
        dias_desde = (ahora.date() - fecha_resultado.date()).days
        if dias_desde < 0 or dias_desde > 2:
            return None  # o es futuro, o ya ha pasado demasiado tiempo

        sorpresa = pasadas.iloc[0].get("Surprise(%)")
        if sorpresa is None or sorpresa != sorpresa or sorpresa <= 10:
            return None  # sorpresa != sorpresa detecta NaN, que no es lo mismo que None y se colaba

        # Variación de precio SOLO informativa, no descarta ni exige nada
        variacion = None
        posiciones_necesarias = dias_desde + 2
        if hist is not None and len(hist) >= posiciones_necesarias:
            precio_antes = hist["Close"].iloc[-posiciones_necesarias]
            precio_ahora = hist["Close"].iloc[-1]
            if precio_antes and precio_antes > 0:
                variacion = round((precio_ahora - precio_antes) / precio_antes * 100, 1)

        return {
            "dias_desde": dias_desde,
            "sorpresa_pct": limpio(round(float(sorpresa), 1)),
            "variacion_pct": limpio(variacion),
        }
    except Exception:
        return None


def limpio(valor):
    """Convierte NaN o infinito a None. JSON estándar no admite NaN, y si se
    cuela en el archivo, rompe el JSON.parse() del navegador por completo
    (no carga nada, aunque el resto del archivo esté bien)."""
    if valor is None:
        return None
    try:
        if valor != valor:  # NaN nunca es igual a sí mismo, es el truco estándar para detectarlo
            return None
        if valor in (float("inf"), float("-inf")):
            return None
    except TypeError:
        pass
    return valor


def calcular_rsi(cierres, periodo=14):
    """RSI 14: mide si el precio está sobrecomprado (>70) o en zona de rebote (<30)."""
    try:
        delta = cierres.diff()
        ganancia = delta.clip(lower=0)
        perdida = -delta.clip(upper=0)
        media_ganancia = ganancia.rolling(periodo).mean()
        media_perdida = perdida.rolling(periodo).mean()
        rs = media_ganancia / media_perdida
        rsi = 100 - (100 / (1 + rs))
        valor = rsi.iloc[-1]
        return round(valor, 1) if valor == valor else None  # valor == valor descarta NaN
    except Exception:
        return None


def tendencia_tecnica(hist, precio_actual):
    """Compara el precio actual con sus medias de 50 y 200 sesiones."""
    try:
        if len(hist) < 50:
            return None, None, None
        sma50 = round(hist["Close"].rolling(50).mean().iloc[-1], 2)
        sma200 = round(hist["Close"].rolling(200).mean().iloc[-1], 2) if len(hist) >= 200 else None

        if sma200 is not None:
            if precio_actual > sma50 > sma200:
                tendencia = "alcista"
            elif precio_actual < sma50 < sma200:
                tendencia = "bajista"
            else:
                tendencia = "mixta"
        else:
            tendencia = "alcista" if precio_actual > sma50 else "bajista"

        return tendencia, sma50, sma200
    except Exception:
        return None, None, None


def tendencia_analistas(ticker_obj):
    """Compara las recomendaciones de analistas de hoy contra las de hace 3 meses:
    ¿están mejorando, empeorando o estables? No es solo la foto fija de hoy."""
    try:
        rec = ticker_obj.recommendations
        if rec is None or rec.empty:
            return None
        pesos = {"strongBuy": 2, "buy": 1, "hold": 0, "sell": -1, "strongSell": -2}

        def puntuar(fila):
            return sum(fila.get(k, 0) * w for k, w in pesos.items())

        fila_actual = rec[rec["period"] == "0m"]
        fila_hace3m = rec[rec["period"] == "-3m"]
        if fila_actual.empty or fila_hace3m.empty:
            return None

        total_analistas = sum(fila_actual.iloc[0].get(k, 0) for k in pesos)
        if total_analistas == 0:
            return None

        diferencia = puntuar(fila_actual.iloc[0]) - puntuar(fila_hace3m.iloc[0])
        if diferencia > 1:
            return "mejorando"
        elif diferencia < -1:
            return "empeorando"
        else:
            return "estable"
    except Exception:
        return None


def calcular_consenso_real(ticker_obj):
    """Mira el REPARTO real de analistas por categoría (no solo la etiqueta
    media que da Yahoo), en % sobre el total para que funcione igual con
    6 analistas que con 40. Devuelve si hay que excluir la candidata por
    demasiada discrepancia, y cuánto empujón extra merece si no."""
    try:
        rec = ticker_obj.recommendations
        if rec is None or rec.empty:
            return None

        fila_actual = rec[rec["period"] == "0m"]
        if fila_actual.empty:
            return None
        fila = fila_actual.iloc[0]

        strong_buy = fila.get("strongBuy", 0)
        buy = fila.get("buy", 0)
        hold = fila.get("hold", 0)
        sell = fila.get("sell", 0)
        strong_sell = fila.get("strongSell", 0)
        total = int(strong_buy + buy + hold + sell + strong_sell)
        if total == 0:
            return None

        pct_strong_buy = strong_buy / total * 100
        pct_buy_o_mas = (strong_buy + buy) / total * 100
        pct_vender = (sell + strong_sell) / total * 100

        if pct_vender >= 30:
            return {"excluida": True, "pct_vender": limpio(round(pct_vender, 1)), "total_analistas": total}

        if pct_vender >= 20:
            empujon = -15
        elif pct_vender >= 10:
            empujon = -8
        elif pct_strong_buy >= 90:
            empujon = 20
        elif pct_buy_o_mas >= 90:
            empujon = 12
        elif pct_strong_buy >= 75:
            empujon = 8
        else:
            empujon = 0

        return {
            "excluida": False,
            "empujon": empujon,
            "pct_strong_buy": limpio(round(pct_strong_buy, 1)),
            "pct_vender": limpio(round(pct_vender, 1)),
            "total_analistas": total,
        }
    except Exception:
        return None


def calcular_score(info, momentum_30d, dispersion_pct, tendencia_tec=None, tendencia_analistas_valor=None, empujon_consenso_real=0):
    """
    Score de 0 a 100. Pondera:
    - Consenso de analistas (peso bajo, es la señal más ruidosa)
    - Dispersión entre precio objetivo alto/bajo (a MENOS dispersión, más fiable el consenso)
    - Momentum reciente (evita comprar algo que ya se ha desplomado o que está sobrecomprado)
    - Tendencia técnica (SMA50/200) y tendencia de recomendaciones (mes a mes), peso menor:
      son un empujón/freno sobre el resto, no el criterio principal.
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

    # Tendencia técnica: pequeño empujón/freno, no domina el score
    if tendencia_tec == "alcista":
        score += 5
    elif tendencia_tec == "bajista":
        score -= 5

    # Tendencia de recomendaciones mes a mes: igual, empujón/freno menor
    if tendencia_analistas_valor == "mejorando":
        score += 5
    elif tendencia_analistas_valor == "empeorando":
        score -= 5

    # Consenso real por reparto de categorías (no solo la etiqueta media)
    score += empujon_consenso_real

    return round(score, 1)


def obtener_isin(ticker_obj):
    """Busca el ISIN vía yfinance. No siempre está disponible (depende del
    mercado y de si Yahoo Finance lo tiene indexado), por eso puede salir
    null - en ese caso el usuario simplemente no rellena ese campo."""
    try:
        isin = ticker_obj.isin
        if isin and isin != "-":
            return isin
    except Exception:
        pass
    return None


def evaluar(ticker):
    try:
        t = yf.Ticker(ticker)
        info = t.info

        precio = info.get("currentPrice") or info.get("regularMarketPrice")
        if not precio or precio > PRECIO_MAXIMO or precio < PRECIO_MINIMO:
            return None  # fuera de presupuesto para acción entera

        dias_resultados = dias_hasta_resultados(t)
        if dias_resultados is not None and 0 <= dias_resultados <= DIAS_MINIMOS_ANTES_DE_RESULTADOS:
            return {"ticker": ticker, "descartado": True,
                    "motivo": f"Resultados en {dias_resultados} días - evento binario, se evita"}

        consenso_real = calcular_consenso_real(t)
        if consenso_real and consenso_real.get("excluida"):
            return {"ticker": ticker, "descartado": True,
                    "motivo": f"{consenso_real['pct_vender']}% de los analistas recomienda vender - discrepancia real, se evita"}

        hist = t.history(period="220d")  # suficiente para SMA200, RSI y momentum de 30 días
        momentum_30d = None
        if len(hist) > 22:
            momentum_30d = round((hist["Close"].iloc[-1] / hist["Close"].iloc[-22] - 1) * 100, 1)

        rsi_14 = calcular_rsi(hist["Close"]) if len(hist) > 14 else None
        tendencia_tec, sma50, sma200 = tendencia_tecnica(hist, precio)
        tendencia_analistas_valor = tendencia_analistas(t)
        isin = obtener_isin(t)
        catalizador = catalizador_resultados_recientes(t, hist)

        target_alto = info.get("targetHighPrice")
        target_bajo = info.get("targetLowPrice")
        dispersion_pct = None
        if target_alto and target_bajo and target_bajo > 0:
            dispersion_pct = round((target_alto - target_bajo) / target_bajo * 100, 1)

        empujon_consenso_real = consenso_real.get("empujon", 0) if consenso_real else 0
        score = calcular_score(info, momentum_30d, dispersion_pct, tendencia_tec, tendencia_analistas_valor, empujon_consenso_real)
        if catalizador:
            score += 12  # empujón notable pero que no domine el resto del método

        cotiza_en_euros = ticker.endswith((".MC", ".DE", ".PA", ".AS", ".BR", ".LS", ".MI", ".VI", ".HE"))
        if cotiza_en_euros:
            score += 8  # sin cambio de divisa: no pierdes céntimos en la conversión al comprar/vender

        return {
            "ticker": ticker,
            "descartado": False,
            "nombre_empresa": info.get("longName") or info.get("shortName"),
            "isin": isin,
            "precio_actual": limpio(precio),
            "score": limpio(score),
            "consenso": info.get("recommendationKey"),
            "precio_objetivo_medio": limpio(info.get("targetMeanPrice")),
            "dispersion_pct": limpio(dispersion_pct),
            "momentum_30d_pct": limpio(momentum_30d),
            "catalizador_resultados": catalizador,
            "consenso_real": consenso_real,
            "cotiza_en_euros": cotiza_en_euros,
            "rsi_14": limpio(rsi_14),
            "tendencia_tecnica": tendencia_tec,
            "sma50": limpio(sma50),
            "sma200": limpio(sma200),
            "tendencia_analistas": tendencia_analistas_valor,
            "sector": info.get("sector"),
            "resumen_negocio": recortar_resumen(traducir(info.get("longBusinessSummary") or "")),
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
        json.dump(salida, f, indent=2, ensure_ascii=False, allow_nan=False)

    print(f"Ranking generado: {len(validos)} candidatas válidas, {len(descartados)} descartadas.")


if __name__ == "__main__":
    ejecutar()
