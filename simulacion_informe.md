# Simulacion en paralelo

Actualizado: 2026-10-30 18:36 · dia 68 de ejecucion
Proxima revision de ponderacion en 7 dias.

- Operaciones cerradas: **252**
- Operaciones abiertas: 63

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 2% | +16.71 EUR |
| beneficio | 5 | 2% | +7.59 EUR |
| flojo | 88 | 35% | +1.34 EUR |
| plano | 17 | 7% | -1.72 EUR |
| perdida | 83 | 33% | -7.22 EUR |
| nefasta | 55 | 22% | -7.09 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 52 | -2.24% | 3/52 (6%) | 9/52 | 10 |
| 11-20 | 63 | -3.09% | 3/63 (5%) | 7/63 | 9 |
| 21-30 | 137 | -3.54% | 3/137 (2%) | 13/137 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 9 | -1.96% | -1.58% | **-0.38%** | 3/9 (33%) |
| 11-20 | 17 | -2.64% | -1.08% | **-1.56%** | 9/17 (53%) |
| 21-30 | 48 | -1.72% | -0.90% | **-0.82%** | 27/48 (56%) |

**En conjunto:** -1.96% de media frente a -1.02% del indice, una diferencia de **-0.94%**. 39 de 74 operaciones (53%) batieron a su indice.

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
| escalera + stop vol x4 | -1.94% | 67 | -130.29 EUR | 4/67 | -10.91 EUR |
| escalera + stop vol x2.5 | -2.24% | 79 | -176.59 EUR | 3/79 | -10.63 EUR |
| trailing pegado (3%) | -2.38% | 93 | -221.31 EUR | 7/93 | -10.00 EUR |
| escalera + stop vol x3 | -2.63% | 78 | -205.50 EUR | 3/78 | -12.76 EUR |
| LA REAL (escalera 25/08) | -3.16% | 252 | -796.07 EUR | 9/252 | -8.08 EUR |
| arranca antes (+3%) | -3.40% | 82 | -279.03 EUR | 6/82 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.61% | 76 | -274.31 EUR | 6/76 | -10.00 EUR |
| arranca despues (+8%) | -3.67% | 74 | -271.33 EUR | 6/74 | -10.00 EUR |
| trailing suelto (7%) | -4.14% | 73 | -301.86 EUR | 5/73 | -10.00 EUR |
| sin trailing, solo stop | -4.47% | 69 | -308.48 EUR | 4/69 | -10.00 EUR |
| stop corto (5%) | -5.24% | 169 | -885.02 EUR | 6/169 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.16%**
- Aciertos (>= 5 EUR limpios): 9/252 (4%)
- Resultado acumulado ficticio: -796.07 EUR sobre 252 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 84 | -2.87 EUR | 2% | 46% |
| nota global | medio | 84 | -3.97 EUR | 2% | 62% |
| nota global | alto | 84 | -2.64 EUR | 6% | 56% |
| puesto en el ranking | bajo | 84 | -2.46 EUR | 6% | 55% |
| puesto en el ranking | medio | 84 | -3.83 EUR | 2% | 58% |
| puesto en el ranking | alto | 84 | -3.19 EUR | 2% | 51% |
| potencial hasta objetivo | bajo | 84 | -3.31 EUR | 5% | 55% |
| potencial hasta objetivo | medio | 84 | -3.73 EUR | 2% | 61% |
| potencial hasta objetivo | alto | 84 | -2.44 EUR | 4% | 49% |
| dispersion | bajo | 84 | -2.72 EUR | 6% | 55% |
| dispersion | medio | 84 | -3.60 EUR | 4% | 58% |
| dispersion | alto | 84 | -3.16 EUR | 1% | 51% |
| % compra fuerte | bajo | 78 | -3.50 EUR | 3% | 55% |
| % compra fuerte | medio | 78 | -2.85 EUR | 4% | 56% |
| % compra fuerte | alto | 78 | -3.37 EUR | 3% | 53% |
| momentum 30d | bajo | 84 | -3.55 EUR | 4% | 57% |
| momentum 30d | medio | 84 | -2.81 EUR | 2% | 50% |
| momentum 30d | alto | 84 | -3.12 EUR | 5% | 57% |
| fuerza relativa | bajo | 84 | -3.53 EUR | 2% | 57% |
| fuerza relativa | medio | 84 | -3.01 EUR | 2% | 51% |
| fuerza relativa | alto | 84 | -2.94 EUR | 6% | 56% |
| RSI | bajo | 84 | -2.74 EUR | 5% | 50% |
| RSI | medio | 84 | -3.20 EUR | 4% | 56% |
| RSI | alto | 84 | -3.54 EUR | 2% | 58% |
| volumen relativo | bajo | 78 | -2.83 EUR | 8% | 56% |
| volumen relativo | medio | 78 | -3.13 EUR | 0% | 49% |
| volumen relativo | alto | 79 | -3.53 EUR | 3% | 54% |
| volatilidad | bajo | 78 | -3.02 EUR | 4% | 50% |
| volatilidad | medio | 78 | -3.46 EUR | 3% | 55% |
| volatilidad | alto | 79 | -3.01 EUR | 4% | 54% |
| liquidez | bajo | 78 | -3.33 EUR | 3% | 54% |
| liquidez | medio | 78 | -3.07 EUR | 4% | 54% |
| liquidez | alto | 79 | -3.10 EUR | 4% | 52% |
| distancia max 52s | bajo | 78 | -2.86 EUR | 3% | 49% |
| distancia max 52s | medio | 78 | -2.83 EUR | 4% | 54% |
| distancia max 52s | alto | 79 | -3.80 EUR | 4% | 57% |
| consenso | buy | 174 | -3.27 EUR | 3% | 54% |
| consenso | strong_buy | 78 | -2.92 EUR | 4% | 56% |
| tendencia tecnica | alcista | 116 | -3.34 EUR | 4% | 57% |
| tendencia tecnica | mixta | 71 | -3.18 EUR | 3% | 55% |
| tendencia tecnica | bajista | 65 | -2.81 EUR | 3% | 51% |
| tendencia analistas | mejorando | 123 | -3.14 EUR | 2% | 53% |
| tendencia analistas | estable | 79 | -3.53 EUR | 5% | 61% |
| tendencia analistas | empeorando | 10 | -5.01 EUR | 0% | 80% |
| regimen de mercado | neutro | 135 | -2.85 EUR | 4% | 50% |
| regimen de mercado | favorable | 111 | -3.44 EUR | 4% | 60% |
| regimen de mercado | adverso | 6 | -5.05 EUR | 0% | 67% |
| catalizador | sin catalizador | 251 | -3.14 EUR | 4% | 55% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.31 | -2.44 | **+0.87 EUR** |
| fuerza relativa | -3.53 | -2.94 | **+0.59 EUR** |
| momentum 30d | -3.55 | -3.12 | **+0.43 EUR** |
| nota global | -2.87 | -2.64 | **+0.24 EUR** |
| liquidez | -3.33 | -3.10 | **+0.23 EUR** |
| % compra fuerte | -3.50 | -3.37 | **+0.13 EUR** |
| volatilidad | -3.02 | -3.01 | **+0.01 EUR** |
| dispersion | -2.72 | -3.16 | **-0.44 EUR** |
| volumen relativo | -2.83 | -3.53 | **-0.70 EUR** |
| puesto en el ranking | -2.46 | -3.19 | **-0.72 EUR** |
| RSI | -2.74 | -3.54 | **-0.79 EUR** |
| distancia max 52s | -2.86 | -3.80 | **-0.94 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
