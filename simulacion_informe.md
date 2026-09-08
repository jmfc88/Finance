# Simulacion en paralelo

Actualizado: 2026-09-08 05:57 · dia 16 de ejecucion
**Revision nº1 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **29**
- Operaciones abiertas: 68

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 7 | 24% | +1.36 EUR |
| plano | 0 | - | - |
| perdida | 9 | 31% | -7.07 EUR |
| nefasta | 13 | 45% | -3.89 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 10 | -2.38% | 0/10 (0%) | 3/10 | 6 |
| 11-20 | 9 | -2.03% | 0/9 (0%) | 0/9 | 4 |
| 21-30 | 10 | -6.26% | 0/10 (0%) | 0/10 | 5 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida


## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -15.76 EUR | -3.15% | 0/5 | -10.00 EUR |
| trailing suelto (7%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| sin trailing, solo stop | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| arranca despues (+8%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| actual (8% / +5% / 5%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| arranca antes (+3%) | -26.95 EUR | -6.74% | 0/4 | -10.00 EUR |
| LA REAL (escalera 25/08) | -104.66 EUR | -3.61% | 0/29 | -8.08 EUR |
| stop corto (5%) | -119.00 EUR | -7.00% | 0/17 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.61%**
- Aciertos (>= 5 EUR limpios): 0/29 (0%)
- Resultado acumulado ficticio: -104.66 EUR sobre 29 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 9 | -7.07 EUR | 0% | 89% |
| nota global | medio | 9 | -2.03 EUR | 0% | 89% |
| nota global | alto | 11 | -2.07 EUR | 0% | 55% |
| puesto en el ranking | bajo | 9 | -1.74 EUR | 0% | 44% |
| puesto en el ranking | medio | 9 | -2.03 EUR | 0% | 78% |
| puesto en el ranking | alto | 11 | -6.43 EUR | 0% | 100% |
| potencial hasta objetivo | bajo | 9 | -3.04 EUR | 0% | 67% |
| potencial hasta objetivo | medio | 9 | -3.04 EUR | 0% | 78% |
| potencial hasta objetivo | alto | 11 | -4.55 EUR | 0% | 82% |
| dispersion | bajo | 9 | -2.03 EUR | 0% | 56% |
| dispersion | medio | 9 | -6.06 EUR | 0% | 89% |
| dispersion | alto | 11 | -2.90 EUR | 0% | 82% |
| % compra fuerte | bajo | 9 | -4.04 EUR | 0% | 67% |
| % compra fuerte | medio | 9 | -1.02 EUR | 0% | 78% |
| % compra fuerte | alto | 10 | -5.10 EUR | 0% | 80% |
| momentum 30d | bajo | 9 | -3.04 EUR | 0% | 67% |
| momentum 30d | medio | 9 | -4.77 EUR | 0% | 78% |
| momentum 30d | alto | 11 | -3.13 EUR | 0% | 82% |
| fuerza relativa | bajo | 9 | -2.03 EUR | 0% | 56% |
| fuerza relativa | medio | 9 | -5.78 EUR | 0% | 89% |
| fuerza relativa | alto | 11 | -3.13 EUR | 0% | 82% |
| RSI | bajo | 9 | -5.05 EUR | 0% | 78% |
| RSI | medio | 9 | -2.75 EUR | 0% | 89% |
| RSI | alto | 11 | -3.13 EUR | 0% | 64% |
| volumen relativo | bajo | 6 | -5.05 EUR | 0% | 83% |
| volumen relativo | medio | 6 | -5.05 EUR | 0% | 100% |
| volumen relativo | alto | 7 | -4.19 EUR | 0% | 57% |
| volatilidad | bajo | 6 | -5.05 EUR | 0% | 83% |
| volatilidad | medio | 6 | -5.05 EUR | 0% | 83% |
| volatilidad | alto | 7 | -4.19 EUR | 0% | 71% |
| liquidez | bajo | 6 | -3.54 EUR | 0% | 67% |
| liquidez | medio | 6 | -5.05 EUR | 0% | 83% |
| liquidez | alto | 7 | -5.49 EUR | 0% | 86% |
| distancia max 52s | bajo | 6 | -5.05 EUR | 0% | 83% |
| distancia max 52s | medio | 6 | -5.05 EUR | 0% | 83% |
| distancia max 52s | alto | 7 | -4.19 EUR | 0% | 71% |
| consenso | buy | 17 | -4.88 EUR | 0% | 88% |
| consenso | strong_buy | 12 | -1.82 EUR | 0% | 58% |
| tendencia tecnica | alcista | 19 | -3.65 EUR | 0% | 74% |
| tendencia tecnica | mixta | 8 | -3.54 EUR | 0% | 75% |
| tendencia analistas | mejorando | 17 | -3.27 EUR | 0% | 76% |
| tendencia analistas | estable | 11 | -4.55 EUR | 0% | 73% |
| regimen de mercado | favorable | 28 | -3.45 EUR | 0% | 75% |
| catalizador | sin catalizador | 29 | -3.61 EUR | 0% | 76% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -7.07 | -2.07 | **+5.00 EUR** |
| RSI | -5.05 | -3.13 | **+1.93 EUR** |
| volumen relativo | -5.05 | -4.19 | **+0.86 EUR** |
| volatilidad | -5.05 | -4.19 | **+0.86 EUR** |
| distancia max 52s | -5.05 | -4.19 | **+0.86 EUR** |
| momentum 30d | -3.04 | -3.13 | **-0.09 EUR** |
| dispersion | -2.03 | -2.90 | **-0.87 EUR** |
| % compra fuerte | -4.04 | -5.10 | **-1.06 EUR** |
| fuerza relativa | -2.03 | -3.13 | **-1.10 EUR** |
| potencial hasta objetivo | -3.04 | -4.55 | **-1.51 EUR** |
| liquidez | -3.54 | -5.49 | **-1.95 EUR** |
| puesto en el ranking | -1.74 | -6.43 | **-4.68 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
