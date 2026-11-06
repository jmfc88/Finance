# Simulacion en paralelo

Actualizado: 2026-11-06 01:35 · dia 75 de ejecucion
**Revision nº5 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **289**
- Operaciones abiertas: 61

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 11 | 4% | +8.70 EUR |
| flojo | 107 | 37% | +1.32 EUR |
| plano | 18 | 6% | -1.74 EUR |
| perdida | 87 | 30% | -7.18 EUR |
| nefasta | 62 | 21% | -7.20 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 58 | -1.97% | 5/58 (9%) | 12/58 | 10 |
| 11-20 | 73 | -2.57% | 6/73 (8%) | 11/73 | 9 |
| 21-30 | 158 | -3.14% | 4/158 (3%) | 19/158 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 14 | -0.54% | -0.48% | **-0.06%** | 6/14 (43%) |
| 11-20 | 26 | -1.13% | -0.76% | **-0.37%** | 15/26 (58%) |
| 21-30 | 69 | -1.37% | -0.44% | **-0.93%** | 35/69 (51%) |

**En conjunto:** -1.21% de media frente a -0.52% del indice, una diferencia de **-0.68%**. 56 de 109 operaciones (51%) batieron a su indice.

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
| escalera + stop vol x4 | -1.13% | 101 | -113.82 EUR | 10/101 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.75% | 116 | -202.97 EUR | 8/116 | -10.63 EUR |
| trailing pegado (3%) | -1.75% | 113 | -198.09 EUR | 14/113 | -10.00 EUR |
| escalera + stop vol x3 | -1.94% | 113 | -218.97 EUR | 8/113 | -12.76 EUR |
| arranca antes (+3%) | -2.70% | 102 | -275.06 EUR | 12/102 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.76% | 289 | -798.43 EUR | 15/289 | -8.08 EUR |
| actual (8% / +5% / 5%) | -2.81% | 95 | -267.04 EUR | 12/95 | -10.00 EUR |
| arranca despues (+8%) | -2.96% | 88 | -260.27 EUR | 12/88 | -10.00 EUR |
| trailing suelto (7%) | -3.44% | 87 | -299.02 EUR | 11/87 | -10.00 EUR |
| sin trailing, solo stop | -3.87% | 81 | -313.32 EUR | 9/81 | -10.00 EUR |
| stop corto (5%) | -4.70% | 195 | -916.79 EUR | 12/195 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.76%**
- Aciertos (>= 5 EUR limpios): 15/289 (5%)
- Resultado acumulado ficticio: -798.43 EUR sobre 289 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 96 | -2.39 EUR | 3% | 43% |
| nota global | medio | 96 | -3.67 EUR | 3% | 58% |
| nota global | alto | 97 | -2.23 EUR | 9% | 54% |
| puesto en el ranking | bajo | 96 | -2.22 EUR | 8% | 53% |
| puesto en el ranking | medio | 96 | -3.36 EUR | 4% | 55% |
| puesto en el ranking | alto | 97 | -2.71 EUR | 3% | 46% |
| potencial hasta objetivo | bajo | 96 | -3.23 EUR | 4% | 53% |
| potencial hasta objetivo | medio | 96 | -3.14 EUR | 4% | 55% |
| potencial hasta objetivo | alto | 97 | -1.93 EUR | 7% | 46% |
| dispersion | bajo | 96 | -2.36 EUR | 8% | 53% |
| dispersion | medio | 96 | -3.20 EUR | 4% | 53% |
| dispersion | alto | 97 | -2.73 EUR | 3% | 48% |
| % compra fuerte | bajo | 90 | -3.17 EUR | 3% | 52% |
| % compra fuerte | medio | 90 | -2.49 EUR | 7% | 53% |
| % compra fuerte | alto | 90 | -2.74 EUR | 4% | 48% |
| momentum 30d | bajo | 96 | -2.86 EUR | 6% | 53% |
| momentum 30d | medio | 96 | -2.41 EUR | 4% | 46% |
| momentum 30d | alto | 97 | -3.02 EUR | 5% | 56% |
| fuerza relativa | bajo | 96 | -3.23 EUR | 3% | 55% |
| fuerza relativa | medio | 96 | -2.21 EUR | 7% | 47% |
| fuerza relativa | alto | 97 | -2.84 EUR | 5% | 53% |
| RSI | bajo | 96 | -2.39 EUR | 7% | 49% |
| RSI | medio | 96 | -2.68 EUR | 4% | 51% |
| RSI | alto | 97 | -3.21 EUR | 4% | 55% |
| volumen relativo | bajo | 90 | -2.11 EUR | 9% | 49% |
| volumen relativo | medio | 90 | -2.77 EUR | 3% | 48% |
| volumen relativo | alto | 92 | -3.33 EUR | 3% | 53% |
| volatilidad | bajo | 90 | -2.63 EUR | 6% | 47% |
| volatilidad | medio | 90 | -2.91 EUR | 6% | 52% |
| volatilidad | alto | 92 | -2.70 EUR | 4% | 51% |
| liquidez | bajo | 90 | -3.24 EUR | 3% | 53% |
| liquidez | medio | 90 | -2.37 EUR | 7% | 49% |
| liquidez | alto | 92 | -2.62 EUR | 5% | 48% |
| distancia max 52s | bajo | 90 | -2.08 EUR | 4% | 42% |
| distancia max 52s | medio | 90 | -2.53 EUR | 6% | 52% |
| distancia max 52s | alto | 92 | -3.60 EUR | 5% | 55% |
| consenso | buy | 201 | -2.83 EUR | 4% | 50% |
| consenso | strong_buy | 88 | -2.60 EUR | 7% | 55% |
| tendencia tecnica | alcista | 132 | -3.20 EUR | 5% | 55% |
| tendencia tecnica | mixta | 81 | -2.80 EUR | 5% | 53% |
| tendencia tecnica | bajista | 76 | -1.97 EUR | 7% | 45% |
| tendencia analistas | mejorando | 138 | -2.54 EUR | 4% | 49% |
| tendencia analistas | estable | 93 | -3.32 EUR | 6% | 58% |
| tendencia analistas | empeorando | 12 | -3.34 EUR | 8% | 67% |
| regimen de mercado | neutro | 156 | -2.11 EUR | 7% | 45% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 18 | -4.55 EUR | 0% | 61% |
| catalizador | sin catalizador | 286 | -2.74 EUR | 5% | 51% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.23 | -1.93 | **+1.30 EUR** |
| liquidez | -3.24 | -2.62 | **+0.62 EUR** |
| % compra fuerte | -3.17 | -2.74 | **+0.43 EUR** |
| fuerza relativa | -3.23 | -2.84 | **+0.39 EUR** |
| nota global | -2.39 | -2.23 | **+0.16 EUR** |
| volatilidad | -2.63 | -2.70 | **-0.07 EUR** |
| momentum 30d | -2.86 | -3.02 | **-0.17 EUR** |
| dispersion | -2.36 | -2.73 | **-0.37 EUR** |
| puesto en el ranking | -2.22 | -2.71 | **-0.49 EUR** |
| RSI | -2.39 | -3.21 | **-0.82 EUR** |
| volumen relativo | -2.11 | -3.33 | **-1.22 EUR** |
| distancia max 52s | -2.08 | -3.60 | **-1.52 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
