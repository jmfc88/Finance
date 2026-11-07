# Simulacion en paralelo

Actualizado: 2026-11-07 00:58 · dia 76 de ejecucion
**Revision nº5 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **312**
- Operaciones abiertas: 54

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 14 | 4% | +8.78 EUR |
| flojo | 125 | 40% | +1.30 EUR |
| plano | 18 | 6% | -1.74 EUR |
| perdida | 88 | 28% | -7.19 EUR |
| nefasta | 63 | 20% | -7.22 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 62 | -1.78% | 5/62 (8%) | 13/62 | 10 |
| 11-20 | 77 | -2.38% | 6/77 (8%) | 11/77 | 9 |
| 21-30 | 173 | -2.73% | 7/173 (4%) | 23/173 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 18 | -0.20% | -0.33% | **+0.13%** | 10/18 (56%) |
| 11-20 | 30 | -0.85% | -0.62% | **-0.23%** | 19/30 (63%) |
| 21-30 | 84 | -0.84% | -0.38% | **-0.46%** | 47/84 (56%) |

**En conjunto:** -0.76% de media frente a -0.43% del indice, una diferencia de **-0.33%**. 76 de 132 operaciones (58%) batieron a su indice.

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
| escalera + stop vol x4 | -0.76% | 123 | -93.86 EUR | 13/123 | -10.91 EUR |
| trailing pegado (3%) | -1.47% | 120 | -176.59 EUR | 16/120 | -10.00 EUR |
| escalera + stop vol x2.5 | -1.51% | 139 | -210.24 EUR | 11/139 | -10.63 EUR |
| escalera + stop vol x3 | -1.62% | 135 | -218.06 EUR | 11/135 | -12.76 EUR |
| LA REAL (escalera 25/08) | -2.46% | 312 | -766.79 EUR | 18/312 | -8.08 EUR |
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

- Media neta: **-2.46%**
- Aciertos (>= 5 EUR limpios): 18/312 (6%)
- Resultado acumulado ficticio: -766.79 EUR sobre 312 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 104 | -2.00 EUR | 5% | 39% |
| nota global | medio | 104 | -3.29 EUR | 4% | 55% |
| nota global | alto | 104 | -2.08 EUR | 9% | 51% |
| puesto en el ranking | bajo | 104 | -2.08 EUR | 8% | 50% |
| puesto en el ranking | medio | 104 | -2.83 EUR | 6% | 51% |
| puesto en el ranking | alto | 104 | -2.47 EUR | 4% | 44% |
| potencial hasta objetivo | bajo | 104 | -2.76 EUR | 5% | 48% |
| potencial hasta objetivo | medio | 104 | -2.70 EUR | 5% | 51% |
| potencial hasta objetivo | alto | 104 | -1.91 EUR | 8% | 46% |
| dispersion | bajo | 104 | -2.21 EUR | 8% | 50% |
| dispersion | medio | 104 | -2.92 EUR | 5% | 51% |
| dispersion | alto | 104 | -2.24 EUR | 5% | 44% |
| % compra fuerte | bajo | 97 | -2.77 EUR | 3% | 47% |
| % compra fuerte | medio | 97 | -2.18 EUR | 9% | 52% |
| % compra fuerte | alto | 99 | -2.46 EUR | 4% | 44% |
| momentum 30d | bajo | 104 | -2.65 EUR | 6% | 50% |
| momentum 30d | medio | 104 | -2.08 EUR | 7% | 45% |
| momentum 30d | alto | 104 | -2.65 EUR | 5% | 50% |
| fuerza relativa | bajo | 104 | -2.85 EUR | 5% | 53% |
| fuerza relativa | medio | 104 | -2.22 EUR | 7% | 45% |
| fuerza relativa | alto | 104 | -2.30 EUR | 6% | 47% |
| RSI | bajo | 104 | -2.45 EUR | 7% | 49% |
| RSI | medio | 104 | -2.37 EUR | 7% | 50% |
| RSI | alto | 104 | -2.55 EUR | 4% | 46% |
| volumen relativo | bajo | 98 | -1.79 EUR | 10% | 46% |
| volumen relativo | medio | 98 | -2.40 EUR | 3% | 44% |
| volumen relativo | alto | 99 | -3.07 EUR | 4% | 51% |
| volatilidad | bajo | 98 | -2.02 EUR | 7% | 42% |
| volatilidad | medio | 98 | -2.64 EUR | 5% | 48% |
| volatilidad | alto | 99 | -2.60 EUR | 5% | 51% |
| liquidez | bajo | 98 | -2.94 EUR | 4% | 50% |
| liquidez | medio | 98 | -2.07 EUR | 7% | 46% |
| liquidez | alto | 99 | -2.26 EUR | 6% | 44% |
| distancia max 52s | bajo | 98 | -1.84 EUR | 6% | 42% |
| distancia max 52s | medio | 98 | -2.11 EUR | 7% | 47% |
| distancia max 52s | alto | 99 | -3.31 EUR | 4% | 52% |
| consenso | buy | 220 | -2.46 EUR | 5% | 47% |
| consenso | strong_buy | 92 | -2.45 EUR | 7% | 52% |
| tendencia tecnica | alcista | 144 | -2.77 EUR | 5% | 50% |
| tendencia tecnica | mixta | 89 | -2.57 EUR | 6% | 51% |
| tendencia tecnica | bajista | 79 | -1.76 EUR | 8% | 43% |
| tendencia analistas | mejorando | 143 | -2.48 EUR | 4% | 48% |
| tendencia analistas | estable | 105 | -2.66 EUR | 9% | 52% |
| tendencia analistas | empeorando | 13 | -3.00 EUR | 8% | 62% |
| regimen de mercado | neutro | 161 | -2.01 EUR | 7% | 44% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 36 | -1.58 EUR | 6% | 33% |
| catalizador | con catalizador | 7 | -1.74 EUR | 14% | 43% |
| catalizador | sin catalizador | 305 | -2.47 EUR | 6% | 49% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.76 | -1.91 | **+0.84 EUR** |
| liquidez | -2.94 | -2.26 | **+0.68 EUR** |
| fuerza relativa | -2.85 | -2.30 | **+0.54 EUR** |
| % compra fuerte | -2.77 | -2.46 | **+0.31 EUR** |
| momentum 30d | -2.65 | -2.65 | **-0.00 EUR** |
| dispersion | -2.21 | -2.24 | **-0.02 EUR** |
| nota global | -2.00 | -2.08 | **-0.07 EUR** |
| RSI | -2.45 | -2.55 | **-0.10 EUR** |
| puesto en el ranking | -2.08 | -2.47 | **-0.39 EUR** |
| volatilidad | -2.02 | -2.60 | **-0.58 EUR** |
| volumen relativo | -1.79 | -3.07 | **-1.28 EUR** |
| distancia max 52s | -1.84 | -3.31 | **-1.48 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
