# Simulacion en paralelo

Actualizado: 2026-09-02 05:47 · dia 10 de ejecucion
Proxima revision de ponderacion en 5 dias.

- Operaciones cerradas: **18**
- Operaciones abiertas: 48

> Con 18 operaciones cerradas todavia NO se puede concluir nada.
> Hacen falta bastantes decenas por tramo para que la comparacion
> signifique algo. Hasta entonces esto solo acumula datos.

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 3 | 17% | +1.85 EUR |
| plano | 0 | - | - |
| perdida | 5 | 28% | -6.26 EUR |
| nefasta | 10 | 56% | -2.63 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 5 | -2.12% | 0/5 (0%) | 2/5 | 6 |
| 11-20 | 6 | -0.51% | 0/6 (0%) | 0/6 | 4 |
| 21-30 | 7 | -5.49% | 0/7 (0%) | 0/7 | 4 |

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
| LA REAL (escalera 25/08) | -52.10 EUR | -2.89% | 0/18 | -8.08 EUR |
| stop corto (5%) | -70.00 EUR | -7.00% | 0/10 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-2.89%**
- Aciertos (>= 5 EUR limpios): 0/18 (0%)
- Resultado acumulado ficticio: -52.10 EUR sobre 18 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 6 | -5.05 EUR | 0% | 100% |
| nota global | medio | 6 | -2.03 EUR | 0% | 83% |
| nota global | alto | 6 | -1.60 EUR | 0% | 67% |
| puesto en el ranking | bajo | 6 | -1.60 EUR | 0% | 67% |
| puesto en el ranking | medio | 6 | -0.51 EUR | 0% | 83% |
| puesto en el ranking | alto | 6 | -6.57 EUR | 0% | 100% |
| potencial hasta objetivo | bajo | 6 | -3.54 EUR | 0% | 83% |
| potencial hasta objetivo | medio | 6 | -1.60 EUR | 0% | 83% |
| potencial hasta objetivo | alto | 6 | -3.54 EUR | 0% | 83% |
| dispersion | bajo | 6 | -2.03 EUR | 0% | 67% |
| dispersion | medio | 6 | -4.63 EUR | 0% | 83% |
| dispersion | alto | 6 | -2.03 EUR | 0% | 100% |
| % compra fuerte | bajo | 5 | -4.45 EUR | 0% | 80% |
| % compra fuerte | medio | 5 | +1.00 EUR | 0% | 100% |
| % compra fuerte | alto | 7 | -3.83 EUR | 0% | 71% |
| momentum 30d | bajo | 6 | -3.54 EUR | 0% | 83% |
| momentum 30d | medio | 6 | -1.60 EUR | 0% | 67% |
| momentum 30d | alto | 6 | -3.54 EUR | 0% | 100% |
| fuerza relativa | bajo | 6 | -3.54 EUR | 0% | 83% |
| fuerza relativa | medio | 6 | -1.60 EUR | 0% | 67% |
| fuerza relativa | alto | 6 | -3.54 EUR | 0% | 100% |
| RSI | bajo | 6 | -5.05 EUR | 0% | 100% |
| RSI | medio | 6 | -1.60 EUR | 0% | 83% |
| RSI | alto | 6 | -2.03 EUR | 0% | 67% |
| consenso | buy | 10 | -4.45 EUR | 0% | 100% |
| consenso | strong_buy | 8 | -0.95 EUR | 0% | 62% |
| tendencia tecnica | alcista | 11 | -2.90 EUR | 0% | 82% |
| tendencia tecnica | mixta | 6 | -3.54 EUR | 0% | 83% |
| tendencia analistas | mejorando | 9 | -3.04 EUR | 0% | 100% |
| tendencia analistas | estable | 8 | -3.22 EUR | 0% | 62% |
| regimen de mercado | favorable | 18 | -2.89 EUR | 0% | 83% |
| catalizador | sin catalizador | 18 | -2.89 EUR | 0% | 83% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.05 | -1.60 | **+3.45 EUR** |
| RSI | -5.05 | -2.03 | **+3.03 EUR** |
| % compra fuerte | -4.45 | -3.83 | **+0.62 EUR** |
| potencial hasta objetivo | -3.54 | -3.54 | **+0.00 EUR** |
| momentum 30d | -3.54 | -3.54 | **+0.00 EUR** |
| fuerza relativa | -3.54 | -3.54 | **+0.00 EUR** |
| dispersion | -2.03 | -2.03 | **+0.00 EUR** |
| puesto en el ranking | -1.60 | -6.57 | **-4.96 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
