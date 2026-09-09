# Simulacion en paralelo

Actualizado: 2026-09-09 13:45 · dia 17 de ejecucion
**Revision nº1 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **41**
- Operaciones abiertas: 64

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 13 | 32% | +1.20 EUR |
| plano | 0 | - | - |
| perdida | 13 | 32% | -7.38 EUR |
| nefasta | 15 | 37% | -4.45 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 15 | -1.86% | 0/15 (0%) | 4/15 | 7 |
| 11-20 | 13 | -2.49% | 0/13 (0%) | 1/13 | 5 |
| 21-30 | 13 | -6.68% | 0/13 (0%) | 0/13 | 5 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida


## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -14.73 EUR | -2.46% | 0/6 | -10.00 EUR |
| trailing suelto (7%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| sin trailing, solo stop | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| arranca despues (+8%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| actual (8% / +5% / 5%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| arranca antes (+3%) | -26.95 EUR | -6.74% | 0/4 | -10.00 EUR |
| LA REAL (escalera 25/08) | -147.14 EUR | -3.59% | 0/41 | -8.08 EUR |
| stop corto (5%) | -168.00 EUR | -7.00% | 0/24 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.59%**
- Aciertos (>= 5 EUR limpios): 0/41 (0%)
- Resultado acumulado ficticio: -147.14 EUR sobre 41 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 13 | -5.98 EUR | 0% | 77% |
| nota global | medio | 13 | -2.49 EUR | 0% | 77% |
| nota global | alto | 15 | -2.46 EUR | 0% | 53% |
| puesto en el ranking | bajo | 13 | -1.60 EUR | 0% | 38% |
| puesto en el ranking | medio | 13 | -2.49 EUR | 0% | 69% |
| puesto en el ranking | alto | 15 | -6.26 EUR | 0% | 93% |
| potencial hasta objetivo | bajo | 13 | -3.89 EUR | 0% | 69% |
| potencial hasta objetivo | medio | 13 | -3.19 EUR | 0% | 69% |
| potencial hasta objetivo | alto | 15 | -3.67 EUR | 0% | 67% |
| dispersion | bajo | 13 | -1.79 EUR | 0% | 46% |
| dispersion | medio | 13 | -5.79 EUR | 0% | 85% |
| dispersion | alto | 15 | -3.24 EUR | 0% | 73% |
| % compra fuerte | bajo | 13 | -3.89 EUR | 0% | 62% |
| % compra fuerte | medio | 13 | -1.79 EUR | 0% | 69% |
| % compra fuerte | alto | 13 | -5.09 EUR | 0% | 77% |
| momentum 30d | bajo | 13 | -3.19 EUR | 0% | 62% |
| momentum 30d | medio | 13 | -4.39 EUR | 0% | 69% |
| momentum 30d | alto | 15 | -3.24 EUR | 0% | 73% |
| fuerza relativa | bajo | 13 | -2.49 EUR | 0% | 54% |
| fuerza relativa | medio | 13 | -4.39 EUR | 0% | 77% |
| fuerza relativa | alto | 15 | -3.84 EUR | 0% | 73% |
| RSI | bajo | 13 | -3.89 EUR | 0% | 62% |
| RSI | medio | 13 | -3.00 EUR | 0% | 77% |
| RSI | alto | 15 | -3.84 EUR | 0% | 67% |
| volumen relativo | bajo | 9 | -4.04 EUR | 0% | 67% |
| volumen relativo | medio | 9 | -4.04 EUR | 0% | 78% |
| volumen relativo | alto | 11 | -3.95 EUR | 0% | 55% |
| volatilidad | bajo | 9 | -5.05 EUR | 0% | 78% |
| volatilidad | medio | 9 | -4.04 EUR | 0% | 67% |
| volatilidad | alto | 11 | -3.13 EUR | 0% | 55% |
| liquidez | bajo | 9 | -3.04 EUR | 0% | 56% |
| liquidez | medio | 9 | -5.05 EUR | 0% | 78% |
| liquidez | alto | 11 | -3.95 EUR | 0% | 64% |
| distancia max 52s | bajo | 9 | -5.05 EUR | 0% | 67% |
| distancia max 52s | medio | 9 | -4.04 EUR | 0% | 78% |
| distancia max 52s | alto | 11 | -3.13 EUR | 0% | 55% |
| consenso | buy | 25 | -4.81 EUR | 0% | 80% |
| consenso | strong_buy | 16 | -1.68 EUR | 0% | 50% |
| tendencia tecnica | alcista | 27 | -3.28 EUR | 0% | 63% |
| tendencia tecnica | mixta | 10 | -3.54 EUR | 0% | 70% |
| tendencia analistas | mejorando | 22 | -3.13 EUR | 0% | 68% |
| tendencia analistas | estable | 15 | -5.49 EUR | 0% | 80% |
| regimen de mercado | favorable | 39 | -3.36 EUR | 0% | 67% |
| catalizador | sin catalizador | 41 | -3.59 EUR | 0% | 68% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.98 | -2.46 | **+3.52 EUR** |
| volatilidad | -5.05 | -3.13 | **+1.93 EUR** |
| distancia max 52s | -5.05 | -3.13 | **+1.93 EUR** |
| potencial hasta objetivo | -3.89 | -3.67 | **+0.22 EUR** |
| volumen relativo | -4.04 | -3.95 | **+0.09 EUR** |
| RSI | -3.89 | -3.84 | **+0.05 EUR** |
| momentum 30d | -3.19 | -3.24 | **-0.05 EUR** |
| liquidez | -3.04 | -3.95 | **-0.92 EUR** |
| % compra fuerte | -3.89 | -5.09 | **-1.20 EUR** |
| fuerza relativa | -2.49 | -3.84 | **-1.35 EUR** |
| dispersion | -1.79 | -3.24 | **-1.44 EUR** |
| puesto en el ranking | -1.60 | -6.26 | **-4.67 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
