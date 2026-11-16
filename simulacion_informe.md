# Simulacion en paralelo

Actualizado: 2026-11-16 22:53 · dia 85 de ejecucion
Proxima revision de ponderacion en 5 dias.

- Operaciones cerradas: **346**
- Operaciones abiertas: 68

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 14 | 4% | +8.78 EUR |
| flojo | 151 | 44% | +1.29 EUR |
| plano | 18 | 5% | -1.74 EUR |
| perdida | 89 | 26% | -7.20 EUR |
| nefasta | 70 | 20% | -7.30 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 66 | -1.61% | 5/66 (8%) | 14/66 | 10 |
| 11-20 | 89 | -2.42% | 6/89 (7%) | 14/89 | 9 |
| 21-30 | 191 | -2.50% | 7/191 (4%) | 28/191 | 8 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 22 | +0.02% | +0.18% | **-0.16%** | 11/22 (50%) |
| 11-20 | 39 | -0.85% | -0.10% | **-0.75%** | 21/39 (54%) |
| 21-30 | 101 | -0.66% | -0.03% | **-0.63%** | 51/101 (50%) |

**En conjunto:** -0.62% de media frente a -0.02% del indice, una diferencia de **-0.60%**. 83 de 162 operaciones (51%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 53 operaciones, media -0.82%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.57% | 153 | -86.75 EUR | 13/153 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.25% | 169 | -211.74 EUR | 11/169 | -10.63 EUR |
| escalera + stop vol x3 | -1.32% | 165 | -217.31 EUR | 11/165 | -12.76 EUR |
| trailing pegado (3%) | -1.63% | 132 | -214.72 EUR | 16/132 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.31% | 346 | -799.07 EUR | 18/346 | -8.08 EUR |
| arranca antes (+3%) | -3.02% | 112 | -338.49 EUR | 12/112 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.09% | 103 | -318.11 EUR | 12/103 | -10.00 EUR |
| arranca despues (+8%) | -3.28% | 94 | -307.98 EUR | 12/94 | -10.00 EUR |
| trailing suelto (7%) | -3.73% | 93 | -346.73 EUR | 11/93 | -10.00 EUR |
| sin trailing, solo stop | -4.15% | 87 | -361.03 EUR | 9/87 | -10.00 EUR |
| stop corto (5%) | -4.76% | 209 | -994.86 EUR | 12/209 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.31%**
- Aciertos (>= 5 EUR limpios): 18/346 (5%)
- Resultado acumulado ficticio: -799.07 EUR sobre 346 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 115 | -1.59 EUR | 4% | 35% |
| nota global | medio | 115 | -3.20 EUR | 3% | 53% |
| nota global | alto | 116 | -2.14 EUR | 8% | 50% |
| puesto en el ranking | bajo | 115 | -2.09 EUR | 7% | 49% |
| puesto en el ranking | medio | 115 | -2.58 EUR | 5% | 47% |
| puesto en el ranking | alto | 116 | -2.26 EUR | 3% | 42% |
| potencial hasta objetivo | bajo | 115 | -2.67 EUR | 4% | 47% |
| potencial hasta objetivo | medio | 115 | -2.50 EUR | 3% | 47% |
| potencial hasta objetivo | alto | 116 | -1.75 EUR | 8% | 44% |
| dispersion | bajo | 115 | -2.22 EUR | 7% | 49% |
| dispersion | medio | 115 | -2.52 EUR | 4% | 46% |
| dispersion | alto | 116 | -2.18 EUR | 4% | 43% |
| % compra fuerte | bajo | 108 | -2.81 EUR | 3% | 47% |
| % compra fuerte | medio | 108 | -1.76 EUR | 8% | 45% |
| % compra fuerte | alto | 110 | -2.42 EUR | 4% | 44% |
| momentum 30d | bajo | 115 | -2.34 EUR | 7% | 48% |
| momentum 30d | medio | 115 | -2.14 EUR | 4% | 43% |
| momentum 30d | alto | 116 | -2.45 EUR | 4% | 47% |
| fuerza relativa | bajo | 115 | -2.51 EUR | 6% | 51% |
| fuerza relativa | medio | 115 | -2.20 EUR | 4% | 43% |
| fuerza relativa | alto | 116 | -2.22 EUR | 5% | 44% |
| RSI | bajo | 115 | -2.37 EUR | 6% | 49% |
| RSI | medio | 115 | -2.35 EUR | 7% | 48% |
| RSI | alto | 116 | -2.21 EUR | 3% | 41% |
| volumen relativo | bajo | 109 | -1.82 EUR | 9% | 45% |
| volumen relativo | medio | 109 | -2.37 EUR | 3% | 43% |
| volumen relativo | alto | 111 | -2.62 EUR | 4% | 45% |
| volatilidad | bajo | 109 | -2.05 EUR | 6% | 41% |
| volatilidad | medio | 109 | -2.31 EUR | 6% | 45% |
| volatilidad | alto | 111 | -2.45 EUR | 4% | 47% |
| liquidez | bajo | 109 | -2.60 EUR | 5% | 48% |
| liquidez | medio | 109 | -2.16 EUR | 6% | 44% |
| liquidez | alto | 111 | -2.05 EUR | 5% | 41% |
| distancia max 52s | bajo | 109 | -1.70 EUR | 6% | 39% |
| distancia max 52s | medio | 109 | -2.03 EUR | 6% | 45% |
| distancia max 52s | alto | 111 | -3.07 EUR | 4% | 49% |
| consenso | buy | 241 | -2.30 EUR | 5% | 44% |
| consenso | strong_buy | 105 | -2.34 EUR | 6% | 50% |
| tendencia tecnica | alcista | 162 | -2.68 EUR | 4% | 48% |
| tendencia tecnica | mixta | 99 | -2.37 EUR | 5% | 47% |
| tendencia tecnica | bajista | 85 | -1.53 EUR | 7% | 40% |
| tendencia analistas | mejorando | 157 | -2.26 EUR | 4% | 45% |
| tendencia analistas | estable | 116 | -2.68 EUR | 8% | 52% |
| tendencia analistas | empeorando | 14 | -2.72 EUR | 7% | 57% |
| regimen de mercado | neutro | 173 | -1.99 EUR | 7% | 43% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 58 | -1.18 EUR | 3% | 28% |
| catalizador | con catalizador | 12 | -0.60 EUR | 8% | 25% |
| catalizador | sin catalizador | 334 | -2.37 EUR | 5% | 47% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.67 | -1.75 | **+0.92 EUR** |
| liquidez | -2.60 | -2.05 | **+0.56 EUR** |
| % compra fuerte | -2.81 | -2.42 | **+0.39 EUR** |
| fuerza relativa | -2.51 | -2.22 | **+0.29 EUR** |
| RSI | -2.37 | -2.21 | **+0.15 EUR** |
| dispersion | -2.22 | -2.18 | **+0.04 EUR** |
| momentum 30d | -2.34 | -2.45 | **-0.11 EUR** |
| puesto en el ranking | -2.09 | -2.26 | **-0.17 EUR** |
| volatilidad | -2.05 | -2.45 | **-0.40 EUR** |
| nota global | -1.59 | -2.14 | **-0.55 EUR** |
| volumen relativo | -1.82 | -2.62 | **-0.80 EUR** |
| distancia max 52s | -1.70 | -3.07 | **-1.38 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
