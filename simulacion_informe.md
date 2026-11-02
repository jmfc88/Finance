# Simulacion en paralelo

Actualizado: 2026-11-02 19:30 · dia 71 de ejecucion
Proxima revision de ponderacion en 4 dias.

- Operaciones cerradas: **257**
- Operaciones abiertas: 65

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 2% | +16.71 EUR |
| beneficio | 5 | 2% | +7.59 EUR |
| flojo | 90 | 35% | +1.33 EUR |
| plano | 17 | 7% | -1.72 EUR |
| perdida | 84 | 33% | -7.19 EUR |
| nefasta | 57 | 22% | -7.12 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 53 | -2.35% | 3/53 (6%) | 9/53 | 10 |
| 11-20 | 65 | -3.20% | 3/65 (5%) | 7/65 | 9 |
| 21-30 | 139 | -3.47% | 3/139 (2%) | 13/139 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 9 | -1.96% | -1.58% | **-0.38%** | 3/9 (33%) |
| 11-20 | 18 | -2.77% | -1.08% | **-1.68%** | 9/18 (50%) |
| 21-30 | 50 | -1.61% | -0.86% | **-0.75%** | 28/50 (56%) |

**En conjunto:** -1.92% de media frente a -1.00% del indice, una diferencia de **-0.93%**. 40 de 77 operaciones (52%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 46 operaciones, media -1.65%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -2.02% | 71 | -143.32 EUR | 4/71 | -10.91 EUR |
| escalera + stop vol x2.5 | -2.28% | 84 | -191.87 EUR | 3/84 | -10.63 EUR |
| trailing pegado (3%) | -2.57% | 96 | -246.27 EUR | 7/96 | -10.00 EUR |
| escalera + stop vol x3 | -2.70% | 83 | -223.93 EUR | 3/83 | -12.76 EUR |
| LA REAL (escalera 25/08) | -3.17% | 257 | -815.19 EUR | 9/257 | -8.08 EUR |
| arranca antes (+3%) | -3.58% | 85 | -303.99 EUR | 6/85 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.79% | 79 | -299.27 EUR | 6/79 | -10.00 EUR |
| arranca despues (+8%) | -3.85% | 77 | -296.29 EUR | 6/77 | -10.00 EUR |
| trailing suelto (7%) | -4.30% | 76 | -326.82 EUR | 5/76 | -10.00 EUR |
| sin trailing, solo stop | -4.63% | 72 | -333.44 EUR | 4/72 | -10.00 EUR |
| stop corto (5%) | -5.28% | 173 | -913.02 EUR | 6/173 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.17%**
- Aciertos (>= 5 EUR limpios): 9/257 (4%)
- Resultado acumulado ficticio: -815.19 EUR sobre 257 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 85 | -2.78 EUR | 2% | 46% |
| nota global | medio | 85 | -3.96 EUR | 2% | 61% |
| nota global | alto | 87 | -2.79 EUR | 6% | 57% |
| puesto en el ranking | bajo | 85 | -2.58 EUR | 6% | 56% |
| puesto en el ranking | medio | 85 | -3.85 EUR | 2% | 58% |
| puesto en el ranking | alto | 87 | -3.09 EUR | 2% | 51% |
| potencial hasta objetivo | bajo | 85 | -3.34 EUR | 5% | 55% |
| potencial hasta objetivo | medio | 85 | -3.66 EUR | 2% | 60% |
| potencial hasta objetivo | alto | 87 | -2.53 EUR | 3% | 49% |
| dispersion | bajo | 85 | -2.75 EUR | 6% | 55% |
| dispersion | medio | 85 | -3.55 EUR | 4% | 58% |
| dispersion | alto | 87 | -3.22 EUR | 1% | 52% |
| % compra fuerte | bajo | 79 | -3.63 EUR | 3% | 57% |
| % compra fuerte | medio | 79 | -2.69 EUR | 4% | 54% |
| % compra fuerte | alto | 81 | -3.43 EUR | 2% | 53% |
| momentum 30d | bajo | 85 | -3.60 EUR | 4% | 58% |
| momentum 30d | medio | 85 | -2.91 EUR | 1% | 51% |
| momentum 30d | alto | 87 | -3.01 EUR | 6% | 56% |
| fuerza relativa | bajo | 85 | -3.52 EUR | 2% | 56% |
| fuerza relativa | medio | 85 | -2.98 EUR | 2% | 52% |
| fuerza relativa | alto | 87 | -3.01 EUR | 6% | 56% |
| RSI | bajo | 85 | -2.84 EUR | 5% | 51% |
| RSI | medio | 85 | -3.08 EUR | 4% | 55% |
| RSI | alto | 87 | -3.59 EUR | 2% | 59% |
| volumen relativo | bajo | 80 | -2.74 EUR | 8% | 55% |
| volumen relativo | medio | 80 | -3.26 EUR | 0% | 50% |
| volumen relativo | alto | 80 | -3.55 EUR | 2% | 55% |
| volatilidad | bajo | 80 | -3.10 EUR | 4% | 51% |
| volatilidad | medio | 80 | -3.33 EUR | 2% | 54% |
| volatilidad | alto | 80 | -3.10 EUR | 4% | 55% |
| liquidez | bajo | 80 | -3.30 EUR | 2% | 54% |
| liquidez | medio | 80 | -3.20 EUR | 4% | 55% |
| liquidez | alto | 80 | -3.04 EUR | 4% | 51% |
| distancia max 52s | bajo | 80 | -2.88 EUR | 2% | 49% |
| distancia max 52s | medio | 80 | -2.84 EUR | 4% | 54% |
| distancia max 52s | alto | 80 | -3.82 EUR | 4% | 57% |
| consenso | buy | 177 | -3.28 EUR | 3% | 54% |
| consenso | strong_buy | 80 | -2.93 EUR | 4% | 56% |
| tendencia tecnica | alcista | 118 | -3.34 EUR | 4% | 57% |
| tendencia tecnica | mixta | 73 | -3.27 EUR | 3% | 56% |
| tendencia tecnica | bajista | 66 | -2.76 EUR | 3% | 50% |
| tendencia analistas | mejorando | 125 | -3.20 EUR | 2% | 54% |
| tendencia analistas | estable | 81 | -3.53 EUR | 5% | 60% |
| tendencia analistas | empeorando | 11 | -4.47 EUR | 0% | 73% |
| regimen de mercado | neutro | 136 | -2.86 EUR | 4% | 50% |
| regimen de mercado | favorable | 113 | -3.44 EUR | 4% | 60% |
| regimen de mercado | adverso | 8 | -4.67 EUR | 0% | 62% |
| catalizador | sin catalizador | 255 | -3.13 EUR | 4% | 55% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.34 | -2.53 | **+0.81 EUR** |
| momentum 30d | -3.60 | -3.01 | **+0.60 EUR** |
| fuerza relativa | -3.52 | -3.01 | **+0.51 EUR** |
| liquidez | -3.30 | -3.04 | **+0.25 EUR** |
| % compra fuerte | -3.63 | -3.43 | **+0.20 EUR** |
| nota global | -2.78 | -2.79 | **-0.00 EUR** |
| volatilidad | -3.10 | -3.10 | **-0.01 EUR** |
| dispersion | -2.75 | -3.22 | **-0.48 EUR** |
| puesto en el ranking | -2.58 | -3.09 | **-0.52 EUR** |
| RSI | -2.84 | -3.59 | **-0.75 EUR** |
| volumen relativo | -2.74 | -3.55 | **-0.81 EUR** |
| distancia max 52s | -2.88 | -3.82 | **-0.95 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
