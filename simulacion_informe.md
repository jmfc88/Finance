# Simulacion en paralelo

Actualizado: 2026-11-11 01:16 · dia 80 de ejecucion
Proxima revision de ponderacion en 10 dias.

- Operaciones cerradas: **321**
- Operaciones abiertas: 62

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 14 | 4% | +8.78 EUR |
| flojo | 131 | 41% | +1.32 EUR |
| plano | 18 | 6% | -1.74 EUR |
| perdida | 88 | 27% | -7.19 EUR |
| nefasta | 66 | 21% | -7.25 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 62 | -1.78% | 5/62 (8%) | 13/62 | 10 |
| 11-20 | 79 | -2.53% | 6/79 (8%) | 11/79 | 9 |
| 21-30 | 180 | -2.61% | 7/180 (4%) | 27/180 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 18 | -0.20% | -0.33% | **+0.13%** | 10/18 (56%) |
| 11-20 | 30 | -0.85% | -0.62% | **-0.23%** | 19/30 (63%) |
| 21-30 | 90 | -0.66% | -0.26% | **-0.41%** | 50/90 (56%) |

**En conjunto:** -0.64% de media frente a -0.34% del indice, una diferencia de **-0.30%**. 79 de 138 operaciones (57%) batieron a su indice.

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
| escalera + stop vol x4 | -0.78% | 132 | -102.99 EUR | 13/132 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.43% | 148 | -212.02 EUR | 11/148 | -10.63 EUR |
| escalera + stop vol x3 | -1.54% | 144 | -222.15 EUR | 11/144 | -12.76 EUR |
| trailing pegado (3%) | -1.57% | 127 | -199.57 EUR | 16/127 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.43% | 321 | -779.96 EUR | 18/321 | -8.08 EUR |
| arranca antes (+3%) | -2.89% | 108 | -312.13 EUR | 12/108 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.00% | 100 | -300.40 EUR | 12/100 | -10.00 EUR |
| arranca despues (+8%) | -3.19% | 91 | -290.27 EUR | 12/91 | -10.00 EUR |
| trailing suelto (7%) | -3.66% | 90 | -329.02 EUR | 11/90 | -10.00 EUR |
| sin trailing, solo stop | -4.09% | 84 | -343.32 EUR | 9/84 | -10.00 EUR |
| stop corto (5%) | -4.74% | 203 | -962.15 EUR | 12/203 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.43%**
- Aciertos (>= 5 EUR limpios): 18/321 (6%)
- Resultado acumulado ficticio: -779.96 EUR sobre 321 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 107 | -1.79 EUR | 5% | 37% |
| nota global | medio | 107 | -3.26 EUR | 4% | 54% |
| nota global | alto | 107 | -2.25 EUR | 8% | 52% |
| puesto en el ranking | bajo | 107 | -2.19 EUR | 7% | 50% |
| puesto en el ranking | medio | 107 | -2.74 EUR | 6% | 50% |
| puesto en el ranking | alto | 107 | -2.37 EUR | 4% | 44% |
| potencial hasta objetivo | bajo | 107 | -2.82 EUR | 5% | 49% |
| potencial hasta objetivo | medio | 107 | -2.58 EUR | 5% | 50% |
| potencial hasta objetivo | alto | 107 | -1.89 EUR | 7% | 46% |
| dispersion | bajo | 107 | -2.29 EUR | 7% | 50% |
| dispersion | medio | 107 | -2.62 EUR | 5% | 48% |
| dispersion | alto | 107 | -2.38 EUR | 5% | 46% |
| % compra fuerte | bajo | 100 | -2.84 EUR | 3% | 48% |
| % compra fuerte | medio | 100 | -2.08 EUR | 9% | 50% |
| % compra fuerte | alto | 101 | -2.46 EUR | 4% | 45% |
| momentum 30d | bajo | 107 | -2.60 EUR | 6% | 50% |
| momentum 30d | medio | 107 | -2.03 EUR | 7% | 45% |
| momentum 30d | alto | 107 | -2.66 EUR | 5% | 50% |
| fuerza relativa | bajo | 107 | -2.80 EUR | 5% | 52% |
| fuerza relativa | medio | 107 | -2.19 EUR | 7% | 46% |
| fuerza relativa | alto | 107 | -2.30 EUR | 6% | 46% |
| RSI | bajo | 107 | -2.47 EUR | 7% | 50% |
| RSI | medio | 107 | -2.19 EUR | 7% | 48% |
| RSI | alto | 107 | -2.62 EUR | 4% | 47% |
| volumen relativo | bajo | 101 | -1.77 EUR | 10% | 46% |
| volumen relativo | medio | 101 | -2.46 EUR | 3% | 45% |
| volumen relativo | alto | 102 | -2.95 EUR | 4% | 49% |
| volatilidad | bajo | 101 | -2.02 EUR | 7% | 42% |
| volatilidad | medio | 101 | -2.61 EUR | 6% | 49% |
| volatilidad | alto | 102 | -2.55 EUR | 4% | 49% |
| liquidez | bajo | 101 | -2.95 EUR | 4% | 50% |
| liquidez | medio | 101 | -2.10 EUR | 7% | 46% |
| liquidez | alto | 102 | -2.14 EUR | 6% | 43% |
| distancia max 52s | bajo | 101 | -1.82 EUR | 6% | 42% |
| distancia max 52s | medio | 101 | -2.04 EUR | 7% | 46% |
| distancia max 52s | alto | 102 | -3.31 EUR | 4% | 52% |
| consenso | buy | 227 | -2.46 EUR | 5% | 47% |
| consenso | strong_buy | 94 | -2.34 EUR | 6% | 51% |
| tendencia tecnica | alcista | 149 | -2.77 EUR | 5% | 50% |
| tendencia tecnica | mixta | 91 | -2.56 EUR | 5% | 51% |
| tendencia tecnica | bajista | 81 | -1.66 EUR | 7% | 42% |
| tendencia analistas | mejorando | 147 | -2.37 EUR | 4% | 46% |
| tendencia analistas | estable | 110 | -2.72 EUR | 8% | 53% |
| tendencia analistas | empeorando | 13 | -3.00 EUR | 8% | 62% |
| regimen de mercado | neutro | 164 | -1.94 EUR | 7% | 43% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 42 | -1.80 EUR | 5% | 36% |
| catalizador | con catalizador | 9 | -1.13 EUR | 11% | 33% |
| catalizador | sin catalizador | 312 | -2.47 EUR | 5% | 48% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.82 | -1.89 | **+0.93 EUR** |
| liquidez | -2.95 | -2.14 | **+0.81 EUR** |
| fuerza relativa | -2.80 | -2.30 | **+0.51 EUR** |
| % compra fuerte | -2.84 | -2.46 | **+0.38 EUR** |
| momentum 30d | -2.60 | -2.66 | **-0.05 EUR** |
| dispersion | -2.29 | -2.38 | **-0.08 EUR** |
| RSI | -2.47 | -2.62 | **-0.15 EUR** |
| puesto en el ranking | -2.19 | -2.37 | **-0.18 EUR** |
| nota global | -1.79 | -2.25 | **-0.46 EUR** |
| volatilidad | -2.02 | -2.55 | **-0.53 EUR** |
| volumen relativo | -1.77 | -2.95 | **-1.18 EUR** |
| distancia max 52s | -1.82 | -3.31 | **-1.49 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
