# Simulacion en paralelo

Actualizado: 2026-11-20 17:48 · dia 89 de ejecucion
Proxima revision de ponderacion en 1 dia.

- Operaciones cerradas: **393**
- Operaciones abiertas: 51

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 18 | 5% | +8.53 EUR |
| flojo | 167 | 42% | +1.32 EUR |
| plano | 19 | 5% | -1.76 EUR |
| perdida | 101 | 26% | -7.31 EUR |
| nefasta | 84 | 21% | -7.43 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 76 | -2.07% | 5/76 (7%) | 15/76 | 9 |
| 11-20 | 103 | -2.52% | 8/103 (8%) | 17/103 | 9 |
| 21-30 | 214 | -2.51% | 9/214 (4%) | 37/214 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 32 | -1.58% | -0.76% | **-0.82%** | 12/32 (38%) |
| 11-20 | 53 | -1.46% | -0.72% | **-0.74%** | 26/53 (49%) |
| 21-30 | 124 | -1.03% | -0.29% | **-0.74%** | 60/124 (48%) |

**En conjunto:** -1.22% de media frente a -0.47% del indice, una diferencia de **-0.75%**. 98 de 209 operaciones (47%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 57 operaciones, media -0.38%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.72% | 186 | -133.65 EUR | 16/186 | -10.91 EUR |
| trailing pegado (3%) | -1.29% | 150 | -193.86 EUR | 20/150 | -10.00 EUR |
| escalera + stop vol x2.5 | -1.48% | 214 | -316.03 EUR | 14/214 | -10.63 EUR |
| escalera + stop vol x3 | -1.59% | 209 | -331.98 EUR | 14/209 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.43% | 393 | -954.65 EUR | 22/393 | -8.08 EUR |
| arranca antes (+3%) | -2.78% | 122 | -339.22 EUR | 15/122 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.82% | 113 | -318.84 EUR | 15/113 | -10.00 EUR |
| arranca despues (+8%) | -3.00% | 103 | -308.76 EUR | 15/103 | -10.00 EUR |
| trailing suelto (7%) | -3.46% | 102 | -352.96 EUR | 14/102 | -10.00 EUR |
| sin trailing, solo stop | -3.84% | 95 | -365.16 EUR | 12/95 | -10.00 EUR |
| stop corto (5%) | -4.80% | 242 | -1161.45 EUR | 14/242 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.43%**
- Aciertos (>= 5 EUR limpios): 22/393 (6%)
- Resultado acumulado ficticio: -954.65 EUR sobre 393 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 131 | -1.64 EUR | 5% | 35% |
| nota global | medio | 131 | -3.13 EUR | 5% | 53% |
| nota global | alto | 131 | -2.52 EUR | 7% | 53% |
| puesto en el ranking | bajo | 131 | -2.34 EUR | 6% | 50% |
| puesto en el ranking | medio | 131 | -2.79 EUR | 6% | 50% |
| puesto en el ranking | alto | 131 | -2.16 EUR | 5% | 41% |
| potencial hasta objetivo | bajo | 131 | -2.64 EUR | 5% | 47% |
| potencial hasta objetivo | medio | 131 | -2.68 EUR | 4% | 49% |
| potencial hasta objetivo | alto | 131 | -1.96 EUR | 8% | 46% |
| dispersion | bajo | 131 | -2.36 EUR | 6% | 50% |
| dispersion | medio | 131 | -2.73 EUR | 5% | 47% |
| dispersion | alto | 131 | -2.19 EUR | 6% | 44% |
| % compra fuerte | bajo | 123 | -2.66 EUR | 4% | 46% |
| % compra fuerte | medio | 123 | -1.90 EUR | 7% | 46% |
| % compra fuerte | alto | 125 | -2.71 EUR | 5% | 47% |
| momentum 30d | bajo | 131 | -2.30 EUR | 7% | 47% |
| momentum 30d | medio | 131 | -2.20 EUR | 7% | 46% |
| momentum 30d | alto | 131 | -2.79 EUR | 3% | 48% |
| fuerza relativa | bajo | 131 | -2.69 EUR | 6% | 53% |
| fuerza relativa | medio | 131 | -2.34 EUR | 6% | 45% |
| fuerza relativa | alto | 131 | -2.25 EUR | 5% | 44% |
| RSI | bajo | 131 | -2.25 EUR | 7% | 47% |
| RSI | medio | 131 | -2.57 EUR | 7% | 50% |
| RSI | alto | 131 | -2.47 EUR | 3% | 44% |
| volumen relativo | bajo | 125 | -2.05 EUR | 10% | 47% |
| volumen relativo | medio | 125 | -2.29 EUR | 3% | 42% |
| volumen relativo | alto | 126 | -2.86 EUR | 4% | 48% |
| volatilidad | bajo | 125 | -1.90 EUR | 7% | 40% |
| volatilidad | medio | 125 | -2.21 EUR | 6% | 45% |
| volatilidad | alto | 126 | -3.09 EUR | 3% | 52% |
| liquidez | bajo | 125 | -2.65 EUR | 6% | 49% |
| liquidez | medio | 125 | -2.26 EUR | 6% | 46% |
| liquidez | alto | 126 | -2.29 EUR | 6% | 43% |
| distancia max 52s | bajo | 125 | -1.88 EUR | 6% | 42% |
| distancia max 52s | medio | 125 | -2.24 EUR | 6% | 45% |
| distancia max 52s | alto | 126 | -3.08 EUR | 5% | 50% |
| consenso | buy | 277 | -2.44 EUR | 5% | 46% |
| consenso | strong_buy | 116 | -2.40 EUR | 6% | 50% |
| tendencia tecnica | alcista | 190 | -2.76 EUR | 5% | 49% |
| tendencia tecnica | mixta | 114 | -2.68 EUR | 4% | 50% |
| tendencia tecnica | bajista | 89 | -1.40 EUR | 8% | 39% |
| tendencia analistas | mejorando | 181 | -2.41 EUR | 5% | 46% |
| tendencia analistas | estable | 129 | -2.78 EUR | 7% | 52% |
| tendencia analistas | empeorando | 16 | -2.66 EUR | 6% | 56% |
| regimen de mercado | neutro | 181 | -2.04 EUR | 8% | 44% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 97 | -2.06 EUR | 4% | 38% |
| catalizador | con catalizador | 16 | -1.90 EUR | 6% | 38% |
| catalizador | sin catalizador | 377 | -2.45 EUR | 6% | 47% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.64 | -1.96 | **+0.68 EUR** |
| fuerza relativa | -2.69 | -2.25 | **+0.44 EUR** |
| liquidez | -2.65 | -2.29 | **+0.37 EUR** |
| puesto en el ranking | -2.34 | -2.16 | **+0.17 EUR** |
| dispersion | -2.36 | -2.19 | **+0.16 EUR** |
| % compra fuerte | -2.66 | -2.71 | **-0.05 EUR** |
| RSI | -2.25 | -2.47 | **-0.22 EUR** |
| momentum 30d | -2.30 | -2.79 | **-0.48 EUR** |
| volumen relativo | -2.05 | -2.86 | **-0.80 EUR** |
| nota global | -1.64 | -2.52 | **-0.89 EUR** |
| volatilidad | -1.90 | -3.09 | **-1.19 EUR** |
| distancia max 52s | -1.88 | -3.08 | **-1.20 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
