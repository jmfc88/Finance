# Simulacion en paralelo

Actualizado: 2026-11-20 00:37 · dia 89 de ejecucion
Proxima revision de ponderacion en 1 dia.

- Operaciones cerradas: **375**
- Operaciones abiertas: 58

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 18 | 5% | +8.53 EUR |
| flojo | 165 | 44% | +1.31 EUR |
| plano | 19 | 5% | -1.76 EUR |
| perdida | 91 | 24% | -7.22 EUR |
| nefasta | 78 | 21% | -7.38 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 71 | -1.81% | 5/71 (7%) | 14/71 | 9 |
| 11-20 | 95 | -2.15% | 8/95 (8%) | 16/95 | 9 |
| 21-30 | 209 | -2.38% | 9/209 (4%) | 37/209 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 27 | -0.81% | -0.17% | **-0.63%** | 11/27 (41%) |
| 11-20 | 45 | -0.49% | -0.03% | **-0.46%** | 25/45 (56%) |
| 21-30 | 119 | -0.73% | -0.14% | **-0.59%** | 60/119 (50%) |

**En conjunto:** -0.68% de media frente a -0.12% del indice, una diferencia de **-0.57%**. 96 de 191 operaciones (50%) batieron a su indice.

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
| escalera + stop vol x2.5 | -1.17% | 197 | -230.24 EUR | 14/197 | -10.63 EUR |
| escalera + stop vol x3 | -1.23% | 192 | -236.10 EUR | 14/192 | -12.76 EUR |
| trailing pegado (3%) | -1.24% | 146 | -181.04 EUR | 19/146 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.21% | 375 | -829.90 EUR | 22/375 | -8.08 EUR |
| arranca antes (+3%) | -2.71% | 119 | -322.57 EUR | 15/119 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.75% | 110 | -302.19 EUR | 15/110 | -10.00 EUR |
| arranca despues (+8%) | -2.92% | 100 | -292.11 EUR | 15/100 | -10.00 EUR |
| trailing suelto (7%) | -3.33% | 100 | -332.96 EUR | 14/100 | -10.00 EUR |
| sin trailing, solo stop | -3.71% | 93 | -345.16 EUR | 12/93 | -10.00 EUR |
| stop corto (5%) | -4.68% | 225 | -1052.80 EUR | 14/225 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.21%**
- Aciertos (>= 5 EUR limpios): 22/375 (6%)
- Resultado acumulado ficticio: -829.90 EUR sobre 375 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 125 | -1.40 EUR | 5% | 33% |
| nota global | medio | 125 | -3.16 EUR | 5% | 53% |
| nota global | alto | 125 | -2.08 EUR | 8% | 50% |
| puesto en el ranking | bajo | 125 | -2.15 EUR | 6% | 48% |
| puesto en el ranking | medio | 125 | -2.27 EUR | 7% | 46% |
| puesto en el ranking | alto | 125 | -2.22 EUR | 4% | 41% |
| potencial hasta objetivo | bajo | 125 | -2.38 EUR | 6% | 44% |
| potencial hasta objetivo | medio | 125 | -2.43 EUR | 4% | 46% |
| potencial hasta objetivo | alto | 125 | -1.83 EUR | 8% | 45% |
| dispersion | bajo | 125 | -2.06 EUR | 7% | 47% |
| dispersion | medio | 125 | -2.66 EUR | 4% | 46% |
| dispersion | alto | 125 | -1.93 EUR | 6% | 42% |
| % compra fuerte | bajo | 118 | -2.43 EUR | 4% | 44% |
| % compra fuerte | medio | 118 | -1.71 EUR | 8% | 44% |
| % compra fuerte | alto | 119 | -2.54 EUR | 5% | 45% |
| momentum 30d | bajo | 125 | -2.17 EUR | 7% | 46% |
| momentum 30d | medio | 125 | -2.03 EUR | 7% | 44% |
| momentum 30d | alto | 125 | -2.44 EUR | 3% | 45% |
| fuerza relativa | bajo | 125 | -2.58 EUR | 6% | 52% |
| fuerza relativa | medio | 125 | -2.16 EUR | 6% | 43% |
| fuerza relativa | alto | 125 | -1.90 EUR | 5% | 40% |
| RSI | bajo | 125 | -2.35 EUR | 7% | 49% |
| RSI | medio | 125 | -2.38 EUR | 7% | 49% |
| RSI | alto | 125 | -1.91 EUR | 3% | 38% |
| volumen relativo | bajo | 119 | -1.67 EUR | 10% | 44% |
| volumen relativo | medio | 119 | -2.32 EUR | 3% | 43% |
| volumen relativo | alto | 120 | -2.52 EUR | 4% | 44% |
| volatilidad | bajo | 119 | -1.79 EUR | 8% | 39% |
| volatilidad | medio | 119 | -2.18 EUR | 7% | 44% |
| volatilidad | alto | 120 | -2.55 EUR | 3% | 48% |
| liquidez | bajo | 119 | -2.28 EUR | 6% | 45% |
| liquidez | medio | 119 | -2.24 EUR | 6% | 45% |
| liquidez | alto | 120 | -2.00 EUR | 6% | 40% |
| distancia max 52s | bajo | 119 | -1.72 EUR | 7% | 41% |
| distancia max 52s | medio | 119 | -2.04 EUR | 6% | 43% |
| distancia max 52s | alto | 120 | -2.75 EUR | 5% | 47% |
| consenso | buy | 264 | -2.20 EUR | 6% | 44% |
| consenso | strong_buy | 111 | -2.25 EUR | 6% | 49% |
| tendencia tecnica | alcista | 180 | -2.52 EUR | 6% | 47% |
| tendencia tecnica | mixta | 108 | -2.38 EUR | 5% | 47% |
| tendencia tecnica | bajista | 87 | -1.38 EUR | 8% | 39% |
| tendencia analistas | mejorando | 174 | -2.25 EUR | 5% | 45% |
| tendencia analistas | estable | 123 | -2.52 EUR | 7% | 50% |
| tendencia analistas | empeorando | 16 | -2.66 EUR | 6% | 56% |
| regimen de mercado | neutro | 180 | -2.00 EUR | 8% | 44% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 80 | -1.03 EUR | 5% | 28% |
| catalizador | con catalizador | 14 | -1.02 EUR | 7% | 29% |
| catalizador | sin catalizador | 361 | -2.26 EUR | 6% | 46% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| fuerza relativa | -2.58 | -1.90 | **+0.68 EUR** |
| potencial hasta objetivo | -2.38 | -1.83 | **+0.55 EUR** |
| RSI | -2.35 | -1.91 | **+0.44 EUR** |
| liquidez | -2.28 | -2.00 | **+0.29 EUR** |
| dispersion | -2.06 | -1.93 | **+0.13 EUR** |
| puesto en el ranking | -2.15 | -2.22 | **-0.06 EUR** |
| % compra fuerte | -2.43 | -2.54 | **-0.11 EUR** |
| momentum 30d | -2.17 | -2.44 | **-0.27 EUR** |
| nota global | -1.40 | -2.08 | **-0.68 EUR** |
| volatilidad | -1.79 | -2.55 | **-0.76 EUR** |
| volumen relativo | -1.67 | -2.52 | **-0.84 EUR** |
| distancia max 52s | -1.72 | -2.75 | **-1.04 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
