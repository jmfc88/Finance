# Simulacion en paralelo

Actualizado: 2026-11-26 03:36 · dia 95 de ejecucion
Proxima revision de ponderacion en 10 dias.

- Operaciones cerradas: **402**
- Operaciones abiertas: 56

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 18 | 4% | +8.53 EUR |
| flojo | 169 | 42% | +1.32 EUR |
| plano | 20 | 5% | -1.81 EUR |
| perdida | 104 | 26% | -7.30 EUR |
| nefasta | 87 | 22% | -7.45 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 80 | -2.22% | 5/80 (6%) | 15/80 | 9 |
| 11-20 | 103 | -2.52% | 8/103 (8%) | 17/103 | 9 |
| 21-30 | 219 | -2.57% | 9/219 (4%) | 37/219 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 35 | -1.79% | -0.75% | **-1.04%** | 12/35 (34%) |
| 11-20 | 53 | -1.46% | -0.72% | **-0.74%** | 26/53 (49%) |
| 21-30 | 128 | -1.13% | -0.36% | **-0.78%** | 61/128 (48%) |

**En conjunto:** -1.32% de media frente a -0.51% del indice, una diferencia de **-0.81%**. 99 de 216 operaciones (46%) batieron a su indice.

La seleccion NO esta aportando: habria salido mejor comprar el
indice. Aqui si toca revisar la ponderacion del scoring.


**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 59 operaciones, media -0.49%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| escalera + stop vol x4 | -0.86% | 193 | -165.78 EUR | 16/193 | -10.91 EUR |
| trailing pegado (3%) | -1.44% | 154 | -221.53 EUR | 20/154 | -10.00 EUR |
| escalera + stop vol x2.5 | -1.57% | 223 | -349.83 EUR | 14/223 | -10.63 EUR |
| escalera + stop vol x3 | -1.70% | 218 | -371.41 EUR | 14/218 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.49% | 402 | -1000.72 EUR | 22/402 | -8.08 EUR |
| arranca antes (+3%) | -2.91% | 126 | -366.89 EUR | 15/126 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.96% | 117 | -346.51 EUR | 15/117 | -10.00 EUR |
| arranca despues (+8%) | -3.14% | 107 | -336.43 EUR | 15/107 | -10.00 EUR |
| trailing suelto (7%) | -3.59% | 106 | -380.63 EUR | 14/106 | -10.00 EUR |
| sin trailing, solo stop | -3.97% | 99 | -392.83 EUR | 12/99 | -10.00 EUR |
| stop corto (5%) | -4.85% | 249 | -1208.39 EUR | 14/249 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.49%**
- Aciertos (>= 5 EUR limpios): 22/402 (5%)
- Resultado acumulado ficticio: -1000.72 EUR sobre 402 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 134 | -1.67 EUR | 4% | 35% |
| nota global | medio | 134 | -3.24 EUR | 5% | 54% |
| nota global | alto | 134 | -2.56 EUR | 7% | 53% |
| puesto en el ranking | bajo | 134 | -2.37 EUR | 6% | 50% |
| puesto en el ranking | medio | 134 | -2.84 EUR | 6% | 51% |
| puesto en el ranking | alto | 134 | -2.26 EUR | 4% | 42% |
| potencial hasta objetivo | bajo | 134 | -2.69 EUR | 5% | 47% |
| potencial hasta objetivo | medio | 134 | -2.77 EUR | 4% | 49% |
| potencial hasta objetivo | alto | 134 | -2.01 EUR | 7% | 46% |
| dispersion | bajo | 134 | -2.46 EUR | 6% | 51% |
| dispersion | medio | 134 | -2.81 EUR | 4% | 48% |
| dispersion | alto | 134 | -2.19 EUR | 6% | 44% |
| % compra fuerte | bajo | 126 | -2.72 EUR | 4% | 47% |
| % compra fuerte | medio | 126 | -2.00 EUR | 7% | 46% |
| % compra fuerte | alto | 127 | -2.72 EUR | 5% | 47% |
| momentum 30d | bajo | 134 | -2.21 EUR | 7% | 46% |
| momentum 30d | medio | 134 | -2.44 EUR | 7% | 48% |
| momentum 30d | alto | 134 | -2.81 EUR | 3% | 49% |
| fuerza relativa | bajo | 134 | -2.66 EUR | 6% | 52% |
| fuerza relativa | medio | 134 | -2.37 EUR | 7% | 46% |
| fuerza relativa | alto | 134 | -2.43 EUR | 4% | 44% |
| RSI | bajo | 134 | -2.21 EUR | 7% | 47% |
| RSI | medio | 134 | -2.69 EUR | 7% | 51% |
| RSI | alto | 134 | -2.57 EUR | 3% | 45% |
| volumen relativo | bajo | 128 | -2.12 EUR | 9% | 48% |
| volumen relativo | medio | 128 | -2.40 EUR | 3% | 44% |
| volumen relativo | alto | 129 | -2.87 EUR | 4% | 47% |
| volatilidad | bajo | 128 | -1.88 EUR | 7% | 40% |
| volatilidad | medio | 128 | -2.38 EUR | 6% | 46% |
| volatilidad | alto | 129 | -3.13 EUR | 3% | 53% |
| liquidez | bajo | 128 | -2.61 EUR | 5% | 48% |
| liquidez | medio | 128 | -2.36 EUR | 5% | 46% |
| liquidez | alto | 129 | -2.42 EUR | 5% | 44% |
| distancia max 52s | bajo | 128 | -1.88 EUR | 6% | 42% |
| distancia max 52s | medio | 128 | -2.37 EUR | 5% | 46% |
| distancia max 52s | alto | 129 | -3.13 EUR | 5% | 50% |
| consenso | buy | 285 | -2.52 EUR | 5% | 46% |
| consenso | strong_buy | 117 | -2.42 EUR | 6% | 50% |
| tendencia tecnica | alcista | 196 | -2.84 EUR | 5% | 49% |
| tendencia tecnica | mixta | 115 | -2.72 EUR | 4% | 50% |
| tendencia tecnica | bajista | 91 | -1.45 EUR | 8% | 40% |
| tendencia analistas | mejorando | 184 | -2.45 EUR | 5% | 47% |
| tendencia analistas | estable | 135 | -2.89 EUR | 7% | 53% |
| tendencia analistas | empeorando | 16 | -2.66 EUR | 6% | 56% |
| regimen de mercado | neutro | 182 | -2.05 EUR | 8% | 45% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 105 | -2.29 EUR | 4% | 40% |
| catalizador | con catalizador | 16 | -1.90 EUR | 6% | 38% |
| catalizador | sin catalizador | 386 | -2.51 EUR | 5% | 48% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.69 | -2.01 | **+0.69 EUR** |
| dispersion | -2.46 | -2.19 | **+0.27 EUR** |
| fuerza relativa | -2.66 | -2.43 | **+0.23 EUR** |
| liquidez | -2.61 | -2.42 | **+0.19 EUR** |
| puesto en el ranking | -2.37 | -2.26 | **+0.12 EUR** |
| % compra fuerte | -2.72 | -2.72 | **-0.01 EUR** |
| RSI | -2.21 | -2.57 | **-0.36 EUR** |
| momentum 30d | -2.21 | -2.81 | **-0.60 EUR** |
| volumen relativo | -2.12 | -2.87 | **-0.74 EUR** |
| nota global | -1.67 | -2.56 | **-0.88 EUR** |
| distancia max 52s | -1.88 | -3.13 | **-1.25 EUR** |
| volatilidad | -1.88 | -3.13 | **-1.26 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
