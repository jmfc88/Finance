# Simulacion en paralelo

Actualizado: 2026-10-19 13:01 · dia 57 de ejecucion
Proxima revision de ponderacion en 3 dias.

- Operaciones cerradas: **192**
- Operaciones abiertas: 53

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 2% | +16.90 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 64 | 33% | +1.28 EUR |
| plano | 12 | 6% | -1.75 EUR |
| perdida | 68 | 35% | -7.25 EUR |
| nefasta | 42 | 22% | -6.78 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 45 | -1.79% | 3/45 (7%) | 9/45 | 9 |
| 11-20 | 52 | -3.29% | 2/52 (4%) | 3/52 | 9 |
| 21-30 | 95 | -4.14% | 1/95 (1%) | 6/95 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 2 | +9.18% | -2.33% | **+11.51%** | 2/2 (100%) |
| 11-20 | 6 | -3.54% | -0.56% | **-2.98%** | 3/6 (50%) |
| 21-30 | 11 | -2.90% | -0.65% | **-2.25%** | 6/11 (55%) |

**En conjunto:** -1.83% de media frente a -0.80% del indice, una diferencia de **-1.03%**. 11 de 19 operaciones (58%) batieron a su indice.

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
| escalera + stop vol x4 | -0.32% | 14 | -4.43 EUR | 1/14 | -8.08 EUR |
| escalera + stop vol x2.5 | -2.42% | 19 | -45.97 EUR | 1/19 | -7.93 EUR |
| trailing pegado (3%) | -2.65% | 59 | -156.49 EUR | 4/59 | -10.00 EUR |
| escalera + stop vol x3 | -3.11% | 19 | -59.08 EUR | 1/19 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.36% | 192 | -645.20 EUR | 6/192 | -8.08 EUR |
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

- Media neta: **-3.36%**
- Aciertos (>= 5 EUR limpios): 6/192 (3%)
- Resultado acumulado ficticio: -645.20 EUR sobre 192 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 64 | -3.56 EUR | 0% | 52% |
| nota global | medio | 64 | -4.12 EUR | 3% | 67% |
| nota global | alto | 64 | -2.40 EUR | 6% | 53% |
| puesto en el ranking | bajo | 64 | -2.19 EUR | 8% | 52% |
| puesto en el ranking | medio | 64 | -3.70 EUR | 2% | 59% |
| puesto en el ranking | alto | 64 | -4.19 EUR | 0% | 61% |
| potencial hasta objetivo | bajo | 64 | -3.81 EUR | 3% | 58% |
| potencial hasta objetivo | medio | 64 | -3.93 EUR | 2% | 62% |
| potencial hasta objetivo | alto | 64 | -2.35 EUR | 5% | 52% |
| dispersion | bajo | 64 | -2.32 EUR | 6% | 52% |
| dispersion | medio | 64 | -4.57 EUR | 2% | 67% |
| dispersion | alto | 64 | -3.19 EUR | 2% | 53% |
| % compra fuerte | bajo | 60 | -4.35 EUR | 2% | 63% |
| % compra fuerte | medio | 60 | -2.90 EUR | 2% | 57% |
| % compra fuerte | alto | 60 | -3.37 EUR | 3% | 53% |
| momentum 30d | bajo | 64 | -2.72 EUR | 5% | 52% |
| momentum 30d | medio | 64 | -3.74 EUR | 2% | 61% |
| momentum 30d | alto | 64 | -3.62 EUR | 3% | 59% |
| fuerza relativa | bajo | 64 | -3.10 EUR | 5% | 58% |
| fuerza relativa | medio | 64 | -3.62 EUR | 0% | 55% |
| fuerza relativa | alto | 64 | -3.36 EUR | 5% | 59% |
| RSI | bajo | 64 | -2.52 EUR | 6% | 50% |
| RSI | medio | 64 | -3.41 EUR | 2% | 58% |
| RSI | alto | 64 | -4.15 EUR | 2% | 64% |
| volumen relativo | bajo | 58 | -3.32 EUR | 5% | 62% |
| volumen relativo | medio | 58 | -2.78 EUR | 0% | 43% |
| volumen relativo | alto | 59 | -4.05 EUR | 3% | 61% |
| volatilidad | bajo | 58 | -3.98 EUR | 0% | 59% |
| volatilidad | medio | 58 | -3.63 EUR | 3% | 55% |
| volatilidad | alto | 59 | -2.57 EUR | 5% | 53% |
| liquidez | bajo | 58 | -3.59 EUR | 2% | 57% |
| liquidez | medio | 58 | -3.09 EUR | 5% | 57% |
| liquidez | alto | 59 | -3.48 EUR | 2% | 53% |
| distancia max 52s | bajo | 58 | -2.34 EUR | 7% | 52% |
| distancia max 52s | medio | 58 | -3.55 EUR | 0% | 55% |
| distancia max 52s | alto | 59 | -4.26 EUR | 2% | 59% |
| consenso | buy | 136 | -3.77 EUR | 2% | 59% |
| consenso | strong_buy | 56 | -2.38 EUR | 5% | 54% |
| tendencia tecnica | alcista | 102 | -3.69 EUR | 3% | 59% |
| tendencia tecnica | mixta | 49 | -2.90 EUR | 2% | 53% |
| tendencia tecnica | bajista | 41 | -3.08 EUR | 5% | 59% |
| tendencia analistas | mejorando | 95 | -3.35 EUR | 3% | 57% |
| tendencia analistas | estable | 58 | -4.06 EUR | 3% | 67% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 104 | -3.56 EUR | 4% | 62% |
| regimen de mercado | neutro | 88 | -3.12 EUR | 2% | 51% |
| catalizador | sin catalizador | 191 | -3.34 EUR | 3% | 57% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.81 | -2.35 | **+1.46 EUR** |
| volatilidad | -3.98 | -2.57 | **+1.42 EUR** |
| nota global | -3.56 | -2.40 | **+1.17 EUR** |
| % compra fuerte | -4.35 | -3.37 | **+0.98 EUR** |
| liquidez | -3.59 | -3.48 | **+0.11 EUR** |
| fuerza relativa | -3.10 | -3.36 | **-0.26 EUR** |
| volumen relativo | -3.32 | -4.05 | **-0.73 EUR** |
| dispersion | -2.32 | -3.19 | **-0.87 EUR** |
| momentum 30d | -2.72 | -3.62 | **-0.90 EUR** |
| RSI | -2.52 | -4.15 | **-1.64 EUR** |
| distancia max 52s | -2.34 | -4.26 | **-1.91 EUR** |
| puesto en el ranking | -2.19 | -4.19 | **-2.00 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
