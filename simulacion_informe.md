# Simulacion en paralelo

Actualizado: 2026-11-05 23:39 · dia 74 de ejecucion
Proxima revision de ponderacion en 1 dia.

- Operaciones cerradas: **288**
- Operaciones abiertas: 62

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 11 | 4% | +8.70 EUR |
| flojo | 106 | 37% | +1.30 EUR |
| plano | 18 | 6% | -1.74 EUR |
| perdida | 87 | 30% | -7.18 EUR |
| nefasta | 62 | 22% | -7.20 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 58 | -1.97% | 5/58 (9%) | 12/58 | 10 |
| 11-20 | 73 | -2.57% | 6/73 (8%) | 11/73 | 9 |
| 21-30 | 157 | -3.19% | 4/157 (3%) | 18/157 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 14 | -0.54% | -0.48% | **-0.06%** | 6/14 (43%) |
| 11-20 | 26 | -1.13% | -0.76% | **-0.37%** | 15/26 (58%) |
| 21-30 | 68 | -1.44% | -0.41% | **-1.03%** | 34/68 (50%) |

**En conjunto:** -1.25% de media frente a -0.50% del indice, una diferencia de **-0.75%**. 55 de 108 operaciones (51%) batieron a su indice.

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
| escalera + stop vol x4 | -1.17% | 100 | -117.35 EUR | 10/100 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.80% | 115 | -206.50 EUR | 8/115 | -10.63 EUR |
| trailing pegado (3%) | -1.83% | 112 | -204.56 EUR | 13/112 | -10.00 EUR |
| escalera + stop vol x3 | -1.99% | 112 | -222.50 EUR | 8/112 | -12.76 EUR |
| arranca antes (+3%) | -2.77% | 101 | -279.29 EUR | 12/101 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.78% | 288 | -801.96 EUR | 15/288 | -8.08 EUR |
| actual (8% / +5% / 5%) | -2.89% | 94 | -271.27 EUR | 12/94 | -10.00 EUR |
| arranca despues (+8%) | -3.04% | 87 | -264.50 EUR | 12/87 | -10.00 EUR |
| trailing suelto (7%) | -3.44% | 87 | -299.02 EUR | 11/87 | -10.00 EUR |
| sin trailing, solo stop | -3.87% | 81 | -313.32 EUR | 9/81 | -10.00 EUR |
| stop corto (5%) | -4.75% | 194 | -921.02 EUR | 12/194 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.78%**
- Aciertos (>= 5 EUR limpios): 15/288 (5%)
- Resultado acumulado ficticio: -801.96 EUR sobre 288 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 96 | -2.50 EUR | 3% | 44% |
| nota global | medio | 96 | -3.65 EUR | 3% | 58% |
| nota global | alto | 96 | -2.21 EUR | 9% | 53% |
| puesto en el ranking | bajo | 96 | -2.22 EUR | 8% | 53% |
| puesto en el ranking | medio | 96 | -3.48 EUR | 4% | 56% |
| puesto en el ranking | alto | 96 | -2.65 EUR | 3% | 46% |
| potencial hasta objetivo | bajo | 96 | -3.23 EUR | 4% | 53% |
| potencial hasta objetivo | medio | 96 | -3.14 EUR | 4% | 55% |
| potencial hasta objetivo | alto | 96 | -1.98 EUR | 7% | 47% |
| dispersion | bajo | 96 | -2.36 EUR | 8% | 53% |
| dispersion | medio | 96 | -3.11 EUR | 5% | 53% |
| dispersion | alto | 96 | -2.88 EUR | 2% | 49% |
| % compra fuerte | bajo | 89 | -3.24 EUR | 3% | 53% |
| % compra fuerte | medio | 89 | -2.43 EUR | 7% | 53% |
| % compra fuerte | alto | 91 | -2.79 EUR | 4% | 48% |
| momentum 30d | bajo | 96 | -2.88 EUR | 6% | 53% |
| momentum 30d | medio | 96 | -2.50 EUR | 4% | 47% |
| momentum 30d | alto | 96 | -2.97 EUR | 5% | 55% |
| fuerza relativa | bajo | 96 | -3.18 EUR | 4% | 55% |
| fuerza relativa | medio | 96 | -2.39 EUR | 6% | 48% |
| fuerza relativa | alto | 96 | -2.79 EUR | 5% | 52% |
| RSI | bajo | 96 | -2.39 EUR | 7% | 49% |
| RSI | medio | 96 | -2.59 EUR | 5% | 51% |
| RSI | alto | 96 | -3.37 EUR | 3% | 55% |
| volumen relativo | bajo | 90 | -2.11 EUR | 9% | 49% |
| volumen relativo | medio | 90 | -2.86 EUR | 3% | 49% |
| volumen relativo | alto | 91 | -3.32 EUR | 3% | 53% |
| volatilidad | bajo | 90 | -2.63 EUR | 6% | 47% |
| volatilidad | medio | 90 | -2.91 EUR | 6% | 52% |
| volatilidad | alto | 91 | -2.76 EUR | 4% | 52% |
| liquidez | bajo | 90 | -3.24 EUR | 3% | 53% |
| liquidez | medio | 90 | -2.40 EUR | 7% | 49% |
| liquidez | alto | 91 | -2.66 EUR | 5% | 48% |
| distancia max 52s | bajo | 90 | -2.08 EUR | 4% | 42% |
| distancia max 52s | medio | 90 | -2.56 EUR | 6% | 52% |
| distancia max 52s | alto | 91 | -3.65 EUR | 5% | 56% |
| consenso | buy | 201 | -2.83 EUR | 4% | 50% |
| consenso | strong_buy | 87 | -2.67 EUR | 7% | 55% |
| tendencia tecnica | alcista | 132 | -3.20 EUR | 5% | 55% |
| tendencia tecnica | mixta | 81 | -2.80 EUR | 5% | 53% |
| tendencia tecnica | bajista | 75 | -2.05 EUR | 7% | 45% |
| tendencia analistas | mejorando | 137 | -2.59 EUR | 4% | 49% |
| tendencia analistas | estable | 93 | -3.32 EUR | 6% | 58% |
| tendencia analistas | empeorando | 12 | -3.34 EUR | 8% | 67% |
| regimen de mercado | neutro | 155 | -2.15 EUR | 7% | 45% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 18 | -4.55 EUR | 0% | 61% |
| catalizador | sin catalizador | 285 | -2.76 EUR | 5% | 52% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.23 | -1.98 | **+1.25 EUR** |
| liquidez | -3.24 | -2.66 | **+0.58 EUR** |
| % compra fuerte | -3.24 | -2.79 | **+0.45 EUR** |
| fuerza relativa | -3.18 | -2.79 | **+0.39 EUR** |
| nota global | -2.50 | -2.21 | **+0.29 EUR** |
| momentum 30d | -2.88 | -2.97 | **-0.09 EUR** |
| volatilidad | -2.63 | -2.76 | **-0.14 EUR** |
| puesto en el ranking | -2.22 | -2.65 | **-0.44 EUR** |
| dispersion | -2.36 | -2.88 | **-0.52 EUR** |
| RSI | -2.39 | -3.37 | **-0.98 EUR** |
| volumen relativo | -2.11 | -3.32 | **-1.21 EUR** |
| distancia max 52s | -2.08 | -3.65 | **-1.57 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
