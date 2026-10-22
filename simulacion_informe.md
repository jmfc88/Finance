# Simulacion en paralelo

Actualizado: 2026-10-22 11:44 · dia 60 de ejecucion
**Revision nº4 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **210**
- Operaciones abiertas: 52

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 1% | +16.90 EUR |
| beneficio | 3 | 1% | +7.07 EUR |
| flojo | 72 | 34% | +1.31 EUR |
| plano | 13 | 6% | -1.84 EUR |
| perdida | 74 | 35% | -7.16 EUR |
| nefasta | 45 | 21% | -6.87 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 48 | -2.01% | 3/48 (6%) | 9/48 | 10 |
| 11-20 | 55 | -3.18% | 2/55 (4%) | 4/55 | 9 |
| 21-30 | 107 | -3.97% | 1/107 (1%) | 8/107 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 5 | +0.46% | -2.00% | **+2.46%** | 2/5 (40%) |
| 11-20 | 9 | -2.75% | -0.78% | **-1.97%** | 5/9 (56%) |
| 21-30 | 22 | -2.52% | -0.86% | **-1.66%** | 12/22 (55%) |

**En conjunto:** -2.16% de media frente a -1.00% del indice, una diferencia de **-1.17%**. 19 de 36 operaciones (53%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 35 operaciones, media -2.64%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -1.69% | 30 | -50.57 EUR | 1/30 | -8.20 EUR |
| escalera + stop vol x2.5 | -2.40% | 37 | -88.64 EUR | 1/37 | -7.93 EUR |
| trailing pegado (3%) | -2.45% | 66 | -161.75 EUR | 4/66 | -10.00 EUR |
| escalera + stop vol x3 | -2.77% | 36 | -99.87 EUR | 1/36 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.32% | 210 | -696.43 EUR | 6/210 | -8.08 EUR |
| arranca antes (+3%) | -3.64% | 58 | -211.33 EUR | 4/58 | -10.00 EUR |
| arranca despues (+8%) | -3.74% | 52 | -194.45 EUR | 4/52 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.74% | 52 | -194.45 EUR | 4/52 | -10.00 EUR |
| trailing suelto (7%) | -4.35% | 50 | -217.59 EUR | 3/50 | -10.00 EUR |
| sin trailing, solo stop | -4.69% | 49 | -229.65 EUR | 2/49 | -10.00 EUR |
| stop corto (5%) | -5.58% | 137 | -764.92 EUR | 4/137 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.32%**
- Aciertos (>= 5 EUR limpios): 6/210 (3%)
- Resultado acumulado ficticio: -696.43 EUR sobre 210 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 70 | -3.62 EUR | 0% | 51% |
| nota global | medio | 70 | -3.82 EUR | 3% | 63% |
| nota global | alto | 70 | -2.51 EUR | 6% | 56% |
| puesto en el ranking | bajo | 70 | -2.27 EUR | 7% | 54% |
| puesto en el ranking | medio | 70 | -3.80 EUR | 1% | 59% |
| puesto en el ranking | alto | 70 | -3.88 EUR | 0% | 57% |
| potencial hasta objetivo | bajo | 70 | -3.56 EUR | 3% | 56% |
| potencial hasta objetivo | medio | 70 | -3.87 EUR | 1% | 61% |
| potencial hasta objetivo | alto | 70 | -2.52 EUR | 4% | 53% |
| dispersion | bajo | 70 | -2.63 EUR | 6% | 54% |
| dispersion | medio | 70 | -4.22 EUR | 1% | 64% |
| dispersion | alto | 70 | -3.09 EUR | 1% | 51% |
| % compra fuerte | bajo | 65 | -4.03 EUR | 2% | 60% |
| % compra fuerte | medio | 65 | -2.96 EUR | 2% | 57% |
| % compra fuerte | alto | 67 | -3.37 EUR | 3% | 54% |
| momentum 30d | bajo | 70 | -3.09 EUR | 4% | 54% |
| momentum 30d | medio | 70 | -3.21 EUR | 1% | 56% |
| momentum 30d | alto | 70 | -3.65 EUR | 3% | 60% |
| fuerza relativa | bajo | 70 | -3.09 EUR | 4% | 57% |
| fuerza relativa | medio | 70 | -3.50 EUR | 0% | 54% |
| fuerza relativa | alto | 70 | -3.37 EUR | 4% | 59% |
| RSI | bajo | 70 | -2.64 EUR | 6% | 51% |
| RSI | medio | 70 | -3.45 EUR | 1% | 57% |
| RSI | alto | 70 | -3.86 EUR | 1% | 61% |
| volumen relativo | bajo | 64 | -3.20 EUR | 5% | 61% |
| volumen relativo | medio | 64 | -3.08 EUR | 0% | 47% |
| volumen relativo | alto | 65 | -3.73 EUR | 3% | 57% |
| volatilidad | bajo | 64 | -3.62 EUR | 0% | 55% |
| volatilidad | medio | 64 | -4.01 EUR | 2% | 58% |
| volatilidad | alto | 65 | -2.40 EUR | 6% | 52% |
| liquidez | bajo | 64 | -3.44 EUR | 2% | 55% |
| liquidez | medio | 64 | -2.94 EUR | 5% | 55% |
| liquidez | alto | 65 | -3.63 EUR | 2% | 55% |
| distancia max 52s | bajo | 64 | -2.37 EUR | 6% | 50% |
| distancia max 52s | medio | 64 | -3.50 EUR | 0% | 56% |
| distancia max 52s | alto | 65 | -4.13 EUR | 2% | 58% |
| consenso | buy | 149 | -3.62 EUR | 2% | 57% |
| consenso | strong_buy | 61 | -2.58 EUR | 5% | 56% |
| tendencia tecnica | alcista | 107 | -3.55 EUR | 3% | 58% |
| tendencia tecnica | mixta | 55 | -3.00 EUR | 2% | 53% |
| tendencia tecnica | bajista | 48 | -3.16 EUR | 4% | 58% |
| tendencia analistas | mejorando | 102 | -3.37 EUR | 3% | 57% |
| tendencia analistas | estable | 65 | -3.75 EUR | 3% | 63% |
| tendencia analistas | empeorando | 9 | -4.67 EUR | 0% | 78% |
| regimen de mercado | favorable | 105 | -3.52 EUR | 4% | 62% |
| regimen de mercado | neutro | 105 | -3.11 EUR | 2% | 51% |
| catalizador | sin catalizador | 209 | -3.29 EUR | 3% | 56% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -3.62 | -2.40 | **+1.22 EUR** |
| nota global | -3.62 | -2.51 | **+1.11 EUR** |
| potencial hasta objetivo | -3.56 | -2.52 | **+1.05 EUR** |
| % compra fuerte | -4.03 | -3.37 | **+0.65 EUR** |
| liquidez | -3.44 | -3.63 | **-0.18 EUR** |
| fuerza relativa | -3.09 | -3.37 | **-0.28 EUR** |
| dispersion | -2.63 | -3.09 | **-0.46 EUR** |
| volumen relativo | -3.20 | -3.73 | **-0.53 EUR** |
| momentum 30d | -3.09 | -3.65 | **-0.57 EUR** |
| RSI | -2.64 | -3.86 | **-1.23 EUR** |
| puesto en el ranking | -2.27 | -3.88 | **-1.62 EUR** |
| distancia max 52s | -2.37 | -4.13 | **-1.75 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
