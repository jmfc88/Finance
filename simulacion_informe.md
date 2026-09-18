# Simulacion en paralelo

Actualizado: 2026-09-18 11:08 · dia 26 de ejecucion
Proxima revision de ponderacion en 4 dias.

- Operaciones cerradas: **65**
- Operaciones abiertas: 63

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 19 | 29% | +1.13 EUR |
| plano | 0 | - | - |
| perdida | 23 | 35% | -7.69 EUR |
| nefasta | 23 | 35% | -5.71 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 17 | -2.59% | 0/17 (0%) | 4/17 | 7 |
| 11-20 | 21 | -3.32% | 0/21 (0%) | 1/21 | 6 |
| 21-30 | 27 | -6.40% | 0/27 (0%) | 0/27 | 6 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida


## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -34.73 EUR | -4.34% | 0/8 | -10.00 EUR |
| trailing suelto (7%) | -40.00 EUR | -10.00% | 0/4 | -10.00 EUR |
| sin trailing, solo stop | -40.00 EUR | -10.00% | 0/4 | -10.00 EUR |
| arranca despues (+8%) | -40.00 EUR | -10.00% | 0/4 | -10.00 EUR |
| actual (8% / +5% / 5%) | -40.00 EUR | -10.00% | 0/4 | -10.00 EUR |
| arranca antes (+3%) | -50.41 EUR | -7.20% | 0/7 | -10.00 EUR |
| LA REAL (escalera 25/08) | -286.58 EUR | -4.41% | 0/65 | -8.08 EUR |
| stop corto (5%) | -294.00 EUR | -7.00% | 0/42 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-4.41%**
- Aciertos (>= 5 EUR limpios): 0/65 (0%)
- Resultado acumulado ficticio: -286.58 EUR sobre 65 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 21 | -5.49 EUR | 0% | 71% |
| nota global | medio | 21 | -5.49 EUR | 0% | 86% |
| nota global | alto | 23 | -2.44 EUR | 0% | 57% |
| puesto en el ranking | bajo | 21 | -2.34 EUR | 0% | 52% |
| puesto en el ranking | medio | 21 | -4.19 EUR | 0% | 71% |
| puesto en el ranking | alto | 23 | -6.50 EUR | 0% | 87% |
| potencial hasta objetivo | bajo | 21 | -5.05 EUR | 0% | 76% |
| potencial hasta objetivo | medio | 21 | -4.62 EUR | 0% | 76% |
| potencial hasta objetivo | alto | 23 | -3.63 EUR | 0% | 61% |
| dispersion | bajo | 21 | -2.89 EUR | 0% | 52% |
| dispersion | medio | 21 | -5.80 EUR | 0% | 81% |
| dispersion | alto | 23 | -4.53 EUR | 0% | 78% |
| % compra fuerte | bajo | 20 | -5.81 EUR | 0% | 80% |
| % compra fuerte | medio | 20 | -3.09 EUR | 0% | 70% |
| % compra fuerte | alto | 21 | -4.93 EUR | 0% | 71% |
| momentum 30d | bajo | 21 | -3.76 EUR | 0% | 62% |
| momentum 30d | medio | 21 | -5.80 EUR | 0% | 81% |
| momentum 30d | alto | 23 | -3.74 EUR | 0% | 70% |
| fuerza relativa | bajo | 21 | -3.32 EUR | 0% | 57% |
| fuerza relativa | medio | 21 | -5.80 EUR | 0% | 86% |
| fuerza relativa | alto | 23 | -4.13 EUR | 0% | 70% |
| RSI | bajo | 21 | -4.19 EUR | 0% | 62% |
| RSI | medio | 21 | -3.64 EUR | 0% | 71% |
| RSI | alto | 23 | -5.32 EUR | 0% | 78% |
| volumen relativo | bajo | 17 | -4.34 EUR | 0% | 65% |
| volumen relativo | medio | 17 | -4.34 EUR | 0% | 71% |
| volumen relativo | alto | 17 | -5.41 EUR | 0% | 71% |
| volatilidad | bajo | 17 | -4.88 EUR | 0% | 71% |
| volatilidad | medio | 17 | -6.48 EUR | 0% | 88% |
| volatilidad | alto | 17 | -2.74 EUR | 0% | 47% |
| liquidez | bajo | 17 | -4.88 EUR | 0% | 71% |
| liquidez | medio | 17 | -4.34 EUR | 0% | 71% |
| liquidez | alto | 17 | -4.88 EUR | 0% | 65% |
| distancia max 52s | bajo | 17 | -4.88 EUR | 0% | 65% |
| distancia max 52s | medio | 17 | -3.81 EUR | 0% | 65% |
| distancia max 52s | alto | 17 | -5.41 EUR | 0% | 76% |
| consenso | buy | 45 | -5.46 EUR | 0% | 80% |
| consenso | strong_buy | 20 | -2.05 EUR | 0% | 50% |
| tendencia tecnica | alcista | 41 | -4.25 EUR | 0% | 68% |
| tendencia tecnica | mixta | 15 | -4.45 EUR | 0% | 73% |
| tendencia tecnica | bajista | 9 | -5.05 EUR | 0% | 78% |
| tendencia analistas | mejorando | 36 | -4.30 EUR | 0% | 72% |
| tendencia analistas | estable | 20 | -6.14 EUR | 0% | 85% |
| regimen de mercado | favorable | 54 | -4.17 EUR | 0% | 70% |
| regimen de mercado | neutro | 11 | -5.60 EUR | 0% | 73% |
| catalizador | sin catalizador | 64 | -4.35 EUR | 0% | 70% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.49 | -2.44 | **+3.04 EUR** |
| volatilidad | -4.88 | -2.74 | **+2.14 EUR** |
| potencial hasta objetivo | -5.05 | -3.63 | **+1.43 EUR** |
| % compra fuerte | -5.81 | -4.93 | **+0.88 EUR** |
| momentum 30d | -3.76 | -3.74 | **+0.02 EUR** |
| liquidez | -4.88 | -4.88 | **+0.00 EUR** |
| distancia max 52s | -4.88 | -5.41 | **-0.53 EUR** |
| fuerza relativa | -3.32 | -4.13 | **-0.81 EUR** |
| volumen relativo | -4.34 | -5.41 | **-1.07 EUR** |
| RSI | -4.19 | -5.32 | **-1.13 EUR** |
| dispersion | -2.89 | -4.53 | **-1.64 EUR** |
| puesto en el ranking | -2.34 | -6.50 | **-4.16 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
