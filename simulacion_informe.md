# Simulacion en paralelo

Actualizado: 2026-10-30 12:46 · dia 68 de ejecucion
Proxima revision de ponderacion en 7 dias.

- Operaciones cerradas: **251**
- Operaciones abiertas: 62

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 2% | +16.71 EUR |
| beneficio | 5 | 2% | +7.59 EUR |
| flojo | 87 | 35% | +1.31 EUR |
| plano | 17 | 7% | -1.72 EUR |
| perdida | 83 | 33% | -7.22 EUR |
| nefasta | 55 | 22% | -7.09 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 52 | -2.24% | 3/52 (6%) | 9/52 | 10 |
| 11-20 | 63 | -3.09% | 3/63 (5%) | 7/63 | 9 |
| 21-30 | 136 | -3.59% | 3/136 (2%) | 12/136 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 9 | -1.96% | -1.58% | **-0.38%** | 3/9 (33%) |
| 11-20 | 17 | -2.64% | -1.08% | **-1.56%** | 9/17 (53%) |
| 21-30 | 47 | -1.84% | -0.90% | **-0.94%** | 26/47 (55%) |

**En conjunto:** -2.04% de media frente a -1.02% del indice, una diferencia de **-1.01%**. 38 de 73 operaciones (52%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 45 operaciones, media -1.58%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -2.03% | 66 | -133.83 EUR | 4/66 | -10.91 EUR |
| escalera + stop vol x2.5 | -2.31% | 78 | -180.13 EUR | 3/78 | -10.63 EUR |
| trailing pegado (3%) | -2.44% | 92 | -224.54 EUR | 7/92 | -10.00 EUR |
| escalera + stop vol x3 | -2.71% | 77 | -209.04 EUR | 3/77 | -12.76 EUR |
| LA REAL (escalera 25/08) | -3.19% | 251 | -799.61 EUR | 9/251 | -8.08 EUR |
| arranca antes (+3%) | -3.46% | 81 | -280.09 EUR | 6/81 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.67% | 75 | -275.37 EUR | 6/75 | -10.00 EUR |
| arranca despues (+8%) | -3.73% | 73 | -272.39 EUR | 6/73 | -10.00 EUR |
| trailing suelto (7%) | -4.18% | 72 | -300.75 EUR | 5/72 | -10.00 EUR |
| sin trailing, solo stop | -4.47% | 69 | -308.48 EUR | 4/69 | -10.00 EUR |
| stop corto (5%) | -5.27% | 168 | -886.08 EUR | 6/168 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.19%**
- Aciertos (>= 5 EUR limpios): 9/251 (4%)
- Resultado acumulado ficticio: -799.61 EUR sobre 251 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 83 | -2.95 EUR | 2% | 47% |
| nota global | medio | 83 | -3.92 EUR | 2% | 61% |
| nota global | alto | 85 | -2.70 EUR | 6% | 56% |
| puesto en el ranking | bajo | 83 | -2.48 EUR | 6% | 55% |
| puesto en el ranking | medio | 83 | -3.86 EUR | 2% | 58% |
| puesto en el ranking | alto | 85 | -3.22 EUR | 2% | 52% |
| potencial hasta objetivo | bajo | 83 | -3.36 EUR | 5% | 55% |
| potencial hasta objetivo | medio | 83 | -3.57 EUR | 2% | 59% |
| potencial hasta objetivo | alto | 85 | -2.64 EUR | 4% | 51% |
| dispersion | bajo | 83 | -2.66 EUR | 6% | 54% |
| dispersion | medio | 83 | -3.65 EUR | 4% | 59% |
| dispersion | alto | 85 | -3.25 EUR | 1% | 52% |
| % compra fuerte | bajo | 77 | -3.52 EUR | 3% | 56% |
| % compra fuerte | medio | 77 | -2.85 EUR | 4% | 56% |
| % compra fuerte | alto | 79 | -3.43 EUR | 3% | 53% |
| momentum 30d | bajo | 83 | -3.63 EUR | 4% | 58% |
| momentum 30d | medio | 83 | -2.85 EUR | 2% | 51% |
| momentum 30d | alto | 85 | -3.07 EUR | 5% | 56% |
| fuerza relativa | bajo | 83 | -3.61 EUR | 2% | 58% |
| fuerza relativa | medio | 83 | -2.95 EUR | 2% | 51% |
| fuerza relativa | alto | 85 | -3.00 EUR | 6% | 56% |
| RSI | bajo | 83 | -2.82 EUR | 5% | 51% |
| RSI | medio | 83 | -3.14 EUR | 4% | 55% |
| RSI | alto | 85 | -3.59 EUR | 2% | 59% |
| volumen relativo | bajo | 78 | -2.83 EUR | 8% | 56% |
| volumen relativo | medio | 78 | -3.13 EUR | 0% | 49% |
| volumen relativo | alto | 78 | -3.62 EUR | 3% | 55% |
| volatilidad | bajo | 78 | -3.02 EUR | 4% | 50% |
| volatilidad | medio | 78 | -3.46 EUR | 3% | 55% |
| volatilidad | alto | 78 | -3.09 EUR | 4% | 55% |
| liquidez | bajo | 78 | -3.33 EUR | 3% | 54% |
| liquidez | medio | 78 | -3.07 EUR | 4% | 54% |
| liquidez | alto | 78 | -3.18 EUR | 4% | 53% |
| distancia max 52s | bajo | 78 | -2.69 EUR | 4% | 49% |
| distancia max 52s | medio | 78 | -3.14 EUR | 3% | 55% |
| distancia max 52s | alto | 78 | -3.75 EUR | 4% | 56% |
| consenso | buy | 174 | -3.27 EUR | 3% | 54% |
| consenso | strong_buy | 77 | -3.00 EUR | 4% | 57% |
| tendencia tecnica | alcista | 116 | -3.34 EUR | 4% | 57% |
| tendencia tecnica | mixta | 70 | -3.28 EUR | 3% | 56% |
| tendencia tecnica | bajista | 65 | -2.81 EUR | 3% | 51% |
| tendencia analistas | mejorando | 122 | -3.20 EUR | 2% | 53% |
| tendencia analistas | estable | 79 | -3.53 EUR | 5% | 61% |
| tendencia analistas | empeorando | 10 | -5.01 EUR | 0% | 80% |
| regimen de mercado | neutro | 134 | -2.89 EUR | 4% | 50% |
| regimen de mercado | favorable | 111 | -3.44 EUR | 4% | 60% |
| regimen de mercado | adverso | 6 | -5.05 EUR | 0% | 67% |
| catalizador | sin catalizador | 250 | -3.17 EUR | 4% | 55% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.36 | -2.64 | **+0.72 EUR** |
| fuerza relativa | -3.61 | -3.00 | **+0.61 EUR** |
| momentum 30d | -3.63 | -3.07 | **+0.56 EUR** |
| nota global | -2.95 | -2.70 | **+0.25 EUR** |
| liquidez | -3.33 | -3.18 | **+0.15 EUR** |
| % compra fuerte | -3.52 | -3.43 | **+0.10 EUR** |
| volatilidad | -3.02 | -3.09 | **-0.07 EUR** |
| dispersion | -2.66 | -3.25 | **-0.59 EUR** |
| puesto en el ranking | -2.48 | -3.22 | **-0.74 EUR** |
| RSI | -2.82 | -3.59 | **-0.77 EUR** |
| volumen relativo | -2.83 | -3.62 | **-0.79 EUR** |
| distancia max 52s | -2.69 | -3.75 | **-1.06 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
