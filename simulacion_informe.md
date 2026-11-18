# Simulacion en paralelo

Actualizado: 2026-11-18 18:05 · dia 87 de ejecucion
Proxima revision de ponderacion en 3 dias.

- Operaciones cerradas: **363**
- Operaciones abiertas: 64

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 17 | 5% | +8.65 EUR |
| flojo | 160 | 44% | +1.29 EUR |
| plano | 18 | 5% | -1.74 EUR |
| perdida | 91 | 25% | -7.22 EUR |
| nefasta | 73 | 20% | -7.33 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 69 | -1.63% | 5/69 (7%) | 14/69 | 10 |
| 11-20 | 94 | -2.18% | 8/94 (9%) | 16/94 | 9 |
| 21-30 | 200 | -2.43% | 8/200 (4%) | 32/200 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 25 | -0.23% | +0.19% | **-0.41%** | 11/25 (44%) |
| 11-20 | 44 | -0.52% | -0.04% | **-0.48%** | 24/44 (55%) |
| 21-30 | 110 | -0.69% | -0.05% | **-0.64%** | 55/110 (50%) |

**En conjunto:** -0.58% de media frente a -0.01% del indice, una diferencia de **-0.57%**. 90 de 179 operaciones (50%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 56 operaciones, media -0.34%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.51% | 168 | -85.81 EUR | 15/168 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.20% | 186 | -222.74 EUR | 13/186 | -10.63 EUR |
| escalera + stop vol x3 | -1.24% | 181 | -224.93 EUR | 13/181 | -12.76 EUR |
| trailing pegado (3%) | -1.32% | 139 | -182.95 EUR | 19/139 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.21% | 363 | -803.87 EUR | 21/363 | -8.08 EUR |
| arranca antes (+3%) | -2.73% | 115 | -314.42 EUR | 15/115 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.77% | 106 | -294.04 EUR | 15/106 | -10.00 EUR |
| arranca despues (+8%) | -2.93% | 97 | -283.91 EUR | 15/97 | -10.00 EUR |
| trailing suelto (7%) | -3.36% | 96 | -322.66 EUR | 14/96 | -10.00 EUR |
| sin trailing, solo stop | -3.74% | 90 | -336.96 EUR | 12/90 | -10.00 EUR |
| stop corto (5%) | -4.70% | 217 | -1019.65 EUR | 14/217 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.21%**
- Aciertos (>= 5 EUR limpios): 21/363 (6%)
- Resultado acumulado ficticio: -803.87 EUR sobre 363 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 121 | -1.52 EUR | 4% | 34% |
| nota global | medio | 121 | -3.09 EUR | 5% | 52% |
| nota global | alto | 121 | -2.03 EUR | 8% | 50% |
| puesto en el ranking | bajo | 121 | -2.11 EUR | 7% | 48% |
| puesto en el ranking | medio | 121 | -2.45 EUR | 7% | 47% |
| puesto en el ranking | alto | 121 | -2.09 EUR | 4% | 40% |
| potencial hasta objetivo | bajo | 121 | -2.50 EUR | 5% | 45% |
| potencial hasta objetivo | medio | 121 | -2.35 EUR | 4% | 45% |
| potencial hasta objetivo | alto | 121 | -1.80 EUR | 8% | 45% |
| dispersion | bajo | 121 | -2.15 EUR | 7% | 48% |
| dispersion | medio | 121 | -2.57 EUR | 5% | 46% |
| dispersion | alto | 121 | -1.92 EUR | 6% | 41% |
| % compra fuerte | bajo | 114 | -2.59 EUR | 4% | 46% |
| % compra fuerte | medio | 114 | -1.75 EUR | 8% | 45% |
| % compra fuerte | alto | 115 | -2.34 EUR | 5% | 43% |
| momentum 30d | bajo | 121 | -2.20 EUR | 7% | 46% |
| momentum 30d | medio | 121 | -2.02 EUR | 7% | 45% |
| momentum 30d | alto | 121 | -2.42 EUR | 3% | 45% |
| fuerza relativa | bajo | 121 | -2.47 EUR | 7% | 51% |
| fuerza relativa | medio | 121 | -2.09 EUR | 6% | 42% |
| fuerza relativa | alto | 121 | -2.08 EUR | 5% | 42% |
| RSI | bajo | 121 | -2.45 EUR | 7% | 50% |
| RSI | medio | 121 | -2.26 EUR | 7% | 47% |
| RSI | alto | 121 | -1.93 EUR | 3% | 39% |
| volumen relativo | bajo | 115 | -1.73 EUR | 10% | 45% |
| volumen relativo | medio | 115 | -2.22 EUR | 3% | 41% |
| volumen relativo | alto | 116 | -2.56 EUR | 4% | 45% |
| volatilidad | bajo | 115 | -1.90 EUR | 7% | 40% |
| volatilidad | medio | 115 | -2.18 EUR | 7% | 44% |
| volatilidad | alto | 116 | -2.43 EUR | 3% | 47% |
| liquidez | bajo | 115 | -2.44 EUR | 5% | 47% |
| liquidez | medio | 115 | -2.14 EUR | 6% | 43% |
| liquidez | alto | 116 | -1.94 EUR | 6% | 41% |
| distancia max 52s | bajo | 115 | -1.60 EUR | 7% | 40% |
| distancia max 52s | medio | 115 | -2.04 EUR | 6% | 43% |
| distancia max 52s | alto | 116 | -2.87 EUR | 4% | 47% |
| consenso | buy | 255 | -2.17 EUR | 6% | 44% |
| consenso | strong_buy | 108 | -2.31 EUR | 6% | 49% |
| tendencia tecnica | alcista | 173 | -2.52 EUR | 5% | 47% |
| tendencia tecnica | mixta | 104 | -2.36 EUR | 5% | 47% |
| tendencia tecnica | bajista | 86 | -1.44 EUR | 8% | 40% |
| tendencia analistas | mejorando | 166 | -2.12 EUR | 5% | 44% |
| tendencia analistas | estable | 121 | -2.58 EUR | 7% | 50% |
| tendencia analistas | empeorando | 15 | -3.07 EUR | 7% | 60% |
| regimen de mercado | neutro | 176 | -1.92 EUR | 8% | 43% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 72 | -1.11 EUR | 4% | 28% |
| catalizador | con catalizador | 13 | -0.47 EUR | 8% | 23% |
| catalizador | sin catalizador | 350 | -2.28 EUR | 6% | 46% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.50 | -1.80 | **+0.70 EUR** |
| RSI | -2.45 | -1.93 | **+0.52 EUR** |
| liquidez | -2.44 | -1.94 | **+0.50 EUR** |
| fuerza relativa | -2.47 | -2.08 | **+0.39 EUR** |
| % compra fuerte | -2.59 | -2.34 | **+0.25 EUR** |
| dispersion | -2.15 | -1.92 | **+0.23 EUR** |
| puesto en el ranking | -2.11 | -2.09 | **+0.02 EUR** |
| momentum 30d | -2.20 | -2.42 | **-0.22 EUR** |
| nota global | -1.52 | -2.03 | **-0.51 EUR** |
| volatilidad | -1.90 | -2.43 | **-0.54 EUR** |
| volumen relativo | -1.73 | -2.56 | **-0.83 EUR** |
| distancia max 52s | -1.60 | -2.87 | **-1.28 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
