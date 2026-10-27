# Simulacion en paralelo

Actualizado: 2026-10-27 00:27 · dia 65 de ejecucion
Proxima revision de ponderacion en 10 dias.

- Operaciones cerradas: **232**
- Operaciones abiertas: 64

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 1% | +16.90 EUR |
| beneficio | 4 | 2% | +7.57 EUR |
| flojo | 78 | 34% | +1.32 EUR |
| plano | 14 | 6% | -1.76 EUR |
| perdida | 79 | 34% | -7.22 EUR |
| nefasta | 54 | 23% | -7.07 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 50 | -2.07% | 3/50 (6%) | 9/50 | 10 |
| 11-20 | 60 | -3.15% | 3/60 (5%) | 6/60 | 9 |
| 21-30 | 122 | -4.10% | 1/122 (1%) | 9/122 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 7 | -0.68% | -1.72% | **+1.04%** | 3/7 (43%) |
| 11-20 | 14 | -2.78% | -0.91% | **-1.87%** | 7/14 (50%) |
| 21-30 | 34 | -3.14% | -1.18% | **-1.96%** | 17/34 (50%) |

**En conjunto:** -2.73% de media frente a -1.18% del indice, una diferencia de **-1.56%**. 27 de 55 operaciones (49%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 37 operaciones, media -2.43%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -2.60% | 48 | -124.91 EUR | 2/48 | -10.34 EUR |
| escalera + stop vol x2.5 | -2.67% | 59 | -157.74 EUR | 2/59 | -7.93 EUR |
| trailing pegado (3%) | -2.72% | 79 | -214.84 EUR | 5/79 | -10.00 EUR |
| escalera + stop vol x3 | -3.14% | 58 | -182.33 EUR | 2/58 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.42% | 232 | -793.18 EUR | 7/232 | -8.08 EUR |
| arranca antes (+3%) | -3.88% | 69 | -268.06 EUR | 4/69 | -10.00 EUR |
| actual (8% / +5% / 5%) | -4.18% | 63 | -263.34 EUR | 4/63 | -10.00 EUR |
| arranca despues (+8%) | -4.21% | 62 | -261.28 EUR | 4/62 | -10.00 EUR |
| trailing suelto (7%) | -4.78% | 60 | -286.59 EUR | 3/60 | -10.00 EUR |
| sin trailing, solo stop | -5.13% | 58 | -297.37 EUR | 2/58 | -10.00 EUR |
| stop corto (5%) | -5.60% | 155 | -867.99 EUR | 4/155 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.42%**
- Aciertos (>= 5 EUR limpios): 7/232 (3%)
- Resultado acumulado ficticio: -793.18 EUR sobre 232 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 77 | -3.55 EUR | 0% | 51% |
| nota global | medio | 77 | -4.04 EUR | 4% | 66% |
| nota global | alto | 78 | -2.68 EUR | 5% | 55% |
| puesto en el ranking | bajo | 77 | -2.33 EUR | 6% | 55% |
| puesto en el ranking | medio | 77 | -3.85 EUR | 3% | 58% |
| puesto en el ranking | alto | 78 | -4.07 EUR | 0% | 59% |
| potencial hasta objetivo | bajo | 77 | -3.76 EUR | 3% | 57% |
| potencial hasta objetivo | medio | 77 | -3.73 EUR | 3% | 61% |
| potencial hasta objetivo | alto | 78 | -2.77 EUR | 4% | 54% |
| dispersion | bajo | 77 | -2.86 EUR | 5% | 56% |
| dispersion | medio | 77 | -4.12 EUR | 3% | 64% |
| dispersion | alto | 78 | -3.28 EUR | 1% | 53% |
| % compra fuerte | bajo | 71 | -3.93 EUR | 1% | 59% |
| % compra fuerte | medio | 71 | -2.95 EUR | 3% | 56% |
| % compra fuerte | alto | 73 | -3.64 EUR | 3% | 56% |
| momentum 30d | bajo | 77 | -3.54 EUR | 4% | 58% |
| momentum 30d | medio | 77 | -3.40 EUR | 1% | 56% |
| momentum 30d | alto | 78 | -3.31 EUR | 4% | 58% |
| fuerza relativa | bajo | 77 | -3.75 EUR | 3% | 61% |
| fuerza relativa | medio | 77 | -3.33 EUR | 3% | 55% |
| fuerza relativa | alto | 78 | -3.17 EUR | 4% | 56% |
| RSI | bajo | 77 | -3.05 EUR | 5% | 55% |
| RSI | medio | 77 | -3.47 EUR | 3% | 57% |
| RSI | alto | 78 | -3.74 EUR | 1% | 60% |
| volumen relativo | bajo | 71 | -3.44 EUR | 6% | 62% |
| volumen relativo | medio | 71 | -3.28 EUR | 0% | 51% |
| volumen relativo | alto | 73 | -3.61 EUR | 3% | 55% |
| volatilidad | bajo | 71 | -3.42 EUR | 1% | 54% |
| volatilidad | medio | 71 | -3.67 EUR | 3% | 56% |
| volatilidad | alto | 73 | -3.25 EUR | 4% | 58% |
| liquidez | bajo | 71 | -3.51 EUR | 1% | 55% |
| liquidez | medio | 71 | -3.32 EUR | 4% | 58% |
| liquidez | alto | 73 | -3.51 EUR | 3% | 55% |
| distancia max 52s | bajo | 71 | -2.65 EUR | 6% | 52% |
| distancia max 52s | medio | 71 | -3.41 EUR | 1% | 56% |
| distancia max 52s | alto | 73 | -4.25 EUR | 1% | 59% |
| consenso | buy | 161 | -3.60 EUR | 2% | 57% |
| consenso | strong_buy | 71 | -3.00 EUR | 4% | 58% |
| tendencia tecnica | alcista | 112 | -3.61 EUR | 3% | 58% |
| tendencia tecnica | mixta | 66 | -3.31 EUR | 3% | 56% |
| tendencia tecnica | bajista | 54 | -3.16 EUR | 4% | 57% |
| tendencia analistas | mejorando | 112 | -3.47 EUR | 3% | 57% |
| tendencia analistas | estable | 74 | -3.77 EUR | 4% | 64% |
| tendencia analistas | empeorando | 9 | -4.67 EUR | 0% | 78% |
| regimen de mercado | neutro | 121 | -3.25 EUR | 2% | 53% |
| regimen de mercado | favorable | 108 | -3.48 EUR | 4% | 61% |
| catalizador | sin catalizador | 231 | -3.40 EUR | 3% | 57% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.76 | -2.77 | **+0.99 EUR** |
| nota global | -3.55 | -2.68 | **+0.87 EUR** |
| fuerza relativa | -3.75 | -3.17 | **+0.58 EUR** |
| % compra fuerte | -3.93 | -3.64 | **+0.30 EUR** |
| momentum 30d | -3.54 | -3.31 | **+0.23 EUR** |
| volatilidad | -3.42 | -3.25 | **+0.17 EUR** |
| liquidez | -3.51 | -3.51 | **+0.01 EUR** |
| volumen relativo | -3.44 | -3.61 | **-0.16 EUR** |
| dispersion | -2.86 | -3.28 | **-0.41 EUR** |
| RSI | -3.05 | -3.74 | **-0.69 EUR** |
| distancia max 52s | -2.65 | -4.25 | **-1.60 EUR** |
| puesto en el ranking | -2.33 | -4.07 | **-1.75 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
