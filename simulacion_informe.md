# Simulacion en paralelo

Actualizado: 2026-10-23 11:32 · dia 61 de ejecucion
**Revision nº4 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **224**
- Operaciones abiertas: 57

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 1% | +16.90 EUR |
| beneficio | 3 | 1% | +7.07 EUR |
| flojo | 76 | 34% | +1.32 EUR |
| plano | 14 | 6% | -1.76 EUR |
| perdida | 78 | 35% | -7.21 EUR |
| nefasta | 50 | 22% | -6.99 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 49 | -2.13% | 3/49 (6%) | 9/49 | 10 |
| 11-20 | 57 | -3.35% | 2/57 (4%) | 4/57 | 9 |
| 21-30 | 118 | -3.97% | 1/118 (1%) | 9/118 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 6 | -0.96% | -1.91% | **+0.95%** | 2/6 (33%) |
| 11-20 | 11 | -3.72% | -0.86% | **-2.87%** | 5/11 (45%) |
| 21-30 | 32 | -2.83% | -1.14% | **-1.69%** | 17/32 (53%) |

**En conjunto:** -2.80% de media frente a -1.17% del indice, una diferencia de **-1.63%**. 24 de 49 operaciones (49%) batieron a su indice.

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
| trailing pegado (3%) | -2.54% | 73 | -185.07 EUR | 4/73 | -10.00 EUR |
| escalera + stop vol x4 | -2.76% | 42 | -116.05 EUR | 1/42 | -10.34 EUR |
| escalera + stop vol x2.5 | -2.81% | 51 | -143.25 EUR | 1/51 | -7.93 EUR |
| escalera + stop vol x3 | -3.27% | 50 | -163.66 EUR | 1/50 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.41% | 224 | -763.87 EUR | 6/224 | -8.08 EUR |
| arranca antes (+3%) | -3.63% | 64 | -232.25 EUR | 4/64 | -10.00 EUR |
| arranca despues (+8%) | -3.82% | 58 | -221.28 EUR | 4/58 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.82% | 58 | -221.28 EUR | 4/58 | -10.00 EUR |
| trailing suelto (7%) | -4.40% | 56 | -246.59 EUR | 3/56 | -10.00 EUR |
| sin trailing, solo stop | -4.77% | 54 | -257.37 EUR | 2/54 | -10.00 EUR |
| stop corto (5%) | -5.58% | 149 | -830.93 EUR | 4/149 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.41%**
- Aciertos (>= 5 EUR limpios): 6/224 (3%)
- Resultado acumulado ficticio: -763.87 EUR sobre 224 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 74 | -3.36 EUR | 0% | 49% |
| nota global | medio | 74 | -4.10 EUR | 3% | 66% |
| nota global | alto | 76 | -2.78 EUR | 5% | 57% |
| puesto en el ranking | bajo | 74 | -2.46 EUR | 7% | 55% |
| puesto en el ranking | medio | 74 | -3.91 EUR | 1% | 59% |
| puesto en el ranking | alto | 76 | -3.85 EUR | 0% | 57% |
| potencial hasta objetivo | bajo | 74 | -3.59 EUR | 3% | 55% |
| potencial hasta objetivo | medio | 74 | -3.94 EUR | 1% | 62% |
| potencial hasta objetivo | alto | 76 | -2.72 EUR | 4% | 54% |
| dispersion | bajo | 74 | -2.78 EUR | 5% | 55% |
| dispersion | medio | 74 | -4.31 EUR | 1% | 65% |
| dispersion | alto | 76 | -3.15 EUR | 1% | 51% |
| % compra fuerte | bajo | 69 | -3.86 EUR | 1% | 58% |
| % compra fuerte | medio | 69 | -3.13 EUR | 1% | 58% |
| % compra fuerte | alto | 71 | -3.51 EUR | 3% | 55% |
| momentum 30d | bajo | 74 | -3.36 EUR | 4% | 57% |
| momentum 30d | medio | 74 | -3.57 EUR | 0% | 57% |
| momentum 30d | alto | 76 | -3.31 EUR | 4% | 58% |
| fuerza relativa | bajo | 74 | -3.58 EUR | 3% | 59% |
| fuerza relativa | medio | 74 | -3.37 EUR | 1% | 54% |
| fuerza relativa | alto | 76 | -3.28 EUR | 4% | 58% |
| RSI | bajo | 74 | -2.97 EUR | 5% | 54% |
| RSI | medio | 74 | -3.51 EUR | 1% | 57% |
| RSI | alto | 76 | -3.74 EUR | 1% | 61% |
| volumen relativo | bajo | 69 | -3.39 EUR | 4% | 62% |
| volumen relativo | medio | 69 | -3.31 EUR | 0% | 49% |
| volumen relativo | alto | 69 | -3.61 EUR | 3% | 55% |
| volatilidad | bajo | 69 | -3.54 EUR | 0% | 54% |
| volatilidad | medio | 69 | -3.68 EUR | 3% | 57% |
| volatilidad | alto | 69 | -3.10 EUR | 4% | 57% |
| liquidez | bajo | 69 | -3.38 EUR | 1% | 54% |
| liquidez | medio | 69 | -3.05 EUR | 4% | 57% |
| liquidez | alto | 69 | -3.88 EUR | 1% | 57% |
| distancia max 52s | bajo | 69 | -2.49 EUR | 6% | 51% |
| distancia max 52s | medio | 69 | -3.57 EUR | 0% | 57% |
| distancia max 52s | alto | 69 | -4.25 EUR | 1% | 59% |
| consenso | buy | 156 | -3.63 EUR | 2% | 57% |
| consenso | strong_buy | 68 | -2.91 EUR | 4% | 57% |
| tendencia tecnica | alcista | 109 | -3.57 EUR | 3% | 58% |
| tendencia tecnica | mixta | 62 | -3.43 EUR | 2% | 56% |
| tendencia tecnica | bajista | 53 | -3.07 EUR | 4% | 57% |
| tendencia analistas | mejorando | 110 | -3.46 EUR | 3% | 57% |
| tendencia analistas | estable | 69 | -3.84 EUR | 3% | 64% |
| tendencia analistas | empeorando | 9 | -4.67 EUR | 0% | 78% |
| regimen de mercado | neutro | 116 | -3.27 EUR | 2% | 53% |
| regimen de mercado | favorable | 107 | -3.52 EUR | 4% | 62% |
| catalizador | sin catalizador | 223 | -3.39 EUR | 3% | 57% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.59 | -2.72 | **+0.87 EUR** |
| nota global | -3.36 | -2.78 | **+0.59 EUR** |
| volatilidad | -3.54 | -3.10 | **+0.44 EUR** |
| % compra fuerte | -3.86 | -3.51 | **+0.35 EUR** |
| fuerza relativa | -3.58 | -3.28 | **+0.29 EUR** |
| momentum 30d | -3.36 | -3.31 | **+0.05 EUR** |
| volumen relativo | -3.39 | -3.61 | **-0.22 EUR** |
| dispersion | -2.78 | -3.15 | **-0.38 EUR** |
| liquidez | -3.38 | -3.88 | **-0.50 EUR** |
| RSI | -2.97 | -3.74 | **-0.78 EUR** |
| puesto en el ranking | -2.46 | -3.85 | **-1.39 EUR** |
| distancia max 52s | -2.49 | -4.25 | **-1.76 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
