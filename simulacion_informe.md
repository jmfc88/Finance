# Simulacion en paralelo

Actualizado: 2026-10-14 00:20 · dia 52 de ejecucion
Proxima revision de ponderacion en 8 dias.

- Operaciones cerradas: **176**
- Operaciones abiertas: 54

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 56 | 32% | +1.27 EUR |
| plano | 12 | 7% | -1.75 EUR |
| perdida | 66 | 38% | -7.22 EUR |
| nefasta | 37 | 21% | -6.61 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 44 | -2.22% | 2/44 (5%) | 8/44 | 9 |
| 11-20 | 46 | -3.26% | 2/46 (4%) | 3/46 | 9 |
| 21-30 | 86 | -4.29% | 1/86 (1%) | 4/86 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 1 | +1.00% | -1.68% | **+2.68%** | 1/1 (100%) |
| 11-20 | 0 | - | - | - | - |
| 21-30 | 2 | -3.54% | -0.52% | **-3.02%** | 1/2 (50%) |

**En conjunto:** -2.03% de media frente a -0.90% del indice, una diferencia de **-1.12%**. 2 de 3 operaciones (67%) batieron a su indice.

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
| escalera + stop vol x4 | +1.00% | 2 | +2.00 EUR | 0/2 | +1.00 EUR |
| escalera + stop vol x2.5 | -1.98% | 3 | -5.93 EUR | 0/3 | -7.93 EUR |
| escalera + stop vol x3 | -2.50% | 3 | -7.51 EUR | 0/3 | -9.51 EUR |
| trailing pegado (3%) | -3.14% | 54 | -169.79 EUR | 3/54 | -10.00 EUR |
| LA REAL (escalera 25/08) | -3.50% | 176 | -616.53 EUR | 5/176 | -8.08 EUR |
| arranca antes (+3%) | -4.05% | 51 | -206.40 EUR | 3/51 | -10.00 EUR |
| arranca despues (+8%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| actual (8% / +5% / 5%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
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

- Media neta: **-3.50%**
- Aciertos (>= 5 EUR limpios): 5/176 (3%)
- Resultado acumulado ficticio: -616.53 EUR sobre 176 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 58 | -3.77 EUR | 0% | 53% |
| nota global | medio | 58 | -4.02 EUR | 3% | 67% |
| nota global | alto | 60 | -2.75 EUR | 5% | 55% |
| puesto en el ranking | bajo | 58 | -2.60 EUR | 5% | 52% |
| puesto en el ranking | medio | 58 | -3.75 EUR | 3% | 64% |
| puesto en el ranking | alto | 60 | -4.13 EUR | 0% | 60% |
| potencial hasta objetivo | bajo | 58 | -4.07 EUR | 3% | 59% |
| potencial hasta objetivo | medio | 58 | -3.58 EUR | 2% | 62% |
| potencial hasta objetivo | alto | 60 | -2.88 EUR | 3% | 55% |
| dispersion | bajo | 58 | -2.40 EUR | 5% | 50% |
| dispersion | medio | 58 | -4.64 EUR | 2% | 69% |
| dispersion | alto | 60 | -3.47 EUR | 2% | 57% |
| % compra fuerte | bajo | 55 | -4.36 EUR | 2% | 64% |
| % compra fuerte | medio | 55 | -2.95 EUR | 2% | 58% |
| % compra fuerte | alto | 56 | -3.52 EUR | 4% | 55% |
| momentum 30d | bajo | 58 | -2.92 EUR | 3% | 52% |
| momentum 30d | medio | 58 | -4.01 EUR | 2% | 64% |
| momentum 30d | alto | 60 | -3.58 EUR | 3% | 60% |
| fuerza relativa | bajo | 58 | -3.27 EUR | 3% | 59% |
| fuerza relativa | medio | 58 | -3.89 EUR | 0% | 57% |
| fuerza relativa | alto | 60 | -3.35 EUR | 5% | 60% |
| RSI | bajo | 58 | -2.85 EUR | 5% | 53% |
| RSI | medio | 58 | -3.24 EUR | 2% | 55% |
| RSI | alto | 60 | -4.39 EUR | 2% | 67% |
| volumen relativo | bajo | 53 | -3.87 EUR | 4% | 64% |
| volumen relativo | medio | 53 | -2.65 EUR | 0% | 43% |
| volumen relativo | alto | 53 | -4.13 EUR | 4% | 62% |
| volatilidad | bajo | 53 | -4.28 EUR | 0% | 60% |
| volatilidad | medio | 53 | -4.03 EUR | 2% | 58% |
| volatilidad | alto | 53 | -2.33 EUR | 6% | 51% |
| liquidez | bajo | 53 | -3.51 EUR | 2% | 57% |
| liquidez | medio | 53 | -3.62 EUR | 4% | 60% |
| liquidez | alto | 53 | -3.52 EUR | 2% | 53% |
| distancia max 52s | bajo | 53 | -2.65 EUR | 6% | 53% |
| distancia max 52s | medio | 53 | -3.56 EUR | 2% | 57% |
| distancia max 52s | alto | 53 | -4.44 EUR | 0% | 60% |
| consenso | buy | 124 | -3.95 EUR | 2% | 61% |
| consenso | strong_buy | 52 | -2.43 EUR | 4% | 52% |
| tendencia tecnica | alcista | 99 | -3.74 EUR | 3% | 60% |
| tendencia tecnica | mixta | 46 | -2.96 EUR | 2% | 54% |
| tendencia tecnica | bajista | 31 | -3.54 EUR | 3% | 61% |
| tendencia analistas | mejorando | 83 | -3.43 EUR | 4% | 59% |
| tendencia analistas | estable | 56 | -4.37 EUR | 2% | 68% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 97 | -3.45 EUR | 4% | 62% |
| regimen de mercado | neutro | 79 | -3.57 EUR | 1% | 54% |
| catalizador | sin catalizador | 175 | -3.48 EUR | 3% | 58% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.28 | -2.33 | **+1.95 EUR** |
| potencial hasta objetivo | -4.07 | -2.88 | **+1.18 EUR** |
| nota global | -3.77 | -2.75 | **+1.02 EUR** |
| % compra fuerte | -4.36 | -3.52 | **+0.84 EUR** |
| liquidez | -3.51 | -3.52 | **-0.02 EUR** |
| fuerza relativa | -3.27 | -3.35 | **-0.08 EUR** |
| volumen relativo | -3.87 | -4.13 | **-0.27 EUR** |
| momentum 30d | -2.92 | -3.58 | **-0.66 EUR** |
| dispersion | -2.40 | -3.47 | **-1.07 EUR** |
| puesto en el ranking | -2.60 | -4.13 | **-1.53 EUR** |
| RSI | -2.85 | -4.39 | **-1.54 EUR** |
| distancia max 52s | -2.65 | -4.44 | **-1.79 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
