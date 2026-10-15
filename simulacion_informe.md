# Simulacion en paralelo

Actualizado: 2026-10-15 05:53 · dia 53 de ejecucion
Proxima revision de ponderacion en 7 dias.

- Operaciones cerradas: **184**
- Operaciones abiertas: 50

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 58 | 32% | +1.31 EUR |
| plano | 12 | 7% | -1.75 EUR |
| perdida | 68 | 37% | -7.25 EUR |
| nefasta | 41 | 22% | -6.75 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 44 | -2.22% | 2/44 (5%) | 8/44 | 9 |
| 11-20 | 48 | -3.46% | 2/48 (4%) | 3/48 | 9 |
| 21-30 | 92 | -4.31% | 1/92 (1%) | 6/92 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 1 | +1.00% | -1.68% | **+2.68%** | 1/1 (100%) |
| 11-20 | 2 | -8.08% | -0.20% | **-7.88%** | 0/2 (0%) |
| 21-30 | 8 | -4.36% | -0.34% | **-4.02%** | 3/8 (38%) |

**En conjunto:** -4.55% de media frente a -0.43% del indice, una diferencia de **-4.11%**. 4 de 11 operaciones (36%) batieron a su indice.

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
| escalera + stop vol x4 | -1.08% | 6 | -6.47 EUR | 0/6 | -6.59 EUR |
| trailing pegado (3%) | -2.95% | 56 | -165.04 EUR | 3/56 | -10.00 EUR |
| LA REAL (escalera 25/08) | -3.59% | 184 | -660.47 EUR | 5/184 | -8.08 EUR |
| escalera + stop vol x2.5 | -3.82% | 11 | -41.99 EUR | 0/11 | -7.93 EUR |
| arranca antes (+3%) | -4.05% | 51 | -206.40 EUR | 3/51 | -10.00 EUR |
| arranca despues (+8%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| actual (8% / +5% / 5%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| escalera + stop vol x3 | -4.68% | 11 | -51.45 EUR | 0/11 | -9.51 EUR |
| trailing suelto (7%) | -4.95% | 43 | -212.66 EUR | 2/43 | -10.00 EUR |
| sin trailing, solo stop | -5.35% | 42 | -224.72 EUR | 1/42 | -10.00 EUR |
| stop corto (5%) | -5.76% | 123 | -708.56 EUR | 3/123 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.59%**
- Aciertos (>= 5 EUR limpios): 5/184 (3%)
- Resultado acumulado ficticio: -660.47 EUR sobre 184 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 61 | -3.79 EUR | 0% | 54% |
| nota global | medio | 61 | -4.22 EUR | 3% | 67% |
| nota global | alto | 62 | -2.77 EUR | 5% | 56% |
| puesto en el ranking | bajo | 61 | -2.47 EUR | 7% | 52% |
| puesto en el ranking | medio | 61 | -3.93 EUR | 2% | 62% |
| puesto en el ranking | alto | 62 | -4.36 EUR | 0% | 63% |
| potencial hasta objetivo | bajo | 61 | -3.97 EUR | 3% | 57% |
| potencial hasta objetivo | medio | 61 | -3.80 EUR | 2% | 64% |
| potencial hasta objetivo | alto | 62 | -3.01 EUR | 3% | 56% |
| dispersion | bajo | 61 | -2.68 EUR | 5% | 52% |
| dispersion | medio | 61 | -4.62 EUR | 2% | 69% |
| dispersion | alto | 62 | -3.47 EUR | 2% | 56% |
| % compra fuerte | bajo | 57 | -4.37 EUR | 2% | 63% |
| % compra fuerte | medio | 57 | -3.04 EUR | 2% | 60% |
| % compra fuerte | alto | 59 | -3.60 EUR | 3% | 56% |
| momentum 30d | bajo | 61 | -3.47 EUR | 3% | 57% |
| momentum 30d | medio | 61 | -3.57 EUR | 2% | 59% |
| momentum 30d | alto | 62 | -3.72 EUR | 3% | 61% |
| fuerza relativa | bajo | 61 | -3.66 EUR | 3% | 62% |
| fuerza relativa | medio | 61 | -3.76 EUR | 0% | 56% |
| fuerza relativa | alto | 62 | -3.36 EUR | 5% | 60% |
| RSI | bajo | 61 | -3.11 EUR | 5% | 56% |
| RSI | medio | 61 | -3.48 EUR | 2% | 57% |
| RSI | alto | 62 | -4.17 EUR | 2% | 65% |
| volumen relativo | bajo | 55 | -3.86 EUR | 4% | 65% |
| volumen relativo | medio | 55 | -3.05 EUR | 0% | 45% |
| volumen relativo | alto | 57 | -4.01 EUR | 4% | 61% |
| volatilidad | bajo | 55 | -4.26 EUR | 0% | 60% |
| volatilidad | medio | 55 | -4.18 EUR | 2% | 60% |
| volatilidad | alto | 57 | -2.53 EUR | 5% | 53% |
| liquidez | bajo | 55 | -3.52 EUR | 2% | 56% |
| liquidez | medio | 55 | -3.77 EUR | 4% | 62% |
| liquidez | alto | 57 | -3.64 EUR | 2% | 54% |
| distancia max 52s | bajo | 55 | -2.66 EUR | 5% | 53% |
| distancia max 52s | medio | 55 | -3.97 EUR | 0% | 60% |
| distancia max 52s | alto | 57 | -4.28 EUR | 2% | 60% |
| consenso | buy | 130 | -3.99 EUR | 2% | 62% |
| consenso | strong_buy | 54 | -2.64 EUR | 4% | 54% |
| tendencia tecnica | alcista | 101 | -3.74 EUR | 3% | 59% |
| tendencia tecnica | mixta | 46 | -2.96 EUR | 2% | 54% |
| tendencia tecnica | bajista | 37 | -3.96 EUR | 3% | 65% |
| tendencia analistas | mejorando | 88 | -3.59 EUR | 3% | 60% |
| tendencia analistas | estable | 57 | -4.43 EUR | 2% | 68% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 102 | -3.56 EUR | 4% | 63% |
| regimen de mercado | neutro | 82 | -3.62 EUR | 1% | 55% |
| catalizador | sin catalizador | 183 | -3.56 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.26 | -2.53 | **+1.72 EUR** |
| nota global | -3.79 | -2.77 | **+1.02 EUR** |
| potencial hasta objetivo | -3.97 | -3.01 | **+0.96 EUR** |
| % compra fuerte | -4.37 | -3.60 | **+0.77 EUR** |
| fuerza relativa | -3.66 | -3.36 | **+0.30 EUR** |
| liquidez | -3.52 | -3.64 | **-0.12 EUR** |
| volumen relativo | -3.86 | -4.01 | **-0.15 EUR** |
| momentum 30d | -3.47 | -3.72 | **-0.25 EUR** |
| dispersion | -2.68 | -3.47 | **-0.80 EUR** |
| RSI | -3.11 | -4.17 | **-1.07 EUR** |
| distancia max 52s | -2.66 | -4.28 | **-1.62 EUR** |
| puesto en el ranking | -2.47 | -4.36 | **-1.89 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
