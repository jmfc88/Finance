"""
VERSION: 2 (04/08/2026) - avisa también cuando el stop-loss SUBE (no solo
cuando salta), con notificación no urgente distinta, para tener visibilidad
del trailing sin tener que mirar posiciones.json a mano en GitHub

BOT DE STOP-LOSS DINÁMICO
==========================================
Trade Republic no tiene trailing stop nativo, así que este bot lo
sustituye: vigila tus posiciones abiertas y, en cuanto el precio cae
hasta el nivel de stop-loss (que solo sube, nunca baja, protegiendo
siempre ganancia neta ya conseguida), te avisa por notificación al
móvil vía ntfy.sh.

Es la ÚNICA notificación que Jose Manuel quiere: protege de pérdidas,
no empuja decisiones de compra.

Entrada:  posiciones.json -> lista de posiciones abiertas
Salida:   posiciones.json actualizado (nuevo stop-loss si ha subido)
          + notificación si el stop-loss ha saltado
"""

import json
import os

import requests
import yfinance as yf

POSICIONES_FILE = "posiciones.json"
NTFY_TOPIC = os.environ.get("NTFY_TOPIC")

COMISION_COMPRA = 1.0
COMISION_VENTA = 1.0
TAX_RATE = 0.19

# Ejemplo de posiciones.json:
# [
#   {
#     "ticker": "OUST",
#     "precio_compra": 41.30,
#     "acciones": 3,
#     "stop_loss_actual": 39.50,     # se actualiza solo, solo puede subir
#     "trailing_pct": 8,             # % por debajo del máximo alcanzado
#     "maximo_alcanzado": 45.10
#   }
# ]


def cargar_posiciones():
    if not os.path.exists(POSICIONES_FILE):
        return []
    with open(POSICIONES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_posiciones(posiciones):
    with open(POSICIONES_FILE, "w", encoding="utf-8") as f:
        json.dump(posiciones, f, indent=2, ensure_ascii=False)


def beneficio_neto(precio_compra, precio_venta, acciones):
    bruto = (precio_venta - precio_compra) * acciones
    comisiones = COMISION_COMPRA + COMISION_VENTA
    ganancia_antes_impuesto = bruto - comisiones
    impuesto = max(ganancia_antes_impuesto, 0) * TAX_RATE
    return round(ganancia_antes_impuesto - impuesto, 2)


def notificar(titulo, mensaje, urgente=True):
    if not NTFY_TOPIC:
        print(f"[SIN NTFY_TOPIC] {titulo}: {mensaje}")
        return
    requests.post(
        f"https://ntfy.sh/{NTFY_TOPIC}",
        data=mensaje.encode("utf-8"),
        headers={
            "Title": titulo,
            "Priority": "urgent" if urgente else "default",
            "Tags": "warning" if urgente else "chart_with_upwards_trend",
        },
    )


def procesar_posicion(pos):
    precio_actual = yf.Ticker(pos["ticker"]).info.get("currentPrice")
    if not precio_actual:
        return pos, False

    stop_anterior = pos.get("stop_loss_actual", 0)

    # Actualiza el máximo alcanzado y sube el stop-loss si corresponde (nunca baja)
    if precio_actual > pos.get("maximo_alcanzado", pos["precio_compra"]):
        pos["maximo_alcanzado"] = precio_actual
        nuevo_stop = round(precio_actual * (1 - pos["trailing_pct"] / 100), 2)
        if nuevo_stop > stop_anterior:
            pos["stop_loss_actual"] = nuevo_stop
            notificar(
                f"📈 {pos['ticker']} sube — sube tu stop-loss",
                f"Nuevo máximo: {precio_actual}$. Sube tu stop-loss en Trade Republic de "
                f"{stop_anterior}$ a {nuevo_stop}$ (protege más ganancia ya conseguida).",
                urgente=False,
            )

    salto = precio_actual <= pos.get("stop_loss_actual", 0)
    if salto:
        neto = beneficio_neto(pos["precio_compra"], precio_actual, pos["acciones"])
        notificar(
            f"🔴 VENDE {pos['ticker']} - stop-loss activado",
            f"Precio actual: {precio_actual}$. Stop-loss: {pos['stop_loss_actual']}$. "
            f"Beneficio neto estimado si vendes ahora: {neto}€. Ejecuta la venta en Trade Republic.",
        )
    return pos, salto


def ejecutar():
    posiciones = cargar_posiciones()
    if not posiciones:
        print("No hay posiciones abiertas que vigilar.")
        return

    actualizadas = []
    for pos in posiciones:
        pos_actualizada, salto = procesar_posicion(pos)
        actualizadas.append(pos_actualizada)
        if salto:
            print(f"{pos['ticker']}: stop-loss saltado, notificación enviada.")
        else:
            print(f"{pos['ticker']}: sigue en vigilancia, stop-loss en {pos_actualizada.get('stop_loss_actual')}")

    guardar_posiciones(actualizadas)


if __name__ == "__main__":
    ejecutar()
