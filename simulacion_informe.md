# Simulacion en paralelo

Actualizado: 2026-09-01 12:57 · dia 9 de ejecucion
Proxima revision de ponderacion en 6 dias.

- Operaciones cerradas: **13**
- Operaciones abiertas: 46

> Con 13 operaciones cerradas todavia NO se puede concluir nada.
> Hacen falta bastantes decenas por tramo para que la comparacion
> signifique algo. Hasta entonces esto solo acumula datos.

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 3 | 23% | +1.85 EUR |
| plano | 0 | - | - |
| perdida | 3 | 23% | -5.05 EUR |
| nefasta | 7 | 54% | -0.30 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 4 | -0.64% | 0/4 (0%) | 2/4 | 6 |
| 11-20 | 5 | +1.00% | 0/5 (0%) | 0/5 | 4 |
| 21-30 | 4 | -3.54% | 0/4 (0%) | 0/4 | 5 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida


## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -7.15 EUR | -2.38% | 0/3 | -10.00 EUR |
| trailing suelto (7%) | -10.00 EUR | -10.00% | 0/1 | -10.00 EUR |
| sin trailing, solo stop | -10.00 EUR | -10.00% | 0/1 | -10.00 EUR |
| arranca despues (+8%) | -10.00 EUR | -10.00% | 0/1 | -10.00 EUR |
| actual (8% / +5% / 5%) | -10.00 EUR | -10.00% | 0/1 | -10.00 EUR |
| LA REAL (escalera 25/08) | -11.70 EUR | -0.90% | 0/13 | -8.08 EUR |
| arranca antes (+3%) | -16.95 EUR | -5.65% | 0/3 | -10.00 EUR |
| stop corto (5%) | -35.00 EUR | -7.00% | 0/5 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-0.90%**
- Aciertos (>= 5 EUR limpios): 0/13 (0%)
- Resultado acumulado ficticio: -11.70 EUR sobre 13 x 100 EUR

## Analisis por factor

Solo hay 13 operaciones cerradas. Hacen falta al menos
15 para que partir en grupos signifique algo.
