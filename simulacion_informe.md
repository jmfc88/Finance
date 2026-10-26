# Simulacion en paralelo

Actualizado: 2026-10-26 06:07 · dia 64 de ejecucion
Proxima revision de ponderacion en 11 dias.

- Operaciones cerradas: **229**
- Operaciones abiertas: 61

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 1% | +16.90 EUR |
| beneficio | 3 | 1% | +7.07 EUR |
| flojo | 77 | 34% | +1.32 EUR |
| plano | 14 | 6% | -1.76 EUR |
| perdida | 79 | 34% | -7.22 EUR |
| nefasta | 53 | 23% | -7.05 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 49 | -2.13% | 3/49 (6%) | 9/49 | 10 |
| 11-20 | 58 | -3.28% | 2/58 (3%) | 5/58 | 9 |
| 21-30 | 122 | -4.10% | 1/122 (1%) | 9/122 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 6 | -0.96% | -1.91% | **+0.95%** | 2/6 (33%) |
| 11-20 | 12 | -3.33% | -0.88% | **-2.44%** | 6/12 (50%) |
| 21-30 | 34 | -3.14% | -1.18% | **-1.96%** | 17/34 (50%) |

**En conjunto:** -2.93% de media frente a -1.19% del indice, una diferencia de **-1.74%**. 25 de 52 operaciones (48%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 37 operaciones, media -2.43%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| trailing pegado (3%) | -2.79% | 77 | -215.02 EUR | 4/77 | -10.00 EUR |
| escalera + stop vol x4 | -2.86% | 45 | -128.70 EUR | 1/45 | -10.34 EUR |
| escalera + stop vol x2.5 | -2.92% | 56 | -163.79 EUR | 1/56 | -7.93 EUR |
| escalera + stop vol x3 | -3.41% | 55 | -187.69 EUR | 1/55 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.47% | 229 | -795.19 EUR | 6/229 | -8.08 EUR |
| arranca antes (+3%) | -3.89% | 68 | -264.31 EUR | 4/68 | -10.00 EUR |
| actual (8% / +5% / 5%) | -4.09% | 62 | -253.34 EUR | 4/62 | -10.00 EUR |
| arranca despues (+8%) | -4.12% | 61 | -251.28 EUR | 4/61 | -10.00 EUR |
| trailing suelto (7%) | -4.69% | 59 | -276.59 EUR | 3/59 | -10.00 EUR |
| sin trailing, solo stop | -5.04% | 57 | -287.37 EUR | 2/57 | -10.00 EUR |
| stop corto (5%) | -5.59% | 154 | -860.99 EUR | 4/154 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.47%**
- Aciertos (>= 5 EUR limpios): 6/229 (3%)
- Resultado acumulado ficticio: -795.19 EUR sobre 229 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 76 | -3.49 EUR | 0% | 50% |
| nota global | medio | 76 | -4.21 EUR | 3% | 67% |
| nota global | alto | 77 | -2.73 EUR | 5% | 56% |
| puesto en el ranking | bajo | 76 | -2.37 EUR | 7% | 55% |
| puesto en el ranking | medio | 76 | -4.02 EUR | 1% | 59% |
| puesto en el ranking | alto | 77 | -4.02 EUR | 0% | 58% |
| potencial hasta objetivo | bajo | 76 | -3.71 EUR | 3% | 57% |
| potencial hasta objetivo | medio | 76 | -3.90 EUR | 1% | 62% |
| potencial hasta objetivo | alto | 77 | -2.82 EUR | 4% | 55% |
| dispersion | bajo | 76 | -2.92 EUR | 5% | 57% |
| dispersion | medio | 76 | -4.29 EUR | 1% | 64% |
| dispersion | alto | 77 | -3.22 EUR | 1% | 52% |
| % compra fuerte | bajo | 71 | -3.93 EUR | 1% | 59% |
| % compra fuerte | medio | 71 | -3.06 EUR | 1% | 56% |
| % compra fuerte | alto | 71 | -3.64 EUR | 3% | 56% |
| momentum 30d | bajo | 76 | -3.60 EUR | 4% | 59% |
| momentum 30d | medio | 76 | -3.45 EUR | 0% | 55% |
| momentum 30d | alto | 77 | -3.37 EUR | 4% | 58% |
| fuerza relativa | bajo | 76 | -3.85 EUR | 3% | 62% |
| fuerza relativa | medio | 76 | -3.34 EUR | 1% | 54% |
| fuerza relativa | alto | 77 | -3.23 EUR | 4% | 57% |
| RSI | bajo | 76 | -2.98 EUR | 5% | 54% |
| RSI | medio | 76 | -3.75 EUR | 1% | 59% |
| RSI | alto | 77 | -3.68 EUR | 1% | 60% |
| volumen relativo | bajo | 70 | -3.62 EUR | 4% | 63% |
| volumen relativo | medio | 70 | -3.21 EUR | 0% | 50% |
| volumen relativo | alto | 72 | -3.67 EUR | 3% | 56% |
| volatilidad | bajo | 70 | -3.60 EUR | 0% | 54% |
| volatilidad | medio | 70 | -3.74 EUR | 3% | 57% |
| volatilidad | alto | 72 | -3.18 EUR | 4% | 57% |
| liquidez | bajo | 70 | -3.45 EUR | 1% | 54% |
| liquidez | medio | 70 | -3.38 EUR | 4% | 59% |
| liquidez | alto | 72 | -3.68 EUR | 1% | 56% |
| distancia max 52s | bajo | 70 | -2.94 EUR | 4% | 53% |
| distancia max 52s | medio | 70 | -3.36 EUR | 1% | 57% |
| distancia max 52s | alto | 72 | -4.20 EUR | 1% | 58% |
| consenso | buy | 159 | -3.65 EUR | 2% | 57% |
| consenso | strong_buy | 70 | -3.06 EUR | 4% | 59% |
| tendencia tecnica | alcista | 110 | -3.61 EUR | 3% | 58% |
| tendencia tecnica | mixta | 65 | -3.50 EUR | 2% | 57% |
| tendencia tecnica | bajista | 54 | -3.16 EUR | 4% | 57% |
| tendencia analistas | mejorando | 112 | -3.47 EUR | 3% | 57% |
| tendencia analistas | estable | 71 | -3.96 EUR | 3% | 65% |
| tendencia analistas | empeorando | 9 | -4.67 EUR | 0% | 78% |
| regimen de mercado | neutro | 119 | -3.39 EUR | 2% | 54% |
| regimen de mercado | favorable | 108 | -3.48 EUR | 4% | 61% |
| catalizador | sin catalizador | 228 | -3.45 EUR | 3% | 57% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.71 | -2.82 | **+0.88 EUR** |
| nota global | -3.49 | -2.73 | **+0.76 EUR** |
| fuerza relativa | -3.85 | -3.23 | **+0.62 EUR** |
| volatilidad | -3.60 | -3.18 | **+0.42 EUR** |
| % compra fuerte | -3.93 | -3.64 | **+0.29 EUR** |
| momentum 30d | -3.60 | -3.37 | **+0.23 EUR** |
| volumen relativo | -3.62 | -3.67 | **-0.05 EUR** |
| liquidez | -3.45 | -3.68 | **-0.23 EUR** |
| dispersion | -2.92 | -3.22 | **-0.30 EUR** |
| RSI | -2.98 | -3.68 | **-0.70 EUR** |
| distancia max 52s | -2.94 | -4.20 | **-1.26 EUR** |
| puesto en el ranking | -2.37 | -4.02 | **-1.65 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
