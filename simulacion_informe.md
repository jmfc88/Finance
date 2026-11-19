# Simulacion en paralelo

Actualizado: 2026-11-19 18:17 · dia 88 de ejecucion
Proxima revision de ponderacion en 2 dias.

- Operaciones cerradas: **374**
- Operaciones abiertas: 57

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 18 | 5% | +8.53 EUR |
| flojo | 165 | 44% | +1.31 EUR |
| plano | 19 | 5% | -1.76 EUR |
| perdida | 91 | 24% | -7.22 EUR |
| nefasta | 77 | 21% | -7.37 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 70 | -1.72% | 5/70 (7%) | 14/70 | 9 |
| 11-20 | 95 | -2.15% | 8/95 (8%) | 16/95 | 9 |
| 21-30 | 209 | -2.38% | 9/209 (4%) | 37/209 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 26 | -0.53% | +0.03% | **-0.56%** | 11/26 (42%) |
| 11-20 | 45 | -0.49% | -0.03% | **-0.46%** | 25/45 (56%) |
| 21-30 | 119 | -0.73% | -0.14% | **-0.59%** | 60/119 (50%) |

**En conjunto:** -0.64% de media frente a -0.09% del indice, una diferencia de **-0.55%**. 96 de 190 operaciones (51%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 57 operaciones, media -0.38%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.48% | 177 | -84.97 EUR | 16/177 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.14% | 196 | -224.13 EUR | 14/196 | -10.63 EUR |
| escalera + stop vol x3 | -1.20% | 191 | -228.77 EUR | 14/191 | -12.76 EUR |
| trailing pegado (3%) | -1.24% | 146 | -181.04 EUR | 19/146 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.20% | 374 | -821.82 EUR | 22/374 | -8.08 EUR |
| arranca antes (+3%) | -2.71% | 119 | -322.57 EUR | 15/119 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.75% | 110 | -302.19 EUR | 15/110 | -10.00 EUR |
| arranca despues (+8%) | -2.92% | 100 | -292.11 EUR | 15/100 | -10.00 EUR |
| trailing suelto (7%) | -3.33% | 100 | -332.96 EUR | 14/100 | -10.00 EUR |
| sin trailing, solo stop | -3.71% | 93 | -345.16 EUR | 12/93 | -10.00 EUR |
| stop corto (5%) | -4.67% | 224 | -1045.80 EUR | 14/224 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.20%**
- Aciertos (>= 5 EUR limpios): 22/374 (6%)
- Resultado acumulado ficticio: -821.82 EUR sobre 374 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 124 | -1.42 EUR | 5% | 33% |
| nota global | medio | 124 | -3.05 EUR | 5% | 52% |
| nota global | alto | 126 | -2.13 EUR | 8% | 50% |
| puesto en el ranking | bajo | 124 | -2.11 EUR | 6% | 48% |
| puesto en el ranking | medio | 124 | -2.42 EUR | 6% | 47% |
| puesto en el ranking | alto | 126 | -2.07 EUR | 5% | 40% |
| potencial hasta objetivo | bajo | 124 | -2.41 EUR | 6% | 44% |
| potencial hasta objetivo | medio | 124 | -2.38 EUR | 4% | 46% |
| potencial hasta objetivo | alto | 126 | -1.81 EUR | 8% | 44% |
| dispersion | bajo | 124 | -2.08 EUR | 7% | 48% |
| dispersion | medio | 124 | -2.63 EUR | 4% | 46% |
| dispersion | alto | 126 | -1.89 EUR | 6% | 41% |
| % compra fuerte | bajo | 118 | -2.43 EUR | 4% | 44% |
| % compra fuerte | medio | 118 | -1.71 EUR | 8% | 44% |
| % compra fuerte | alto | 118 | -2.49 EUR | 5% | 45% |
| momentum 30d | bajo | 124 | -2.20 EUR | 7% | 47% |
| momentum 30d | medio | 124 | -2.05 EUR | 7% | 44% |
| momentum 30d | alto | 126 | -2.34 EUR | 3% | 44% |
| fuerza relativa | bajo | 124 | -2.61 EUR | 6% | 52% |
| fuerza relativa | medio | 124 | -2.09 EUR | 6% | 43% |
| fuerza relativa | alto | 126 | -1.90 EUR | 5% | 40% |
| RSI | bajo | 124 | -2.30 EUR | 7% | 48% |
| RSI | medio | 124 | -2.50 EUR | 6% | 49% |
| RSI | alto | 126 | -1.80 EUR | 4% | 37% |
| volumen relativo | bajo | 119 | -1.67 EUR | 10% | 44% |
| volumen relativo | medio | 119 | -2.24 EUR | 3% | 42% |
| volumen relativo | alto | 119 | -2.55 EUR | 4% | 45% |
| volatilidad | bajo | 119 | -1.79 EUR | 8% | 39% |
| volatilidad | medio | 119 | -2.18 EUR | 7% | 44% |
| volatilidad | alto | 119 | -2.50 EUR | 3% | 47% |
| liquidez | bajo | 119 | -2.28 EUR | 6% | 45% |
| liquidez | medio | 119 | -2.24 EUR | 6% | 45% |
| liquidez | alto | 119 | -1.95 EUR | 6% | 39% |
| distancia max 52s | bajo | 119 | -1.72 EUR | 7% | 41% |
| distancia max 52s | medio | 119 | -1.96 EUR | 6% | 42% |
| distancia max 52s | alto | 119 | -2.79 EUR | 5% | 47% |
| consenso | buy | 263 | -2.17 EUR | 6% | 43% |
| consenso | strong_buy | 111 | -2.25 EUR | 6% | 49% |
| tendencia tecnica | alcista | 179 | -2.49 EUR | 6% | 46% |
| tendencia tecnica | mixta | 108 | -2.38 EUR | 5% | 47% |
| tendencia tecnica | bajista | 87 | -1.38 EUR | 8% | 39% |
| tendencia analistas | mejorando | 173 | -2.21 EUR | 5% | 45% |
| tendencia analistas | estable | 123 | -2.52 EUR | 7% | 50% |
| tendencia analistas | empeorando | 16 | -2.66 EUR | 6% | 56% |
| regimen de mercado | neutro | 179 | -1.97 EUR | 8% | 44% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 80 | -1.03 EUR | 5% | 28% |
| catalizador | con catalizador | 13 | -0.47 EUR | 8% | 23% |
| catalizador | sin catalizador | 361 | -2.26 EUR | 6% | 46% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| fuerza relativa | -2.61 | -1.90 | **+0.71 EUR** |
| potencial hasta objetivo | -2.41 | -1.81 | **+0.60 EUR** |
| RSI | -2.30 | -1.80 | **+0.51 EUR** |
| liquidez | -2.28 | -1.95 | **+0.34 EUR** |
| dispersion | -2.08 | -1.89 | **+0.19 EUR** |
| puesto en el ranking | -2.11 | -2.07 | **+0.03 EUR** |
| % compra fuerte | -2.43 | -2.49 | **-0.06 EUR** |
| momentum 30d | -2.20 | -2.34 | **-0.14 EUR** |
| nota global | -1.42 | -2.13 | **-0.71 EUR** |
| volatilidad | -1.79 | -2.50 | **-0.71 EUR** |
| volumen relativo | -1.67 | -2.55 | **-0.87 EUR** |
| distancia max 52s | -1.72 | -2.79 | **-1.07 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
