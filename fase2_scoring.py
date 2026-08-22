"""
VERSION: 32 (23/08/2026) - ARREGLO CRITICO descubierto al auditar los datos
reales del repo: las 107 candidatas europeas de 141 (y 19 de las 30 que se
ven en el cuaderno) no tenian NINGUN dato de precio. Yahoo devolvia filas con
todos los cierres a NaN para .PA .MI .MC .AS .HE .LS .BR y .L, mientras que
EEUU, .AX y .TO funcionaban. Peor aun, el sistema no se enteraba: como NaN no
es mayor ni menor que nada, las comparaciones daban False y esas acciones
salian etiquetadas como tendencia "mixta", indistinguibles de una candidata
con datos completos. Tres cambios: (1) historico_util() prueba tres formas de
pedir el historico y comprueba que vengan precios de verdad; (2)
tendencia_tecnica() devuelve None en vez de inventarse "mixta"; (3) una
candidata sin datos de precio se descarta con motivo explicito en vez de
competir a ciegas en el ranking. Tambien corrige estado_indice(), que exigia
mas de 200 sesiones sobre un periodo de 220 dias naturales (~148 sesiones) y
por tanto habria dejado el regimen de mercado SIEMPRE en "desconocido".

VERSION: 31 (23/08/2026) - tres mejoras adoptadas del proyecto abierto
RyanJHamby/stock-screener, todas dentro del mismo presupuesto de 100 puntos
(el maximo teorico NO cambia):

(1) REGIMEN DE MERCADO. Antes una candidata puntuaba igual con todo el
    mercado subiendo que con todo el mercado desplomandose. Ahora, una vez
    por ejecucion, se mira el estado del EuroStoxx50 y del S&P500 (precio vs
    SMA50/SMA200 y pendiente de la SMA50) y cada candidata recibe el regimen
    del mercado que le corresponde: favorable 0, neutro -3, adverso -8. Como
    el caso favorable no suma nada, el maximo sigue siendo 100.

(2) FUERZA RELATIVA. El momentum era absoluto: subir un 5% puntuaba igual
    con el indice plano que con el indice subiendo un 12% (donde en realidad
    se esta quedando atras). El presupuesto de momentum (12,9) se reparte
    ahora en 8,9 de momentum propio + 4,0 de fuerza relativa frente al
    indice de su mercado. Suma identica.

(3) PUNTUACION LINEAL en vez de escalones, en dispersion y momentum. Los
    escalones creaban acantilados absurdos (dispersion 29,9% valia 16,1 y
    30,1% valia 9,7 — casi 7 puntos por dos decimas). Ahora la puntuacion
    baja de forma continua. Los topes maximos y minimos son los mismos.

Ademas cada candidata sale etiquetada con version_scoring, para que al
analizar el historico se pueda distinguir lo puntuado con v30 de lo
puntuado con v31 y no se mezclen dos metodos distintos en la misma
estadistica.

VERSION: 30 (19/08/2026) - dos arreglos: (1) CORRECCIÓN de ruido de coma
flotante en el score (visto en la práctica: "64.10000000000001" en vez de
"64.1") — catalizador/euros/noticias se sumaban DESPUÉS del redondeo
interno de calcular_score() sin volver a redondear el resultado final;
(2) en caso de empate exacto de score, desempata por nombre de empresa
A-Z (antes el orden entre empatados no estaba definido).

VERSION: 29 (19/08/2026) - CORRECCIÓN IMPORTANTE: el score podía superar
100 (visto en la práctica: Lottomatica dio 104,3), porque la suma de los
máximos de los 10 factores daba 155, no 100. Reescalado TODO
proporcionalmente (factor 100/155 = 0,6452) para que el máximo teórico
absoluto sea exactamente 100 — ninguna lógica ni umbral ha cambiado, solo
los números de puntos. Además, el empujón de "consenso real" pasa de una
fórmula continua a bloques de 20% (60-79% / 80-99% / 100%), tal como se
pidió, dentro de su nuevo presupuesto (16,1 máximo).

VERSION: 28 (11/08/2026) - unifica el consenso real en una sola fórmula
continua que empieza en 60% de consenso combinado (antes el premio fuerte
solo empezaba en 90%, dejando un hueco enorme sin recompensa entre 75% y
90%). Escala de +10 a +25 según lo amplio del consenso Y la convicción
real (compra fuerte), a partes iguales, pesado también por tamaño de
muestra. Sustituye a los escalones sueltos de 75%/90% anteriores.

VERSION: 27 (11/08/2026) - dos cambios: (1) corrige la ventana del
catalizador de resultados, de 1-4 días de vuelta a 0-4 (el usuario se
había equivocado al pedir 1-4); (2) rediseña el bloque de momentum:
añade momentum_5d para distinguir si un movimiento fuerte (>+25% o
<-15% en el mes) sigue activo ahora mismo o ya se ha calmado — una
caída fuerte YA ESTABILIZADA se trata como posible rebote (+15), no
como cuchillo cayendo (+0); una subida fuerte YA CALMADA mantiene el
+5 de antes, pero si sigue disparándose ahora mismo baja a +0.

VERSION: 26 (11/08/2026) - tres ajustes de calibración a petición del
usuario: (1) potencial ahora alcanza el tope +25 con 75% de subida
esperada, no 100% (divisor 4→3); (2) catalizador de resultados: ventana
cambiada de 0-2 días a 1-4 días; (3) tendencia de recomendaciones (3
meses) sube de ±5 a ±10.

VERSION: 25 (11/08/2026) - añade un factor de confianza por tamaño de
muestra al empujón de "compra fuerte": con menos de 10 analistas totales,
un mismo % es menos fiable estadísticamente que con 10+, así que se reduce
proporcionalmente (confianza plena a partir de 10 analistas). También sube
el umbral del techo del empujón de 50% a 75% de compra fuerte. Con esto,
"4 de 10" (mismo 40%, más gente detrás) pesa casi el doble que "2 de 5".

VERSION: 24 (11/08/2026) - el escalón de "compra fuerte + compra ≥90%
combinado" ya no da un +12 fijo diera igual el reparto interno — ahora
escala entre +8 y +12 según cuánta "compra fuerte" hay de verdad (no solo
"compra" normal). Detectado con EXO.AS (12,5% compra fuerte) y UNI.MI
(40%) llevándose exactamente el mismo empujón pese a convicción distinta.

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
VERSION_SCORING = 32

# Indices de referencia para el regimen de mercado y la fuerza relativa.
# Cada candidata se compara con el indice de SU mercado: no tiene sentido
# medir a una espanola contra el S&P500.
INDICE_EURO = "^STOXX50E"
INDICE_USA = "^GSPC"
PENALIZACION_REGIMEN = {"favorable": 0.0, "neutro": -3.0, "adverso": -8.0}


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
        if dias_desde < 0 or dias_desde > 4:
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


def historico_util(ticker_obj, ticker):
    """Pide el historico de precios y NO SE FIA del resultado.

    Descubierto el 22/08/2026: para las acciones europeas (.PA .MI .MC .AS
    .HE .LS .BR .L) Yahoo devolvia filas pero con TODOS los cierres a NaN.
    Como NaN no es mayor ni menor que nada, todas las comparaciones daban
    False y el sistema etiquetaba esas acciones como tendencia "mixta" en
    vez de reconocer que no tenia datos. 107 de 141 candidatas, y 19 de las
    30 que se ven en el cuaderno, se estaban puntuando a ciegas sin que
    nada lo indicara.

    Ahora se prueban varias formas de pedirlo y se comprueba que de verdad
    vengan precios. Devuelve (hist, metodo) o (None, None) si ninguna
    funciona — y None significa None, no se disfraza de dato."""
    intentos = [
        ("periodo_220d", lambda: ticker_obj.history(period="220d")),
        ("periodo_1y", lambda: ticker_obj.history(period="1y")),
        ("fechas_explicitas", lambda: ticker_obj.history(
            start=(datetime.now() - timedelta(days=400)).strftime("%Y-%m-%d"),
            end=datetime.now().strftime("%Y-%m-%d"))),
    ]
    for nombre, intento in intentos:
        try:
            hist = intento()
        except Exception:
            continue
        if hist is None or len(hist) == 0 or "Close" not in hist.columns:
            continue
        # Lo importante: que haya precios de verdad, no solo filas
        hist = hist[hist["Close"].notna()]
        if len(hist) >= 30:
            return hist, nombre
    return None, None


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

        # Si la media sale NaN no hay tendencia que valga: devolver "mixta"
        # aqui seria inventarse una etiqueta. Es justo lo que pasaba con las
        # europeas hasta el 22/08/2026.
        if sma50 != sma50:  # NaN
            return None, None, None
        if sma200 is not None and sma200 != sma200:
            sma200 = None

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
            empujon = -9.7
        elif pct_vender >= 10:
            empujon = -5.2
        elif pct_buy_o_mas >= 60:
            # Por bloques de 20% de consenso combinado (compra fuerte +
            # compra normal), empezando en 60% — cada bloque que se cruza
            # sube de nivel. Reparte el presupuesto de este factor (16.1
            # máximo) en 3 niveles: 60-79% / 80-99% / 100%. Dentro de cada
            # nivel, se pesa además por cuánta "compra fuerte" hay de
            # verdad (no solo "compra" normal) y por el tamaño de
            # muestra (con menos de 10 analistas, un mismo % es menos
            # fiable estadísticamente).
            if pct_buy_o_mas >= 100:
                nivel = 3
            elif pct_buy_o_mas >= 80:
                nivel = 2
            else:
                nivel = 1
            base_por_nivel = {1: 5.4, 2: 10.7, 3: 16.1}
            base = base_por_nivel[nivel]
            factor_conviccion = min(pct_strong_buy, 75) / 75
            confianza_muestra = min(1.0, total / 10)
            empujon = round(base * (0.5 + 0.5 * factor_conviccion) * confianza_muestra, 1)
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


_cache_indices = {}


def estado_indice(simbolo):
    """Estado de un indice de referencia, calculado UNA sola vez por
    ejecucion y reutilizado para todas las candidatas de ese mercado.

    Devuelve (regimen, momentum_30d):
      - "favorable": el indice esta por encima de sus dos medias y la de 50
        sesiones sube -> el viento sopla a favor
      - "adverso": el indice esta por debajo de la media de 200 sesiones o
        la de 50 cae con claridad -> comprar aqui tiene la probabilidad en
        contra por mucho que la accion concreta pinte bien
      - "neutro": ni una cosa ni la otra
      - "desconocido": no hay datos suficientes; en ese caso NO se penaliza
        nada, porque castigar por falta de datos seria castigar al azar
    """
    if simbolo in _cache_indices:
        return _cache_indices[simbolo]

    resultado = ("desconocido", None)
    try:
        obj = yf.Ticker(simbolo)
        hist, _ = historico_util(obj, simbolo)
        # 220 dias naturales son solo ~148 sesiones, asi que exigir >200
        # dejaba el regimen SIEMPRE en "desconocido" y esta mejora no habria
        # hecho nada. historico_util prueba tambien 1 año y fechas explicitas.
        if hist is not None and len(hist) > 200:
            cierres = hist["Close"]
            actual = cierres.iloc[-1]
            sma50 = cierres.rolling(50).mean().iloc[-1]
            sma200 = cierres.rolling(200).mean().iloc[-1]
            sma50_hace_un_mes = cierres.rolling(50).mean().iloc[-22]
            pendiente50 = (sma50 / sma50_hace_un_mes - 1) * 100
            momentum = round((actual / cierres.iloc[-22] - 1) * 100, 1)

            if actual > sma50 and actual > sma200 and pendiente50 > 0:
                regimen = "favorable"
            elif actual < sma200 or pendiente50 < -1.5:
                regimen = "adverso"
            else:
                regimen = "neutro"
            resultado = (regimen, momentum)
    except Exception:
        pass  # sin datos del indice, se sigue adelante sin penalizar

    _cache_indices[simbolo] = resultado
    return resultado


def indice_de_referencia(cotiza_en_euros):
    return INDICE_EURO if cotiza_en_euros else INDICE_USA


def puntos_dispersion(dispersion_pct):
    """Antes: escalones en 30/60/100 que creaban saltos de casi 7 puntos por
    dos decimas de diferencia. Ahora baja de forma continua desde el maximo
    (16,1 con dispersion <=20%) hasta 0 (dispersion >=110%). Mismos topes."""
    if dispersion_pct is None:
        return 0.0
    proporcion = (110 - dispersion_pct) / 90  # 1 en el 20%, 0 en el 110%
    return round(16.1 * min(max(proporcion, 0.0), 1.0), 2)


def puntos_momentum(momentum_30d, momentum_5d):
    """Momentum propio de la accion, ahora continuo (maximo 8,9; antes 12,9,
    porque 4,0 se han movido a fuerza relativa).

    La logica de fondo es la misma de siempre y no cambia:
      - Dentro del rango normal (-15% a +25% en el mes): puntuacion plena.
      - Subida parabolica: cuanto mas se ha disparado y mas siga
        disparandose AHORA MISMO (momentum de 5 dias), peor punto de entrada.
      - Caida fuerte: si sigue cayendo es un cuchillo cayendo; si ya se ha
        estabilizado es una posible entrada de rebote.
    Lo que cambia es que el paso entre "sigue disparado" y "ya se ha
    calmado" es un degradado, no un interruptor en +8% / -8%."""
    MAX = 8.9
    if momentum_30d is None:
        return 0.0
    if -15 <= momentum_30d <= 25:
        return MAX

    if momentum_30d > 25:
        # 1 justo en el +25%, 0 a partir del +65%
        atenuacion = min(max(1 - (momentum_30d - 25) / 40, 0.0), 1.0)
        # 1 = ya calmado (5d <= -8), 0 = todavia disparandose (5d >= +8)
        calmado = 1.0 if momentum_5d is None else min(max((8 - momentum_5d) / 16, 0.0), 1.0)
        return round(MAX * atenuacion * (0.05 + 0.55 * calmado), 2)

    # Caida fuerte (<-15%)
    # 1 justo en el -15%, no baja de 0,3 por muy grande que sea el desplome
    atenuacion = min(max(1 - (-15 - momentum_30d) / 45, 0.3), 1.0)
    # 1 = ya estabilizada (5d >= +8), 0 = todavia en caida libre (5d <= -8)
    estabilizada = 1.0 if momentum_5d is None else min(max((momentum_5d + 8) / 16, 0.0), 1.0)
    return round(MAX * atenuacion * (0.05 + 0.95 * estabilizada), 2)


def puntos_fuerza_relativa(fuerza_relativa):
    """Factor NUEVO (maximo 4,0, minimo -2,0): cuanto lo hace la accion por
    encima o por debajo de su indice en el ultimo mes.

    Motivo: subir un 5% no significa lo mismo con el indice plano que con el
    indice subiendo un 12% — en el segundo caso la accion se esta quedando
    atras aunque en absoluto suba. El momentum de arriba no distingue esos
    dos casos; este factor si."""
    if fuerza_relativa is None:
        return 0.0
    # +10 puntos porcentuales por encima del indice = tope; -10 = suelo
    proporcion = min(max(fuerza_relativa / 10, -1.0), 1.0)
    return round(4.0 * proporcion if proporcion >= 0 else 2.0 * proporcion, 2)


def calcular_score(info, momentum_30d, dispersion_pct, tendencia_tec=None, tendencia_analistas_valor=None, empujon_consenso_real=0, momentum_5d=None, fuerza_relativa=None, regimen=None):
    """
    Score de 0 a 100 de verdad — reescalado (11/08/2026) para que la suma
    de los máximos de los 10 factores dé exactamente 100 (antes sumaban
    155, por eso podían salir notas de 104+). Factor de reescalado:
    100/155 = 0,6452, aplicado a cada factor por igual — ninguna lógica
    ni umbral ha cambiado, solo los números de puntos.
    - Consenso de analistas (peso bajo, es la señal más ruidosa)
    - Dispersión entre precio objetivo alto/bajo (a MENOS dispersión, más fiable el consenso)
    - Momentum reciente (evita comprar algo que ya se ha desplomado o que está sobrecomprado)
    - Tendencia técnica (SMA50/200) y tendencia de recomendaciones (mes a mes), peso menor:
      son un empujón/freno sobre el resto, no el criterio principal.
    """
    score = 0

    recomendacion = (info.get("recommendationKey") or "").lower()
    puntos_consenso = {
        "strong_buy": 9.7,
        "buy": 6.5,
        "hold": 1.9,
        "underperform": -6.5,
        "sell": -12.9,
    }
    score += puntos_consenso.get(recomendacion, 0)

    # Menos dispersión = consenso más fiable = más puntos.
    # v31: continuo en vez de escalones (ver puntos_dispersion).
    score += puntos_dispersion(dispersion_pct)

    # Momentum propio de la acción (v31: continuo, máximo 8,9)
    score += puntos_momentum(momentum_30d, momentum_5d)

    # Fuerza relativa frente al índice de su mercado (v31, nuevo: máx +4,0)
    score += puntos_fuerza_relativa(fuerza_relativa)

    # Potencial de subida hasta precio objetivo medio — mismo 75% para
    # alcanzar el tope que antes, solo que el tope ahora es 16.1 en vez de 25
    target = info.get("targetMeanPrice")
    precio = info.get("currentPrice") or info.get("regularMarketPrice")
    if target and precio and precio > 0:
        potencial = (target - precio) / precio * 100
        score += min(max(potencial / 4.65, -6.5), 16.1)

    # Tendencia técnica: pequeño empujón/freno, no domina el score
    if tendencia_tec == "alcista":
        score += 3.2
    elif tendencia_tec == "bajista":
        score -= 3.2

    # Tendencia de recomendaciones mes a mes
    if tendencia_analistas_valor == "mejorando":
        score += 6.5
    elif tendencia_analistas_valor == "empeorando":
        score -= 6.5

    # Consenso real por reparto de categorías (no solo la etiqueta media)
    score += empujon_consenso_real

    # Régimen de mercado (v31): resta cuando el mercado entero rema en
    # contra. El caso favorable suma 0, así que el máximo teórico sigue
    # siendo exactamente 100. Si el régimen es desconocido, no penaliza.
    score += PENALIZACION_REGIMEN.get(regimen, 0.0)

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

        hist, metodo_datos = historico_util(t, ticker)
        if hist is None:
            # Antes esto seguia adelante en silencio y la candidata competia
            # en el ranking sin ningun dato tecnico, aparentando normalidad.
            return {"ticker": ticker, "descartado": True,
                    "motivo": "Sin datos de precio utilizables en Yahoo - no se puede evaluar"}

        momentum_30d = None
        if len(hist) > 22:
            momentum_30d = round((hist["Close"].iloc[-1] / hist["Close"].iloc[-22] - 1) * 100, 1)

        momentum_5d = None
        if len(hist) > 6:
            momentum_5d = round((hist["Close"].iloc[-1] / hist["Close"].iloc[-6] - 1) * 100, 1)

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

        # v31: el índice de referencia depende del mercado de la acción, así
        # que hay que saber si cotiza en euros ANTES de puntuar (antes esto
        # se calculaba después, solo para el bonus de divisa).
        cotiza_en_euros = ticker.endswith((".MC", ".DE", ".PA", ".AS", ".BR", ".LS", ".MI", ".VI", ".HE"))
        indice = indice_de_referencia(cotiza_en_euros)
        regimen, momentum_indice = estado_indice(indice)

        fuerza_relativa = None
        if momentum_30d is not None and momentum_indice is not None:
            fuerza_relativa = round(momentum_30d - momentum_indice, 1)

        score = calcular_score(info, momentum_30d, dispersion_pct, tendencia_tec,
                               tendencia_analistas_valor, empujon_consenso_real, momentum_5d,
                               fuerza_relativa, regimen)
        if catalizador:
            score += 7.7  # empujón notable pero que no domine el resto del método

        if cotiza_en_euros:
            score += 5.2  # sin cambio de divisa: no pierdes céntimos en la conversión al comprar/vender

        nombre_empresa_valor = info.get("longName") or info.get("shortName")
        noticias = analizar_noticias(t, ticker, nombre_empresa_valor)
        empujon_noticias = max(-6.5, min(6.5, noticias["sentimiento_total"] * 1.3))  # tope para que no domine el resto
        score += empujon_noticias
        score = round(score, 1)  # redondeo final — catalizador/euros/noticias se suman DESPUÉS del
        # redondeo interno de calcular_score(), y sumar varios decimales seguidos sin volver a
        # redondear genera ruido de coma flotante (ej. "64.10000000000001" en vez de "64.1")

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
            "momentum_5d_pct": limpio(momentum_5d),
            "fuerza_relativa_pct": limpio(fuerza_relativa),
            "regimen_mercado": regimen,
            "indice_referencia": indice,
            "version_scoring": VERSION_SCORING,
            "metodo_datos": metodo_datos,
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
    # Orden principal por score (de más a menos); si empatan exactamente
    # (mismo score tras redondear), desempata por nombre de empresa A-Z
    validos.sort(key=lambda x: (x.get("nombre_empresa") or x["ticker"]).lower())
    validos.sort(key=lambda x: x["score"], reverse=True)  # estable: conserva el orden alfabético dentro de cada empate

    descartados = [r for r in resultados if r.get("descartado")]

    salida = {
        "generado": datetime.now().isoformat(),
        "version_scoring": VERSION_SCORING,
        "regimen_mercado": {
            "euro": {"indice": INDICE_EURO, "estado": estado_indice(INDICE_EURO)[0],
                     "momentum_30d_pct": estado_indice(INDICE_EURO)[1]},
            "usa": {"indice": INDICE_USA, "estado": estado_indice(INDICE_USA)[0],
                    "momentum_30d_pct": estado_indice(INDICE_USA)[1]},
        },
        "ranking": validos,
        "descartados": descartados,
    }

    with open(SALIDA, "w", encoding="utf-8") as f:
        json.dump(salida, f, indent=2, ensure_ascii=False, allow_nan=False, default=convertir_tipos_numpy)

    print(f"Ranking generado: {len(validos)} candidatas válidas, {len(descartados)} descartadas.")


if __name__ == "__main__":
    ejecutar()
