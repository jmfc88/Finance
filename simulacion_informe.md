# Simulacion en paralelo

Actualizado: 2026-10-30 01:02 · dia 68 de ejecucion
Proxima revision de ponderacion en 7 dias.

- Operaciones cerradas: **247**
- Operaciones abiertas: 64

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 2% | +16.71 EUR |
| beneficio | 5 | 2% | +7.59 EUR |
| flojo | 85 | 34% | +1.32 EUR |
| plano | 17 | 7% | -1.72 EUR |
| perdida | 81 | 33% | -7.24 EUR |
| nefasta | 55 | 22% | -7.09 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 51 | -2.19% | 3/51 (6%) | 9/51 | 10 |
| 11-20 | 63 | -3.09% | 3/63 (5%) | 7/63 | 9 |
| 21-30 | 133 | -3.63% | 3/133 (2%) | 11/133 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 8 | -1.61% | -1.57% | **-0.04%** | 3/8 (38%) |
| 11-20 | 17 | -2.64% | -1.08% | **-1.56%** | 9/17 (53%) |
| 21-30 | 44 | -1.82% | -0.99% | **-0.83%** | 24/44 (55%) |

**En conjunto:** -2.00% de media frente a -1.08% del indice, una diferencia de **-0.92%**. 36 de 69 operaciones (52%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 44 operaciones, media -1.51%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -1.91% | 62 | -118.25 EUR | 4/62 | -10.34 EUR |
| escalera + stop vol x2.5 | -2.31% | 74 | -171.14 EUR | 3/74 | -10.63 EUR |
| trailing pegado (3%) | -2.37% | 89 | -210.95 EUR | 7/89 | -10.00 EUR |
| escalera + stop vol x3 | -2.71% | 73 | -197.86 EUR | 3/73 | -12.76 EUR |
| LA REAL (escalera 25/08) | -3.19% | 247 | -788.73 EUR | 9/247 | -8.08 EUR |
| arranca antes (+3%) | -3.39% | 78 | -264.37 EUR | 6/78 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.61% | 72 | -259.65 EUR | 6/72 | -10.00 EUR |
| arranca despues (+8%) | -3.63% | 71 | -257.59 EUR | 6/71 | -10.00 EUR |
| trailing suelto (7%) | -4.10% | 69 | -282.90 EUR | 5/69 | -10.00 EUR |
| sin trailing, solo stop | -4.38% | 67 | -293.68 EUR | 4/67 | -10.00 EUR |
| stop corto (5%) | -5.28% | 165 | -871.16 EUR | 6/165 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.19%**
- Aciertos (>= 5 EUR limpios): 9/247 (4%)
- Resultado acumulado ficticio: -788.73 EUR sobre 247 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 82 | -3.11 EUR | 2% | 49% |
| nota global | medio | 82 | -3.87 EUR | 2% | 61% |
| nota global | alto | 83 | -2.61 EUR | 6% | 55% |
| puesto en el ranking | bajo | 82 | -2.45 EUR | 6% | 55% |
| puesto en el ranking | medio | 82 | -3.80 EUR | 2% | 57% |
| puesto en el ranking | alto | 83 | -3.32 EUR | 2% | 53% |
| potencial hasta objetivo | bajo | 82 | -3.30 EUR | 5% | 55% |
| potencial hasta objetivo | medio | 82 | -3.66 EUR | 2% | 60% |
| potencial hasta objetivo | alto | 83 | -2.62 EUR | 4% | 51% |
| dispersion | bajo | 82 | -2.63 EUR | 6% | 54% |
| dispersion | medio | 82 | -3.71 EUR | 4% | 60% |
| dispersion | alto | 83 | -3.24 EUR | 1% | 52% |
| % compra fuerte | bajo | 76 | -3.58 EUR | 3% | 57% |
| % compra fuerte | medio | 76 | -2.82 EUR | 4% | 55% |
| % compra fuerte | alto | 77 | -3.42 EUR | 3% | 53% |
| momentum 30d | bajo | 82 | -3.62 EUR | 4% | 57% |
| momentum 30d | medio | 82 | -2.90 EUR | 2% | 51% |
| momentum 30d | alto | 83 | -3.06 EUR | 5% | 57% |
| fuerza relativa | bajo | 82 | -3.60 EUR | 2% | 57% |
| fuerza relativa | medio | 82 | -3.00 EUR | 2% | 51% |
| fuerza relativa | alto | 83 | -2.99 EUR | 6% | 57% |
| RSI | bajo | 82 | -2.79 EUR | 5% | 50% |
| RSI | medio | 82 | -3.19 EUR | 4% | 56% |
| RSI | alto | 83 | -3.59 EUR | 2% | 59% |
| volumen relativo | bajo | 76 | -2.81 EUR | 8% | 57% |
| volumen relativo | medio | 76 | -3.24 EUR | 0% | 50% |
| volumen relativo | alto | 78 | -3.54 EUR | 3% | 54% |
| volatilidad | bajo | 76 | -2.96 EUR | 4% | 50% |
| volatilidad | medio | 76 | -3.77 EUR | 1% | 55% |
| volatilidad | alto | 78 | -2.88 EUR | 5% | 55% |
| liquidez | bajo | 76 | -3.20 EUR | 3% | 53% |
| liquidez | medio | 76 | -3.22 EUR | 4% | 55% |
| liquidez | alto | 78 | -3.18 EUR | 4% | 53% |
| distancia max 52s | bajo | 76 | -2.99 EUR | 3% | 50% |
| distancia max 52s | medio | 76 | -2.73 EUR | 4% | 53% |
| distancia max 52s | alto | 78 | -3.86 EUR | 4% | 58% |
| consenso | buy | 172 | -3.26 EUR | 3% | 54% |
| consenso | strong_buy | 75 | -3.03 EUR | 4% | 57% |
| tendencia tecnica | alcista | 114 | -3.34 EUR | 4% | 57% |
| tendencia tecnica | mixta | 68 | -3.32 EUR | 3% | 56% |
| tendencia tecnica | bajista | 65 | -2.81 EUR | 3% | 51% |
| tendencia analistas | mejorando | 120 | -3.19 EUR | 2% | 53% |
| tendencia analistas | estable | 78 | -3.59 EUR | 5% | 62% |
| tendencia analistas | empeorando | 10 | -5.01 EUR | 0% | 80% |
| regimen de mercado | neutro | 131 | -2.94 EUR | 4% | 50% |
| regimen de mercado | favorable | 111 | -3.44 EUR | 4% | 60% |
| regimen de mercado | adverso | 5 | -4.45 EUR | 0% | 60% |
| catalizador | sin catalizador | 246 | -3.17 EUR | 4% | 55% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.30 | -2.62 | **+0.68 EUR** |
| fuerza relativa | -3.60 | -2.99 | **+0.61 EUR** |
| momentum 30d | -3.62 | -3.06 | **+0.56 EUR** |
| nota global | -3.11 | -2.61 | **+0.50 EUR** |
| % compra fuerte | -3.58 | -3.42 | **+0.16 EUR** |
| volatilidad | -2.96 | -2.88 | **+0.08 EUR** |
| liquidez | -3.20 | -3.18 | **+0.02 EUR** |
| dispersion | -2.63 | -3.24 | **-0.61 EUR** |
| volumen relativo | -2.81 | -3.54 | **-0.73 EUR** |
| RSI | -2.79 | -3.59 | **-0.80 EUR** |
| puesto en el ranking | -2.45 | -3.32 | **-0.87 EUR** |
| distancia max 52s | -2.99 | -3.86 | **-0.87 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
