# Simulacion en paralelo

Actualizado: 2026-09-25 21:35 · dia 33 de ejecucion
Proxima revision de ponderacion en 12 dias.

- Operaciones cerradas: **103**
- Operaciones abiertas: 58

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 1 | 1% | +16.67 EUR |
| beneficio | 2 | 2% | +7.32 EUR |
| flojo | 35 | 34% | +1.22 EUR |
| plano | 5 | 5% | -1.87 EUR |
| perdida | 35 | 34% | -7.16 EUR |
| nefasta | 25 | 24% | -5.90 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 25 | -1.91% | 0/25 (0%) | 5/25 | 8 |
| 11-20 | 28 | -1.96% | 2/28 (7%) | 3/28 | 8 |
| 21-30 | 50 | -4.62% | 1/50 (2%) | 2/50 | 9 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 12 operaciones, media -2.44%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -52.74 EUR | -2.20% | 1/24 | -10.00 EUR |
| arranca despues (+8%) | -62.14 EUR | -3.45% | 2/18 | -10.00 EUR |
| actual (8% / +5% / 5%) | -62.14 EUR | -3.45% | 2/18 | -10.00 EUR |
| trailing suelto (7%) | -64.59 EUR | -3.59% | 2/18 | -10.00 EUR |
| sin trailing, solo stop | -76.65 EUR | -4.51% | 1/17 | -10.00 EUR |
| arranca antes (+3%) | -78.67 EUR | -3.58% | 2/22 | -10.00 EUR |
| LA REAL (escalera 25/08) | -333.64 EUR | -3.24% | 3/103 | -8.08 EUR |
| stop corto (5%) | -385.34 EUR | -5.93% | 2/65 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.24%**
- Aciertos (>= 5 EUR limpios): 3/103 (3%)
- Resultado acumulado ficticio: -333.64 EUR sobre 103 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 34 | -4.40 EUR | 0% | 62% |
| nota global | medio | 34 | -3.46 EUR | 6% | 68% |
| nota global | alto | 35 | -1.89 EUR | 3% | 46% |
| puesto en el ranking | bajo | 34 | -1.78 EUR | 3% | 41% |
| puesto en el ranking | medio | 34 | -3.13 EUR | 6% | 65% |
| puesto en el ranking | alto | 35 | -4.77 EUR | 0% | 69% |
| potencial hasta objetivo | bajo | 34 | -4.00 EUR | 3% | 62% |
| potencial hasta objetivo | medio | 34 | -3.42 EUR | 0% | 62% |
| potencial hasta objetivo | alto | 35 | -2.33 EUR | 6% | 51% |
| dispersion | bajo | 34 | -1.06 EUR | 6% | 38% |
| dispersion | medio | 34 | -5.16 EUR | 0% | 74% |
| dispersion | alto | 35 | -3.49 EUR | 3% | 63% |
| % compra fuerte | bajo | 32 | -4.15 EUR | 3% | 66% |
| % compra fuerte | medio | 32 | -2.82 EUR | 3% | 62% |
| % compra fuerte | alto | 34 | -3.59 EUR | 0% | 53% |
| momentum 30d | bajo | 34 | -2.89 EUR | 3% | 53% |
| momentum 30d | medio | 34 | -3.62 EUR | 3% | 59% |
| momentum 30d | alto | 35 | -3.21 EUR | 3% | 63% |
| fuerza relativa | bajo | 34 | -3.06 EUR | 3% | 56% |
| fuerza relativa | medio | 34 | -3.63 EUR | 0% | 56% |
| fuerza relativa | alto | 35 | -3.04 EUR | 6% | 63% |
| RSI | bajo | 34 | -2.67 EUR | 6% | 53% |
| RSI | medio | 34 | -2.96 EUR | 0% | 56% |
| RSI | alto | 35 | -4.07 EUR | 3% | 66% |
| volumen relativo | bajo | 28 | -2.90 EUR | 7% | 57% |
| volumen relativo | medio | 28 | -3.04 EUR | 0% | 54% |
| volumen relativo | alto | 30 | -3.84 EUR | 0% | 53% |
| volatilidad | bajo | 28 | -3.73 EUR | 0% | 57% |
| volatilidad | medio | 28 | -4.11 EUR | 0% | 61% |
| volatilidad | alto | 30 | -2.06 EUR | 7% | 47% |
| liquidez | bajo | 28 | -3.70 EUR | 0% | 57% |
| liquidez | medio | 28 | -2.96 EUR | 4% | 57% |
| liquidez | alto | 30 | -3.16 EUR | 3% | 50% |
| distancia max 52s | bajo | 28 | -2.35 EUR | 7% | 50% |
| distancia max 52s | medio | 28 | -3.68 EUR | 0% | 61% |
| distancia max 52s | alto | 30 | -3.75 EUR | 0% | 53% |
| consenso | buy | 72 | -4.17 EUR | 3% | 67% |
| consenso | strong_buy | 31 | -1.08 EUR | 3% | 39% |
| tendencia tecnica | alcista | 63 | -3.33 EUR | 3% | 59% |
| tendencia tecnica | mixta | 27 | -2.38 EUR | 4% | 52% |
| tendencia tecnica | bajista | 13 | -4.59 EUR | 0% | 69% |
| tendencia analistas | mejorando | 53 | -3.02 EUR | 4% | 57% |
| tendencia analistas | estable | 36 | -4.89 EUR | 0% | 72% |
| tendencia analistas | empeorando | 5 | -2.63 EUR | 0% | 60% |
| regimen de mercado | favorable | 79 | -3.18 EUR | 4% | 61% |
| regimen de mercado | neutro | 24 | -3.43 EUR | 0% | 50% |
| catalizador | sin catalizador | 102 | -3.19 EUR | 3% | 58% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.40 | -1.89 | **+2.51 EUR** |
| potencial hasta objetivo | -4.00 | -2.33 | **+1.67 EUR** |
| volatilidad | -3.73 | -2.06 | **+1.67 EUR** |
| % compra fuerte | -4.15 | -3.59 | **+0.56 EUR** |
| liquidez | -3.70 | -3.16 | **+0.54 EUR** |
| fuerza relativa | -3.06 | -3.04 | **+0.02 EUR** |
| momentum 30d | -2.89 | -3.21 | **-0.33 EUR** |
| volumen relativo | -2.90 | -3.84 | **-0.94 EUR** |
| distancia max 52s | -2.35 | -3.75 | **-1.40 EUR** |
| RSI | -2.67 | -4.07 | **-1.40 EUR** |
| dispersion | -1.06 | -3.49 | **-2.43 EUR** |
| puesto en el ranking | -1.78 | -4.77 | **-2.98 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
