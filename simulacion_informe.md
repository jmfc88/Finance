# Simulacion en paralelo

Actualizado: 2026-11-09 07:55 · dia 78 de ejecucion
Proxima revision de ponderacion en 12 dias.

- Operaciones cerradas: **315**
- Operaciones abiertas: 56

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 14 | 4% | +8.78 EUR |
| flojo | 125 | 40% | +1.30 EUR |
| plano | 18 | 6% | -1.74 EUR |
| perdida | 88 | 28% | -7.19 EUR |
| nefasta | 66 | 21% | -7.25 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 62 | -1.78% | 5/62 (8%) | 13/62 | 10 |
| 11-20 | 79 | -2.53% | 6/79 (8%) | 11/79 | 9 |
| 21-30 | 174 | -2.76% | 7/174 (4%) | 23/174 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 18 | -0.20% | -0.33% | **+0.13%** | 10/18 (56%) |
| 11-20 | 30 | -0.85% | -0.62% | **-0.23%** | 19/30 (63%) |
| 21-30 | 84 | -0.84% | -0.38% | **-0.46%** | 47/84 (56%) |

**En conjunto:** -0.76% de media frente a -0.43% del indice, una diferencia de **-0.33%**. 76 de 132 operaciones (58%) batieron a su indice.

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
| escalera + stop vol x4 | -0.91% | 126 | -114.06 EUR | 13/126 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.57% | 142 | -223.09 EUR | 11/142 | -10.63 EUR |
| trailing pegado (3%) | -1.68% | 123 | -206.59 EUR | 16/123 | -10.00 EUR |
| escalera + stop vol x3 | -1.69% | 138 | -233.22 EUR | 11/138 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.51% | 315 | -791.03 EUR | 18/315 | -8.08 EUR |
| arranca antes (+3%) | -2.90% | 107 | -310.18 EUR | 12/107 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.01% | 99 | -298.45 EUR | 12/99 | -10.00 EUR |
| arranca despues (+8%) | -3.19% | 91 | -290.27 EUR | 12/91 | -10.00 EUR |
| trailing suelto (7%) | -3.66% | 90 | -329.02 EUR | 11/90 | -10.00 EUR |
| sin trailing, solo stop | -4.09% | 84 | -343.32 EUR | 9/84 | -10.00 EUR |
| stop corto (5%) | -4.75% | 202 | -960.20 EUR | 12/202 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.51%**
- Aciertos (>= 5 EUR limpios): 18/315 (6%)
- Resultado acumulado ficticio: -791.03 EUR sobre 315 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 105 | -2.06 EUR | 5% | 40% |
| nota global | medio | 105 | -3.34 EUR | 4% | 55% |
| nota global | alto | 105 | -2.13 EUR | 9% | 51% |
| puesto en el ranking | bajo | 105 | -2.22 EUR | 8% | 51% |
| puesto en el ranking | medio | 105 | -2.84 EUR | 6% | 50% |
| puesto en el ranking | alto | 105 | -2.48 EUR | 4% | 45% |
| potencial hasta objetivo | bajo | 105 | -2.89 EUR | 5% | 50% |
| potencial hasta objetivo | medio | 105 | -2.67 EUR | 5% | 50% |
| potencial hasta objetivo | alto | 105 | -1.97 EUR | 8% | 47% |
| dispersion | bajo | 105 | -2.27 EUR | 8% | 50% |
| dispersion | medio | 105 | -2.80 EUR | 5% | 50% |
| dispersion | alto | 105 | -2.47 EUR | 5% | 47% |
| % compra fuerte | bajo | 98 | -2.83 EUR | 3% | 48% |
| % compra fuerte | medio | 98 | -2.24 EUR | 9% | 52% |
| % compra fuerte | alto | 100 | -2.52 EUR | 4% | 45% |
| momentum 30d | bajo | 105 | -2.70 EUR | 6% | 50% |
| momentum 30d | medio | 105 | -2.11 EUR | 7% | 46% |
| momentum 30d | alto | 105 | -2.73 EUR | 5% | 50% |
| fuerza relativa | bajo | 105 | -2.90 EUR | 5% | 53% |
| fuerza relativa | medio | 105 | -2.19 EUR | 7% | 46% |
| fuerza relativa | alto | 105 | -2.44 EUR | 6% | 48% |
| RSI | bajo | 105 | -2.48 EUR | 7% | 50% |
| RSI | medio | 105 | -2.37 EUR | 7% | 50% |
| RSI | alto | 105 | -2.69 EUR | 4% | 48% |
| volumen relativo | bajo | 99 | -1.85 EUR | 10% | 46% |
| volumen relativo | medio | 99 | -2.46 EUR | 3% | 44% |
| volumen relativo | alto | 100 | -3.12 EUR | 4% | 51% |
| volatilidad | bajo | 99 | -2.08 EUR | 7% | 42% |
| volatilidad | medio | 99 | -2.96 EUR | 4% | 49% |
| volatilidad | alto | 100 | -2.40 EUR | 6% | 50% |
| liquidez | bajo | 99 | -3.05 EUR | 4% | 52% |
| liquidez | medio | 99 | -2.16 EUR | 7% | 46% |
| liquidez | alto | 100 | -2.23 EUR | 6% | 44% |
| distancia max 52s | bajo | 99 | -1.90 EUR | 6% | 42% |
| distancia max 52s | medio | 99 | -2.10 EUR | 7% | 46% |
| distancia max 52s | alto | 100 | -3.42 EUR | 4% | 53% |
| consenso | buy | 223 | -2.54 EUR | 5% | 48% |
| consenso | strong_buy | 92 | -2.45 EUR | 7% | 52% |
| tendencia tecnica | alcista | 146 | -2.84 EUR | 5% | 51% |
| tendencia tecnica | mixta | 90 | -2.63 EUR | 6% | 51% |
| tendencia tecnica | bajista | 79 | -1.76 EUR | 8% | 43% |
| tendencia analistas | mejorando | 143 | -2.48 EUR | 4% | 48% |
| tendencia analistas | estable | 108 | -2.81 EUR | 8% | 54% |
| tendencia analistas | empeorando | 13 | -3.00 EUR | 8% | 62% |
| regimen de mercado | neutro | 161 | -2.01 EUR | 7% | 44% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 39 | -2.08 EUR | 5% | 38% |
| catalizador | con catalizador | 7 | -1.74 EUR | 14% | 43% |
| catalizador | sin catalizador | 308 | -2.53 EUR | 6% | 49% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.89 | -1.97 | **+0.92 EUR** |
| liquidez | -3.05 | -2.23 | **+0.83 EUR** |
| fuerza relativa | -2.90 | -2.44 | **+0.45 EUR** |
| % compra fuerte | -2.83 | -2.52 | **+0.31 EUR** |
| momentum 30d | -2.70 | -2.73 | **-0.03 EUR** |
| nota global | -2.06 | -2.13 | **-0.07 EUR** |
| dispersion | -2.27 | -2.47 | **-0.20 EUR** |
| RSI | -2.48 | -2.69 | **-0.21 EUR** |
| puesto en el ranking | -2.22 | -2.48 | **-0.26 EUR** |
| volatilidad | -2.08 | -2.40 | **-0.32 EUR** |
| volumen relativo | -1.85 | -3.12 | **-1.27 EUR** |
| distancia max 52s | -1.90 | -3.42 | **-1.52 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
