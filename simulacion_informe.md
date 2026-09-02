# Simulacion en paralelo

Actualizado: 2026-09-02 13:42 · dia 10 de ejecucion
Proxima revision de ponderacion en 5 dias.

- Operaciones cerradas: **21**
- Operaciones abiertas: 54

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 4 | 19% | +1.64 EUR |
| plano | 0 | - | - |
| perdida | 5 | 24% | -6.26 EUR |
| nefasta | 12 | 57% | -3.54 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 7 | -2.53% | 0/7 (0%) | 2/7 | 6 |
| 11-20 | 7 | -1.59% | 0/7 (0%) | 0/7 | 3 |
| 21-30 | 7 | -5.49% | 0/7 (0%) | 0/7 | 4 |

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
| LA REAL (escalera 25/08) | -67.26 EUR | -3.20% | 0/21 | -8.08 EUR |
| stop corto (5%) | -84.00 EUR | -7.00% | 0/12 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.20%**
- Aciertos (>= 5 EUR limpios): 0/21 (0%)
- Resultado acumulado ficticio: -67.26 EUR sobre 21 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 7 | -5.49 EUR | 0% | 100% |
| nota global | medio | 7 | -1.59 EUR | 0% | 86% |
| nota global | alto | 7 | -2.53 EUR | 0% | 57% |
| puesto en el ranking | bajo | 7 | -2.53 EUR | 0% | 57% |
| puesto en el ranking | medio | 7 | -1.59 EUR | 0% | 86% |
| puesto en el ranking | alto | 7 | -5.49 EUR | 0% | 100% |
| potencial hasta objetivo | bajo | 7 | -2.89 EUR | 0% | 71% |
| potencial hasta objetivo | medio | 7 | -2.53 EUR | 0% | 86% |
| potencial hasta objetivo | alto | 7 | -4.19 EUR | 0% | 86% |
| dispersion | bajo | 7 | -1.59 EUR | 0% | 57% |
| dispersion | medio | 7 | -5.12 EUR | 0% | 86% |
| dispersion | alto | 7 | -2.89 EUR | 0% | 100% |
| % compra fuerte | bajo | 6 | -3.54 EUR | 0% | 67% |
| % compra fuerte | medio | 6 | -0.51 EUR | 0% | 100% |
| % compra fuerte | alto | 8 | -4.36 EUR | 0% | 75% |
| momentum 30d | bajo | 7 | -4.19 EUR | 0% | 86% |
| momentum 30d | medio | 7 | -2.53 EUR | 0% | 71% |
| momentum 30d | alto | 7 | -2.89 EUR | 0% | 86% |
| fuerza relativa | bajo | 7 | -2.89 EUR | 0% | 71% |
| fuerza relativa | medio | 7 | -3.83 EUR | 0% | 86% |
| fuerza relativa | alto | 7 | -2.89 EUR | 0% | 86% |
| RSI | bajo | 7 | -4.19 EUR | 0% | 100% |
| RSI | medio | 7 | -2.53 EUR | 0% | 71% |
| RSI | alto | 7 | -2.89 EUR | 0% | 71% |
| consenso | buy | 12 | -4.30 EUR | 0% | 92% |
| consenso | strong_buy | 9 | -1.74 EUR | 0% | 67% |
| tendencia tecnica | alcista | 14 | -3.36 EUR | 0% | 79% |
| tendencia tecnica | mixta | 6 | -3.54 EUR | 0% | 83% |
| tendencia analistas | mejorando | 11 | -3.13 EUR | 0% | 91% |
| tendencia analistas | estable | 9 | -3.76 EUR | 0% | 67% |
| regimen de mercado | favorable | 20 | -2.96 EUR | 0% | 80% |
| catalizador | sin catalizador | 21 | -3.20 EUR | 0% | 81% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.49 | -2.53 | **+2.96 EUR** |
| momentum 30d | -4.19 | -2.89 | **+1.30 EUR** |
| RSI | -4.19 | -2.89 | **+1.30 EUR** |
| fuerza relativa | -2.89 | -2.89 | **+0.00 EUR** |
| % compra fuerte | -3.54 | -4.36 | **-0.82 EUR** |
| potencial hasta objetivo | -2.89 | -4.19 | **-1.30 EUR** |
| dispersion | -1.59 | -2.89 | **-1.30 EUR** |
| puesto en el ranking | -2.53 | -5.49 | **-2.96 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
