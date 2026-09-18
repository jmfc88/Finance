# Simulacion en paralelo

Actualizado: 2026-09-18 17:05 · dia 26 de ejecucion
Proxima revision de ponderacion en 4 dias.

- Operaciones cerradas: **66**
- Operaciones abiertas: 63

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 20 | 30% | +1.13 EUR |
| plano | 0 | - | - |
| perdida | 23 | 35% | -7.69 EUR |
| nefasta | 23 | 35% | -5.71 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 18 | -2.39% | 0/18 (0%) | 4/18 | 7 |
| 11-20 | 21 | -3.32% | 0/21 (0%) | 1/21 | 6 |
| 21-30 | 27 | -6.40% | 0/27 (0%) | 0/27 | 6 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida


## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -34.73 EUR | -4.34% | 0/8 | -10.00 EUR |
| trailing suelto (7%) | -40.00 EUR | -10.00% | 0/4 | -10.00 EUR |
| sin trailing, solo stop | -40.00 EUR | -10.00% | 0/4 | -10.00 EUR |
| arranca despues (+8%) | -40.00 EUR | -10.00% | 0/4 | -10.00 EUR |
| actual (8% / +5% / 5%) | -40.00 EUR | -10.00% | 0/4 | -10.00 EUR |
| arranca antes (+3%) | -50.41 EUR | -7.20% | 0/7 | -10.00 EUR |
| LA REAL (escalera 25/08) | -285.58 EUR | -4.33% | 0/66 | -8.08 EUR |
| stop corto (5%) | -294.00 EUR | -7.00% | 0/42 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-4.33%**
- Aciertos (>= 5 EUR limpios): 0/66 (0%)
- Resultado acumulado ficticio: -285.58 EUR sobre 66 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 22 | -5.19 EUR | 0% | 68% |
| nota global | medio | 22 | -5.19 EUR | 0% | 91% |
| nota global | alto | 22 | -2.60 EUR | 0% | 50% |
| puesto en el ranking | bajo | 22 | -2.19 EUR | 0% | 50% |
| puesto en el ranking | medio | 22 | -4.37 EUR | 0% | 73% |
| puesto en el ranking | alto | 22 | -6.43 EUR | 0% | 86% |
| potencial hasta objetivo | bajo | 22 | -5.19 EUR | 0% | 77% |
| potencial hasta objetivo | medio | 22 | -4.37 EUR | 0% | 73% |
| potencial hasta objetivo | alto | 22 | -3.42 EUR | 0% | 59% |
| dispersion | bajo | 22 | -2.71 EUR | 0% | 50% |
| dispersion | medio | 22 | -5.49 EUR | 0% | 77% |
| dispersion | alto | 22 | -4.78 EUR | 0% | 82% |
| % compra fuerte | bajo | 20 | -5.81 EUR | 0% | 80% |
| % compra fuerte | medio | 20 | -3.09 EUR | 0% | 70% |
| % compra fuerte | alto | 22 | -4.66 EUR | 0% | 68% |
| momentum 30d | bajo | 22 | -3.95 EUR | 0% | 64% |
| momentum 30d | medio | 22 | -5.49 EUR | 0% | 77% |
| momentum 30d | alto | 22 | -3.54 EUR | 0% | 68% |
| fuerza relativa | bajo | 22 | -3.54 EUR | 0% | 59% |
| fuerza relativa | medio | 22 | -5.08 EUR | 0% | 77% |
| fuerza relativa | alto | 22 | -4.37 EUR | 0% | 73% |
| RSI | bajo | 22 | -4.37 EUR | 0% | 64% |
| RSI | medio | 22 | -3.84 EUR | 0% | 73% |
| RSI | alto | 22 | -4.78 EUR | 0% | 73% |
| volumen relativo | bajo | 17 | -4.34 EUR | 0% | 65% |
| volumen relativo | medio | 17 | -4.34 EUR | 0% | 71% |
| volumen relativo | alto | 18 | -5.05 EUR | 0% | 67% |
| volatilidad | bajo | 17 | -4.88 EUR | 0% | 71% |
| volatilidad | medio | 17 | -6.48 EUR | 0% | 88% |
| volatilidad | alto | 18 | -2.53 EUR | 0% | 44% |
| liquidez | bajo | 17 | -4.88 EUR | 0% | 71% |
| liquidez | medio | 17 | -4.34 EUR | 0% | 71% |
| liquidez | alto | 18 | -4.55 EUR | 0% | 61% |
| distancia max 52s | bajo | 17 | -4.88 EUR | 0% | 65% |
| distancia max 52s | medio | 17 | -3.81 EUR | 0% | 65% |
| distancia max 52s | alto | 18 | -5.05 EUR | 0% | 72% |
| consenso | buy | 45 | -5.46 EUR | 0% | 80% |
| consenso | strong_buy | 21 | -1.91 EUR | 0% | 48% |
| tendencia tecnica | alcista | 42 | -4.13 EUR | 0% | 67% |
| tendencia tecnica | mixta | 15 | -4.45 EUR | 0% | 73% |
| tendencia tecnica | bajista | 9 | -5.05 EUR | 0% | 78% |
| tendencia analistas | mejorando | 37 | -4.15 EUR | 0% | 70% |
| tendencia analistas | estable | 20 | -6.14 EUR | 0% | 85% |
| regimen de mercado | favorable | 55 | -4.07 EUR | 0% | 69% |
| regimen de mercado | neutro | 11 | -5.60 EUR | 0% | 73% |
| catalizador | sin catalizador | 65 | -4.27 EUR | 0% | 69% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.19 | -2.60 | **+2.59 EUR** |
| volatilidad | -4.88 | -2.53 | **+2.34 EUR** |
| potencial hasta objetivo | -5.19 | -3.42 | **+1.77 EUR** |
| % compra fuerte | -5.81 | -4.66 | **+1.15 EUR** |
| momentum 30d | -3.95 | -3.54 | **+0.41 EUR** |
| liquidez | -4.88 | -4.55 | **+0.33 EUR** |
| distancia max 52s | -4.88 | -5.05 | **-0.18 EUR** |
| RSI | -4.37 | -4.78 | **-0.41 EUR** |
| volumen relativo | -4.34 | -5.05 | **-0.71 EUR** |
| fuerza relativa | -3.54 | -4.37 | **-0.83 EUR** |
| dispersion | -2.71 | -4.78 | **-2.06 EUR** |
| puesto en el ranking | -2.19 | -6.43 | **-4.24 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
