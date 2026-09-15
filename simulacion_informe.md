# Simulacion en paralelo

Actualizado: 2026-09-15 06:10 · dia 23 de ejecucion
Proxima revision de ponderacion en 7 dias.

- Operaciones cerradas: **55**
- Operaciones abiertas: 65

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 17 | 31% | +1.15 EUR |
| plano | 0 | - | - |
| perdida | 17 | 31% | -7.55 EUR |
| nefasta | 21 | 38% | -5.49 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 16 | -2.25% | 0/16 (0%) | 4/16 | 6 |
| 11-20 | 18 | -3.04% | 0/18 (0%) | 1/18 | 6 |
| 21-30 | 21 | -6.35% | 0/21 (0%) | 0/21 | 5 |

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
| LA REAL (escalera 25/08) | -223.94 EUR | -4.07% | 0/55 | -8.08 EUR |
| stop corto (5%) | -238.00 EUR | -7.00% | 0/34 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-4.07%**
- Aciertos (>= 5 EUR limpios): 0/55 (0%)
- Resultado acumulado ficticio: -223.94 EUR sobre 55 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 18 | -5.56 EUR | 0% | 72% |
| nota global | medio | 18 | -4.04 EUR | 0% | 83% |
| nota global | alto | 19 | -2.69 EUR | 0% | 53% |
| puesto en el ranking | bajo | 18 | -2.39 EUR | 0% | 44% |
| puesto en el ranking | medio | 18 | -3.04 EUR | 0% | 72% |
| puesto en el ranking | alto | 19 | -6.65 EUR | 0% | 89% |
| potencial hasta objetivo | bajo | 18 | -4.55 EUR | 0% | 72% |
| potencial hasta objetivo | medio | 18 | -4.55 EUR | 0% | 78% |
| potencial hasta objetivo | alto | 19 | -3.17 EUR | 0% | 58% |
| dispersion | bajo | 18 | -2.53 EUR | 0% | 50% |
| dispersion | medio | 18 | -4.91 EUR | 0% | 72% |
| dispersion | alto | 19 | -4.73 EUR | 0% | 84% |
| % compra fuerte | bajo | 17 | -4.88 EUR | 0% | 71% |
| % compra fuerte | medio | 17 | -2.74 EUR | 0% | 71% |
| % compra fuerte | alto | 17 | -5.26 EUR | 0% | 76% |
| momentum 30d | bajo | 18 | -4.04 EUR | 0% | 67% |
| momentum 30d | medio | 18 | -4.91 EUR | 0% | 72% |
| momentum 30d | alto | 19 | -3.30 EUR | 0% | 68% |
| fuerza relativa | bajo | 18 | -3.54 EUR | 0% | 61% |
| fuerza relativa | medio | 18 | -4.91 EUR | 0% | 78% |
| fuerza relativa | alto | 19 | -3.78 EUR | 0% | 68% |
| RSI | bajo | 18 | -4.55 EUR | 0% | 67% |
| RSI | medio | 18 | -2.89 EUR | 0% | 67% |
| RSI | alto | 19 | -4.73 EUR | 0% | 74% |
| volumen relativo | bajo | 14 | -2.89 EUR | 0% | 50% |
| volumen relativo | medio | 14 | -4.84 EUR | 0% | 79% |
| volumen relativo | alto | 14 | -5.49 EUR | 0% | 71% |
| volatilidad | bajo | 14 | -4.84 EUR | 0% | 71% |
| volatilidad | medio | 14 | -4.84 EUR | 0% | 71% |
| volatilidad | alto | 14 | -3.54 EUR | 0% | 57% |
| liquidez | bajo | 14 | -4.19 EUR | 0% | 64% |
| liquidez | medio | 14 | -4.84 EUR | 0% | 71% |
| liquidez | alto | 14 | -4.19 EUR | 0% | 64% |
| distancia max 52s | bajo | 14 | -4.84 EUR | 0% | 64% |
| distancia max 52s | medio | 14 | -4.19 EUR | 0% | 71% |
| distancia max 52s | alto | 14 | -4.19 EUR | 0% | 64% |
| consenso | buy | 36 | -5.31 EUR | 0% | 81% |
| consenso | strong_buy | 19 | -1.73 EUR | 0% | 47% |
| tendencia tecnica | alcista | 35 | -3.60 EUR | 0% | 63% |
| tendencia tecnica | mixta | 13 | -4.59 EUR | 0% | 77% |
| tendencia tecnica | bajista | 7 | -5.49 EUR | 0% | 86% |
| tendencia analistas | mejorando | 31 | -4.27 EUR | 0% | 74% |
| tendencia analistas | estable | 17 | -5.79 EUR | 0% | 82% |
| regimen de mercado | favorable | 48 | -3.87 EUR | 0% | 69% |
| regimen de mercado | neutro | 7 | -5.49 EUR | 0% | 71% |
| catalizador | sin catalizador | 54 | -4.00 EUR | 0% | 69% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.56 | -2.69 | **+2.87 EUR** |
| potencial hasta objetivo | -4.55 | -3.17 | **+1.38 EUR** |
| volatilidad | -4.84 | -3.54 | **+1.30 EUR** |
| momentum 30d | -4.04 | -3.30 | **+0.74 EUR** |
| distancia max 52s | -4.84 | -4.19 | **+0.65 EUR** |
| liquidez | -4.19 | -4.19 | **+0.00 EUR** |
| RSI | -4.55 | -4.73 | **-0.19 EUR** |
| fuerza relativa | -3.54 | -3.78 | **-0.24 EUR** |
| % compra fuerte | -4.88 | -5.26 | **-0.38 EUR** |
| dispersion | -2.53 | -4.73 | **-2.20 EUR** |
| volumen relativo | -2.89 | -5.49 | **-2.59 EUR** |
| puesto en el ranking | -2.39 | -6.65 | **-4.26 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
