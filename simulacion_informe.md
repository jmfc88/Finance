# Simulacion en paralelo

Actualizado: 2026-10-22 14:32 · dia 60 de ejecucion
**Revision nº4 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **213**
- Operaciones abiertas: 53

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 1% | +16.90 EUR |
| beneficio | 3 | 1% | +7.07 EUR |
| flojo | 74 | 35% | +1.30 EUR |
| plano | 13 | 6% | -1.84 EUR |
| perdida | 74 | 35% | -7.16 EUR |
| nefasta | 46 | 22% | -6.90 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 48 | -2.01% | 3/48 (6%) | 9/48 | 10 |
| 11-20 | 56 | -3.27% | 2/56 (4%) | 4/56 | 9 |
| 21-30 | 109 | -3.88% | 1/109 (1%) | 8/109 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 5 | +0.46% | -2.00% | **+2.46%** | 2/5 (40%) |
| 11-20 | 10 | -3.29% | -0.82% | **-2.47%** | 5/10 (50%) |
| 21-30 | 24 | -2.23% | -0.82% | **-1.40%** | 14/24 (58%) |

**En conjunto:** -2.15% de media frente a -0.97% del indice, una diferencia de **-1.18%**. 21 de 39 operaciones (54%) batieron a su indice.

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
| escalera + stop vol x4 | -1.52% | 32 | -48.57 EUR | 1/32 | -8.20 EUR |
| escalera + stop vol x2.5 | -2.32% | 40 | -92.88 EUR | 1/40 | -7.93 EUR |
| trailing pegado (3%) | -2.39% | 67 | -160.41 EUR | 4/67 | -10.00 EUR |
| escalera + stop vol x3 | -2.70% | 39 | -105.35 EUR | 1/39 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.30% | 213 | -702.51 EUR | 6/213 | -8.08 EUR |
| arranca antes (+3%) | -3.64% | 58 | -211.33 EUR | 4/58 | -10.00 EUR |
| arranca despues (+8%) | -3.74% | 52 | -194.45 EUR | 4/52 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.74% | 52 | -194.45 EUR | 4/52 | -10.00 EUR |
| trailing suelto (7%) | -4.35% | 50 | -217.59 EUR | 3/50 | -10.00 EUR |
| sin trailing, solo stop | -4.69% | 49 | -229.65 EUR | 2/49 | -10.00 EUR |
| stop corto (5%) | -5.59% | 138 | -771.92 EUR | 4/138 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.30%**
- Aciertos (>= 5 EUR limpios): 6/213 (3%)
- Resultado acumulado ficticio: -702.51 EUR sobre 213 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 71 | -3.43 EUR | 0% | 49% |
| nota global | medio | 71 | -3.88 EUR | 3% | 63% |
| nota global | alto | 71 | -2.59 EUR | 6% | 56% |
| puesto en el ranking | bajo | 71 | -2.35 EUR | 7% | 55% |
| puesto en el ranking | medio | 71 | -3.73 EUR | 1% | 58% |
| puesto en el ranking | alto | 71 | -3.82 EUR | 0% | 56% |
| potencial hasta objetivo | bajo | 71 | -3.50 EUR | 3% | 55% |
| potencial hasta objetivo | medio | 71 | -3.76 EUR | 1% | 61% |
| potencial hasta objetivo | alto | 71 | -2.63 EUR | 4% | 54% |
| dispersion | bajo | 71 | -2.71 EUR | 6% | 55% |
| dispersion | medio | 71 | -4.15 EUR | 1% | 63% |
| dispersion | alto | 71 | -3.03 EUR | 1% | 51% |
| % compra fuerte | bajo | 66 | -3.95 EUR | 2% | 59% |
| % compra fuerte | medio | 66 | -3.04 EUR | 2% | 58% |
| % compra fuerte | alto | 68 | -3.31 EUR | 3% | 53% |
| momentum 30d | bajo | 71 | -3.03 EUR | 4% | 54% |
| momentum 30d | medio | 71 | -3.15 EUR | 1% | 55% |
| momentum 30d | alto | 71 | -3.72 EUR | 3% | 61% |
| fuerza relativa | bajo | 71 | -3.16 EUR | 4% | 58% |
| fuerza relativa | medio | 71 | -3.43 EUR | 0% | 54% |
| fuerza relativa | alto | 71 | -3.30 EUR | 4% | 58% |
| RSI | bajo | 71 | -2.62 EUR | 6% | 51% |
| RSI | medio | 71 | -3.48 EUR | 1% | 58% |
| RSI | alto | 71 | -3.80 EUR | 1% | 61% |
| volumen relativo | bajo | 65 | -3.27 EUR | 5% | 62% |
| volumen relativo | medio | 65 | -3.02 EUR | 0% | 46% |
| volumen relativo | alto | 66 | -3.66 EUR | 3% | 56% |
| volatilidad | bajo | 65 | -3.69 EUR | 0% | 55% |
| volatilidad | medio | 65 | -3.79 EUR | 2% | 55% |
| volatilidad | alto | 66 | -2.49 EUR | 6% | 53% |
| liquidez | bajo | 65 | -3.51 EUR | 2% | 55% |
| liquidez | medio | 65 | -2.74 EUR | 5% | 54% |
| liquidez | alto | 66 | -3.69 EUR | 2% | 55% |
| distancia max 52s | bajo | 65 | -2.32 EUR | 6% | 49% |
| distancia max 52s | medio | 65 | -3.53 EUR | 0% | 57% |
| distancia max 52s | alto | 66 | -4.09 EUR | 2% | 58% |
| consenso | buy | 151 | -3.55 EUR | 2% | 56% |
| consenso | strong_buy | 62 | -2.67 EUR | 5% | 56% |
| tendencia tecnica | alcista | 107 | -3.55 EUR | 3% | 58% |
| tendencia tecnica | mixta | 57 | -3.02 EUR | 2% | 53% |
| tendencia tecnica | bajista | 49 | -3.07 EUR | 4% | 57% |
| tendencia analistas | mejorando | 105 | -3.33 EUR | 3% | 56% |
| tendencia analistas | estable | 65 | -3.75 EUR | 3% | 63% |
| tendencia analistas | empeorando | 9 | -4.67 EUR | 0% | 78% |
| regimen de mercado | neutro | 107 | -3.04 EUR | 2% | 50% |
| regimen de mercado | favorable | 106 | -3.56 EUR | 4% | 62% |
| catalizador | sin catalizador | 212 | -3.28 EUR | 3% | 56% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -3.69 | -2.49 | **+1.20 EUR** |
| potencial hasta objetivo | -3.50 | -2.63 | **+0.87 EUR** |
| nota global | -3.43 | -2.59 | **+0.84 EUR** |
| % compra fuerte | -3.95 | -3.31 | **+0.64 EUR** |
| fuerza relativa | -3.16 | -3.30 | **-0.15 EUR** |
| liquidez | -3.51 | -3.69 | **-0.18 EUR** |
| dispersion | -2.71 | -3.03 | **-0.32 EUR** |
| volumen relativo | -3.27 | -3.66 | **-0.38 EUR** |
| momentum 30d | -3.03 | -3.72 | **-0.69 EUR** |
| RSI | -2.62 | -3.80 | **-1.17 EUR** |
| puesto en el ranking | -2.35 | -3.82 | **-1.46 EUR** |
| distancia max 52s | -2.32 | -4.09 | **-1.77 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
