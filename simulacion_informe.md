# Simulacion en paralelo

Actualizado: 2026-09-04 11:13 · dia 12 de ejecucion
Proxima revision de ponderacion en 3 dias.

- Operaciones cerradas: **25**
- Operaciones abiertas: 63

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 5 | 20% | +1.51 EUR |
| plano | 0 | - | - |
| perdida | 7 | 28% | -6.78 EUR |
| nefasta | 13 | 52% | -3.89 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 9 | -2.75% | 0/9 (0%) | 2/9 | 6 |
| 11-20 | 7 | -1.59% | 0/7 (0%) | 0/7 | 3 |
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
| LA REAL (escalera 25/08) | -90.50 EUR | -3.62% | 0/25 | -8.08 EUR |
| stop corto (5%) | -105.00 EUR | -7.00% | 0/15 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.62%**
- Aciertos (>= 5 EUR limpios): 0/25 (0%)
- Resultado acumulado ficticio: -90.50 EUR sobre 25 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 8 | -6.94 EUR | 0% | 100% |
| nota global | medio | 8 | -1.27 EUR | 0% | 88% |
| nota global | alto | 9 | -2.75 EUR | 0% | 56% |
| puesto en el ranking | bajo | 8 | -2.09 EUR | 0% | 50% |
| puesto en el ranking | medio | 8 | -2.41 EUR | 0% | 88% |
| puesto en el ranking | alto | 9 | -6.06 EUR | 0% | 100% |
| potencial hasta objetivo | bajo | 8 | -2.41 EUR | 0% | 75% |
| potencial hasta objetivo | medio | 8 | -4.67 EUR | 0% | 88% |
| potencial hasta objetivo | alto | 9 | -3.76 EUR | 0% | 78% |
| dispersion | bajo | 8 | -2.41 EUR | 0% | 62% |
| dispersion | medio | 8 | -5.81 EUR | 0% | 88% |
| dispersion | alto | 9 | -2.75 EUR | 0% | 89% |
| % compra fuerte | bajo | 8 | -3.54 EUR | 0% | 62% |
| % compra fuerte | medio | 8 | -0.95 EUR | 0% | 88% |
| % compra fuerte | alto | 8 | -5.81 EUR | 0% | 88% |
| momentum 30d | bajo | 8 | -3.54 EUR | 0% | 75% |
| momentum 30d | medio | 8 | -4.36 EUR | 0% | 75% |
| momentum 30d | alto | 9 | -3.04 EUR | 0% | 89% |
| fuerza relativa | bajo | 8 | -2.41 EUR | 0% | 62% |
| fuerza relativa | medio | 8 | -5.49 EUR | 0% | 88% |
| fuerza relativa | alto | 9 | -3.04 EUR | 0% | 89% |
| RSI | bajo | 8 | -5.81 EUR | 0% | 88% |
| RSI | medio | 8 | -2.09 EUR | 0% | 88% |
| RSI | alto | 9 | -3.04 EUR | 0% | 67% |
| volumen relativo | bajo | 5 | -4.45 EUR | 0% | 80% |
| volumen relativo | medio | 5 | -6.26 EUR | 0% | 100% |
| volumen relativo | alto | 6 | -5.05 EUR | 0% | 83% |
| volatilidad | bajo | 5 | -4.45 EUR | 0% | 80% |
| volatilidad | medio | 5 | -4.45 EUR | 0% | 80% |
| volatilidad | alto | 6 | -6.57 EUR | 0% | 100% |
| liquidez | bajo | 5 | -4.45 EUR | 0% | 80% |
| liquidez | medio | 5 | -4.45 EUR | 0% | 80% |
| liquidez | alto | 6 | -6.57 EUR | 0% | 100% |
| distancia max 52s | bajo | 5 | -6.26 EUR | 0% | 100% |
| distancia max 52s | medio | 5 | -4.45 EUR | 0% | 80% |
| distancia max 52s | alto | 6 | -5.05 EUR | 0% | 83% |
| consenso | buy | 14 | -4.84 EUR | 0% | 93% |
| consenso | strong_buy | 11 | -2.07 EUR | 0% | 64% |
| tendencia tecnica | alcista | 15 | -3.67 EUR | 0% | 80% |
| tendencia tecnica | mixta | 8 | -3.54 EUR | 0% | 75% |
| tendencia analistas | mejorando | 14 | -3.54 EUR | 0% | 86% |
| tendencia analistas | estable | 10 | -4.19 EUR | 0% | 70% |
| regimen de mercado | favorable | 24 | -3.43 EUR | 0% | 79% |
| catalizador | sin catalizador | 25 | -3.62 EUR | 0% | 80% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -6.94 | -2.75 | **+4.19 EUR** |
| RSI | -5.81 | -3.04 | **+2.77 EUR** |
| distancia max 52s | -6.26 | -5.05 | **+1.21 EUR** |
| momentum 30d | -3.54 | -3.04 | **+0.50 EUR** |
| dispersion | -2.41 | -2.75 | **-0.35 EUR** |
| volumen relativo | -4.45 | -5.05 | **-0.61 EUR** |
| fuerza relativa | -2.41 | -3.04 | **-0.63 EUR** |
| potencial hasta objetivo | -2.41 | -3.76 | **-1.36 EUR** |
| volatilidad | -4.45 | -6.57 | **-2.12 EUR** |
| liquidez | -4.45 | -6.57 | **-2.12 EUR** |
| % compra fuerte | -3.54 | -5.81 | **-2.27 EUR** |
| puesto en el ranking | -2.09 | -6.06 | **-3.97 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
