# Simulacion en paralelo

Actualizado: 2026-11-20 08:29 · dia 89 de ejecucion
Proxima revision de ponderacion en 1 dia.

- Operaciones cerradas: **385**
- Operaciones abiertas: 48

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 18 | 5% | +8.53 EUR |
| flojo | 166 | 43% | +1.32 EUR |
| plano | 19 | 5% | -1.76 EUR |
| perdida | 97 | 25% | -7.27 EUR |
| nefasta | 81 | 21% | -7.41 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 73 | -1.82% | 5/73 (7%) | 15/73 | 9 |
| 11-20 | 99 | -2.39% | 8/99 (8%) | 16/99 | 9 |
| 21-30 | 213 | -2.48% | 9/213 (4%) | 37/213 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 29 | -0.91% | -0.42% | **-0.49%** | 12/29 (41%) |
| 11-20 | 49 | -1.11% | -0.44% | **-0.67%** | 25/49 (51%) |
| 21-30 | 123 | -0.97% | -0.25% | **-0.71%** | 60/123 (49%) |

**En conjunto:** -0.99% de media frente a -0.32% del indice, una diferencia de **-0.67%**. 97 de 201 operaciones (48%) batieron a su indice.

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
| escalera + stop vol x4 | -0.52% | 180 | -94.45 EUR | 16/180 | -10.91 EUR |
| trailing pegado (3%) | -1.19% | 147 | -175.47 EUR | 20/147 | -10.00 EUR |
| escalera + stop vol x2.5 | -1.35% | 207 | -279.17 EUR | 14/207 | -10.63 EUR |
| escalera + stop vol x3 | -1.46% | 202 | -295.04 EUR | 14/202 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.34% | 385 | -899.09 EUR | 22/385 | -8.08 EUR |
| arranca antes (+3%) | -2.66% | 120 | -319.22 EUR | 15/120 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.69% | 111 | -298.84 EUR | 15/111 | -10.00 EUR |
| arranca despues (+8%) | -2.86% | 101 | -288.76 EUR | 15/101 | -10.00 EUR |
| trailing suelto (7%) | -3.33% | 100 | -332.96 EUR | 14/100 | -10.00 EUR |
| sin trailing, solo stop | -3.71% | 93 | -345.16 EUR | 12/93 | -10.00 EUR |
| stop corto (5%) | -4.73% | 235 | -1112.45 EUR | 14/235 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.34%**
- Aciertos (>= 5 EUR limpios): 22/385 (6%)
- Resultado acumulado ficticio: -899.09 EUR sobre 385 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 128 | -1.49 EUR | 5% | 34% |
| nota global | medio | 128 | -3.35 EUR | 5% | 55% |
| nota global | alto | 129 | -2.17 EUR | 8% | 50% |
| puesto en el ranking | bajo | 128 | -2.20 EUR | 6% | 48% |
| puesto en el ranking | medio | 128 | -2.66 EUR | 6% | 49% |
| puesto en el ranking | alto | 129 | -2.14 EUR | 5% | 41% |
| potencial hasta objetivo | bajo | 128 | -2.59 EUR | 5% | 46% |
| potencial hasta objetivo | medio | 128 | -2.56 EUR | 4% | 48% |
| potencial hasta objetivo | alto | 129 | -1.87 EUR | 8% | 45% |
| dispersion | bajo | 128 | -2.18 EUR | 7% | 48% |
| dispersion | medio | 128 | -2.71 EUR | 4% | 47% |
| dispersion | alto | 129 | -2.12 EUR | 6% | 43% |
| % compra fuerte | bajo | 121 | -2.57 EUR | 4% | 45% |
| % compra fuerte | medio | 121 | -1.80 EUR | 7% | 45% |
| % compra fuerte | alto | 122 | -2.65 EUR | 5% | 47% |
| momentum 30d | bajo | 128 | -2.24 EUR | 7% | 47% |
| momentum 30d | medio | 128 | -2.22 EUR | 7% | 46% |
| momentum 30d | alto | 129 | -2.54 EUR | 3% | 46% |
| fuerza relativa | bajo | 128 | -2.71 EUR | 6% | 53% |
| fuerza relativa | medio | 128 | -2.21 EUR | 6% | 44% |
| fuerza relativa | alto | 129 | -2.09 EUR | 5% | 42% |
| RSI | bajo | 128 | -2.34 EUR | 7% | 48% |
| RSI | medio | 128 | -2.50 EUR | 7% | 50% |
| RSI | alto | 129 | -2.17 EUR | 3% | 40% |
| volumen relativo | bajo | 122 | -1.91 EUR | 10% | 46% |
| volumen relativo | medio | 122 | -2.29 EUR | 3% | 43% |
| volumen relativo | alto | 124 | -2.70 EUR | 4% | 46% |
| volatilidad | bajo | 122 | -1.82 EUR | 7% | 39% |
| volatilidad | medio | 122 | -2.11 EUR | 7% | 43% |
| volatilidad | alto | 124 | -2.97 EUR | 3% | 52% |
| liquidez | bajo | 122 | -2.59 EUR | 6% | 48% |
| liquidez | medio | 122 | -2.19 EUR | 6% | 44% |
| liquidez | alto | 124 | -2.12 EUR | 6% | 42% |
| distancia max 52s | bajo | 122 | -1.88 EUR | 7% | 43% |
| distancia max 52s | medio | 122 | -2.02 EUR | 6% | 43% |
| distancia max 52s | alto | 124 | -3.00 EUR | 5% | 49% |
| consenso | buy | 272 | -2.37 EUR | 6% | 45% |
| consenso | strong_buy | 113 | -2.25 EUR | 6% | 49% |
| tendencia tecnica | alcista | 185 | -2.67 EUR | 5% | 48% |
| tendencia tecnica | mixta | 111 | -2.53 EUR | 5% | 49% |
| tendencia tecnica | bajista | 89 | -1.40 EUR | 8% | 39% |
| tendencia analistas | mejorando | 180 | -2.38 EUR | 5% | 46% |
| tendencia analistas | estable | 126 | -2.66 EUR | 7% | 51% |
| tendencia analistas | empeorando | 16 | -2.66 EUR | 6% | 56% |
| regimen de mercado | neutro | 181 | -2.04 EUR | 8% | 44% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 89 | -1.62 EUR | 4% | 34% |
| catalizador | con catalizador | 15 | -1.49 EUR | 7% | 33% |
| catalizador | sin catalizador | 370 | -2.37 EUR | 6% | 47% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.59 | -1.87 | **+0.72 EUR** |
| fuerza relativa | -2.71 | -2.09 | **+0.62 EUR** |
| liquidez | -2.59 | -2.12 | **+0.47 EUR** |
| RSI | -2.34 | -2.17 | **+0.17 EUR** |
| puesto en el ranking | -2.20 | -2.14 | **+0.06 EUR** |
| dispersion | -2.18 | -2.12 | **+0.06 EUR** |
| % compra fuerte | -2.57 | -2.65 | **-0.08 EUR** |
| momentum 30d | -2.24 | -2.54 | **-0.30 EUR** |
| nota global | -1.49 | -2.17 | **-0.69 EUR** |
| volumen relativo | -1.91 | -2.70 | **-0.79 EUR** |
| distancia max 52s | -1.88 | -3.00 | **-1.12 EUR** |
| volatilidad | -1.82 | -2.97 | **-1.15 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
