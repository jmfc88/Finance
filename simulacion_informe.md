# Simulacion en paralelo

Actualizado: 2026-10-19 06:08 · dia 57 de ejecucion
Proxima revision de ponderacion en 3 dias.

- Operaciones cerradas: **187**
- Operaciones abiertas: 58

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 60 | 32% | +1.30 EUR |
| plano | 12 | 6% | -1.75 EUR |
| perdida | 68 | 36% | -7.25 EUR |
| nefasta | 42 | 22% | -6.78 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 44 | -2.22% | 2/44 (5%) | 8/44 | 9 |
| 11-20 | 50 | -3.47% | 2/50 (4%) | 3/50 | 9 |
| 21-30 | 93 | -4.25% | 1/93 (1%) | 6/93 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 1 | +1.00% | -1.68% | **+2.68%** | 1/1 (100%) |
| 11-20 | 4 | -5.81% | -0.25% | **-5.56%** | 1/4 (25%) |
| 21-30 | 9 | -3.76% | -0.37% | **-3.39%** | 4/9 (44%) |

**En conjunto:** -4.01% de media frente a -0.43% del indice, una diferencia de **-3.58%**. 6 de 14 operaciones (43%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 29 operaciones, media -3.36%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -1.39% | 9 | -12.55 EUR | 0/9 | -8.08 EUR |
| trailing pegado (3%) | -3.07% | 57 | -175.04 EUR | 3/57 | -10.00 EUR |
| LA REAL (escalera 25/08) | -3.56% | 187 | -666.55 EUR | 5/187 | -8.08 EUR |
| escalera + stop vol x2.5 | -3.72% | 14 | -52.02 EUR | 0/14 | -7.93 EUR |
| arranca antes (+3%) | -4.16% | 52 | -216.40 EUR | 3/52 | -10.00 EUR |
| arranca despues (+8%) | -4.34% | 46 | -199.52 EUR | 3/46 | -10.00 EUR |
| actual (8% / +5% / 5%) | -4.34% | 46 | -199.52 EUR | 3/46 | -10.00 EUR |
| escalera + stop vol x3 | -4.55% | 14 | -63.69 EUR | 0/14 | -9.51 EUR |
| trailing suelto (7%) | -5.06% | 44 | -222.66 EUR | 2/44 | -10.00 EUR |
| sin trailing, solo stop | -5.46% | 43 | -234.72 EUR | 1/43 | -10.00 EUR |
| stop corto (5%) | -5.78% | 125 | -722.56 EUR | 3/125 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.56%**
- Aciertos (>= 5 EUR limpios): 5/187 (3%)
- Resultado acumulado ficticio: -666.55 EUR sobre 187 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 62 | -3.71 EUR | 0% | 53% |
| nota global | medio | 62 | -4.14 EUR | 3% | 66% |
| nota global | alto | 63 | -2.86 EUR | 5% | 57% |
| puesto en el ranking | bajo | 62 | -2.56 EUR | 6% | 53% |
| puesto en el ranking | medio | 62 | -3.85 EUR | 2% | 61% |
| puesto en el ranking | alto | 63 | -4.27 EUR | 0% | 62% |
| potencial hasta objetivo | bajo | 62 | -3.89 EUR | 3% | 58% |
| potencial hasta objetivo | medio | 62 | -3.87 EUR | 2% | 63% |
| potencial hasta objetivo | alto | 63 | -2.95 EUR | 3% | 56% |
| dispersion | bajo | 62 | -2.62 EUR | 5% | 52% |
| dispersion | medio | 62 | -4.68 EUR | 2% | 69% |
| dispersion | alto | 63 | -3.40 EUR | 2% | 56% |
| % compra fuerte | bajo | 58 | -4.28 EUR | 2% | 62% |
| % compra fuerte | medio | 58 | -2.97 EUR | 2% | 59% |
| % compra fuerte | alto | 60 | -3.68 EUR | 3% | 57% |
| momentum 30d | bajo | 62 | -3.25 EUR | 3% | 55% |
| momentum 30d | medio | 62 | -3.74 EUR | 2% | 61% |
| momentum 30d | alto | 63 | -3.69 EUR | 3% | 60% |
| fuerza relativa | bajo | 62 | -3.58 EUR | 3% | 61% |
| fuerza relativa | medio | 62 | -3.68 EUR | 0% | 55% |
| fuerza relativa | alto | 63 | -3.43 EUR | 5% | 60% |
| RSI | bajo | 62 | -3.04 EUR | 5% | 53% |
| RSI | medio | 62 | -3.41 EUR | 2% | 58% |
| RSI | alto | 63 | -4.24 EUR | 2% | 65% |
| volumen relativo | bajo | 56 | -3.77 EUR | 4% | 64% |
| volumen relativo | medio | 56 | -3.07 EUR | 0% | 46% |
| volumen relativo | alto | 58 | -3.98 EUR | 3% | 60% |
| volatilidad | bajo | 56 | -4.16 EUR | 0% | 61% |
| volatilidad | medio | 56 | -4.25 EUR | 2% | 59% |
| volatilidad | alto | 58 | -2.47 EUR | 5% | 52% |
| liquidez | bajo | 56 | -3.60 EUR | 2% | 57% |
| liquidez | medio | 56 | -3.69 EUR | 4% | 61% |
| liquidez | alto | 58 | -3.56 EUR | 2% | 53% |
| distancia max 52s | bajo | 56 | -2.75 EUR | 5% | 54% |
| distancia max 52s | medio | 56 | -3.72 EUR | 0% | 57% |
| distancia max 52s | alto | 58 | -4.35 EUR | 2% | 60% |
| consenso | buy | 132 | -3.91 EUR | 2% | 61% |
| consenso | strong_buy | 55 | -2.73 EUR | 4% | 55% |
| tendencia tecnica | alcista | 101 | -3.74 EUR | 3% | 59% |
| tendencia tecnica | mixta | 48 | -2.99 EUR | 2% | 54% |
| tendencia tecnica | bajista | 38 | -3.83 EUR | 3% | 63% |
| tendencia analistas | mejorando | 91 | -3.54 EUR | 3% | 59% |
| tendencia analistas | estable | 57 | -4.43 EUR | 2% | 68% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 104 | -3.56 EUR | 4% | 62% |
| regimen de mercado | neutro | 83 | -3.57 EUR | 1% | 54% |
| catalizador | sin catalizador | 186 | -3.54 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.16 | -2.47 | **+1.69 EUR** |
| potencial hasta objetivo | -3.89 | -2.95 | **+0.94 EUR** |
| nota global | -3.71 | -2.86 | **+0.86 EUR** |
| % compra fuerte | -4.28 | -3.68 | **+0.60 EUR** |
| fuerza relativa | -3.58 | -3.43 | **+0.15 EUR** |
| liquidez | -3.60 | -3.56 | **+0.04 EUR** |
| volumen relativo | -3.77 | -3.98 | **-0.21 EUR** |
| momentum 30d | -3.25 | -3.69 | **-0.44 EUR** |
| dispersion | -2.62 | -3.40 | **-0.78 EUR** |
| RSI | -3.04 | -4.24 | **-1.20 EUR** |
| distancia max 52s | -2.75 | -4.35 | **-1.59 EUR** |
| puesto en el ranking | -2.56 | -4.27 | **-1.72 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
