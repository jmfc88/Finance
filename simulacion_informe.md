# Simulacion en paralelo

Actualizado: 2026-10-29 07:01 · dia 67 de ejecucion
Proxima revision de ponderacion en 8 dias.

- Operaciones cerradas: **240**
- Operaciones abiertas: 66

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 1% | +16.90 EUR |
| beneficio | 5 | 2% | +7.59 EUR |
| flojo | 81 | 34% | +1.33 EUR |
| plano | 16 | 7% | -1.75 EUR |
| perdida | 80 | 33% | -7.23 EUR |
| nefasta | 55 | 23% | -7.09 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 51 | -2.19% | 3/51 (6%) | 9/51 | 10 |
| 11-20 | 62 | -3.01% | 3/62 (5%) | 7/62 | 9 |
| 21-30 | 127 | -3.95% | 2/127 (2%) | 10/127 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 8 | -1.61% | -1.57% | **-0.04%** | 3/8 (38%) |
| 11-20 | 16 | -2.30% | -1.16% | **-1.14%** | 9/16 (56%) |
| 21-30 | 38 | -2.61% | -1.23% | **-1.38%** | 21/38 (55%) |

**En conjunto:** -2.40% de media frente a -1.25% del indice, una diferencia de **-1.15%**. 33 de 62 operaciones (53%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 42 operaciones, media -1.93%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -2.40% | 55 | -132.08 EUR | 3/55 | -10.34 EUR |
| trailing pegado (3%) | -2.54% | 85 | -216.11 EUR | 6/85 | -10.00 EUR |
| escalera + stop vol x2.5 | -2.73% | 67 | -183.19 EUR | 2/67 | -10.63 EUR |
| escalera + stop vol x3 | -3.18% | 66 | -209.91 EUR | 2/66 | -12.76 EUR |
| LA REAL (escalera 25/08) | -3.33% | 240 | -799.61 EUR | 8/240 | -8.08 EUR |
| arranca antes (+3%) | -3.59% | 75 | -269.33 EUR | 5/75 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.83% | 69 | -264.61 EUR | 5/69 | -10.00 EUR |
| arranca despues (+8%) | -3.86% | 68 | -262.55 EUR | 5/68 | -10.00 EUR |
| trailing suelto (7%) | -4.36% | 66 | -287.86 EUR | 4/66 | -10.00 EUR |
| sin trailing, solo stop | -4.67% | 64 | -298.64 EUR | 3/64 | -10.00 EUR |
| stop corto (5%) | -5.43% | 162 | -879.12 EUR | 5/162 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.33%**
- Aciertos (>= 5 EUR limpios): 8/240 (3%)
- Resultado acumulado ficticio: -799.61 EUR sobre 240 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 80 | -3.44 EUR | 1% | 50% |
| nota global | medio | 80 | -3.96 EUR | 2% | 64% |
| nota global | alto | 80 | -2.60 EUR | 6% | 55% |
| puesto en el ranking | bajo | 80 | -2.31 EUR | 6% | 54% |
| puesto en el ranking | medio | 80 | -4.01 EUR | 2% | 60% |
| puesto en el ranking | alto | 80 | -3.67 EUR | 1% | 55% |
| potencial hasta objetivo | bajo | 80 | -3.60 EUR | 4% | 56% |
| potencial hasta objetivo | medio | 80 | -3.55 EUR | 2% | 59% |
| potencial hasta objetivo | alto | 80 | -2.84 EUR | 4% | 54% |
| dispersion | bajo | 80 | -2.61 EUR | 6% | 54% |
| dispersion | medio | 80 | -4.10 EUR | 2% | 62% |
| dispersion | alto | 80 | -3.28 EUR | 1% | 52% |
| % compra fuerte | bajo | 74 | -3.94 EUR | 1% | 58% |
| % compra fuerte | medio | 74 | -2.77 EUR | 4% | 55% |
| % compra fuerte | alto | 75 | -3.51 EUR | 3% | 55% |
| momentum 30d | bajo | 80 | -3.56 EUR | 4% | 57% |
| momentum 30d | medio | 80 | -3.11 EUR | 2% | 54% |
| momentum 30d | alto | 80 | -3.32 EUR | 4% | 57% |
| fuerza relativa | bajo | 80 | -3.69 EUR | 2% | 59% |
| fuerza relativa | medio | 80 | -3.21 EUR | 2% | 54% |
| fuerza relativa | alto | 80 | -3.10 EUR | 5% | 56% |
| RSI | bajo | 80 | -2.98 EUR | 5% | 52% |
| RSI | medio | 80 | -3.37 EUR | 2% | 56% |
| RSI | alto | 80 | -3.65 EUR | 2% | 60% |
| volumen relativo | bajo | 74 | -3.09 EUR | 7% | 58% |
| volumen relativo | medio | 74 | -3.35 EUR | 0% | 51% |
| volumen relativo | alto | 75 | -3.61 EUR | 3% | 55% |
| volatilidad | bajo | 74 | -3.25 EUR | 3% | 51% |
| volatilidad | medio | 74 | -3.55 EUR | 3% | 55% |
| volatilidad | alto | 75 | -3.26 EUR | 4% | 57% |
| liquidez | bajo | 74 | -3.32 EUR | 3% | 54% |
| liquidez | medio | 74 | -3.18 EUR | 4% | 55% |
| liquidez | alto | 75 | -3.55 EUR | 3% | 55% |
| distancia max 52s | bajo | 74 | -2.98 EUR | 4% | 53% |
| distancia max 52s | medio | 74 | -3.04 EUR | 3% | 54% |
| distancia max 52s | alto | 75 | -4.02 EUR | 3% | 57% |
| consenso | buy | 168 | -3.44 EUR | 3% | 55% |
| consenso | strong_buy | 72 | -3.07 EUR | 4% | 58% |
| tendencia tecnica | alcista | 113 | -3.51 EUR | 4% | 58% |
| tendencia tecnica | mixta | 67 | -3.38 EUR | 3% | 57% |
| tendencia tecnica | bajista | 60 | -2.94 EUR | 3% | 53% |
| tendencia analistas | mejorando | 117 | -3.30 EUR | 3% | 55% |
| tendencia analistas | estable | 76 | -3.68 EUR | 5% | 63% |
| tendencia analistas | empeorando | 10 | -5.01 EUR | 0% | 80% |
| regimen de mercado | neutro | 127 | -3.09 EUR | 3% | 51% |
| regimen de mercado | favorable | 110 | -3.48 EUR | 4% | 61% |
| catalizador | sin catalizador | 239 | -3.31 EUR | 3% | 56% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -3.44 | -2.60 | **+0.83 EUR** |
| potencial hasta objetivo | -3.60 | -2.84 | **+0.75 EUR** |
| fuerza relativa | -3.69 | -3.10 | **+0.59 EUR** |
| % compra fuerte | -3.94 | -3.51 | **+0.43 EUR** |
| momentum 30d | -3.56 | -3.32 | **+0.24 EUR** |
| volatilidad | -3.25 | -3.26 | **-0.01 EUR** |
| liquidez | -3.32 | -3.55 | **-0.23 EUR** |
| volumen relativo | -3.09 | -3.61 | **-0.51 EUR** |
| RSI | -2.98 | -3.65 | **-0.67 EUR** |
| dispersion | -2.61 | -3.28 | **-0.68 EUR** |
| distancia max 52s | -2.98 | -4.02 | **-1.04 EUR** |
| puesto en el ranking | -2.31 | -3.67 | **-1.36 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
