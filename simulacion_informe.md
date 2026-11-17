# Simulacion en paralelo

Actualizado: 2026-11-17 18:35 · dia 86 de ejecucion
Proxima revision de ponderacion en 4 dias.

- Operaciones cerradas: **356**
- Operaciones abiertas: 63

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 16 | 4% | +8.70 EUR |
| flojo | 157 | 44% | +1.28 EUR |
| plano | 18 | 5% | -1.74 EUR |
| perdida | 89 | 25% | -7.20 EUR |
| nefasta | 72 | 20% | -7.32 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 68 | -1.54% | 5/68 (7%) | 14/68 | 10 |
| 11-20 | 93 | -2.22% | 8/93 (9%) | 16/93 | 9 |
| 21-30 | 195 | -2.47% | 7/195 (4%) | 29/195 | 8 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 24 | +0.10% | +0.34% | **-0.24%** | 11/24 (46%) |
| 11-20 | 43 | -0.56% | -0.03% | **-0.52%** | 23/43 (53%) |
| 21-30 | 105 | -0.69% | -0.03% | **-0.65%** | 53/105 (50%) |

**En conjunto:** -0.54% de media frente a +0.02% del indice, una diferencia de **-0.56%**. 87 de 172 operaciones (51%) batieron a su indice.

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
| escalera + stop vol x4 | -0.49% | 161 | -78.18 EUR | 14/161 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.20% | 179 | -214.49 EUR | 12/179 | -10.63 EUR |
| escalera + stop vol x3 | -1.23% | 174 | -213.89 EUR | 12/174 | -12.76 EUR |
| trailing pegado (3%) | -1.45% | 135 | -196.32 EUR | 18/135 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.23% | 356 | -792.89 EUR | 20/356 | -8.08 EUR |
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

- Media neta: **-2.23%**
- Aciertos (>= 5 EUR limpios): 20/356 (6%)
- Resultado acumulado ficticio: -792.89 EUR sobre 356 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 118 | -1.53 EUR | 4% | 34% |
| nota global | medio | 118 | -3.18 EUR | 4% | 53% |
| nota global | alto | 120 | -1.98 EUR | 8% | 49% |
| puesto en el ranking | bajo | 118 | -2.01 EUR | 7% | 47% |
| puesto en el ranking | medio | 118 | -2.45 EUR | 7% | 47% |
| puesto en el ranking | alto | 120 | -2.23 EUR | 3% | 42% |
| potencial hasta objetivo | bajo | 118 | -2.55 EUR | 5% | 46% |
| potencial hasta objetivo | medio | 118 | -2.40 EUR | 3% | 46% |
| potencial hasta objetivo | alto | 120 | -1.74 EUR | 8% | 44% |
| dispersion | bajo | 118 | -2.16 EUR | 7% | 48% |
| dispersion | medio | 118 | -2.45 EUR | 5% | 45% |
| dispersion | alto | 120 | -2.08 EUR | 5% | 42% |
| % compra fuerte | bajo | 112 | -2.76 EUR | 4% | 47% |
| % compra fuerte | medio | 112 | -1.64 EUR | 8% | 44% |
| % compra fuerte | alto | 112 | -2.33 EUR | 4% | 43% |
| momentum 30d | bajo | 118 | -2.21 EUR | 8% | 47% |
| momentum 30d | medio | 118 | -2.07 EUR | 6% | 45% |
| momentum 30d | alto | 120 | -2.40 EUR | 3% | 44% |
| fuerza relativa | bajo | 118 | -2.45 EUR | 7% | 51% |
| fuerza relativa | medio | 118 | -2.12 EUR | 5% | 42% |
| fuerza relativa | alto | 120 | -2.11 EUR | 5% | 42% |
| RSI | bajo | 118 | -2.39 EUR | 7% | 49% |
| RSI | medio | 118 | -2.19 EUR | 8% | 47% |
| RSI | alto | 120 | -2.11 EUR | 2% | 40% |
| volumen relativo | bajo | 113 | -1.62 EUR | 10% | 44% |
| volumen relativo | medio | 113 | -2.30 EUR | 4% | 42% |
| volumen relativo | alto | 113 | -2.64 EUR | 4% | 45% |
| volatilidad | bajo | 113 | -1.87 EUR | 7% | 40% |
| volatilidad | medio | 113 | -2.14 EUR | 6% | 43% |
| volatilidad | alto | 113 | -2.55 EUR | 4% | 48% |
| liquidez | bajo | 113 | -2.42 EUR | 5% | 47% |
| liquidez | medio | 113 | -2.28 EUR | 5% | 45% |
| liquidez | alto | 113 | -1.86 EUR | 6% | 39% |
| distancia max 52s | bajo | 113 | -1.79 EUR | 6% | 41% |
| distancia max 52s | medio | 113 | -1.87 EUR | 6% | 42% |
| distancia max 52s | alto | 113 | -2.90 EUR | 4% | 48% |
| consenso | buy | 250 | -2.19 EUR | 6% | 44% |
| consenso | strong_buy | 106 | -2.31 EUR | 6% | 49% |
| tendencia tecnica | alcista | 169 | -2.53 EUR | 5% | 47% |
| tendencia tecnica | mixta | 101 | -2.39 EUR | 5% | 48% |
| tendencia tecnica | bajista | 86 | -1.44 EUR | 8% | 40% |
| tendencia analistas | mejorando | 164 | -2.15 EUR | 5% | 44% |
| tendencia analistas | estable | 118 | -2.62 EUR | 8% | 51% |
| tendencia analistas | empeorando | 14 | -2.72 EUR | 7% | 57% |
| regimen de mercado | neutro | 175 | -1.97 EUR | 7% | 43% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 66 | -0.93 EUR | 5% | 26% |
| catalizador | con catalizador | 12 | -0.60 EUR | 8% | 25% |
| catalizador | sin catalizador | 344 | -2.28 EUR | 6% | 46% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.55 | -1.74 | **+0.80 EUR** |
| liquidez | -2.42 | -1.86 | **+0.56 EUR** |
| % compra fuerte | -2.76 | -2.33 | **+0.43 EUR** |
| fuerza relativa | -2.45 | -2.11 | **+0.34 EUR** |
| RSI | -2.39 | -2.11 | **+0.28 EUR** |
| dispersion | -2.16 | -2.08 | **+0.07 EUR** |
| momentum 30d | -2.21 | -2.40 | **-0.19 EUR** |
| puesto en el ranking | -2.01 | -2.23 | **-0.22 EUR** |
| nota global | -1.53 | -1.98 | **-0.45 EUR** |
| volatilidad | -1.87 | -2.55 | **-0.68 EUR** |
| volumen relativo | -1.62 | -2.64 | **-1.02 EUR** |
| distancia max 52s | -1.79 | -2.90 | **-1.11 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
