# Simulacion en paralelo

Actualizado: 2026-10-13 16:58 · dia 51 de ejecucion
Proxima revision de ponderacion en 9 dias.

- Operaciones cerradas: **175**
- Operaciones abiertas: 54

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 55 | 31% | +1.28 EUR |
| plano | 12 | 7% | -1.75 EUR |
| perdida | 66 | 38% | -7.22 EUR |
| nefasta | 37 | 21% | -6.61 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 43 | -2.30% | 2/43 (5%) | 8/43 | 9 |
| 11-20 | 46 | -3.26% | 2/46 (4%) | 3/46 | 9 |
| 21-30 | 86 | -4.29% | 1/86 (1%) | 4/86 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 0 | - | - | - | - |
| 11-20 | 0 | - | - | - | - |
| 21-30 | 2 | -3.54% | -0.52% | **-3.02%** | 1/2 (50%) |

**En conjunto:** -3.54% de media frente a -0.52% del indice, una diferencia de **-3.02%**. 1 de 2 operaciones (50%) batieron a su indice.

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
| escalera + stop vol x4 | +1.00% | 1 | +1.00 EUR | 0/1 | +1.00 EUR |
| trailing pegado (3%) | -3.14% | 54 | -169.79 EUR | 3/54 | -10.00 EUR |
| escalera + stop vol x2.5 | -3.46% | 2 | -6.93 EUR | 0/2 | -7.93 EUR |
| LA REAL (escalera 25/08) | -3.53% | 175 | -617.53 EUR | 5/175 | -8.08 EUR |
| arranca antes (+3%) | -4.05% | 51 | -206.40 EUR | 3/51 | -10.00 EUR |
| arranca despues (+8%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| actual (8% / +5% / 5%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| escalera + stop vol x3 | -4.25% | 2 | -8.51 EUR | 0/2 | -9.51 EUR |
| trailing suelto (7%) | -4.95% | 43 | -212.66 EUR | 2/43 | -10.00 EUR |
| sin trailing, solo stop | -5.35% | 42 | -224.72 EUR | 1/42 | -10.00 EUR |
| stop corto (5%) | -5.70% | 117 | -666.56 EUR | 3/117 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.53%**
- Aciertos (>= 5 EUR limpios): 5/175 (3%)
- Resultado acumulado ficticio: -617.53 EUR sobre 175 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 58 | -3.77 EUR | 0% | 53% |
| nota global | medio | 58 | -4.02 EUR | 3% | 67% |
| nota global | alto | 59 | -2.81 EUR | 5% | 56% |
| puesto en el ranking | bajo | 58 | -2.76 EUR | 5% | 53% |
| puesto en el ranking | medio | 58 | -3.75 EUR | 3% | 64% |
| puesto en el ranking | alto | 59 | -4.06 EUR | 0% | 59% |
| potencial hasta objetivo | bajo | 58 | -4.07 EUR | 3% | 59% |
| potencial hasta objetivo | medio | 58 | -3.58 EUR | 2% | 62% |
| potencial hasta objetivo | alto | 59 | -2.95 EUR | 3% | 56% |
| dispersion | bajo | 58 | -2.40 EUR | 5% | 50% |
| dispersion | medio | 58 | -4.80 EUR | 2% | 71% |
| dispersion | alto | 59 | -3.39 EUR | 2% | 56% |
| % compra fuerte | bajo | 55 | -4.36 EUR | 2% | 64% |
| % compra fuerte | medio | 55 | -3.11 EUR | 2% | 60% |
| % compra fuerte | alto | 55 | -3.44 EUR | 4% | 55% |
| momentum 30d | bajo | 58 | -2.92 EUR | 3% | 52% |
| momentum 30d | medio | 58 | -4.01 EUR | 2% | 64% |
| momentum 30d | alto | 59 | -3.66 EUR | 3% | 61% |
| fuerza relativa | bajo | 58 | -3.27 EUR | 3% | 59% |
| fuerza relativa | medio | 58 | -3.85 EUR | 0% | 57% |
| fuerza relativa | alto | 59 | -3.47 EUR | 5% | 61% |
| RSI | bajo | 58 | -2.85 EUR | 5% | 53% |
| RSI | medio | 58 | -3.40 EUR | 2% | 57% |
| RSI | alto | 59 | -4.33 EUR | 2% | 66% |
| volumen relativo | bajo | 52 | -3.79 EUR | 4% | 63% |
| volumen relativo | medio | 52 | -2.69 EUR | 0% | 44% |
| volumen relativo | alto | 54 | -4.23 EUR | 4% | 63% |
| volatilidad | bajo | 52 | -4.21 EUR | 0% | 60% |
| volatilidad | medio | 52 | -4.30 EUR | 2% | 62% |
| volatilidad | alto | 54 | -2.27 EUR | 6% | 50% |
| liquidez | bajo | 52 | -3.43 EUR | 2% | 56% |
| liquidez | medio | 52 | -3.70 EUR | 4% | 62% |
| liquidez | alto | 54 | -3.61 EUR | 2% | 54% |
| distancia max 52s | bajo | 52 | -2.72 EUR | 6% | 54% |
| distancia max 52s | medio | 52 | -3.75 EUR | 0% | 58% |
| distancia max 52s | alto | 54 | -4.24 EUR | 2% | 59% |
| consenso | buy | 124 | -3.95 EUR | 2% | 61% |
| consenso | strong_buy | 51 | -2.49 EUR | 4% | 53% |
| tendencia tecnica | alcista | 99 | -3.74 EUR | 3% | 60% |
| tendencia tecnica | mixta | 46 | -2.96 EUR | 2% | 54% |
| tendencia tecnica | bajista | 30 | -3.69 EUR | 3% | 63% |
| tendencia analistas | mejorando | 83 | -3.43 EUR | 4% | 59% |
| tendencia analistas | estable | 55 | -4.46 EUR | 2% | 69% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 97 | -3.45 EUR | 4% | 62% |
| regimen de mercado | neutro | 78 | -3.63 EUR | 1% | 55% |
| catalizador | sin catalizador | 174 | -3.50 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.21 | -2.27 | **+1.94 EUR** |
| potencial hasta objetivo | -4.07 | -2.95 | **+1.12 EUR** |
| nota global | -3.77 | -2.81 | **+0.96 EUR** |
| % compra fuerte | -4.36 | -3.44 | **+0.92 EUR** |
| liquidez | -3.43 | -3.61 | **-0.18 EUR** |
| fuerza relativa | -3.27 | -3.47 | **-0.19 EUR** |
| volumen relativo | -3.79 | -4.23 | **-0.45 EUR** |
| momentum 30d | -2.92 | -3.66 | **-0.74 EUR** |
| dispersion | -2.40 | -3.39 | **-1.00 EUR** |
| puesto en el ranking | -2.76 | -4.06 | **-1.31 EUR** |
| RSI | -2.85 | -4.33 | **-1.48 EUR** |
| distancia max 52s | -2.72 | -4.24 | **-1.52 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
