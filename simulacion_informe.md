# Simulacion en paralelo

Actualizado: 2026-11-03 17:04 · dia 72 de ejecucion
Proxima revision de ponderacion en 3 dias.

- Operaciones cerradas: **263**
- Operaciones abiertas: 64

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 2% | +16.71 EUR |
| beneficio | 7 | 3% | +7.86 EUR |
| flojo | 94 | 36% | +1.32 EUR |
| plano | 17 | 6% | -1.72 EUR |
| perdida | 84 | 32% | -7.19 EUR |
| nefasta | 57 | 22% | -7.12 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 54 | -2.29% | 3/54 (6%) | 9/54 | 10 |
| 11-20 | 67 | -3.01% | 4/67 (6%) | 8/67 | 9 |
| 21-30 | 142 | -3.30% | 4/142 (3%) | 15/142 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 10 | -1.66% | -1.25% | **-0.42%** | 3/10 (30%) |
| 11-20 | 20 | -2.17% | -1.14% | **-1.03%** | 11/20 (55%) |
| 21-30 | 53 | -1.27% | -0.79% | **-0.47%** | 30/53 (57%) |

**En conjunto:** -1.53% de media frente a -0.93% del indice, una diferencia de **-0.60%**. 44 de 83 operaciones (53%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 48 operaciones, media -1.23%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -1.59% | 77 | -122.22 EUR | 6/77 | -10.91 EUR |
| escalera + stop vol x2.5 | -2.06% | 90 | -185.37 EUR | 4/90 | -10.63 EUR |
| trailing pegado (3%) | -2.29% | 99 | -226.44 EUR | 9/99 | -10.00 EUR |
| escalera + stop vol x3 | -2.45% | 89 | -217.84 EUR | 4/89 | -12.76 EUR |
| LA REAL (escalera 25/08) | -3.02% | 263 | -794.09 EUR | 11/263 | -8.08 EUR |
| arranca antes (+3%) | -3.25% | 88 | -286.32 EUR | 8/88 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.43% | 82 | -281.60 EUR | 8/82 | -10.00 EUR |
| arranca despues (+8%) | -3.53% | 79 | -279.19 EUR | 8/79 | -10.00 EUR |
| trailing suelto (7%) | -3.97% | 78 | -309.72 EUR | 7/78 | -10.00 EUR |
| sin trailing, solo stop | -4.27% | 74 | -316.34 EUR | 6/74 | -10.00 EUR |
| stop corto (5%) | -5.09% | 176 | -895.35 EUR | 8/176 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.02%**
- Aciertos (>= 5 EUR limpios): 11/263 (4%)
- Resultado acumulado ficticio: -794.09 EUR sobre 263 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 87 | -2.57 EUR | 3% | 45% |
| nota global | medio | 87 | -3.84 EUR | 2% | 60% |
| nota global | alto | 89 | -2.65 EUR | 7% | 56% |
| puesto en el ranking | bajo | 87 | -2.44 EUR | 7% | 54% |
| puesto en el ranking | medio | 87 | -3.74 EUR | 2% | 57% |
| puesto en el ranking | alto | 89 | -2.88 EUR | 3% | 49% |
| potencial hasta objetivo | bajo | 87 | -3.24 EUR | 5% | 54% |
| potencial hasta objetivo | medio | 87 | -3.50 EUR | 3% | 59% |
| potencial hasta objetivo | alto | 89 | -2.33 EUR | 4% | 48% |
| dispersion | bajo | 87 | -2.72 EUR | 6% | 55% |
| dispersion | medio | 87 | -3.33 EUR | 5% | 55% |
| dispersion | alto | 89 | -3.01 EUR | 2% | 51% |
| % compra fuerte | bajo | 81 | -3.40 EUR | 2% | 54% |
| % compra fuerte | medio | 81 | -2.53 EUR | 6% | 54% |
| % compra fuerte | alto | 83 | -3.32 EUR | 2% | 52% |
| momentum 30d | bajo | 87 | -3.37 EUR | 5% | 56% |
| momentum 30d | medio | 87 | -2.77 EUR | 2% | 49% |
| momentum 30d | alto | 89 | -2.92 EUR | 6% | 55% |
| fuerza relativa | bajo | 87 | -3.35 EUR | 3% | 56% |
| fuerza relativa | medio | 87 | -2.78 EUR | 3% | 49% |
| fuerza relativa | alto | 89 | -2.92 EUR | 6% | 55% |
| RSI | bajo | 87 | -2.60 EUR | 6% | 49% |
| RSI | medio | 87 | -3.02 EUR | 3% | 54% |
| RSI | alto | 89 | -3.44 EUR | 3% | 57% |
| volumen relativo | bajo | 82 | -2.64 EUR | 7% | 54% |
| volumen relativo | medio | 82 | -2.91 EUR | 1% | 48% |
| volumen relativo | alto | 82 | -3.49 EUR | 4% | 55% |
| volatilidad | bajo | 82 | -2.98 EUR | 5% | 50% |
| volatilidad | medio | 82 | -3.09 EUR | 4% | 52% |
| volatilidad | alto | 82 | -2.97 EUR | 4% | 54% |
| liquidez | bajo | 82 | -3.30 EUR | 2% | 54% |
| liquidez | medio | 82 | -2.86 EUR | 5% | 52% |
| liquidez | alto | 82 | -2.89 EUR | 5% | 50% |
| distancia max 52s | bajo | 82 | -2.65 EUR | 4% | 48% |
| distancia max 52s | medio | 82 | -2.75 EUR | 4% | 52% |
| distancia max 52s | alto | 82 | -3.65 EUR | 5% | 56% |
| consenso | buy | 181 | -3.13 EUR | 4% | 53% |
| consenso | strong_buy | 82 | -2.78 EUR | 5% | 55% |
| tendencia tecnica | alcista | 122 | -3.16 EUR | 5% | 55% |
| tendencia tecnica | mixta | 73 | -3.27 EUR | 3% | 56% |
| tendencia tecnica | bajista | 68 | -2.49 EUR | 4% | 49% |
| tendencia analistas | mejorando | 128 | -3.02 EUR | 3% | 52% |
| tendencia analistas | estable | 84 | -3.31 EUR | 6% | 58% |
| tendencia analistas | empeorando | 11 | -4.47 EUR | 0% | 73% |
| regimen de mercado | neutro | 139 | -2.67 EUR | 5% | 49% |
| regimen de mercado | favorable | 114 | -3.40 EUR | 4% | 60% |
| regimen de mercado | adverso | 10 | -3.54 EUR | 0% | 50% |
| catalizador | sin catalizador | 261 | -2.98 EUR | 4% | 53% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -3.24 | -2.33 | **+0.91 EUR** |
| momentum 30d | -3.37 | -2.92 | **+0.46 EUR** |
| fuerza relativa | -3.35 | -2.92 | **+0.43 EUR** |
| liquidez | -3.30 | -2.89 | **+0.41 EUR** |
| % compra fuerte | -3.40 | -3.32 | **+0.08 EUR** |
| volatilidad | -2.98 | -2.97 | **+0.00 EUR** |
| nota global | -2.57 | -2.65 | **-0.08 EUR** |
| dispersion | -2.72 | -3.01 | **-0.29 EUR** |
| puesto en el ranking | -2.44 | -2.88 | **-0.44 EUR** |
| RSI | -2.60 | -3.44 | **-0.84 EUR** |
| volumen relativo | -2.64 | -3.49 | **-0.85 EUR** |
| distancia max 52s | -2.65 | -3.65 | **-1.00 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
