# Simulacion en paralelo

Actualizado: 2026-10-14 14:32 · dia 52 de ejecucion
Proxima revision de ponderacion en 8 dias.

- Operaciones cerradas: **180**
- Operaciones abiertas: 50

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 57 | 32% | +1.31 EUR |
| plano | 12 | 7% | -1.75 EUR |
| perdida | 66 | 37% | -7.22 EUR |
| nefasta | 40 | 22% | -6.72 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 44 | -2.22% | 2/44 (5%) | 8/44 | 9 |
| 11-20 | 47 | -3.36% | 2/47 (4%) | 3/47 | 9 |
| 21-30 | 89 | -4.28% | 1/89 (1%) | 5/89 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 1 | +1.00% | -1.68% | **+2.68%** | 1/1 (100%) |
| 11-20 | 1 | -8.08% | +0.20% | **-8.28%** | 0/1 (0%) |
| 21-30 | 5 | -3.94% | -0.00% | **-3.94%** | 2/5 (40%) |

**En conjunto:** -3.83% de media frente a -0.21% del indice, una diferencia de **-3.61%**. 3 de 7 operaciones (43%) batieron a su indice.

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
| escalera + stop vol x4 | -0.22% | 4 | -0.88 EUR | 0/4 | -6.42 EUR |
| escalera + stop vol x2.5 | -2.69% | 7 | -18.83 EUR | 0/7 | -7.93 EUR |
| trailing pegado (3%) | -3.03% | 55 | -166.73 EUR | 3/55 | -10.00 EUR |
| escalera + stop vol x3 | -3.38% | 7 | -23.66 EUR | 0/7 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.54% | 180 | -637.23 EUR | 5/180 | -8.08 EUR |
| arranca antes (+3%) | -4.05% | 51 | -206.40 EUR | 3/51 | -10.00 EUR |
| arranca despues (+8%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| actual (8% / +5% / 5%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| trailing suelto (7%) | -4.95% | 43 | -212.66 EUR | 2/43 | -10.00 EUR |
| sin trailing, solo stop | -5.35% | 42 | -224.72 EUR | 1/42 | -10.00 EUR |
| stop corto (5%) | -5.73% | 120 | -687.56 EUR | 3/120 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.54%**
- Aciertos (>= 5 EUR limpios): 5/180 (3%)
- Resultado acumulado ficticio: -637.23 EUR sobre 180 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 60 | -3.72 EUR | 0% | 53% |
| nota global | medio | 60 | -4.16 EUR | 3% | 68% |
| nota global | alto | 60 | -2.75 EUR | 5% | 55% |
| puesto en el ranking | bajo | 60 | -2.79 EUR | 5% | 53% |
| puesto en el ranking | medio | 60 | -3.60 EUR | 3% | 62% |
| puesto en el ranking | alto | 60 | -4.24 EUR | 0% | 62% |
| potencial hasta objetivo | bajo | 60 | -4.05 EUR | 3% | 58% |
| potencial hasta objetivo | medio | 60 | -3.73 EUR | 2% | 63% |
| potencial hasta objetivo | alto | 60 | -2.84 EUR | 3% | 55% |
| dispersion | bajo | 60 | -2.44 EUR | 5% | 50% |
| dispersion | medio | 60 | -4.71 EUR | 2% | 70% |
| dispersion | alto | 60 | -3.47 EUR | 2% | 57% |
| % compra fuerte | bajo | 56 | -4.31 EUR | 2% | 62% |
| % compra fuerte | medio | 56 | -2.95 EUR | 2% | 59% |
| % compra fuerte | alto | 57 | -3.60 EUR | 4% | 56% |
| momentum 30d | bajo | 60 | -3.24 EUR | 3% | 55% |
| momentum 30d | medio | 60 | -3.80 EUR | 2% | 62% |
| momentum 30d | alto | 60 | -3.58 EUR | 3% | 60% |
| fuerza relativa | bajo | 60 | -3.59 EUR | 3% | 62% |
| fuerza relativa | medio | 60 | -3.68 EUR | 0% | 55% |
| fuerza relativa | alto | 60 | -3.35 EUR | 5% | 60% |
| RSI | bajo | 60 | -3.02 EUR | 5% | 55% |
| RSI | medio | 60 | -3.40 EUR | 2% | 57% |
| RSI | alto | 60 | -4.19 EUR | 2% | 65% |
| volumen relativo | bajo | 54 | -3.78 EUR | 4% | 65% |
| volumen relativo | medio | 54 | -2.96 EUR | 0% | 44% |
| volumen relativo | alto | 55 | -4.02 EUR | 4% | 62% |
| volatilidad | bajo | 54 | -4.18 EUR | 0% | 59% |
| volatilidad | medio | 54 | -4.28 EUR | 2% | 61% |
| volatilidad | alto | 55 | -2.33 EUR | 5% | 51% |
| liquidez | bajo | 54 | -3.60 EUR | 2% | 57% |
| liquidez | medio | 54 | -3.69 EUR | 4% | 61% |
| liquidez | alto | 55 | -3.48 EUR | 2% | 53% |
| distancia max 52s | bajo | 54 | -2.56 EUR | 6% | 52% |
| distancia max 52s | medio | 54 | -3.89 EUR | 0% | 59% |
| distancia max 52s | alto | 55 | -4.31 EUR | 2% | 60% |
| consenso | buy | 127 | -3.96 EUR | 2% | 61% |
| consenso | strong_buy | 53 | -2.53 EUR | 4% | 53% |
| tendencia tecnica | alcista | 99 | -3.74 EUR | 3% | 60% |
| tendencia tecnica | mixta | 46 | -2.96 EUR | 2% | 54% |
| tendencia tecnica | bajista | 35 | -3.73 EUR | 3% | 63% |
| tendencia analistas | mejorando | 85 | -3.54 EUR | 4% | 60% |
| tendencia analistas | estable | 56 | -4.37 EUR | 2% | 68% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 100 | -3.47 EUR | 4% | 62% |
| regimen de mercado | neutro | 80 | -3.62 EUR | 1% | 55% |
| catalizador | sin catalizador | 179 | -3.51 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.18 | -2.33 | **+1.85 EUR** |
| potencial hasta objetivo | -4.05 | -2.84 | **+1.21 EUR** |
| nota global | -3.72 | -2.75 | **+0.97 EUR** |
| % compra fuerte | -4.31 | -3.60 | **+0.70 EUR** |
| fuerza relativa | -3.59 | -3.35 | **+0.24 EUR** |
| liquidez | -3.60 | -3.48 | **+0.12 EUR** |
| volumen relativo | -3.78 | -4.02 | **-0.25 EUR** |
| momentum 30d | -3.24 | -3.58 | **-0.33 EUR** |
| dispersion | -2.44 | -3.47 | **-1.04 EUR** |
| RSI | -3.02 | -4.19 | **-1.17 EUR** |
| puesto en el ranking | -2.79 | -4.24 | **-1.45 EUR** |
| distancia max 52s | -2.56 | -4.31 | **-1.75 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
