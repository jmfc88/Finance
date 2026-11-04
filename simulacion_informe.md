# Simulacion en paralelo

Actualizado: 2026-11-04 14:25 · dia 73 de ejecucion
Proxima revision de ponderacion en 2 dias.

- Operaciones cerradas: **271**
- Operaciones abiertas: 62

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 8 | 3% | +8.02 EUR |
| flojo | 98 | 36% | +1.30 EUR |
| plano | 18 | 7% | -1.74 EUR |
| perdida | 85 | 31% | -7.16 EUR |
| nefasta | 58 | 21% | -7.14 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 55 | -2.08% | 4/55 (7%) | 10/55 | 10 |
| 11-20 | 69 | -2.97% | 4/69 (6%) | 8/69 | 10 |
| 21-30 | 147 | -3.24% | 4/147 (3%) | 15/147 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 11 | -0.69% | -1.01% | **+0.33%** | 4/11 (36%) |
| 11-20 | 22 | -2.12% | -0.93% | **-1.20%** | 12/22 (55%) |
| 21-30 | 58 | -1.28% | -0.53% | **-0.75%** | 30/58 (52%) |

**En conjunto:** -1.41% de media frente a -0.69% del indice, una diferencia de **-0.73%**. 46 de 91 operaciones (51%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 50 operaciones, media -1.31%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -1.50% | 85 | -127.49 EUR | 7/85 | -10.91 EUR |
| escalera + stop vol x2.5 | -2.03% | 98 | -199.22 EUR | 5/98 | -10.63 EUR |
| trailing pegado (3%) | -2.24% | 104 | -232.68 EUR | 10/104 | -10.00 EUR |
| escalera + stop vol x3 | -2.34% | 97 | -227.13 EUR | 5/97 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.94% | 271 | -795.53 EUR | 12/271 | -8.08 EUR |
| arranca antes (+3%) | -3.18% | 92 | -292.74 EUR | 9/92 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.35% | 86 | -288.49 EUR | 9/86 | -10.00 EUR |
| arranca despues (+8%) | -3.45% | 83 | -286.08 EUR | 9/83 | -10.00 EUR |
| trailing suelto (7%) | -3.86% | 82 | -316.61 EUR | 8/82 | -10.00 EUR |
| sin trailing, solo stop | -4.14% | 78 | -323.23 EUR | 7/78 | -10.00 EUR |
| stop corto (5%) | -5.00% | 180 | -899.24 EUR | 9/180 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.94%**
- Aciertos (>= 5 EUR limpios): 12/271 (4%)
- Resultado acumulado ficticio: -795.53 EUR sobre 271 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 90 | -2.56 EUR | 3% | 44% |
| nota global | medio | 90 | -3.81 EUR | 2% | 59% |
| nota global | alto | 91 | -2.44 EUR | 8% | 55% |
| puesto en el ranking | bajo | 90 | -2.30 EUR | 8% | 53% |
| puesto en el ranking | medio | 90 | -3.63 EUR | 2% | 57% |
| puesto en el ranking | alto | 91 | -2.88 EUR | 3% | 48% |
| potencial hasta objetivo | bajo | 90 | -3.22 EUR | 4% | 53% |
| potencial hasta objetivo | medio | 90 | -3.36 EUR | 3% | 57% |
| potencial hasta objetivo | alto | 91 | -2.23 EUR | 5% | 48% |
| dispersion | bajo | 90 | -2.67 EUR | 7% | 56% |
| dispersion | medio | 90 | -3.22 EUR | 4% | 53% |
| dispersion | alto | 91 | -2.92 EUR | 2% | 49% |
| % compra fuerte | bajo | 84 | -3.35 EUR | 2% | 54% |
| % compra fuerte | medio | 84 | -2.44 EUR | 6% | 52% |
| % compra fuerte | alto | 84 | -3.17 EUR | 4% | 51% |
| momentum 30d | bajo | 90 | -3.30 EUR | 6% | 57% |
| momentum 30d | medio | 90 | -2.68 EUR | 2% | 48% |
| momentum 30d | alto | 91 | -2.83 EUR | 5% | 54% |
| fuerza relativa | bajo | 90 | -3.37 EUR | 3% | 57% |
| fuerza relativa | medio | 90 | -2.67 EUR | 4% | 49% |
| fuerza relativa | alto | 91 | -2.77 EUR | 5% | 53% |
| RSI | bajo | 90 | -2.55 EUR | 7% | 50% |
| RSI | medio | 90 | -2.98 EUR | 3% | 53% |
| RSI | alto | 91 | -3.27 EUR | 3% | 55% |
| volumen relativo | bajo | 84 | -2.46 EUR | 8% | 52% |
| volumen relativo | medio | 84 | -2.81 EUR | 1% | 46% |
| volumen relativo | alto | 86 | -3.49 EUR | 3% | 55% |
| volatilidad | bajo | 84 | -2.78 EUR | 5% | 48% |
| volatilidad | medio | 84 | -3.10 EUR | 4% | 52% |
| volatilidad | alto | 86 | -2.91 EUR | 5% | 53% |
| liquidez | bajo | 84 | -3.30 EUR | 2% | 54% |
| liquidez | medio | 84 | -2.44 EUR | 6% | 49% |
| liquidez | alto | 86 | -3.04 EUR | 5% | 51% |
| distancia max 52s | bajo | 84 | -2.56 EUR | 4% | 46% |
| distancia max 52s | medio | 84 | -2.63 EUR | 5% | 52% |
| distancia max 52s | alto | 86 | -3.57 EUR | 5% | 55% |
| consenso | buy | 186 | -3.03 EUR | 4% | 52% |
| consenso | strong_buy | 85 | -2.72 EUR | 6% | 55% |
| tendencia tecnica | alcista | 124 | -3.12 EUR | 5% | 54% |
| tendencia tecnica | mixta | 76 | -3.07 EUR | 4% | 55% |
| tendencia tecnica | bajista | 71 | -2.47 EUR | 4% | 48% |
| tendencia analistas | mejorando | 130 | -2.95 EUR | 3% | 52% |
| tendencia analistas | estable | 87 | -3.27 EUR | 6% | 57% |
| tendencia analistas | empeorando | 12 | -3.34 EUR | 8% | 67% |
| regimen de mercado | neutro | 144 | -2.54 EUR | 6% | 48% |
| regimen de mercado | favorable | 114 | -3.40 EUR | 4% | 60% |
| regimen de mercado | adverso | 13 | -3.19 EUR | 0% | 46% |
| catalizador | sin catalizador | 269 | -2.90 EUR | 4% | 52% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.22 | -2.23 | **+0.99 EUR** |
| fuerza relativa | -3.37 | -2.77 | **+0.60 EUR** |
| momentum 30d | -3.30 | -2.83 | **+0.47 EUR** |
| liquidez | -3.30 | -3.04 | **+0.26 EUR** |
| % compra fuerte | -3.35 | -3.17 | **+0.18 EUR** |
| nota global | -2.56 | -2.44 | **+0.11 EUR** |
| volatilidad | -2.78 | -2.91 | **-0.13 EUR** |
| dispersion | -2.67 | -2.92 | **-0.26 EUR** |
| puesto en el ranking | -2.30 | -2.88 | **-0.58 EUR** |
| RSI | -2.55 | -3.27 | **-0.72 EUR** |
| distancia max 52s | -2.56 | -3.57 | **-1.00 EUR** |
| volumen relativo | -2.46 | -3.49 | **-1.03 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
