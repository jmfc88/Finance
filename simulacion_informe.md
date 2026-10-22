# Simulacion en paralelo

Actualizado: 2026-10-22 17:59 · dia 60 de ejecucion
**Revision nº4 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **216**
- Operaciones abiertas: 57

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 1% | +16.90 EUR |
| beneficio | 3 | 1% | +7.07 EUR |
| flojo | 74 | 34% | +1.30 EUR |
| plano | 13 | 6% | -1.84 EUR |
| perdida | 76 | 35% | -7.18 EUR |
| nefasta | 47 | 22% | -6.92 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 49 | -2.13% | 3/49 (6%) | 9/49 | 10 |
| 11-20 | 56 | -3.27% | 2/56 (4%) | 4/56 | 9 |
| 21-30 | 111 | -3.96% | 1/111 (1%) | 8/111 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 6 | -0.96% | -1.91% | **+0.95%** | 2/6 (33%) |
| 11-20 | 10 | -3.29% | -0.82% | **-2.47%** | 5/10 (50%) |
| 21-30 | 26 | -2.68% | -0.93% | **-1.75%** | 14/26 (54%) |

**En conjunto:** -2.58% de media frente a -1.04% del indice, una diferencia de **-1.53%**. 21 de 42 operaciones (50%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 35 operaciones, media -2.64%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -2.00% | 35 | -69.90 EUR | 1/35 | -8.20 EUR |
| trailing pegado (3%) | -2.39% | 67 | -160.41 EUR | 4/67 | -10.00 EUR |
| escalera + stop vol x2.5 | -2.48% | 43 | -106.81 EUR | 1/43 | -7.93 EUR |
| escalera + stop vol x3 | -2.89% | 42 | -121.35 EUR | 1/42 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.36% | 216 | -726.75 EUR | 6/216 | -8.08 EUR |
| arranca antes (+3%) | -3.64% | 58 | -211.33 EUR | 4/58 | -10.00 EUR |
| arranca despues (+8%) | -3.74% | 52 | -194.45 EUR | 4/52 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.74% | 52 | -194.45 EUR | 4/52 | -10.00 EUR |
| trailing suelto (7%) | -4.35% | 50 | -217.59 EUR | 3/50 | -10.00 EUR |
| sin trailing, solo stop | -4.69% | 49 | -229.65 EUR | 2/49 | -10.00 EUR |
| stop corto (5%) | -5.62% | 141 | -792.92 EUR | 4/141 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.36%**
- Aciertos (>= 5 EUR limpios): 6/216 (3%)
- Resultado acumulado ficticio: -726.75 EUR sobre 216 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 72 | -3.49 EUR | 0% | 50% |
| nota global | medio | 72 | -3.94 EUR | 3% | 64% |
| nota global | alto | 72 | -2.66 EUR | 6% | 57% |
| puesto en el ranking | bajo | 72 | -2.43 EUR | 7% | 56% |
| puesto en el ranking | medio | 72 | -3.79 EUR | 1% | 58% |
| puesto en el ranking | alto | 72 | -3.87 EUR | 0% | 57% |
| potencial hasta objetivo | bajo | 72 | -3.56 EUR | 3% | 56% |
| potencial hasta objetivo | medio | 72 | -3.98 EUR | 1% | 62% |
| potencial hasta objetivo | alto | 72 | -2.55 EUR | 4% | 53% |
| dispersion | bajo | 72 | -2.73 EUR | 6% | 56% |
| dispersion | medio | 72 | -4.26 EUR | 1% | 64% |
| dispersion | alto | 72 | -3.10 EUR | 1% | 51% |
| % compra fuerte | bajo | 67 | -3.96 EUR | 1% | 60% |
| % compra fuerte | medio | 67 | -3.03 EUR | 1% | 57% |
| % compra fuerte | alto | 69 | -3.51 EUR | 3% | 55% |
| momentum 30d | bajo | 72 | -3.10 EUR | 4% | 54% |
| momentum 30d | medio | 72 | -3.56 EUR | 0% | 57% |
| momentum 30d | alto | 72 | -3.43 EUR | 4% | 60% |
| fuerza relativa | bajo | 72 | -3.23 EUR | 4% | 58% |
| fuerza relativa | medio | 72 | -3.62 EUR | 0% | 54% |
| fuerza relativa | alto | 72 | -3.24 EUR | 4% | 58% |
| RSI | bajo | 72 | -2.83 EUR | 6% | 53% |
| RSI | medio | 72 | -3.54 EUR | 1% | 57% |
| RSI | alto | 72 | -3.73 EUR | 1% | 61% |
| volumen relativo | bajo | 66 | -3.35 EUR | 5% | 62% |
| volumen relativo | medio | 66 | -3.10 EUR | 0% | 47% |
| volumen relativo | alto | 67 | -3.72 EUR | 3% | 57% |
| volatilidad | bajo | 66 | -3.67 EUR | 0% | 55% |
| volatilidad | medio | 66 | -3.94 EUR | 2% | 58% |
| volatilidad | alto | 67 | -2.57 EUR | 6% | 54% |
| liquidez | bajo | 66 | -3.58 EUR | 2% | 56% |
| liquidez | medio | 66 | -2.83 EUR | 5% | 55% |
| liquidez | alto | 67 | -3.76 EUR | 1% | 55% |
| distancia max 52s | bajo | 66 | -2.41 EUR | 6% | 50% |
| distancia max 52s | medio | 66 | -3.50 EUR | 0% | 56% |
| distancia max 52s | alto | 67 | -4.24 EUR | 1% | 60% |
| consenso | buy | 154 | -3.64 EUR | 2% | 57% |
| consenso | strong_buy | 62 | -2.67 EUR | 5% | 56% |
| tendencia tecnica | alcista | 107 | -3.55 EUR | 3% | 58% |
| tendencia tecnica | mixta | 60 | -3.27 EUR | 2% | 55% |
| tendencia tecnica | bajista | 49 | -3.07 EUR | 4% | 57% |
| tendencia analistas | mejorando | 107 | -3.42 EUR | 3% | 57% |
| tendencia analistas | estable | 66 | -3.82 EUR | 3% | 64% |
| tendencia analistas | empeorando | 9 | -4.67 EUR | 0% | 78% |
| regimen de mercado | neutro | 110 | -3.17 EUR | 2% | 52% |
| regimen de mercado | favorable | 106 | -3.56 EUR | 4% | 62% |
| catalizador | sin catalizador | 215 | -3.34 EUR | 3% | 57% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -3.67 | -2.57 | **+1.10 EUR** |
| potencial hasta objetivo | -3.56 | -2.55 | **+1.02 EUR** |
| nota global | -3.49 | -2.66 | **+0.83 EUR** |
| % compra fuerte | -3.96 | -3.51 | **+0.45 EUR** |
| fuerza relativa | -3.23 | -3.24 | **-0.02 EUR** |
| liquidez | -3.58 | -3.76 | **-0.18 EUR** |
| momentum 30d | -3.10 | -3.43 | **-0.33 EUR** |
| volumen relativo | -3.35 | -3.72 | **-0.37 EUR** |
| dispersion | -2.73 | -3.10 | **-0.38 EUR** |
| RSI | -2.83 | -3.73 | **-0.90 EUR** |
| puesto en el ranking | -2.43 | -3.87 | **-1.44 EUR** |
| distancia max 52s | -2.41 | -4.24 | **-1.84 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
