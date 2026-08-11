"""
VERSION: 23 (11/08/2026) - las búsquedas de Google News ya no se fuerzan a
español (hl=es-419&gl=ES) — ahora se busca en español E inglés y se
combinan los resultados, deduplicando entre los dos. El idioma de los
titulares no es una limitación del proyecto: si hay más cobertura en
inglés (Reuters, Bloomberg, WSJ...), ahora también se recoge.

VERSION: 22 (11/08/2026) - sentimiento con detección de negaciones ("no
batieron expectativas" ya no cuenta como positivo, se invierte el signo)
y vocabulario ampliado en español (supera/superó/batió/decepciona) para
que casos reales como este sí se detecten bien.

VERSION: 21 (11/08/2026) - añade eToro a la lista negra de fuentes
(consistencia con fase3_profundizar.py) y peso doble (×2) a prensa
económica de referencia (Reuters, Bloomberg, FT, WSJ, The Economist,
Barron's) en las noticias de Google News.

VERSION: 20 (04/08/2026) - filtra también TradingKey y cualquier titular
con formato de cotización en bruto (2+ barras verticales tipo
"TICKER|Nombre|Precio:X|Variación %:Y"), detectado en REN.AS

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
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from urllib.parse import quote

import numpy as np
import requests
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
    """Compara el precio actual con sus medias de 50 y 200 sesiones.
    Antes exigía el orden encadenado precio > sma50 > sma200 (cruce dorado
    exacto) para "alcista" — eso hacía que casi cualquier caso normal
    cayera en "mixta", incluso con el precio claramente por encima de
    ambas medias. Ahora mira cada media por separado: alcista = por
    encima de las dos, bajista = por debajo de las dos, mixta = solo
    cuando de verdad está entre medias (señal mixta real, no un cruce
    ligeramente desordenado)."""
    try:
        if len(hist) < 50:
            return None, None, None
        sma50 = round(hist["Close"].rolling(50).mean().iloc[-1], 2)
        sma200 = round(hist["Close"].rolling(200).mean().iloc[-1], 2) if len(hist) >= 200 else None

        if sma200 is not None:
            if precio_actual > sma50 and precio_actual > sma200:
                tendencia = "alcista"
            elif precio_actual < sma50 and precio_actual < sma200:
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


MUESTRA_MINIMA_ANALISTAS = 5  # por debajo de esto, la tabla de reparto de
# Yahoo suele estar incompleta (aunque el consenso agregado sí tenga más
# analistas reales detrás) — no fiable para excluir ni dar empujón


MAX_NOTICIAS_POR_TICKER = 5
MAX_NOTICIAS_GOOGLE = 5
CABECERAS_NOTICIAS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}

PALABRAS_POSITIVAS = [
    "upgrade", "beat", "record", "growth", "contract", "surge", "soar",
    "raises", "buy rating", "strong", "profit", "expand", "win", "partnership",
    # español, porque Google News en español devuelve titulares en español
    "mejora", "sube", "récord", "crecimiento", "contrato", "dispara", "eleva",
    "recomendación de compra", "fuerte", "beneficio", "expande", "gana", "acuerdo",
    "supera", "superó", "superaron", "bate el", "batió", "batieron",
]
PALABRAS_NEGATIVAS = [
    "downgrade", "miss", "loss", "lawsuit", "investigation", "recall",
    "cuts", "sell rating", "weak", "delay", "dilution", "bankruptcy", "fraud",
    # español
    "rebaja", "cae", "pérdida", "demanda judicial", "investigación", "retirada",
    "recorta", "recomendación de venta", "débil", "retraso", "dilución", "quiebra", "fraude",
    "decepciona", "decepcionan", "no logra", "no logró", "no alcanza",
]


NEGACIONES = (
    " no ", " not ", " sin ", " nunca ", " tampoco ", " ni ", " apenas ",
    "didn't ", "doesn't ", "won't ", "isn't ", "aren't ", "n't ",
)
VENTANA_NEGACION = 18  # caracteres a mirar hacia atrás desde la palabra clave


def _hay_negacion_antes(texto, posicion):
    contexto = texto[max(0, posicion - VENTANA_NEGACION):posicion]
    return any(neg in contexto for neg in NEGACIONES)


def sentimiento_titular(titular):
    """Cuenta palabras clave, pero mirando si hay una negación justo antes
    (ej. "no batieron expectativas") — si la hay, se invierte el signo en
    vez de contar la palabra tal cual."""
    t = f" {titular.lower()} "
    puntos = 0
    for palabra in PALABRAS_POSITIVAS:
        inicio = 0
        while True:
            idx = t.find(palabra, inicio)
            if idx == -1:
                break
            puntos += -1 if _hay_negacion_antes(t, idx) else 1
            inicio = idx + len(palabra)
    for palabra in PALABRAS_NEGATIVAS:
        inicio = 0
        while True:
            idx = t.find(palabra, inicio)
            if idx == -1:
                break
            puntos += 1 if _hay_negacion_antes(t, idx) else -1
            inicio = idx + len(palabra)
    return puntos


FUENTES_NO_NOTICIA = {
    "tradingview", "simply wall st", "stockanalysis", "stockanalysis.org",
    "marketbeat", "gurufocus", "insider monkey", "barchart", "investing.com markets",
    "tradingkey", "etoro",
}

FUENTES_PREMIUM = {
    "reuters", "bloomberg", "financial times", "the wall street journal",
    "wsj", "bloomberg businessweek", "the economist", "barron's", "barrons",
}


def peso_fuente(fuente):
    """Da el doble de peso a prensa económica de referencia (Reuters,
    Bloomberg, FT, WSJ...) frente al resto de fuentes de periodismo real."""
    return 2 if any(p in fuente.lower() for p in FUENTES_PREMIUM) else 1


def parece_cotizacion_en_bruto(titulo):
    """Algunas fuentes de datos formatean el titular como una cotización
    en tabla: "TICKER|Nombre|Precio:X|Variación %:Y" — eso no es una
    noticia redactada, es un volcado de datos. Dos o más barras verticales
    es la señal: una noticia real casi nunca lleva ese formato."""
    return titulo.count("|") >= 2


def parece_pagina_de_datos(titulo):
    """Filtro adicional por contenido: algunas páginas de datos (ratios,
    métricas sueltas) se cuelan con fuentes no listadas arriba. Si el
    título es solo una métrica financiera suelta, probablemente no es
    una noticia de verdad."""
    t = titulo.lower()
    metricas_sueltas = ["ebitda", "forward p/e", "price to earnings", "enterprise value"]
    return any(m in t for m in metricas_sueltas)


def buscar_google_news(consulta, maximo=MAX_NOTICIAS_GOOGLE, idioma="es"):
    """Busca en el RSS de Google News (gratis, sin clave). idioma: 'es'
    (España) o 'en' (internacional/inglés) — se llama a esta función con
    los dos por separado y se combinan los resultados, para no perder
    cobertura de prensa en inglés (Reuters, Bloomberg, WSJ...) solo por
    buscar en español; el idioma de los titulares no es una limitación
    del proyecto, se traen tal cual vengan. Filtra fuentes que son
    páginas de datos financieros (TradingView, Simply Wall St...) en vez
    de prensa real, porque Google News las indexa igual que noticias y se
    colaban mezcladas con titulares de verdad. Si falla (sin conexión,
    cambio de formato, etc.) devuelve vacío, sin romper el resto."""
    hl, gl, ceid = ("en-US", "US", "US:en") if idioma == "en" else ("es-419", "ES", "ES:es")
    try:
        url = f"https://news.google.com/rss/search?q={quote(consulta)}&hl={hl}&gl={gl}&ceid={ceid}"
        resp = requests.get(url, headers=CABECERAS_NOTICIAS, timeout=10)
        resp.raise_for_status()
        raiz = ET.fromstring(resp.content)
        items = raiz.findall(".//item")[: maximo * 2]  # pedimos de más, porque filtramos después
        resultado = []
        for item in items:
            titulo = (item.findtext("title") or "").strip()
            fuente = (item.findtext("source") or "").strip()
            if not titulo:
                continue
            if fuente.lower() in FUENTES_NO_NOTICIA:
                continue
            if parece_pagina_de_datos(titulo):
                continue
            if parece_cotizacion_en_bruto(titulo):
                continue
            resultado.append({"titulo": titulo, "fuente": fuente})
            if len(resultado) >= maximo:
                break
        return resultado
    except Exception:
        return []


def analizar_noticias(ticker_obj, ticker, nombre):
    """Combina noticias de Yahoo Finance y Google News, con sentimiento por
    palabras clave. Devuelve el total y hasta 3 titulares (los que más pesan,
    para no inflar el tamaño del archivo con 150+ candidatas)."""
    try:
        titulares = []
        sentimiento_total = 0

        try:
            noticias_yahoo = ticker_obj.news[:MAX_NOTICIAS_POR_TICKER]
        except Exception:
            noticias_yahoo = []
        for n in noticias_yahoo:
            titulo = n.get("title", "")
            if not titulo:
                continue
            puntos = sentimiento_titular(titulo)
            sentimiento_total += puntos
            titulares.append({"titulo": titulo, "fuente": "Yahoo Finance", "sentimiento": puntos})

        vistos_google = set()
        for idioma in ("es", "en"):
            for n in buscar_google_news(nombre or ticker, idioma=idioma):
                clave = n["titulo"].strip().lower()
                if clave in vistos_google:
                    continue  # mismo artículo devuelto por las dos búsquedas de idioma
                vistos_google.add(clave)
                puntos = sentimiento_titular(n["titulo"]) * peso_fuente(n["fuente"] or "")
                sentimiento_total += puntos
                titulares.append({"titulo": n["titulo"], "fuente": n["fuente"] or "Google News", "sentimiento": puntos})

        titulares.sort(key=lambda t: abs(t["sentimiento"]), reverse=True)
        return {"sentimiento_total": sentimiento_total, "titulares": titulares[:3]}
    except Exception:
        return {"sentimiento_total": 0, "titulares": []}


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
        if total < MUESTRA_MINIMA_ANALISTAS:
            return {"excluida": False, "empujon": 0, "muestra_insuficiente": True, "total_analistas": total}

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

        nombre_empresa_valor = info.get("longName") or info.get("shortName")
        noticias = analizar_noticias(t, ticker, nombre_empresa_valor)
        empujon_noticias = max(-10, min(10, noticias["sentimiento_total"] * 2))  # tope para que no domine el resto
        score += empujon_noticias

        return {
            "ticker": ticker,
            "descartado": False,
            "nombre_empresa": nombre_empresa_valor,
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
            "noticias": noticias,
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


def convertir_tipos_numpy(obj):
    """Red de seguridad GENÉRICA: pandas/yfinance a veces devuelven números
    en formato numpy (int64, float64, bool_...) en vez de tipos nativos de
    Python, y json.dump no sabe convertirlos por sí solo. En vez de cazar
    cada campo nuevo uno a uno cada vez que aparece, esto los convierte
    automáticamente a su equivalente nativo de Python, sea cual sea el
    campo donde se cuele."""
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    if isinstance(obj, np.bool_):
        return bool(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


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
        json.dump(salida, f, indent=2, ensure_ascii=False, allow_nan=False, default=convertir_tipos_numpy)

    print(f"Ranking generado: {len(validos)} candidatas válidas, {len(descartados)} descartadas.")


if __name__ == "__main__":
    ejecutar()
