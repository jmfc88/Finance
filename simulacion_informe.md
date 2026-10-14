# Simulacion en paralelo

Actualizado: 2026-10-14 11:45 · dia 52 de ejecucion
Proxima revision de ponderacion en 8 dias.

- Operaciones cerradas: **177**
- Operaciones abiertas: 53

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 56 | 32% | +1.27 EUR |
| plano | 12 | 7% | -1.75 EUR |
| perdida | 66 | 37% | -7.22 EUR |
| nefasta | 38 | 21% | -6.65 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 44 | -2.22% | 2/44 (5%) | 8/44 | 9 |
| 11-20 | 46 | -3.26% | 2/46 (4%) | 3/46 | 9 |
| 21-30 | 87 | -4.33% | 1/87 (1%) | 4/87 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 1 | +1.00% | -1.68% | **+2.68%** | 1/1 (100%) |
| 11-20 | 0 | - | - | - | - |
| 21-30 | 3 | -5.05% | -0.17% | **-4.88%** | 1/3 (33%) |

**En conjunto:** -3.54% de media frente a -0.55% del indice, una diferencia de **-2.99%**. 2 de 4 operaciones (50%) batieron a su indice.

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
| escalera + stop vol x2.5 | -3.03% | 4 | -12.12 EUR | 0/4 | -7.93 EUR |
| trailing pegado (3%) | -3.14% | 54 | -169.79 EUR | 3/54 | -10.00 EUR |
| LA REAL (escalera 25/08) | -3.53% | 177 | -624.61 EUR | 5/177 | -8.08 EUR |
| escalera + stop vol x3 | -3.73% | 4 | -14.93 EUR | 0/4 | -9.51 EUR |
| arranca antes (+3%) | -4.05% | 51 | -206.40 EUR | 3/51 | -10.00 EUR |
| arranca despues (+8%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| actual (8% / +5% / 5%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| trailing suelto (7%) | -4.95% | 43 | -212.66 EUR | 2/43 | -10.00 EUR |
| sin trailing, solo stop | -5.35% | 42 | -224.72 EUR | 1/42 | -10.00 EUR |
| stop corto (5%) | -5.71% | 118 | -673.56 EUR | 3/118 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.53%**
- Aciertos (>= 5 EUR limpios): 5/177 (3%)
- Resultado acumulado ficticio: -624.61 EUR sobre 177 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 59 | -3.84 EUR | 0% | 54% |
| nota global | medio | 59 | -4.09 EUR | 3% | 68% |
| nota global | alto | 59 | -2.66 EUR | 5% | 54% |
| puesto en el ranking | bajo | 59 | -2.70 EUR | 5% | 53% |
| puesto en el ranking | medio | 59 | -3.72 EUR | 3% | 63% |
| puesto en el ranking | alto | 59 | -4.17 EUR | 0% | 61% |
| potencial hasta objetivo | bajo | 59 | -4.14 EUR | 3% | 59% |
| potencial hasta objetivo | medio | 59 | -3.50 EUR | 2% | 61% |
| potencial hasta objetivo | alto | 59 | -2.95 EUR | 3% | 56% |
| dispersion | bajo | 59 | -2.34 EUR | 5% | 49% |
| dispersion | medio | 59 | -4.85 EUR | 2% | 71% |
| dispersion | alto | 59 | -3.39 EUR | 2% | 56% |
| % compra fuerte | bajo | 55 | -4.36 EUR | 2% | 64% |
| % compra fuerte | medio | 55 | -2.95 EUR | 2% | 58% |
| % compra fuerte | alto | 57 | -3.60 EUR | 4% | 56% |
| momentum 30d | bajo | 59 | -3.01 EUR | 3% | 53% |
| momentum 30d | medio | 59 | -3.92 EUR | 2% | 63% |
| momentum 30d | alto | 59 | -3.66 EUR | 3% | 61% |
| fuerza relativa | bajo | 59 | -3.36 EUR | 3% | 59% |
| fuerza relativa | medio | 59 | -3.76 EUR | 0% | 56% |
| fuerza relativa | alto | 59 | -3.47 EUR | 5% | 61% |
| RSI | bajo | 59 | -2.94 EUR | 5% | 54% |
| RSI | medio | 59 | -3.32 EUR | 2% | 56% |
| RSI | alto | 59 | -4.33 EUR | 2% | 66% |
| volumen relativo | bajo | 53 | -3.87 EUR | 4% | 64% |
| volumen relativo | medio | 53 | -2.69 EUR | 0% | 43% |
| volumen relativo | alto | 54 | -4.16 EUR | 4% | 63% |
| volatilidad | bajo | 53 | -4.28 EUR | 0% | 60% |
| volatilidad | medio | 53 | -4.03 EUR | 2% | 58% |
| volatilidad | alto | 54 | -2.44 EUR | 6% | 52% |
| liquidez | bajo | 53 | -3.51 EUR | 2% | 57% |
| liquidez | medio | 53 | -3.61 EUR | 4% | 60% |
| liquidez | alto | 54 | -3.61 EUR | 2% | 54% |
| distancia max 52s | bajo | 53 | -2.67 EUR | 6% | 53% |
| distancia max 52s | medio | 53 | -3.81 EUR | 0% | 58% |
| distancia max 52s | alto | 54 | -4.24 EUR | 2% | 59% |
| consenso | buy | 125 | -3.99 EUR | 2% | 62% |
| consenso | strong_buy | 52 | -2.43 EUR | 4% | 52% |
| tendencia tecnica | alcista | 99 | -3.74 EUR | 3% | 60% |
| tendencia tecnica | mixta | 46 | -2.96 EUR | 2% | 54% |
| tendencia tecnica | bajista | 32 | -3.68 EUR | 3% | 62% |
| tendencia analistas | mejorando | 84 | -3.49 EUR | 4% | 60% |
| tendencia analistas | estable | 56 | -4.37 EUR | 2% | 68% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 98 | -3.50 EUR | 4% | 62% |
| regimen de mercado | neutro | 79 | -3.57 EUR | 1% | 54% |
| catalizador | sin catalizador | 176 | -3.50 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.28 | -2.44 | **+1.84 EUR** |
| potencial hasta objetivo | -4.14 | -2.95 | **+1.19 EUR** |
| nota global | -3.84 | -2.66 | **+1.18 EUR** |
| % compra fuerte | -4.36 | -3.60 | **+0.76 EUR** |
| liquidez | -3.51 | -3.61 | **-0.09 EUR** |
| fuerza relativa | -3.36 | -3.47 | **-0.11 EUR** |
| volumen relativo | -3.87 | -4.16 | **-0.30 EUR** |
| momentum 30d | -3.01 | -3.66 | **-0.65 EUR** |
| dispersion | -2.34 | -3.39 | **-1.05 EUR** |
| RSI | -2.94 | -4.33 | **-1.39 EUR** |
| puesto en el ranking | -2.70 | -4.17 | **-1.47 EUR** |
| distancia max 52s | -2.67 | -4.24 | **-1.57 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
