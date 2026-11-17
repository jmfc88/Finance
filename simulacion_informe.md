# Simulacion en paralelo

Actualizado: 2026-11-17 09:10 · dia 86 de ejecucion
Proxima revision de ponderacion en 4 dias.

- Operaciones cerradas: **352**
- Operaciones abiertas: 62

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 16 | 5% | +8.70 EUR |
| flojo | 155 | 44% | +1.28 EUR |
| plano | 18 | 5% | -1.74 EUR |
| perdida | 89 | 25% | -7.20 EUR |
| nefasta | 70 | 20% | -7.30 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 68 | -1.54% | 5/68 (7%) | 14/68 | 10 |
| 11-20 | 92 | -2.16% | 8/92 (9%) | 16/92 | 9 |
| 21-30 | 192 | -2.48% | 7/192 (4%) | 28/192 | 8 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 24 | +0.10% | +0.34% | **-0.24%** | 11/24 (46%) |
| 11-20 | 42 | -0.38% | +0.07% | **-0.44%** | 23/42 (55%) |
| 21-30 | 102 | -0.65% | -0.03% | **-0.62%** | 52/102 (51%) |

**En conjunto:** -0.47% de media frente a +0.05% del indice, una diferencia de **-0.52%**. 86 de 168 operaciones (51%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 55 operaciones, media -0.49%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.50% | 159 | -80.18 EUR | 14/159 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.16% | 175 | -202.58 EUR | 12/175 | -10.63 EUR |
| escalera + stop vol x3 | -1.22% | 171 | -209.01 EUR | 12/171 | -12.76 EUR |
| trailing pegado (3%) | -1.48% | 134 | -198.38 EUR | 18/134 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.21% | 352 | -778.73 EUR | 20/352 | -8.08 EUR |
| arranca antes (+3%) | -2.83% | 114 | -322.15 EUR | 14/114 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.87% | 105 | -301.77 EUR | 14/105 | -10.00 EUR |
| arranca despues (+8%) | -3.04% | 96 | -291.64 EUR | 14/96 | -10.00 EUR |
| trailing suelto (7%) | -3.48% | 95 | -330.39 EUR | 13/95 | -10.00 EUR |
| sin trailing, solo stop | -3.87% | 89 | -344.69 EUR | 11/89 | -10.00 EUR |
| stop corto (5%) | -4.70% | 211 | -992.38 EUR | 13/211 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.21%**
- Aciertos (>= 5 EUR limpios): 20/352 (6%)
- Resultado acumulado ficticio: -778.73 EUR sobre 352 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 117 | -1.55 EUR | 4% | 34% |
| nota global | medio | 117 | -3.00 EUR | 5% | 52% |
| nota global | alto | 118 | -2.09 EUR | 8% | 49% |
| puesto en el ranking | bajo | 117 | -2.03 EUR | 7% | 48% |
| puesto en el ranking | medio | 117 | -2.40 EUR | 7% | 46% |
| puesto en el ranking | alto | 118 | -2.21 EUR | 3% | 42% |
| potencial hasta objetivo | bajo | 117 | -2.50 EUR | 5% | 45% |
| potencial hasta objetivo | medio | 117 | -2.41 EUR | 3% | 46% |
| potencial hasta objetivo | alto | 118 | -1.74 EUR | 8% | 44% |
| dispersion | bajo | 117 | -2.20 EUR | 7% | 49% |
| dispersion | medio | 117 | -2.38 EUR | 5% | 44% |
| dispersion | alto | 118 | -2.06 EUR | 5% | 42% |
| % compra fuerte | bajo | 110 | -2.75 EUR | 4% | 47% |
| % compra fuerte | medio | 110 | -1.60 EUR | 8% | 44% |
| % compra fuerte | alto | 112 | -2.33 EUR | 4% | 43% |
| momentum 30d | bajo | 117 | -2.23 EUR | 8% | 47% |
| momentum 30d | medio | 117 | -2.15 EUR | 5% | 44% |
| momentum 30d | alto | 118 | -2.25 EUR | 4% | 44% |
| fuerza relativa | bajo | 117 | -2.48 EUR | 7% | 51% |
| fuerza relativa | medio | 117 | -2.07 EUR | 5% | 42% |
| fuerza relativa | alto | 118 | -2.09 EUR | 5% | 42% |
| RSI | bajo | 117 | -2.34 EUR | 7% | 49% |
| RSI | medio | 117 | -2.22 EUR | 8% | 47% |
| RSI | alto | 118 | -2.08 EUR | 3% | 40% |
| volumen relativo | bajo | 111 | -1.69 EUR | 10% | 44% |
| volumen relativo | medio | 111 | -2.26 EUR | 4% | 42% |
| volumen relativo | alto | 113 | -2.56 EUR | 4% | 44% |
| volatilidad | bajo | 111 | -1.92 EUR | 7% | 41% |
| volatilidad | medio | 111 | -2.22 EUR | 6% | 44% |
| volatilidad | alto | 113 | -2.37 EUR | 4% | 46% |
| liquidez | bajo | 111 | -2.40 EUR | 5% | 47% |
| liquidez | medio | 111 | -2.25 EUR | 5% | 44% |
| liquidez | alto | 113 | -1.86 EUR | 6% | 40% |
| distancia max 52s | bajo | 111 | -1.68 EUR | 6% | 40% |
| distancia max 52s | medio | 111 | -1.92 EUR | 6% | 43% |
| distancia max 52s | alto | 113 | -2.90 EUR | 4% | 48% |
| consenso | buy | 246 | -2.17 EUR | 6% | 43% |
| consenso | strong_buy | 106 | -2.31 EUR | 6% | 49% |
| tendencia tecnica | alcista | 166 | -2.54 EUR | 5% | 47% |
| tendencia tecnica | mixta | 100 | -2.33 EUR | 5% | 47% |
| tendencia tecnica | bajista | 86 | -1.44 EUR | 8% | 40% |
| tendencia analistas | mejorando | 160 | -2.11 EUR | 5% | 44% |
| tendencia analistas | estable | 118 | -2.62 EUR | 8% | 51% |
| tendencia analistas | empeorando | 14 | -2.72 EUR | 7% | 57% |
| regimen de mercado | neutro | 174 | -1.94 EUR | 7% | 43% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 63 | -0.87 EUR | 5% | 25% |
| catalizador | con catalizador | 12 | -0.60 EUR | 8% | 25% |
| catalizador | sin catalizador | 340 | -2.27 EUR | 6% | 46% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.50 | -1.74 | **+0.76 EUR** |
| liquidez | -2.40 | -1.86 | **+0.54 EUR** |
| % compra fuerte | -2.75 | -2.33 | **+0.41 EUR** |
| fuerza relativa | -2.48 | -2.09 | **+0.39 EUR** |
| RSI | -2.34 | -2.08 | **+0.26 EUR** |
| dispersion | -2.20 | -2.06 | **+0.15 EUR** |
| momentum 30d | -2.23 | -2.25 | **-0.02 EUR** |
| puesto en el ranking | -2.03 | -2.21 | **-0.17 EUR** |
| volatilidad | -1.92 | -2.37 | **-0.45 EUR** |
| nota global | -1.55 | -2.09 | **-0.54 EUR** |
| volumen relativo | -1.69 | -2.56 | **-0.87 EUR** |
| distancia max 52s | -1.68 | -2.90 | **-1.22 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
