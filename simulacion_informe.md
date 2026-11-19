# Simulacion en paralelo

Actualizado: 2026-11-19 00:22 · dia 88 de ejecucion
Proxima revision de ponderacion en 2 dias.

- Operaciones cerradas: **364**
- Operaciones abiertas: 64

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 17 | 5% | +8.65 EUR |
| flojo | 160 | 44% | +1.29 EUR |
| plano | 18 | 5% | -1.74 EUR |
| perdida | 91 | 25% | -7.22 EUR |
| nefasta | 74 | 20% | -7.34 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 69 | -1.63% | 5/69 (7%) | 14/69 | 10 |
| 11-20 | 94 | -2.18% | 8/94 (9%) | 16/94 | 9 |
| 21-30 | 201 | -2.46% | 8/201 (4%) | 32/201 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 25 | -0.23% | +0.19% | **-0.41%** | 11/25 (44%) |
| 11-20 | 44 | -0.52% | -0.04% | **-0.48%** | 24/44 (55%) |
| 21-30 | 111 | -0.76% | -0.06% | **-0.70%** | 55/111 (50%) |

**En conjunto:** -0.63% de media frente a -0.02% del indice, una diferencia de **-0.61%**. 90 de 180 operaciones (50%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 56 operaciones, media -0.34%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.51% | 168 | -85.81 EUR | 15/168 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.20% | 186 | -222.74 EUR | 13/186 | -10.63 EUR |
| escalera + stop vol x3 | -1.24% | 181 | -224.93 EUR | 13/181 | -12.76 EUR |
| trailing pegado (3%) | -1.38% | 140 | -192.95 EUR | 19/140 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.23% | 364 | -811.95 EUR | 21/364 | -8.08 EUR |
| arranca antes (+3%) | -2.80% | 116 | -324.42 EUR | 15/116 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.84% | 107 | -304.04 EUR | 15/107 | -10.00 EUR |
| arranca despues (+8%) | -3.00% | 98 | -293.91 EUR | 15/98 | -10.00 EUR |
| trailing suelto (7%) | -3.43% | 97 | -332.66 EUR | 14/97 | -10.00 EUR |
| sin trailing, solo stop | -3.81% | 91 | -346.96 EUR | 12/91 | -10.00 EUR |
| stop corto (5%) | -4.71% | 218 | -1026.65 EUR | 14/218 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.23%**
- Aciertos (>= 5 EUR limpios): 21/364 (6%)
- Resultado acumulado ficticio: -811.95 EUR sobre 364 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 121 | -1.52 EUR | 4% | 34% |
| nota global | medio | 121 | -3.17 EUR | 5% | 53% |
| nota global | alto | 122 | -2.01 EUR | 8% | 49% |
| puesto en el ranking | bajo | 121 | -2.11 EUR | 7% | 48% |
| puesto en el ranking | medio | 121 | -2.45 EUR | 7% | 47% |
| puesto en el ranking | alto | 122 | -2.14 EUR | 4% | 41% |
| potencial hasta objetivo | bajo | 121 | -2.50 EUR | 5% | 45% |
| potencial hasta objetivo | medio | 121 | -2.35 EUR | 4% | 45% |
| potencial hasta objetivo | alto | 122 | -1.85 EUR | 8% | 45% |
| dispersion | bajo | 121 | -2.15 EUR | 7% | 48% |
| dispersion | medio | 121 | -2.59 EUR | 5% | 46% |
| dispersion | alto | 122 | -1.95 EUR | 6% | 42% |
| % compra fuerte | bajo | 114 | -2.59 EUR | 4% | 46% |
| % compra fuerte | medio | 114 | -1.83 EUR | 8% | 46% |
| % compra fuerte | alto | 116 | -2.32 EUR | 5% | 43% |
| momentum 30d | bajo | 121 | -2.28 EUR | 7% | 47% |
| momentum 30d | medio | 121 | -1.95 EUR | 7% | 44% |
| momentum 30d | alto | 122 | -2.46 EUR | 3% | 45% |
| fuerza relativa | bajo | 121 | -2.55 EUR | 7% | 52% |
| fuerza relativa | medio | 121 | -2.09 EUR | 6% | 42% |
| fuerza relativa | alto | 122 | -2.06 EUR | 5% | 42% |
| RSI | bajo | 121 | -2.45 EUR | 7% | 50% |
| RSI | medio | 121 | -2.26 EUR | 7% | 47% |
| RSI | alto | 122 | -1.98 EUR | 3% | 39% |
| volumen relativo | bajo | 115 | -1.73 EUR | 10% | 45% |
| volumen relativo | medio | 115 | -2.22 EUR | 3% | 41% |
| volumen relativo | alto | 117 | -2.61 EUR | 4% | 45% |
| volatilidad | bajo | 115 | -1.90 EUR | 7% | 40% |
| volatilidad | medio | 115 | -2.18 EUR | 7% | 44% |
| volatilidad | alto | 117 | -2.48 EUR | 3% | 47% |
| liquidez | bajo | 115 | -2.44 EUR | 5% | 47% |
| liquidez | medio | 115 | -2.22 EUR | 6% | 44% |
| liquidez | alto | 117 | -1.92 EUR | 6% | 40% |
| distancia max 52s | bajo | 115 | -1.68 EUR | 7% | 41% |
| distancia max 52s | medio | 115 | -2.01 EUR | 6% | 43% |
| distancia max 52s | alto | 117 | -2.87 EUR | 4% | 47% |
| consenso | buy | 255 | -2.17 EUR | 6% | 44% |
| consenso | strong_buy | 109 | -2.36 EUR | 6% | 50% |
| tendencia tecnica | alcista | 173 | -2.52 EUR | 5% | 47% |
| tendencia tecnica | mixta | 105 | -2.41 EUR | 5% | 48% |
| tendencia tecnica | bajista | 86 | -1.44 EUR | 8% | 40% |
| tendencia analistas | mejorando | 167 | -2.16 EUR | 5% | 44% |
| tendencia analistas | estable | 121 | -2.58 EUR | 7% | 50% |
| tendencia analistas | empeorando | 15 | -3.07 EUR | 7% | 60% |
| regimen de mercado | neutro | 177 | -1.95 EUR | 8% | 44% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 72 | -1.11 EUR | 4% | 28% |
| catalizador | con catalizador | 13 | -0.47 EUR | 8% | 23% |
| catalizador | sin catalizador | 351 | -2.30 EUR | 6% | 46% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.50 | -1.85 | **+0.65 EUR** |
| liquidez | -2.44 | -1.92 | **+0.52 EUR** |
| fuerza relativa | -2.55 | -2.06 | **+0.49 EUR** |
| RSI | -2.45 | -1.98 | **+0.47 EUR** |
| % compra fuerte | -2.59 | -2.32 | **+0.28 EUR** |
| dispersion | -2.15 | -1.95 | **+0.20 EUR** |
| puesto en el ranking | -2.11 | -2.14 | **-0.03 EUR** |
| momentum 30d | -2.28 | -2.46 | **-0.19 EUR** |
| nota global | -1.52 | -2.01 | **-0.49 EUR** |
| volatilidad | -1.90 | -2.48 | **-0.59 EUR** |
| volumen relativo | -1.73 | -2.61 | **-0.88 EUR** |
| distancia max 52s | -1.68 | -2.87 | **-1.19 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
