# Simulacion en paralelo

Actualizado: 2026-11-10 01:31 · dia 79 de ejecucion
Proxima revision de ponderacion en 11 dias.

- Operaciones cerradas: **317**
- Operaciones abiertas: 62

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 14 | 4% | +8.78 EUR |
| flojo | 127 | 40% | +1.31 EUR |
| plano | 18 | 6% | -1.74 EUR |
| perdida | 88 | 28% | -7.19 EUR |
| nefasta | 66 | 21% | -7.25 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 62 | -1.78% | 5/62 (8%) | 13/62 | 10 |
| 11-20 | 79 | -2.53% | 6/79 (8%) | 11/79 | 9 |
| 21-30 | 176 | -2.71% | 7/176 (4%) | 24/176 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 18 | -0.20% | -0.33% | **+0.13%** | 10/18 (56%) |
| 11-20 | 30 | -0.85% | -0.62% | **-0.23%** | 19/30 (63%) |
| 21-30 | 86 | -0.77% | -0.32% | **-0.45%** | 49/86 (57%) |

**En conjunto:** -0.71% de media frente a -0.39% del indice, una diferencia de **-0.32%**. 78 de 134 operaciones (58%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 52 operaciones, media -0.87%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.86% | 128 | -109.53 EUR | 13/128 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.52% | 144 | -218.56 EUR | 11/144 | -10.63 EUR |
| escalera + stop vol x3 | -1.63% | 140 | -228.69 EUR | 11/140 | -12.76 EUR |
| trailing pegado (3%) | -1.64% | 124 | -203.07 EUR | 16/124 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.48% | 317 | -786.50 EUR | 18/317 | -8.08 EUR |
| arranca antes (+3%) | -2.90% | 107 | -310.18 EUR | 12/107 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.01% | 99 | -298.45 EUR | 12/99 | -10.00 EUR |
| arranca despues (+8%) | -3.19% | 91 | -290.27 EUR | 12/91 | -10.00 EUR |
| trailing suelto (7%) | -3.66% | 90 | -329.02 EUR | 11/90 | -10.00 EUR |
| sin trailing, solo stop | -4.09% | 84 | -343.32 EUR | 9/84 | -10.00 EUR |
| stop corto (5%) | -4.75% | 202 | -960.20 EUR | 12/202 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.48%**
- Aciertos (>= 5 EUR limpios): 18/317 (6%)
- Resultado acumulado ficticio: -786.50 EUR sobre 317 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 105 | -1.95 EUR | 5% | 39% |
| nota global | medio | 105 | -3.25 EUR | 4% | 54% |
| nota global | alto | 107 | -2.25 EUR | 8% | 52% |
| puesto en el ranking | bajo | 105 | -2.22 EUR | 8% | 51% |
| puesto en el ranking | medio | 105 | -2.84 EUR | 6% | 50% |
| puesto en el ranking | alto | 107 | -2.39 EUR | 4% | 44% |
| potencial hasta objetivo | bajo | 105 | -2.89 EUR | 5% | 50% |
| potencial hasta objetivo | medio | 105 | -2.72 EUR | 4% | 50% |
| potencial hasta objetivo | alto | 107 | -1.84 EUR | 8% | 46% |
| dispersion | bajo | 105 | -2.27 EUR | 8% | 50% |
| dispersion | medio | 105 | -2.80 EUR | 5% | 50% |
| dispersion | alto | 107 | -2.38 EUR | 5% | 46% |
| % compra fuerte | bajo | 99 | -2.88 EUR | 3% | 48% |
| % compra fuerte | medio | 99 | -2.11 EUR | 9% | 51% |
| % compra fuerte | alto | 100 | -2.49 EUR | 4% | 45% |
| momentum 30d | bajo | 105 | -2.70 EUR | 6% | 50% |
| momentum 30d | medio | 105 | -1.94 EUR | 7% | 44% |
| momentum 30d | alto | 107 | -2.80 EUR | 5% | 51% |
| fuerza relativa | bajo | 105 | -2.90 EUR | 5% | 53% |
| fuerza relativa | medio | 105 | -2.08 EUR | 7% | 44% |
| fuerza relativa | alto | 107 | -2.46 EUR | 6% | 49% |
| RSI | bajo | 105 | -2.48 EUR | 7% | 50% |
| RSI | medio | 105 | -2.34 EUR | 7% | 50% |
| RSI | alto | 107 | -2.62 EUR | 4% | 47% |
| volumen relativo | bajo | 100 | -1.80 EUR | 10% | 46% |
| volumen relativo | medio | 100 | -2.52 EUR | 3% | 45% |
| volumen relativo | alto | 100 | -3.03 EUR | 4% | 50% |
| volatilidad | bajo | 100 | -2.02 EUR | 7% | 42% |
| volatilidad | medio | 100 | -2.75 EUR | 5% | 49% |
| volatilidad | alto | 100 | -2.57 EUR | 5% | 50% |
| liquidez | bajo | 100 | -3.04 EUR | 4% | 51% |
| liquidez | medio | 100 | -2.10 EUR | 7% | 46% |
| liquidez | alto | 100 | -2.20 EUR | 6% | 44% |
| distancia max 52s | bajo | 100 | -1.87 EUR | 6% | 42% |
| distancia max 52s | medio | 100 | -2.07 EUR | 7% | 46% |
| distancia max 52s | alto | 100 | -3.40 EUR | 4% | 53% |
| consenso | buy | 225 | -2.50 EUR | 5% | 47% |
| consenso | strong_buy | 92 | -2.45 EUR | 7% | 52% |
| tendencia tecnica | alcista | 146 | -2.84 EUR | 5% | 51% |
| tendencia tecnica | mixta | 91 | -2.56 EUR | 5% | 51% |
| tendencia tecnica | bajista | 80 | -1.72 EUR | 8% | 42% |
| tendencia analistas | mejorando | 144 | -2.46 EUR | 4% | 47% |
| tendencia analistas | estable | 109 | -2.75 EUR | 8% | 53% |
| tendencia analistas | empeorando | 13 | -3.00 EUR | 8% | 62% |
| regimen de mercado | neutro | 161 | -2.01 EUR | 7% | 44% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 41 | -1.87 EUR | 5% | 37% |
| catalizador | con catalizador | 8 | -1.39 EUR | 12% | 38% |
| catalizador | sin catalizador | 309 | -2.51 EUR | 6% | 49% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.89 | -1.84 | **+1.05 EUR** |
| liquidez | -3.04 | -2.20 | **+0.84 EUR** |
| fuerza relativa | -2.90 | -2.46 | **+0.43 EUR** |
| % compra fuerte | -2.88 | -2.49 | **+0.39 EUR** |
| momentum 30d | -2.70 | -2.80 | **-0.10 EUR** |
| dispersion | -2.27 | -2.38 | **-0.11 EUR** |
| RSI | -2.48 | -2.62 | **-0.15 EUR** |
| puesto en el ranking | -2.22 | -2.39 | **-0.17 EUR** |
| nota global | -1.95 | -2.25 | **-0.29 EUR** |
| volatilidad | -2.02 | -2.57 | **-0.54 EUR** |
| volumen relativo | -1.80 | -3.03 | **-1.23 EUR** |
| distancia max 52s | -1.87 | -3.40 | **-1.53 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
