# Simulacion en paralelo

Actualizado: 2026-10-20 11:29 · dia 58 de ejecucion
Proxima revision de ponderacion en 2 dias.

- Operaciones cerradas: **198**
- Operaciones abiertas: 53

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 2% | +16.90 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 66 | 33% | +1.27 EUR |
| plano | 12 | 6% | -1.75 EUR |
| perdida | 71 | 36% | -7.29 EUR |
| nefasta | 43 | 22% | -6.81 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 46 | -1.92% | 3/46 (7%) | 9/46 | 9 |
| 11-20 | 53 | -3.38% | 2/53 (4%) | 3/53 | 9 |
| 21-30 | 99 | -4.12% | 1/99 (1%) | 6/99 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 3 | +3.42% | -1.79% | **+5.21%** | 2/3 (67%) |
| 11-20 | 7 | -4.19% | -0.70% | **-3.48%** | 3/7 (43%) |
| 21-30 | 14 | -2.71% | -0.68% | **-2.03%** | 8/14 (57%) |

**En conjunto:** -2.37% de media frente a -0.83% del indice, una diferencia de **-1.55%**. 13 de 24 operaciones (54%) batieron a su indice.

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
| escalera + stop vol x2.5 | -2.61% | 25 | -65.32 EUR | 1/25 | -7.93 EUR |
| trailing pegado (3%) | -2.65% | 59 | -156.49 EUR | 4/59 | -10.00 EUR |
| escalera + stop vol x3 | -3.08% | 24 | -73.86 EUR | 1/24 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.41% | 198 | -675.52 EUR | 6/198 | -8.08 EUR |
| arranca antes (+3%) | -3.76% | 53 | -199.05 EUR | 4/53 | -10.00 EUR |
| arranca despues (+8%) | -3.88% | 47 | -182.17 EUR | 4/47 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.88% | 47 | -182.17 EUR | 4/47 | -10.00 EUR |
| trailing suelto (7%) | -4.56% | 45 | -205.31 EUR | 3/45 | -10.00 EUR |
| sin trailing, solo stop | -4.94% | 44 | -217.37 EUR | 2/44 | -10.00 EUR |
| stop corto (5%) | -5.64% | 130 | -733.21 EUR | 4/130 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.41%**
- Aciertos (>= 5 EUR limpios): 6/198 (3%)
- Resultado acumulado ficticio: -675.52 EUR sobre 198 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 66 | -3.56 EUR | 0% | 52% |
| nota global | medio | 66 | -4.10 EUR | 3% | 67% |
| nota global | alto | 66 | -2.57 EUR | 6% | 55% |
| puesto en el ranking | bajo | 66 | -2.23 EUR | 8% | 53% |
| puesto en el ranking | medio | 66 | -3.97 EUR | 2% | 61% |
| puesto en el ranking | alto | 66 | -4.03 EUR | 0% | 59% |
| potencial hasta objetivo | bajo | 66 | -3.80 EUR | 3% | 58% |
| potencial hasta objetivo | medio | 66 | -4.05 EUR | 2% | 64% |
| potencial hasta objetivo | alto | 66 | -2.38 EUR | 5% | 52% |
| dispersion | bajo | 66 | -2.56 EUR | 6% | 53% |
| dispersion | medio | 66 | -4.47 EUR | 2% | 67% |
| dispersion | alto | 66 | -3.20 EUR | 2% | 53% |
| % compra fuerte | bajo | 61 | -4.26 EUR | 2% | 62% |
| % compra fuerte | medio | 61 | -2.98 EUR | 2% | 57% |
| % compra fuerte | alto | 63 | -3.45 EUR | 3% | 54% |
| momentum 30d | bajo | 66 | -3.16 EUR | 5% | 55% |
| momentum 30d | medio | 66 | -3.51 EUR | 2% | 59% |
| momentum 30d | alto | 66 | -3.57 EUR | 3% | 59% |
| fuerza relativa | bajo | 66 | -3.16 EUR | 5% | 58% |
| fuerza relativa | medio | 66 | -3.66 EUR | 0% | 56% |
| fuerza relativa | alto | 66 | -3.42 EUR | 5% | 59% |
| RSI | bajo | 66 | -2.59 EUR | 6% | 50% |
| RSI | medio | 66 | -3.65 EUR | 2% | 59% |
| RSI | alto | 66 | -4.00 EUR | 2% | 64% |
| volumen relativo | bajo | 60 | -3.29 EUR | 5% | 62% |
| volumen relativo | medio | 60 | -3.15 EUR | 0% | 47% |
| volumen relativo | alto | 61 | -3.89 EUR | 3% | 59% |
| volatilidad | bajo | 60 | -3.97 EUR | 0% | 58% |
| volatilidad | medio | 60 | -3.63 EUR | 3% | 55% |
| volatilidad | alto | 61 | -2.75 EUR | 5% | 54% |
| liquidez | bajo | 60 | -3.74 EUR | 2% | 58% |
| liquidez | medio | 60 | -3.11 EUR | 5% | 57% |
| liquidez | alto | 61 | -3.48 EUR | 2% | 52% |
| distancia max 52s | bajo | 60 | -2.23 EUR | 7% | 50% |
| distancia max 52s | medio | 60 | -3.85 EUR | 0% | 58% |
| distancia max 52s | alto | 61 | -4.23 EUR | 2% | 59% |
| consenso | buy | 139 | -3.73 EUR | 2% | 58% |
| consenso | strong_buy | 59 | -2.67 EUR | 5% | 56% |
| tendencia tecnica | alcista | 102 | -3.69 EUR | 3% | 59% |
| tendencia tecnica | mixta | 52 | -3.20 EUR | 2% | 56% |
| tendencia tecnica | bajista | 44 | -3.01 EUR | 5% | 57% |
| tendencia analistas | mejorando | 98 | -3.40 EUR | 3% | 57% |
| tendencia analistas | estable | 59 | -3.97 EUR | 3% | 66% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 105 | -3.52 EUR | 4% | 62% |
| regimen de mercado | neutro | 93 | -3.29 EUR | 2% | 53% |
| catalizador | sin catalizador | 197 | -3.39 EUR | 3% | 57% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.80 | -2.38 | **+1.42 EUR** |
| volatilidad | -3.97 | -2.75 | **+1.22 EUR** |
| nota global | -3.56 | -2.57 | **+0.99 EUR** |
| % compra fuerte | -4.26 | -3.45 | **+0.81 EUR** |
| liquidez | -3.74 | -3.48 | **+0.25 EUR** |
| fuerza relativa | -3.16 | -3.42 | **-0.26 EUR** |
| momentum 30d | -3.16 | -3.57 | **-0.40 EUR** |
| volumen relativo | -3.29 | -3.89 | **-0.60 EUR** |
| dispersion | -2.56 | -3.20 | **-0.64 EUR** |
| RSI | -2.59 | -4.00 | **-1.41 EUR** |
| puesto en el ranking | -2.23 | -4.03 | **-1.80 EUR** |
| distancia max 52s | -2.23 | -4.23 | **-2.00 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
