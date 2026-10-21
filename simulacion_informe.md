# Simulacion en paralelo

Actualizado: 2026-10-21 06:00 · dia 59 de ejecucion
Proxima revision de ponderacion en 1 dia.

- Operaciones cerradas: **199**
- Operaciones abiertas: 58

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 2% | +16.90 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 66 | 33% | +1.27 EUR |
| plano | 12 | 6% | -1.75 EUR |
| perdida | 71 | 36% | -7.29 EUR |
| nefasta | 44 | 22% | -6.84 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 46 | -1.92% | 3/46 (7%) | 9/46 | 9 |
| 11-20 | 53 | -3.38% | 2/53 (4%) | 3/53 | 9 |
| 21-30 | 100 | -4.16% | 1/100 (1%) | 6/100 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 3 | +3.42% | -1.79% | **+5.21%** | 2/3 (67%) |
| 11-20 | 7 | -4.19% | -0.70% | **-3.48%** | 3/7 (43%) |
| 21-30 | 15 | -3.07% | -0.68% | **-2.39%** | 8/15 (53%) |

**En conjunto:** -2.60% de media frente a -0.82% del indice, una diferencia de **-1.79%**. 13 de 25 operaciones (52%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 30 operaciones, media -2.67%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -1.31% | 19 | -24.81 EUR | 1/19 | -8.20 EUR |
| trailing pegado (3%) | -2.65% | 59 | -156.49 EUR | 4/59 | -10.00 EUR |
| escalera + stop vol x2.5 | -2.73% | 26 | -71.00 EUR | 1/26 | -7.93 EUR |
| escalera + stop vol x3 | -3.23% | 25 | -80.68 EUR | 1/25 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.44% | 199 | -683.60 EUR | 6/199 | -8.08 EUR |
| arranca antes (+3%) | -3.76% | 53 | -199.05 EUR | 4/53 | -10.00 EUR |
| arranca despues (+8%) | -3.88% | 47 | -182.17 EUR | 4/47 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.88% | 47 | -182.17 EUR | 4/47 | -10.00 EUR |
| trailing suelto (7%) | -4.56% | 45 | -205.31 EUR | 3/45 | -10.00 EUR |
| sin trailing, solo stop | -4.94% | 44 | -217.37 EUR | 2/44 | -10.00 EUR |
| stop corto (5%) | -5.65% | 131 | -740.21 EUR | 4/131 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.44%**
- Aciertos (>= 5 EUR limpios): 6/199 (3%)
- Resultado acumulado ficticio: -683.60 EUR sobre 199 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 66 | -3.56 EUR | 0% | 52% |
| nota global | medio | 66 | -4.24 EUR | 3% | 67% |
| nota global | alto | 67 | -2.52 EUR | 6% | 55% |
| puesto en el ranking | bajo | 66 | -2.23 EUR | 8% | 53% |
| puesto en el ranking | medio | 66 | -3.97 EUR | 2% | 61% |
| puesto en el ranking | alto | 67 | -4.10 EUR | 0% | 60% |
| potencial hasta objetivo | bajo | 66 | -3.80 EUR | 3% | 58% |
| potencial hasta objetivo | medio | 66 | -4.05 EUR | 2% | 64% |
| potencial hasta objetivo | alto | 67 | -2.47 EUR | 4% | 52% |
| dispersion | bajo | 66 | -2.56 EUR | 6% | 53% |
| dispersion | medio | 66 | -4.61 EUR | 2% | 68% |
| dispersion | alto | 67 | -3.14 EUR | 1% | 52% |
| % compra fuerte | bajo | 62 | -4.32 EUR | 2% | 63% |
| % compra fuerte | medio | 62 | -2.92 EUR | 2% | 56% |
| % compra fuerte | alto | 62 | -3.53 EUR | 3% | 55% |
| momentum 30d | bajo | 66 | -3.30 EUR | 5% | 56% |
| momentum 30d | medio | 66 | -3.37 EUR | 2% | 58% |
| momentum 30d | alto | 67 | -3.63 EUR | 3% | 60% |
| fuerza relativa | bajo | 66 | -3.30 EUR | 5% | 59% |
| fuerza relativa | medio | 66 | -3.52 EUR | 0% | 55% |
| fuerza relativa | alto | 67 | -3.49 EUR | 4% | 60% |
| RSI | bajo | 66 | -2.72 EUR | 6% | 52% |
| RSI | medio | 66 | -3.65 EUR | 2% | 59% |
| RSI | alto | 67 | -3.92 EUR | 1% | 63% |
| volumen relativo | bajo | 60 | -3.48 EUR | 5% | 63% |
| volumen relativo | medio | 60 | -2.95 EUR | 0% | 45% |
| volumen relativo | alto | 62 | -3.96 EUR | 3% | 60% |
| volatilidad | bajo | 60 | -3.97 EUR | 0% | 58% |
| volatilidad | medio | 60 | -3.63 EUR | 3% | 55% |
| volatilidad | alto | 62 | -2.83 EUR | 5% | 55% |
| liquidez | bajo | 60 | -3.74 EUR | 2% | 58% |
| liquidez | medio | 60 | -3.11 EUR | 5% | 57% |
| liquidez | alto | 62 | -3.56 EUR | 2% | 53% |
| distancia max 52s | bajo | 60 | -2.38 EUR | 7% | 52% |
| distancia max 52s | medio | 60 | -3.70 EUR | 0% | 57% |
| distancia max 52s | alto | 62 | -4.29 EUR | 2% | 60% |
| consenso | buy | 140 | -3.76 EUR | 2% | 59% |
| consenso | strong_buy | 59 | -2.67 EUR | 5% | 56% |
| tendencia tecnica | alcista | 102 | -3.69 EUR | 3% | 59% |
| tendencia tecnica | mixta | 52 | -3.20 EUR | 2% | 56% |
| tendencia tecnica | bajista | 45 | -3.12 EUR | 4% | 58% |
| tendencia analistas | mejorando | 99 | -3.45 EUR | 3% | 58% |
| tendencia analistas | estable | 59 | -3.97 EUR | 3% | 66% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 105 | -3.52 EUR | 4% | 62% |
| regimen de mercado | neutro | 94 | -3.34 EUR | 2% | 53% |
| catalizador | sin catalizador | 198 | -3.41 EUR | 3% | 58% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.80 | -2.47 | **+1.33 EUR** |
| volatilidad | -3.97 | -2.83 | **+1.14 EUR** |
| nota global | -3.56 | -2.52 | **+1.05 EUR** |
| % compra fuerte | -4.32 | -3.53 | **+0.80 EUR** |
| liquidez | -3.74 | -3.56 | **+0.18 EUR** |
| fuerza relativa | -3.30 | -3.49 | **-0.19 EUR** |
| momentum 30d | -3.30 | -3.63 | **-0.33 EUR** |
| volumen relativo | -3.48 | -3.96 | **-0.47 EUR** |
| dispersion | -2.56 | -3.14 | **-0.58 EUR** |
| RSI | -2.72 | -3.92 | **-1.20 EUR** |
| puesto en el ranking | -2.23 | -4.10 | **-1.86 EUR** |
| distancia max 52s | -2.38 | -4.29 | **-1.91 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
