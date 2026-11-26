# Simulacion en paralelo

Actualizado: 2026-11-26 09:29 · dia 95 de ejecucion
Proxima revision de ponderacion en 10 dias.

- Operaciones cerradas: **403**
- Operaciones abiertas: 55

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 18 | 4% | +8.53 EUR |
| flojo | 170 | 42% | +1.33 EUR |
| plano | 20 | 5% | -1.81 EUR |
| perdida | 104 | 26% | -7.30 EUR |
| nefasta | 87 | 22% | -7.45 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 81 | -2.15% | 5/81 (6%) | 16/81 | 9 |
| 11-20 | 103 | -2.52% | 8/103 (8%) | 17/103 | 9 |
| 21-30 | 219 | -2.57% | 9/219 (4%) | 37/219 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 36 | -1.64% | -0.82% | **-0.82%** | 13/36 (36%) |
| 11-20 | 53 | -1.46% | -0.72% | **-0.74%** | 26/53 (49%) |
| 21-30 | 128 | -1.13% | -0.36% | **-0.78%** | 61/128 (48%) |

**En conjunto:** -1.30% de media frente a -0.52% del indice, una diferencia de **-0.78%**. 100 de 217 operaciones (46%) batieron a su indice.

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
| escalera + stop vol x4 | -0.84% | 194 | -162.25 EUR | 16/194 | -10.91 EUR |
| trailing pegado (3%) | -1.44% | 154 | -221.53 EUR | 20/154 | -10.00 EUR |
| escalera + stop vol x2.5 | -1.58% | 224 | -353.87 EUR | 14/224 | -10.63 EUR |
| escalera + stop vol x3 | -1.71% | 219 | -375.45 EUR | 14/219 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.47% | 403 | -997.19 EUR | 22/403 | -8.08 EUR |
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

- Media neta: **-2.47%**
- Aciertos (>= 5 EUR limpios): 22/403 (5%)
- Resultado acumulado ficticio: -997.19 EUR sobre 403 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 134 | -1.67 EUR | 4% | 35% |
| nota global | medio | 134 | -3.24 EUR | 5% | 54% |
| nota global | alto | 135 | -2.51 EUR | 7% | 53% |
| puesto en el ranking | bajo | 134 | -2.33 EUR | 6% | 50% |
| puesto en el ranking | medio | 134 | -2.86 EUR | 6% | 51% |
| puesto en el ranking | alto | 135 | -2.23 EUR | 4% | 41% |
| potencial hasta objetivo | bajo | 134 | -2.64 EUR | 5% | 46% |
| potencial hasta objetivo | medio | 134 | -2.74 EUR | 4% | 49% |
| potencial hasta objetivo | alto | 135 | -2.05 EUR | 7% | 47% |
| dispersion | bajo | 134 | -2.46 EUR | 6% | 51% |
| dispersion | medio | 134 | -2.73 EUR | 4% | 47% |
| dispersion | alto | 135 | -2.23 EUR | 6% | 44% |
| % compra fuerte | bajo | 126 | -2.72 EUR | 4% | 47% |
| % compra fuerte | medio | 126 | -2.00 EUR | 7% | 46% |
| % compra fuerte | alto | 128 | -2.67 EUR | 5% | 47% |
| momentum 30d | bajo | 134 | -2.21 EUR | 7% | 46% |
| momentum 30d | medio | 134 | -2.44 EUR | 7% | 48% |
| momentum 30d | alto | 135 | -2.77 EUR | 3% | 48% |
| fuerza relativa | bajo | 134 | -2.66 EUR | 6% | 52% |
| fuerza relativa | medio | 134 | -2.37 EUR | 7% | 46% |
| fuerza relativa | alto | 135 | -2.39 EUR | 4% | 44% |
| RSI | bajo | 134 | -2.21 EUR | 7% | 47% |
| RSI | medio | 134 | -2.69 EUR | 7% | 51% |
| RSI | alto | 135 | -2.52 EUR | 3% | 44% |
| volumen relativo | bajo | 128 | -2.12 EUR | 9% | 48% |
| volumen relativo | medio | 128 | -2.38 EUR | 3% | 44% |
| volumen relativo | alto | 130 | -2.84 EUR | 4% | 47% |
| volatilidad | bajo | 128 | -1.88 EUR | 7% | 40% |
| volatilidad | medio | 128 | -2.32 EUR | 6% | 45% |
| volatilidad | alto | 130 | -3.13 EUR | 3% | 53% |
| liquidez | bajo | 128 | -2.61 EUR | 5% | 48% |
| liquidez | medio | 128 | -2.34 EUR | 5% | 45% |
| liquidez | alto | 130 | -2.39 EUR | 5% | 45% |
| distancia max 52s | bajo | 128 | -1.88 EUR | 6% | 42% |
| distancia max 52s | medio | 128 | -2.37 EUR | 5% | 46% |
| distancia max 52s | alto | 130 | -3.08 EUR | 5% | 50% |
| consenso | buy | 286 | -2.50 EUR | 5% | 46% |
| consenso | strong_buy | 117 | -2.42 EUR | 6% | 50% |
| tendencia tecnica | alcista | 197 | -2.80 EUR | 5% | 49% |
| tendencia tecnica | mixta | 115 | -2.72 EUR | 4% | 50% |
| tendencia tecnica | bajista | 91 | -1.45 EUR | 8% | 40% |
| tendencia analistas | mejorando | 185 | -2.42 EUR | 5% | 46% |
| tendencia analistas | estable | 135 | -2.89 EUR | 7% | 53% |
| tendencia analistas | empeorando | 16 | -2.66 EUR | 6% | 56% |
| regimen de mercado | neutro | 182 | -2.05 EUR | 8% | 45% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 106 | -2.24 EUR | 4% | 40% |
| catalizador | con catalizador | 16 | -1.90 EUR | 6% | 38% |
| catalizador | sin catalizador | 387 | -2.50 EUR | 5% | 48% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.64 | -2.05 | **+0.59 EUR** |
| fuerza relativa | -2.66 | -2.39 | **+0.27 EUR** |
| dispersion | -2.46 | -2.23 | **+0.23 EUR** |
| liquidez | -2.61 | -2.39 | **+0.21 EUR** |
| puesto en el ranking | -2.33 | -2.23 | **+0.10 EUR** |
| % compra fuerte | -2.72 | -2.67 | **+0.04 EUR** |
| RSI | -2.21 | -2.52 | **-0.31 EUR** |
| momentum 30d | -2.21 | -2.77 | **-0.56 EUR** |
| volumen relativo | -2.12 | -2.84 | **-0.71 EUR** |
| nota global | -1.67 | -2.51 | **-0.84 EUR** |
| distancia max 52s | -1.88 | -3.08 | **-1.20 EUR** |
| volatilidad | -1.88 | -3.13 | **-1.25 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
