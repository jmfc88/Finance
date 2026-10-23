# Simulacion en paralelo

Actualizado: 2026-10-23 14:15 · dia 61 de ejecucion
**Revision nº4 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **228**
- Operaciones abiertas: 55

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 1% | +16.90 EUR |
| beneficio | 3 | 1% | +7.07 EUR |
| flojo | 77 | 34% | +1.32 EUR |
| plano | 14 | 6% | -1.76 EUR |
| perdida | 79 | 35% | -7.22 EUR |
| nefasta | 52 | 23% | -7.03 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 49 | -2.13% | 3/49 (6%) | 9/49 | 10 |
| 11-20 | 58 | -3.28% | 2/58 (3%) | 5/58 | 9 |
| 21-30 | 121 | -4.07% | 1/121 (1%) | 9/121 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 6 | -0.96% | -1.91% | **+0.95%** | 2/6 (33%) |
| 11-20 | 12 | -3.33% | -0.88% | **-2.44%** | 6/12 (50%) |
| 21-30 | 34 | -3.14% | -1.18% | **-1.96%** | 17/34 (50%) |

**En conjunto:** -2.93% de media frente a -1.19% del indice, una diferencia de **-1.74%**. 25 de 52 operaciones (48%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 37 operaciones, media -2.43%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| trailing pegado (3%) | -2.70% | 76 | -205.02 EUR | 4/76 | -10.00 EUR |
| escalera + stop vol x4 | -2.81% | 44 | -123.65 EUR | 1/44 | -10.34 EUR |
| escalera + stop vol x2.5 | -2.90% | 55 | -159.75 EUR | 1/55 | -7.93 EUR |
| escalera + stop vol x3 | -3.40% | 54 | -183.65 EUR | 1/54 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.45% | 228 | -787.11 EUR | 6/228 | -8.08 EUR |
| arranca antes (+3%) | -3.80% | 67 | -254.31 EUR | 4/67 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.99% | 61 | -243.34 EUR | 4/61 | -10.00 EUR |
| arranca despues (+8%) | -4.02% | 60 | -241.28 EUR | 4/60 | -10.00 EUR |
| trailing suelto (7%) | -4.60% | 58 | -266.59 EUR | 3/58 | -10.00 EUR |
| sin trailing, solo stop | -4.95% | 56 | -277.37 EUR | 2/56 | -10.00 EUR |
| stop corto (5%) | -5.58% | 153 | -853.99 EUR | 4/153 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.45%**
- Aciertos (>= 5 EUR limpios): 6/228 (3%)
- Resultado acumulado ficticio: -787.11 EUR sobre 228 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 76 | -3.49 EUR | 0% | 50% |
| nota global | medio | 76 | -4.13 EUR | 3% | 66% |
| nota global | alto | 76 | -2.74 EUR | 5% | 57% |
| puesto en el ranking | bajo | 76 | -2.37 EUR | 7% | 55% |
| puesto en el ranking | medio | 76 | -4.02 EUR | 1% | 59% |
| puesto en el ranking | alto | 76 | -3.97 EUR | 0% | 58% |
| potencial hasta objetivo | bajo | 76 | -3.59 EUR | 3% | 55% |
| potencial hasta objetivo | medio | 76 | -4.02 EUR | 1% | 63% |
| potencial hasta objetivo | alto | 76 | -2.75 EUR | 4% | 54% |
| dispersion | bajo | 76 | -2.92 EUR | 5% | 57% |
| dispersion | medio | 76 | -4.29 EUR | 1% | 64% |
| dispersion | alto | 76 | -3.15 EUR | 1% | 51% |
| % compra fuerte | bajo | 70 | -3.92 EUR | 1% | 59% |
| % compra fuerte | medio | 70 | -3.07 EUR | 1% | 57% |
| % compra fuerte | alto | 72 | -3.58 EUR | 3% | 56% |
| momentum 30d | bajo | 76 | -3.60 EUR | 4% | 59% |
| momentum 30d | medio | 76 | -3.45 EUR | 0% | 55% |
| momentum 30d | alto | 76 | -3.31 EUR | 4% | 58% |
| fuerza relativa | bajo | 76 | -3.85 EUR | 3% | 62% |
| fuerza relativa | medio | 76 | -3.34 EUR | 1% | 54% |
| fuerza relativa | alto | 76 | -3.16 EUR | 4% | 57% |
| RSI | bajo | 76 | -2.98 EUR | 5% | 54% |
| RSI | medio | 76 | -3.75 EUR | 1% | 59% |
| RSI | alto | 76 | -3.62 EUR | 1% | 59% |
| volumen relativo | bajo | 70 | -3.49 EUR | 4% | 63% |
| volumen relativo | medio | 70 | -3.34 EUR | 0% | 50% |
| volumen relativo | alto | 71 | -3.61 EUR | 3% | 55% |
| volatilidad | bajo | 70 | -3.60 EUR | 0% | 54% |
| volatilidad | medio | 70 | -3.74 EUR | 3% | 57% |
| volatilidad | alto | 71 | -3.11 EUR | 4% | 56% |
| liquidez | bajo | 70 | -3.45 EUR | 1% | 54% |
| liquidez | medio | 70 | -3.25 EUR | 4% | 57% |
| liquidez | alto | 71 | -3.75 EUR | 1% | 56% |
| distancia max 52s | bajo | 70 | -2.94 EUR | 4% | 53% |
| distancia max 52s | medio | 70 | -3.36 EUR | 1% | 57% |
| distancia max 52s | alto | 71 | -4.14 EUR | 1% | 58% |
| consenso | buy | 158 | -3.63 EUR | 2% | 57% |
| consenso | strong_buy | 70 | -3.06 EUR | 4% | 59% |
| tendencia tecnica | alcista | 109 | -3.57 EUR | 3% | 58% |
| tendencia tecnica | mixta | 65 | -3.50 EUR | 2% | 57% |
| tendencia tecnica | bajista | 54 | -3.16 EUR | 4% | 57% |
| tendencia analistas | mejorando | 112 | -3.47 EUR | 3% | 57% |
| tendencia analistas | estable | 70 | -3.90 EUR | 3% | 64% |
| tendencia analistas | empeorando | 9 | -4.67 EUR | 0% | 78% |
| regimen de mercado | neutro | 119 | -3.39 EUR | 2% | 54% |
| regimen de mercado | favorable | 108 | -3.48 EUR | 4% | 61% |
| catalizador | sin catalizador | 227 | -3.43 EUR | 3% | 57% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.59 | -2.75 | **+0.83 EUR** |
| nota global | -3.49 | -2.74 | **+0.75 EUR** |
| fuerza relativa | -3.85 | -3.16 | **+0.68 EUR** |
| volatilidad | -3.60 | -3.11 | **+0.49 EUR** |
| % compra fuerte | -3.92 | -3.58 | **+0.35 EUR** |
| momentum 30d | -3.60 | -3.31 | **+0.29 EUR** |
| volumen relativo | -3.49 | -3.61 | **-0.11 EUR** |
| dispersion | -2.92 | -3.15 | **-0.24 EUR** |
| liquidez | -3.45 | -3.75 | **-0.30 EUR** |
| RSI | -2.98 | -3.62 | **-0.64 EUR** |
| distancia max 52s | -2.94 | -4.14 | **-1.21 EUR** |
| puesto en el ranking | -2.37 | -3.97 | **-1.60 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
