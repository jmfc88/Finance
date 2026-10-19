# Simulacion en paralelo

Actualizado: 2026-10-19 16:29 · dia 57 de ejecucion
Proxima revision de ponderacion en 3 dias.

- Operaciones cerradas: **194**
- Operaciones abiertas: 54

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 2% | +16.90 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 66 | 34% | +1.27 EUR |
| plano | 12 | 6% | -1.75 EUR |
| perdida | 68 | 35% | -7.25 EUR |
| nefasta | 42 | 22% | -6.78 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 45 | -1.79% | 3/45 (7%) | 9/45 | 9 |
| 11-20 | 52 | -3.29% | 2/52 (4%) | 3/52 | 9 |
| 21-30 | 97 | -4.04% | 1/97 (1%) | 6/97 | 9 |

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
| escalera + stop vol x4 | -0.15% | 16 | -2.43 EUR | 1/16 | -8.08 EUR |
| escalera + stop vol x2.5 | -2.09% | 21 | -43.97 EUR | 1/21 | -7.93 EUR |
| trailing pegado (3%) | -2.65% | 59 | -156.49 EUR | 4/59 | -10.00 EUR |
| escalera + stop vol x3 | -2.72% | 21 | -57.08 EUR | 1/21 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.32% | 194 | -643.20 EUR | 6/194 | -8.08 EUR |
| arranca antes (+3%) | -3.76% | 53 | -199.05 EUR | 4/53 | -10.00 EUR |
| arranca despues (+8%) | -3.88% | 47 | -182.17 EUR | 4/47 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.88% | 47 | -182.17 EUR | 4/47 | -10.00 EUR |
| trailing suelto (7%) | -4.56% | 45 | -205.31 EUR | 3/45 | -10.00 EUR |
| sin trailing, solo stop | -4.94% | 44 | -217.37 EUR | 2/44 | -10.00 EUR |
| stop corto (5%) | -5.60% | 126 | -705.21 EUR | 4/126 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.32%**
- Aciertos (>= 5 EUR limpios): 6/194 (3%)
- Resultado acumulado ficticio: -643.20 EUR sobre 194 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 64 | -3.56 EUR | 0% | 52% |
| nota global | medio | 64 | -3.98 EUR | 3% | 64% |
| nota global | alto | 66 | -2.43 EUR | 6% | 55% |
| puesto en el ranking | bajo | 64 | -2.19 EUR | 8% | 52% |
| puesto en el ranking | medio | 64 | -3.70 EUR | 2% | 59% |
| puesto en el ranking | alto | 66 | -4.03 EUR | 0% | 59% |
| potencial hasta objetivo | bajo | 64 | -3.81 EUR | 3% | 58% |
| potencial hasta objetivo | medio | 64 | -3.93 EUR | 2% | 62% |
| potencial hasta objetivo | alto | 66 | -2.24 EUR | 5% | 50% |
| dispersion | bajo | 64 | -2.32 EUR | 6% | 52% |
| dispersion | medio | 64 | -4.43 EUR | 2% | 66% |
| dispersion | alto | 66 | -3.20 EUR | 2% | 53% |
| % compra fuerte | bajo | 60 | -4.26 EUR | 2% | 62% |
| % compra fuerte | medio | 60 | -2.99 EUR | 2% | 58% |
| % compra fuerte | alto | 62 | -3.23 EUR | 3% | 52% |
| momentum 30d | bajo | 64 | -2.72 EUR | 5% | 50% |
| momentum 30d | medio | 64 | -3.65 EUR | 2% | 61% |
| momentum 30d | alto | 66 | -3.57 EUR | 3% | 59% |
| fuerza relativa | bajo | 64 | -2.96 EUR | 5% | 56% |
| fuerza relativa | medio | 64 | -3.57 EUR | 0% | 55% |
| fuerza relativa | alto | 66 | -3.42 EUR | 5% | 59% |
| RSI | bajo | 64 | -2.37 EUR | 6% | 48% |
| RSI | medio | 64 | -3.55 EUR | 2% | 58% |
| RSI | alto | 66 | -4.00 EUR | 2% | 64% |
| volumen relativo | bajo | 59 | -3.21 EUR | 5% | 61% |
| volumen relativo | medio | 59 | -2.97 EUR | 0% | 44% |
| volumen relativo | alto | 59 | -3.84 EUR | 3% | 59% |
| volatilidad | bajo | 59 | -3.90 EUR | 0% | 58% |
| volatilidad | medio | 59 | -3.55 EUR | 3% | 54% |
| volatilidad | alto | 59 | -2.57 EUR | 5% | 53% |
| liquidez | bajo | 59 | -3.66 EUR | 2% | 58% |
| liquidez | medio | 59 | -3.02 EUR | 5% | 56% |
| liquidez | alto | 59 | -3.33 EUR | 2% | 51% |
| distancia max 52s | bajo | 59 | -2.13 EUR | 7% | 49% |
| distancia max 52s | medio | 59 | -3.63 EUR | 0% | 56% |
| distancia max 52s | alto | 59 | -4.26 EUR | 2% | 59% |
| consenso | buy | 138 | -3.70 EUR | 2% | 58% |
| consenso | strong_buy | 56 | -2.38 EUR | 5% | 54% |
| tendencia tecnica | alcista | 102 | -3.69 EUR | 3% | 59% |
| tendencia tecnica | mixta | 49 | -2.90 EUR | 2% | 53% |
| tendencia tecnica | bajista | 43 | -2.89 EUR | 5% | 56% |
| tendencia analistas | mejorando | 96 | -3.31 EUR | 3% | 56% |
| tendencia analistas | estable | 59 | -3.97 EUR | 3% | 66% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 105 | -3.52 EUR | 4% | 62% |
| regimen de mercado | neutro | 89 | -3.08 EUR | 2% | 51% |
| catalizador | sin catalizador | 193 | -3.29 EUR | 3% | 56% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.81 | -2.24 | **+1.56 EUR** |
| volatilidad | -3.90 | -2.57 | **+1.33 EUR** |
| nota global | -3.56 | -2.43 | **+1.13 EUR** |
| % compra fuerte | -4.26 | -3.23 | **+1.02 EUR** |
| liquidez | -3.66 | -3.33 | **+0.34 EUR** |
| fuerza relativa | -2.96 | -3.42 | **-0.46 EUR** |
| volumen relativo | -3.21 | -3.84 | **-0.63 EUR** |
| momentum 30d | -2.72 | -3.57 | **-0.84 EUR** |
| dispersion | -2.32 | -3.20 | **-0.88 EUR** |
| RSI | -2.37 | -4.00 | **-1.62 EUR** |
| puesto en el ranking | -2.19 | -4.03 | **-1.84 EUR** |
| distancia max 52s | -2.13 | -4.26 | **-2.12 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
