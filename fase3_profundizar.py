"""
VERSION: 10 (19/08/2026) - en caso de empate exacto de score tras la
profundización, desempata por nombre de empresa A-Z (igual que fase2).

VERSION: 9 (11/08/2026) - búsquedas en español E inglés (antes solo
español), deduplicando entre los dos. Ojo: dobla el número de peticiones
por candidata (2 consultas × 2 idiomas = 4), así que esta fase tarda algo
más que antes.

VERSION: 8 (11/08/2026) - dos mejoras: (1) sentimiento con detección de
negaciones y vocabulario ampliado en español, igual que fase2_scoring.py;
(2) guarda un histórico acumulado (historial_scoring.json) con snapshot
de las mejores candidatas en cada pasada, para poder cruzar más adelante
contra tus compras/ventas reales y validar si el score de verdad predice
algo — antes no quedaba ningún rastro histórico del ranking.

VERSION: 7 (11/08/2026) - añade peso doble (×2) a prensa económica de
referencia (Reuters, Bloomberg, Financial Times, WSJ, The Economist,
Barron's) cuando aparecen — Google News sigue decidiendo solo qué fuentes
salen, esto solo hace que su opinión cuente más cuando sí aparecen.

VERSION: 6 (11/08/2026) - añade eToro a la lista negra de fuentes (páginas
de plantilla tipo "noticias y previsiones de los analistas" para cada
listado de la empresa, no noticias redactadas — detectado con RELX
apareciendo dos veces vía REN.NV y RELX-ADR). También añadido un filtro
por patrón de título como red de seguridad genérica, por si otra fuente
usa la misma plantilla.

VERSION: 5 (06/08/2026) - contradicción con más peso: tope de -20 a -40, y
multiplicador de 3 a 4 por titular negativo — una contradicción real es
peligrosa y tiene que poder hundir a una candidata de verdad, no un tirón
de orejas simbólico.

VERSION: 4 (06/08/2026) - dos arreglos de calidad detectados con RELX: (1)
deduplicación entre las dos búsquedas (antes el mismo artículo podía
contar dos veces si aparecía en ambas); (2) filtro de relevancia: descarta
titulares que no mencionan de verdad el nombre de la empresa (detectado un
artículo de Bloomberg sobre bancos europeos que no tenía nada que ver con
RELX, pero Google News lo devolvió por coincidencia floja).

VERSION: 3 (06/08/2026) - rediseño según lo pedido: si CONFIRMA (neutro o
positivo) no se tocan ni el score ni el orden, solo se marca "verificado".
Si CONTRADICE (encuentra algo claramente negativo pese al score alto), se
resta puntos con tope ±20 — mueve de posición, pero nunca la descarta.
Antes sumaba puntos también en el caso positivo; ya no.

VERSION: 2 (06/08/2026) - amplía el margen de ajuste de ±8 a ±30: antes era
un empujón tan pequeño que casi nunca cambiaba el orden del ranking. Ahora,
si esta pasada encuentra algo fuerte (varias noticias muy negativas o muy
positivas), sí puede redefinir de verdad la posición de la candidata, no
solo maquillar el número.

VERSION: 1 (06/08/2026) - segunda pasada automática, solo sobre las mejores
candidatas del ranking que ya generó fase2_scoring.py (no las 150+, sería
demasiado lento). Hace búsquedas de Google News más específicas
("analistas", "previsión") además de la búsqueda simple que ya hace fase2,
para pillar contexto que la primera pasada no cogió. Reddit se descartó
a propósito: señal ruidosa y manipulable en small-caps, y su API ya no es
de acceso libre (requiere aprobación manual de Reddit, 2-4 semanas).

Entrada/salida: el mismo candidatos_rankeados.json que genera fase2_scoring.py
— lo relee, ajusta el score de las mejores, reordena, y lo vuelve a guardar.
"""

import json
import time
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.parse import quote

import requests

ARCHIVO = "candidatos_rankeados.json"
HISTORICO = "historial_scoring.json"
TOP_N_HISTORICO = 30  # cuántas candidatas se guardan cada vez en el histórico
MAX_ENTRADAS_HISTORICO = 20000  # límite de seguridad para que el archivo no crezca sin fin
TOP_N_A_PROFUNDIZAR = 25  # solo las mejores, para no disparar el tiempo de ejecución
MAX_NOTICIAS_POR_CONSULTA = 4
PAUSA_ENTRE_PETICIONES = 0.6
AJUSTE_MAXIMO_NEGATIVO = 40  # una contradicción es peligrosa de verdad — con
# esto puede tirar a una candidata de estar entre las mejores a la parte
# baja del listado, no un tirón de orejas simbólico. Si CONFIRMA (neutro o
# positivo) no se suma nada, solo se marca como verificada — la
# confirmación no es un motivo para subir puntos.

CABECERAS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}

FUENTES_NO_NOTICIA = {
    "tradingview", "simply wall st", "stockanalysis", "stockanalysis.org",
    "marketbeat", "gurufocus", "insider monkey", "barchart", "investing.com markets",
    "tradingkey", "etoro",
}

PALABRAS_POSITIVAS = [
    "upgrade", "beat", "record", "growth", "contract", "surge", "soar",
    "raises", "buy rating", "strong", "profit", "expand", "win", "partnership",
    "mejora", "sube", "récord", "crecimiento", "contrato", "dispara", "eleva",
    "recomendación de compra", "fuerte", "beneficio", "expande", "gana", "acuerdo",
    "supera", "superó", "superaron", "bate el", "batió", "batieron",
]
PALABRAS_NEGATIVAS = [
    "downgrade", "miss", "loss", "lawsuit", "investigation", "recall",
    "cuts", "sell rating", "weak", "delay", "dilution", "bankruptcy", "fraud",
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
    vez de contar la palabra tal cual. No es NLP de verdad, pero es mucho
    mejor que contar palabras sueltas sin ningún contexto."""
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


FUENTES_PREMIUM = {
    "reuters", "bloomberg", "financial times", "the wall street journal",
    "wsj", "bloomberg businessweek", "the economist", "barron's", "barrons",
}


def peso_fuente(fuente):
    """Da el doble de peso a prensa económica de referencia (Reuters,
    Bloomberg, FT, WSJ...) frente al resto de fuentes de periodismo real —
    no las prioriza en cuáles aparecen (eso lo decide Google News solo,
    no elegimos nosotros de una lista cerrada), solo pesa más su opinión
    cuando sí aparecen."""
    return 2 if any(p in fuente.lower() for p in FUENTES_PREMIUM) else 1


def parece_pagina_de_datos(titulo):
    t = titulo.lower()
    metricas = ("ebitda", "forward p/e", "price to earnings", "enterprise value")
    plantillas_genericas = ("noticias y previsiones de los analistas",)  # patrón de página de perfil, no una noticia redactada
    return any(m in t for m in metricas) or any(p in t for p in plantillas_genericas)


def parece_cotizacion_en_bruto(titulo):
    return titulo.count("|") >= 2


def buscar_google_news(consulta, maximo=MAX_NOTICIAS_POR_CONSULTA, idioma="es"):
    hl, gl, ceid = ("en-US", "US", "US:en") if idioma == "en" else ("es-419", "ES", "ES:es")
    try:
        url = f"https://news.google.com/rss/search?q={quote(consulta)}&hl={hl}&gl={gl}&ceid={ceid}"
        resp = requests.get(url, headers=CABECERAS, timeout=10)
        resp.raise_for_status()
        raiz = ET.fromstring(resp.content)
        items = raiz.findall(".//item")[: maximo * 2]
        resultado = []
        for item in items:
            titulo = (item.findtext("title") or "").strip()
            fuente = (item.findtext("source") or "").strip()
            if not titulo:
                continue
            if fuente.lower() in FUENTES_NO_NOTICIA:
                continue
            if parece_pagina_de_datos(titulo) or parece_cotizacion_en_bruto(titulo):
                continue
            resultado.append({"titulo": titulo, "fuente": fuente})
            if len(resultado) >= maximo:
                break
        return resultado
    except Exception:
        return []


PALABRAS_GENERICAS_EMPRESA = {
    "s.a.", "sa", "plc", "inc", "inc.", "nv", "n.v.", "sgps", "ag", "spa",
    "s.p.a.", "corp", "corp.", "ltd", "ltd.", "co", "co.", "group",
    "holding", "holdings", "s.a", "sociedad", "società", "société",
}


def es_relevante(titulo, nombre_empresa):
    """Filtra artículos que no mencionan de verdad la empresa — a veces
    Google News devuelve resultados de mercado general poco relacionados
    aunque la búsqueda incluyera el nombre exacto (detectado con RELX:
    salió un artículo de Bloomberg sobre bancos europeos que no tenía
    nada que ver con la empresa)."""
    palabras = [p.strip(",.") for p in nombre_empresa.split()
                if p.strip(",.").lower() not in PALABRAS_GENERICAS_EMPRESA]
    if not palabras:
        return True  # si no queda ninguna palabra útil del nombre, no filtramos por si acaso
    return palabras[0].lower() in titulo.lower()


def profundizar_candidata(candidata):
    nombre = candidata.get("nombre_empresa") or candidata["ticker"]
    consultas = [f"{nombre} analistas", f"{nombre} previsión"]

    vistos = set()
    encontrados = []
    for consulta in consultas:
        for idioma in ("es", "en"):
            for n in buscar_google_news(consulta, idioma=idioma):
                clave = n["titulo"].strip().lower()
                if clave in vistos:
                    continue  # mismo artículo devuelto por otra búsqueda/idioma, no se cuenta dos veces
                if not es_relevante(n["titulo"], nombre):
                    continue  # no menciona de verdad la empresa, se descarta
                vistos.add(clave)
                encontrados.append(n)
            time.sleep(PAUSA_ENTRE_PETICIONES)

    sentimiento_adicional = 0
    titulares_adicionales = []
    for n in encontrados:
        puntos = sentimiento_titular(n["titulo"]) * peso_fuente(n["fuente"])
        sentimiento_adicional += puntos
        titulares_adicionales.append({"titulo": n["titulo"], "fuente": n["fuente"], "sentimiento": puntos})

    titulares_adicionales.sort(key=lambda t: abs(t["sentimiento"]), reverse=True)

    if sentimiento_adicional < 0:
        # Contradice la puntuación: está entre las mejores (score alto de
        # fase 2) pero esta búsqueda más a fondo encuentra noticias
        # claramente negativas. Se resta, nunca se descarta del todo.
        verificado = False
        ajuste = max(-AJUSTE_MAXIMO_NEGATIVO, sentimiento_adicional * 4)
        candidata["score"] = round(candidata["score"] + ajuste, 1)
    else:
        # Confirma (neutro o positivo): no se toca el score ni el orden,
        # solo se marca como verificada.
        verificado = True
        ajuste = 0

    candidata["profundizacion"] = {
        "sentimiento_adicional": sentimiento_adicional,
        "verificado": verificado,
        "ajuste": ajuste,
        "titulares_adicionales": titulares_adicionales[:3],
    }
    return candidata


def guardar_historico(ranking):
    """Guarda un snapshot con marca de tiempo de las mejores candidatas de
    esta pasada, SIN tocar ni sobreescribir lo anterior — se acumula. Esto
    es lo que en el futuro nos permite responder de verdad "¿las candidatas
    con score alto rindieron mejor?": cruzando este histórico con las
    fechas y precios reales de tus compras/ventas en el ledger."""
    try:
        with open(HISTORICO, "r", encoding="utf-8") as f:
            historico = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        historico = []

    ahora = datetime.now().isoformat()
    for c in ranking[:TOP_N_HISTORICO]:
        historico.append({
            "fecha_hora": ahora,
            "ticker": c["ticker"],
            "score": c["score"],
            "precio": c.get("precio_actual"),
            "consenso": c.get("consenso"),
            "momentum_30d_pct": c.get("momentum_30d_pct"),
            "dispersion_pct": c.get("dispersion_pct"),
            "tendencia_tecnica": c.get("tendencia_tecnica"),
            "rsi_14": c.get("rsi_14"),
            "cotiza_en_euros": c.get("cotiza_en_euros"),
            "catalizador_resultados": c.get("catalizador_resultados") is not None,
            "profundizacion_verificado": (c.get("profundizacion") or {}).get("verificado"),
        })

    if len(historico) > MAX_ENTRADAS_HISTORICO:
        historico = historico[-MAX_ENTRADAS_HISTORICO:]  # recorta lo más viejo si se dispara

    with open(HISTORICO, "w", encoding="utf-8") as f:
        json.dump(historico, f, indent=2, ensure_ascii=False, allow_nan=False)

    print(f"Histórico actualizado: {len(historico)} snapshots acumulados en total.")


def ejecutar():
    with open(ARCHIVO, "r", encoding="utf-8") as f:
        data = json.load(f)

    ranking = data.get("ranking", [])
    if not ranking:
        print("No hay candidatas en el ranking, nada que profundizar.")
        return

    a_profundizar = ranking[:TOP_N_A_PROFUNDIZAR]
    resto = ranking[TOP_N_A_PROFUNDIZAR:]

    profundizadas = []
    for i, candidata in enumerate(a_profundizar, 1):
        profundizadas.append(profundizar_candidata(candidata))
        print(f"  profundizado {i}/{len(a_profundizar)}: {candidata['ticker']}")

    todas = sorted(profundizadas + resto, key=lambda c: (c.get("nombre_empresa") or c["ticker"]).lower())
    nuevo_ranking = sorted(todas, key=lambda c: c["score"], reverse=True)  # estable: conserva alfabético dentro de cada empate
    data["ranking"] = nuevo_ranking

    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, allow_nan=False)

    guardar_historico(nuevo_ranking)

    print(f"Profundización completa: {len(a_profundizar)} candidatas revisadas con búsquedas adicionales.")


if __name__ == "__main__":
    ejecutar()
