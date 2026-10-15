# Simulacion en paralelo

Actualizado: 2026-10-15 17:46 · dia 53 de ejecucion
Proxima revision de ponderacion en 7 dias.

- Operaciones cerradas: **186**
- Operaciones abiertas: 53

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 59 | 32% | +1.30 EUR |
| plano | 12 | 6% | -1.75 EUR |
| perdida | 68 | 37% | -7.25 EUR |
| nefasta | 42 | 23% | -6.78 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 44 | -2.22% | 2/44 (5%) | 8/44 | 9 |
| 11-20 | 49 | -3.56% | 2/49 (4%) | 3/49 | 9 |
| 21-30 | 93 | -4.25% | 1/93 (1%) | 6/93 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 1 | +1.00% | -1.68% | **+2.68%** | 1/1 (100%) |
| 11-20 | 3 | -8.08% | -0.19% | **-7.89%** | 0/3 (0%) |
| 21-30 | 9 | -3.76% | -0.37% | **-3.39%** | 4/9 (44%) |

**En conjunto:** -4.39% de media frente a -0.43% del indice, una diferencia de **-3.96%**. 5 de 13 operaciones (38%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 29 operaciones, media -3.36%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -1.69% | 8 | -13.55 EUR | 0/8 | -8.08 EUR |
| trailing pegado (3%) | -3.07% | 57 | -175.04 EUR | 3/57 | -10.00 EUR |
| escalera + stop vol x2.5 | -3.54% | 13 | -46.04 EUR | 0/13 | -7.93 EUR |
| LA REAL (escalera 25/08) | -3.59% | 186 | -667.55 EUR | 5/186 | -8.08 EUR |
| arranca antes (+3%) | -4.16% | 52 | -216.40 EUR | 3/52 | -10.00 EUR |
| arranca despues (+8%) | -4.34% | 46 | -199.52 EUR | 3/46 | -10.00 EUR |
| actual (8% / +5% / 5%) | -4.34% | 46 | -199.52 EUR | 3/46 | -10.00 EUR |
| escalera + stop vol x3 | -4.35% | 13 | -56.51 EUR | 0/13 | -9.51 EUR |
| trailing suelto (7%) | -5.06% | 44 | -222.66 EUR | 2/44 | -10.00 EUR |
| sin trailing, solo stop | -5.46% | 43 | -234.72 EUR | 1/43 | -10.00 EUR |
| stop corto (5%) | -5.77% | 124 | -715.56 EUR | 3/124 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.59%**
- Aciertos (>= 5 EUR limpios): 5/186 (3%)
- Resultado acumulado ficticio: -667.55 EUR sobre 186 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 62 | -3.71 EUR | 0% | 53% |
| nota global | medio | 62 | -4.14 EUR | 3% | 68% |
| nota global | alto | 62 | -2.92 EUR | 5% | 56% |
| puesto en el ranking | bajo | 62 | -2.56 EUR | 6% | 53% |
| puesto en el ranking | medio | 62 | -4.00 EUR | 2% | 63% |
| puesto en el ranking | alto | 62 | -4.21 EUR | 0% | 61% |
| potencial hasta objetivo | bajo | 62 | -3.89 EUR | 3% | 58% |
| potencial hasta objetivo | medio | 62 | -3.87 EUR | 2% | 63% |
| potencial hasta objetivo | alto | 62 | -3.01 EUR | 3% | 56% |
| dispersion | bajo | 62 | -2.62 EUR | 5% | 52% |
| dispersion | medio | 62 | -4.68 EUR | 2% | 69% |
| dispersion | alto | 62 | -3.47 EUR | 2% | 56% |
| % compra fuerte | bajo | 58 | -4.28 EUR | 2% | 62% |
| % compra fuerte | medio | 58 | -3.13 EUR | 2% | 60% |
| % compra fuerte | alto | 59 | -3.60 EUR | 3% | 56% |
| momentum 30d | bajo | 62 | -3.40 EUR | 3% | 56% |
| momentum 30d | medio | 62 | -3.64 EUR | 2% | 60% |
| momentum 30d | alto | 62 | -3.72 EUR | 3% | 61% |
| fuerza relativa | bajo | 62 | -3.73 EUR | 3% | 63% |
| fuerza relativa | medio | 62 | -3.68 EUR | 0% | 55% |
| fuerza relativa | alto | 62 | -3.36 EUR | 5% | 60% |
| RSI | bajo | 62 | -3.04 EUR | 5% | 55% |
| RSI | medio | 62 | -3.55 EUR | 2% | 58% |
| RSI | alto | 62 | -4.17 EUR | 2% | 65% |
| volumen relativo | bajo | 56 | -3.77 EUR | 4% | 64% |
| volumen relativo | medio | 56 | -3.14 EUR | 0% | 46% |
| volumen relativo | alto | 57 | -4.01 EUR | 4% | 61% |
| volatilidad | bajo | 56 | -4.16 EUR | 0% | 61% |
| volatilidad | medio | 56 | -4.25 EUR | 2% | 59% |
| volatilidad | alto | 57 | -2.53 EUR | 5% | 53% |
| liquidez | bajo | 56 | -3.60 EUR | 2% | 57% |
| liquidez | medio | 56 | -3.69 EUR | 4% | 61% |
| liquidez | alto | 57 | -3.64 EUR | 2% | 54% |
| distancia max 52s | bajo | 56 | -2.75 EUR | 5% | 54% |
| distancia max 52s | medio | 56 | -3.88 EUR | 0% | 59% |
| distancia max 52s | alto | 57 | -4.28 EUR | 2% | 60% |
| consenso | buy | 131 | -3.95 EUR | 2% | 61% |
| consenso | strong_buy | 55 | -2.73 EUR | 4% | 55% |
| tendencia tecnica | alcista | 101 | -3.74 EUR | 3% | 59% |
| tendencia tecnica | mixta | 47 | -3.07 EUR | 2% | 55% |
| tendencia tecnica | bajista | 38 | -3.83 EUR | 3% | 63% |
| tendencia analistas | mejorando | 90 | -3.59 EUR | 3% | 60% |
| tendencia analistas | estable | 57 | -4.43 EUR | 2% | 68% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 103 | -3.61 EUR | 4% | 63% |
| regimen de mercado | neutro | 83 | -3.57 EUR | 1% | 54% |
| catalizador | sin catalizador | 185 | -3.56 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.16 | -2.53 | **+1.63 EUR** |
| potencial hasta objetivo | -3.89 | -3.01 | **+0.88 EUR** |
| nota global | -3.71 | -2.92 | **+0.79 EUR** |
| % compra fuerte | -4.28 | -3.60 | **+0.68 EUR** |
| fuerza relativa | -3.73 | -3.36 | **+0.37 EUR** |
| liquidez | -3.60 | -3.64 | **-0.04 EUR** |
| volumen relativo | -3.77 | -4.01 | **-0.24 EUR** |
| momentum 30d | -3.40 | -3.72 | **-0.32 EUR** |
| dispersion | -2.62 | -3.47 | **-0.86 EUR** |
| RSI | -3.04 | -4.17 | **-1.13 EUR** |
| distancia max 52s | -2.75 | -4.28 | **-1.53 EUR** |
| puesto en el ranking | -2.56 | -4.21 | **-1.66 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
