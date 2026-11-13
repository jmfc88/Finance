# Simulacion en paralelo

Actualizado: 2026-11-13 07:54 · dia 82 de ejecucion
Proxima revision de ponderacion en 8 dias.

- Operaciones cerradas: **336**
- Operaciones abiertas: 67

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 4 | 1% | +16.71 EUR |
| beneficio | 14 | 4% | +8.78 EUR |
| flojo | 143 | 43% | +1.30 EUR |
| plano | 18 | 5% | -1.74 EUR |
| perdida | 89 | 26% | -7.20 EUR |
| nefasta | 68 | 20% | -7.28 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 65 | -1.65% | 5/65 (8%) | 14/65 | 10 |
| 11-20 | 84 | -2.43% | 6/84 (7%) | 13/84 | 9 |
| 21-30 | 187 | -2.57% | 7/187 (4%) | 28/187 | 9 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 21 | -0.03% | +0.03% | **-0.05%** | 11/21 (52%) |
| 11-20 | 35 | -0.84% | -0.23% | **-0.61%** | 20/35 (57%) |
| 21-30 | 97 | -0.73% | -0.08% | **-0.65%** | 50/97 (52%) |

**En conjunto:** -0.66% de media frente a -0.10% del indice, una diferencia de **-0.56%**. 81 de 153 operaciones (53%) batieron a su indice.

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
| escalera + stop vol x4 | -0.66% | 145 | -96.04 EUR | 13/145 | -10.91 EUR |
| escalera + stop vol x2.5 | -1.30% | 161 | -209.10 EUR | 11/161 | -10.63 EUR |
| escalera + stop vol x3 | -1.40% | 157 | -219.67 EUR | 11/157 | -12.76 EUR |
| trailing pegado (3%) | -1.59% | 130 | -207.01 EUR | 16/130 | -10.00 EUR |
| LA REAL (escalera 25/08) | -2.36% | 336 | -792.20 EUR | 18/336 | -8.08 EUR |
| arranca antes (+3%) | -2.96% | 109 | -322.13 EUR | 12/109 | -10.00 EUR |
| actual (8% / +5% / 5%) | -3.07% | 101 | -310.40 EUR | 12/101 | -10.00 EUR |
| arranca despues (+8%) | -3.26% | 92 | -300.27 EUR | 12/92 | -10.00 EUR |
| trailing suelto (7%) | -3.73% | 91 | -339.02 EUR | 11/91 | -10.00 EUR |
| sin trailing, solo stop | -4.16% | 85 | -353.32 EUR | 9/85 | -10.00 EUR |
| stop corto (5%) | -4.77% | 206 | -983.15 EUR | 12/206 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-2.36%**
- Aciertos (>= 5 EUR limpios): 18/336 (5%)
- Resultado acumulado ficticio: -792.20 EUR sobre 336 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 112 | -1.66 EUR | 4% | 36% |
| nota global | medio | 112 | -3.23 EUR | 4% | 54% |
| nota global | alto | 112 | -2.18 EUR | 8% | 51% |
| puesto en el ranking | bajo | 112 | -2.10 EUR | 7% | 49% |
| puesto en el ranking | medio | 112 | -2.72 EUR | 5% | 49% |
| puesto en el ranking | alto | 112 | -2.26 EUR | 4% | 42% |
| potencial hasta objetivo | bajo | 112 | -2.73 EUR | 4% | 47% |
| potencial hasta objetivo | medio | 112 | -2.50 EUR | 4% | 48% |
| potencial hasta objetivo | alto | 112 | -1.84 EUR | 7% | 45% |
| dispersion | bajo | 112 | -2.23 EUR | 7% | 49% |
| dispersion | medio | 112 | -2.54 EUR | 4% | 46% |
| dispersion | alto | 112 | -2.31 EUR | 4% | 45% |
| % compra fuerte | bajo | 105 | -2.92 EUR | 3% | 49% |
| % compra fuerte | medio | 105 | -1.76 EUR | 9% | 46% |
| % compra fuerte | alto | 106 | -2.47 EUR | 4% | 44% |
| momentum 30d | bajo | 112 | -2.48 EUR | 7% | 49% |
| momentum 30d | medio | 112 | -2.09 EUR | 4% | 44% |
| momentum 30d | alto | 112 | -2.50 EUR | 4% | 47% |
| fuerza relativa | bajo | 112 | -2.64 EUR | 6% | 53% |
| fuerza relativa | medio | 112 | -2.21 EUR | 4% | 43% |
| fuerza relativa | alto | 112 | -2.23 EUR | 5% | 45% |
| RSI | bajo | 112 | -2.40 EUR | 6% | 49% |
| RSI | medio | 112 | -2.34 EUR | 7% | 48% |
| RSI | alto | 112 | -2.34 EUR | 3% | 43% |
| volumen relativo | bajo | 106 | -1.81 EUR | 9% | 45% |
| volumen relativo | medio | 106 | -2.46 EUR | 3% | 44% |
| volumen relativo | alto | 107 | -2.68 EUR | 4% | 46% |
| volatilidad | bajo | 106 | -1.97 EUR | 7% | 41% |
| volatilidad | medio | 106 | -2.61 EUR | 6% | 48% |
| volatilidad | alto | 107 | -2.38 EUR | 4% | 47% |
| liquidez | bajo | 106 | -2.87 EUR | 4% | 49% |
| liquidez | medio | 106 | -2.01 EUR | 7% | 44% |
| liquidez | alto | 107 | -2.08 EUR | 6% | 42% |
| distancia max 52s | bajo | 106 | -1.77 EUR | 6% | 41% |
| distancia max 52s | medio | 106 | -1.98 EUR | 7% | 44% |
| distancia max 52s | alto | 107 | -3.20 EUR | 4% | 50% |
| consenso | buy | 237 | -2.36 EUR | 5% | 45% |
| consenso | strong_buy | 99 | -2.36 EUR | 6% | 51% |
| tendencia tecnica | alcista | 156 | -2.71 EUR | 4% | 49% |
| tendencia tecnica | mixta | 96 | -2.47 EUR | 5% | 49% |
| tendencia tecnica | bajista | 84 | -1.56 EUR | 7% | 40% |
| tendencia analistas | mejorando | 153 | -2.30 EUR | 4% | 45% |
| tendencia analistas | estable | 113 | -2.70 EUR | 8% | 52% |
| tendencia analistas | empeorando | 14 | -2.72 EUR | 7% | 57% |
| regimen de mercado | neutro | 169 | -1.96 EUR | 7% | 43% |
| regimen de mercado | favorable | 115 | -3.36 EUR | 3% | 59% |
| regimen de mercado | adverso | 52 | -1.43 EUR | 4% | 31% |
| catalizador | con catalizador | 11 | -0.74 EUR | 9% | 27% |
| catalizador | sin catalizador | 325 | -2.41 EUR | 5% | 47% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| potencial hasta objetivo | -2.73 | -1.84 | **+0.89 EUR** |
| liquidez | -2.87 | -2.08 | **+0.80 EUR** |
| % compra fuerte | -2.92 | -2.47 | **+0.45 EUR** |
| fuerza relativa | -2.64 | -2.23 | **+0.41 EUR** |
| RSI | -2.40 | -2.34 | **+0.06 EUR** |
| momentum 30d | -2.48 | -2.50 | **-0.02 EUR** |
| dispersion | -2.23 | -2.31 | **-0.08 EUR** |
| puesto en el ranking | -2.10 | -2.26 | **-0.16 EUR** |
| volatilidad | -1.97 | -2.38 | **-0.42 EUR** |
| nota global | -1.66 | -2.18 | **-0.52 EUR** |
| volumen relativo | -1.81 | -2.68 | **-0.87 EUR** |
| distancia max 52s | -1.77 | -3.20 | **-1.42 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
