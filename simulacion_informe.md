# Simulacion en paralelo

Actualizado: 2026-10-21 11:42 · dia 59 de ejecucion
Proxima revision de ponderacion en 1 dia.

- Operaciones cerradas: **204**
- Operaciones abiertas: 53

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 3 | 1% | +16.90 EUR |
| beneficio | 3 | 1% | +7.07 EUR |
| flojo | 68 | 33% | +1.29 EUR |
| plano | 13 | 6% | -1.84 EUR |
| perdida | 73 | 36% | -7.20 EUR |
| nefasta | 44 | 22% | -6.84 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 47 | -1.97% | 3/47 (6%) | 9/47 | 10 |
| 11-20 | 54 | -3.30% | 2/54 (4%) | 3/54 | 8 |
| 21-30 | 103 | -4.08% | 1/103 (1%) | 7/103 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 4 | +1.56% | -1.85% | **+3.40%** | 2/4 (50%) |
| 11-20 | 8 | -3.54% | -0.56% | **-2.98%** | 4/8 (50%) |
| 21-30 | 18 | -2.80% | -0.90% | **-1.90%** | 9/18 (50%) |

**En conjunto:** -2.41% de media frente a -0.94% del indice, una diferencia de **-1.48%**. 15 de 30 operaciones (50%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 34 operaciones, media -2.60%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -1.83% | 24 | -43.97 EUR | 1/24 | -8.20 EUR |
| trailing pegado (3%) | -2.62% | 63 | -164.85 EUR | 4/63 | -10.00 EUR |
| escalera + stop vol x2.5 | -2.78% | 31 | -86.16 EUR | 1/31 | -7.93 EUR |
| escalera + stop vol x3 | -3.21% | 30 | -96.39 EUR | 1/30 | -9.51 EUR |
| LA REAL (escalera 25/08) | -3.39% | 204 | -690.96 EUR | 6/204 | -8.08 EUR |
| arranca antes (+3%) | -3.64% | 57 | -207.41 EUR | 4/57 | -10.00 EUR |
| arranca despues (+8%) | -3.74% | 51 | -190.53 EUR | 4/51 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.74% | 51 | -190.53 EUR | 4/51 | -10.00 EUR |
| trailing suelto (7%) | -4.36% | 49 | -213.67 EUR | 3/49 | -10.00 EUR |
| sin trailing, solo stop | -4.70% | 48 | -225.73 EUR | 2/48 | -10.00 EUR |
| stop corto (5%) | -5.56% | 135 | -750.92 EUR | 4/135 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.39%**
- Aciertos (>= 5 EUR limpios): 6/204 (3%)
- Resultado acumulado ficticio: -690.96 EUR sobre 204 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 68 | -3.62 EUR | 0% | 51% |
| nota global | medio | 68 | -4.00 EUR | 3% | 66% |
| nota global | alto | 68 | -2.54 EUR | 6% | 54% |
| puesto en el ranking | bajo | 68 | -2.21 EUR | 7% | 53% |
| puesto en el ranking | medio | 68 | -3.92 EUR | 1% | 60% |
| puesto en el ranking | alto | 68 | -4.03 EUR | 0% | 59% |
| potencial hasta objetivo | bajo | 68 | -3.70 EUR | 3% | 57% |
| potencial hasta objetivo | medio | 68 | -3.91 EUR | 1% | 62% |
| potencial hasta objetivo | alto | 68 | -2.55 EUR | 4% | 53% |
| dispersion | bajo | 68 | -2.60 EUR | 6% | 53% |
| dispersion | medio | 68 | -4.48 EUR | 1% | 68% |
| dispersion | alto | 68 | -3.08 EUR | 1% | 51% |
| % compra fuerte | bajo | 63 | -4.24 EUR | 2% | 62% |
| % compra fuerte | medio | 63 | -3.00 EUR | 2% | 57% |
| % compra fuerte | alto | 65 | -3.37 EUR | 3% | 54% |
| momentum 30d | bajo | 68 | -3.17 EUR | 4% | 54% |
| momentum 30d | medio | 68 | -3.29 EUR | 1% | 57% |
| momentum 30d | alto | 68 | -3.70 EUR | 3% | 60% |
| fuerza relativa | bajo | 68 | -3.31 EUR | 4% | 59% |
| fuerza relativa | medio | 68 | -3.36 EUR | 0% | 53% |
| fuerza relativa | alto | 68 | -3.49 EUR | 4% | 60% |
| RSI | bajo | 68 | -2.71 EUR | 6% | 51% |
| RSI | medio | 68 | -3.44 EUR | 1% | 57% |
| RSI | alto | 68 | -4.01 EUR | 1% | 63% |
| volumen relativo | bajo | 62 | -3.44 EUR | 5% | 63% |
| volumen relativo | medio | 62 | -2.92 EUR | 0% | 45% |
| volumen relativo | alto | 63 | -3.88 EUR | 3% | 59% |
| volatilidad | bajo | 62 | -3.69 EUR | 0% | 55% |
| volatilidad | medio | 62 | -3.80 EUR | 3% | 58% |
| volatilidad | alto | 63 | -2.77 EUR | 5% | 54% |
| liquidez | bajo | 62 | -3.79 EUR | 2% | 58% |
| liquidez | medio | 62 | -2.82 EUR | 5% | 55% |
| liquidez | alto | 63 | -3.63 EUR | 2% | 54% |
| distancia max 52s | bajo | 62 | -2.34 EUR | 6% | 50% |
| distancia max 52s | medio | 62 | -3.61 EUR | 0% | 56% |
| distancia max 52s | alto | 63 | -4.29 EUR | 2% | 60% |
| consenso | buy | 145 | -3.68 EUR | 2% | 58% |
| consenso | strong_buy | 59 | -2.67 EUR | 5% | 56% |
| tendencia tecnica | alcista | 105 | -3.64 EUR | 3% | 59% |
| tendencia tecnica | mixta | 54 | -3.12 EUR | 2% | 54% |
| tendencia tecnica | bajista | 45 | -3.12 EUR | 4% | 58% |
| tendencia analistas | mejorando | 101 | -3.41 EUR | 3% | 57% |
| tendencia analistas | estable | 61 | -3.83 EUR | 3% | 64% |
| tendencia analistas | empeorando | 9 | -4.67 EUR | 0% | 78% |
| regimen de mercado | favorable | 105 | -3.52 EUR | 4% | 62% |
| regimen de mercado | neutro | 99 | -3.25 EUR | 2% | 53% |
| catalizador | sin catalizador | 203 | -3.36 EUR | 3% | 57% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.70 | -2.55 | **+1.15 EUR** |
| nota global | -3.62 | -2.54 | **+1.08 EUR** |
| volatilidad | -3.69 | -2.77 | **+0.92 EUR** |
| % compra fuerte | -4.24 | -3.37 | **+0.87 EUR** |
| liquidez | -3.79 | -3.63 | **+0.17 EUR** |
| fuerza relativa | -3.31 | -3.49 | **-0.19 EUR** |
| volumen relativo | -3.44 | -3.88 | **-0.43 EUR** |
| dispersion | -2.60 | -3.08 | **-0.48 EUR** |
| momentum 30d | -3.17 | -3.70 | **-0.53 EUR** |
| RSI | -2.71 | -4.01 | **-1.30 EUR** |
| puesto en el ranking | -2.21 | -4.03 | **-1.82 EUR** |
| distancia max 52s | -2.34 | -4.29 | **-1.95 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
