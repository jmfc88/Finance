# Simulacion en paralelo

Actualizado: 2026-10-21 18:01 · dia 59 de ejecucion
Proxima revision de ponderacion en 1 dia.

- Operaciones cerradas: **205**
- Operaciones abiertas: 55

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 1% | +16.90 EUR |
| beneficio | 3 | 1% | +7.07 EUR |
| flojo | 69 | 34% | +1.29 EUR |
| plano | 13 | 6% | -1.84 EUR |
| perdida | 73 | 36% | -7.20 EUR |
| nefasta | 44 | 21% | -6.84 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 47 | -1.97% | 3/47 (6%) | 9/47 | 10 |
| 11-20 | 54 | -3.30% | 2/54 (4%) | 3/54 | 8 |
| 21-30 | 104 | -4.03% | 1/104 (1%) | 7/104 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 4 | +1.56% | -1.85% | **+3.40%** | 2/4 (50%) |
| 11-20 | 8 | -3.54% | -0.56% | **-2.98%** | 4/8 (50%) |
| 21-30 | 19 | -2.60% | -0.85% | **-1.75%** | 10/19 (53%) |

**En conjunto:** -2.30% de media frente a -0.90% del indice, una diferencia de **-1.40%**. 16 de 31 operaciones (52%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 34 operaciones, media -2.60%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -1.72% | 25 | -42.97 EUR | 1/25 | -8.20 EUR |
| trailing pegado (3%) | -2.62% | 63 | -164.85 EUR | 4/63 | -10.00 EUR |
| escalera + stop vol x2.5 | -2.66% | 32 | -85.16 EUR | 1/32 | -7.93 EUR |
| escalera + stop vol x3 | -3.08% | 31 | -95.39 EUR | 1/31 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.37% | 205 | -689.96 EUR | 6/205 | -8.08 EUR |
| arranca antes (+3%) | -3.64% | 57 | -207.41 EUR | 4/57 | -10.00 EUR |
| arranca despues (+8%) | -3.74% | 51 | -190.53 EUR | 4/51 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.74% | 51 | -190.53 EUR | 4/51 | -10.00 EUR |
| trailing suelto (7%) | -4.36% | 49 | -213.67 EUR | 3/49 | -10.00 EUR |
| sin trailing, solo stop | -4.70% | 48 | -225.73 EUR | 2/48 | -10.00 EUR |
| stop corto (5%) | -5.56% | 135 | -750.92 EUR | 4/135 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.37%**
- Aciertos (>= 5 EUR limpios): 6/205 (3%)
- Resultado acumulado ficticio: -689.96 EUR sobre 205 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 68 | -3.62 EUR | 0% | 51% |
| nota global | medio | 68 | -4.00 EUR | 3% | 65% |
| nota global | alto | 69 | -2.49 EUR | 6% | 55% |
| puesto en el ranking | bajo | 68 | -2.21 EUR | 7% | 53% |
| puesto en el ranking | medio | 68 | -3.92 EUR | 1% | 60% |
| puesto en el ranking | alto | 69 | -3.95 EUR | 0% | 58% |
| potencial hasta objetivo | bajo | 68 | -3.57 EUR | 3% | 56% |
| potencial hasta objetivo | medio | 68 | -4.05 EUR | 1% | 63% |
| potencial hasta objetivo | alto | 69 | -2.50 EUR | 4% | 52% |
| dispersion | bajo | 68 | -2.60 EUR | 6% | 53% |
| dispersion | medio | 68 | -4.48 EUR | 1% | 68% |
| dispersion | alto | 69 | -3.02 EUR | 1% | 51% |
| % compra fuerte | bajo | 64 | -4.30 EUR | 2% | 62% |
| % compra fuerte | medio | 64 | -2.80 EUR | 2% | 55% |
| % compra fuerte | alto | 64 | -3.44 EUR | 3% | 55% |
| momentum 30d | bajo | 68 | -3.17 EUR | 4% | 54% |
| momentum 30d | medio | 68 | -3.29 EUR | 1% | 57% |
| momentum 30d | alto | 69 | -3.63 EUR | 3% | 59% |
| fuerza relativa | bajo | 68 | -3.31 EUR | 4% | 59% |
| fuerza relativa | medio | 68 | -3.36 EUR | 0% | 53% |
| fuerza relativa | alto | 69 | -3.43 EUR | 4% | 59% |
| RSI | bajo | 68 | -2.71 EUR | 6% | 51% |
| RSI | medio | 68 | -3.44 EUR | 1% | 57% |
| RSI | alto | 69 | -3.94 EUR | 1% | 62% |
| volumen relativo | bajo | 62 | -3.44 EUR | 5% | 63% |
| volumen relativo | medio | 62 | -2.92 EUR | 0% | 45% |
| volumen relativo | alto | 64 | -3.80 EUR | 3% | 58% |
| volatilidad | bajo | 62 | -3.69 EUR | 0% | 55% |
| volatilidad | medio | 62 | -3.80 EUR | 3% | 58% |
| volatilidad | alto | 64 | -2.71 EUR | 5% | 53% |
| liquidez | bajo | 62 | -3.65 EUR | 2% | 56% |
| liquidez | medio | 62 | -2.97 EUR | 5% | 55% |
| liquidez | alto | 64 | -3.56 EUR | 2% | 55% |
| distancia max 52s | bajo | 62 | -2.34 EUR | 6% | 50% |
| distancia max 52s | medio | 62 | -3.61 EUR | 0% | 56% |
| distancia max 52s | alto | 64 | -4.21 EUR | 2% | 59% |
| consenso | buy | 146 | -3.65 EUR | 2% | 58% |
| consenso | strong_buy | 59 | -2.67 EUR | 5% | 56% |
| tendencia tecnica | alcista | 106 | -3.59 EUR | 3% | 58% |
| tendencia tecnica | mixta | 54 | -3.12 EUR | 2% | 54% |
| tendencia tecnica | bajista | 45 | -3.12 EUR | 4% | 58% |
| tendencia analistas | mejorando | 102 | -3.37 EUR | 3% | 57% |
| tendencia analistas | estable | 61 | -3.83 EUR | 3% | 64% |
| tendencia analistas | empeorando | 9 | -4.67 EUR | 0% | 78% |
| regimen de mercado | favorable | 105 | -3.52 EUR | 4% | 62% |
| regimen de mercado | neutro | 100 | -3.20 EUR | 2% | 52% |
| catalizador | sin catalizador | 204 | -3.34 EUR | 3% | 57% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -3.62 | -2.49 | **+1.13 EUR** |
| potencial hasta objetivo | -3.57 | -2.50 | **+1.07 EUR** |
| volatilidad | -3.69 | -2.71 | **+0.98 EUR** |
| % compra fuerte | -4.30 | -3.44 | **+0.86 EUR** |
| liquidez | -3.65 | -3.56 | **+0.09 EUR** |
| fuerza relativa | -3.31 | -3.43 | **-0.12 EUR** |
| volumen relativo | -3.44 | -3.80 | **-0.36 EUR** |
| dispersion | -2.60 | -3.02 | **-0.42 EUR** |
| momentum 30d | -3.17 | -3.63 | **-0.46 EUR** |
| RSI | -2.71 | -3.94 | **-1.23 EUR** |
| puesto en el ranking | -2.21 | -3.95 | **-1.74 EUR** |
| distancia max 52s | -2.34 | -4.21 | **-1.87 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
