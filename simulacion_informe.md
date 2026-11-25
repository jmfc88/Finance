# Simulacion en paralelo

Actualizado: 2026-11-25 04:13 · dia 94 de ejecucion
Proxima revision de ponderacion en 11 dias.

- Operaciones cerradas: **398**
- Operaciones abiertas: 55

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 18 | 5% | +8.53 EUR |
| flojo | 169 | 42% | +1.32 EUR |
| plano | 19 | 5% | -1.76 EUR |
| perdida | 102 | 26% | -7.28 EUR |
| nefasta | 86 | 22% | -7.45 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 79 | -2.15% | 5/79 (6%) | 15/79 | 9 |
| 11-20 | 103 | -2.52% | 8/103 (8%) | 17/103 | 9 |
| 21-30 | 216 | -2.52% | 9/216 (4%) | 37/216 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 34 | -1.60% | -0.75% | **-0.86%** | 12/34 (35%) |
| 11-20 | 53 | -1.46% | -0.72% | **-0.74%** | 26/53 (49%) |
| 21-30 | 125 | -1.01% | -0.28% | **-0.73%** | 60/125 (48%) |

**En conjunto:** -1.22% de media frente a -0.46% del indice, una diferencia de **-0.76%**. 98 de 212 operaciones (46%) batieron a su indice.

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
| escalera + stop vol x4 | -0.77% | 190 | -145.62 EUR | 16/190 | -10.91 EUR |
| trailing pegado (3%) | -1.43% | 153 | -218.80 EUR | 20/153 | -10.00 EUR |
| escalera + stop vol x2.5 | -1.51% | 219 | -330.52 EUR | 14/219 | -10.63 EUR |
| escalera + stop vol x3 | -1.63% | 214 | -349.03 EUR | 14/214 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.45% | 398 | -973.75 EUR | 22/398 | -8.08 EUR |
| arranca antes (+3%) | -2.91% | 125 | -364.16 EUR | 15/125 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.96% | 116 | -343.78 EUR | 15/116 | -10.00 EUR |
| arranca despues (+8%) | -3.15% | 106 | -333.70 EUR | 15/106 | -10.00 EUR |
| trailing suelto (7%) | -3.60% | 105 | -377.90 EUR | 14/105 | -10.00 EUR |
| sin trailing, solo stop | -3.98% | 98 | -390.10 EUR | 12/98 | -10.00 EUR |
| stop corto (5%) | -4.82% | 245 | -1180.39 EUR | 14/245 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.45%**
- Aciertos (>= 5 EUR limpios): 22/398 (6%)
- Resultado acumulado ficticio: -973.75 EUR sobre 398 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 132 | -1.62 EUR | 5% | 35% |
| nota global | medio | 132 | -3.17 EUR | 5% | 54% |
| nota global | alto | 134 | -2.56 EUR | 7% | 53% |
| puesto en el ranking | bajo | 132 | -2.33 EUR | 6% | 50% |
| puesto en el ranking | medio | 132 | -2.78 EUR | 6% | 50% |
| puesto en el ranking | alto | 134 | -2.23 EUR | 4% | 42% |
| potencial hasta objetivo | bajo | 132 | -2.65 EUR | 5% | 47% |
| potencial hasta objetivo | medio | 132 | -2.69 EUR | 4% | 48% |
| potencial hasta objetivo | alto | 134 | -2.01 EUR | 7% | 46% |
| dispersion | bajo | 132 | -2.46 EUR | 6% | 51% |
| dispersion | medio | 132 | -2.69 EUR | 5% | 47% |
| dispersion | alto | 134 | -2.19 EUR | 6% | 44% |
| % compra fuerte | bajo | 125 | -2.75 EUR | 4% | 47% |
| % compra fuerte | medio | 125 | -1.92 EUR | 7% | 46% |
| % compra fuerte | alto | 125 | -2.64 EUR | 5% | 46% |
| momentum 30d | bajo | 132 | -2.28 EUR | 7% | 47% |
| momentum 30d | medio | 132 | -2.24 EUR | 7% | 46% |
| momentum 30d | alto | 134 | -2.81 EUR | 3% | 49% |
| fuerza relativa | bajo | 132 | -2.67 EUR | 6% | 52% |
| fuerza relativa | medio | 132 | -2.39 EUR | 6% | 45% |
| fuerza relativa | alto | 134 | -2.29 EUR | 4% | 44% |
| RSI | bajo | 132 | -2.22 EUR | 7% | 47% |
| RSI | medio | 132 | -2.68 EUR | 7% | 52% |
| RSI | alto | 134 | -2.43 EUR | 3% | 43% |
| volumen relativo | bajo | 127 | -2.08 EUR | 9% | 47% |
| volumen relativo | medio | 127 | -2.28 EUR | 3% | 43% |
| volumen relativo | alto | 127 | -2.90 EUR | 4% | 48% |
| volatilidad | bajo | 127 | -1.87 EUR | 7% | 40% |
| volatilidad | medio | 127 | -2.33 EUR | 6% | 46% |
| volatilidad | alto | 127 | -3.06 EUR | 3% | 52% |
| liquidez | bajo | 127 | -2.58 EUR | 6% | 48% |
| liquidez | medio | 127 | -2.42 EUR | 6% | 46% |
| liquidez | alto | 127 | -2.26 EUR | 6% | 43% |
| distancia max 52s | bajo | 127 | -1.90 EUR | 6% | 43% |
| distancia max 52s | medio | 127 | -2.26 EUR | 6% | 45% |
| distancia max 52s | alto | 127 | -3.09 EUR | 5% | 50% |
| consenso | buy | 281 | -2.46 EUR | 5% | 46% |
| consenso | strong_buy | 117 | -2.42 EUR | 6% | 50% |
| tendencia tecnica | alcista | 193 | -2.78 EUR | 5% | 49% |
| tendencia tecnica | mixta | 114 | -2.68 EUR | 4% | 50% |
| tendencia tecnica | bajista | 91 | -1.45 EUR | 8% | 40% |
| tendencia analistas | mejorando | 183 | -2.42 EUR | 5% | 46% |
| tendencia analistas | estable | 132 | -2.81 EUR | 7% | 52% |
| tendencia analistas | empeorando | 16 | -2.66 EUR | 6% | 56% |
| regimen de mercado | neutro | 182 | -2.05 EUR | 8% | 45% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 101 | -2.11 EUR | 4% | 39% |
| catalizador | con catalizador | 16 | -1.90 EUR | 6% | 38% |
| catalizador | sin catalizador | 382 | -2.47 EUR | 5% | 48% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.65 | -2.01 | **+0.64 EUR** |
| fuerza relativa | -2.67 | -2.29 | **+0.38 EUR** |
| liquidez | -2.58 | -2.26 | **+0.32 EUR** |
| dispersion | -2.46 | -2.19 | **+0.27 EUR** |
| % compra fuerte | -2.75 | -2.64 | **+0.11 EUR** |
| puesto en el ranking | -2.33 | -2.23 | **+0.11 EUR** |
| RSI | -2.22 | -2.43 | **-0.21 EUR** |
| momentum 30d | -2.28 | -2.81 | **-0.53 EUR** |
| volumen relativo | -2.08 | -2.90 | **-0.82 EUR** |
| nota global | -1.62 | -2.56 | **-0.94 EUR** |
| volatilidad | -1.87 | -3.06 | **-1.18 EUR** |
| distancia max 52s | -1.90 | -3.09 | **-1.19 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
