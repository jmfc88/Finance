# Simulacion en paralelo

Actualizado: 2026-11-10 23:19 · dia 79 de ejecucion
Proxima revision de ponderacion en 11 dias.

- Operaciones cerradas: **319**
- Operaciones abiertas: 64

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 14 | 4% | +8.78 EUR |
| flojo | 129 | 40% | +1.31 EUR |
| plano | 18 | 6% | -1.74 EUR |
| perdida | 88 | 28% | -7.19 EUR |
| nefasta | 66 | 21% | -7.25 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 62 | -1.78% | 5/62 (8%) | 13/62 | 10 |
| 11-20 | 79 | -2.53% | 6/79 (8%) | 11/79 | 9 |
| 21-30 | 178 | -2.67% | 7/178 (4%) | 25/178 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 18 | -0.20% | -0.33% | **+0.13%** | 10/18 (56%) |
| 11-20 | 30 | -0.85% | -0.62% | **-0.23%** | 19/30 (63%) |
| 21-30 | 88 | -0.73% | -0.28% | **-0.45%** | 49/88 (56%) |

**En conjunto:** -0.69% de media frente a -0.36% del indice, una diferencia de **-0.32%**. 78 de 136 operaciones (57%) batieron a su indice.

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
| escalera + stop vol x4 | -0.83% | 130 | -107.53 EUR | 13/130 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.48% | 146 | -216.56 EUR | 11/146 | -10.63 EUR |
| escalera + stop vol x3 | -1.60% | 142 | -226.69 EUR | 11/142 | -12.76 EUR |
| trailing pegado (3%) | -1.62% | 125 | -202.10 EUR | 16/125 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.46% | 319 | -784.50 EUR | 18/319 | -8.08 EUR |
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

- Media neta: **-2.46%**
- Aciertos (>= 5 EUR limpios): 18/319 (6%)
- Resultado acumulado ficticio: -784.50 EUR sobre 319 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 106 | -1.84 EUR | 5% | 38% |
| nota global | medio | 106 | -3.30 EUR | 4% | 55% |
| nota global | alto | 107 | -2.25 EUR | 8% | 52% |
| puesto en el ranking | bajo | 106 | -2.19 EUR | 8% | 51% |
| puesto en el ranking | medio | 106 | -2.80 EUR | 6% | 50% |
| puesto en el ranking | alto | 107 | -2.39 EUR | 4% | 44% |
| potencial hasta objetivo | bajo | 106 | -2.86 EUR | 5% | 49% |
| potencial hasta objetivo | medio | 106 | -2.69 EUR | 4% | 50% |
| potencial hasta objetivo | alto | 107 | -1.84 EUR | 8% | 46% |
| dispersion | bajo | 106 | -2.32 EUR | 8% | 51% |
| dispersion | medio | 106 | -2.68 EUR | 5% | 48% |
| dispersion | alto | 107 | -2.38 EUR | 5% | 46% |
| % compra fuerte | bajo | 100 | -2.93 EUR | 3% | 49% |
| % compra fuerte | medio | 100 | -1.99 EUR | 9% | 49% |
| % compra fuerte | alto | 100 | -2.49 EUR | 4% | 45% |
| momentum 30d | bajo | 106 | -2.66 EUR | 6% | 50% |
| momentum 30d | medio | 106 | -2.06 EUR | 7% | 45% |
| momentum 30d | alto | 107 | -2.66 EUR | 5% | 50% |
| fuerza relativa | bajo | 106 | -2.86 EUR | 5% | 53% |
| fuerza relativa | medio | 106 | -2.14 EUR | 7% | 45% |
| fuerza relativa | alto | 107 | -2.38 EUR | 6% | 47% |
| RSI | bajo | 106 | -2.53 EUR | 7% | 50% |
| RSI | medio | 106 | -2.22 EUR | 7% | 48% |
| RSI | alto | 107 | -2.62 EUR | 4% | 47% |
| volumen relativo | bajo | 100 | -1.80 EUR | 10% | 46% |
| volumen relativo | medio | 100 | -2.43 EUR | 3% | 44% |
| volumen relativo | alto | 102 | -3.04 EUR | 4% | 50% |
| volatilidad | bajo | 100 | -2.02 EUR | 7% | 42% |
| volatilidad | medio | 100 | -2.75 EUR | 5% | 49% |
| volatilidad | alto | 102 | -2.50 EUR | 5% | 49% |
| liquidez | bajo | 100 | -3.01 EUR | 4% | 51% |
| liquidez | medio | 100 | -2.13 EUR | 7% | 46% |
| liquidez | alto | 102 | -2.14 EUR | 6% | 43% |
| distancia max 52s | bajo | 100 | -1.87 EUR | 6% | 42% |
| distancia max 52s | medio | 100 | -2.07 EUR | 7% | 46% |
| distancia max 52s | alto | 102 | -3.31 EUR | 4% | 52% |
| consenso | buy | 227 | -2.46 EUR | 5% | 47% |
| consenso | strong_buy | 92 | -2.45 EUR | 7% | 52% |
| tendencia tecnica | alcista | 148 | -2.79 EUR | 5% | 50% |
| tendencia tecnica | mixta | 91 | -2.56 EUR | 5% | 51% |
| tendencia tecnica | bajista | 80 | -1.72 EUR | 8% | 42% |
| tendencia analistas | mejorando | 145 | -2.44 EUR | 4% | 47% |
| tendencia analistas | estable | 110 | -2.72 EUR | 8% | 53% |
| tendencia analistas | empeorando | 13 | -3.00 EUR | 8% | 62% |
| regimen de mercado | neutro | 162 | -1.99 EUR | 7% | 44% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 42 | -1.80 EUR | 5% | 36% |
| catalizador | con catalizador | 9 | -1.13 EUR | 11% | 33% |
| catalizador | sin catalizador | 310 | -2.50 EUR | 5% | 49% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.86 | -1.84 | **+1.02 EUR** |
| liquidez | -3.01 | -2.14 | **+0.87 EUR** |
| fuerza relativa | -2.86 | -2.38 | **+0.48 EUR** |
| % compra fuerte | -2.93 | -2.49 | **+0.44 EUR** |
| momentum 30d | -2.66 | -2.66 | **+0.01 EUR** |
| dispersion | -2.32 | -2.38 | **-0.05 EUR** |
| RSI | -2.53 | -2.62 | **-0.09 EUR** |
| puesto en el ranking | -2.19 | -2.39 | **-0.20 EUR** |
| nota global | -1.84 | -2.25 | **-0.41 EUR** |
| volatilidad | -2.02 | -2.50 | **-0.47 EUR** |
| volumen relativo | -1.80 | -3.04 | **-1.24 EUR** |
| distancia max 52s | -1.87 | -3.31 | **-1.44 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
