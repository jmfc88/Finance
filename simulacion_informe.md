# Simulacion en paralelo

Actualizado: 2026-11-27 01:44 · dia 96 de ejecucion
Proxima revision de ponderacion en 9 dias.

- Operaciones cerradas: **404**
- Operaciones abiertas: 59

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 18 | 4% | +8.53 EUR |
| flojo | 170 | 42% | +1.33 EUR |
| plano | 20 | 5% | -1.81 EUR |
| perdida | 105 | 26% | -7.31 EUR |
| nefasta | 87 | 22% | -7.45 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 81 | -2.15% | 5/81 (6%) | 16/81 | 9 |
| 11-20 | 103 | -2.52% | 8/103 (8%) | 17/103 | 9 |
| 21-30 | 220 | -2.60% | 9/220 (4%) | 37/220 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 36 | -1.64% | -0.82% | **-0.82%** | 13/36 (36%) |
| 11-20 | 53 | -1.46% | -0.72% | **-0.74%** | 26/53 (49%) |
| 21-30 | 129 | -1.19% | -0.37% | **-0.82%** | 61/129 (47%) |

**En conjunto:** -1.33% de media frente a -0.53% del indice, una diferencia de **-0.80%**. 100 de 218 operaciones (46%) batieron a su indice.

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
| escalera + stop vol x4 | -0.87% | 195 | -169.00 EUR | 16/195 | -10.91 EUR |
| trailing pegado (3%) | -1.44% | 154 | -221.53 EUR | 20/154 | -10.00 EUR |
| escalera + stop vol x2.5 | -1.59% | 225 | -358.09 EUR | 14/225 | -10.63 EUR |
| escalera + stop vol x3 | -1.73% | 220 | -380.51 EUR | 14/220 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.49% | 404 | -1005.27 EUR | 22/404 | -8.08 EUR |
| arranca antes (+3%) | -2.91% | 126 | -366.89 EUR | 15/126 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.96% | 117 | -346.51 EUR | 15/117 | -10.00 EUR |
| arranca despues (+8%) | -3.14% | 107 | -336.43 EUR | 15/107 | -10.00 EUR |
| trailing suelto (7%) | -3.59% | 106 | -380.63 EUR | 14/106 | -10.00 EUR |
| sin trailing, solo stop | -3.97% | 99 | -392.83 EUR | 12/99 | -10.00 EUR |
| stop corto (5%) | -4.86% | 250 | -1215.39 EUR | 14/250 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.49%**
- Aciertos (>= 5 EUR limpios): 22/404 (5%)
- Resultado acumulado ficticio: -1005.27 EUR sobre 404 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 134 | -1.74 EUR | 4% | 36% |
| nota global | medio | 134 | -3.36 EUR | 4% | 54% |
| nota global | alto | 136 | -2.37 EUR | 7% | 52% |
| puesto en el ranking | bajo | 134 | -2.33 EUR | 6% | 50% |
| puesto en el ranking | medio | 134 | -2.86 EUR | 6% | 51% |
| puesto en el ranking | alto | 136 | -2.27 EUR | 4% | 42% |
| potencial hasta objetivo | bajo | 134 | -2.71 EUR | 5% | 47% |
| potencial hasta objetivo | medio | 134 | -2.75 EUR | 4% | 49% |
| potencial hasta objetivo | alto | 136 | -2.01 EUR | 7% | 46% |
| dispersion | bajo | 134 | -2.46 EUR | 6% | 51% |
| dispersion | medio | 134 | -2.80 EUR | 4% | 48% |
| dispersion | alto | 136 | -2.21 EUR | 6% | 44% |
| % compra fuerte | bajo | 127 | -2.76 EUR | 4% | 47% |
| % compra fuerte | medio | 127 | -1.98 EUR | 7% | 46% |
| % compra fuerte | alto | 127 | -2.70 EUR | 5% | 47% |
| momentum 30d | bajo | 134 | -2.21 EUR | 7% | 46% |
| momentum 30d | medio | 134 | -2.44 EUR | 7% | 48% |
| momentum 30d | alto | 136 | -2.81 EUR | 3% | 49% |
| fuerza relativa | bajo | 134 | -2.66 EUR | 6% | 52% |
| fuerza relativa | medio | 134 | -2.56 EUR | 6% | 47% |
| fuerza relativa | alto | 136 | -2.25 EUR | 4% | 43% |
| RSI | bajo | 134 | -2.21 EUR | 7% | 47% |
| RSI | medio | 134 | -2.69 EUR | 7% | 51% |
| RSI | alto | 136 | -2.57 EUR | 3% | 45% |
| volumen relativo | bajo | 129 | -2.17 EUR | 9% | 48% |
| volumen relativo | medio | 129 | -2.35 EUR | 3% | 43% |
| volumen relativo | alto | 129 | -2.87 EUR | 4% | 47% |
| volatilidad | bajo | 129 | -1.84 EUR | 7% | 40% |
| volatilidad | medio | 129 | -2.42 EUR | 6% | 47% |
| volatilidad | alto | 129 | -3.13 EUR | 3% | 53% |
| liquidez | bajo | 129 | -2.62 EUR | 5% | 49% |
| liquidez | medio | 129 | -2.34 EUR | 5% | 46% |
| liquidez | alto | 129 | -2.42 EUR | 5% | 44% |
| distancia max 52s | bajo | 129 | -1.93 EUR | 6% | 43% |
| distancia max 52s | medio | 129 | -2.42 EUR | 5% | 47% |
| distancia max 52s | alto | 129 | -3.04 EUR | 5% | 50% |
| consenso | buy | 287 | -2.51 EUR | 5% | 46% |
| consenso | strong_buy | 117 | -2.42 EUR | 6% | 50% |
| tendencia tecnica | alcista | 198 | -2.83 EUR | 5% | 49% |
| tendencia tecnica | mixta | 115 | -2.72 EUR | 4% | 50% |
| tendencia tecnica | bajista | 91 | -1.45 EUR | 8% | 40% |
| tendencia analistas | mejorando | 185 | -2.42 EUR | 5% | 46% |
| tendencia analistas | estable | 136 | -2.93 EUR | 7% | 53% |
| tendencia analistas | empeorando | 16 | -2.66 EUR | 6% | 56% |
| regimen de mercado | neutro | 182 | -2.05 EUR | 8% | 45% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 107 | -2.29 EUR | 4% | 40% |
| catalizador | con catalizador | 16 | -1.90 EUR | 6% | 38% |
| catalizador | sin catalizador | 388 | -2.51 EUR | 5% | 48% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.71 | -2.01 | **+0.69 EUR** |
| fuerza relativa | -2.66 | -2.25 | **+0.41 EUR** |
| dispersion | -2.46 | -2.21 | **+0.25 EUR** |
| liquidez | -2.62 | -2.42 | **+0.20 EUR** |
| puesto en el ranking | -2.33 | -2.27 | **+0.06 EUR** |
| % compra fuerte | -2.76 | -2.70 | **+0.05 EUR** |
| RSI | -2.21 | -2.57 | **-0.35 EUR** |
| momentum 30d | -2.21 | -2.81 | **-0.60 EUR** |
| nota global | -1.74 | -2.37 | **-0.63 EUR** |
| volumen relativo | -2.17 | -2.87 | **-0.69 EUR** |
| distancia max 52s | -1.93 | -3.04 | **-1.11 EUR** |
| volatilidad | -1.84 | -3.13 | **-1.30 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
