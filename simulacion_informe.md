# Simulacion en paralelo

Actualizado: 2026-10-14 21:41 · dia 52 de ejecucion
Proxima revision de ponderacion en 8 dias.

- Operaciones cerradas: **183**
- Operaciones abiertas: 51

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 58 | 32% | +1.31 EUR |
| plano | 12 | 7% | -1.75 EUR |
| perdida | 68 | 37% | -7.25 EUR |
| nefasta | 40 | 22% | -6.72 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 44 | -2.22% | 2/44 (5%) | 8/44 | 9 |
| 11-20 | 47 | -3.36% | 2/47 (4%) | 3/47 | 9 |
| 21-30 | 92 | -4.31% | 1/92 (1%) | 6/92 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 1 | +1.00% | -1.68% | **+2.68%** | 1/1 (100%) |
| 11-20 | 1 | -8.08% | +0.20% | **-8.28%** | 0/1 (0%) |
| 21-30 | 8 | -4.36% | -0.34% | **-4.02%** | 3/8 (38%) |

**En conjunto:** -4.19% de media frente a -0.42% del indice, una diferencia de **-3.78%**. 4 de 10 operaciones (40%) batieron a su indice.

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
| escalera + stop vol x4 | -1.08% | 6 | -6.47 EUR | 0/6 | -6.59 EUR |
| trailing pegado (3%) | -2.95% | 56 | -165.04 EUR | 3/56 | -10.00 EUR |
| escalera + stop vol x2.5 | -3.48% | 10 | -34.77 EUR | 0/10 | -7.93 EUR |
| LA REAL (escalera 25/08) | -3.56% | 183 | -652.39 EUR | 5/183 | -8.08 EUR |
| arranca antes (+3%) | -4.05% | 51 | -206.40 EUR | 3/51 | -10.00 EUR |
| arranca despues (+8%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| actual (8% / +5% / 5%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| escalera + stop vol x3 | -4.28% | 10 | -42.78 EUR | 0/10 | -9.51 EUR |
| trailing suelto (7%) | -4.95% | 43 | -212.66 EUR | 2/43 | -10.00 EUR |
| sin trailing, solo stop | -5.35% | 42 | -224.72 EUR | 1/42 | -10.00 EUR |
| stop corto (5%) | -5.75% | 122 | -701.56 EUR | 3/122 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.56%**
- Aciertos (>= 5 EUR limpios): 5/183 (3%)
- Resultado acumulado ficticio: -652.39 EUR sobre 183 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 61 | -3.79 EUR | 0% | 54% |
| nota global | medio | 61 | -4.07 EUR | 3% | 67% |
| nota global | alto | 61 | -2.83 EUR | 5% | 56% |
| puesto en el ranking | bajo | 61 | -2.47 EUR | 7% | 52% |
| puesto en el ranking | medio | 61 | -3.93 EUR | 2% | 62% |
| puesto en el ranking | alto | 61 | -4.30 EUR | 0% | 62% |
| potencial hasta objetivo | bajo | 61 | -3.97 EUR | 3% | 57% |
| potencial hasta objetivo | medio | 61 | -3.80 EUR | 2% | 64% |
| potencial hasta objetivo | alto | 61 | -2.93 EUR | 3% | 56% |
| dispersion | bajo | 61 | -2.53 EUR | 5% | 51% |
| dispersion | medio | 61 | -4.77 EUR | 2% | 70% |
| dispersion | alto | 61 | -3.40 EUR | 2% | 56% |
| % compra fuerte | bajo | 57 | -4.37 EUR | 2% | 63% |
| % compra fuerte | medio | 57 | -2.88 EUR | 2% | 58% |
| % compra fuerte | alto | 58 | -3.68 EUR | 3% | 57% |
| momentum 30d | bajo | 61 | -3.32 EUR | 3% | 56% |
| momentum 30d | medio | 61 | -3.72 EUR | 2% | 61% |
| momentum 30d | alto | 61 | -3.65 EUR | 3% | 61% |
| fuerza relativa | bajo | 61 | -3.66 EUR | 3% | 62% |
| fuerza relativa | medio | 61 | -3.61 EUR | 0% | 54% |
| fuerza relativa | alto | 61 | -3.43 EUR | 5% | 61% |
| RSI | bajo | 61 | -3.11 EUR | 5% | 56% |
| RSI | medio | 61 | -3.33 EUR | 2% | 56% |
| RSI | alto | 61 | -4.26 EUR | 2% | 66% |
| volumen relativo | bajo | 55 | -3.64 EUR | 4% | 64% |
| volumen relativo | medio | 55 | -3.22 EUR | 0% | 47% |
| volumen relativo | alto | 56 | -3.97 EUR | 4% | 61% |
| volatilidad | bajo | 55 | -4.26 EUR | 0% | 60% |
| volatilidad | medio | 55 | -4.18 EUR | 2% | 60% |
| volatilidad | alto | 56 | -2.43 EUR | 5% | 52% |
| liquidez | bajo | 55 | -3.52 EUR | 2% | 56% |
| liquidez | medio | 55 | -3.77 EUR | 4% | 62% |
| liquidez | alto | 56 | -3.56 EUR | 2% | 54% |
| distancia max 52s | bajo | 55 | -2.66 EUR | 5% | 53% |
| distancia max 52s | medio | 55 | -3.97 EUR | 0% | 60% |
| distancia max 52s | alto | 56 | -4.21 EUR | 2% | 59% |
| consenso | buy | 130 | -3.99 EUR | 2% | 62% |
| consenso | strong_buy | 53 | -2.53 EUR | 4% | 53% |
| tendencia tecnica | alcista | 101 | -3.74 EUR | 3% | 59% |
| tendencia tecnica | mixta | 46 | -2.96 EUR | 2% | 54% |
| tendencia tecnica | bajista | 36 | -3.85 EUR | 3% | 64% |
| tendencia analistas | mejorando | 88 | -3.59 EUR | 3% | 60% |
| tendencia analistas | estable | 56 | -4.37 EUR | 2% | 68% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 101 | -3.52 EUR | 4% | 62% |
| regimen de mercado | neutro | 82 | -3.62 EUR | 1% | 55% |
| catalizador | sin catalizador | 182 | -3.54 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.26 | -2.43 | **+1.82 EUR** |
| potencial hasta objetivo | -3.97 | -2.93 | **+1.04 EUR** |
| nota global | -3.79 | -2.83 | **+0.96 EUR** |
| % compra fuerte | -4.37 | -3.68 | **+0.69 EUR** |
| fuerza relativa | -3.66 | -3.43 | **+0.23 EUR** |
| liquidez | -3.52 | -3.56 | **-0.04 EUR** |
| momentum 30d | -3.32 | -3.65 | **-0.33 EUR** |
| volumen relativo | -3.64 | -3.97 | **-0.33 EUR** |
| dispersion | -2.53 | -3.40 | **-0.87 EUR** |
| RSI | -3.11 | -4.26 | **-1.15 EUR** |
| distancia max 52s | -2.66 | -4.21 | **-1.56 EUR** |
| puesto en el ranking | -2.47 | -4.30 | **-1.83 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
