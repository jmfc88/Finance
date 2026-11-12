# Simulacion en paralelo

Actualizado: 2026-11-12 08:16 · dia 81 de ejecucion
Proxima revision de ponderacion en 9 dias.

- Operaciones cerradas: **327**
- Operaciones abiertas: 68

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 14 | 4% | +8.78 EUR |
| flojo | 137 | 42% | +1.31 EUR |
| plano | 18 | 6% | -1.74 EUR |
| perdida | 88 | 27% | -7.19 EUR |
| nefasta | 66 | 20% | -7.25 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 62 | -1.78% | 5/62 (8%) | 13/62 | 10 |
| 11-20 | 81 | -2.44% | 6/81 (7%) | 12/81 | 9 |
| 21-30 | 184 | -2.53% | 7/184 (4%) | 28/184 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 18 | -0.20% | -0.33% | **+0.13%** | 10/18 (56%) |
| 11-20 | 32 | -0.73% | -0.37% | **-0.36%** | 19/32 (59%) |
| 21-30 | 94 | -0.59% | -0.14% | **-0.45%** | 50/94 (53%) |

**En conjunto:** -0.57% de media frente a -0.21% del indice, una diferencia de **-0.36%**. 79 de 144 operaciones (55%) batieron a su indice.

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
| escalera + stop vol x4 | -0.70% | 138 | -96.99 EUR | 13/138 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.37% | 154 | -211.06 EUR | 11/154 | -10.63 EUR |
| escalera + stop vol x3 | -1.48% | 150 | -221.63 EUR | 11/150 | -12.76 EUR |
| trailing pegado (3%) | -1.57% | 127 | -199.57 EUR | 16/127 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.37% | 327 | -773.96 EUR | 18/327 | -8.08 EUR |
| arranca antes (+3%) | -2.89% | 108 | -312.13 EUR | 12/108 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.00% | 100 | -300.40 EUR | 12/100 | -10.00 EUR |
| arranca despues (+8%) | -3.19% | 91 | -290.27 EUR | 12/91 | -10.00 EUR |
| trailing suelto (7%) | -3.66% | 90 | -329.02 EUR | 11/90 | -10.00 EUR |
| sin trailing, solo stop | -4.09% | 84 | -343.32 EUR | 9/84 | -10.00 EUR |
| stop corto (5%) | -4.74% | 203 | -962.15 EUR | 12/203 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.37%**
- Aciertos (>= 5 EUR limpios): 18/327 (6%)
- Resultado acumulado ficticio: -773.96 EUR sobre 327 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 109 | -1.57 EUR | 5% | 35% |
| nota global | medio | 109 | -3.49 EUR | 3% | 55% |
| nota global | alto | 109 | -2.04 EUR | 9% | 51% |
| puesto en el ranking | bajo | 109 | -2.21 EUR | 7% | 50% |
| puesto en el ranking | medio | 109 | -2.71 EUR | 6% | 50% |
| puesto en el ranking | alto | 109 | -2.18 EUR | 4% | 41% |
| potencial hasta objetivo | bajo | 109 | -2.75 EUR | 5% | 48% |
| potencial hasta objetivo | medio | 109 | -2.51 EUR | 5% | 49% |
| potencial hasta objetivo | alto | 109 | -1.84 EUR | 7% | 45% |
| dispersion | bajo | 109 | -2.23 EUR | 7% | 50% |
| dispersion | medio | 109 | -2.55 EUR | 5% | 47% |
| dispersion | alto | 109 | -2.31 EUR | 5% | 45% |
| % compra fuerte | bajo | 102 | -2.77 EUR | 3% | 47% |
| % compra fuerte | medio | 102 | -2.02 EUR | 9% | 49% |
| % compra fuerte | alto | 103 | -2.39 EUR | 4% | 44% |
| momentum 30d | bajo | 109 | -2.41 EUR | 7% | 49% |
| momentum 30d | medio | 109 | -2.02 EUR | 5% | 43% |
| momentum 30d | alto | 109 | -2.67 EUR | 5% | 50% |
| fuerza relativa | bajo | 109 | -2.71 EUR | 6% | 52% |
| fuerza relativa | medio | 109 | -2.07 EUR | 6% | 43% |
| fuerza relativa | alto | 109 | -2.32 EUR | 6% | 46% |
| RSI | bajo | 109 | -2.41 EUR | 6% | 49% |
| RSI | medio | 109 | -2.18 EUR | 7% | 48% |
| RSI | alto | 109 | -2.51 EUR | 3% | 45% |
| volumen relativo | bajo | 103 | -1.71 EUR | 10% | 45% |
| volumen relativo | medio | 103 | -2.39 EUR | 3% | 44% |
| volumen relativo | alto | 104 | -2.88 EUR | 4% | 48% |
| volatilidad | bajo | 103 | -1.96 EUR | 7% | 41% |
| volatilidad | medio | 103 | -2.62 EUR | 5% | 48% |
| volatilidad | alto | 104 | -2.40 EUR | 5% | 48% |
| liquidez | bajo | 103 | -2.87 EUR | 4% | 50% |
| liquidez | medio | 103 | -1.95 EUR | 7% | 44% |
| liquidez | alto | 104 | -2.16 EUR | 6% | 43% |
| distancia max 52s | bajo | 103 | -1.76 EUR | 6% | 41% |
| distancia max 52s | medio | 103 | -1.98 EUR | 7% | 45% |
| distancia max 52s | alto | 104 | -3.23 EUR | 4% | 51% |
| consenso | buy | 231 | -2.40 EUR | 5% | 46% |
| consenso | strong_buy | 96 | -2.28 EUR | 6% | 50% |
| tendencia tecnica | alcista | 149 | -2.77 EUR | 5% | 50% |
| tendencia tecnica | mixta | 95 | -2.41 EUR | 5% | 48% |
| tendencia tecnica | bajista | 83 | -1.59 EUR | 7% | 41% |
| tendencia analistas | mejorando | 147 | -2.37 EUR | 4% | 46% |
| tendencia analistas | estable | 112 | -2.65 EUR | 8% | 52% |
| tendencia analistas | empeorando | 13 | -3.00 EUR | 8% | 62% |
| regimen de mercado | neutro | 164 | -1.94 EUR | 7% | 43% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 48 | -1.45 EUR | 4% | 31% |
| catalizador | con catalizador | 9 | -1.13 EUR | 11% | 33% |
| catalizador | sin catalizador | 318 | -2.40 EUR | 5% | 47% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.75 | -1.84 | **+0.91 EUR** |
| liquidez | -2.87 | -2.16 | **+0.71 EUR** |
| fuerza relativa | -2.71 | -2.32 | **+0.39 EUR** |
| % compra fuerte | -2.77 | -2.39 | **+0.38 EUR** |
| puesto en el ranking | -2.21 | -2.18 | **+0.03 EUR** |
| dispersion | -2.23 | -2.31 | **-0.08 EUR** |
| RSI | -2.41 | -2.51 | **-0.10 EUR** |
| momentum 30d | -2.41 | -2.67 | **-0.26 EUR** |
| volatilidad | -1.96 | -2.40 | **-0.44 EUR** |
| nota global | -1.57 | -2.04 | **-0.47 EUR** |
| volumen relativo | -1.71 | -2.88 | **-1.16 EUR** |
| distancia max 52s | -1.76 | -3.23 | **-1.46 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
