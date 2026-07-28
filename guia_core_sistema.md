# Guía Core — Sistema de Inversión (200€ → escalado a 1 año)

## El flujo completo, de un vistazo

```
fase1_screening.py  →  fase2_scoring.py  →  candidatos_rankeados.json
        (NO corren solos: los lanzas tú a mano desde GitHub Actions,
         botón "Run workflow", cuando quieras datos frescos. Cero coste
         mientras no los lances)

Tú, el día que quieras comprar:
   1. lanzas ranking-github-actions.yml a mano (Actions → Run workflow)
   2. abres scoring_viewer.html → pulsas "Traer lista" → ves el ranking
   3. decides → compras en Trade Republic
   4. registras la compra en simulador.html

Mientras tienes posiciones abiertas:
   bot.py vigila el precio → cuando el stop-loss dinámico salta, TE AVISA (esta
   sí es una notificación que quieres, porque protege de pérdidas)

Cuando vendes:
   registras la venta en simulador.html (historial guardado, FIFO, resumen fiscal)
   actualizas tu capital en el panel de progreso de scoring_viewer.html
   esperas tu pausa personal (~10 días) y vuelves a abrir el visor cuando quieras
```

---

## Piezas activas

### 1. `fase1_screening.py`
**Qué hace:** recorre en lotes los índices globales (S&P500, DAX, FTSE100, CAC40, IBEX35, Nikkei225, EuroStoxx50) buscando consenso de analistas de compra + beta alto. Guarda los candidatos fuertes en `candidatos_fase1.json`.
**Cómo se usa:** no se toca a mano. Lo ejecuta `ranking-github-actions.yml` solo, cada 12h.

### 2. `fase2_scoring.py`
**Qué hace:** coge `candidatos_fase1.json` y le pone un score real (0-100) combinando consenso, dispersión entre analistas, momentum de 30 días y potencial de subida. Descarta automáticamente las que publican resultados en menos de 5 días (riesgo de evento binario) y las que superan ~200€/acción. Genera `candidatos_rankeados.json`.
**Cómo se usa:** tampoco se toca a mano, corre junto al anterior en el mismo workflow.

### 3. `ranking-github-actions.yml`
**Qué hace:** el workflow de GitHub Actions que ejecuta 1 y 2 y sube los resultados a tu repo. Solo corre cuando tú lo lanzas — sin cron, sin coste automático.
**Cómo se usa:** se sube una vez al repo (carpeta `.github/workflows/`). Cuando quieras datos frescos: pestaña "Actions" en la app de GitHub → seleccionas el workflow → botón "Run workflow". Tarda 1-2 minutos.

### 4. `scoring_viewer.html`
**Qué hace:** tu punto de entrada real. Trae el ranking del repo bajo demanda (tú decides cuándo mirarlo, nada empuja hacia ti) y muestra cada candidata con score, precio, consenso, potencial, momentum y motivo si fue descartada. Incluye el panel de progreso de capital (nivel actual, cuánto te falta para poder abrir más posiciones).
**Cómo se usa:**
- La primera vez, escribe tu `usuario/repositorio` de GitHub y pulsa "Traer lista" (se guarda solo).
- Cada vez que quieras comprar: ábrelo, pulsa "Traer lista", decide.
- Cada vez que tu capital cambie: actualiza el número en "capital €" y pulsa "Guardar".

### 5. `simulador.html`
**Qué hace:** tu cuaderno de cuentas. Break-even, stop-loss con beneficio neto garantizado, trailing stop dinámico con historial, ledger FIFO de operaciones y resumen fiscal (comisiones, 19% Hacienda, coste prorateado del asesor, ganancia neta real).
**Cómo se usa:** aquí registras cada compra y cada venta, a mano, copiando el precio real de Trade Republic. El historial queda guardado permanentemente.

### 6. `bot.py`
**Qué hace:** vigila el precio de tus posiciones abiertas y calcula el stop-loss/trailing stop dinámico (Trade Republic no tiene esta función). Cuando salta, te avisa por notificación al móvil vía ntfy.sh — esta es la única notificación que quieres, porque te protege de perder dinero.
**Cómo se usa:** corre en GitHub Actions en segundo plano mientras tengas posiciones abiertas. Tú solo reaccionas cuando te avisa: entras a Trade Republic y vendes.

### 7. `bot1_noticias.py`
**Qué hace:** analiza sentimiento de noticias solo de las candidatas que ya pasaron la fase 1, como capa extra de contexto antes de decidir.
**Cómo se usa:** complementario, se consulta si quieres una segunda opinión antes de comprar una candidata concreta.

---

## Piezas descartadas (ya no forman parte del flujo)

| Archivo | Por qué se dejó de usar |
|---|---|
| `gestor_capital.py` | Decidía él solo cuántas posiciones abrir y repartía el capital. Preferiste decidir tú mismo tras ver el ranking. |
| `notificar_plan.py` | Notificación diaria del plan de compra — ya no quieres avisos de compra, solo de stop-loss. |
| `plan-diario-github-actions.yml` | Workflow que encadenaba screening + capital + notificación. Sustituido por `ranking-github-actions.yml`, más simple. |
| `capital.json` | Lo usaba `gestor_capital.py`. El capital ahora se gestiona a mano en el panel de progreso de `scoring_viewer.html`. |

---

## Orden de ejecución — primera simulación

1. **Sube al repo de GitHub:** `fase1_screening.py`, `fase2_scoring.py`, `bot1_noticias.py`, `bot.py`, y `ranking-github-actions.yml` (dentro de `.github/workflows/`).
2. **Lanza el workflow a mano:** app de GitHub → pestaña "Actions" → `ranking-github-actions.yml` → "Run workflow". Espera 1-2 min a que termine.
3. **Abre `scoring_viewer.html`:** escribe tu `usuario/repositorio`, pulsa "Traer lista". Revisa el ranking y las descartadas.
4. **Mete tu capital (200€) en el panel de progreso** del visor y guarda, para ver tu nivel de partida.
5. **Elige tu candidata** del ranking, teniendo en cuenta precio (<200€, acción entera) y que no publique resultados pronto.
6. **Compra en Trade Republic** (modo automático, 1€ comisión).
7. **Registra la compra en `simulador.html`** (precio real, comisión, fecha).
8. **Deja `bot.py` corriendo** (o lo activas tú) para que vigile el stop-loss dinámico de esa posición.
9. **Cuando `bot.py` te avise** de que el stop-loss ha saltado: vendes en Trade Republic.
10. **Registra la venta en `simulador.html`** (beneficio neto, 19% Hacienda, ledger FIFO).
11. **Actualiza tu capital** en el panel de progreso del visor.
12. **Pausa personal (~10 días)**, y vuelves al paso 2 cuando quieras.

---

## Tu regla personal (no está en ningún archivo, es tuya)

Compras hoy → mantienes con stop-loss dinámico protegiendo ganancias → cuando vendes, pausa de ~10 días antes de volver a mirar el visor (para no operar en caliente, sin presión de notificaciones). Objetivo: escalar de 1 posición a 3-4 en 1 año, según el panel de progreso.

**Aviso fiscal importante:** si alguna vez vendes con **pérdida** y quieres recomprar el **mismo ticker**, espera **2 meses**, no 10 días — si no, Hacienda bloquea esa pérdida ese ejercicio (art. 33.5 LIRPF). Para tickers distintos, esto no aplica.
