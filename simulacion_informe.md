# Simulacion en paralelo

Actualizado: 2026-11-05 14:33 · dia 74 de ejecucion
Proxima revision de ponderacion en 1 dia.

- Operaciones cerradas: **279**
- Operaciones abiertas: 61

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 10 | 4% | +8.40 EUR |
| flojo | 99 | 35% | +1.30 EUR |
| plano | 18 | 6% | -1.74 EUR |
| perdida | 86 | 31% | -7.17 EUR |
| nefasta | 62 | 22% | -7.20 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 56 | -1.92% | 5/56 (9%) | 11/56 | 10 |
| 11-20 | 71 | -2.82% | 5/71 (7%) | 9/71 | 10 |
| 21-30 | 152 | -3.34% | 4/152 (3%) | 15/152 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 12 | -0.04% | -0.68% | **+0.64%** | 5/12 (42%) |
| 11-20 | 24 | -1.75% | -0.64% | **-1.11%** | 13/24 (54%) |
| 21-30 | 63 | -1.68% | -0.33% | **-1.35%** | 30/63 (48%) |

**En conjunto:** -1.50% de media frente a -0.44% del indice, una diferencia de **-1.05%**. 48 de 99 operaciones (48%) batieron a su indice.

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
| escalera + stop vol x4 | -1.44% | 92 | -132.40 EUR | 9/92 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.97% | 106 | -208.37 EUR | 7/106 | -10.63 EUR |
| trailing pegado (3%) | -2.08% | 107 | -222.77 EUR | 12/107 | -10.00 EUR |
| escalera + stop vol x3 | -2.22% | 104 | -230.78 EUR | 7/104 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.92% | 279 | -815.02 EUR | 14/279 | -8.08 EUR |
| arranca antes (+3%) | -2.98% | 95 | -282.83 EUR | 11/95 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.13% | 89 | -278.58 EUR | 11/89 | -10.00 EUR |
| arranca despues (+8%) | -3.21% | 86 | -276.17 EUR | 11/86 | -10.00 EUR |
| trailing suelto (7%) | -3.61% | 85 | -306.70 EUR | 10/85 | -10.00 EUR |
| sin trailing, solo stop | -3.87% | 81 | -313.32 EUR | 9/81 | -10.00 EUR |
| stop corto (5%) | -4.89% | 187 | -914.33 EUR | 11/187 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.92%**
- Aciertos (>= 5 EUR limpios): 14/279 (5%)
- Resultado acumulado ficticio: -815.02 EUR sobre 279 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 93 | -2.68 EUR | 3% | 45% |
| nota global | medio | 93 | -3.87 EUR | 2% | 60% |
| nota global | alto | 93 | -2.21 EUR | 10% | 54% |
| puesto en el ranking | bajo | 93 | -2.22 EUR | 9% | 54% |
| puesto en el ranking | medio | 93 | -3.64 EUR | 3% | 57% |
| puesto en el ranking | alto | 93 | -2.90 EUR | 3% | 48% |
| potencial hasta objetivo | bajo | 93 | -3.39 EUR | 4% | 55% |
| potencial hasta objetivo | medio | 93 | -3.28 EUR | 4% | 57% |
| potencial hasta objetivo | alto | 93 | -2.10 EUR | 6% | 47% |
| dispersion | bajo | 93 | -2.52 EUR | 8% | 55% |
| dispersion | medio | 93 | -3.21 EUR | 5% | 54% |
| dispersion | alto | 93 | -3.03 EUR | 2% | 51% |
| % compra fuerte | bajo | 86 | -3.29 EUR | 3% | 53% |
| % compra fuerte | medio | 86 | -2.67 EUR | 6% | 55% |
| % compra fuerte | alto | 88 | -2.95 EUR | 5% | 50% |
| momentum 30d | bajo | 93 | -3.03 EUR | 6% | 55% |
| momentum 30d | medio | 93 | -2.42 EUR | 4% | 46% |
| momentum 30d | alto | 93 | -3.31 EUR | 4% | 58% |
| fuerza relativa | bajo | 93 | -3.42 EUR | 3% | 57% |
| fuerza relativa | medio | 93 | -2.19 EUR | 8% | 46% |
| fuerza relativa | alto | 93 | -3.15 EUR | 4% | 56% |
| RSI | bajo | 93 | -2.40 EUR | 8% | 49% |
| RSI | medio | 93 | -2.79 EUR | 4% | 53% |
| RSI | alto | 93 | -3.57 EUR | 3% | 57% |
| volumen relativo | bajo | 87 | -2.34 EUR | 8% | 51% |
| volumen relativo | medio | 87 | -2.89 EUR | 3% | 49% |
| volumen relativo | alto | 88 | -3.49 EUR | 3% | 55% |
| volatilidad | bajo | 87 | -2.62 EUR | 6% | 47% |
| volatilidad | medio | 87 | -3.09 EUR | 5% | 53% |
| volatilidad | alto | 88 | -3.02 EUR | 5% | 55% |
| liquidez | bajo | 87 | -3.29 EUR | 3% | 54% |
| liquidez | medio | 87 | -2.29 EUR | 7% | 48% |
| liquidez | alto | 88 | -3.15 EUR | 5% | 52% |
| distancia max 52s | bajo | 87 | -2.37 EUR | 5% | 46% |
| distancia max 52s | medio | 87 | -2.51 EUR | 6% | 51% |
| distancia max 52s | alto | 88 | -3.85 EUR | 5% | 58% |
| consenso | buy | 193 | -3.06 EUR | 4% | 52% |
| consenso | strong_buy | 86 | -2.61 EUR | 7% | 55% |
| tendencia tecnica | alcista | 130 | -3.28 EUR | 5% | 55% |
| tendencia tecnica | mixta | 76 | -3.07 EUR | 4% | 55% |
| tendencia tecnica | bajista | 73 | -2.13 EUR | 7% | 47% |
| tendencia analistas | mejorando | 132 | -2.80 EUR | 4% | 51% |
| tendencia analistas | estable | 91 | -3.31 EUR | 7% | 58% |
| tendencia analistas | empeorando | 12 | -3.34 EUR | 8% | 67% |
| regimen de mercado | neutro | 147 | -2.35 EUR | 7% | 47% |
| regimen de mercado | favorable | 114 | -3.40 EUR | 4% | 60% |
| regimen de mercado | adverso | 18 | -4.55 EUR | 0% | 61% |
| catalizador | sin catalizador | 277 | -2.88 EUR | 5% | 53% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.39 | -2.10 | **+1.30 EUR** |
| nota global | -2.68 | -2.21 | **+0.47 EUR** |
| % compra fuerte | -3.29 | -2.95 | **+0.33 EUR** |
| fuerza relativa | -3.42 | -3.15 | **+0.27 EUR** |
| liquidez | -3.29 | -3.15 | **+0.13 EUR** |
| momentum 30d | -3.03 | -3.31 | **-0.27 EUR** |
| volatilidad | -2.62 | -3.02 | **-0.41 EUR** |
| dispersion | -2.52 | -3.03 | **-0.51 EUR** |
| puesto en el ranking | -2.22 | -2.90 | **-0.67 EUR** |
| volumen relativo | -2.34 | -3.49 | **-1.15 EUR** |
| RSI | -2.40 | -3.57 | **-1.17 EUR** |
| distancia max 52s | -2.37 | -3.85 | **-1.48 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
