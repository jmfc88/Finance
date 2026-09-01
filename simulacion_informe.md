# Simulacion en paralelo

Actualizado: 2026-09-01 21:02 · dia 9 de ejecucion
Proxima revision de ponderacion en 6 dias.

- Operaciones cerradas: **16**
- Operaciones abiertas: 50

> Con 16 operaciones cerradas todavia NO se puede concluir nada.
> Hacen falta bastantes decenas por tramo para que la comparacion
> signifique algo. Hasta entonces esto solo acumula datos.

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 3 | 19% | +1.85 EUR |
| plano | 0 | - | - |
| perdida | 5 | 31% | -6.26 EUR |
| nefasta | 8 | 50% | -1.27 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 5 | -2.12% | 0/5 (0%) | 2/5 | 6 |
| 11-20 | 6 | -0.51% | 0/6 (0%) | 0/6 | 4 |
| 21-30 | 5 | -4.45% | 0/5 (0%) | 0/5 | 5 |

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
| arranca antes (+3%) | -16.95 EUR | -5.65% | 0/3 | -10.00 EUR |
| LA REAL (escalera 25/08) | -35.94 EUR | -2.25% | 0/16 | -8.08 EUR |
| stop corto (5%) | -56.00 EUR | -7.00% | 0/8 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-2.25%**
- Aciertos (>= 5 EUR limpios): 0/16 (0%)
- Resultado acumulado ficticio: -35.94 EUR sobre 16 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 5 | -4.45 EUR | 0% | 100% |
| nota global | medio | 5 | -0.82 EUR | 0% | 80% |
| nota global | alto | 6 | -1.60 EUR | 0% | 67% |
| puesto en el ranking | bajo | 5 | -2.12 EUR | 0% | 60% |
| puesto en el ranking | medio | 5 | -0.82 EUR | 0% | 100% |
| puesto en el ranking | alto | 6 | -3.54 EUR | 0% | 83% |
| potencial hasta objetivo | bajo | 5 | -2.63 EUR | 0% | 80% |
| potencial hasta objetivo | medio | 5 | -2.63 EUR | 0% | 100% |
| potencial hasta objetivo | alto | 6 | -1.60 EUR | 0% | 67% |
| dispersion | bajo | 5 | -0.82 EUR | 0% | 60% |
| dispersion | medio | 5 | -6.26 EUR | 0% | 100% |
| dispersion | alto | 6 | -0.09 EUR | 0% | 83% |
| % compra fuerte | bajo | 5 | -2.63 EUR | 0% | 80% |
| % compra fuerte | medio | 5 | -0.82 EUR | 0% | 100% |
| % compra fuerte | alto | 6 | -3.12 EUR | 0% | 67% |
| momentum 30d | bajo | 5 | -4.45 EUR | 0% | 100% |
| momentum 30d | medio | 5 | -2.12 EUR | 0% | 60% |
| momentum 30d | alto | 6 | -0.51 EUR | 0% | 83% |
| fuerza relativa | bajo | 5 | -2.63 EUR | 0% | 80% |
| fuerza relativa | medio | 5 | -3.94 EUR | 0% | 80% |
| fuerza relativa | alto | 6 | -0.51 EUR | 0% | 83% |
| RSI | bajo | 5 | -6.26 EUR | 0% | 100% |
| RSI | medio | 5 | +1.51 EUR | 0% | 80% |
| RSI | alto | 6 | -2.03 EUR | 0% | 67% |
| consenso | buy | 9 | -4.04 EUR | 0% | 100% |
| consenso | strong_buy | 7 | +0.07 EUR | 0% | 57% |
| tendencia tecnica | alcista | 10 | -2.38 EUR | 0% | 80% |
| tendencia tecnica | mixta | 5 | -2.63 EUR | 0% | 80% |
| tendencia analistas | mejorando | 8 | -2.41 EUR | 0% | 100% |
| tendencia analistas | estable | 7 | -2.53 EUR | 0% | 57% |
| regimen de mercado | favorable | 16 | -2.25 EUR | 0% | 81% |
| catalizador | sin catalizador | 16 | -2.25 EUR | 0% | 81% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| RSI | -6.26 | -2.03 | **+4.24 EUR** |
| momentum 30d | -4.45 | -0.51 | **+3.93 EUR** |
| nota global | -4.45 | -1.60 | **+2.84 EUR** |
| fuerza relativa | -2.63 | -0.51 | **+2.12 EUR** |
| potencial hasta objetivo | -2.63 | -1.60 | **+1.03 EUR** |
| dispersion | -0.82 | -0.09 | **+0.73 EUR** |
| % compra fuerte | -2.63 | -3.12 | **-0.48 EUR** |
| puesto en el ranking | -2.12 | -3.54 | **-1.42 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
