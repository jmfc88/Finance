# Simulacion en paralelo

Actualizado: 2026-10-15 11:21 · dia 53 de ejecucion
Proxima revision de ponderacion en 7 dias.

- Operaciones cerradas: **185**
- Operaciones abiertas: 51

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 59 | 32% | +1.30 EUR |
| plano | 12 | 6% | -1.75 EUR |
| perdida | 68 | 37% | -7.25 EUR |
| nefasta | 41 | 22% | -6.75 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 44 | -2.22% | 2/44 (5%) | 8/44 | 9 |
| 11-20 | 48 | -3.46% | 2/48 (4%) | 3/48 | 9 |
| 21-30 | 93 | -4.25% | 1/93 (1%) | 6/93 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 1 | +1.00% | -1.68% | **+2.68%** | 1/1 (100%) |
| 11-20 | 2 | -8.08% | -0.20% | **-7.88%** | 0/2 (0%) |
| 21-30 | 9 | -3.76% | -0.37% | **-3.39%** | 4/9 (44%) |

**En conjunto:** -4.08% de media frente a -0.45% del indice, una diferencia de **-3.63%**. 5 de 12 operaciones (42%) batieron a su indice.

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
| escalera + stop vol x4 | -0.78% | 7 | -5.47 EUR | 0/7 | -6.59 EUR |
| trailing pegado (3%) | -2.95% | 56 | -165.04 EUR | 3/56 | -10.00 EUR |
| escalera + stop vol x2.5 | -3.42% | 12 | -40.99 EUR | 0/12 | -7.93 EUR |
| LA REAL (escalera 25/08) | -3.56% | 185 | -659.47 EUR | 5/185 | -8.08 EUR |
| arranca antes (+3%) | -4.05% | 51 | -206.40 EUR | 3/51 | -10.00 EUR |
| escalera + stop vol x3 | -4.20% | 12 | -50.45 EUR | 0/12 | -9.51 EUR |
| arranca despues (+8%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| actual (8% / +5% / 5%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| trailing suelto (7%) | -4.95% | 43 | -212.66 EUR | 2/43 | -10.00 EUR |
| sin trailing, solo stop | -5.35% | 42 | -224.72 EUR | 1/42 | -10.00 EUR |
| stop corto (5%) | -5.76% | 123 | -708.56 EUR | 3/123 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.56%**
- Aciertos (>= 5 EUR limpios): 5/185 (3%)
- Resultado acumulado ficticio: -659.47 EUR sobre 185 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 61 | -3.75 EUR | 0% | 54% |
| nota global | medio | 61 | -4.23 EUR | 3% | 67% |
| nota global | alto | 63 | -2.75 EUR | 5% | 56% |
| puesto en el ranking | bajo | 61 | -2.47 EUR | 7% | 52% |
| puesto en el ranking | medio | 61 | -3.93 EUR | 2% | 62% |
| puesto en el ranking | alto | 63 | -4.27 EUR | 0% | 62% |
| potencial hasta objetivo | bajo | 61 | -3.97 EUR | 3% | 57% |
| potencial hasta objetivo | medio | 61 | -3.65 EUR | 2% | 62% |
| potencial hasta objetivo | alto | 63 | -3.09 EUR | 3% | 57% |
| dispersion | bajo | 61 | -2.68 EUR | 5% | 52% |
| dispersion | medio | 61 | -4.62 EUR | 2% | 69% |
| dispersion | alto | 63 | -3.40 EUR | 2% | 56% |
| % compra fuerte | bajo | 58 | -4.28 EUR | 2% | 62% |
| % compra fuerte | medio | 58 | -2.97 EUR | 2% | 59% |
| % compra fuerte | alto | 58 | -3.68 EUR | 3% | 57% |
| momentum 30d | bajo | 61 | -3.32 EUR | 3% | 56% |
| momentum 30d | medio | 61 | -3.67 EUR | 2% | 61% |
| momentum 30d | alto | 63 | -3.69 EUR | 3% | 60% |
| fuerza relativa | bajo | 61 | -3.66 EUR | 3% | 62% |
| fuerza relativa | medio | 61 | -3.61 EUR | 0% | 54% |
| fuerza relativa | alto | 63 | -3.43 EUR | 5% | 60% |
| RSI | bajo | 61 | -3.11 EUR | 5% | 54% |
| RSI | medio | 61 | -3.33 EUR | 2% | 57% |
| RSI | alto | 63 | -4.24 EUR | 2% | 65% |
| volumen relativo | bajo | 56 | -3.77 EUR | 4% | 64% |
| volumen relativo | medio | 56 | -3.10 EUR | 0% | 46% |
| volumen relativo | alto | 56 | -3.97 EUR | 4% | 61% |
| volatilidad | bajo | 56 | -4.16 EUR | 0% | 61% |
| volatilidad | medio | 56 | -4.04 EUR | 2% | 57% |
| volatilidad | alto | 56 | -2.64 EUR | 5% | 54% |
| liquidez | bajo | 56 | -3.60 EUR | 2% | 57% |
| liquidez | medio | 56 | -3.69 EUR | 4% | 61% |
| liquidez | alto | 56 | -3.56 EUR | 2% | 54% |
| distancia max 52s | bajo | 56 | -2.75 EUR | 5% | 54% |
| distancia max 52s | medio | 56 | -3.88 EUR | 0% | 59% |
| distancia max 52s | alto | 56 | -4.21 EUR | 2% | 59% |
| consenso | buy | 131 | -3.95 EUR | 2% | 61% |
| consenso | strong_buy | 54 | -2.64 EUR | 4% | 54% |
| tendencia tecnica | alcista | 101 | -3.74 EUR | 3% | 59% |
| tendencia tecnica | mixta | 46 | -2.96 EUR | 2% | 54% |
| tendencia tecnica | bajista | 38 | -3.83 EUR | 3% | 63% |
| tendencia analistas | mejorando | 89 | -3.54 EUR | 3% | 60% |
| tendencia analistas | estable | 57 | -4.43 EUR | 2% | 68% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 102 | -3.56 EUR | 4% | 63% |
| regimen de mercado | neutro | 83 | -3.57 EUR | 1% | 54% |
| catalizador | sin catalizador | 184 | -3.54 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.16 | -2.64 | **+1.52 EUR** |
| nota global | -3.75 | -2.75 | **+1.00 EUR** |
| potencial hasta objetivo | -3.97 | -3.09 | **+0.88 EUR** |
| % compra fuerte | -4.28 | -3.68 | **+0.60 EUR** |
| fuerza relativa | -3.66 | -3.43 | **+0.23 EUR** |
| liquidez | -3.60 | -3.56 | **+0.04 EUR** |
| volumen relativo | -3.77 | -3.97 | **-0.21 EUR** |
| momentum 30d | -3.32 | -3.69 | **-0.37 EUR** |
| dispersion | -2.68 | -3.40 | **-0.73 EUR** |
| RSI | -3.11 | -4.24 | **-1.13 EUR** |
| distancia max 52s | -2.75 | -4.21 | **-1.46 EUR** |
| puesto en el ranking | -2.47 | -4.27 | **-1.81 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
