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
**Qué hace:** reconstruye el universo de tickers en cada ejecución leyendo los componentes ACTUALES de S&P500, NASDAQ-100, DJIA, TSX60 (Canadá), IBEX35, DAX, MDAX, SDAX, TecDAX, FTSE100, CAC40, AEX, BEL20, PSI20, FTSE MIB, SMI, ATX, OMXS30 (Suecia), OMXC25 (Dinamarca), OMXH25 (Finlandia), Nikkei225 y EuroStoxx50 directamente de Wikipedia. También incluye ASX200 (Australia), IPC (México) e Ibovespa (Brasil) como intento — sus páginas de Wikipedia no parecen tener tabla de tickers limpia. Quedan fuera MSCI World y Russell 2000. Si un índice falla puntualmente, usa el último listado bueno conocido de ese índice. Busca en todo ese universo consenso de analistas de compra + beta alto (movimiento fuerte) — **excepto en acciones que cotizan en euros** (IBEX35, DAX, CAC40, AEX, BEL20, PSI20, FTSE MIB, ATX, EuroStoxx50), donde basta el consenso de compra sin exigir beta alto, porque no generan cambio de divisa y así entran también empresas consolidadas (ej. BBVA) si tienen un catalizador puntual bueno. Guarda los candidatos fuertes en `candidatos_fase1.json`.
**Cómo se usa:** no se toca a mano. Lo ejecuta `ranking-github-actions.yml` cuando tú lo lanzas o en sus horarios automáticos.

### 2. `fase2_scoring.py`
**Qué hace:** coge `candidatos_fase1.json` y le pone un score real (0-100) combinando: consenso real por reparto de categorías de analistas (strongBuy/buy/hold/sell/strongSell en % del total, con muestra mínima de 5 analistas — excluye candidatas con ≥30% recomendando vender, penaliza 10-29%, da empujón extra por unanimidad real en strong_buy puro o combinado con buy), dispersión entre analistas, momentum de 30 días, potencial de subida, tendencia técnica (SMA50/200), tendencia de recomendaciones a 3 meses, catalizador reciente de resultados (sorpresa >10% en 1-2 días), empujón por cotizar en euros (sin cambio de divisa), y **sentimiento de noticias** (Yahoo Finance + Google News, palabras clave en inglés/español, empujón con tope ±10). Descarta automáticamente las que publican resultados en menos de 5 días y las que están fuera de 0,05€-200€. Traduce el resumen del negocio al español. Genera `candidatos_rankeados.json`.
**Cómo se usa:** tampoco se toca a mano, corre junto al anterior en el mismo workflow.

### 3. `ranking-github-actions.yml`
**Qué hace:** el workflow de GitHub Actions que ejecuta 1 y 2 y sube los resultados a tu repo. Corre solo 7 veces al día (5:11, 7:11, 10:11, 12:11, 14:11, 16:11 y 18:11 hora española) y también cuando tú lo lanzas a mano. Al guardar, usa `merge` con estrategia `ours` (no `rebase`) para los archivos generados: como se regeneran enteros cada vez, si hay conflicto se queda con la versión recién creada sin atascarse.
**Cómo se usa:** se sube una vez al repo (carpeta `.github/workflows/`). Corre solo en sus horarios; si quieres datos frescos al momento, pestaña "Actions" → seleccionas el workflow → botón "Run workflow".

### 4. `scoring_viewer.html`
**Qué hace:** tu punto de entrada real. Trae el ranking del repo bajo demanda y muestra cada candidata con score, precio (en su moneda real — €, $, £, C$, A$, ¥... con aviso claro de si genera cambio de divisa o no), consenso, reparto real de analistas (como frase legible: "de 16 analistas: 31.2% compra fuerte · 0% vender"), potencial (con tooltip aclarando que es a ~12 meses vista según analistas, no garantizado), momentum/tendencia técnica/RSI en texto claro (bueno/malo/estable, no jerga técnica ni solo números), sentimiento de noticias con los titulares más relevantes, y badge de catalizador reciente de resultados. Cada término tiene un tooltip tocable. Incluye el panel de progreso de capital, enlace directo "Lanzar actualización en GitHub →" y el timestamp de la última ejecución, con ✅/❌ si falló.
**Cómo se usa:**
- La primera vez, escribe tu `usuario/repositorio` de GitHub y pulsa "Traer lista" (se guarda solo).
- Cada vez que quieras comprar: ábrelo, pulsa "Traer lista", decide.
- Cada vez que tu capital cambie: actualiza el número en "capital €" y pulsa "Guardar".

### 5. `simulador.html`
**Qué hace:** tu cuaderno de cuentas. Registro de operaciones (FIFO, con nombre e ISIN opcional), break-even automático, stop-loss inicial con 3 presets fijos (10%, 12,5%, 15% de pérdida máxima, comisiones incluidas), lista de posiciones abiertas clicable (ver cálculos o vender), últimas 5 operaciones en tarjetas clicables (tocar para desplegar editar/borrar), gráfico de ganancia neta acumulada, y resumen fiscal al final.
**Cómo se usa:** registras la compra en la sección 1 — el break-even y los 3 presets de stop-loss se calculan solos al confirmar. Para revisar o corregir operaciones antiguas, pulsa "Ver historial completo →".

### 5b. `historial.html`
**Qué hace:** página aparte (mismo repo, mismo localStorage) con el listado completo de todas las operaciones, en tarjetas clicables — tocar una despliega editar y borrar debajo, sin tablas anchas ni scroll horizontal. Al editar o borrar, recalcula el FIFO completo para que las cifras no queden descuadradas.
**Cómo se usa:** se llega desde el enlace "Ver historial completo →" en `simulador.html`, o directamente en `https://jmfc88.github.io/Finance/historial.html`.

### 5c. `simulador-datos.js`
**Qué hace:** lógica compartida entre `simulador.html` e `historial.html` (constantes de comisión/impuesto, acceso al ledger, cálculo de neto y recálculo FIFO). Además, si hay un repo + token de GitHub configurados (panel "Sincronización entre dispositivos" en `simulador.html`), cada guardado sube también `ledger.json` al repo, y cada carga lo trae de ahí primero — así el historial se ve igual en el móvil y en el PC. Sin token, sigue funcionando exactamente igual que antes (solo local, por dispositivo).
**Cómo se usa:** el cálculo no se toca a mano, ambas páginas lo cargan automáticamente. La sincronización se activa una vez desde el panel en `simulador.html` (repo + token de GitHub con permiso "Contents: Read and write" limitado a este repo).

### 6. `bot.py`
**Qué hace:** vigila el precio de tus posiciones abiertas y calcula el stop-loss/trailing stop dinámico (Trade Republic no tiene esta función). Cuando salta, te avisa por notificación al móvil vía ntfy.sh — esta es la única notificación que quieres, porque te protege de perder dinero.
**Cómo se usa:** corre en GitHub Actions en segundo plano mientras tengas posiciones abiertas. Tú solo reaccionas cuando te avisa: entras a Trade Republic y vendes.

### 7. `bot1_noticias.py`
**Qué hace:** analiza sentimiento de noticias (Yahoo Finance + Google News, palabras clave en inglés/español). **Ya no hace falta usarlo aparte** — esta misma lógica está fusionada dentro de `fase2_scoring.py` (v18+) y corre automáticamente para cada candidata del ranking.
**Cómo se usa:** se deja solo por si algún día quieres consultar noticias de un ticker que no esté en el ranking actual, fuera del flujo normal. No forma parte del workflow automático (y ya no necesita formar parte, porque su función ya está cubierta).

### 8. `bot-stoploss-github-actions.yml`
**Qué hace:** el workflow que ejecuta `bot.py` cada 30 minutos en horario de mercado US, automáticamente, sin que tengas que lanzarlo tú.
**Cómo se usa:** se sube una vez a `.github/workflows/` y corre solo mientras haya posiciones en `posiciones.json`.

### 9. `posiciones.json`
**Qué hace:** la lista de tus posiciones abiertas que vigila `bot.py` (ticker, precio de compra, acciones, % de trailing, stop-loss actual).
**Cómo se usa:** cuando compras, añades ahí la posición a mano (editor de GitHub, icono del lápiz). Empieza vacío: `[]`.

---

## Piezas descartadas (ya no forman parte del flujo)

| Archivo | Por qué se dejó de usar |
|---|---|
| `gestor_capital.py` | Decidía él solo cuántas posiciones abrir y repartía el capital. Preferiste decidir tú mismo tras ver el ranking. |
| `notificar_plan.py` | Notificación diaria del plan de compra — ya no quieres avisos de compra, solo de stop-loss. |
| `plan-diario-github-actions.yml` | Workflow que encadenaba screening + capital + notificación. Sustituido por `ranking-github-actions.yml`, más simple. |
| `capital.json` | Lo usaba `gestor_capital.py`. El capital ahora se gestiona a mano en el panel de progreso de `scoring_viewer.html`. |

---

## Despliegue en GitHub — tu repo real

**Repositorio:** `jmfc88/Finance` (público, necesario para que GitHub Pages sea gratis).

**Ya hecho:**
- ✅ Repo creado, archivos y workflows subidos
- ✅ Secreto `NTFY_TOPIC` creado, app ntfy instalada y suscrita
- ✅ GitHub Pages activo:
  - `https://jmfc88.github.io/Finance/scoring_viewer.html`
  - `https://jmfc88.github.io/Finance/simulador.html`
- ✅ Permisos de escritura de Actions corregidos (Read and write)
- ✅ Primer ranking generado y comprobado con éxito, universo dinámico funcionando

**Pendiente:**
- ⬜ Subir `historial.html` y `simulador-datos.js` (archivos nuevos, raíz del repo, junto a `simulador.html`)
- ⬜ Elegir la primera candidata real y comprarla en Trade Republic (empieza tu primera simulación)

---

## Orden de ejecución — primera simulación

1. ~~Sube al repo de GitHub `jmfc88/Finance` los archivos~~ ✅ ya hecho.
2. **Lanza el workflow a mano:** `jmfc88/Finance` → pestaña "Actions" → `Actualizar ranking de candidatas` → "Run workflow". Espera 1-2 min a que termine.
3. **Abre `scoring_viewer.html`** (vía GitHub Pages, una vez activado): escribe `jmfc88/Finance`, pulsa "Traer lista". Revisa el ranking y las descartadas.
4. **Mete tu capital (200€) en el panel de progreso** del visor y guarda, para ver tu nivel de partida.
5. **Elige tu candidata** del ranking, teniendo en cuenta precio (<200€, acción entera) y que no publique resultados pronto.
6. **Busca la empresa por NOMBRE en Trade Republic** (no pegues el ticker con sufijo del visor, ej. `.AX`, `.TO`) y **compra** (modo automático, 1€ comisión). ⚠️ Si el precio que ves en Trade Republic no se parece al del visor (ni con la conversión de divisa), es que la empresa cotiza en varias bolsas a la vez y TR usa un listado distinto al del visor — sigue siendo la misma empresa, simplemente confírmalo por el nombre antes de comprar.
7. **Registra la compra en `simulador.html`** (precio real, comisión, fecha).
8. **Añade la posición a `posiciones.json`** en GitHub (ticker, precio de compra, acciones, % de trailing) para que `bot.py` empiece a vigilarla.
9. **Cuando `bot.py` te avise por ntfy** de que el stop-loss ha saltado: vendes en Trade Republic.
10. **Registra la venta en `simulador.html`** (beneficio neto, 19% Hacienda, ledger FIFO).
11. **Actualiza tu capital** en el panel de progreso del visor.
12. **Pausa personal (~10 días)**, y vuelves al paso 2 cuando quieras.

---

## Control de versiones

Cada archivo activo tiene un comentario de versión en su primera línea (`VERSION: N (fecha) - qué cambió`). Cuando me mandes una captura de un archivo, mira esa primera línea y dímela si no se ve clara — así sé exactamente qué versión tienes desplegada sin tener que adivinar.

| Archivo | Versión actual |
|---|---|
| `fase1_screening.py` | 9 — relaja el filtro de beta para acciones en euros (sin cambio de divisa) |
| `fase2_scoring.py` | 18 — fusiona bot1_noticias.py, ahora automático para cada candidata |
| `ranking-github-actions.yml` | 11 — 7 ejecuciones automáticas al día (5:11 a 18:11) por si GitHub se salta alguna |
| `bot-stoploss-github-actions.yml` | 1 |
| `bot.py` | 1 |
| `bot1_noticias.py` | 3 — ya no hace falta usarlo, su lógica vive dentro de fase2_scoring.py |
| `scoring_viewer.html` | 18 — muestra sentimiento de noticias y titulares por tarjeta |
| `simulador.html` | 16 — panel de sincronización entre dispositivos vía GitHub (repo + token) |
| `historial.html` | 2 — tarjetas clicables con editar/borrar desplegable, sin scroll horizontal |
| `simulador-datos.js` | 2 — sincronización opcional: lee/escribe ledger.json en GitHub si hay repo+token |
| `posiciones.json` | 1 |

---

## Tu regla personal (no está en ningún archivo, es tuya)

Compras hoy → mantienes con stop-loss dinámico protegiendo ganancias → cuando vendes, pausa de ~10 días antes de volver a mirar el visor (para no operar en caliente, sin presión de notificaciones). Objetivo: escalar de 1 posición a 3-4 en 1 año, según el panel de progreso.

**Aviso fiscal importante:** si alguna vez vendes con **pérdida** y quieres recomprar el **mismo ticker**, espera **2 meses**, no 10 días — si no, Hacienda bloquea esa pérdida ese ejercicio (art. 33.5 LIRPF). Para tickers distintos, esto no aplica.
