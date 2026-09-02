# Simulacion en paralelo

Actualizado: 2026-09-02 17:10 · dia 10 de ejecucion
Proxima revision de ponderacion en 5 dias.

- Operaciones cerradas: **23**
- Operaciones abiertas: 54

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 5 | 22% | +1.51 EUR |
| plano | 0 | - | - |
| perdida | 6 | 26% | -6.57 EUR |
| nefasta | 12 | 52% | -3.54 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 8 | -2.09% | 0/8 (0%) | 2/8 | 6 |
| 11-20 | 7 | -1.59% | 0/7 (0%) | 0/7 | 3 |
| 21-30 | 8 | -5.81% | 0/8 (0%) | 0/8 | 4 |

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
| LA REAL (escalera 25/08) | -74.34 EUR | -3.23% | 0/23 | -8.08 EUR |
| stop corto (5%) | -91.00 EUR | -7.00% | 0/13 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.23%**
- Aciertos (>= 5 EUR limpios): 0/23 (0%)
- Resultado acumulado ficticio: -74.34 EUR sobre 23 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 7 | -6.78 EUR | 0% | 100% |
| nota global | medio | 7 | -1.59 EUR | 0% | 86% |
| nota global | alto | 9 | -1.74 EUR | 0% | 56% |
| puesto en el ranking | bajo | 7 | -2.53 EUR | 0% | 57% |
| puesto en el ranking | medio | 7 | -1.59 EUR | 0% | 86% |
| puesto en el ranking | alto | 9 | -5.05 EUR | 0% | 89% |
| potencial hasta objetivo | bajo | 7 | -2.89 EUR | 0% | 71% |
| potencial hasta objetivo | medio | 7 | -2.89 EUR | 0% | 86% |
| potencial hasta objetivo | alto | 9 | -3.76 EUR | 0% | 78% |
| dispersion | bajo | 7 | -1.59 EUR | 0% | 57% |
| dispersion | medio | 7 | -5.49 EUR | 0% | 86% |
| dispersion | alto | 9 | -2.75 EUR | 0% | 89% |
| % compra fuerte | bajo | 7 | -2.89 EUR | 0% | 57% |
| % compra fuerte | medio | 7 | -1.59 EUR | 0% | 100% |
| % compra fuerte | alto | 8 | -4.36 EUR | 0% | 75% |
| momentum 30d | bajo | 7 | -2.89 EUR | 0% | 71% |
| momentum 30d | medio | 7 | -3.83 EUR | 0% | 71% |
| momentum 30d | alto | 9 | -3.04 EUR | 0% | 89% |
| fuerza relativa | bajo | 7 | -1.59 EUR | 0% | 57% |
| fuerza relativa | medio | 7 | -5.12 EUR | 0% | 86% |
| fuerza relativa | alto | 9 | -3.04 EUR | 0% | 89% |
| RSI | bajo | 7 | -5.49 EUR | 0% | 86% |
| RSI | medio | 7 | -1.23 EUR | 0% | 86% |
| RSI | alto | 9 | -3.04 EUR | 0% | 67% |
| consenso | buy | 13 | -4.59 EUR | 0% | 92% |
| consenso | strong_buy | 10 | -1.47 EUR | 0% | 60% |
| tendencia tecnica | alcista | 14 | -3.36 EUR | 0% | 79% |
| tendencia tecnica | mixta | 7 | -2.89 EUR | 0% | 71% |
| tendencia analistas | mejorando | 13 | -3.19 EUR | 0% | 85% |
| tendencia analistas | estable | 9 | -3.76 EUR | 0% | 67% |
| regimen de mercado | favorable | 22 | -3.01 EUR | 0% | 77% |
| catalizador | sin catalizador | 23 | -3.23 EUR | 0% | 78% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -6.78 | -1.74 | **+5.04 EUR** |
| RSI | -5.49 | -3.04 | **+2.45 EUR** |
| momentum 30d | -2.89 | -3.04 | **-0.14 EUR** |
| potencial hasta objetivo | -2.89 | -3.76 | **-0.87 EUR** |
| dispersion | -1.59 | -2.75 | **-1.16 EUR** |
| fuerza relativa | -1.59 | -3.04 | **-1.44 EUR** |
| % compra fuerte | -2.89 | -4.36 | **-1.47 EUR** |
| puesto en el ranking | -2.53 | -5.05 | **-2.52 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
