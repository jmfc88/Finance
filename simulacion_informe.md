# Simulacion en paralelo

Actualizado: 2026-09-08 11:13 · dia 16 de ejecucion
**Revision nº1 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **30**
- Operaciones abiertas: 68

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 7 | 23% | +1.36 EUR |
| plano | 0 | - | - |
| perdida | 10 | 33% | -7.17 EUR |
| nefasta | 13 | 43% | -3.89 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 10 | -2.38% | 0/10 (0%) | 3/10 | 6 |
| 11-20 | 10 | -2.63% | 0/10 (0%) | 0/10 | 5 |
| 21-30 | 10 | -6.26% | 0/10 (0%) | 0/10 | 5 |

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
| LA REAL (escalera 25/08) | -112.74 EUR | -3.76% | 0/30 | -8.08 EUR |
| stop corto (5%) | -126.00 EUR | -7.00% | 0/18 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.76%**
- Aciertos (>= 5 EUR limpios): 0/30 (0%)
- Resultado acumulado ficticio: -112.74 EUR sobre 30 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 10 | -6.26 EUR | 0% | 90% |
| nota global | medio | 10 | -2.63 EUR | 0% | 90% |
| nota global | alto | 10 | -2.38 EUR | 0% | 50% |
| puesto en el ranking | bajo | 10 | -2.38 EUR | 0% | 50% |
| puesto en el ranking | medio | 10 | -2.63 EUR | 0% | 80% |
| puesto en el ranking | alto | 10 | -6.26 EUR | 0% | 100% |
| potencial hasta objetivo | bajo | 10 | -3.54 EUR | 0% | 70% |
| potencial hasta objetivo | medio | 10 | -3.54 EUR | 0% | 80% |
| potencial hasta objetivo | alto | 10 | -4.19 EUR | 0% | 80% |
| dispersion | bajo | 10 | -1.72 EUR | 0% | 50% |
| dispersion | medio | 10 | -6.01 EUR | 0% | 90% |
| dispersion | alto | 10 | -3.54 EUR | 0% | 90% |
| % compra fuerte | bajo | 9 | -4.04 EUR | 0% | 67% |
| % compra fuerte | medio | 9 | -1.02 EUR | 0% | 78% |
| % compra fuerte | alto | 11 | -5.37 EUR | 0% | 82% |
| momentum 30d | bajo | 10 | -3.54 EUR | 0% | 70% |
| momentum 30d | medio | 10 | -4.19 EUR | 0% | 80% |
| momentum 30d | alto | 10 | -3.54 EUR | 0% | 80% |
| fuerza relativa | bajo | 10 | -2.63 EUR | 0% | 60% |
| fuerza relativa | medio | 10 | -4.19 EUR | 0% | 80% |
| fuerza relativa | alto | 10 | -4.45 EUR | 0% | 90% |
| RSI | bajo | 10 | -5.36 EUR | 0% | 80% |
| RSI | medio | 10 | -2.38 EUR | 0% | 80% |
| RSI | alto | 10 | -3.54 EUR | 0% | 70% |
| volumen relativo | bajo | 6 | -5.05 EUR | 0% | 83% |
| volumen relativo | medio | 6 | -5.05 EUR | 0% | 100% |
| volumen relativo | alto | 7 | -4.19 EUR | 0% | 57% |
| volatilidad | bajo | 6 | -5.05 EUR | 0% | 83% |
| volatilidad | medio | 6 | -5.05 EUR | 0% | 83% |
| volatilidad | alto | 7 | -4.19 EUR | 0% | 71% |
| liquidez | bajo | 6 | -3.54 EUR | 0% | 67% |
| liquidez | medio | 6 | -5.05 EUR | 0% | 83% |
| liquidez | alto | 7 | -5.49 EUR | 0% | 86% |
| distancia max 52s | bajo | 6 | -5.05 EUR | 0% | 83% |
| distancia max 52s | medio | 6 | -5.05 EUR | 0% | 83% |
| distancia max 52s | alto | 7 | -4.19 EUR | 0% | 71% |
| consenso | buy | 18 | -5.05 EUR | 0% | 89% |
| consenso | strong_buy | 12 | -1.82 EUR | 0% | 58% |
| tendencia tecnica | alcista | 20 | -3.87 EUR | 0% | 75% |
| tendencia tecnica | mixta | 8 | -3.54 EUR | 0% | 75% |
| tendencia analistas | mejorando | 18 | -3.54 EUR | 0% | 78% |
| tendencia analistas | estable | 11 | -4.55 EUR | 0% | 73% |
| regimen de mercado | favorable | 29 | -3.61 EUR | 0% | 76% |
| catalizador | sin catalizador | 30 | -3.76 EUR | 0% | 77% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -6.26 | -2.38 | **+3.89 EUR** |
| RSI | -5.36 | -3.54 | **+1.82 EUR** |
| volumen relativo | -5.05 | -4.19 | **+0.86 EUR** |
| volatilidad | -5.05 | -4.19 | **+0.86 EUR** |
| distancia max 52s | -5.05 | -4.19 | **+0.86 EUR** |
| momentum 30d | -3.54 | -3.54 | **+0.00 EUR** |
| potencial hasta objetivo | -3.54 | -4.19 | **-0.65 EUR** |
| % compra fuerte | -4.04 | -5.37 | **-1.33 EUR** |
| fuerza relativa | -2.63 | -4.45 | **-1.82 EUR** |
| dispersion | -1.72 | -3.54 | **-1.82 EUR** |
| liquidez | -3.54 | -5.49 | **-1.95 EUR** |
| puesto en el ranking | -2.38 | -6.26 | **-3.89 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
