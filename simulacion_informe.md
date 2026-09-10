# Simulacion en paralelo

Actualizado: 2026-09-10 11:14 · dia 18 de ejecucion
Proxima revision de ponderacion en 12 dias.

- Operaciones cerradas: **45**
- Operaciones abiertas: 62

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 16 | 36% | +1.16 EUR |
| plano | 0 | - | - |
| perdida | 13 | 29% | -7.38 EUR |
| nefasta | 16 | 36% | -4.67 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 15 | -1.86% | 0/15 (0%) | 4/15 | 7 |
| 11-20 | 15 | -2.03% | 0/15 (0%) | 1/15 | 5 |
| 21-30 | 15 | -6.26% | 0/15 (0%) | 0/15 | 5 |

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
| LA REAL (escalera 25/08) | -152.22 EUR | -3.38% | 0/45 | -8.08 EUR |
| stop corto (5%) | -175.00 EUR | -7.00% | 0/25 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.38%**
- Aciertos (>= 5 EUR limpios): 0/45 (0%)
- Resultado acumulado ficticio: -152.22 EUR sobre 45 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 15 | -5.05 EUR | 0% | 67% |
| nota global | medio | 15 | -2.63 EUR | 0% | 73% |
| nota global | alto | 15 | -2.46 EUR | 0% | 53% |
| puesto en el ranking | bajo | 15 | -1.86 EUR | 0% | 40% |
| puesto en el ranking | medio | 15 | -2.03 EUR | 0% | 60% |
| puesto en el ranking | alto | 15 | -6.26 EUR | 0% | 93% |
| potencial hasta objetivo | bajo | 15 | -3.24 EUR | 0% | 67% |
| potencial hasta objetivo | medio | 15 | -3.67 EUR | 0% | 67% |
| potencial hasta objetivo | alto | 15 | -3.24 EUR | 0% | 60% |
| dispersion | bajo | 15 | -1.42 EUR | 0% | 40% |
| dispersion | medio | 15 | -5.49 EUR | 0% | 80% |
| dispersion | alto | 15 | -3.24 EUR | 0% | 73% |
| % compra fuerte | bajo | 14 | -4.19 EUR | 0% | 64% |
| % compra fuerte | medio | 14 | -1.59 EUR | 0% | 64% |
| % compra fuerte | alto | 14 | -4.66 EUR | 0% | 71% |
| momentum 30d | bajo | 15 | -3.24 EUR | 0% | 60% |
| momentum 30d | medio | 15 | -4.28 EUR | 0% | 73% |
| momentum 30d | alto | 15 | -2.63 EUR | 0% | 60% |
| fuerza relativa | bajo | 15 | -2.63 EUR | 0% | 53% |
| fuerza relativa | medio | 15 | -4.28 EUR | 0% | 73% |
| fuerza relativa | alto | 15 | -3.24 EUR | 0% | 67% |
| RSI | bajo | 15 | -3.84 EUR | 0% | 60% |
| RSI | medio | 15 | -2.46 EUR | 0% | 67% |
| RSI | alto | 15 | -3.84 EUR | 0% | 67% |
| volumen relativo | bajo | 11 | -3.13 EUR | 0% | 55% |
| volumen relativo | medio | 11 | -3.95 EUR | 0% | 73% |
| volumen relativo | alto | 11 | -3.95 EUR | 0% | 55% |
| volatilidad | bajo | 11 | -3.95 EUR | 0% | 64% |
| volatilidad | medio | 11 | -4.78 EUR | 0% | 73% |
| volatilidad | alto | 11 | -2.30 EUR | 0% | 45% |
| liquidez | bajo | 11 | -3.95 EUR | 0% | 64% |
| liquidez | medio | 11 | -3.13 EUR | 0% | 64% |
| liquidez | alto | 11 | -3.95 EUR | 0% | 55% |
| distancia max 52s | bajo | 11 | -4.78 EUR | 0% | 64% |
| distancia max 52s | medio | 11 | -3.13 EUR | 0% | 64% |
| distancia max 52s | alto | 11 | -3.13 EUR | 0% | 55% |
| consenso | buy | 28 | -4.51 EUR | 0% | 75% |
| consenso | strong_buy | 17 | -1.52 EUR | 0% | 47% |
| tendencia tecnica | alcista | 29 | -2.98 EUR | 0% | 59% |
| tendencia tecnica | mixta | 10 | -3.54 EUR | 0% | 70% |
| tendencia tecnica | bajista | 6 | -5.05 EUR | 0% | 83% |
| tendencia analistas | mejorando | 24 | -3.16 EUR | 0% | 67% |
| tendencia analistas | estable | 15 | -5.49 EUR | 0% | 80% |
| regimen de mercado | favorable | 41 | -3.15 EUR | 0% | 63% |
| catalizador | sin catalizador | 45 | -3.38 EUR | 0% | 64% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.05 | -2.46 | **+2.59 EUR** |
| volatilidad | -3.95 | -2.30 | **+1.65 EUR** |
| distancia max 52s | -4.78 | -3.13 | **+1.65 EUR** |
| momentum 30d | -3.24 | -2.63 | **+0.61 EUR** |
| potencial hasta objetivo | -3.24 | -3.24 | **+0.00 EUR** |
| liquidez | -3.95 | -3.95 | **+0.00 EUR** |
| RSI | -3.84 | -3.84 | **+0.00 EUR** |
| % compra fuerte | -4.19 | -4.66 | **-0.47 EUR** |
| fuerza relativa | -2.63 | -3.24 | **-0.61 EUR** |
| volumen relativo | -3.13 | -3.95 | **-0.83 EUR** |
| dispersion | -1.42 | -3.24 | **-1.82 EUR** |
| puesto en el ranking | -1.86 | -6.26 | **-4.41 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
