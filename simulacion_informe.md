# Simulacion en paralelo

Actualizado: 2026-09-04 13:34 · dia 12 de ejecucion
Proxima revision de ponderacion en 3 dias.

- Operaciones cerradas: **26**
- Operaciones abiertas: 62

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 6 | 23% | +1.42 EUR |
| plano | 0 | - | - |
| perdida | 7 | 27% | -6.78 EUR |
| nefasta | 13 | 50% | -3.89 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 9 | -2.75% | 0/9 (0%) | 2/9 | 6 |
| 11-20 | 8 | -1.27% | 0/8 (0%) | 0/8 | 3 |
| 21-30 | 9 | -6.06% | 0/9 (0%) | 0/9 | 4 |

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
| LA REAL (escalera 25/08) | -89.50 EUR | -3.44% | 0/26 | -8.08 EUR |
| stop corto (5%) | -105.00 EUR | -7.00% | 0/15 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.44%**
- Aciertos (>= 5 EUR limpios): 0/26 (0%)
- Resultado acumulado ficticio: -89.50 EUR sobre 26 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 8 | -6.94 EUR | 0% | 88% |
| nota global | medio | 8 | -1.27 EUR | 0% | 88% |
| nota global | alto | 10 | -2.38 EUR | 0% | 60% |
| puesto en el ranking | bajo | 8 | -2.09 EUR | 0% | 50% |
| puesto en el ranking | medio | 8 | -2.41 EUR | 0% | 88% |
| puesto en el ranking | alto | 10 | -5.36 EUR | 0% | 90% |
| potencial hasta objetivo | bajo | 8 | -2.41 EUR | 0% | 75% |
| potencial hasta objetivo | medio | 8 | -3.54 EUR | 0% | 75% |
| potencial hasta objetivo | alto | 10 | -4.19 EUR | 0% | 80% |
| dispersion | bajo | 8 | -2.41 EUR | 0% | 62% |
| dispersion | medio | 8 | -5.81 EUR | 0% | 88% |
| dispersion | alto | 10 | -2.38 EUR | 0% | 80% |
| % compra fuerte | bajo | 8 | -3.54 EUR | 0% | 62% |
| % compra fuerte | medio | 8 | -1.27 EUR | 0% | 88% |
| % compra fuerte | alto | 9 | -4.77 EUR | 0% | 78% |
| momentum 30d | bajo | 8 | -2.41 EUR | 0% | 62% |
| momentum 30d | medio | 8 | -4.36 EUR | 0% | 75% |
| momentum 30d | alto | 10 | -3.54 EUR | 0% | 90% |
| fuerza relativa | bajo | 8 | -2.41 EUR | 0% | 62% |
| fuerza relativa | medio | 8 | -4.36 EUR | 0% | 75% |
| fuerza relativa | alto | 10 | -3.54 EUR | 0% | 90% |
| RSI | bajo | 8 | -4.67 EUR | 0% | 75% |
| RSI | medio | 8 | -2.09 EUR | 0% | 88% |
| RSI | alto | 10 | -3.54 EUR | 0% | 70% |
| volumen relativo | bajo | 5 | -4.45 EUR | 0% | 80% |
| volumen relativo | medio | 5 | -6.26 EUR | 0% | 100% |
| volumen relativo | alto | 7 | -4.19 EUR | 0% | 71% |
| volatilidad | bajo | 5 | -4.45 EUR | 0% | 80% |
| volatilidad | medio | 5 | -4.45 EUR | 0% | 80% |
| volatilidad | alto | 7 | -5.49 EUR | 0% | 86% |
| liquidez | bajo | 5 | -4.45 EUR | 0% | 80% |
| liquidez | medio | 5 | -4.45 EUR | 0% | 80% |
| liquidez | alto | 7 | -5.49 EUR | 0% | 86% |
| distancia max 52s | bajo | 5 | -6.26 EUR | 0% | 100% |
| distancia max 52s | medio | 5 | -4.45 EUR | 0% | 80% |
| distancia max 52s | alto | 7 | -4.19 EUR | 0% | 71% |
| consenso | buy | 15 | -4.45 EUR | 0% | 87% |
| consenso | strong_buy | 11 | -2.07 EUR | 0% | 64% |
| tendencia tecnica | alcista | 16 | -3.38 EUR | 0% | 75% |
| tendencia tecnica | mixta | 8 | -3.54 EUR | 0% | 75% |
| tendencia analistas | mejorando | 15 | -3.24 EUR | 0% | 80% |
| tendencia analistas | estable | 10 | -4.19 EUR | 0% | 70% |
| regimen de mercado | favorable | 25 | -3.26 EUR | 0% | 76% |
| catalizador | sin catalizador | 26 | -3.44 EUR | 0% | 77% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -6.94 | -2.38 | **+4.57 EUR** |
| distancia max 52s | -6.26 | -4.19 | **+2.08 EUR** |
| RSI | -4.67 | -3.54 | **+1.13 EUR** |
| volumen relativo | -4.45 | -4.19 | **+0.26 EUR** |
| dispersion | -2.41 | -2.38 | **+0.03 EUR** |
| volatilidad | -4.45 | -5.49 | **-1.04 EUR** |
| liquidez | -4.45 | -5.49 | **-1.04 EUR** |
| momentum 30d | -2.41 | -3.54 | **-1.13 EUR** |
| fuerza relativa | -2.41 | -3.54 | **-1.13 EUR** |
| % compra fuerte | -3.54 | -4.77 | **-1.23 EUR** |
| potencial hasta objetivo | -2.41 | -4.19 | **-1.79 EUR** |
| puesto en el ranking | -2.09 | -5.36 | **-3.27 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
