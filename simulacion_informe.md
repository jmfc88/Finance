# Simulacion en paralelo

Actualizado: 2026-09-09 11:17 · dia 17 de ejecucion
**Revision nº1 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **38**
- Operaciones abiertas: 62

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 11 | 29% | +1.23 EUR |
| plano | 0 | - | - |
| perdida | 12 | 32% | -7.32 EUR |
| nefasta | 15 | 39% | -4.45 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 13 | -2.30% | 0/13 (0%) | 3/13 | 7 |
| 11-20 | 13 | -2.49% | 0/13 (0%) | 1/13 | 5 |
| 21-30 | 12 | -6.57% | 0/12 (0%) | 0/12 | 5 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida


## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -15.76 EUR | -3.15% | 0/5 | -10.00 EUR |
| trailing suelto (7%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| sin trailing, solo stop | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| arranca despues (+8%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| actual (8% / +5% / 5%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| arranca antes (+3%) | -26.95 EUR | -6.74% | 0/4 | -10.00 EUR |
| LA REAL (escalera 25/08) | -141.06 EUR | -3.71% | 0/38 | -8.08 EUR |
| stop corto (5%) | -161.00 EUR | -7.00% | 0/23 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.71%**
- Aciertos (>= 5 EUR limpios): 0/38 (0%)
- Resultado acumulado ficticio: -141.06 EUR sobre 38 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 12 | -6.57 EUR | 0% | 83% |
| nota global | medio | 12 | -2.03 EUR | 0% | 75% |
| nota global | alto | 14 | -2.71 EUR | 0% | 57% |
| puesto en el ranking | bajo | 12 | -1.82 EUR | 0% | 42% |
| puesto en el ranking | medio | 12 | -2.78 EUR | 0% | 75% |
| puesto en el ranking | alto | 14 | -6.13 EUR | 0% | 93% |
| potencial hasta objetivo | bajo | 12 | -3.54 EUR | 0% | 67% |
| potencial hasta objetivo | medio | 12 | -3.54 EUR | 0% | 75% |
| potencial hasta objetivo | alto | 14 | -4.01 EUR | 0% | 71% |
| dispersion | bajo | 12 | -1.27 EUR | 0% | 42% |
| dispersion | medio | 12 | -6.35 EUR | 0% | 92% |
| dispersion | alto | 14 | -3.54 EUR | 0% | 79% |
| % compra fuerte | bajo | 12 | -4.30 EUR | 0% | 67% |
| % compra fuerte | medio | 12 | -0.51 EUR | 0% | 58% |
| % compra fuerte | alto | 13 | -5.79 EUR | 0% | 85% |
| momentum 30d | bajo | 12 | -3.54 EUR | 0% | 67% |
| momentum 30d | medio | 12 | -4.08 EUR | 0% | 75% |
| momentum 30d | alto | 14 | -3.54 EUR | 0% | 71% |
| fuerza relativa | bajo | 12 | -2.78 EUR | 0% | 58% |
| fuerza relativa | medio | 12 | -4.84 EUR | 0% | 83% |
| fuerza relativa | alto | 14 | -3.54 EUR | 0% | 71% |
| RSI | bajo | 12 | -4.30 EUR | 0% | 67% |
| RSI | medio | 12 | -2.57 EUR | 0% | 75% |
| RSI | alto | 14 | -4.19 EUR | 0% | 71% |
| volumen relativo | bajo | 8 | -4.67 EUR | 0% | 75% |
| volumen relativo | medio | 8 | -4.67 EUR | 0% | 75% |
| volumen relativo | alto | 10 | -3.54 EUR | 0% | 60% |
| volatilidad | bajo | 8 | -4.67 EUR | 0% | 75% |
| volatilidad | medio | 8 | -4.67 EUR | 0% | 75% |
| volatilidad | alto | 10 | -3.54 EUR | 0% | 60% |
| liquidez | bajo | 8 | -3.54 EUR | 0% | 62% |
| liquidez | medio | 8 | -5.81 EUR | 0% | 88% |
| liquidez | alto | 10 | -3.54 EUR | 0% | 60% |
| distancia max 52s | bajo | 8 | -5.81 EUR | 0% | 75% |
| distancia max 52s | medio | 8 | -3.54 EUR | 0% | 75% |
| distancia max 52s | alto | 10 | -3.54 EUR | 0% | 60% |
| consenso | buy | 24 | -4.67 EUR | 0% | 79% |
| consenso | strong_buy | 14 | -2.06 EUR | 0% | 57% |
| tendencia tecnica | alcista | 25 | -3.62 EUR | 0% | 68% |
| tendencia tecnica | mixta | 10 | -3.54 EUR | 0% | 70% |
| tendencia analistas | mejorando | 22 | -3.13 EUR | 0% | 68% |
| tendencia analistas | estable | 14 | -5.30 EUR | 0% | 79% |
| regimen de mercado | favorable | 36 | -3.47 EUR | 0% | 69% |
| catalizador | sin catalizador | 38 | -3.71 EUR | 0% | 71% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -6.57 | -2.71 | **+3.86 EUR** |
| distancia max 52s | -5.81 | -3.54 | **+2.27 EUR** |
| volumen relativo | -4.67 | -3.54 | **+1.13 EUR** |
| volatilidad | -4.67 | -3.54 | **+1.13 EUR** |
| RSI | -4.30 | -4.19 | **+0.11 EUR** |
| momentum 30d | -3.54 | -3.54 | **+0.00 EUR** |
| liquidez | -3.54 | -3.54 | **+0.00 EUR** |
| potencial hasta objetivo | -3.54 | -4.01 | **-0.47 EUR** |
| fuerza relativa | -2.78 | -3.54 | **-0.76 EUR** |
| % compra fuerte | -4.30 | -5.79 | **-1.49 EUR** |
| dispersion | -1.27 | -3.54 | **-2.27 EUR** |
| puesto en el ranking | -1.82 | -6.13 | **-4.32 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
