"""
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
from urllib.parse import quote

import requests

ARCHIVO = "candidatos_rankeados.json"
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
    "tradingkey",
}

PALABRAS_POSITIVAS = [
    "upgrade", "beat", "record", "growth", "contract", "surge", "soar",
    "raises", "buy rating", "strong", "profit", "expand", "win", "partnership",
    "mejora", "sube", "récord", "crecimiento", "contrato", "dispara", "eleva",
    "recomendación de compra", "fuerte", "beneficio", "expande", "gana", "acuerdo",
]
PALABRAS_NEGATIVAS = [
    "downgrade", "miss", "loss", "lawsuit", "investigation", "recall",
    "cuts", "sell rating", "weak", "delay", "dilution", "bankruptcy", "fraud",
    "rebaja", "cae", "pérdida", "demanda judicial", "investigación", "retirada",
    "recorta", "recomendación de venta", "débil", "retraso", "dilución", "quiebra", "fraude",
]


def sentimiento_titular(titular):
    t = titular.lower()
    return sum(1 for p in PALABRAS_POSITIVAS if p in t) - sum(1 for p in PALABRAS_NEGATIVAS if p in t)


def parece_pagina_de_datos(titulo):
    t = titulo.lower()
    return any(m in t for m in ("ebitda", "forward p/e", "price to earnings", "enterprise value"))


def parece_cotizacion_en_bruto(titulo):
    return titulo.count("|") >= 2


def buscar_google_news(consulta, maximo=MAX_NOTICIAS_POR_CONSULTA):
    try:
        url = f"https://news.google.com/rss/search?q={quote(consulta)}&hl=es-419&gl=ES&ceid=ES:es"
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
        for n in buscar_google_news(consulta):
            clave = n["titulo"].strip().lower()
            if clave in vistos:
                continue  # mismo artículo devuelto por las dos búsquedas, no se cuenta dos veces
            if not es_relevante(n["titulo"], nombre):
                continue  # no menciona de verdad la empresa, se descarta
            vistos.add(clave)
            encontrados.append(n)
        time.sleep(PAUSA_ENTRE_PETICIONES)

    sentimiento_adicional = 0
    titulares_adicionales = []
    for n in encontrados:
        puntos = sentimiento_titular(n["titulo"])
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

    nuevo_ranking = sorted(profundizadas + resto, key=lambda c: c["score"], reverse=True)
    data["ranking"] = nuevo_ranking

    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False, allow_nan=False)

    print(f"Profundización completa: {len(a_profundizar)} candidatas revisadas con búsquedas adicionales.")


if __name__ == "__main__":
    ejecutar()
