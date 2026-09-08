# Simulacion en paralelo

Actualizado: 2026-09-08 23:26 · dia 16 de ejecucion
**Revision nº1 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **31**
- Operaciones abiertas: 68

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 8 | 26% | +1.32 EUR |
| plano | 0 | - | - |
| perdida | 10 | 32% | -7.17 EUR |
| nefasta | 13 | 42% | -3.89 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 11 | -2.07% | 0/11 (0%) | 3/11 | 6 |
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
| LA REAL (escalera 25/08) | -111.74 EUR | -3.60% | 0/31 | -8.08 EUR |
| stop corto (5%) | -133.00 EUR | -7.00% | 0/19 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.60%**
- Aciertos (>= 5 EUR limpios): 0/31 (0%)
- Resultado acumulado ficticio: -111.74 EUR sobre 31 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 10 | -6.26 EUR | 0% | 90% |
| nota global | medio | 10 | -1.72 EUR | 0% | 80% |
| nota global | alto | 11 | -2.90 EUR | 0% | 55% |
| puesto en el ranking | bajo | 10 | -1.47 EUR | 0% | 40% |
| puesto en el ranking | medio | 10 | -2.63 EUR | 0% | 80% |
| puesto en el ranking | alto | 11 | -6.43 EUR | 0% | 100% |
| potencial hasta objetivo | bajo | 10 | -3.54 EUR | 0% | 70% |
| potencial hasta objetivo | medio | 10 | -2.63 EUR | 0% | 70% |
| potencial hasta objetivo | alto | 11 | -4.55 EUR | 0% | 82% |
| dispersion | bajo | 10 | -1.72 EUR | 0% | 50% |
| dispersion | medio | 10 | -5.10 EUR | 0% | 80% |
| dispersion | alto | 11 | -3.95 EUR | 0% | 91% |
| % compra fuerte | bajo | 10 | -4.45 EUR | 0% | 70% |
| % compra fuerte | medio | 10 | -0.82 EUR | 0% | 70% |
| % compra fuerte | alto | 10 | -5.10 EUR | 0% | 80% |
| momentum 30d | bajo | 10 | -3.54 EUR | 0% | 70% |
| momentum 30d | medio | 10 | -4.19 EUR | 0% | 80% |
| momentum 30d | alto | 11 | -3.13 EUR | 0% | 73% |
| fuerza relativa | bajo | 10 | -2.63 EUR | 0% | 60% |
| fuerza relativa | medio | 10 | -4.19 EUR | 0% | 80% |
| fuerza relativa | alto | 11 | -3.95 EUR | 0% | 82% |
| RSI | bajo | 10 | -4.45 EUR | 0% | 70% |
| RSI | medio | 10 | -2.38 EUR | 0% | 80% |
| RSI | alto | 11 | -3.95 EUR | 0% | 73% |
| volumen relativo | bajo | 6 | -5.05 EUR | 0% | 83% |
| volumen relativo | medio | 6 | -5.05 EUR | 0% | 83% |
| volumen relativo | alto | 8 | -3.54 EUR | 0% | 62% |
| volatilidad | bajo | 6 | -5.05 EUR | 0% | 83% |
| volatilidad | medio | 6 | -5.05 EUR | 0% | 83% |
| volatilidad | alto | 8 | -3.54 EUR | 0% | 62% |
| liquidez | bajo | 6 | -3.54 EUR | 0% | 67% |
| liquidez | medio | 6 | -5.05 EUR | 0% | 83% |
| liquidez | alto | 8 | -4.67 EUR | 0% | 75% |
| distancia max 52s | bajo | 6 | -5.05 EUR | 0% | 83% |
| distancia max 52s | medio | 6 | -3.54 EUR | 0% | 67% |
| distancia max 52s | alto | 8 | -4.67 EUR | 0% | 75% |
| consenso | buy | 19 | -4.73 EUR | 0% | 84% |
| consenso | strong_buy | 12 | -1.82 EUR | 0% | 58% |
| tendencia tecnica | alcista | 21 | -3.64 EUR | 0% | 71% |
| tendencia tecnica | mixta | 8 | -3.54 EUR | 0% | 75% |
| tendencia analistas | mejorando | 19 | -3.30 EUR | 0% | 74% |
| tendencia analistas | estable | 11 | -4.55 EUR | 0% | 73% |
| regimen de mercado | favorable | 30 | -3.46 EUR | 0% | 73% |
| catalizador | sin catalizador | 31 | -3.60 EUR | 0% | 74% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -6.26 | -2.90 | **+3.37 EUR** |
| volumen relativo | -5.05 | -3.54 | **+1.51 EUR** |
| volatilidad | -5.05 | -3.54 | **+1.51 EUR** |
| RSI | -4.45 | -3.95 | **+0.50 EUR** |
| momentum 30d | -3.54 | -3.13 | **+0.41 EUR** |
| distancia max 52s | -5.05 | -4.67 | **+0.38 EUR** |
| % compra fuerte | -4.45 | -5.10 | **-0.65 EUR** |
| potencial hasta objetivo | -3.54 | -4.55 | **-1.01 EUR** |
| liquidez | -3.54 | -4.67 | **-1.13 EUR** |
| fuerza relativa | -2.63 | -3.95 | **-1.32 EUR** |
| dispersion | -1.72 | -3.95 | **-2.23 EUR** |
| puesto en el ranking | -1.47 | -6.43 | **-4.96 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
