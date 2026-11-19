# Simulacion en paralelo

Actualizado: 2026-11-19 08:43 · dia 88 de ejecucion
Proxima revision de ponderacion en 2 dias.

- Operaciones cerradas: **366**
- Operaciones abiertas: 62

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 18 | 5% | +8.53 EUR |
| flojo | 161 | 44% | +1.29 EUR |
| plano | 18 | 5% | -1.74 EUR |
| perdida | 91 | 25% | -7.22 EUR |
| nefasta | 74 | 20% | -7.34 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 69 | -1.63% | 5/69 (7%) | 14/69 | 10 |
| 11-20 | 95 | -2.15% | 8/95 (8%) | 16/95 | 9 |
| 21-30 | 202 | -2.41% | 9/202 (4%) | 33/202 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 25 | -0.23% | +0.19% | **-0.41%** | 11/25 (44%) |
| 11-20 | 45 | -0.49% | -0.03% | **-0.46%** | 25/45 (56%) |
| 21-30 | 112 | -0.69% | -0.05% | **-0.64%** | 56/112 (50%) |

**En conjunto:** -0.58% de media frente a -0.01% del indice, una diferencia de **-0.56%**. 92 de 182 operaciones (51%) batieron a su indice.

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
| escalera + stop vol x4 | -0.46% | 170 | -78.24 EUR | 16/170 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.14% | 188 | -215.17 EUR | 14/188 | -10.63 EUR |
| escalera + stop vol x3 | -1.19% | 183 | -217.36 EUR | 14/183 | -12.76 EUR |
| trailing pegado (3%) | -1.34% | 142 | -189.81 EUR | 19/142 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.20% | 366 | -804.38 EUR | 22/366 | -8.08 EUR |
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

- Media neta: **-2.20%**
- Aciertos (>= 5 EUR limpios): 22/366 (6%)
- Resultado acumulado ficticio: -804.38 EUR sobre 366 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 122 | -1.45 EUR | 5% | 34% |
| nota global | medio | 122 | -3.14 EUR | 5% | 52% |
| nota global | alto | 122 | -2.01 EUR | 8% | 49% |
| puesto en el ranking | bajo | 122 | -2.08 EUR | 7% | 48% |
| puesto en el ranking | medio | 122 | -2.42 EUR | 7% | 47% |
| puesto en el ranking | alto | 122 | -2.09 EUR | 5% | 41% |
| potencial hasta objetivo | bajo | 122 | -2.42 EUR | 6% | 45% |
| potencial hasta objetivo | medio | 122 | -2.32 EUR | 4% | 45% |
| potencial hasta objetivo | alto | 122 | -1.85 EUR | 8% | 45% |
| dispersion | bajo | 122 | -2.08 EUR | 7% | 48% |
| dispersion | medio | 122 | -2.74 EUR | 4% | 48% |
| dispersion | alto | 122 | -1.78 EUR | 7% | 40% |
| % compra fuerte | bajo | 115 | -2.51 EUR | 4% | 45% |
| % compra fuerte | medio | 115 | -1.81 EUR | 8% | 45% |
| % compra fuerte | alto | 116 | -2.32 EUR | 5% | 43% |
| momentum 30d | bajo | 122 | -2.25 EUR | 7% | 47% |
| momentum 30d | medio | 122 | -1.95 EUR | 7% | 44% |
| momentum 30d | alto | 122 | -2.39 EUR | 3% | 44% |
| fuerza relativa | bajo | 122 | -2.52 EUR | 7% | 52% |
| fuerza relativa | medio | 122 | -2.02 EUR | 7% | 42% |
| fuerza relativa | alto | 122 | -2.06 EUR | 5% | 42% |
| RSI | bajo | 122 | -2.42 EUR | 7% | 49% |
| RSI | medio | 122 | -2.39 EUR | 7% | 48% |
| RSI | alto | 122 | -1.78 EUR | 4% | 38% |
| volumen relativo | bajo | 116 | -1.66 EUR | 10% | 45% |
| volumen relativo | medio | 116 | -2.19 EUR | 3% | 41% |
| volumen relativo | alto | 117 | -2.61 EUR | 4% | 45% |
| volatilidad | bajo | 116 | -1.82 EUR | 8% | 40% |
| volatilidad | medio | 116 | -2.16 EUR | 7% | 44% |
| volatilidad | alto | 117 | -2.48 EUR | 3% | 47% |
| liquidez | bajo | 116 | -2.36 EUR | 6% | 47% |
| liquidez | medio | 116 | -2.19 EUR | 6% | 44% |
| liquidez | alto | 117 | -1.92 EUR | 6% | 40% |
| distancia max 52s | bajo | 116 | -1.65 EUR | 7% | 41% |
| distancia max 52s | medio | 116 | -2.01 EUR | 6% | 43% |
| distancia max 52s | alto | 117 | -2.79 EUR | 5% | 47% |
| consenso | buy | 256 | -2.16 EUR | 6% | 43% |
| consenso | strong_buy | 110 | -2.28 EUR | 6% | 49% |
| tendencia tecnica | alcista | 175 | -2.44 EUR | 6% | 46% |
| tendencia tecnica | mixta | 105 | -2.41 EUR | 5% | 48% |
| tendencia tecnica | bajista | 86 | -1.44 EUR | 8% | 40% |
| tendencia analistas | mejorando | 168 | -2.14 EUR | 5% | 44% |
| tendencia analistas | estable | 121 | -2.58 EUR | 7% | 50% |
| tendencia analistas | empeorando | 15 | -3.07 EUR | 7% | 60% |
| regimen de mercado | neutro | 177 | -1.95 EUR | 8% | 44% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 74 | -0.98 EUR | 5% | 27% |
| catalizador | con catalizador | 13 | -0.47 EUR | 8% | 23% |
| catalizador | sin catalizador | 353 | -2.26 EUR | 6% | 46% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| RSI | -2.42 | -1.78 | **+0.64 EUR** |
| potencial hasta objetivo | -2.42 | -1.85 | **+0.57 EUR** |
| fuerza relativa | -2.52 | -2.06 | **+0.46 EUR** |
| liquidez | -2.36 | -1.92 | **+0.44 EUR** |
| dispersion | -2.08 | -1.78 | **+0.30 EUR** |
| % compra fuerte | -2.51 | -2.32 | **+0.20 EUR** |
| puesto en el ranking | -2.08 | -2.09 | **-0.01 EUR** |
| momentum 30d | -2.25 | -2.39 | **-0.14 EUR** |
| nota global | -1.45 | -2.01 | **-0.55 EUR** |
| volatilidad | -1.82 | -2.48 | **-0.66 EUR** |
| volumen relativo | -1.66 | -2.61 | **-0.95 EUR** |
| distancia max 52s | -1.65 | -2.79 | **-1.14 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
