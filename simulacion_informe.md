# Simulacion en paralelo

Actualizado: 2026-11-25 09:47 · dia 94 de ejecucion
Proxima revision de ponderacion en 11 dias.

- Operaciones cerradas: **400**
- Operaciones abiertas: 53

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 18 | 4% | +8.53 EUR |
| flojo | 169 | 42% | +1.32 EUR |
| plano | 20 | 5% | -1.81 EUR |
| perdida | 103 | 26% | -7.29 EUR |
| nefasta | 86 | 22% | -7.45 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 79 | -2.15% | 5/79 (6%) | 15/79 | 9 |
| 11-20 | 103 | -2.52% | 8/103 (8%) | 17/103 | 9 |
| 21-30 | 218 | -2.55% | 9/218 (4%) | 37/218 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 34 | -1.60% | -0.75% | **-0.86%** | 12/34 (35%) |
| 11-20 | 53 | -1.46% | -0.72% | **-0.74%** | 26/53 (49%) |
| 21-30 | 127 | -1.08% | -0.32% | **-0.76%** | 61/127 (48%) |

**En conjunto:** -1.26% de media frente a -0.49% del indice, una diferencia de **-0.77%**. 99 de 214 operaciones (46%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 59 operaciones, media -0.49%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.82% | 192 | -158.06 EUR | 16/192 | -10.91 EUR |
| trailing pegado (3%) | -1.44% | 154 | -221.53 EUR | 20/154 | -10.00 EUR |
| escalera + stop vol x2.5 | -1.53% | 221 | -339.18 EUR | 14/221 | -10.63 EUR |
| escalera + stop vol x3 | -1.66% | 216 | -358.62 EUR | 14/216 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.46% | 400 | -984.56 EUR | 22/400 | -8.08 EUR |
| arranca antes (+3%) | -2.91% | 126 | -366.89 EUR | 15/126 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.96% | 117 | -346.51 EUR | 15/117 | -10.00 EUR |
| arranca despues (+8%) | -3.14% | 107 | -336.43 EUR | 15/107 | -10.00 EUR |
| trailing suelto (7%) | -3.59% | 106 | -380.63 EUR | 14/106 | -10.00 EUR |
| sin trailing, solo stop | -3.97% | 99 | -392.83 EUR | 12/99 | -10.00 EUR |
| stop corto (5%) | -4.84% | 247 | -1194.39 EUR | 14/247 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.46%**
- Aciertos (>= 5 EUR limpios): 22/400 (6%)
- Resultado acumulado ficticio: -984.56 EUR sobre 400 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 133 | -1.62 EUR | 5% | 35% |
| nota global | medio | 133 | -3.20 EUR | 5% | 54% |
| nota global | alto | 134 | -2.56 EUR | 7% | 53% |
| puesto en el ranking | bajo | 133 | -2.33 EUR | 6% | 50% |
| puesto en el ranking | medio | 133 | -2.80 EUR | 6% | 50% |
| puesto en el ranking | alto | 134 | -2.26 EUR | 4% | 42% |
| potencial hasta objetivo | bajo | 133 | -2.68 EUR | 5% | 47% |
| potencial hasta objetivo | medio | 133 | -2.70 EUR | 4% | 49% |
| potencial hasta objetivo | alto | 134 | -2.01 EUR | 7% | 46% |
| dispersion | bajo | 133 | -2.51 EUR | 6% | 51% |
| dispersion | medio | 133 | -2.69 EUR | 5% | 47% |
| dispersion | alto | 134 | -2.19 EUR | 6% | 44% |
| % compra fuerte | bajo | 125 | -2.75 EUR | 4% | 47% |
| % compra fuerte | medio | 125 | -1.88 EUR | 7% | 45% |
| % compra fuerte | alto | 127 | -2.72 EUR | 5% | 47% |
| momentum 30d | bajo | 133 | -2.25 EUR | 7% | 47% |
| momentum 30d | medio | 133 | -2.31 EUR | 7% | 47% |
| momentum 30d | alto | 134 | -2.81 EUR | 3% | 49% |
| fuerza relativa | bajo | 133 | -2.62 EUR | 6% | 52% |
| fuerza relativa | medio | 133 | -2.51 EUR | 6% | 47% |
| fuerza relativa | alto | 134 | -2.25 EUR | 4% | 43% |
| RSI | bajo | 133 | -2.26 EUR | 7% | 47% |
| RSI | medio | 133 | -2.63 EUR | 7% | 50% |
| RSI | alto | 134 | -2.50 EUR | 3% | 44% |
| volumen relativo | bajo | 127 | -2.08 EUR | 9% | 47% |
| volumen relativo | medio | 127 | -2.35 EUR | 3% | 43% |
| volumen relativo | alto | 129 | -2.87 EUR | 4% | 47% |
| volatilidad | bajo | 127 | -1.93 EUR | 7% | 40% |
| volatilidad | medio | 127 | -2.27 EUR | 6% | 45% |
| volatilidad | alto | 129 | -3.09 EUR | 3% | 53% |
| liquidez | bajo | 127 | -2.58 EUR | 6% | 48% |
| liquidez | medio | 127 | -2.45 EUR | 6% | 46% |
| liquidez | alto | 129 | -2.28 EUR | 5% | 43% |
| distancia max 52s | bajo | 127 | -1.90 EUR | 6% | 43% |
| distancia max 52s | medio | 127 | -2.26 EUR | 6% | 45% |
| distancia max 52s | alto | 129 | -3.13 EUR | 5% | 50% |
| consenso | buy | 283 | -2.48 EUR | 5% | 46% |
| consenso | strong_buy | 117 | -2.42 EUR | 6% | 50% |
| tendencia tecnica | alcista | 195 | -2.81 EUR | 5% | 49% |
| tendencia tecnica | mixta | 114 | -2.68 EUR | 4% | 50% |
| tendencia tecnica | bajista | 91 | -1.45 EUR | 8% | 40% |
| tendencia analistas | mejorando | 183 | -2.42 EUR | 5% | 46% |
| tendencia analistas | estable | 134 | -2.85 EUR | 7% | 52% |
| tendencia analistas | empeorando | 16 | -2.66 EUR | 6% | 56% |
| regimen de mercado | neutro | 182 | -2.05 EUR | 8% | 45% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 103 | -2.18 EUR | 4% | 39% |
| catalizador | con catalizador | 16 | -1.90 EUR | 6% | 38% |
| catalizador | sin catalizador | 384 | -2.48 EUR | 5% | 48% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.68 | -2.01 | **+0.68 EUR** |
| fuerza relativa | -2.62 | -2.25 | **+0.37 EUR** |
| dispersion | -2.51 | -2.19 | **+0.32 EUR** |
| liquidez | -2.58 | -2.28 | **+0.30 EUR** |
| puesto en el ranking | -2.33 | -2.26 | **+0.08 EUR** |
| % compra fuerte | -2.75 | -2.72 | **+0.02 EUR** |
| RSI | -2.26 | -2.50 | **-0.25 EUR** |
| momentum 30d | -2.25 | -2.81 | **-0.56 EUR** |
| volumen relativo | -2.08 | -2.87 | **-0.79 EUR** |
| nota global | -1.62 | -2.56 | **-0.93 EUR** |
| volatilidad | -1.93 | -3.09 | **-1.17 EUR** |
| distancia max 52s | -1.90 | -3.13 | **-1.23 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
