# Simulacion en paralelo

Actualizado: 2026-11-18 15:33 · dia 87 de ejecucion
Proxima revision de ponderacion en 3 dias.

- Operaciones cerradas: **362**
- Operaciones abiertas: 60

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 17 | 5% | +8.65 EUR |
| flojo | 160 | 44% | +1.29 EUR |
| plano | 18 | 5% | -1.74 EUR |
| perdida | 90 | 25% | -7.21 EUR |
| nefasta | 73 | 20% | -7.33 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 69 | -1.63% | 5/69 (7%) | 14/69 | 10 |
| 11-20 | 94 | -2.18% | 8/94 (9%) | 16/94 | 9 |
| 21-30 | 199 | -2.40% | 8/199 (4%) | 32/199 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 25 | -0.23% | +0.19% | **-0.41%** | 11/25 (44%) |
| 11-20 | 44 | -0.52% | -0.04% | **-0.48%** | 24/44 (55%) |
| 21-30 | 109 | -0.62% | -0.02% | **-0.60%** | 55/109 (50%) |

**En conjunto:** -0.54% de media frente a +0.00% del indice, una diferencia de **-0.55%**. 90 de 178 operaciones (51%) batieron a su indice.

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
| escalera + stop vol x4 | -0.47% | 167 | -77.73 EUR | 15/167 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.18% | 185 | -217.69 EUR | 13/185 | -10.63 EUR |
| escalera + stop vol x3 | -1.22% | 180 | -218.87 EUR | 13/180 | -12.76 EUR |
| trailing pegado (3%) | -1.32% | 139 | -182.95 EUR | 19/139 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.20% | 362 | -795.79 EUR | 21/362 | -8.08 EUR |
| arranca antes (+3%) | -2.73% | 115 | -314.42 EUR | 15/115 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.77% | 106 | -294.04 EUR | 15/106 | -10.00 EUR |
| arranca despues (+8%) | -2.93% | 97 | -283.91 EUR | 15/97 | -10.00 EUR |
| trailing suelto (7%) | -3.36% | 96 | -322.66 EUR | 14/96 | -10.00 EUR |
| sin trailing, solo stop | -3.74% | 90 | -336.96 EUR | 12/90 | -10.00 EUR |
| stop corto (5%) | -4.69% | 216 | -1012.65 EUR | 14/216 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.20%**
- Aciertos (>= 5 EUR limpios): 21/362 (6%)
- Resultado acumulado ficticio: -795.79 EUR sobre 362 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 120 | -1.46 EUR | 4% | 33% |
| nota global | medio | 120 | -3.13 EUR | 5% | 52% |
| nota global | alto | 122 | -2.01 EUR | 8% | 49% |
| puesto en el ranking | bajo | 120 | -2.06 EUR | 7% | 48% |
| puesto en el ranking | medio | 120 | -2.40 EUR | 7% | 47% |
| puesto en el ranking | alto | 122 | -2.14 EUR | 4% | 41% |
| potencial hasta objetivo | bajo | 120 | -2.49 EUR | 5% | 45% |
| potencial hasta objetivo | medio | 120 | -2.34 EUR | 4% | 46% |
| potencial hasta objetivo | alto | 122 | -1.77 EUR | 8% | 44% |
| dispersion | bajo | 120 | -2.18 EUR | 7% | 48% |
| dispersion | medio | 120 | -2.47 EUR | 5% | 45% |
| dispersion | alto | 122 | -1.95 EUR | 6% | 42% |
| % compra fuerte | bajo | 114 | -2.59 EUR | 4% | 46% |
| % compra fuerte | medio | 114 | -1.75 EUR | 8% | 45% |
| % compra fuerte | alto | 114 | -2.29 EUR | 5% | 43% |
| momentum 30d | bajo | 120 | -2.23 EUR | 8% | 47% |
| momentum 30d | medio | 120 | -1.97 EUR | 7% | 44% |
| momentum 30d | alto | 122 | -2.39 EUR | 3% | 44% |
| fuerza relativa | bajo | 120 | -2.50 EUR | 7% | 52% |
| fuerza relativa | medio | 120 | -2.04 EUR | 6% | 42% |
| fuerza relativa | alto | 122 | -2.06 EUR | 5% | 42% |
| RSI | bajo | 120 | -2.41 EUR | 7% | 49% |
| RSI | medio | 120 | -2.22 EUR | 8% | 47% |
| RSI | alto | 122 | -1.98 EUR | 3% | 39% |
| volumen relativo | bajo | 115 | -1.73 EUR | 10% | 45% |
| volumen relativo | medio | 115 | -2.14 EUR | 3% | 40% |
| volumen relativo | alto | 115 | -2.59 EUR | 4% | 45% |
| volatilidad | bajo | 115 | -1.90 EUR | 7% | 40% |
| volatilidad | medio | 115 | -2.08 EUR | 7% | 43% |
| volatilidad | alto | 115 | -2.49 EUR | 3% | 47% |
| liquidez | bajo | 115 | -2.44 EUR | 5% | 47% |
| liquidez | medio | 115 | -2.14 EUR | 6% | 43% |
| liquidez | alto | 115 | -1.89 EUR | 6% | 40% |
| distancia max 52s | bajo | 115 | -1.60 EUR | 7% | 40% |
| distancia max 52s | medio | 115 | -1.96 EUR | 6% | 43% |
| distancia max 52s | alto | 115 | -2.91 EUR | 4% | 48% |
| consenso | buy | 254 | -2.15 EUR | 6% | 43% |
| consenso | strong_buy | 108 | -2.31 EUR | 6% | 49% |
| tendencia tecnica | alcista | 173 | -2.52 EUR | 5% | 47% |
| tendencia tecnica | mixta | 103 | -2.30 EUR | 5% | 47% |
| tendencia tecnica | bajista | 86 | -1.44 EUR | 8% | 40% |
| tendencia analistas | mejorando | 165 | -2.09 EUR | 5% | 44% |
| tendencia analistas | estable | 121 | -2.58 EUR | 7% | 50% |
| tendencia analistas | empeorando | 15 | -3.07 EUR | 7% | 60% |
| regimen de mercado | neutro | 176 | -1.92 EUR | 8% | 43% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 71 | -1.01 EUR | 4% | 27% |
| catalizador | con catalizador | 13 | -0.47 EUR | 8% | 23% |
| catalizador | sin catalizador | 349 | -2.26 EUR | 6% | 46% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.49 | -1.77 | **+0.71 EUR** |
| liquidez | -2.44 | -1.89 | **+0.55 EUR** |
| fuerza relativa | -2.50 | -2.06 | **+0.45 EUR** |
| RSI | -2.41 | -1.98 | **+0.43 EUR** |
| % compra fuerte | -2.59 | -2.29 | **+0.30 EUR** |
| dispersion | -2.18 | -1.95 | **+0.22 EUR** |
| puesto en el ranking | -2.06 | -2.14 | **-0.08 EUR** |
| momentum 30d | -2.23 | -2.39 | **-0.16 EUR** |
| nota global | -1.46 | -2.01 | **-0.54 EUR** |
| volatilidad | -1.90 | -2.49 | **-0.59 EUR** |
| volumen relativo | -1.73 | -2.59 | **-0.86 EUR** |
| distancia max 52s | -1.60 | -2.91 | **-1.31 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
