# Simulacion en paralelo

Actualizado: 2026-09-09 20:56 · dia 17 de ejecucion
**Revision nº1 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **42**
- Operaciones abiertas: 65

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 14 | 33% | +1.18 EUR |
| plano | 0 | - | - |
| perdida | 13 | 31% | -7.38 EUR |
| nefasta | 15 | 36% | -4.45 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 15 | -1.86% | 0/15 (0%) | 4/15 | 7 |
| 11-20 | 14 | -2.24% | 0/14 (0%) | 1/14 | 5 |
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
| LA REAL (escalera 25/08) | -146.14 EUR | -3.48% | 0/42 | -8.08 EUR |
| stop corto (5%) | -168.00 EUR | -7.00% | 0/24 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.48%**
- Aciertos (>= 5 EUR limpios): 0/42 (0%)
- Resultado acumulado ficticio: -146.14 EUR sobre 42 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 14 | -6.13 EUR | 0% | 79% |
| nota global | medio | 14 | -1.59 EUR | 0% | 71% |
| nota global | alto | 14 | -2.71 EUR | 0% | 50% |
| puesto en el ranking | bajo | 14 | -2.06 EUR | 0% | 43% |
| puesto en el ranking | medio | 14 | -2.24 EUR | 0% | 64% |
| puesto en el ranking | alto | 14 | -6.13 EUR | 0% | 93% |
| potencial hasta objetivo | bajo | 14 | -3.54 EUR | 0% | 64% |
| potencial hasta objetivo | medio | 14 | -3.54 EUR | 0% | 71% |
| potencial hasta objetivo | alto | 14 | -3.36 EUR | 0% | 64% |
| dispersion | bajo | 14 | -1.59 EUR | 0% | 43% |
| dispersion | medio | 14 | -5.30 EUR | 0% | 79% |
| dispersion | alto | 14 | -3.54 EUR | 0% | 79% |
| % compra fuerte | bajo | 13 | -3.89 EUR | 0% | 62% |
| % compra fuerte | medio | 13 | -1.79 EUR | 0% | 69% |
| % compra fuerte | alto | 14 | -4.66 EUR | 0% | 71% |
| momentum 30d | bajo | 14 | -3.54 EUR | 0% | 64% |
| momentum 30d | medio | 14 | -4.01 EUR | 0% | 71% |
| momentum 30d | alto | 14 | -2.89 EUR | 0% | 64% |
| fuerza relativa | bajo | 14 | -2.89 EUR | 0% | 57% |
| fuerza relativa | medio | 14 | -4.01 EUR | 0% | 71% |
| fuerza relativa | alto | 14 | -3.54 EUR | 0% | 71% |
| RSI | bajo | 14 | -4.19 EUR | 0% | 64% |
| RSI | medio | 14 | -2.71 EUR | 0% | 71% |
| RSI | alto | 14 | -3.54 EUR | 0% | 64% |
| volumen relativo | bajo | 10 | -3.54 EUR | 0% | 60% |
| volumen relativo | medio | 10 | -3.54 EUR | 0% | 70% |
| volumen relativo | alto | 10 | -4.45 EUR | 0% | 60% |
| volatilidad | bajo | 10 | -4.45 EUR | 0% | 70% |
| volatilidad | medio | 10 | -4.45 EUR | 0% | 70% |
| volatilidad | alto | 10 | -2.63 EUR | 0% | 50% |
| liquidez | bajo | 10 | -3.54 EUR | 0% | 60% |
| liquidez | medio | 10 | -4.45 EUR | 0% | 80% |
| liquidez | alto | 10 | -3.54 EUR | 0% | 50% |
| distancia max 52s | bajo | 10 | -4.45 EUR | 0% | 70% |
| distancia max 52s | medio | 10 | -3.54 EUR | 0% | 60% |
| distancia max 52s | alto | 10 | -3.54 EUR | 0% | 60% |
| consenso | buy | 26 | -4.59 EUR | 0% | 77% |
| consenso | strong_buy | 16 | -1.68 EUR | 0% | 50% |
| tendencia tecnica | alcista | 28 | -3.12 EUR | 0% | 61% |
| tendencia tecnica | mixta | 10 | -3.54 EUR | 0% | 70% |
| tendencia analistas | mejorando | 23 | -2.95 EUR | 0% | 65% |
| tendencia analistas | estable | 15 | -5.49 EUR | 0% | 80% |
| regimen de mercado | favorable | 40 | -3.25 EUR | 0% | 65% |
| catalizador | sin catalizador | 42 | -3.48 EUR | 0% | 67% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -6.13 | -2.71 | **+3.42 EUR** |
| volatilidad | -4.45 | -2.63 | **+1.82 EUR** |
| distancia max 52s | -4.45 | -3.54 | **+0.91 EUR** |
| momentum 30d | -3.54 | -2.89 | **+0.65 EUR** |
| RSI | -4.19 | -3.54 | **+0.65 EUR** |
| potencial hasta objetivo | -3.54 | -3.36 | **+0.18 EUR** |
| liquidez | -3.54 | -3.54 | **+0.00 EUR** |
| fuerza relativa | -2.89 | -3.54 | **-0.65 EUR** |
| % compra fuerte | -3.89 | -4.66 | **-0.77 EUR** |
| volumen relativo | -3.54 | -4.45 | **-0.91 EUR** |
| dispersion | -1.59 | -3.54 | **-1.95 EUR** |
| puesto en el ranking | -2.06 | -6.13 | **-4.07 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
