# Simulacion en paralelo

Actualizado: 2026-11-23 17:58 · dia 92 de ejecucion
**Revision nº6 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **394**
- Operaciones abiertas: 55

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 18 | 5% | +8.53 EUR |
| flojo | 167 | 42% | +1.32 EUR |
| plano | 19 | 5% | -1.76 EUR |
| perdida | 102 | 26% | -7.28 EUR |
| nefasta | 84 | 21% | -7.43 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 77 | -2.11% | 5/77 (6%) | 15/77 | 9 |
| 11-20 | 103 | -2.52% | 8/103 (8%) | 17/103 | 9 |
| 21-30 | 214 | -2.51% | 9/214 (4%) | 37/214 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 33 | -1.68% | -0.80% | **-0.88%** | 12/33 (36%) |
| 11-20 | 53 | -1.46% | -0.72% | **-0.74%** | 26/53 (49%) |
| 21-30 | 124 | -1.03% | -0.29% | **-0.74%** | 60/124 (48%) |

**En conjunto:** -1.24% de media frente a -0.48% del indice, una diferencia de **-0.76%**. 98 de 210 operaciones (47%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 58 operaciones, media -0.45%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.74% | 187 | -139.14 EUR | 16/187 | -10.91 EUR |
| trailing pegado (3%) | -1.32% | 151 | -198.80 EUR | 20/151 | -10.00 EUR |
| escalera + stop vol x2.5 | -1.49% | 215 | -320.07 EUR | 14/215 | -10.63 EUR |
| escalera + stop vol x3 | -1.60% | 210 | -336.10 EUR | 14/210 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.44% | 394 | -959.59 EUR | 22/394 | -8.08 EUR |
| arranca antes (+3%) | -2.80% | 123 | -344.16 EUR | 15/123 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.84% | 114 | -323.78 EUR | 15/114 | -10.00 EUR |
| arranca despues (+8%) | -3.02% | 104 | -313.70 EUR | 15/104 | -10.00 EUR |
| trailing suelto (7%) | -3.47% | 103 | -357.90 EUR | 14/103 | -10.00 EUR |
| sin trailing, solo stop | -3.86% | 96 | -370.10 EUR | 12/96 | -10.00 EUR |
| stop corto (5%) | -4.80% | 243 | -1166.39 EUR | 14/243 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.44%**
- Aciertos (>= 5 EUR limpios): 22/394 (6%)
- Resultado acumulado ficticio: -959.59 EUR sobre 394 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 131 | -1.64 EUR | 5% | 35% |
| nota global | medio | 131 | -3.13 EUR | 5% | 53% |
| nota global | alto | 132 | -2.54 EUR | 7% | 53% |
| puesto en el ranking | bajo | 131 | -2.31 EUR | 6% | 50% |
| puesto en el ranking | medio | 131 | -2.79 EUR | 6% | 50% |
| puesto en el ranking | alto | 132 | -2.21 EUR | 5% | 42% |
| potencial hasta objetivo | bajo | 131 | -2.64 EUR | 5% | 47% |
| potencial hasta objetivo | medio | 131 | -2.68 EUR | 4% | 49% |
| potencial hasta objetivo | alto | 132 | -1.98 EUR | 8% | 46% |
| dispersion | bajo | 131 | -2.40 EUR | 6% | 50% |
| dispersion | medio | 131 | -2.67 EUR | 5% | 47% |
| dispersion | alto | 132 | -2.24 EUR | 6% | 45% |
| % compra fuerte | bajo | 123 | -2.66 EUR | 4% | 46% |
| % compra fuerte | medio | 123 | -1.90 EUR | 7% | 46% |
| % compra fuerte | alto | 125 | -2.71 EUR | 5% | 47% |
| momentum 30d | bajo | 131 | -2.30 EUR | 7% | 47% |
| momentum 30d | medio | 131 | -2.20 EUR | 7% | 46% |
| momentum 30d | alto | 132 | -2.80 EUR | 3% | 48% |
| fuerza relativa | bajo | 131 | -2.69 EUR | 6% | 53% |
| fuerza relativa | medio | 131 | -2.34 EUR | 6% | 45% |
| fuerza relativa | alto | 132 | -2.27 EUR | 5% | 44% |
| RSI | bajo | 131 | -2.25 EUR | 7% | 47% |
| RSI | medio | 131 | -2.57 EUR | 7% | 50% |
| RSI | alto | 132 | -2.49 EUR | 3% | 44% |
| volumen relativo | bajo | 125 | -2.05 EUR | 10% | 47% |
| volumen relativo | medio | 125 | -2.33 EUR | 3% | 43% |
| volumen relativo | alto | 127 | -2.83 EUR | 4% | 47% |
| volatilidad | bajo | 125 | -1.94 EUR | 7% | 41% |
| volatilidad | medio | 125 | -2.18 EUR | 6% | 44% |
| volatilidad | alto | 127 | -3.09 EUR | 3% | 53% |
| liquidez | bajo | 125 | -2.65 EUR | 6% | 49% |
| liquidez | medio | 125 | -2.31 EUR | 6% | 46% |
| liquidez | alto | 127 | -2.26 EUR | 6% | 43% |
| distancia max 52s | bajo | 125 | -1.88 EUR | 6% | 42% |
| distancia max 52s | medio | 125 | -2.24 EUR | 6% | 45% |
| distancia max 52s | alto | 127 | -3.09 EUR | 5% | 50% |
| consenso | buy | 277 | -2.44 EUR | 5% | 46% |
| consenso | strong_buy | 117 | -2.42 EUR | 6% | 50% |
| tendencia tecnica | alcista | 191 | -2.77 EUR | 5% | 49% |
| tendencia tecnica | mixta | 114 | -2.68 EUR | 4% | 50% |
| tendencia tecnica | bajista | 89 | -1.40 EUR | 8% | 39% |
| tendencia analistas | mejorando | 181 | -2.41 EUR | 5% | 46% |
| tendencia analistas | estable | 130 | -2.80 EUR | 7% | 52% |
| tendencia analistas | empeorando | 16 | -2.66 EUR | 6% | 56% |
| regimen de mercado | neutro | 182 | -2.05 EUR | 8% | 45% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 97 | -2.06 EUR | 4% | 38% |
| catalizador | con catalizador | 16 | -1.90 EUR | 6% | 38% |
| catalizador | sin catalizador | 378 | -2.46 EUR | 6% | 48% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.64 | -1.98 | **+0.66 EUR** |
| fuerza relativa | -2.69 | -2.27 | **+0.42 EUR** |
| liquidez | -2.65 | -2.26 | **+0.39 EUR** |
| dispersion | -2.40 | -2.24 | **+0.16 EUR** |
| puesto en el ranking | -2.31 | -2.21 | **+0.11 EUR** |
| % compra fuerte | -2.66 | -2.71 | **-0.05 EUR** |
| RSI | -2.25 | -2.49 | **-0.24 EUR** |
| momentum 30d | -2.30 | -2.80 | **-0.50 EUR** |
| volumen relativo | -2.05 | -2.83 | **-0.77 EUR** |
| nota global | -1.64 | -2.54 | **-0.90 EUR** |
| volatilidad | -1.94 | -3.09 | **-1.14 EUR** |
| distancia max 52s | -1.88 | -3.09 | **-1.22 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
