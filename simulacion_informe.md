# Simulacion en paralelo

Actualizado: 2026-09-14 23:54 · dia 22 de ejecucion
Proxima revision de ponderacion en 8 dias.

- Operaciones cerradas: **54**
- Operaciones abiertas: 66

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 16 | 30% | +1.16 EUR |
| plano | 0 | - | - |
| perdida | 17 | 31% | -7.55 EUR |
| nefasta | 21 | 39% | -5.49 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 16 | -2.25% | 0/16 (0%) | 4/16 | 6 |
| 11-20 | 18 | -3.04% | 0/18 (0%) | 1/18 | 6 |
| 21-30 | 20 | -6.72% | 0/20 (0%) | 0/20 | 5 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida


## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -24.73 EUR | -3.53% | 0/7 | -10.00 EUR |
| trailing suelto (7%) | -30.00 EUR | -10.00% | 0/3 | -10.00 EUR |
| sin trailing, solo stop | -30.00 EUR | -10.00% | 0/3 | -10.00 EUR |
| arranca despues (+8%) | -30.00 EUR | -10.00% | 0/3 | -10.00 EUR |
| actual (8% / +5% / 5%) | -30.00 EUR | -10.00% | 0/3 | -10.00 EUR |
| arranca antes (+3%) | -40.41 EUR | -6.74% | 0/6 | -10.00 EUR |
| LA REAL (escalera 25/08) | -224.94 EUR | -4.17% | 0/54 | -8.08 EUR |
| stop corto (5%) | -238.00 EUR | -7.00% | 0/34 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-4.17%**
- Aciertos (>= 5 EUR limpios): 0/54 (0%)
- Resultado acumulado ficticio: -224.94 EUR sobre 54 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 18 | -5.56 EUR | 0% | 72% |
| nota global | medio | 18 | -4.04 EUR | 0% | 83% |
| nota global | alto | 18 | -2.89 EUR | 0% | 56% |
| puesto en el ranking | bajo | 18 | -2.39 EUR | 0% | 44% |
| puesto en el ranking | medio | 18 | -3.04 EUR | 0% | 72% |
| puesto en el ranking | alto | 18 | -7.07 EUR | 0% | 94% |
| potencial hasta objetivo | bajo | 18 | -4.55 EUR | 0% | 72% |
| potencial hasta objetivo | medio | 18 | -4.55 EUR | 0% | 78% |
| potencial hasta objetivo | alto | 18 | -3.40 EUR | 0% | 61% |
| dispersion | bajo | 18 | -2.53 EUR | 0% | 50% |
| dispersion | medio | 18 | -5.42 EUR | 0% | 78% |
| dispersion | alto | 18 | -4.55 EUR | 0% | 83% |
| % compra fuerte | bajo | 17 | -4.88 EUR | 0% | 71% |
| % compra fuerte | medio | 17 | -2.74 EUR | 0% | 71% |
| % compra fuerte | alto | 17 | -5.26 EUR | 0% | 76% |
| momentum 30d | bajo | 18 | -4.04 EUR | 0% | 67% |
| momentum 30d | medio | 18 | -5.42 EUR | 0% | 78% |
| momentum 30d | alto | 18 | -3.04 EUR | 0% | 67% |
| fuerza relativa | bajo | 18 | -3.54 EUR | 0% | 61% |
| fuerza relativa | medio | 18 | -4.91 EUR | 0% | 78% |
| fuerza relativa | alto | 18 | -4.04 EUR | 0% | 72% |
| RSI | bajo | 18 | -4.55 EUR | 0% | 67% |
| RSI | medio | 18 | -2.89 EUR | 0% | 67% |
| RSI | alto | 18 | -5.05 EUR | 0% | 78% |
| volumen relativo | bajo | 13 | -3.19 EUR | 0% | 54% |
| volumen relativo | medio | 13 | -4.59 EUR | 0% | 77% |
| volumen relativo | alto | 15 | -5.66 EUR | 0% | 73% |
| volatilidad | bajo | 13 | -4.59 EUR | 0% | 69% |
| volatilidad | medio | 13 | -5.98 EUR | 0% | 85% |
| volatilidad | alto | 15 | -3.24 EUR | 0% | 53% |
| liquidez | bajo | 13 | -4.59 EUR | 0% | 69% |
| liquidez | medio | 13 | -5.29 EUR | 0% | 77% |
| liquidez | alto | 15 | -3.84 EUR | 0% | 60% |
| distancia max 52s | bajo | 13 | -5.29 EUR | 0% | 69% |
| distancia max 52s | medio | 13 | -4.59 EUR | 0% | 77% |
| distancia max 52s | alto | 15 | -3.84 EUR | 0% | 60% |
| consenso | buy | 36 | -5.31 EUR | 0% | 81% |
| consenso | strong_buy | 18 | -1.89 EUR | 0% | 50% |
| tendencia tecnica | alcista | 34 | -3.73 EUR | 0% | 65% |
| tendencia tecnica | mixta | 13 | -4.59 EUR | 0% | 77% |
| tendencia tecnica | bajista | 7 | -5.49 EUR | 0% | 86% |
| tendencia analistas | mejorando | 31 | -4.27 EUR | 0% | 74% |
| tendencia analistas | estable | 17 | -5.79 EUR | 0% | 82% |
| regimen de mercado | favorable | 48 | -3.87 EUR | 0% | 69% |
| regimen de mercado | neutro | 6 | -6.57 EUR | 0% | 83% |
| catalizador | sin catalizador | 53 | -4.09 EUR | 0% | 70% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.56 | -2.89 | **+2.66 EUR** |
| distancia max 52s | -5.29 | -3.84 | **+1.44 EUR** |
| volatilidad | -4.59 | -3.24 | **+1.35 EUR** |
| potencial hasta objetivo | -4.55 | -3.40 | **+1.15 EUR** |
| momentum 30d | -4.04 | -3.04 | **+1.01 EUR** |
| liquidez | -4.59 | -3.84 | **+0.75 EUR** |
| % compra fuerte | -4.88 | -5.26 | **-0.38 EUR** |
| RSI | -4.55 | -5.05 | **-0.50 EUR** |
| fuerza relativa | -3.54 | -4.04 | **-0.50 EUR** |
| dispersion | -2.53 | -4.55 | **-2.02 EUR** |
| volumen relativo | -3.19 | -5.66 | **-2.47 EUR** |
| puesto en el ranking | -2.39 | -7.07 | **-4.68 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
