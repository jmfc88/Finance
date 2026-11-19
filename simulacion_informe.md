# Simulacion en paralelo

Actualizado: 2026-11-19 15:41 · dia 88 de ejecucion
Proxima revision de ponderacion en 2 dias.

- Operaciones cerradas: **372**
- Operaciones abiertas: 57

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 18 | 5% | +8.53 EUR |
| flojo | 164 | 44% | +1.31 EUR |
| plano | 19 | 5% | -1.76 EUR |
| perdida | 91 | 24% | -7.22 EUR |
| nefasta | 76 | 20% | -7.36 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 70 | -1.72% | 5/70 (7%) | 14/70 | 9 |
| 11-20 | 95 | -2.15% | 8/95 (8%) | 16/95 | 9 |
| 21-30 | 207 | -2.37% | 9/207 (4%) | 36/207 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 26 | -0.53% | +0.03% | **-0.56%** | 11/26 (42%) |
| 11-20 | 45 | -0.49% | -0.03% | **-0.46%** | 25/45 (56%) |
| 21-30 | 117 | -0.68% | -0.08% | **-0.60%** | 59/117 (50%) |

**En conjunto:** -0.61% de media frente a -0.05% del indice, una diferencia de **-0.56%**. 95 de 188 operaciones (51%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 57 operaciones, media -0.38%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.49% | 176 | -85.97 EUR | 16/176 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.13% | 194 | -218.41 EUR | 14/194 | -10.63 EUR |
| escalera + stop vol x3 | -1.17% | 189 | -221.71 EUR | 14/189 | -12.76 EUR |
| trailing pegado (3%) | -1.24% | 146 | -181.04 EUR | 19/146 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.19% | 372 | -814.74 EUR | 22/372 | -8.08 EUR |
| arranca antes (+3%) | -2.71% | 119 | -322.57 EUR | 15/119 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.75% | 110 | -302.19 EUR | 15/110 | -10.00 EUR |
| arranca despues (+8%) | -2.92% | 100 | -292.11 EUR | 15/100 | -10.00 EUR |
| trailing suelto (7%) | -3.33% | 100 | -332.96 EUR | 14/100 | -10.00 EUR |
| sin trailing, solo stop | -3.71% | 93 | -345.16 EUR | 12/93 | -10.00 EUR |
| stop corto (5%) | -4.66% | 223 | -1038.80 EUR | 14/223 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.19%**
- Aciertos (>= 5 EUR limpios): 22/372 (6%)
- Resultado acumulado ficticio: -814.74 EUR sobre 372 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 124 | -1.35 EUR | 5% | 32% |
| nota global | medio | 124 | -3.19 EUR | 5% | 53% |
| nota global | alto | 124 | -2.03 EUR | 8% | 49% |
| puesto en el ranking | bajo | 124 | -2.11 EUR | 6% | 48% |
| puesto en el ranking | medio | 124 | -2.42 EUR | 6% | 47% |
| puesto en el ranking | alto | 124 | -2.05 EUR | 5% | 40% |
| potencial hasta objetivo | bajo | 124 | -2.34 EUR | 6% | 44% |
| potencial hasta objetivo | medio | 124 | -2.38 EUR | 4% | 46% |
| potencial hasta objetivo | alto | 124 | -1.85 EUR | 8% | 45% |
| dispersion | bajo | 124 | -2.01 EUR | 7% | 47% |
| dispersion | medio | 124 | -2.69 EUR | 4% | 47% |
| dispersion | alto | 124 | -1.88 EUR | 6% | 41% |
| % compra fuerte | bajo | 117 | -2.46 EUR | 4% | 44% |
| % compra fuerte | medio | 117 | -1.74 EUR | 8% | 44% |
| % compra fuerte | alto | 118 | -2.41 EUR | 5% | 44% |
| momentum 30d | bajo | 124 | -2.20 EUR | 7% | 47% |
| momentum 30d | medio | 124 | -2.05 EUR | 7% | 44% |
| momentum 30d | alto | 124 | -2.32 EUR | 3% | 44% |
| fuerza relativa | bajo | 124 | -2.61 EUR | 6% | 52% |
| fuerza relativa | medio | 124 | -2.09 EUR | 6% | 43% |
| fuerza relativa | alto | 124 | -1.87 EUR | 5% | 40% |
| RSI | bajo | 124 | -2.30 EUR | 7% | 48% |
| RSI | medio | 124 | -2.54 EUR | 6% | 50% |
| RSI | alto | 124 | -1.73 EUR | 4% | 36% |
| volumen relativo | bajo | 118 | -1.62 EUR | 10% | 44% |
| volumen relativo | medio | 118 | -2.27 EUR | 3% | 42% |
| volumen relativo | alto | 119 | -2.55 EUR | 4% | 45% |
| volatilidad | bajo | 118 | -1.81 EUR | 8% | 40% |
| volatilidad | medio | 118 | -2.05 EUR | 7% | 42% |
| volatilidad | alto | 119 | -2.58 EUR | 3% | 48% |
| liquidez | bajo | 118 | -2.31 EUR | 6% | 46% |
| liquidez | medio | 118 | -2.19 EUR | 6% | 44% |
| liquidez | alto | 119 | -1.95 EUR | 6% | 40% |
| distancia max 52s | bajo | 118 | -1.66 EUR | 7% | 41% |
| distancia max 52s | medio | 118 | -1.99 EUR | 6% | 42% |
| distancia max 52s | alto | 119 | -2.79 EUR | 5% | 47% |
| consenso | buy | 262 | -2.15 EUR | 6% | 43% |
| consenso | strong_buy | 110 | -2.28 EUR | 6% | 49% |
| tendencia tecnica | alcista | 178 | -2.46 EUR | 6% | 46% |
| tendencia tecnica | mixta | 107 | -2.41 EUR | 5% | 48% |
| tendencia tecnica | bajista | 87 | -1.38 EUR | 8% | 39% |
| tendencia analistas | mejorando | 172 | -2.18 EUR | 5% | 44% |
| tendencia analistas | estable | 122 | -2.55 EUR | 7% | 50% |
| tendencia analistas | empeorando | 16 | -2.66 EUR | 6% | 56% |
| regimen de mercado | neutro | 177 | -1.95 EUR | 8% | 44% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 80 | -1.03 EUR | 5% | 28% |
| catalizador | con catalizador | 13 | -0.47 EUR | 8% | 23% |
| catalizador | sin catalizador | 359 | -2.25 EUR | 6% | 46% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| fuerza relativa | -2.61 | -1.87 | **+0.74 EUR** |
| RSI | -2.30 | -1.73 | **+0.57 EUR** |
| potencial hasta objetivo | -2.34 | -1.85 | **+0.48 EUR** |
| liquidez | -2.31 | -1.95 | **+0.36 EUR** |
| dispersion | -2.01 | -1.88 | **+0.13 EUR** |
| puesto en el ranking | -2.11 | -2.05 | **+0.06 EUR** |
| % compra fuerte | -2.46 | -2.41 | **+0.05 EUR** |
| momentum 30d | -2.20 | -2.32 | **-0.12 EUR** |
| nota global | -1.35 | -2.03 | **-0.68 EUR** |
| volatilidad | -1.81 | -2.58 | **-0.77 EUR** |
| volumen relativo | -1.62 | -2.55 | **-0.93 EUR** |
| distancia max 52s | -1.66 | -2.79 | **-1.12 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
