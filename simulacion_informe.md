# Simulacion en paralelo

Actualizado: 2026-10-23 00:00 · dia 61 de ejecucion
**Revision nº4 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **219**
- Operaciones abiertas: 58

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 1% | +16.90 EUR |
| beneficio | 3 | 1% | +7.07 EUR |
| flojo | 75 | 34% | +1.30 EUR |
| plano | 13 | 6% | -1.84 EUR |
| perdida | 76 | 35% | -7.18 EUR |
| nefasta | 49 | 22% | -6.97 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 49 | -2.13% | 3/49 (6%) | 9/49 | 10 |
| 11-20 | 56 | -3.27% | 2/56 (4%) | 4/56 | 9 |
| 21-30 | 114 | -3.99% | 1/114 (1%) | 9/114 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 6 | -0.96% | -1.91% | **+0.95%** | 2/6 (33%) |
| 11-20 | 10 | -3.29% | -0.82% | **-2.47%** | 5/10 (50%) |
| 21-30 | 28 | -2.74% | -0.91% | **-1.83%** | 15/28 (54%) |

**En conjunto:** -2.62% de media frente a -1.03% del indice, una diferencia de **-1.59%**. 22 de 44 operaciones (50%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 35 operaciones, media -2.64%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -2.12% | 37 | -78.60 EUR | 1/37 | -9.70 EUR |
| trailing pegado (3%) | -2.43% | 69 | -167.35 EUR | 4/69 | -10.00 EUR |
| escalera + stop vol x2.5 | -2.57% | 46 | -118.21 EUR | 1/46 | -7.93 EUR |
| escalera + stop vol x3 | -3.00% | 45 | -135.22 EUR | 1/45 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.39% | 219 | -741.91 EUR | 6/219 | -8.08 EUR |
| arranca antes (+3%) | -3.67% | 60 | -220.44 EUR | 4/60 | -10.00 EUR |
| arranca despues (+8%) | -3.77% | 54 | -203.56 EUR | 4/54 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.77% | 54 | -203.56 EUR | 4/54 | -10.00 EUR |
| trailing suelto (7%) | -4.40% | 52 | -228.87 EUR | 3/52 | -10.00 EUR |
| sin trailing, solo stop | -4.79% | 50 | -239.65 EUR | 2/50 | -10.00 EUR |
| stop corto (5%) | -5.60% | 144 | -806.03 EUR | 4/144 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.39%**
- Aciertos (>= 5 EUR limpios): 6/219 (3%)
- Resultado acumulado ficticio: -741.91 EUR sobre 219 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 73 | -3.55 EUR | 0% | 51% |
| nota global | medio | 73 | -3.96 EUR | 3% | 64% |
| nota global | alto | 73 | -2.65 EUR | 5% | 56% |
| puesto en el ranking | bajo | 73 | -2.38 EUR | 7% | 55% |
| puesto en el ranking | medio | 73 | -3.85 EUR | 1% | 59% |
| puesto en el ranking | alto | 73 | -3.93 EUR | 0% | 58% |
| potencial hasta objetivo | bajo | 73 | -3.63 EUR | 3% | 56% |
| potencial hasta objetivo | medio | 73 | -3.88 EUR | 1% | 62% |
| potencial hasta objetivo | alto | 73 | -2.66 EUR | 4% | 53% |
| dispersion | bajo | 73 | -2.68 EUR | 5% | 55% |
| dispersion | medio | 73 | -4.31 EUR | 1% | 64% |
| dispersion | alto | 73 | -3.17 EUR | 1% | 52% |
| % compra fuerte | bajo | 68 | -4.02 EUR | 1% | 60% |
| % compra fuerte | medio | 68 | -2.97 EUR | 1% | 56% |
| % compra fuerte | alto | 69 | -3.51 EUR | 3% | 55% |
| momentum 30d | bajo | 73 | -3.17 EUR | 4% | 55% |
| momentum 30d | medio | 73 | -3.50 EUR | 0% | 56% |
| momentum 30d | alto | 73 | -3.50 EUR | 4% | 60% |
| fuerza relativa | bajo | 73 | -3.52 EUR | 3% | 59% |
| fuerza relativa | medio | 73 | -3.46 EUR | 1% | 55% |
| fuerza relativa | alto | 73 | -3.19 EUR | 4% | 58% |
| RSI | bajo | 73 | -2.77 EUR | 5% | 52% |
| RSI | medio | 73 | -3.73 EUR | 1% | 59% |
| RSI | alto | 73 | -3.66 EUR | 1% | 60% |
| volumen relativo | bajo | 67 | -3.42 EUR | 4% | 63% |
| volumen relativo | medio | 67 | -3.17 EUR | 0% | 48% |
| volumen relativo | alto | 68 | -3.65 EUR | 3% | 56% |
| volatilidad | bajo | 67 | -3.68 EUR | 0% | 55% |
| volatilidad | medio | 67 | -3.68 EUR | 3% | 57% |
| volatilidad | alto | 68 | -2.89 EUR | 4% | 54% |
| liquidez | bajo | 67 | -3.51 EUR | 1% | 55% |
| liquidez | medio | 67 | -2.90 EUR | 4% | 55% |
| liquidez | alto | 68 | -3.82 EUR | 1% | 56% |
| distancia max 52s | bajo | 67 | -2.49 EUR | 6% | 51% |
| distancia max 52s | medio | 67 | -3.53 EUR | 0% | 57% |
| distancia max 52s | alto | 68 | -4.21 EUR | 1% | 59% |
| consenso | buy | 154 | -3.64 EUR | 2% | 57% |
| consenso | strong_buy | 65 | -2.78 EUR | 5% | 57% |
| tendencia tecnica | alcista | 107 | -3.55 EUR | 3% | 58% |
| tendencia tecnica | mixta | 61 | -3.35 EUR | 2% | 56% |
| tendencia tecnica | bajista | 51 | -3.09 EUR | 4% | 57% |
| tendencia analistas | mejorando | 109 | -3.42 EUR | 3% | 57% |
| tendencia analistas | estable | 67 | -3.88 EUR | 3% | 64% |
| tendencia analistas | empeorando | 9 | -4.67 EUR | 0% | 78% |
| regimen de mercado | neutro | 112 | -3.26 EUR | 2% | 53% |
| regimen de mercado | favorable | 107 | -3.52 EUR | 4% | 62% |
| catalizador | sin catalizador | 218 | -3.37 EUR | 3% | 57% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.63 | -2.66 | **+0.97 EUR** |
| nota global | -3.55 | -2.65 | **+0.91 EUR** |
| volatilidad | -3.68 | -2.89 | **+0.78 EUR** |
| % compra fuerte | -4.02 | -3.51 | **+0.51 EUR** |
| fuerza relativa | -3.52 | -3.19 | **+0.33 EUR** |
| volumen relativo | -3.42 | -3.65 | **-0.23 EUR** |
| liquidez | -3.51 | -3.82 | **-0.31 EUR** |
| momentum 30d | -3.17 | -3.50 | **-0.33 EUR** |
| dispersion | -2.68 | -3.17 | **-0.50 EUR** |
| RSI | -2.77 | -3.66 | **-0.89 EUR** |
| puesto en el ranking | -2.38 | -3.93 | **-1.54 EUR** |
| distancia max 52s | -2.49 | -4.21 | **-1.72 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
