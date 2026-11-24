# Simulacion en paralelo

Actualizado: 2026-11-24 17:35 · dia 93 de ejecucion
Proxima revision de ponderacion en 12 dias.

- Operaciones cerradas: **396**
- Operaciones abiertas: 54

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 18 | 5% | +8.53 EUR |
| flojo | 169 | 43% | +1.32 EUR |
| plano | 19 | 5% | -1.76 EUR |
| perdida | 102 | 26% | -7.28 EUR |
| nefasta | 84 | 21% | -7.43 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 78 | -2.07% | 5/78 (6%) | 15/78 | 9 |
| 11-20 | 103 | -2.52% | 8/103 (8%) | 17/103 | 9 |
| 21-30 | 215 | -2.49% | 9/215 (4%) | 37/215 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 34 | -1.60% | -0.75% | **-0.86%** | 12/34 (35%) |
| 11-20 | 53 | -1.46% | -0.72% | **-0.74%** | 26/53 (49%) |
| 21-30 | 125 | -1.01% | -0.28% | **-0.73%** | 60/125 (48%) |

**En conjunto:** -1.22% de media frente a -0.46% del indice, una diferencia de **-0.76%**. 98 de 212 operaciones (46%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 58 operaciones, media -0.45%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.73% | 189 | -137.14 EUR | 16/189 | -10.91 EUR |
| trailing pegado (3%) | -1.32% | 151 | -198.80 EUR | 20/151 | -10.00 EUR |
| escalera + stop vol x2.5 | -1.47% | 217 | -318.07 EUR | 14/217 | -10.63 EUR |
| escalera + stop vol x3 | -1.58% | 212 | -334.10 EUR | 14/212 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.42% | 396 | -957.59 EUR | 22/396 | -8.08 EUR |
| arranca antes (+3%) | -2.80% | 123 | -344.16 EUR | 15/123 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.84% | 114 | -323.78 EUR | 15/114 | -10.00 EUR |
| arranca despues (+8%) | -3.02% | 104 | -313.70 EUR | 15/104 | -10.00 EUR |
| trailing suelto (7%) | -3.47% | 103 | -357.90 EUR | 14/103 | -10.00 EUR |
| sin trailing, solo stop | -3.86% | 96 | -370.10 EUR | 12/96 | -10.00 EUR |
| stop corto (5%) | -4.80% | 243 | -1166.39 EUR | 14/243 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.42%**
- Aciertos (>= 5 EUR limpios): 22/396 (6%)
- Resultado acumulado ficticio: -957.59 EUR sobre 396 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 132 | -1.62 EUR | 5% | 35% |
| nota global | medio | 132 | -3.10 EUR | 5% | 53% |
| nota global | alto | 132 | -2.54 EUR | 7% | 53% |
| puesto en el ranking | bajo | 132 | -2.29 EUR | 6% | 49% |
| puesto en el ranking | medio | 132 | -2.83 EUR | 6% | 51% |
| puesto en el ranking | alto | 132 | -2.14 EUR | 5% | 41% |
| potencial hasta objetivo | bajo | 132 | -2.65 EUR | 5% | 47% |
| potencial hasta objetivo | medio | 132 | -2.62 EUR | 4% | 48% |
| potencial hasta objetivo | alto | 132 | -1.98 EUR | 8% | 46% |
| dispersion | bajo | 132 | -2.38 EUR | 6% | 50% |
| dispersion | medio | 132 | -2.71 EUR | 5% | 47% |
| dispersion | alto | 132 | -2.17 EUR | 6% | 44% |
| % compra fuerte | bajo | 124 | -2.70 EUR | 4% | 47% |
| % compra fuerte | medio | 124 | -1.87 EUR | 7% | 45% |
| % compra fuerte | alto | 125 | -2.64 EUR | 5% | 46% |
| momentum 30d | bajo | 132 | -2.28 EUR | 7% | 47% |
| momentum 30d | medio | 132 | -2.20 EUR | 7% | 45% |
| momentum 30d | alto | 132 | -2.78 EUR | 3% | 48% |
| fuerza relativa | bajo | 132 | -2.67 EUR | 6% | 52% |
| fuerza relativa | medio | 132 | -2.39 EUR | 6% | 45% |
| fuerza relativa | alto | 132 | -2.20 EUR | 5% | 43% |
| RSI | bajo | 132 | -2.22 EUR | 7% | 47% |
| RSI | medio | 132 | -2.55 EUR | 7% | 50% |
| RSI | alto | 132 | -2.49 EUR | 3% | 44% |
| volumen relativo | bajo | 126 | -2.03 EUR | 10% | 47% |
| volumen relativo | medio | 126 | -2.31 EUR | 3% | 43% |
| volumen relativo | alto | 127 | -2.83 EUR | 4% | 47% |
| volatilidad | bajo | 126 | -1.92 EUR | 7% | 40% |
| volatilidad | medio | 126 | -2.19 EUR | 6% | 44% |
| volatilidad | alto | 127 | -3.06 EUR | 3% | 52% |
| liquidez | bajo | 126 | -2.60 EUR | 6% | 48% |
| liquidez | medio | 126 | -2.30 EUR | 6% | 45% |
| liquidez | alto | 127 | -2.26 EUR | 6% | 43% |
| distancia max 52s | bajo | 126 | -1.86 EUR | 6% | 42% |
| distancia max 52s | medio | 126 | -2.21 EUR | 6% | 44% |
| distancia max 52s | alto | 127 | -3.09 EUR | 5% | 50% |
| consenso | buy | 279 | -2.42 EUR | 5% | 46% |
| consenso | strong_buy | 117 | -2.42 EUR | 6% | 50% |
| tendencia tecnica | alcista | 192 | -2.76 EUR | 5% | 49% |
| tendencia tecnica | mixta | 114 | -2.68 EUR | 4% | 50% |
| tendencia tecnica | bajista | 90 | -1.37 EUR | 8% | 39% |
| tendencia analistas | mejorando | 182 | -2.39 EUR | 5% | 46% |
| tendencia analistas | estable | 131 | -2.77 EUR | 7% | 52% |
| tendencia analistas | empeorando | 16 | -2.66 EUR | 6% | 56% |
| regimen de mercado | neutro | 182 | -2.05 EUR | 8% | 45% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 99 | -1.99 EUR | 4% | 37% |
| catalizador | con catalizador | 16 | -1.90 EUR | 6% | 38% |
| catalizador | sin catalizador | 380 | -2.44 EUR | 6% | 47% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.65 | -1.98 | **+0.67 EUR** |
| fuerza relativa | -2.67 | -2.20 | **+0.47 EUR** |
| liquidez | -2.60 | -2.26 | **+0.34 EUR** |
| dispersion | -2.38 | -2.17 | **+0.21 EUR** |
| puesto en el ranking | -2.29 | -2.14 | **+0.15 EUR** |
| % compra fuerte | -2.70 | -2.64 | **+0.06 EUR** |
| RSI | -2.22 | -2.49 | **-0.26 EUR** |
| momentum 30d | -2.28 | -2.78 | **-0.50 EUR** |
| volumen relativo | -2.03 | -2.83 | **-0.79 EUR** |
| nota global | -1.62 | -2.54 | **-0.92 EUR** |
| volatilidad | -1.92 | -3.06 | **-1.13 EUR** |
| distancia max 52s | -1.86 | -3.09 | **-1.24 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
