# Simulacion en paralelo

Actualizado: 2026-11-05 01:29 · dia 74 de ejecucion
Proxima revision de ponderacion en 1 dia.

- Operaciones cerradas: **273**
- Operaciones abiertas: 64

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 8 | 3% | +8.02 EUR |
| flojo | 98 | 36% | +1.30 EUR |
| plano | 18 | 7% | -1.74 EUR |
| perdida | 86 | 32% | -7.17 EUR |
| nefasta | 59 | 22% | -7.16 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 55 | -2.08% | 4/55 (7%) | 10/55 | 10 |
| 11-20 | 69 | -2.97% | 4/69 (6%) | 8/69 | 10 |
| 21-30 | 149 | -3.30% | 4/149 (3%) | 15/149 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 11 | -0.69% | -1.01% | **+0.33%** | 4/11 (36%) |
| 11-20 | 22 | -2.12% | -0.93% | **-1.20%** | 12/22 (55%) |
| 21-30 | 60 | -1.51% | -0.43% | **-1.07%** | 30/60 (50%) |

**En conjunto:** -1.56% de media frente a -0.62% del indice, una diferencia de **-0.94%**. 46 de 93 operaciones (49%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 50 operaciones, media -1.31%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -1.55% | 86 | -133.19 EUR | 7/86 | -10.91 EUR |
| escalera + stop vol x2.5 | -2.10% | 100 | -210.38 EUR | 5/100 | -10.63 EUR |
| trailing pegado (3%) | -2.24% | 104 | -232.68 EUR | 10/104 | -10.00 EUR |
| escalera + stop vol x3 | -2.36% | 98 | -231.40 EUR | 5/98 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.97% | 273 | -811.69 EUR | 12/273 | -8.08 EUR |
| arranca antes (+3%) | -3.18% | 92 | -292.74 EUR | 9/92 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.35% | 86 | -288.49 EUR | 9/86 | -10.00 EUR |
| arranca despues (+8%) | -3.45% | 83 | -286.08 EUR | 9/83 | -10.00 EUR |
| trailing suelto (7%) | -3.86% | 82 | -316.61 EUR | 8/82 | -10.00 EUR |
| sin trailing, solo stop | -4.14% | 78 | -323.23 EUR | 7/78 | -10.00 EUR |
| stop corto (5%) | -5.02% | 182 | -913.24 EUR | 9/182 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.97%**
- Aciertos (>= 5 EUR limpios): 12/273 (4%)
- Resultado acumulado ficticio: -811.69 EUR sobre 273 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 91 | -2.63 EUR | 3% | 45% |
| nota global | medio | 91 | -3.85 EUR | 2% | 59% |
| nota global | alto | 91 | -2.44 EUR | 8% | 55% |
| puesto en el ranking | bajo | 91 | -2.26 EUR | 8% | 54% |
| puesto en el ranking | medio | 91 | -3.78 EUR | 2% | 57% |
| puesto en el ranking | alto | 91 | -2.88 EUR | 3% | 48% |
| potencial hasta objetivo | bajo | 91 | -3.29 EUR | 4% | 54% |
| potencial hasta objetivo | medio | 91 | -3.40 EUR | 3% | 57% |
| potencial hasta objetivo | alto | 91 | -2.23 EUR | 5% | 48% |
| dispersion | bajo | 91 | -2.63 EUR | 7% | 55% |
| dispersion | medio | 91 | -3.37 EUR | 4% | 55% |
| dispersion | alto | 91 | -2.92 EUR | 2% | 49% |
| % compra fuerte | bajo | 84 | -3.46 EUR | 2% | 55% |
| % compra fuerte | medio | 84 | -2.44 EUR | 6% | 52% |
| % compra fuerte | alto | 86 | -3.18 EUR | 3% | 51% |
| momentum 30d | bajo | 91 | -3.25 EUR | 5% | 56% |
| momentum 30d | medio | 91 | -2.56 EUR | 3% | 47% |
| momentum 30d | alto | 91 | -3.10 EUR | 4% | 56% |
| fuerza relativa | bajo | 91 | -3.42 EUR | 3% | 57% |
| fuerza relativa | medio | 91 | -2.63 EUR | 4% | 48% |
| fuerza relativa | alto | 91 | -2.87 EUR | 5% | 54% |
| RSI | bajo | 91 | -2.51 EUR | 7% | 49% |
| RSI | medio | 91 | -2.94 EUR | 3% | 54% |
| RSI | alto | 91 | -3.47 EUR | 3% | 56% |
| volumen relativo | bajo | 85 | -2.42 EUR | 8% | 52% |
| volumen relativo | medio | 85 | -2.98 EUR | 1% | 48% |
| volumen relativo | alto | 86 | -3.49 EUR | 3% | 55% |
| volatilidad | bajo | 85 | -2.84 EUR | 5% | 48% |
| volatilidad | medio | 85 | -3.05 EUR | 4% | 52% |
| volatilidad | alto | 86 | -3.01 EUR | 5% | 55% |
| liquidez | bajo | 85 | -3.35 EUR | 2% | 54% |
| liquidez | medio | 85 | -2.51 EUR | 6% | 49% |
| liquidez | alto | 86 | -3.04 EUR | 5% | 51% |
| distancia max 52s | bajo | 85 | -2.63 EUR | 4% | 47% |
| distancia max 52s | medio | 85 | -2.58 EUR | 5% | 52% |
| distancia max 52s | alto | 86 | -3.68 EUR | 5% | 56% |
| consenso | buy | 188 | -3.09 EUR | 4% | 52% |
| consenso | strong_buy | 85 | -2.72 EUR | 6% | 55% |
| tendencia tecnica | alcista | 126 | -3.20 EUR | 5% | 55% |
| tendencia tecnica | mixta | 76 | -3.07 EUR | 4% | 55% |
| tendencia tecnica | bajista | 71 | -2.47 EUR | 4% | 48% |
| tendencia analistas | mejorando | 130 | -2.95 EUR | 3% | 52% |
| tendencia analistas | estable | 89 | -3.38 EUR | 6% | 58% |
| tendencia analistas | empeorando | 12 | -3.34 EUR | 8% | 67% |
| regimen de mercado | neutro | 144 | -2.54 EUR | 6% | 48% |
| regimen de mercado | favorable | 114 | -3.40 EUR | 4% | 60% |
| regimen de mercado | adverso | 15 | -3.84 EUR | 0% | 53% |
| catalizador | sin catalizador | 271 | -2.94 EUR | 4% | 53% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.29 | -2.23 | **+1.06 EUR** |
| fuerza relativa | -3.42 | -2.87 | **+0.55 EUR** |
| liquidez | -3.35 | -3.04 | **+0.31 EUR** |
| % compra fuerte | -3.46 | -3.18 | **+0.28 EUR** |
| nota global | -2.63 | -2.44 | **+0.19 EUR** |
| momentum 30d | -3.25 | -3.10 | **+0.15 EUR** |
| volatilidad | -2.84 | -3.01 | **-0.17 EUR** |
| dispersion | -2.63 | -2.92 | **-0.30 EUR** |
| puesto en el ranking | -2.26 | -2.88 | **-0.62 EUR** |
| RSI | -2.51 | -3.47 | **-0.96 EUR** |
| distancia max 52s | -2.63 | -3.68 | **-1.05 EUR** |
| volumen relativo | -2.42 | -3.49 | **-1.07 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
