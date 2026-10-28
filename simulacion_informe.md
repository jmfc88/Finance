# Simulacion en paralelo

Actualizado: 2026-10-28 18:50 · dia 66 de ejecucion
Proxima revision de ponderacion en 9 dias.

- Operaciones cerradas: **239**
- Operaciones abiertas: 63

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 1% | +16.90 EUR |
| beneficio | 5 | 2% | +7.59 EUR |
| flojo | 81 | 34% | +1.33 EUR |
| plano | 16 | 7% | -1.75 EUR |
| perdida | 80 | 33% | -7.23 EUR |
| nefasta | 54 | 23% | -7.07 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 51 | -2.19% | 3/51 (6%) | 9/51 | 10 |
| 11-20 | 62 | -3.01% | 3/62 (5%) | 7/62 | 9 |
| 21-30 | 126 | -3.91% | 2/126 (2%) | 10/126 | 9 |

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
| trailing pegado (3%) | -2.45% | 84 | -206.11 EUR | 6/84 | -10.00 EUR |
| escalera + stop vol x2.5 | -2.61% | 66 | -172.56 EUR | 2/66 | -7.93 EUR |
| escalera + stop vol x3 | -3.03% | 65 | -197.15 EUR | 2/65 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.31% | 239 | -791.53 EUR | 8/239 | -8.08 EUR |
| arranca antes (+3%) | -3.50% | 74 | -259.33 EUR | 5/74 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.74% | 68 | -254.61 EUR | 5/68 | -10.00 EUR |
| arranca despues (+8%) | -3.77% | 67 | -252.55 EUR | 5/67 | -10.00 EUR |
| trailing suelto (7%) | -4.27% | 65 | -277.86 EUR | 4/65 | -10.00 EUR |
| sin trailing, solo stop | -4.58% | 63 | -288.64 EUR | 3/63 | -10.00 EUR |
| stop corto (5%) | -5.42% | 161 | -872.12 EUR | 5/161 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.31%**
- Aciertos (>= 5 EUR limpios): 8/239 (3%)
- Resultado acumulado ficticio: -791.53 EUR sobre 239 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 79 | -3.38 EUR | 1% | 49% |
| nota global | medio | 79 | -4.06 EUR | 3% | 65% |
| nota global | alto | 81 | -2.52 EUR | 6% | 54% |
| puesto en el ranking | bajo | 79 | -2.35 EUR | 6% | 53% |
| puesto en el ranking | medio | 79 | -3.84 EUR | 3% | 59% |
| puesto en el ranking | alto | 81 | -3.73 EUR | 1% | 56% |
| potencial hasta objetivo | bajo | 79 | -3.56 EUR | 4% | 56% |
| potencial hasta objetivo | medio | 79 | -3.71 EUR | 3% | 61% |
| potencial hasta objetivo | alto | 81 | -2.68 EUR | 4% | 52% |
| dispersion | bajo | 79 | -2.59 EUR | 6% | 53% |
| dispersion | medio | 79 | -4.11 EUR | 3% | 63% |
| dispersion | alto | 81 | -3.23 EUR | 1% | 52% |
| % compra fuerte | bajo | 74 | -3.90 EUR | 1% | 58% |
| % compra fuerte | medio | 74 | -2.70 EUR | 4% | 54% |
| % compra fuerte | alto | 74 | -3.57 EUR | 3% | 55% |
| momentum 30d | bajo | 79 | -3.65 EUR | 4% | 58% |
| momentum 30d | medio | 79 | -3.05 EUR | 3% | 53% |
| momentum 30d | alto | 81 | -3.24 EUR | 4% | 57% |
| fuerza relativa | bajo | 79 | -3.74 EUR | 3% | 59% |
| fuerza relativa | medio | 79 | -3.03 EUR | 3% | 52% |
| fuerza relativa | alto | 81 | -3.16 EUR | 5% | 57% |
| RSI | bajo | 79 | -3.03 EUR | 5% | 53% |
| RSI | medio | 79 | -3.31 EUR | 3% | 56% |
| RSI | alto | 81 | -3.59 EUR | 2% | 59% |
| volumen relativo | bajo | 74 | -3.09 EUR | 7% | 58% |
| volumen relativo | medio | 74 | -3.35 EUR | 0% | 51% |
| volumen relativo | alto | 74 | -3.54 EUR | 3% | 54% |
| volatilidad | bajo | 74 | -3.25 EUR | 3% | 51% |
| volatilidad | medio | 74 | -3.55 EUR | 3% | 55% |
| volatilidad | alto | 74 | -3.19 EUR | 4% | 57% |
| liquidez | bajo | 74 | -3.32 EUR | 3% | 54% |
| liquidez | medio | 74 | -3.18 EUR | 4% | 55% |
| liquidez | alto | 74 | -3.49 EUR | 3% | 54% |
| distancia max 52s | bajo | 74 | -2.64 EUR | 5% | 51% |
| distancia max 52s | medio | 74 | -3.26 EUR | 1% | 54% |
| distancia max 52s | alto | 74 | -4.09 EUR | 3% | 58% |
| consenso | buy | 167 | -3.42 EUR | 3% | 55% |
| consenso | strong_buy | 72 | -3.07 EUR | 4% | 58% |
| tendencia tecnica | alcista | 113 | -3.51 EUR | 4% | 58% |
| tendencia tecnica | mixta | 66 | -3.31 EUR | 3% | 56% |
| tendencia tecnica | bajista | 60 | -2.94 EUR | 3% | 53% |
| tendencia analistas | mejorando | 117 | -3.30 EUR | 3% | 55% |
| tendencia analistas | estable | 76 | -3.68 EUR | 5% | 63% |
| tendencia analistas | empeorando | 9 | -4.67 EUR | 0% | 78% |
| regimen de mercado | neutro | 127 | -3.09 EUR | 3% | 51% |
| regimen de mercado | favorable | 109 | -3.44 EUR | 4% | 61% |
| catalizador | sin catalizador | 238 | -3.29 EUR | 3% | 56% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.56 | -2.68 | **+0.87 EUR** |
| nota global | -3.38 | -2.52 | **+0.86 EUR** |
| fuerza relativa | -3.74 | -3.16 | **+0.58 EUR** |
| momentum 30d | -3.65 | -3.24 | **+0.42 EUR** |
| % compra fuerte | -3.90 | -3.57 | **+0.32 EUR** |
| volatilidad | -3.25 | -3.19 | **+0.05 EUR** |
| liquidez | -3.32 | -3.49 | **-0.17 EUR** |
| volumen relativo | -3.09 | -3.54 | **-0.45 EUR** |
| RSI | -3.03 | -3.59 | **-0.57 EUR** |
| dispersion | -2.59 | -3.23 | **-0.64 EUR** |
| puesto en el ranking | -2.35 | -3.73 | **-1.37 EUR** |
| distancia max 52s | -2.64 | -4.09 | **-1.45 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
