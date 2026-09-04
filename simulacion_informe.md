# Simulacion en paralelo

Actualizado: 2026-09-04 20:46 · dia 12 de ejecucion
Proxima revision de ponderacion en 3 dias.

- Operaciones cerradas: **27**
- Operaciones abiertas: 67

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 6 | 22% | +1.42 EUR |
| plano | 0 | - | - |
| perdida | 8 | 30% | -6.94 EUR |
| nefasta | 13 | 48% | -3.89 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 9 | -2.75% | 0/9 (0%) | 2/9 | 6 |
| 11-20 | 9 | -2.03% | 0/9 (0%) | 0/9 | 4 |
| 21-30 | 9 | -6.06% | 0/9 (0%) | 0/9 | 4 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida


## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -17.15 EUR | -4.29% | 0/4 | -10.00 EUR |
| trailing suelto (7%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| sin trailing, solo stop | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| arranca despues (+8%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| actual (8% / +5% / 5%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| arranca antes (+3%) | -26.95 EUR | -6.74% | 0/4 | -10.00 EUR |
| LA REAL (escalera 25/08) | -97.58 EUR | -3.61% | 0/27 | -8.08 EUR |
| stop corto (5%) | -112.00 EUR | -7.00% | 0/16 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.61%**
- Aciertos (>= 5 EUR limpios): 0/27 (0%)
- Resultado acumulado ficticio: -97.58 EUR sobre 27 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 9 | -6.06 EUR | 0% | 89% |
| nota global | medio | 9 | -2.03 EUR | 0% | 89% |
| nota global | alto | 9 | -2.75 EUR | 0% | 56% |
| puesto en el ranking | bajo | 9 | -2.75 EUR | 0% | 56% |
| puesto en el ranking | medio | 9 | -2.03 EUR | 0% | 78% |
| puesto en el ranking | alto | 9 | -6.06 EUR | 0% | 100% |
| potencial hasta objetivo | bajo | 9 | -3.04 EUR | 0% | 78% |
| potencial hasta objetivo | medio | 9 | -4.04 EUR | 0% | 78% |
| potencial hasta objetivo | alto | 9 | -3.76 EUR | 0% | 78% |
| dispersion | bajo | 9 | -2.03 EUR | 0% | 56% |
| dispersion | medio | 9 | -5.78 EUR | 0% | 89% |
| dispersion | alto | 9 | -3.04 EUR | 0% | 89% |
| % compra fuerte | bajo | 8 | -3.54 EUR | 0% | 62% |
| % compra fuerte | medio | 8 | -1.27 EUR | 0% | 88% |
| % compra fuerte | alto | 10 | -5.10 EUR | 0% | 80% |
| momentum 30d | bajo | 9 | -3.04 EUR | 0% | 67% |
| momentum 30d | medio | 9 | -4.77 EUR | 0% | 78% |
| momentum 30d | alto | 9 | -3.04 EUR | 0% | 89% |
| fuerza relativa | bajo | 9 | -2.03 EUR | 0% | 56% |
| fuerza relativa | medio | 9 | -5.78 EUR | 0% | 89% |
| fuerza relativa | alto | 9 | -3.04 EUR | 0% | 89% |
| RSI | bajo | 9 | -5.05 EUR | 0% | 78% |
| RSI | medio | 9 | -2.75 EUR | 0% | 89% |
| RSI | alto | 9 | -3.04 EUR | 0% | 67% |
| volumen relativo | bajo | 5 | -4.45 EUR | 0% | 80% |
| volumen relativo | medio | 5 | -6.26 EUR | 0% | 100% |
| volumen relativo | alto | 7 | -4.19 EUR | 0% | 71% |
| volatilidad | bajo | 5 | -4.45 EUR | 0% | 80% |
| volatilidad | medio | 5 | -4.45 EUR | 0% | 80% |
| volatilidad | alto | 7 | -5.49 EUR | 0% | 86% |
| liquidez | bajo | 5 | -4.45 EUR | 0% | 80% |
| liquidez | medio | 5 | -4.45 EUR | 0% | 80% |
| liquidez | alto | 7 | -5.49 EUR | 0% | 86% |
| distancia max 52s | bajo | 5 | -6.26 EUR | 0% | 100% |
| distancia max 52s | medio | 5 | -4.45 EUR | 0% | 80% |
| distancia max 52s | alto | 7 | -4.19 EUR | 0% | 71% |
| consenso | buy | 16 | -4.67 EUR | 0% | 88% |
| consenso | strong_buy | 11 | -2.07 EUR | 0% | 64% |
| tendencia tecnica | alcista | 17 | -3.66 EUR | 0% | 76% |
| tendencia tecnica | mixta | 8 | -3.54 EUR | 0% | 75% |
| tendencia analistas | mejorando | 16 | -3.54 EUR | 0% | 81% |
| tendencia analistas | estable | 10 | -4.19 EUR | 0% | 70% |
| regimen de mercado | favorable | 26 | -3.44 EUR | 0% | 77% |
| catalizador | sin catalizador | 27 | -3.61 EUR | 0% | 78% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -6.06 | -2.75 | **+3.31 EUR** |
| distancia max 52s | -6.26 | -4.19 | **+2.08 EUR** |
| RSI | -5.05 | -3.04 | **+2.02 EUR** |
| volumen relativo | -4.45 | -4.19 | **+0.26 EUR** |
| momentum 30d | -3.04 | -3.04 | **+0.00 EUR** |
| potencial hasta objetivo | -3.04 | -3.76 | **-0.73 EUR** |
| fuerza relativa | -2.03 | -3.04 | **-1.01 EUR** |
| dispersion | -2.03 | -3.04 | **-1.01 EUR** |
| volatilidad | -4.45 | -5.49 | **-1.04 EUR** |
| liquidez | -4.45 | -5.49 | **-1.04 EUR** |
| % compra fuerte | -3.54 | -5.10 | **-1.56 EUR** |
| puesto en el ranking | -2.75 | -6.06 | **-3.31 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
