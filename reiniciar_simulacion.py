"""
VERSION: 1 (24/08/2026) - REINICIO LIMPIO de la simulacion.

POR QUE HACE FALTA: simulacion_operaciones.json tiene 31 operaciones, pero 6
son basura de la primerisima ejecucion, cuando el simulador aun compraba
ACCIONES ENTERAS. Esas 6 invirtieron 56, 71 o 97 euros en vez de 100, y
ademas llevan el campo viejo "franja" en vez de "tramo", por eso en el visor
salian como "TRAMO UNDEFINED".

Mezclar posiciones de 56 EUR con posiciones de 100 EUR estropea cualquier
comparacion posterior: los porcentajes no serian comparables entre si y el
analisis por factores heredaria ese ruido desde el primer dia.

QUE HACE ESTE SCRIPT:
  1. Borra TODAS las operaciones existentes y empieza de cero.
  2. Reconstruye desde historial_tarjetas.json, que guarda las tarjetas de
     los ultimos 5 dias. Asi la simulacion no arranca hoy: arranca en la
     fecha real en que cada candidata aparecio por primera vez en el
     cuaderno, con el precio que tenia ESE dia.
  3. Invierte 100,00 EUR EXACTOS en cada una, con participaciones
     fraccionadas. Si una accion cuesta 167 EUR, se compran 0,598
     participaciones. Lo que se mide es la variacion sobre 100 EUR, no si
     cabia una accion entera.

Se ejecuta UNA VEZ. Despues, simulacion.py sigue como siempre.

CUIDADO: borra el historico de la simulacion. No toca ledger.json ni nada de
la operativa real; solo el banco de pruebas.
"""

import json
from datetime import datetime

TARJETAS = "historial_tarjetas.json"
OPERACIONES = "simulacion_operaciones.json"
CAPITAL_POR_OPERACION = 100.0
TOP_N = 30


def tramo_de(posicion):
    if posicion <= 10:
        return "1-10"
    if posicion <= 20:
        return "11-20"
    return "21-30"


def ejecutar():
    try:
        with open(TARJETAS, "r", encoding="utf-8") as f:
            datos = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"No se pudo leer {TARJETAS}: {e}")
        print("Sin tarjetas guardadas no hay nada que reconstruir.")
        return

    # Cuantas habia antes, solo para dejar constancia de lo que se descarta
    try:
        with open(OPERACIONES, "r", encoding="utf-8") as f:
            antiguas = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        antiguas = []

    print(f"Operaciones antes del reinicio: {len(antiguas)}")
    if antiguas:
        malas = [o for o in antiguas if abs(o.get("invertido", 0) - 100) > 0.01]
        print(f"  de las cuales con importe distinto de 100 EUR: {len(malas)}")
    print()

    operaciones = []
    ya_abiertos = set()

    # Se recorren los dias de mas antiguo a mas reciente: una candidata se
    # abre en la PRIMERA fecha en que aparecio, no en la ultima.
    for dia in sorted(datos.get("dias", []), key=lambda d: d.get("fecha", "")):
        fecha = dia.get("fecha")

        # Dentro de un dia puede haber varias versiones de la misma tarjeta.
        # Se coge la de mejor posicion en el ranking, que es la que mas
        # probablemente vio el usuario en el cuaderno.
        mejor_por_ticker = {}
        for t in dia.get("tarjetas", []):
            tk = t.get("ticker")
            if not tk:
                continue
            # El precio se saca de las APARICIONES, no de la tarjeta: fase3
            # hasta la v12 no guardaba precio_actual dentro de la tarjeta
            # (campo que faltaba en la lista). Las apariciones si lo tienen.
            validas = [a for a in t.get("apariciones", [])
                       if a.get("posicion") and a.get("precio")]
            if not validas:
                continue
            mejor = min(validas, key=lambda a: a["posicion"])
            pos = mejor["posicion"]
            if tk not in mejor_por_ticker or pos < mejor_por_ticker[tk][0]:
                mejor_por_ticker[tk] = (pos, t, mejor["precio"])

        for tk, (pos, t, precio) in sorted(mejor_por_ticker.items(), key=lambda x: x[1][0]):
            if pos > TOP_N or tk in ya_abiertos:
                continue
            tarjeta = dict(t.get("tarjeta") or {})
            tarjeta["precio_actual"] = precio  # se rellena el campo que faltaba
            if not precio or precio <= 0:
                continue

            ya_abiertos.add(tk)
            acciones = round(CAPITAL_POR_OPERACION / precio, 6)
            objetivo = tarjeta.get("precio_objetivo_medio")
            operaciones.append({
                "id": f"{tk}-{fecha}",
                "ticker": tk,
                "nombre": t.get("nombre_empresa"),
                "estado": "abierta",
                "fecha_entrada": fecha,
                "precio_entrada": precio,
                "acciones": acciones,
                # Siempre 100,00 exactos: es el punto de todo esto
                "invertido": round(precio * acciones, 2),
                "posicion_ranking": pos,
                "tramo": tramo_de(pos),
                "score": tarjeta.get("score"),
                "potencial_pct": (round((objetivo / precio - 1) * 100, 1) if objetivo else None),
                "tarjeta": tarjeta,
                "reconstruida": True,  # marca de que viene del historico, no de una pasada en vivo
            })

    with open(OPERACIONES, "w", encoding="utf-8") as f:
        json.dump(operaciones, f, indent=2, ensure_ascii=False, allow_nan=False)

    print(f"Operaciones reconstruidas: {len(operaciones)}")
    print()
    from collections import Counter
    print("Por fecha de entrada:", dict(Counter(o["fecha_entrada"] for o in operaciones)))
    print("Por tramo:", dict(Counter(o["tramo"] for o in operaciones)))
    importes = {round(o["invertido"], 2) for o in operaciones}
    print(f"Importes distintos: {importes}   <- debe ser solo {{100.0}}")
    print()
    print("Ejemplos:")
    for o in operaciones[:5]:
        print(f"  {o['fecha_entrada']}  tramo {o['tramo']:6} nº{o['posicion_ranking']:2}  "
              f"{o['ticker']:10} {o['acciones']:9.4f} part. a {o['precio_entrada']:8.2f} = {o['invertido']:.2f} EUR")
    print()
    print("Listo. La proxima ejecucion de simulacion.py las evaluara con el")
    print("historico de precios desde su fecha de entrada, asi que algunas")
    print("pueden cerrarse ya en esa misma pasada.")


if __name__ == "__main__":
    ejecutar()
