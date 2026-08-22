# Guía Core — Sistema de Inversión Sistemático (Trade Republic, España)

*Última revisión completa: 22/08/2026. Este documento sustituye a todas las versiones parciales anteriores.*

---

## 1. Qué es esto y por qué existe

Un sistema de cribado, puntuación y aviso de acciones, construido para operar **desde el móvil, sin PC ni servidor propio**, con capital inicial reducido y reglas fiscales españolas incorporadas desde el diseño (no añadidas después).

**No es un robo-advisor ni un agente de IA.** No ejecuta operaciones — tú compras y vendes siempre a mano en Trade Republic. Es un **sistema de reglas deterministas** (código Python con umbrales fijos, sin modelo de IA corriendo dentro del pipeline): dado el mismo dato de entrada, siempre da el mismo resultado, y cada número se puede explicar. Eso es una ventaja de diseño, no una limitación — significa que puedes auditar por qué una candidata puntúa lo que puntúa.

**Principios de diseño que se han mantenido desde el principio:**
- **Sistemático sobre intuitivo:** toda decisión de compra pasa por el cribado → puntuación → profundización. Cero impulsos.
- **Coste cero mientras no se usa:** GitHub Actions (cómputo gratis) + GitHub Pages (hosting gratis) + ntfy.sh (notificaciones gratis, sin clave) + Yahoo Finance/Google News (datos gratis).
- **Fiscal desde el diseño:** ledger FIFO, comisiones reales, retenciones, regla de los 2 meses (art. 33.5 LIRPF) — no parches a posteriori.
- **Protección de capital antes que caza de ganancias:** es estructuralmente más fácil perder puntos fuerte que ganarlos fuerte (ver sección 4).
- **Disciplina de versiones:** cada archivo activo lleva `VERSION: N (fecha) - qué cambió` en su primera línea, sin excepción.

---

## 2. El flujo completo, de un vistazo

```
AUTOMÁTICO, 6 veces al día (4h/7h/10h/13h/16h/19h hora española):
  fase1_screening.py  →  candidatos_fase1.json
        (reconstruye el universo entero desde Wikipedia cada vez)
            ↓
  fase2_scoring.py    →  candidatos_rankeados.json
        (puntúa 0-100: consenso, dispersión, momentum, potencial,
         técnica, tendencia analistas, consenso real, catalizador,
         euros, noticias)
            ↓
  fase3_profundizar.py → mismo candidatos_rankeados.json, reordenado
        (segunda pasada de Google News SOLO sobre el top 25: confirma
         con etiqueta, o contradice restando puntos — nunca suma)
            ↓
  historial_scoring.json (se ACUMULA, nunca se sobreescribe)
        (snapshot con fecha de las 30 mejores, para poder comparar
         más adelante "qué pinta tenía esto cuando lo compré")

TÚ, cuando quieres comprar:
  1. Abres scoring_viewer.html → "Traer lista" → ves el ranking
  2. Buscas la empresa por NOMBRE en Trade Republic (no por ticker)
  3. Compras (1€ comisión, automático)
  4. Registras la compra en simulador.html (con comisión real,
     cambio de divisa si aplica)

MIENTRAS TIENES POSICIONES ABIERTAS:
  bot.py corre cada 15 min (horario de mercado US) y SOLO:
  - lee ledger.json y ajusta posiciones.json solo (ya no se edita a mano)
  - vigila el precio y te avisa por ntfy.sh cuando hace falta

CUANDO VENDES:
  registras la venta en simulador.html → FIFO, neto, resumen fiscal
  actualizas tu capital en el panel de progreso de scoring_viewer.html
  pausa personal ~10 días → vuelves al paso 1
```

---

## 3. Cada pieza, en detalle

### 3.1 `fase1_screening.py` (v11)

**Qué hace:** reconstruye el universo de tickers **desde cero en cada ejecución**, leyendo los componentes actuales de Wikipedia de: S&P500, NASDAQ-100, DJIA, TSX60, IBEX35, DAX, MDAX, SDAX, TecDAX, FTSE100, CAC40, AEX, BEL20, PSI20, FTSE MIB, SMI, ATX, OMXS30, OMXC25, OMXH25, Nikkei225, ASX200 y EuroStoxx50. Si un índice falla puntualmente, usa el último listado bueno conocido (guardado en `universo_por_indice.json`).

**Filtro de calidad:** consenso de analistas de compra + beta alto (movimiento fuerte) — **excepto en acciones que cotizan en euros** (IBEX35, DAX, CAC40, AEX, BEL20, PSI20, FTSE MIB, ATX, EuroStoxx50), donde basta el consenso sin exigir beta alto, porque no generan cambio de divisa y así entran también empresas consolidadas con un catalizador puntual.

**Bugs de tickers corregidos por el camino** (detectados con datos reales, no en teoría):
- Acciones de doble clase con punto propio (`BT.A`, `CCL.B`, `CTC.A`, `GIB.A`, `BIP.UN`) generaban tickers rotos de doble punto al añadir el sufijo de bolsa (`BT.A` + `.L` = `BT.A.L`, no existe). Ahora el punto interno se convierte a guion antes de añadir el sufijo (`BT-A.L`, correcto).
- Empresas que cotizan en varias bolsas a la vez (ej. ArcelorMittal aparece en la tabla del CAC40 como `MT.AS` porque cotiza de verdad en Ámsterdam) ya no se llevan un segundo sufijo encima.
- URL de NASDAQ100 apuntaba al artículo general del índice, no al listado de empresas — corregida.
- `IPC_MEXICO` quitado: no existe tabla de constituyentes en Wikipedia para el S&P/BMV IPC, llevaba fallando desde el principio sin remedio posible.
- Red de seguridad genérica: si ninguno de los nombres de columna configurados coincide con lo que trae Wikipedia esa vez, busca cualquier columna que contenga "ticker"/"symbol"/"code" — así futuros cambios de formato de Wikipedia no rompen el índice entero sin avisar.
- Logger de `yfinance` silenciado para tickers que genuinamente no existen (ruido inevitable, ya se descartan solos sin romper nada).

**Descarta:** precio fuera de 0,05€-200€, resultados en menos de 5 días (riesgo binario).

**Cómo se usa:** no se toca a mano. Lo ejecuta `ranking-github-actions.yml`.

---

### 3.2 `fase2_scoring.py` (v30) — el corazón del sistema

Coge `candidatos_fase1.json` y le pone una nota de **0 a 100 de verdad** (ver sección 4 para el desglose completo de puntos). Traduce el resumen del negocio al español. Genera `candidatos_rankeados.json`.

**Componentes de la puntuación** (ver tabla completa en sección 4):
1. Consenso de Yahoo (etiqueta `strong_buy`/`buy`/`hold`/`underperform`/`sell`)
2. Dispersión del precio objetivo entre analistas
3. Momentum de 30 días, con distinción de si un movimiento fuerte **sigue activo ahora mismo o ya se ha calmado** (usa `momentum_5d`)
4. Potencial de subida hasta el precio objetivo medio
5. Tendencia técnica (SMA50 vs SMA200)
6. Tendencia de recomendaciones de analistas a 3 meses
7. **Consenso real** por reparto de categorías — el factor más elaborado, por bloques de 20% desde el 60% de consenso combinado, pesado por convicción real (% compra fuerte) y tamaño de muestra
8. Catalizador de resultados recientes (sorpresa >10%, ventana de 0 a 4 días)
9. Empujón por cotizar en euros (sin cambio de divisa)
10. Sentimiento de noticias (Yahoo Finance + Google News, español **e inglés**)

**Momentum — la lógica de "activo vs. calmado":** un movimiento fuerte (>+25% o <-15% en 30 días) no se trata igual si sigue ocurriendo ahora mismo que si ya pasó. Se compara contra `momentum_5d` (los últimos 5 días):
- Cayendo fuerte y **sigue** cayendo → 0 puntos (cuchillo cayendo de verdad, mal momento)
- Cayendo fuerte pero **ya se ha estabilizado** → puntos altos (posible rebote — lo normal es que tienda a recuperar su precio habitual, salvo mala noticia detrás)
- Subiendo fuerte y **sigue** disparándose → 0 puntos (perseguirlo es el peor punto de entrada)
- Subiendo fuerte pero **ya se ha calmado** → puntos moderados (sigue "cara", pero se puede valorar con calma)

**Consenso real — filtros y lógica:**
- Muestra mínima de 5 analistas; con menos, se marca "muestra insuficiente" y no puntúa (ni bonus ni malus) — Yahoo a veces da tablas incompletas para cotizaciones duales.
- ≥30% de los analistas recomienda vender → **candidata excluida del listado entero**, por mucho que la etiqueta agregada de Yahoo diga `strong_buy`.
- 20-29% vender → malus. 10-19% vender → malus menor.
- 60% o más de consenso combinado (compra fuerte + compra normal) → empujón por bloques de 20% (60-79% / 80-99% / 100%), multiplicado por cuánta convicción real hay (% compra fuerte específicamente, no solo "compra") y por el tamaño de la muestra (confianza plena a partir de 10 analistas — con menos, un mismo % es menos fiable estadísticamente y se reduce proporcionalmente).

**Sentimiento de noticias — mejoras acumuladas:**
- Busca en **español e inglés** a la vez (Google News ya no se fuerza a un solo idioma) y combina resultados sin duplicar.
- **Detecta negaciones:** "los resultados **no** batieron expectativas" ya no cuenta como positivo — mira si hay una negación en los caracteres previos a la palabra clave y, si la hay, invierte el signo.
- Vocabulario ampliado en español: `supera`, `superó`, `batió`, `decepciona`, etc., además del inglés original.
- Doble peso a prensa económica de referencia cuando aparece: Reuters, Bloomberg, Financial Times, WSJ, The Economist, Barron's — sin elegir nosotros qué fuentes salen (eso lo decide Google News solo según quién cubra la noticia), solo pesando más su opinión cuando sí aparecen.
- Lista negra de fuentes que son fichas de datos, no periodismo (TradingView, Simply Wall St, StockAnalysis, MarketBeat, GuruFocus, Insider Monkey, Barchart, TradingKey, eToro) más un filtro de patrón para cotizaciones en bruto tipo `TICKER|Nombre|Precio:X|Variación%:Y`.

**Corrección crítica de escala (19/08/2026):** el score podía superar 100 en la práctica (visto: Lottomatica dio 104,3) porque la suma de los máximos de los 10 factores daba **155**, no 100. Se reescaló todo proporcionalmente (factor 100/155 = 0,6452) para que el máximo teórico absoluto sea exactamente 100 — ninguna lógica ni umbral cambió, solo los números de puntos. Verificado matemáticamente: el mejor caso posible en los 10 factores a la vez da 100,0 exacto, ni un decimal más.

**Corrección de coma flotante (19/08/2026):** catalizador/euros/noticias se sumaban después del redondeo interno sin volver a redondear el resultado final, generando números como `64.10000000000001` en vez de `64.1`. Corregido con un redondeo final.

**Desempate:** si dos candidatas empatan exactamente en score, se ordena por nombre de empresa A-Z (antes el orden entre empatadas no estaba definido).

**Descarta:** resultados en menos de 5 días, precio fuera de 0,05€-200€, ≥30% de analistas recomendando vender.

**Cómo se usa:** no se toca a mano, corre junto a fase1 en el mismo workflow.

---

### 3.3 `fase3_profundizar.py` (v10)

**Qué hace:** segunda pasada **automática**, solo sobre las mejores 25 candidatas del ranking que ya generó fase2 (no las 150+, sería demasiado lento). Hace búsquedas de Google News más específicas ("analistas", "previsión", en español e inglés) para verificar si lo que dice la prensa **confirma o contradice** la puntuación que ya tiene la candidata.

**La regla, importante:**
- **Confirma** (tono neutro o positivo) → solo se marca **"✓ verificado"**, cero puntos añadidos. Una confirmación no es motivo para subir el score.
- **Contradice** (encuentra algo claramente negativo pese al score alto) → **resta puntos**, con tope de **-40** y multiplicador ×4 por titular negativo — a propósito un malus grande, porque una contradicción real es peligrosa y tiene que poder hundir de verdad la posición de una candidata, sin llegar a excluirla del listado por completo.

**Filtros de calidad añadidos tras detectar problemas reales:**
- Deduplicación entre las dos búsquedas (antes el mismo artículo podía contarse dos veces).
- Filtro de relevancia: descarta titulares que no mencionan de verdad el nombre de la empresa (detectado con un artículo de Bloomberg sobre bancos europeos que no tenía nada que ver con la candidata en cuestión, colado por coincidencia floja de la búsqueda).
- Reddit se evaluó y se descartó a propósito: señal ruidosa y manipulable en small-caps (el tipo de empresa que este sistema encuentra), y su API ya no es de acceso libre (requiere aprobación manual de Reddit, 2-4 semanas de espera).

**Además, guarda `historial_scoring.json`:** un snapshot con fecha/hora de las 30 mejores candidatas de cada pasada, que se **acumula** (nunca se sobreescribe). Es la base para poder responder en el futuro "¿las candidatas con score alto de verdad rindieron mejor?" cruzando este histórico contra tus compras/ventas reales — el sistema nunca se ha validado contra datos históricos, esto es el primer paso real hacia esa validación. Empezó a guardar desde el 06/08/2026 en adelante; no hay datos retroactivos de antes de esa fecha.

**Cómo se usa:** no se toca a mano, corre como tercer paso del mismo workflow.

---

### 3.4 `ranking-github-actions.yml` (v13)

El workflow de GitHub Actions que ejecuta fase1 → fase2 → fase3 y sube los resultados. Corre **6 veces al día** (4h, 7h, 10h, 13h, 16h, 19h hora española) y también cuando lo lanzas a mano (Actions → "Run workflow"). Al guardar, usa `merge` con estrategia `ours` para los archivos generados (se regeneran enteros cada vez, así que en caso de conflicto se queda con la versión recién creada sin atascarse). Sube también `historial_scoring.json`.

---

### 3.5 `scoring_viewer.html` (v23)

Tu punto de entrada real para decidir qué comprar. Trae el ranking bajo demanda y muestra cada candidata con:
- Score, precio en su moneda real (con aviso de cambio de divisa)
- Consenso de Yahoo y **reparto real** de analistas en frase legible ("de 16 analistas: 31,2% compra fuerte · 0% vender")
- Potencial (tooltip aclarando que es la opinión de analistas a ~12 meses vista, no una garantía)
- Momentum, tendencia técnica y RSI en **texto claro**, no jerga técnica ni solo números — y el momentum distingue si un movimiento fuerte sigue activo o ya se ha calmado
- Sentimiento de noticias con los titulares más relevantes
- Badge de "✓ verificado" o "⚠ contradice la puntuación" de la Fase 3
- Badge de catalizador de resultados recientes
- Muestra solo las **primeras 25 por defecto** (las que la Fase 3 profundiza de verdad), con botón "Ver X candidatas más" para el resto sin volver a pedir el archivo

Cada término tiene un tooltip tocable. Incluye el panel de progreso de capital, enlace directo "Lanzar actualización en GitHub →", y el timestamp de la última ejecución con ✅/❌ si falló.

**Cómo se usa:** escribe tu `usuario/repositorio` una vez (se guarda solo). Cada vez que quieras comprar, ábrelo y pulsa "Traer lista".

---

### 3.6 El cuaderno de cuentas: `simulador.html` (v24), `historial.html` (v6), `simulador-datos.js` (v8)

**`simulador.html`** es tu registro de operaciones (FIFO), con:
- **Comisión real por operación**, no una constante fija asumida — configurable UNA vez en "Ajustes avanzados" (comisión de compra/venta por defecto), precarga el campo del registro sin tener que escribirla cada vez. Si Trade Republic cambia su tarifa algún día, se ajusta ahí una vez y afecta solo a operaciones nuevas; las ya guardadas mantienen su comisión real histórica.
- **Coste de cambio de divisa** estimado y configurable (por defecto 1,2%, ajustable) para operaciones que no son en euros — Trade Republic no lo publica como línea aparte, va escondido dentro del margen de ejecución.
- Break-even y stop-loss inicial con **3 presets**: **-7,5% [CUIDADO]**, **-10% [PIENSA]**, **-12,5% [VENDE]** — alineados con los mismos niveles que vigila `bot.py`, así ves en el simulador exactamente a qué precio saltará cada aviso antes de comprar.
- Tarjetas de operaciones con **desglose completo**: precio × acciones + / − comisión = total, y el neto en verde/rojo si es una venta cerrada.
- Lista de posiciones abiertas clicable (ver cálculos o vender), gráfico de ganancia neta acumulada, y resumen fiscal (ganancia neta, comisiones pagadas de verdad, ahorro 10% intocable, reinvertible 90%, **operaciones cerradas** — cuenta ventas/trades completados, no filas totales del ledger).
- Panel de "Sincronización entre dispositivos": con un token de GitHub configurado, cada operación se guarda también en `ledger.json` del repo. Al cargar, **fusiona** lo local con lo de GitHub (nunca uno borra al otro) — antes, si un dispositivo guardaba algo local sin token puesto, una recarga con GitHub desactualizado podía borrar esos datos; ahora se combinan sin duplicar, y si hacía falta, sube la fusión de vuelta. Botón "Cargar datos ahora" para forzar la sincronización manualmente.

**`historial.html`** es el listado completo de todas las operaciones (mismo `ledger.json`), en tarjetas clicables con editar/borrar, mismo desglose de comisión/total que el simulador.

**`simulador-datos.js`** es la lógica compartida entre los dos: constantes de comisión histórica (respaldo fijo para operaciones antiguas sin el dato guardado), funciones de comisión/coste FX configurables, cálculo de neto con comisión real, fusión de ledgers, recálculo FIFO completo.

**Cómo se usa:** registras la compra en la sección 1 nada más comprarla en Trade Republic. Break-even y los 3 presets de stop-loss se calculan solos al confirmar.

---

### 3.7 El vigilante: `bot.py` (v10) + `bot-stoploss-github-actions.yml` (v2)

Corre **cada 15 minutos**, en horario de mercado de EE.UU. (13-21h UTC, lunes a viernes). No hace falta editar nada a mano para que funcione — solo que la sincronización del simulador esté activa (repo + token), para que `ledger.json` exista en el repo.

**Antes de vigilar, se auto-reconcilia con tu ledger real:** lee `ledger.json` y ajusta `posiciones.json` solo — añade las posiciones nuevas que detecte abiertas (con un stop-loss de referencia automático, preset 12,5%, y te avisa para que lo revises si no era el nivel que querías) y quita las que ya hayas vendido del todo. **Ya no hace falta editar `posiciones.json` a mano** cada vez que compras o vendes.

**Corrección crítica de divisa (05/08/2026):** Yahoo Finance da el precio en la divisa real de cotización (ej. CAD para tickers `.TO`), no en euros. El bot comparaba ese precio directamente contra el punto de equilibrio en euros — unidades distintas, la comparación no tenía sentido matemático, y por eso las alertas nunca saltaban bien en posiciones con cambio de divisa. Ahora se detecta la divisa real (de la propia info de Yahoo, no solo el checkbox) y se convierte con un tipo de cambio en vivo antes de cualquier comparación.

**Tres métodos de stop-loss que conviven a la vez**, quedándose siempre con el más protector (más alto):
1. **Trailing continuo:** baja del máximo precio alcanzado, según `trailing_pct`.
2. **Escalones de +5% de beneficio** desde el punto de equilibrio: cada vez que el precio supera un nuevo escalón de +5% sobre el break-even, avisa la ganancia (`[GANANCIA]`) Y sube el stop-loss ORIGINAL por ese mismo múltiplo — pasados suficientes escalones, el peor caso deja de ser perder dinero y pasa a ser ganar algo seguro.
3. **Avisos escalonados de pérdida**, antes del stop-loss real: **-7,5% `[CUIDADO]`** (aviso suave), **-10% `[PIENSA]`** (piensa si vender), **-12,5% `[VENDE]`** (el de siempre, urgente). Cada nivel avisa una sola vez.

**Método 4 — cierre y apertura de mercado (20/08/2026):** si al **cerrar el mercado** (usando `marketState` de Yahoo, así no hay que programar a mano el horario de cada bolsa) sigues por debajo del -7,5%, avisa `[CIERRE MERCADO]` y programa un **único recordatorio** para la siguiente apertura (`[RECORDATORIO]`), para estar al loro apenas vuelva a cotizar.

**Opción B (11/08/2026):** si Yahoo Finance falla o no da precio, prueba con Stooq (gratis, sin clave) como respaldo — pero **solo para tickers de EE.UU. sin sufijo** (el mapeo de tickers entre Yahoo y Stooq para otras bolsas no es lo bastante fiable como para confiar en él a ciegas).

**Notificaciones en texto plano, sin emojis** (rompían el envío por completo — las cabeceras HTTP normales solo admiten Latin-1, y `💰📈🔴🎯` daban un `UnicodeEncodeError` que tumbaba todo el script; cambiado también al formato JSON de ntfy, que sí los admitiría, pero se quitaron de todas formas por seguridad extra): `[GANANCIA]`, `[SUBE STOP-LOSS]`, `[CUIDADO]`, `[PIENSA]` no urgentes; `[VENDE]` y `[CIERRE MERCADO]` urgentes.

**Cómo se usa:** tú reaccionas a las notificaciones — subes el stop-loss en Trade Republic cuando avisa que subió, y vendes cuando avisa que saltó. `bot-stoploss-github-actions.yml` lo ejecuta solo, sin que lo lances tú.

---

### 3.8 `bot1_noticias.py` (v3) — ya no hace falta usarlo

Analizaba sentimiento de noticias por separado. Su lógica está **fusionada dentro de `fase2_scoring.py`** desde la v18, y corre automáticamente para cada candidata del ranking. Se deja en el repo solo por si algún día quieres consultar noticias de un ticker que no esté en el ranking actual, fuera del flujo normal.

---

### 3.9 `posiciones.json` — ya no se edita a mano

Antes había que añadir cada posición nueva manualmente en GitHub al comprar, y quitarla al vender — eso generó varios fallos reales (posiciones fantasma que ya no existían, posiciones nuevas sin vigilar). Desde que `bot.py` se auto-reconcilia con `ledger.json` (v7+), **este archivo se mantiene solo**. Solo hace falta tocarlo a mano si el stop-loss de referencia automático (preset 12,5%) no es el nivel que de verdad querías para una posición nueva recién detectada.

---

## 4. El sistema de puntuación — referencia completa

El máximo teórico absoluto es **exactamente 100** (verificado matemáticamente, ver sección 3.2). En la práctica, casi ninguna candidata se acerca a ese máximo porque requeriría que los 10 factores coincidieran en su mejor valor simultáneamente.

| Factor | Máximo | Cómo se gana |
|---|---|---|
| Consenso Yahoo | +9,7 | Etiqueta `strong_buy` (resto: buy +6,5, hold +1,9, underperform -6,5, sell -12,9) |
| Dispersión precio objetivo | +16,1 | Dispersión <30% entre precio objetivo alto y bajo |
| Momentum 30 días | +12,9 | Rango normal (-15% a +25%); +9,7 si cayó fuerte pero ya se estabilizó; +3,2 si subió fuerte pero ya se calmó; 0 si el movimiento fuerte sigue activo |
| Potencial de subida | +16,1 | Tope alcanzado con 75% de subida esperada al precio objetivo |
| Tendencia técnica | +3,2 | Precio por encima de SMA50 y SMA200 |
| Tendencia analistas (3m) | +6,5 | Recomendaciones mejorando mes a mes |
| **Consenso real** | **+16,1** | Bloques de 20% desde 60% de consenso combinado, pesado por convicción (% compra fuerte, tope en 75%) y tamaño de muestra (confianza plena a partir de 10 analistas) |
| Catalizador de resultados | +7,7 | Sorpresa >10% en beneficios, hace 0-4 días |
| Cotiza en euros | +5,2 | Sin cambio de divisa (fijo) |
| Sentimiento de noticias | +6,5 | Tono positivo confirmado en Yahoo + Google News (español e inglés) |
| **Fase 3 — contradice** | **-40** | Malus aparte, fuera del presupuesto de 100 — si la profundización encuentra algo negativo pese al score alto |

**La asimetría es deliberada:** es más fácil perder puntos fuerte (Fase 3 hasta -40, consenso real hasta -9,7 en malus) que ganarlos fuerte (máximo individual +16,1). El sistema está construido para proteger capital antes que perseguir ganancias.

---

## 5. Reglas personales y fiscales (España)

- **Acciones enteras, sin fracciones** — más simple para la declaración de la renta.
- **Rango de precio:** excluye penny stocks por debajo de 0,05€ y acciones por encima de ~200€/acción.
- **Bróker:** Trade Republic — 1€/operación, regulado por CNMV, genera certificado fiscal español, sin API pública ni trailing stop nativo (de ahí todo el sistema de vigilancia externo).
- **Escalado de capital:** 200€=1 posición, 500€=2, 1000€=3, 2000€=4, 4000€=5.
- **Pausa personal tras vender:** ~10 días antes de evaluar nuevas candidatas (disciplina, no obligación fiscal).
- **Regla del 10%/90%:** al cerrar con ganancia, 10% del beneficio neto va a ahorro intocable; el 90% restante es reinvertible.
- **⚠️ Regla de los 2 meses (art. 33.5 LIRPF):** si vendes con **pérdida** y recompras el **mismo ticker** dentro de 2 meses, Hacienda bloquea la deducción de esa pérdida ese ejercicio. Un ticker distinto no se ve afectado. (Esto es distinto de la pausa personal de ~10 días, que es solo disciplina.)
- **Dividendos:** retención del 19% automática vía Trade Republic. Extranjeros van a la casilla 0588 (máximo 15% deducible); nacionales a la casilla 0029.
- **Búsqueda en Trade Republic siempre por NOMBRE de empresa, no por ticker con sufijo** — empresas con cotización múltiple (ej. mineras en Toronto/NYSE/ASX a la vez) pueden aparecer con un ticker distinto al que usa el visor. El ISIN que muestra el visor (de Yahoo Finance) es orientativo; el que cuenta de verdad para el simulador y la declaración es el que enseña Trade Republic al comprar.

---

## 6. Aprendizajes clave del desarrollo

- **Turbos/warrants no sirven para este enfoque** — barreras de knock-out y coste de financiación los hacen inadecuados para "comprar y dejar"; ETCs y acciones mineras son el instrumento correcto para exposición a materias primas.
- **El riesgo de resultados es binario** — el sistema excluye a propósito candidatas con resultados en menos de 5 días; el valor está en pillar el catalizador *después* de la buena noticia confirmada, no en especular antes.
- **El contexto del momentum importa más que el número solo** — un desplome ya estabilizado es una posible entrada de recuperación, no un cuchillo cayendo; el sistema ahora distingue esto de verdad, no solo en la puntuación sino también en el texto que ves.
- **El empujón por cotizar en euros es real** — sin riesgo de cambio de divisa, las acciones en euros son estructuralmente preferibles con capital pequeño.
- **Una sola fuente de datos (Yahoo Finance) es un punto único de fallo** — si Yahoo cambia su API o bloquea `yfinance` más fuerte, todo el pipeline se cae de golpe. Solo hay respaldo parcial (Stooq, solo para EE.UU. sin sufijo) en el bot de vigilancia, no en el cribado completo.
- **El sistema nunca se ha validado contra datos históricos** — las reglas de puntuación suenan razonables, pero nadie ha comprobado todavía si un score alto de verdad predice mejor rendimiento a 30-90 días. `historial_scoring.json` es el primer paso hacia poder responder esto, pero necesita tiempo para acumular una muestra real.
- **Fuentes de datos aparcadas por poco fiables o poco viables:** Reddit (ruidoso y manipulable en small-caps, además de fricción de acceso desde el cambio de su API en 2023); Simply Wall St, Investing.com, eToro, TradingView (no son periodismo, son fichas de datos); Financial Times/Bloomberg/WSJ completos (paywall, pero sus titulares en Google News sí se usan).

---

## 7. Historial de versiones — estado verificado el 22/08/2026

| Archivo | Versión | Cambio más reciente |
|---|---|---|
| `fase1_screening.py` | 11 | Corrige NASDAQ100, quita IPC_MEXICO, red de seguridad genérica de columnas |
| `fase2_scoring.py` | 30 | Corrige ruido de coma flotante, desempate alfabético |
| `fase3_profundizar.py` | 10 | Desempate alfabético también aquí |
| `ranking-github-actions.yml` | 13 | Sube también `historial_scoring.json` |
| `bot-stoploss-github-actions.yml` | 2 | De cada 30 a cada 15 minutos |
| `bot.py` | 10 | Aviso al cierre de mercado, recordatorio a la apertura |
| `bot1_noticias.py` | 3 | Ya no hace falta usarlo, fusionado en fase2 |
| `scoring_viewer.html` | 23 | Momentum distingue activo vs. calmado, top-25 con botón "ver más" |
| `simulador.html` | 24 | Tarjetas con desglose completo: precio × acciones +/− comisión = total |
| `historial.html` | 6 | Mismo desglose completo en las tarjetas |
| `simulador-datos.js` | 8 | `comisionEfectivaOp()`/`totalOperacion()` compartidas |
| `posiciones.json` | — | Se auto-gestiona; contenía SCYR.MC (cerrada 21/08, pérdida real -18,10€ según Trade Republic) |

---

## 8. Pendientes / próximos pasos

- Registrar en `simulador.html` la venta de SCYR.MC (ya ejecutada en Trade Republic el 21/08).
- Dejar pasar tiempo suficiente para que `historial_scoring.json` acumule una muestra real, y entonces construir el cruce automático contra el ledger de compras/ventas para validar si el score predice algo de verdad.
- Sin plan de backtesting formal todavía — es la carencia más grande señalada hasta ahora.
