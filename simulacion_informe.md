# Simulacion en paralelo

Actualizado: 2026-10-27 15:22 · dia 65 de ejecucion
Proxima revision de ponderacion en 10 dias.

- Operaciones cerradas: **238**
- Operaciones abiertas: 60

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 1% | +16.90 EUR |
| beneficio | 5 | 2% | +7.59 EUR |
| flojo | 80 | 34% | +1.35 EUR |
| plano | 16 | 7% | -1.75 EUR |
| perdida | 80 | 34% | -7.23 EUR |
| nefasta | 54 | 23% | -7.07 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 51 | -2.19% | 3/51 (6%) | 9/51 | 10 |
| 11-20 | 62 | -3.01% | 3/62 (5%) | 7/62 | 9 |
| 21-30 | 125 | -3.95% | 2/125 (2%) | 10/125 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 8 | -1.61% | -1.57% | **-0.04%** | 3/8 (38%) |
| 11-20 | 16 | -2.30% | -1.16% | **-1.14%** | 9/16 (56%) |
| 21-30 | 37 | -2.68% | -1.22% | **-1.47%** | 20/37 (54%) |

**En conjunto:** -2.44% de media frente a -1.25% del indice, una diferencia de **-1.19%**. 32 de 61 operaciones (52%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 41 operaciones, media -1.98%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -2.35% | 54 | -127.03 EUR | 3/54 | -10.34 EUR |
| trailing pegado (3%) | -2.48% | 83 | -206.17 EUR | 6/83 | -10.00 EUR |
| escalera + stop vol x2.5 | -2.59% | 65 | -168.52 EUR | 2/65 | -7.93 EUR |
| escalera + stop vol x3 | -3.02% | 64 | -193.11 EUR | 2/64 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.33% | 238 | -791.59 EUR | 8/238 | -8.08 EUR |
| arranca antes (+3%) | -3.55% | 73 | -259.39 EUR | 5/73 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.80% | 67 | -254.67 EUR | 5/67 | -10.00 EUR |
| arranca despues (+8%) | -3.83% | 66 | -252.61 EUR | 5/66 | -10.00 EUR |
| trailing suelto (7%) | -4.34% | 64 | -277.92 EUR | 4/64 | -10.00 EUR |
| sin trailing, solo stop | -4.66% | 62 | -288.70 EUR | 3/62 | -10.00 EUR |
| stop corto (5%) | -5.45% | 160 | -872.18 EUR | 5/160 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.33%**
- Aciertos (>= 5 EUR limpios): 8/238 (3%)
- Resultado acumulado ficticio: -791.59 EUR sobre 238 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 79 | -3.38 EUR | 1% | 49% |
| nota global | medio | 79 | -4.01 EUR | 3% | 65% |
| nota global | alto | 80 | -2.60 EUR | 6% | 55% |
| puesto en el ranking | bajo | 79 | -2.35 EUR | 6% | 53% |
| puesto en el ranking | medio | 79 | -3.84 EUR | 3% | 59% |
| puesto en el ranking | alto | 80 | -3.77 EUR | 1% | 56% |
| potencial hasta objetivo | bajo | 79 | -3.56 EUR | 4% | 56% |
| potencial hasta objetivo | medio | 79 | -3.71 EUR | 3% | 61% |
| potencial hasta objetivo | alto | 80 | -2.72 EUR | 4% | 52% |
| dispersion | bajo | 79 | -2.64 EUR | 6% | 54% |
| dispersion | medio | 79 | -4.05 EUR | 3% | 62% |
| dispersion | alto | 80 | -3.28 EUR | 1% | 52% |
| % compra fuerte | bajo | 73 | -3.95 EUR | 1% | 59% |
| % compra fuerte | medio | 73 | -2.75 EUR | 4% | 55% |
| % compra fuerte | alto | 75 | -3.51 EUR | 3% | 55% |
| momentum 30d | bajo | 79 | -3.61 EUR | 4% | 58% |
| momentum 30d | medio | 79 | -3.05 EUR | 3% | 53% |
| momentum 30d | alto | 80 | -3.32 EUR | 4% | 57% |
| fuerza relativa | bajo | 79 | -3.73 EUR | 3% | 59% |
| fuerza relativa | medio | 79 | -3.15 EUR | 3% | 53% |
| fuerza relativa | alto | 80 | -3.10 EUR | 5% | 56% |
| RSI | bajo | 79 | -3.01 EUR | 5% | 53% |
| RSI | medio | 79 | -3.42 EUR | 3% | 57% |
| RSI | alto | 80 | -3.54 EUR | 2% | 59% |
| volumen relativo | bajo | 73 | -3.13 EUR | 7% | 59% |
| volumen relativo | medio | 73 | -3.29 EUR | 0% | 51% |
| volumen relativo | alto | 75 | -3.61 EUR | 3% | 55% |
| volatilidad | bajo | 73 | -3.29 EUR | 3% | 52% |
| volatilidad | medio | 73 | -3.84 EUR | 1% | 56% |
| volatilidad | alto | 75 | -2.92 EUR | 5% | 56% |
| liquidez | bajo | 73 | -3.25 EUR | 3% | 53% |
| liquidez | medio | 73 | -3.35 EUR | 4% | 58% |
| liquidez | alto | 75 | -3.43 EUR | 3% | 53% |
| distancia max 52s | bajo | 73 | -2.68 EUR | 5% | 52% |
| distancia max 52s | medio | 73 | -3.32 EUR | 1% | 55% |
| distancia max 52s | alto | 75 | -4.02 EUR | 3% | 57% |
| consenso | buy | 166 | -3.44 EUR | 3% | 55% |
| consenso | strong_buy | 72 | -3.07 EUR | 4% | 58% |
| tendencia tecnica | alcista | 113 | -3.51 EUR | 4% | 58% |
| tendencia tecnica | mixta | 66 | -3.31 EUR | 3% | 56% |
| tendencia tecnica | bajista | 59 | -2.99 EUR | 3% | 54% |
| tendencia analistas | mejorando | 116 | -3.33 EUR | 3% | 55% |
| tendencia analistas | estable | 76 | -3.68 EUR | 5% | 63% |
| tendencia analistas | empeorando | 9 | -4.67 EUR | 0% | 78% |
| regimen de mercado | neutro | 126 | -3.12 EUR | 3% | 52% |
| regimen de mercado | favorable | 109 | -3.44 EUR | 4% | 61% |
| catalizador | sin catalizador | 237 | -3.31 EUR | 3% | 56% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.56 | -2.72 | **+0.84 EUR** |
| nota global | -3.38 | -2.60 | **+0.77 EUR** |
| fuerza relativa | -3.73 | -3.10 | **+0.63 EUR** |
| % compra fuerte | -3.95 | -3.51 | **+0.44 EUR** |
| volatilidad | -3.29 | -2.92 | **+0.37 EUR** |
| momentum 30d | -3.61 | -3.32 | **+0.29 EUR** |
| liquidez | -3.25 | -3.43 | **-0.18 EUR** |
| volumen relativo | -3.13 | -3.61 | **-0.47 EUR** |
| RSI | -3.01 | -3.54 | **-0.52 EUR** |
| dispersion | -2.64 | -3.28 | **-0.64 EUR** |
| distancia max 52s | -2.68 | -4.02 | **-1.35 EUR** |
| puesto en el ranking | -2.35 | -3.77 | **-1.42 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
