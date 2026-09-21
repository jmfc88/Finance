# Simulacion en paralelo

Actualizado: 2026-09-21 06:17 · dia 29 de ejecucion
Proxima revision de ponderacion en 1 dia.

- Operaciones cerradas: **67**
- Operaciones abiertas: 65

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 21 | 31% | +1.12 EUR |
| plano | 0 | - | - |
| perdida | 23 | 34% | -7.69 EUR |
| nefasta | 23 | 34% | -5.71 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 18 | -2.39% | 0/18 (0%) | 4/18 | 7 |
| 11-20 | 22 | -3.13% | 0/22 (0%) | 1/22 | 6 |
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
| arranca antes (+3%) | -53.74 EUR | -6.72% | 0/8 | -10.00 EUR |
| LA REAL (escalera 25/08) | -284.58 EUR | -4.25% | 0/67 | -8.08 EUR |
| stop corto (5%) | -301.00 EUR | -7.00% | 0/43 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-4.25%**
- Aciertos (>= 5 EUR limpios): 0/67 (0%)
- Resultado acumulado ficticio: -284.58 EUR sobre 67 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 22 | -5.19 EUR | 0% | 68% |
| nota global | medio | 22 | -5.19 EUR | 0% | 86% |
| nota global | alto | 23 | -2.44 EUR | 0% | 52% |
| puesto en el ranking | bajo | 22 | -2.19 EUR | 0% | 50% |
| puesto en el ranking | medio | 22 | -3.95 EUR | 0% | 68% |
| puesto en el ranking | alto | 23 | -6.50 EUR | 0% | 87% |
| potencial hasta objetivo | bajo | 22 | -5.19 EUR | 0% | 77% |
| potencial hasta objetivo | medio | 22 | -3.95 EUR | 0% | 68% |
| potencial hasta objetivo | alto | 23 | -3.63 EUR | 0% | 61% |
| dispersion | bajo | 22 | -2.71 EUR | 0% | 50% |
| dispersion | medio | 22 | -5.49 EUR | 0% | 77% |
| dispersion | alto | 23 | -4.53 EUR | 0% | 78% |
| % compra fuerte | bajo | 21 | -5.92 EUR | 0% | 81% |
| % compra fuerte | medio | 21 | -3.32 EUR | 0% | 71% |
| % compra fuerte | alto | 21 | -4.07 EUR | 0% | 62% |
| momentum 30d | bajo | 22 | -3.95 EUR | 0% | 64% |
| momentum 30d | medio | 22 | -5.08 EUR | 0% | 73% |
| momentum 30d | alto | 23 | -3.74 EUR | 0% | 70% |
| fuerza relativa | bajo | 22 | -3.54 EUR | 0% | 59% |
| fuerza relativa | medio | 22 | -5.08 EUR | 0% | 77% |
| fuerza relativa | alto | 23 | -4.13 EUR | 0% | 70% |
| RSI | bajo | 22 | -3.95 EUR | 0% | 59% |
| RSI | medio | 22 | -3.84 EUR | 0% | 73% |
| RSI | alto | 23 | -4.92 EUR | 0% | 74% |
| volumen relativo | bajo | 17 | -3.81 EUR | 0% | 59% |
| volumen relativo | medio | 17 | -4.34 EUR | 0% | 71% |
| volumen relativo | alto | 19 | -5.21 EUR | 0% | 68% |
| volatilidad | bajo | 17 | -4.88 EUR | 0% | 71% |
| volatilidad | medio | 17 | -6.48 EUR | 0% | 88% |
| volatilidad | alto | 19 | -2.35 EUR | 0% | 42% |
| liquidez | bajo | 17 | -4.34 EUR | 0% | 65% |
| liquidez | medio | 17 | -4.88 EUR | 0% | 71% |
| liquidez | alto | 19 | -4.26 EUR | 0% | 63% |
| distancia max 52s | bajo | 17 | -4.34 EUR | 0% | 59% |
| distancia max 52s | medio | 17 | -3.81 EUR | 0% | 65% |
| distancia max 52s | alto | 19 | -5.21 EUR | 0% | 74% |
| consenso | buy | 45 | -5.46 EUR | 0% | 80% |
| consenso | strong_buy | 22 | -1.77 EUR | 0% | 45% |
| tendencia tecnica | alcista | 42 | -4.13 EUR | 0% | 67% |
| tendencia tecnica | mixta | 16 | -4.11 EUR | 0% | 69% |
| tendencia tecnica | bajista | 9 | -5.05 EUR | 0% | 78% |
| tendencia analistas | mejorando | 38 | -4.02 EUR | 0% | 68% |
| tendencia analistas | estable | 20 | -6.14 EUR | 0% | 85% |
| regimen de mercado | favorable | 55 | -4.07 EUR | 0% | 69% |
| regimen de mercado | neutro | 12 | -5.05 EUR | 0% | 67% |
| catalizador | sin catalizador | 66 | -4.19 EUR | 0% | 68% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.19 | -2.44 | **+2.75 EUR** |
| volatilidad | -4.88 | -2.35 | **+2.53 EUR** |
| % compra fuerte | -5.92 | -4.07 | **+1.85 EUR** |
| potencial hasta objetivo | -5.19 | -3.63 | **+1.56 EUR** |
| momentum 30d | -3.95 | -3.74 | **+0.22 EUR** |
| liquidez | -4.34 | -4.26 | **+0.08 EUR** |
| fuerza relativa | -3.54 | -4.13 | **-0.59 EUR** |
| distancia max 52s | -4.34 | -5.21 | **-0.87 EUR** |
| RSI | -3.95 | -4.92 | **-0.97 EUR** |
| volumen relativo | -3.81 | -5.21 | **-1.41 EUR** |
| dispersion | -2.71 | -4.53 | **-1.81 EUR** |
| puesto en el ranking | -2.19 | -6.50 | **-4.31 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
