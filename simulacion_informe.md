# Simulacion en paralelo

Actualizado: 2026-11-13 14:30 · dia 82 de ejecucion
Proxima revision de ponderacion en 8 dias.

- Operaciones cerradas: **340**
- Operaciones abiertas: 65

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 14 | 4% | +8.78 EUR |
| flojo | 147 | 43% | +1.29 EUR |
| plano | 18 | 5% | -1.74 EUR |
| perdida | 89 | 26% | -7.20 EUR |
| nefasta | 68 | 20% | -7.28 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 66 | -1.61% | 5/66 (8%) | 14/66 | 10 |
| 11-20 | 84 | -2.43% | 6/84 (7%) | 13/84 | 9 |
| 21-30 | 190 | -2.52% | 7/190 (4%) | 28/190 | 8 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 22 | +0.02% | +0.18% | **-0.16%** | 11/22 (50%) |
| 11-20 | 35 | -0.84% | -0.23% | **-0.61%** | 20/35 (57%) |
| 21-30 | 100 | -0.68% | -0.05% | **-0.63%** | 51/100 (51%) |

**En conjunto:** -0.62% de media frente a -0.06% del indice, una diferencia de **-0.56%**. 82 de 157 operaciones (52%) batieron a su indice.

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
| escalera + stop vol x4 | -0.62% | 149 | -92.04 EUR | 13/149 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.24% | 165 | -205.10 EUR | 11/165 | -10.63 EUR |
| escalera + stop vol x3 | -1.34% | 161 | -215.67 EUR | 11/161 | -12.76 EUR |
| trailing pegado (3%) | -1.59% | 130 | -207.01 EUR | 16/130 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.32% | 340 | -788.20 EUR | 18/340 | -8.08 EUR |
| arranca antes (+3%) | -2.96% | 109 | -322.13 EUR | 12/109 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.07% | 101 | -310.40 EUR | 12/101 | -10.00 EUR |
| arranca despues (+8%) | -3.26% | 92 | -300.27 EUR | 12/92 | -10.00 EUR |
| trailing suelto (7%) | -3.73% | 91 | -339.02 EUR | 11/91 | -10.00 EUR |
| sin trailing, solo stop | -4.16% | 85 | -353.32 EUR | 9/85 | -10.00 EUR |
| stop corto (5%) | -4.77% | 206 | -983.15 EUR | 12/206 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.32%**
- Aciertos (>= 5 EUR limpios): 18/340 (5%)
- Resultado acumulado ficticio: -788.20 EUR sobre 340 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 113 | -1.56 EUR | 4% | 35% |
| nota global | medio | 113 | -3.41 EUR | 3% | 54% |
| nota global | alto | 114 | -1.99 EUR | 9% | 50% |
| puesto en el ranking | bajo | 113 | -2.07 EUR | 7% | 49% |
| puesto en el ranking | medio | 113 | -2.60 EUR | 5% | 48% |
| puesto en el ranking | alto | 114 | -2.28 EUR | 4% | 42% |
| potencial hasta objetivo | bajo | 113 | -2.70 EUR | 4% | 47% |
| potencial hasta objetivo | medio | 113 | -2.54 EUR | 4% | 48% |
| potencial hasta objetivo | alto | 114 | -1.72 EUR | 8% | 44% |
| dispersion | bajo | 113 | -2.20 EUR | 7% | 49% |
| dispersion | medio | 113 | -2.51 EUR | 4% | 46% |
| dispersion | alto | 114 | -2.25 EUR | 4% | 44% |
| % compra fuerte | bajo | 106 | -2.88 EUR | 3% | 48% |
| % compra fuerte | medio | 106 | -1.74 EUR | 8% | 45% |
| % compra fuerte | alto | 108 | -2.40 EUR | 4% | 44% |
| momentum 30d | bajo | 113 | -2.42 EUR | 7% | 49% |
| momentum 30d | medio | 113 | -2.07 EUR | 4% | 43% |
| momentum 30d | alto | 114 | -2.46 EUR | 4% | 46% |
| fuerza relativa | bajo | 113 | -2.71 EUR | 5% | 52% |
| fuerza relativa | medio | 113 | -1.99 EUR | 5% | 42% |
| fuerza relativa | alto | 114 | -2.25 EUR | 5% | 45% |
| RSI | bajo | 113 | -2.35 EUR | 6% | 49% |
| RSI | medio | 113 | -2.33 EUR | 7% | 48% |
| RSI | alto | 114 | -2.28 EUR | 3% | 42% |
| volumen relativo | bajo | 107 | -1.78 EUR | 9% | 45% |
| volumen relativo | medio | 107 | -2.43 EUR | 3% | 44% |
| volumen relativo | alto | 109 | -2.61 EUR | 4% | 45% |
| volatilidad | bajo | 107 | -2.02 EUR | 7% | 41% |
| volatilidad | medio | 107 | -2.47 EUR | 6% | 47% |
| volatilidad | alto | 109 | -2.35 EUR | 4% | 46% |
| liquidez | bajo | 107 | -2.68 EUR | 5% | 49% |
| liquidez | medio | 107 | -2.14 EUR | 6% | 44% |
| liquidez | alto | 109 | -2.02 EUR | 6% | 41% |
| distancia max 52s | bajo | 107 | -1.75 EUR | 6% | 40% |
| distancia max 52s | medio | 107 | -1.93 EUR | 7% | 44% |
| distancia max 52s | alto | 109 | -3.14 EUR | 4% | 50% |
| consenso | buy | 239 | -2.33 EUR | 5% | 45% |
| consenso | strong_buy | 101 | -2.29 EUR | 6% | 50% |
| tendencia tecnica | alcista | 156 | -2.71 EUR | 4% | 49% |
| tendencia tecnica | mixta | 99 | -2.37 EUR | 5% | 47% |
| tendencia tecnica | bajista | 85 | -1.53 EUR | 7% | 40% |
| tendencia analistas | mejorando | 155 | -2.26 EUR | 4% | 45% |
| tendencia analistas | estable | 113 | -2.70 EUR | 8% | 52% |
| tendencia analistas | empeorando | 14 | -2.72 EUR | 7% | 57% |
| regimen de mercado | neutro | 169 | -1.96 EUR | 7% | 43% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 56 | -1.26 EUR | 4% | 29% |
| catalizador | con catalizador | 12 | -0.60 EUR | 8% | 25% |
| catalizador | sin catalizador | 328 | -2.38 EUR | 5% | 47% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.70 | -1.72 | **+0.97 EUR** |
| liquidez | -2.68 | -2.02 | **+0.66 EUR** |
| % compra fuerte | -2.88 | -2.40 | **+0.48 EUR** |
| fuerza relativa | -2.71 | -2.25 | **+0.46 EUR** |
| RSI | -2.35 | -2.28 | **+0.07 EUR** |
| momentum 30d | -2.42 | -2.46 | **-0.04 EUR** |
| dispersion | -2.20 | -2.25 | **-0.05 EUR** |
| puesto en el ranking | -2.07 | -2.28 | **-0.21 EUR** |
| volatilidad | -2.02 | -2.35 | **-0.32 EUR** |
| nota global | -1.56 | -1.99 | **-0.43 EUR** |
| volumen relativo | -1.78 | -2.61 | **-0.83 EUR** |
| distancia max 52s | -1.75 | -3.14 | **-1.40 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
