# Simulacion en paralelo

Actualizado: 2026-11-18 08:30 · dia 87 de ejecucion
Proxima revision de ponderacion en 3 dias.

- Operaciones cerradas: **357**
- Operaciones abiertas: 63

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 16 | 4% | +8.70 EUR |
| flojo | 158 | 44% | +1.28 EUR |
| plano | 18 | 5% | -1.74 EUR |
| perdida | 89 | 25% | -7.20 EUR |
| nefasta | 72 | 20% | -7.32 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 68 | -1.54% | 5/68 (7%) | 14/68 | 10 |
| 11-20 | 94 | -2.18% | 8/94 (9%) | 16/94 | 9 |
| 21-30 | 195 | -2.47% | 7/195 (4%) | 29/195 | 8 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 24 | +0.10% | +0.34% | **-0.24%** | 11/24 (46%) |
| 11-20 | 44 | -0.52% | -0.04% | **-0.48%** | 24/44 (55%) |
| 21-30 | 105 | -0.69% | -0.03% | **-0.65%** | 53/105 (50%) |

**En conjunto:** -0.54% de media frente a +0.02% del indice, una diferencia de **-0.55%**. 88 de 173 operaciones (51%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 55 operaciones, media -0.49%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.48% | 162 | -77.18 EUR | 14/162 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.19% | 180 | -213.49 EUR | 12/180 | -10.63 EUR |
| escalera + stop vol x3 | -1.22% | 175 | -212.89 EUR | 12/175 | -12.76 EUR |
| trailing pegado (3%) | -1.44% | 136 | -195.64 EUR | 18/136 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.22% | 357 | -791.89 EUR | 20/357 | -8.08 EUR |
| arranca antes (+3%) | -2.83% | 114 | -322.15 EUR | 14/114 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.87% | 105 | -301.77 EUR | 14/105 | -10.00 EUR |
| arranca despues (+8%) | -3.04% | 96 | -291.64 EUR | 14/96 | -10.00 EUR |
| trailing suelto (7%) | -3.48% | 95 | -330.39 EUR | 13/95 | -10.00 EUR |
| sin trailing, solo stop | -3.87% | 89 | -344.69 EUR | 11/89 | -10.00 EUR |
| stop corto (5%) | -4.72% | 213 | -1006.38 EUR | 13/213 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.22%**
- Aciertos (>= 5 EUR limpios): 20/357 (6%)
- Resultado acumulado ficticio: -791.89 EUR sobre 357 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 119 | -1.58 EUR | 4% | 34% |
| nota global | medio | 119 | -2.94 EUR | 5% | 51% |
| nota global | alto | 119 | -2.14 EUR | 8% | 50% |
| puesto en el ranking | bajo | 119 | -2.01 EUR | 7% | 47% |
| puesto en el ranking | medio | 119 | -2.43 EUR | 7% | 47% |
| puesto en el ranking | alto | 119 | -2.22 EUR | 3% | 41% |
| potencial hasta objetivo | bajo | 119 | -2.52 EUR | 5% | 45% |
| potencial hasta objetivo | medio | 119 | -2.35 EUR | 3% | 45% |
| potencial hasta objetivo | alto | 119 | -1.79 EUR | 8% | 45% |
| dispersion | bajo | 119 | -2.13 EUR | 7% | 48% |
| dispersion | medio | 119 | -2.49 EUR | 5% | 45% |
| dispersion | alto | 119 | -2.03 EUR | 5% | 42% |
| % compra fuerte | bajo | 112 | -2.68 EUR | 4% | 46% |
| % compra fuerte | medio | 112 | -1.72 EUR | 8% | 45% |
| % compra fuerte | alto | 113 | -2.30 EUR | 4% | 42% |
| momentum 30d | bajo | 119 | -2.26 EUR | 8% | 47% |
| momentum 30d | medio | 119 | -2.08 EUR | 6% | 45% |
| momentum 30d | alto | 119 | -2.32 EUR | 3% | 44% |
| fuerza relativa | bajo | 119 | -2.50 EUR | 7% | 51% |
| fuerza relativa | medio | 119 | -2.08 EUR | 5% | 42% |
| fuerza relativa | alto | 119 | -2.08 EUR | 5% | 42% |
| RSI | bajo | 119 | -2.36 EUR | 7% | 49% |
| RSI | medio | 119 | -2.24 EUR | 8% | 47% |
| RSI | alto | 119 | -2.05 EUR | 3% | 39% |
| volumen relativo | bajo | 113 | -1.62 EUR | 10% | 44% |
| volumen relativo | medio | 113 | -2.30 EUR | 4% | 42% |
| volumen relativo | alto | 114 | -2.60 EUR | 4% | 45% |
| volatilidad | bajo | 113 | -1.87 EUR | 7% | 40% |
| volatilidad | medio | 113 | -2.14 EUR | 6% | 43% |
| volatilidad | alto | 114 | -2.52 EUR | 4% | 47% |
| liquidez | bajo | 113 | -2.42 EUR | 5% | 47% |
| liquidez | medio | 113 | -2.20 EUR | 5% | 44% |
| liquidez | alto | 114 | -1.92 EUR | 6% | 39% |
| distancia max 52s | bajo | 113 | -1.79 EUR | 6% | 41% |
| distancia max 52s | medio | 113 | -1.87 EUR | 6% | 42% |
| distancia max 52s | alto | 114 | -2.86 EUR | 4% | 47% |
| consenso | buy | 251 | -2.18 EUR | 6% | 43% |
| consenso | strong_buy | 106 | -2.31 EUR | 6% | 49% |
| tendencia tecnica | alcista | 170 | -2.51 EUR | 5% | 46% |
| tendencia tecnica | mixta | 101 | -2.39 EUR | 5% | 48% |
| tendencia tecnica | bajista | 86 | -1.44 EUR | 8% | 40% |
| tendencia analistas | mejorando | 164 | -2.15 EUR | 5% | 44% |
| tendencia analistas | estable | 118 | -2.62 EUR | 8% | 51% |
| tendencia analistas | empeorando | 14 | -2.72 EUR | 7% | 57% |
| regimen de mercado | neutro | 175 | -1.97 EUR | 7% | 43% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 67 | -0.90 EUR | 4% | 25% |
| catalizador | con catalizador | 13 | -0.47 EUR | 8% | 23% |
| catalizador | sin catalizador | 344 | -2.28 EUR | 6% | 46% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.52 | -1.79 | **+0.73 EUR** |
| liquidez | -2.42 | -1.92 | **+0.50 EUR** |
| fuerza relativa | -2.50 | -2.08 | **+0.42 EUR** |
| % compra fuerte | -2.68 | -2.30 | **+0.38 EUR** |
| RSI | -2.36 | -2.05 | **+0.30 EUR** |
| dispersion | -2.13 | -2.03 | **+0.10 EUR** |
| momentum 30d | -2.26 | -2.32 | **-0.07 EUR** |
| puesto en el ranking | -2.01 | -2.22 | **-0.21 EUR** |
| nota global | -1.58 | -2.14 | **-0.55 EUR** |
| volatilidad | -1.87 | -2.52 | **-0.65 EUR** |
| volumen relativo | -1.62 | -2.60 | **-0.99 EUR** |
| distancia max 52s | -1.79 | -2.86 | **-1.07 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
