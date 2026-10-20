# Simulacion en paralelo

Actualizado: 2026-10-20 00:22 · dia 58 de ejecucion
Proxima revision de ponderacion en 2 dias.

- Operaciones cerradas: **195**
- Operaciones abiertas: 55

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 2% | +16.90 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 66 | 34% | +1.27 EUR |
| plano | 12 | 6% | -1.75 EUR |
| perdida | 68 | 35% | -7.25 EUR |
| nefasta | 43 | 22% | -6.81 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 45 | -1.79% | 3/45 (7%) | 9/45 | 9 |
| 11-20 | 52 | -3.29% | 2/52 (4%) | 3/52 | 9 |
| 21-30 | 98 | -4.08% | 1/98 (1%) | 6/98 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 2 | +9.18% | -2.33% | **+11.51%** | 2/2 (100%) |
| 11-20 | 6 | -3.54% | -0.56% | **-2.98%** | 3/6 (50%) |
| 21-30 | 13 | -2.30% | -0.68% | **-1.62%** | 8/13 (62%) |

**En conjunto:** -1.56% de media frente a -0.80% del indice, una diferencia de **-0.76%**. 13 de 21 operaciones (62%) batieron a su indice.

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
| escalera + stop vol x4 | -0.63% | 17 | -10.63 EUR | 1/17 | -8.20 EUR |
| escalera + stop vol x2.5 | -2.23% | 22 | -49.09 EUR | 1/22 | -7.93 EUR |
| trailing pegado (3%) | -2.65% | 59 | -156.49 EUR | 4/59 | -10.00 EUR |
| escalera + stop vol x3 | -2.87% | 22 | -63.23 EUR | 1/22 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.34% | 195 | -651.28 EUR | 6/195 | -8.08 EUR |
| arranca antes (+3%) | -3.76% | 53 | -199.05 EUR | 4/53 | -10.00 EUR |
| arranca despues (+8%) | -3.88% | 47 | -182.17 EUR | 4/47 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.88% | 47 | -182.17 EUR | 4/47 | -10.00 EUR |
| trailing suelto (7%) | -4.56% | 45 | -205.31 EUR | 3/45 | -10.00 EUR |
| sin trailing, solo stop | -4.94% | 44 | -217.37 EUR | 2/44 | -10.00 EUR |
| stop corto (5%) | -5.61% | 127 | -712.21 EUR | 4/127 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.34%**
- Aciertos (>= 5 EUR limpios): 6/195 (3%)
- Resultado acumulado ficticio: -651.28 EUR sobre 195 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 65 | -3.49 EUR | 0% | 51% |
| nota global | medio | 65 | -4.04 EUR | 3% | 66% |
| nota global | alto | 65 | -2.49 EUR | 6% | 54% |
| puesto en el ranking | bajo | 65 | -2.14 EUR | 8% | 52% |
| puesto en el ranking | medio | 65 | -3.91 EUR | 2% | 60% |
| puesto en el ranking | alto | 65 | -3.97 EUR | 0% | 58% |
| potencial hasta objetivo | bajo | 65 | -3.73 EUR | 3% | 57% |
| potencial hasta objetivo | medio | 65 | -3.99 EUR | 2% | 63% |
| potencial hasta objetivo | alto | 65 | -2.29 EUR | 5% | 51% |
| dispersion | bajo | 65 | -2.41 EUR | 6% | 52% |
| dispersion | medio | 65 | -4.48 EUR | 2% | 66% |
| dispersion | alto | 65 | -3.13 EUR | 2% | 52% |
| % compra fuerte | bajo | 60 | -4.26 EUR | 2% | 62% |
| % compra fuerte | medio | 60 | -2.99 EUR | 2% | 58% |
| % compra fuerte | alto | 62 | -3.23 EUR | 3% | 52% |
| momentum 30d | bajo | 65 | -2.81 EUR | 5% | 51% |
| momentum 30d | medio | 65 | -3.60 EUR | 2% | 60% |
| momentum 30d | alto | 65 | -3.61 EUR | 3% | 60% |
| fuerza relativa | bajo | 65 | -3.04 EUR | 5% | 57% |
| fuerza relativa | medio | 65 | -3.64 EUR | 0% | 55% |
| fuerza relativa | alto | 65 | -3.34 EUR | 5% | 58% |
| RSI | bajo | 65 | -2.46 EUR | 6% | 49% |
| RSI | medio | 65 | -3.48 EUR | 2% | 58% |
| RSI | alto | 65 | -4.07 EUR | 2% | 63% |
| volumen relativo | bajo | 59 | -3.21 EUR | 5% | 61% |
| volumen relativo | medio | 59 | -3.06 EUR | 0% | 46% |
| volumen relativo | alto | 60 | -3.82 EUR | 3% | 58% |
| volatilidad | bajo | 59 | -3.90 EUR | 0% | 58% |
| volatilidad | medio | 59 | -3.55 EUR | 3% | 54% |
| volatilidad | alto | 60 | -2.66 EUR | 5% | 53% |
| liquidez | bajo | 59 | -3.66 EUR | 2% | 58% |
| liquidez | medio | 59 | -3.02 EUR | 5% | 56% |
| liquidez | alto | 60 | -3.41 EUR | 2% | 52% |
| distancia max 52s | bajo | 59 | -2.29 EUR | 7% | 51% |
| distancia max 52s | medio | 59 | -3.63 EUR | 0% | 56% |
| distancia max 52s | alto | 60 | -4.17 EUR | 2% | 58% |
| consenso | buy | 138 | -3.70 EUR | 2% | 58% |
| consenso | strong_buy | 57 | -2.48 EUR | 5% | 54% |
| tendencia tecnica | alcista | 102 | -3.69 EUR | 3% | 59% |
| tendencia tecnica | mixta | 49 | -2.90 EUR | 2% | 53% |
| tendencia tecnica | bajista | 44 | -3.01 EUR | 5% | 57% |
| tendencia analistas | mejorando | 96 | -3.31 EUR | 3% | 56% |
| tendencia analistas | estable | 59 | -3.97 EUR | 3% | 66% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 105 | -3.52 EUR | 4% | 62% |
| regimen de mercado | neutro | 90 | -3.13 EUR | 2% | 51% |
| catalizador | sin catalizador | 194 | -3.32 EUR | 3% | 57% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.73 | -2.29 | **+1.44 EUR** |
| volatilidad | -3.90 | -2.66 | **+1.24 EUR** |
| % compra fuerte | -4.26 | -3.23 | **+1.02 EUR** |
| nota global | -3.49 | -2.49 | **+1.01 EUR** |
| liquidez | -3.66 | -3.41 | **+0.26 EUR** |
| fuerza relativa | -3.04 | -3.34 | **-0.31 EUR** |
| volumen relativo | -3.21 | -3.82 | **-0.61 EUR** |
| dispersion | -2.41 | -3.13 | **-0.72 EUR** |
| momentum 30d | -2.81 | -3.61 | **-0.81 EUR** |
| RSI | -2.46 | -4.07 | **-1.61 EUR** |
| puesto en el ranking | -2.14 | -3.97 | **-1.83 EUR** |
| distancia max 52s | -2.29 | -4.17 | **-1.88 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
