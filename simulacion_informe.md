# Simulacion en paralelo

Actualizado: 2026-09-10 05:57 · dia 18 de ejecucion
Proxima revision de ponderacion en 12 dias.

- Operaciones cerradas: **43**
- Operaciones abiertas: 64

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 15 | 35% | +1.17 EUR |
| plano | 0 | - | - |
| perdida | 13 | 30% | -7.38 EUR |
| nefasta | 15 | 35% | -4.45 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 15 | -1.86% | 0/15 (0%) | 4/15 | 7 |
| 11-20 | 15 | -2.03% | 0/15 (0%) | 1/15 | 5 |
| 21-30 | 13 | -6.68% | 0/13 (0%) | 0/13 | 5 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida


## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -14.73 EUR | -2.46% | 0/6 | -10.00 EUR |
| trailing suelto (7%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| sin trailing, solo stop | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| arranca despues (+8%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| actual (8% / +5% / 5%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| arranca antes (+3%) | -26.95 EUR | -6.74% | 0/4 | -10.00 EUR |
| LA REAL (escalera 25/08) | -145.14 EUR | -3.38% | 0/43 | -8.08 EUR |
| stop corto (5%) | -168.00 EUR | -7.00% | 0/24 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.38%**
- Aciertos (>= 5 EUR limpios): 0/43 (0%)
- Resultado acumulado ficticio: -145.14 EUR sobre 43 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 14 | -5.49 EUR | 0% | 71% |
| nota global | medio | 14 | -2.24 EUR | 0% | 71% |
| nota global | alto | 15 | -2.46 EUR | 0% | 53% |
| puesto en el ranking | bajo | 14 | -2.06 EUR | 0% | 43% |
| puesto en el ranking | medio | 14 | -2.24 EUR | 0% | 64% |
| puesto en el ranking | alto | 15 | -5.66 EUR | 0% | 87% |
| potencial hasta objetivo | bajo | 14 | -3.54 EUR | 0% | 64% |
| potencial hasta objetivo | medio | 14 | -3.54 EUR | 0% | 71% |
| potencial hasta objetivo | alto | 15 | -3.07 EUR | 0% | 60% |
| dispersion | bajo | 14 | -1.59 EUR | 0% | 43% |
| dispersion | medio | 14 | -5.30 EUR | 0% | 79% |
| dispersion | alto | 15 | -3.24 EUR | 0% | 73% |
| % compra fuerte | bajo | 13 | -3.89 EUR | 0% | 62% |
| % compra fuerte | medio | 13 | -1.79 EUR | 0% | 69% |
| % compra fuerte | alto | 14 | -4.66 EUR | 0% | 71% |
| momentum 30d | bajo | 14 | -3.54 EUR | 0% | 64% |
| momentum 30d | medio | 14 | -4.01 EUR | 0% | 71% |
| momentum 30d | alto | 15 | -2.63 EUR | 0% | 60% |
| fuerza relativa | bajo | 14 | -2.89 EUR | 0% | 57% |
| fuerza relativa | medio | 14 | -4.01 EUR | 0% | 71% |
| fuerza relativa | alto | 15 | -3.24 EUR | 0% | 67% |
| RSI | bajo | 14 | -4.19 EUR | 0% | 64% |
| RSI | medio | 14 | -2.06 EUR | 0% | 64% |
| RSI | alto | 15 | -3.84 EUR | 0% | 67% |
| volumen relativo | bajo | 10 | -3.54 EUR | 0% | 60% |
| volumen relativo | medio | 10 | -3.54 EUR | 0% | 70% |
| volumen relativo | alto | 11 | -3.95 EUR | 0% | 55% |
| volatilidad | bajo | 10 | -4.45 EUR | 0% | 70% |
| volatilidad | medio | 10 | -4.45 EUR | 0% | 70% |
| volatilidad | alto | 11 | -2.30 EUR | 0% | 45% |
| liquidez | bajo | 10 | -3.54 EUR | 0% | 60% |
| liquidez | medio | 10 | -3.54 EUR | 0% | 70% |
| liquidez | alto | 11 | -3.95 EUR | 0% | 55% |
| distancia max 52s | bajo | 10 | -4.45 EUR | 0% | 60% |
| distancia max 52s | medio | 10 | -3.54 EUR | 0% | 70% |
| distancia max 52s | alto | 11 | -3.13 EUR | 0% | 55% |
| consenso | buy | 26 | -4.59 EUR | 0% | 77% |
| consenso | strong_buy | 17 | -1.52 EUR | 0% | 47% |
| tendencia tecnica | alcista | 29 | -2.98 EUR | 0% | 59% |
| tendencia tecnica | mixta | 10 | -3.54 EUR | 0% | 70% |
| tendencia analistas | mejorando | 23 | -2.95 EUR | 0% | 65% |
| tendencia analistas | estable | 15 | -5.49 EUR | 0% | 80% |
| regimen de mercado | favorable | 41 | -3.15 EUR | 0% | 63% |
| catalizador | sin catalizador | 43 | -3.38 EUR | 0% | 65% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.49 | -2.46 | **+3.02 EUR** |
| volatilidad | -4.45 | -2.30 | **+2.15 EUR** |
| distancia max 52s | -4.45 | -3.13 | **+1.32 EUR** |
| momentum 30d | -3.54 | -2.63 | **+0.91 EUR** |
| potencial hasta objetivo | -3.54 | -3.07 | **+0.47 EUR** |
| RSI | -4.19 | -3.84 | **+0.35 EUR** |
| fuerza relativa | -2.89 | -3.24 | **-0.35 EUR** |
| volumen relativo | -3.54 | -3.95 | **-0.41 EUR** |
| liquidez | -3.54 | -3.95 | **-0.41 EUR** |
| % compra fuerte | -3.89 | -4.66 | **-0.77 EUR** |
| dispersion | -1.59 | -3.24 | **-1.64 EUR** |
| puesto en el ranking | -2.06 | -5.66 | **-3.60 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
