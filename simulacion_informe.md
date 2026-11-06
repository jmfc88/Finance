# Simulacion en paralelo

Actualizado: 2026-11-06 14:12 · dia 75 de ejecucion
**Revision nº5 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **310**
- Operaciones abiertas: 41

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 13 | 4% | +8.76 EUR |
| flojo | 124 | 40% | +1.30 EUR |
| plano | 18 | 6% | -1.74 EUR |
| perdida | 88 | 28% | -7.19 EUR |
| nefasta | 63 | 20% | -7.22 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 62 | -1.78% | 5/62 (8%) | 13/62 | 10 |
| 11-20 | 77 | -2.38% | 6/77 (8%) | 11/77 | 9 |
| 21-30 | 171 | -2.82% | 6/171 (4%) | 22/171 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 18 | -0.20% | -0.33% | **+0.13%** | 10/18 (56%) |
| 11-20 | 30 | -0.85% | -0.62% | **-0.23%** | 19/30 (63%) |
| 21-30 | 82 | -0.99% | -0.36% | **-0.62%** | 46/82 (56%) |

**En conjunto:** -0.85% de media frente a -0.42% del indice, una diferencia de **-0.43%**. 75 de 130 operaciones (58%) batieron a su indice.

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
| escalera + stop vol x4 | -0.86% | 121 | -103.95 EUR | 12/121 | -10.91 EUR |
| trailing pegado (3%) | -1.47% | 120 | -176.59 EUR | 16/120 | -10.00 EUR |
| escalera + stop vol x2.5 | -1.61% | 137 | -220.33 EUR | 10/137 | -10.63 EUR |
| escalera + stop vol x3 | -1.72% | 133 | -228.15 EUR | 10/133 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.51% | 310 | -776.88 EUR | 17/310 | -8.08 EUR |
| arranca antes (+3%) | -2.69% | 104 | -280.18 EUR | 12/104 | -10.00 EUR |
| actual (8% / +5% / 5%) | -2.80% | 96 | -268.45 EUR | 12/96 | -10.00 EUR |
| arranca despues (+8%) | -2.96% | 88 | -260.27 EUR | 12/88 | -10.00 EUR |
| trailing suelto (7%) | -3.44% | 87 | -299.02 EUR | 11/87 | -10.00 EUR |
| sin trailing, solo stop | -3.87% | 81 | -313.32 EUR | 9/81 | -10.00 EUR |
| stop corto (5%) | -4.72% | 199 | -939.20 EUR | 12/199 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.51%**
- Aciertos (>= 5 EUR limpios): 17/310 (5%)
- Resultado acumulado ficticio: -776.88 EUR sobre 310 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 103 | -2.15 EUR | 4% | 41% |
| nota global | medio | 103 | -3.29 EUR | 4% | 54% |
| nota global | alto | 104 | -2.08 EUR | 9% | 51% |
| puesto en el ranking | bajo | 103 | -2.11 EUR | 8% | 50% |
| puesto en el ranking | medio | 103 | -2.94 EUR | 5% | 51% |
| puesto en el ranking | alto | 104 | -2.47 EUR | 4% | 44% |
| potencial hasta objetivo | bajo | 103 | -2.79 EUR | 5% | 49% |
| potencial hasta objetivo | medio | 103 | -2.82 EUR | 4% | 51% |
| potencial hasta objetivo | alto | 104 | -1.91 EUR | 8% | 46% |
| dispersion | bajo | 103 | -2.22 EUR | 8% | 50% |
| dispersion | medio | 103 | -2.90 EUR | 5% | 50% |
| dispersion | alto | 104 | -2.40 EUR | 4% | 45% |
| % compra fuerte | bajo | 97 | -2.77 EUR | 3% | 47% |
| % compra fuerte | medio | 97 | -2.26 EUR | 8% | 52% |
| % compra fuerte | alto | 97 | -2.53 EUR | 4% | 45% |
| momentum 30d | bajo | 103 | -2.68 EUR | 6% | 50% |
| momentum 30d | medio | 103 | -2.19 EUR | 6% | 46% |
| momentum 30d | alto | 104 | -2.65 EUR | 5% | 50% |
| fuerza relativa | bajo | 103 | -2.88 EUR | 5% | 53% |
| fuerza relativa | medio | 103 | -2.33 EUR | 6% | 46% |
| fuerza relativa | alto | 104 | -2.30 EUR | 6% | 47% |
| RSI | bajo | 103 | -2.48 EUR | 7% | 50% |
| RSI | medio | 103 | -2.48 EUR | 6% | 50% |
| RSI | alto | 104 | -2.55 EUR | 4% | 46% |
| volumen relativo | bajo | 97 | -1.72 EUR | 10% | 45% |
| volumen relativo | medio | 97 | -2.47 EUR | 3% | 44% |
| volumen relativo | alto | 99 | -3.21 EUR | 3% | 52% |
| volatilidad | bajo | 97 | -2.05 EUR | 7% | 42% |
| volatilidad | medio | 97 | -2.77 EUR | 4% | 48% |
| volatilidad | alto | 99 | -2.60 EUR | 5% | 51% |
| liquidez | bajo | 97 | -2.95 EUR | 4% | 51% |
| liquidez | medio | 97 | -2.13 EUR | 7% | 46% |
| liquidez | alto | 99 | -2.34 EUR | 5% | 44% |
| distancia max 52s | bajo | 97 | -1.87 EUR | 6% | 42% |
| distancia max 52s | medio | 97 | -2.22 EUR | 6% | 47% |
| distancia max 52s | alto | 99 | -3.31 EUR | 4% | 52% |
| consenso | buy | 218 | -2.53 EUR | 5% | 47% |
| consenso | strong_buy | 92 | -2.45 EUR | 7% | 52% |
| tendencia tecnica | alcista | 143 | -2.80 EUR | 5% | 50% |
| tendencia tecnica | mixta | 88 | -2.70 EUR | 5% | 51% |
| tendencia tecnica | bajista | 79 | -1.76 EUR | 8% | 43% |
| tendencia analistas | mejorando | 142 | -2.51 EUR | 4% | 48% |
| tendencia analistas | estable | 104 | -2.77 EUR | 8% | 53% |
| tendencia analistas | empeorando | 13 | -3.00 EUR | 8% | 62% |
| regimen de mercado | neutro | 160 | -2.08 EUR | 7% | 44% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 35 | -1.65 EUR | 6% | 34% |
| catalizador | con catalizador | 6 | -3.54 EUR | 0% | 50% |
| catalizador | sin catalizador | 304 | -2.49 EUR | 6% | 49% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.79 | -1.91 | **+0.88 EUR** |
| liquidez | -2.95 | -2.34 | **+0.61 EUR** |
| fuerza relativa | -2.88 | -2.30 | **+0.58 EUR** |
| % compra fuerte | -2.77 | -2.53 | **+0.24 EUR** |
| nota global | -2.15 | -2.08 | **+0.08 EUR** |
| momentum 30d | -2.68 | -2.65 | **+0.03 EUR** |
| RSI | -2.48 | -2.55 | **-0.07 EUR** |
| dispersion | -2.22 | -2.40 | **-0.18 EUR** |
| puesto en el ranking | -2.11 | -2.47 | **-0.36 EUR** |
| volatilidad | -2.05 | -2.60 | **-0.55 EUR** |
| distancia max 52s | -1.87 | -3.31 | **-1.45 EUR** |
| volumen relativo | -1.72 | -3.21 | **-1.49 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
