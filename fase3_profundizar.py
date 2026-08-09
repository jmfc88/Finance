"""
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
EMPUJON_MAXIMO = 8  # tope, para que esta pasada afine sin dominar el score

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


def profundizar_candidata(candidata):
    nombre = candidata.get("nombre_empresa") or candidata["ticker"]
    consultas = [f"{nombre} analistas", f"{nombre} previsión"]

    sentimiento_adicional = 0
    titulares_adicionales = []
    for consulta in consultas:
        for n in buscar_google_news(consulta):
            puntos = sentimiento_titular(n["titulo"])
            sentimiento_adicional += puntos
            titulares_adicionales.append({"titulo": n["titulo"], "fuente": n["fuente"], "sentimiento": puntos})
        time.sleep(PAUSA_ENTRE_PETICIONES)

    titulares_adicionales.sort(key=lambda t: abs(t["sentimiento"]), reverse=True)
    empujon = max(-EMPUJON_MAXIMO, min(EMPUJON_MAXIMO, sentimiento_adicional * 2))

    candidata["profundizacion"] = {
        "sentimiento_adicional": sentimiento_adicional,
        "empujon": empujon,
        "titulares_adicionales": titulares_adicionales[:3],
    }
    candidata["score"] = round(candidata["score"] + empujon, 1)
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
