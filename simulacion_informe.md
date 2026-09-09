# Simulacion en paralelo

Actualizado: 2026-09-09 05:58 · dia 17 de ejecucion
**Revision nº1 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **32**
- Operaciones abiertas: 67

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 8 | 25% | +1.32 EUR |
| plano | 0 | - | - |
| perdida | 10 | 31% | -7.17 EUR |
| nefasta | 14 | 44% | -4.19 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 11 | -2.07% | 0/11 (0%) | 3/11 | 6 |
| 11-20 | 10 | -2.63% | 0/10 (0%) | 0/10 | 5 |
| 21-30 | 11 | -6.43% | 0/11 (0%) | 0/11 | 5 |

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
| LA REAL (escalera 25/08) | -119.82 EUR | -3.74% | 0/32 | -8.08 EUR |
| stop corto (5%) | -140.00 EUR | -7.00% | 0/20 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.74%**
- Aciertos (>= 5 EUR limpios): 0/32 (0%)
- Resultado acumulado ficticio: -119.82 EUR sobre 32 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 10 | -7.17 EUR | 0% | 90% |
| nota global | medio | 10 | -1.72 EUR | 0% | 80% |
| nota global | alto | 12 | -2.57 EUR | 0% | 58% |
| puesto en el ranking | bajo | 10 | -1.47 EUR | 0% | 40% |
| puesto en el ranking | medio | 10 | -2.63 EUR | 0% | 80% |
| puesto en el ranking | alto | 12 | -6.57 EUR | 0% | 100% |
| potencial hasta objetivo | bajo | 10 | -3.54 EUR | 0% | 70% |
| potencial hasta objetivo | medio | 10 | -2.63 EUR | 0% | 70% |
| potencial hasta objetivo | alto | 12 | -4.84 EUR | 0% | 83% |
| dispersion | bajo | 10 | -1.72 EUR | 0% | 50% |
| dispersion | medio | 10 | -5.10 EUR | 0% | 80% |
| dispersion | alto | 12 | -4.30 EUR | 0% | 92% |
| % compra fuerte | bajo | 10 | -4.45 EUR | 0% | 70% |
| % compra fuerte | medio | 10 | -0.82 EUR | 0% | 70% |
| % compra fuerte | alto | 11 | -5.37 EUR | 0% | 82% |
| momentum 30d | bajo | 10 | -3.54 EUR | 0% | 70% |
| momentum 30d | medio | 10 | -4.19 EUR | 0% | 80% |
| momentum 30d | alto | 12 | -3.54 EUR | 0% | 75% |
| fuerza relativa | bajo | 10 | -2.63 EUR | 0% | 60% |
| fuerza relativa | medio | 10 | -5.10 EUR | 0% | 90% |
| fuerza relativa | alto | 12 | -3.54 EUR | 0% | 75% |
| RSI | bajo | 10 | -4.45 EUR | 0% | 70% |
| RSI | medio | 10 | -3.29 EUR | 0% | 90% |
| RSI | alto | 12 | -3.54 EUR | 0% | 67% |
| volumen relativo | bajo | 7 | -4.19 EUR | 0% | 71% |
| volumen relativo | medio | 7 | -5.49 EUR | 0% | 100% |
| volumen relativo | alto | 7 | -4.19 EUR | 0% | 57% |
| volatilidad | bajo | 7 | -5.49 EUR | 0% | 86% |
| volatilidad | medio | 7 | -4.19 EUR | 0% | 71% |
| volatilidad | alto | 7 | -4.19 EUR | 0% | 71% |
| liquidez | bajo | 7 | -4.19 EUR | 0% | 71% |
| liquidez | medio | 7 | -4.19 EUR | 0% | 86% |
| liquidez | alto | 7 | -5.49 EUR | 0% | 71% |
| distancia max 52s | bajo | 7 | -5.49 EUR | 0% | 86% |
| distancia max 52s | medio | 7 | -4.19 EUR | 0% | 71% |
| distancia max 52s | alto | 7 | -4.19 EUR | 0% | 71% |
| consenso | buy | 19 | -4.73 EUR | 0% | 84% |
| consenso | strong_buy | 13 | -2.30 EUR | 0% | 62% |
| tendencia tecnica | alcista | 21 | -3.64 EUR | 0% | 71% |
| tendencia tecnica | mixta | 8 | -3.54 EUR | 0% | 75% |
| tendencia analistas | mejorando | 19 | -3.30 EUR | 0% | 74% |
| tendencia analistas | estable | 12 | -4.84 EUR | 0% | 75% |
| regimen de mercado | favorable | 31 | -3.60 EUR | 0% | 74% |
| catalizador | sin catalizador | 32 | -3.74 EUR | 0% | 75% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -7.17 | -2.57 | **+4.60 EUR** |
| volatilidad | -5.49 | -4.19 | **+1.30 EUR** |
| distancia max 52s | -5.49 | -4.19 | **+1.30 EUR** |
| RSI | -4.45 | -3.54 | **+0.91 EUR** |
| momentum 30d | -3.54 | -3.54 | **+0.00 EUR** |
| volumen relativo | -4.19 | -4.19 | **+0.00 EUR** |
| fuerza relativa | -2.63 | -3.54 | **-0.91 EUR** |
| % compra fuerte | -4.45 | -5.37 | **-0.92 EUR** |
| liquidez | -4.19 | -5.49 | **-1.30 EUR** |
| potencial hasta objetivo | -3.54 | -4.84 | **-1.30 EUR** |
| dispersion | -1.72 | -4.30 | **-2.57 EUR** |
| puesto en el ranking | -1.47 | -6.57 | **-5.10 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
