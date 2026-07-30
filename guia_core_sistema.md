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
**Qué hace:** reconstruye el universo de tickers en cada ejecución leyendo los componentes ACTUALES de S&P500, NASDAQ-100, DJIA, TSX60 (Canadá), IBEX35, DAX, MDAX, SDAX, TecDAX, FTSE100, CAC40, AEX, BEL20, PSI20, FTSE MIB, SMI, ATX, OMXS30 (Suecia), OMXC25 (Dinamarca), OMXH25 (Finlandia), Nikkei225 y EuroStoxx50 directamente de Wikipedia — ajustado al filtro real de índices y países de la app de Trade Republic (comprobado con capturas del usuario), con columnas y formato de ticker verificados a mano. También incluye ASX200 (Australia), IPC (México) e Ibovespa (Brasil) como intento — sus páginas de Wikipedia no parecen tener tabla de tickers limpia, así que probablemente no aporten candidatas hasta revisarlos con más calma, pero no rompen nada si fallan. Quedan fuera MSCI World y Russell 2000 (demasiados componentes, sin tabla fiable) y los sub-índices franceses CAC Large/Mid/NEXT/SMALL. Si un índice falla puntualmente, usa el último listado bueno conocido de ese índice. Luego busca en todo ese universo consenso de analistas de compra + beta alto. Guarda los candidatos fuertes en `candidatos_fase1.json`.
**Cómo se usa:** no se toca a mano. Lo ejecuta `ranking-github-actions.yml` cuando tú lo lanzas.

### 2. `fase2_scoring.py`
**Qué hace:** coge `candidatos_fase1.json` y le pone un score real (0-100) combinando consenso, dispersión entre analistas, momentum de 30 días y potencial de subida, más un empujón/freno menor por tendencia técnica (SMA50/200) y tendencia de recomendaciones de analistas a 3 meses. Descarta automáticamente las que publican resultados en menos de 5 días (riesgo de evento binario) y las que superan ~200€/acción. Traduce el resumen del negocio al español, acumulando frases completas hasta tener contexto real (normalmente 2 frases) en vez de un tope rígido de caracteres — nunca a medias, siempre con sentido propio. Genera `candidatos_rankeados.json`.
**Cómo se usa:** tampoco se toca a mano, corre junto al anterior en el mismo workflow.

### 3. `ranking-github-actions.yml`
**Qué hace:** el workflow de GitHub Actions que ejecuta 1 y 2 y sube los resultados a tu repo. Solo corre cuando tú lo lanzas — sin cron, sin coste automático. Al guardar, usa `merge` con estrategia `ours` (no `rebase`) para los archivos generados: como se regeneran enteros cada vez, si hay conflicto se queda con la versión recién creada sin atascarse.
**Cómo se usa:** se sube una vez al repo (carpeta `.github/workflows/`). Cuando quieras datos frescos: pestaña "Actions" en la app de GitHub → seleccionas el workflow → botón "Run workflow". Tarda unos minutos.

### 4. `scoring_viewer.html`
**Qué hace:** tu punto de entrada real. Trae el ranking del repo bajo demanda (tú decides cuándo mirarlo, nada empuja hacia ti) y muestra cada candidata con score, precio (en $ y su equivalente en €), consenso, potencial, momentum, dispersión, tendencia técnica (vs. su media de 50/200 sesiones), RSI y tendencia de analistas a 3 meses. Cada término tiene un tooltip tocable con su explicación. Incluye el panel de progreso de capital, un enlace directo "Lanzar actualización en GitHub →" (a la página de Actions, con tu propia sesión, sin claves guardadas) y el timestamp real de cuándo se lanzó la última ejecución (vía API pública de GitHub).
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
**Qué hace:** lógica compartida entre `simulador.html` e `historial.html` (constantes de comisión/impuesto, acceso al ledger, cálculo de neto y recálculo FIFO), para que las dos páginas usen exactamente el mismo cálculo y no se desincronicen.
**Cómo se usa:** no se toca a mano, ambas páginas lo cargan automáticamente.

### 6. `bot.py`
**Qué hace:** vigila el precio de tus posiciones abiertas y calcula el stop-loss/trailing stop dinámico (Trade Republic no tiene esta función). Cuando salta, te avisa por notificación al móvil vía ntfy.sh — esta es la única notificación que quieres, porque te protege de perder dinero.
**Cómo se usa:** corre en GitHub Actions en segundo plano mientras tengas posiciones abiertas. Tú solo reaccionas cuando te avisa: entras a Trade Republic y vendes.

### 7. `bot1_noticias.py`
**Qué hace:** analiza sentimiento de noticias solo de las candidatas que ya pasaron la fase 1, como capa extra de contexto antes de decidir.
**Cómo se usa:** complementario, se consulta si quieres una segunda opinión antes de comprar una candidata concreta.

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
| `fase1_screening.py` | 8 — columnas de TSX60/OMXC25 verificadas y corregidas, conversión espacio→guión |
| `fase2_scoring.py` | 9 — añade nombre completo e ISIN por candidata |
| `ranking-github-actions.yml` | 7 — resumen final con enlaces clicables a las dos webs |
| `bot-stoploss-github-actions.yml` | 1 |
| `bot.py` | 1 |
| `bot1_noticias.py` | 1 |
| `scoring_viewer.html` | 10 — enlace directo a GitHub Actions + timestamp real de lanzamiento |
| `simulador.html` | 15 — corrige recálculo al vender, Tipo vuelve solo a "Compra" tras cada registro |
| `historial.html` | 2 — tarjetas clicables con editar/borrar desplegable, sin scroll horizontal |
| `simulador-datos.js` | 1 — página nueva: lógica compartida entre simulador e historial |
| `posiciones.json` | 1 |

---

## Tu regla personal (no está en ningún archivo, es tuya)

Compras hoy → mantienes con stop-loss dinámico protegiendo ganancias → cuando vendes, pausa de ~10 días antes de volver a mirar el visor (para no operar en caliente, sin presión de notificaciones). Objetivo: escalar de 1 posición a 3-4 en 1 año, según el panel de progreso.

**Aviso fiscal importante:** si alguna vez vendes con **pérdida** y quieres recomprar el **mismo ticker**, espera **2 meses**, no 10 días — si no, Hacienda bloquea esa pérdida ese ejercicio (art. 33.5 LIRPF). Para tickers distintos, esto no aplica.
