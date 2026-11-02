# Simulacion en paralelo

Actualizado: 2026-11-02 07:39 · dia 71 de ejecucion
Proxima revision de ponderacion en 4 dias.

- Operaciones cerradas: **255**
- Operaciones abiertas: 63

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 2% | +16.71 EUR |
| beneficio | 5 | 2% | +7.59 EUR |
| flojo | 89 | 35% | +1.33 EUR |
| plano | 17 | 7% | -1.72 EUR |
| perdida | 83 | 33% | -7.22 EUR |
| nefasta | 57 | 22% | -7.12 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 53 | -2.35% | 3/53 (6%) | 9/53 | 10 |
| 11-20 | 64 | -3.17% | 3/64 (5%) | 7/64 | 9 |
| 21-30 | 138 | -3.51% | 3/138 (2%) | 13/138 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 9 | -1.96% | -1.58% | **-0.38%** | 3/9 (33%) |
| 11-20 | 17 | -2.64% | -1.08% | **-1.56%** | 9/17 (53%) |
| 21-30 | 49 | -1.67% | -0.92% | **-0.75%** | 28/49 (57%) |

**En conjunto:** -1.92% de media frente a -1.03% del indice, una diferencia de **-0.89%**. 40 de 75 operaciones (53%) batieron a su indice.

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
| escalera + stop vol x4 | -2.00% | 69 | -138.26 EUR | 4/69 | -10.91 EUR |
| escalera + stop vol x2.5 | -2.30% | 82 | -188.83 EUR | 3/82 | -10.63 EUR |
| trailing pegado (3%) | -2.54% | 95 | -241.31 EUR | 7/95 | -10.00 EUR |
| escalera + stop vol x3 | -2.72% | 81 | -220.38 EUR | 3/81 | -12.76 EUR |
| LA REAL (escalera 25/08) | -3.18% | 255 | -811.23 EUR | 9/255 | -8.08 EUR |
| arranca antes (+3%) | -3.56% | 84 | -299.03 EUR | 6/84 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.77% | 78 | -294.31 EUR | 6/78 | -10.00 EUR |
| arranca despues (+8%) | -3.83% | 76 | -291.33 EUR | 6/76 | -10.00 EUR |
| trailing suelto (7%) | -4.29% | 75 | -321.86 EUR | 5/75 | -10.00 EUR |
| sin trailing, solo stop | -4.63% | 71 | -328.48 EUR | 4/71 | -10.00 EUR |
| stop corto (5%) | -5.27% | 172 | -906.02 EUR | 6/172 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.18%**
- Aciertos (>= 5 EUR limpios): 9/255 (4%)
- Resultado acumulado ficticio: -811.23 EUR sobre 255 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 85 | -2.83 EUR | 2% | 46% |
| nota global | medio | 85 | -4.02 EUR | 2% | 62% |
| nota global | alto | 85 | -2.70 EUR | 6% | 56% |
| puesto en el ranking | bajo | 85 | -2.61 EUR | 6% | 56% |
| puesto en el ranking | medio | 85 | -3.74 EUR | 2% | 56% |
| puesto en el ranking | alto | 85 | -3.19 EUR | 2% | 52% |
| potencial hasta objetivo | bajo | 85 | -3.36 EUR | 5% | 55% |
| potencial hasta objetivo | medio | 85 | -3.67 EUR | 2% | 60% |
| potencial hasta objetivo | alto | 85 | -2.51 EUR | 4% | 49% |
| dispersion | bajo | 85 | -2.74 EUR | 6% | 55% |
| dispersion | medio | 85 | -3.59 EUR | 4% | 58% |
| dispersion | alto | 85 | -3.22 EUR | 1% | 52% |
| % compra fuerte | bajo | 79 | -3.64 EUR | 3% | 57% |
| % compra fuerte | medio | 79 | -2.84 EUR | 4% | 56% |
| % compra fuerte | alto | 79 | -3.31 EUR | 3% | 52% |
| momentum 30d | bajo | 85 | -3.60 EUR | 4% | 58% |
| momentum 30d | medio | 85 | -2.76 EUR | 2% | 49% |
| momentum 30d | alto | 85 | -3.18 EUR | 5% | 58% |
| fuerza relativa | bajo | 85 | -3.52 EUR | 2% | 56% |
| fuerza relativa | medio | 85 | -3.02 EUR | 2% | 52% |
| fuerza relativa | alto | 85 | -3.00 EUR | 6% | 56% |
| RSI | bajo | 85 | -2.84 EUR | 5% | 51% |
| RSI | medio | 85 | -3.12 EUR | 4% | 55% |
| RSI | alto | 85 | -3.59 EUR | 2% | 59% |
| volumen relativo | bajo | 79 | -2.78 EUR | 8% | 56% |
| volumen relativo | medio | 79 | -3.19 EUR | 0% | 49% |
| volumen relativo | alto | 80 | -3.59 EUR | 2% | 55% |
| volatilidad | bajo | 79 | -3.04 EUR | 4% | 51% |
| volatilidad | medio | 79 | -3.43 EUR | 3% | 54% |
| volatilidad | alto | 80 | -3.10 EUR | 4% | 55% |
| liquidez | bajo | 79 | -3.27 EUR | 3% | 53% |
| liquidez | medio | 79 | -3.24 EUR | 4% | 56% |
| liquidez | alto | 80 | -3.06 EUR | 4% | 51% |
| distancia max 52s | bajo | 79 | -2.81 EUR | 3% | 48% |
| distancia max 52s | medio | 79 | -2.89 EUR | 4% | 54% |
| distancia max 52s | alto | 80 | -3.86 EUR | 4% | 57% |
| consenso | buy | 175 | -3.30 EUR | 3% | 54% |
| consenso | strong_buy | 80 | -2.93 EUR | 4% | 56% |
| tendencia tecnica | alcista | 117 | -3.38 EUR | 4% | 57% |
| tendencia tecnica | mixta | 72 | -3.25 EUR | 3% | 56% |
| tendencia tecnica | bajista | 66 | -2.76 EUR | 3% | 50% |
| tendencia analistas | mejorando | 124 | -3.18 EUR | 2% | 53% |
| tendencia analistas | estable | 81 | -3.53 EUR | 5% | 60% |
| tendencia analistas | empeorando | 10 | -5.01 EUR | 0% | 80% |
| regimen de mercado | neutro | 135 | -2.85 EUR | 4% | 50% |
| regimen de mercado | favorable | 113 | -3.44 EUR | 4% | 60% |
| regimen de mercado | adverso | 7 | -5.49 EUR | 0% | 71% |
| catalizador | sin catalizador | 253 | -3.14 EUR | 4% | 55% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.36 | -2.51 | **+0.86 EUR** |
| fuerza relativa | -3.52 | -3.00 | **+0.52 EUR** |
| momentum 30d | -3.60 | -3.18 | **+0.42 EUR** |
| % compra fuerte | -3.64 | -3.31 | **+0.33 EUR** |
| liquidez | -3.27 | -3.06 | **+0.22 EUR** |
| nota global | -2.83 | -2.70 | **+0.13 EUR** |
| volatilidad | -3.04 | -3.10 | **-0.07 EUR** |
| dispersion | -2.74 | -3.22 | **-0.48 EUR** |
| puesto en el ranking | -2.61 | -3.19 | **-0.58 EUR** |
| RSI | -2.84 | -3.59 | **-0.76 EUR** |
| volumen relativo | -2.78 | -3.59 | **-0.80 EUR** |
| distancia max 52s | -2.81 | -3.86 | **-1.05 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
