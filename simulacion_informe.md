# Simulacion en paralelo

Actualizado: 2026-09-07 18:16 · dia 15 de ejecucion
**Revision nº1 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **28**
- Operaciones abiertas: 69

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 6 | 21% | +1.42 EUR |
| plano | 0 | - | - |
| perdida | 9 | 32% | -7.07 EUR |
| nefasta | 13 | 46% | -3.89 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 9 | -2.75% | 0/9 (0%) | 2/9 | 6 |
| 11-20 | 9 | -2.03% | 0/9 (0%) | 0/9 | 4 |
| 21-30 | 10 | -6.26% | 0/10 (0%) | 0/10 | 5 |

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
| LA REAL (escalera 25/08) | -105.66 EUR | -3.77% | 0/28 | -8.08 EUR |
| stop corto (5%) | -119.00 EUR | -7.00% | 0/17 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.77%**
- Aciertos (>= 5 EUR limpios): 0/28 (0%)
- Resultado acumulado ficticio: -105.66 EUR sobre 28 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 9 | -7.07 EUR | 0% | 89% |
| nota global | medio | 9 | -2.03 EUR | 0% | 89% |
| nota global | alto | 10 | -2.38 EUR | 0% | 60% |
| puesto en el ranking | bajo | 9 | -2.75 EUR | 0% | 56% |
| puesto en el ranking | medio | 9 | -2.03 EUR | 0% | 78% |
| puesto en el ranking | alto | 10 | -6.26 EUR | 0% | 100% |
| potencial hasta objetivo | bajo | 9 | -3.04 EUR | 0% | 78% |
| potencial hasta objetivo | medio | 9 | -4.04 EUR | 0% | 78% |
| potencial hasta objetivo | alto | 10 | -4.19 EUR | 0% | 80% |
| dispersion | bajo | 9 | -2.03 EUR | 0% | 56% |
| dispersion | medio | 9 | -5.78 EUR | 0% | 89% |
| dispersion | alto | 10 | -3.54 EUR | 0% | 90% |
| % compra fuerte | bajo | 9 | -4.04 EUR | 0% | 67% |
| % compra fuerte | medio | 9 | -0.74 EUR | 0% | 78% |
| % compra fuerte | alto | 9 | -6.06 EUR | 0% | 89% |
| momentum 30d | bajo | 9 | -3.04 EUR | 0% | 67% |
| momentum 30d | medio | 9 | -4.77 EUR | 0% | 78% |
| momentum 30d | alto | 10 | -3.54 EUR | 0% | 90% |
| fuerza relativa | bajo | 9 | -2.03 EUR | 0% | 56% |
| fuerza relativa | medio | 9 | -5.78 EUR | 0% | 89% |
| fuerza relativa | alto | 10 | -3.54 EUR | 0% | 90% |
| RSI | bajo | 9 | -5.05 EUR | 0% | 78% |
| RSI | medio | 9 | -2.75 EUR | 0% | 89% |
| RSI | alto | 10 | -3.54 EUR | 0% | 70% |
| volumen relativo | bajo | 6 | -5.05 EUR | 0% | 83% |
| volumen relativo | medio | 6 | -5.05 EUR | 0% | 100% |
| volumen relativo | alto | 6 | -5.05 EUR | 0% | 67% |
| volatilidad | bajo | 6 | -5.05 EUR | 0% | 83% |
| volatilidad | medio | 6 | -5.05 EUR | 0% | 83% |
| volatilidad | alto | 6 | -5.05 EUR | 0% | 83% |
| liquidez | bajo | 6 | -5.05 EUR | 0% | 83% |
| liquidez | medio | 6 | -3.54 EUR | 0% | 83% |
| liquidez | alto | 6 | -6.57 EUR | 0% | 83% |
| distancia max 52s | bajo | 6 | -6.57 EUR | 0% | 100% |
| distancia max 52s | medio | 6 | -5.05 EUR | 0% | 83% |
| distancia max 52s | alto | 6 | -3.54 EUR | 0% | 67% |
| consenso | buy | 17 | -4.88 EUR | 0% | 88% |
| consenso | strong_buy | 11 | -2.07 EUR | 0% | 64% |
| tendencia tecnica | alcista | 18 | -3.90 EUR | 0% | 78% |
| tendencia tecnica | mixta | 8 | -3.54 EUR | 0% | 75% |
| tendencia analistas | mejorando | 16 | -3.54 EUR | 0% | 81% |
| tendencia analistas | estable | 11 | -4.55 EUR | 0% | 73% |
| regimen de mercado | favorable | 27 | -3.61 EUR | 0% | 78% |
| catalizador | sin catalizador | 28 | -3.77 EUR | 0% | 79% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -7.07 | -2.38 | **+4.69 EUR** |
| distancia max 52s | -6.57 | -3.54 | **+3.03 EUR** |
| RSI | -5.05 | -3.54 | **+1.51 EUR** |
| volumen relativo | -5.05 | -5.05 | **+0.00 EUR** |
| volatilidad | -5.05 | -5.05 | **+0.00 EUR** |
| momentum 30d | -3.04 | -3.54 | **-0.50 EUR** |
| potencial hasta objetivo | -3.04 | -4.19 | **-1.16 EUR** |
| liquidez | -5.05 | -6.57 | **-1.51 EUR** |
| fuerza relativa | -2.03 | -3.54 | **-1.51 EUR** |
| dispersion | -2.03 | -3.54 | **-1.51 EUR** |
| % compra fuerte | -4.04 | -6.06 | **-2.02 EUR** |
| puesto en el ranking | -2.75 | -6.26 | **-3.51 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
