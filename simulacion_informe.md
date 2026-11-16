# Simulacion en paralelo

Actualizado: 2026-11-16 07:57 · dia 85 de ejecucion
Proxima revision de ponderacion en 5 dias.

- Operaciones cerradas: **343**
- Operaciones abiertas: 67

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 14 | 4% | +8.78 EUR |
| flojo | 149 | 43% | +1.28 EUR |
| plano | 18 | 5% | -1.74 EUR |
| perdida | 89 | 26% | -7.20 EUR |
| nefasta | 69 | 20% | -7.29 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 66 | -1.61% | 5/66 (8%) | 14/66 | 10 |
| 11-20 | 86 | -2.45% | 6/86 (7%) | 14/86 | 9 |
| 21-30 | 191 | -2.50% | 7/191 (4%) | 28/191 | 8 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 22 | +0.02% | +0.18% | **-0.16%** | 11/22 (50%) |
| 11-20 | 36 | -0.79% | -0.26% | **-0.53%** | 21/36 (58%) |
| 21-30 | 101 | -0.66% | -0.03% | **-0.63%** | 51/101 (50%) |

**En conjunto:** -0.60% de media frente a -0.05% del indice, una diferencia de **-0.54%**. 83 de 159 operaciones (52%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 52 operaciones, media -0.87%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.60% | 151 | -90.04 EUR | 13/151 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.25% | 167 | -208.70 EUR | 11/167 | -10.63 EUR |
| escalera + stop vol x3 | -1.31% | 163 | -213.67 EUR | 11/163 | -12.76 EUR |
| trailing pegado (3%) | -1.66% | 131 | -217.01 EUR | 16/131 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.32% | 343 | -794.28 EUR | 18/343 | -8.08 EUR |
| arranca antes (+3%) | -3.01% | 111 | -334.57 EUR | 12/111 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.14% | 102 | -320.40 EUR | 12/102 | -10.00 EUR |
| arranca despues (+8%) | -3.34% | 93 | -310.27 EUR | 12/93 | -10.00 EUR |
| trailing suelto (7%) | -3.79% | 92 | -349.02 EUR | 11/92 | -10.00 EUR |
| sin trailing, solo stop | -4.22% | 86 | -363.32 EUR | 9/86 | -10.00 EUR |
| stop corto (5%) | -4.78% | 207 | -990.15 EUR | 12/207 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.32%**
- Aciertos (>= 5 EUR limpios): 18/343 (5%)
- Resultado acumulado ficticio: -794.28 EUR sobre 343 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 114 | -1.54 EUR | 4% | 34% |
| nota global | medio | 114 | -3.45 EUR | 3% | 54% |
| nota global | alto | 115 | -1.96 EUR | 9% | 50% |
| puesto en el ranking | bajo | 114 | -2.05 EUR | 7% | 48% |
| puesto en el ranking | medio | 114 | -2.65 EUR | 5% | 48% |
| puesto en el ranking | alto | 115 | -2.25 EUR | 3% | 42% |
| potencial hasta objetivo | bajo | 114 | -2.71 EUR | 4% | 47% |
| potencial hasta objetivo | medio | 114 | -2.55 EUR | 4% | 47% |
| potencial hasta objetivo | alto | 115 | -1.70 EUR | 8% | 43% |
| dispersion | bajo | 114 | -2.17 EUR | 7% | 48% |
| dispersion | medio | 114 | -2.56 EUR | 4% | 46% |
| dispersion | alto | 115 | -2.22 EUR | 4% | 43% |
| % compra fuerte | bajo | 107 | -2.85 EUR | 3% | 48% |
| % compra fuerte | medio | 107 | -1.80 EUR | 8% | 46% |
| % compra fuerte | alto | 109 | -2.37 EUR | 4% | 43% |
| momentum 30d | bajo | 114 | -2.37 EUR | 7% | 48% |
| momentum 30d | medio | 114 | -2.09 EUR | 4% | 43% |
| momentum 30d | alto | 115 | -2.49 EUR | 4% | 47% |
| fuerza relativa | bajo | 114 | -2.57 EUR | 6% | 52% |
| fuerza relativa | medio | 114 | -2.15 EUR | 4% | 42% |
| fuerza relativa | alto | 115 | -2.22 EUR | 5% | 44% |
| RSI | bajo | 114 | -2.40 EUR | 6% | 49% |
| RSI | medio | 114 | -2.30 EUR | 7% | 47% |
| RSI | alto | 115 | -2.25 EUR | 3% | 42% |
| volumen relativo | bajo | 108 | -1.84 EUR | 9% | 45% |
| volumen relativo | medio | 108 | -2.32 EUR | 3% | 43% |
| volumen relativo | alto | 110 | -2.66 EUR | 4% | 45% |
| volatilidad | bajo | 108 | -2.08 EUR | 6% | 42% |
| volatilidad | medio | 108 | -2.35 EUR | 6% | 45% |
| volatilidad | alto | 110 | -2.40 EUR | 4% | 46% |
| liquidez | bajo | 108 | -2.65 EUR | 5% | 48% |
| liquidez | medio | 108 | -2.19 EUR | 6% | 44% |
| liquidez | alto | 110 | -1.99 EUR | 5% | 41% |
| distancia max 52s | bajo | 108 | -1.72 EUR | 6% | 40% |
| distancia max 52s | medio | 108 | -1.99 EUR | 6% | 44% |
| distancia max 52s | alto | 110 | -3.11 EUR | 4% | 49% |
| consenso | buy | 240 | -2.32 EUR | 5% | 45% |
| consenso | strong_buy | 103 | -2.32 EUR | 6% | 50% |
| tendencia tecnica | alcista | 159 | -2.70 EUR | 4% | 48% |
| tendencia tecnica | mixta | 99 | -2.37 EUR | 5% | 47% |
| tendencia tecnica | bajista | 85 | -1.53 EUR | 7% | 40% |
| tendencia analistas | mejorando | 156 | -2.29 EUR | 4% | 45% |
| tendencia analistas | estable | 115 | -2.63 EUR | 8% | 51% |
| tendencia analistas | empeorando | 14 | -2.72 EUR | 7% | 57% |
| regimen de mercado | neutro | 171 | -1.98 EUR | 7% | 43% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 57 | -1.22 EUR | 4% | 28% |
| catalizador | con catalizador | 12 | -0.60 EUR | 8% | 25% |
| catalizador | sin catalizador | 331 | -2.38 EUR | 5% | 47% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.71 | -1.70 | **+1.01 EUR** |
| liquidez | -2.65 | -1.99 | **+0.66 EUR** |
| % compra fuerte | -2.85 | -2.37 | **+0.47 EUR** |
| fuerza relativa | -2.57 | -2.22 | **+0.35 EUR** |
| RSI | -2.40 | -2.25 | **+0.15 EUR** |
| dispersion | -2.17 | -2.22 | **-0.05 EUR** |
| momentum 30d | -2.37 | -2.49 | **-0.12 EUR** |
| puesto en el ranking | -2.05 | -2.25 | **-0.21 EUR** |
| volatilidad | -2.08 | -2.40 | **-0.32 EUR** |
| nota global | -1.54 | -1.96 | **-0.43 EUR** |
| volumen relativo | -1.84 | -2.66 | **-0.82 EUR** |
| distancia max 52s | -1.72 | -3.11 | **-1.39 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
