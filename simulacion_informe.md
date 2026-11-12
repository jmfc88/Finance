# Simulacion en paralelo

Actualizado: 2026-11-12 15:05 · dia 81 de ejecucion
Proxima revision de ponderacion en 9 dias.

- Operaciones cerradas: **332**
- Operaciones abiertas: 66

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 14 | 4% | +8.78 EUR |
| flojo | 141 | 42% | +1.30 EUR |
| plano | 18 | 5% | -1.74 EUR |
| perdida | 89 | 27% | -7.20 EUR |
| nefasta | 66 | 20% | -7.25 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 63 | -1.74% | 5/63 (8%) | 13/63 | 10 |
| 11-20 | 83 | -2.36% | 6/83 (7%) | 13/83 | 9 |
| 21-30 | 186 | -2.54% | 7/186 (4%) | 28/186 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 19 | -0.14% | -0.28% | **+0.15%** | 11/19 (58%) |
| 11-20 | 34 | -0.63% | -0.23% | **-0.40%** | 20/34 (59%) |
| 21-30 | 96 | -0.65% | -0.08% | **-0.58%** | 50/96 (52%) |

**En conjunto:** -0.58% de media frente a -0.14% del indice, una diferencia de **-0.44%**. 81 de 149 operaciones (54%) batieron a su indice.

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
| escalera + stop vol x4 | -0.69% | 143 | -98.04 EUR | 13/143 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.33% | 159 | -211.10 EUR | 11/159 | -10.63 EUR |
| escalera + stop vol x3 | -1.43% | 155 | -221.67 EUR | 11/155 | -12.76 EUR |
| trailing pegado (3%) | -1.55% | 128 | -198.48 EUR | 16/128 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.34% | 332 | -778.04 EUR | 18/332 | -8.08 EUR |
| arranca antes (+3%) | -2.89% | 108 | -312.13 EUR | 12/108 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.00% | 100 | -300.40 EUR | 12/100 | -10.00 EUR |
| arranca despues (+8%) | -3.19% | 91 | -290.27 EUR | 12/91 | -10.00 EUR |
| trailing suelto (7%) | -3.66% | 90 | -329.02 EUR | 11/90 | -10.00 EUR |
| sin trailing, solo stop | -4.09% | 84 | -343.32 EUR | 9/84 | -10.00 EUR |
| stop corto (5%) | -4.75% | 204 | -969.15 EUR | 12/204 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.34%**
- Aciertos (>= 5 EUR limpios): 18/332 (5%)
- Resultado acumulado ficticio: -778.04 EUR sobre 332 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 110 | -1.55 EUR | 5% | 35% |
| nota global | medio | 110 | -3.45 EUR | 3% | 55% |
| nota global | alto | 112 | -2.04 EUR | 9% | 51% |
| puesto en el ranking | bajo | 110 | -2.10 EUR | 7% | 49% |
| puesto en el ranking | medio | 110 | -2.67 EUR | 5% | 49% |
| puesto en el ranking | alto | 112 | -2.26 EUR | 4% | 42% |
| potencial hasta objetivo | bajo | 110 | -2.72 EUR | 5% | 47% |
| potencial hasta objetivo | medio | 110 | -2.64 EUR | 4% | 49% |
| potencial hasta objetivo | alto | 112 | -1.69 EUR | 8% | 44% |
| dispersion | bajo | 110 | -2.29 EUR | 7% | 50% |
| dispersion | medio | 110 | -2.52 EUR | 5% | 46% |
| dispersion | alto | 112 | -2.23 EUR | 4% | 44% |
| % compra fuerte | bajo | 104 | -2.87 EUR | 3% | 48% |
| % compra fuerte | medio | 104 | -1.79 EUR | 9% | 46% |
| % compra fuerte | alto | 104 | -2.45 EUR | 4% | 44% |
| momentum 30d | bajo | 110 | -2.46 EUR | 7% | 49% |
| momentum 30d | medio | 110 | -2.07 EUR | 5% | 44% |
| momentum 30d | alto | 112 | -2.49 EUR | 4% | 47% |
| fuerza relativa | bajo | 110 | -2.76 EUR | 5% | 53% |
| fuerza relativa | medio | 110 | -2.04 EUR | 5% | 43% |
| fuerza relativa | alto | 112 | -2.23 EUR | 5% | 45% |
| RSI | bajo | 110 | -2.46 EUR | 6% | 49% |
| RSI | medio | 110 | -2.07 EUR | 7% | 46% |
| RSI | alto | 112 | -2.50 EUR | 3% | 45% |
| volumen relativo | bajo | 105 | -1.75 EUR | 10% | 45% |
| volumen relativo | medio | 105 | -2.41 EUR | 3% | 44% |
| volumen relativo | alto | 105 | -2.75 EUR | 4% | 47% |
| volatilidad | bajo | 105 | -1.99 EUR | 7% | 41% |
| volatilidad | medio | 105 | -2.56 EUR | 6% | 48% |
| volatilidad | alto | 105 | -2.36 EUR | 4% | 47% |
| liquidez | bajo | 105 | -2.91 EUR | 4% | 50% |
| liquidez | medio | 105 | -1.95 EUR | 7% | 44% |
| liquidez | alto | 105 | -2.05 EUR | 6% | 42% |
| distancia max 52s | bajo | 105 | -1.71 EUR | 6% | 40% |
| distancia max 52s | medio | 105 | -1.93 EUR | 7% | 44% |
| distancia max 52s | alto | 105 | -3.27 EUR | 4% | 51% |
| consenso | buy | 236 | -2.37 EUR | 5% | 45% |
| consenso | strong_buy | 96 | -2.28 EUR | 6% | 50% |
| tendencia tecnica | alcista | 153 | -2.73 EUR | 5% | 49% |
| tendencia tecnica | mixta | 95 | -2.41 EUR | 5% | 48% |
| tendencia tecnica | bajista | 84 | -1.56 EUR | 7% | 40% |
| tendencia analistas | mejorando | 151 | -2.28 EUR | 4% | 45% |
| tendencia analistas | estable | 113 | -2.70 EUR | 8% | 52% |
| tendencia analistas | empeorando | 13 | -3.00 EUR | 8% | 62% |
| regimen de mercado | neutro | 166 | -1.90 EUR | 7% | 43% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 51 | -1.48 EUR | 4% | 31% |
| catalizador | con catalizador | 11 | -0.74 EUR | 9% | 27% |
| catalizador | sin catalizador | 321 | -2.40 EUR | 5% | 47% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.72 | -1.69 | **+1.03 EUR** |
| liquidez | -2.91 | -2.05 | **+0.86 EUR** |
| fuerza relativa | -2.76 | -2.23 | **+0.53 EUR** |
| % compra fuerte | -2.87 | -2.45 | **+0.42 EUR** |
| dispersion | -2.29 | -2.23 | **+0.06 EUR** |
| momentum 30d | -2.46 | -2.49 | **-0.03 EUR** |
| RSI | -2.46 | -2.50 | **-0.04 EUR** |
| puesto en el ranking | -2.10 | -2.26 | **-0.16 EUR** |
| volatilidad | -1.99 | -2.36 | **-0.37 EUR** |
| nota global | -1.55 | -2.04 | **-0.50 EUR** |
| volumen relativo | -1.75 | -2.75 | **-1.00 EUR** |
| distancia max 52s | -1.71 | -3.27 | **-1.56 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
