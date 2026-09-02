# Simulacion en paralelo

Actualizado: 2026-09-02 11:13 · dia 10 de ejecucion
Proxima revision de ponderacion en 5 dias.

- Operaciones cerradas: **20**
- Operaciones abiertas: 47

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 4 | 20% | +1.64 EUR |
| plano | 0 | - | - |
| perdida | 5 | 25% | -6.26 EUR |
| nefasta | 11 | 55% | -3.13 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 7 | -2.53% | 0/7 (0%) | 2/7 | 6 |
| 11-20 | 6 | -0.51% | 0/6 (0%) | 0/6 | 4 |
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
| LA REAL (escalera 25/08) | -59.18 EUR | -2.96% | 0/20 | -8.08 EUR |
| stop corto (5%) | -77.00 EUR | -7.00% | 0/11 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-2.96%**
- Aciertos (>= 5 EUR limpios): 0/20 (0%)
- Resultado acumulado ficticio: -59.18 EUR sobre 20 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 6 | -5.05 EUR | 0% | 100% |
| nota global | medio | 6 | -2.03 EUR | 0% | 83% |
| nota global | alto | 8 | -2.09 EUR | 0% | 62% |
| puesto en el ranking | bajo | 6 | -3.12 EUR | 0% | 67% |
| puesto en el ranking | medio | 6 | -0.51 EUR | 0% | 83% |
| puesto en el ranking | alto | 8 | -4.67 EUR | 0% | 88% |
| potencial hasta objetivo | bajo | 6 | -2.03 EUR | 0% | 67% |
| potencial hasta objetivo | medio | 6 | -3.54 EUR | 0% | 100% |
| potencial hasta objetivo | alto | 8 | -3.22 EUR | 0% | 75% |
| dispersion | bajo | 6 | -2.03 EUR | 0% | 67% |
| dispersion | medio | 6 | -5.05 EUR | 0% | 83% |
| dispersion | alto | 8 | -2.09 EUR | 0% | 88% |
| % compra fuerte | bajo | 6 | -3.54 EUR | 0% | 67% |
| % compra fuerte | medio | 6 | -0.51 EUR | 0% | 100% |
| % compra fuerte | alto | 7 | -3.83 EUR | 0% | 71% |
| momentum 30d | bajo | 6 | -3.54 EUR | 0% | 83% |
| momentum 30d | medio | 6 | -3.12 EUR | 0% | 67% |
| momentum 30d | alto | 8 | -2.41 EUR | 0% | 88% |
| fuerza relativa | bajo | 6 | -2.03 EUR | 0% | 67% |
| fuerza relativa | medio | 6 | -4.63 EUR | 0% | 83% |
| fuerza relativa | alto | 8 | -2.41 EUR | 0% | 88% |
| RSI | bajo | 6 | -5.05 EUR | 0% | 100% |
| RSI | medio | 6 | -1.60 EUR | 0% | 83% |
| RSI | alto | 8 | -2.41 EUR | 0% | 62% |
| consenso | buy | 11 | -3.95 EUR | 0% | 91% |
| consenso | strong_buy | 9 | -1.74 EUR | 0% | 67% |
| tendencia tecnica | alcista | 13 | -3.00 EUR | 0% | 77% |
| tendencia tecnica | mixta | 6 | -3.54 EUR | 0% | 83% |
| tendencia analistas | mejorando | 10 | -2.63 EUR | 0% | 90% |
| tendencia analistas | estable | 9 | -3.76 EUR | 0% | 67% |
| regimen de mercado | favorable | 19 | -2.69 EUR | 0% | 79% |
| catalizador | sin catalizador | 20 | -2.96 EUR | 0% | 80% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.05 | -2.09 | **+2.97 EUR** |
| RSI | -5.05 | -2.41 | **+2.65 EUR** |
| momentum 30d | -3.54 | -2.41 | **+1.14 EUR** |
| dispersion | -2.03 | -2.09 | **-0.06 EUR** |
| % compra fuerte | -3.54 | -3.83 | **-0.29 EUR** |
| fuerza relativa | -2.03 | -2.41 | **-0.38 EUR** |
| potencial hasta objetivo | -2.03 | -3.22 | **-1.20 EUR** |
| puesto en el ranking | -3.12 | -4.67 | **-1.56 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
