# Simulacion en paralelo

Actualizado: 2026-09-17 17:39 · dia 25 de ejecucion
Proxima revision de ponderacion en 5 dias.

- Operaciones cerradas: **64**
- Operaciones abiertas: 63

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 19 | 30% | +1.13 EUR |
| plano | 0 | - | - |
| perdida | 22 | 34% | -7.67 EUR |
| nefasta | 23 | 36% | -5.71 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 17 | -2.59% | 0/17 (0%) | 4/17 | 7 |
| 11-20 | 20 | -3.09% | 0/20 (0%) | 1/20 | 6 |
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
| LA REAL (escalera 25/08) | -278.50 EUR | -4.35% | 0/64 | -8.08 EUR |
| stop corto (5%) | -287.00 EUR | -7.00% | 0/41 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-4.35%**
- Aciertos (>= 5 EUR limpios): 0/64 (0%)
- Resultado acumulado ficticio: -278.50 EUR sobre 64 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 21 | -5.49 EUR | 0% | 71% |
| nota global | medio | 21 | -5.05 EUR | 0% | 86% |
| nota global | alto | 22 | -2.60 EUR | 0% | 55% |
| puesto en el ranking | bajo | 21 | -2.34 EUR | 0% | 52% |
| puesto en el ranking | medio | 21 | -4.19 EUR | 0% | 71% |
| puesto en el ranking | alto | 22 | -6.43 EUR | 0% | 86% |
| potencial hasta objetivo | bajo | 21 | -5.05 EUR | 0% | 76% |
| potencial hasta objetivo | medio | 21 | -4.62 EUR | 0% | 76% |
| potencial hasta objetivo | alto | 22 | -3.42 EUR | 0% | 59% |
| dispersion | bajo | 21 | -2.89 EUR | 0% | 52% |
| dispersion | medio | 21 | -5.36 EUR | 0% | 76% |
| dispersion | alto | 22 | -4.78 EUR | 0% | 82% |
| % compra fuerte | bajo | 20 | -5.81 EUR | 0% | 80% |
| % compra fuerte | medio | 20 | -3.09 EUR | 0% | 70% |
| % compra fuerte | alto | 20 | -4.77 EUR | 0% | 70% |
| momentum 30d | bajo | 21 | -3.76 EUR | 0% | 62% |
| momentum 30d | medio | 21 | -5.80 EUR | 0% | 81% |
| momentum 30d | alto | 22 | -3.54 EUR | 0% | 68% |
| fuerza relativa | bajo | 21 | -3.32 EUR | 0% | 57% |
| fuerza relativa | medio | 21 | -5.80 EUR | 0% | 86% |
| fuerza relativa | alto | 22 | -3.95 EUR | 0% | 68% |
| RSI | bajo | 21 | -4.19 EUR | 0% | 62% |
| RSI | medio | 21 | -3.64 EUR | 0% | 71% |
| RSI | alto | 22 | -5.19 EUR | 0% | 77% |
| volumen relativo | bajo | 16 | -4.11 EUR | 0% | 62% |
| volumen relativo | medio | 16 | -4.67 EUR | 0% | 75% |
| volumen relativo | alto | 18 | -5.05 EUR | 0% | 67% |
| volatilidad | bajo | 16 | -4.67 EUR | 0% | 69% |
| volatilidad | medio | 16 | -6.38 EUR | 0% | 88% |
| volatilidad | alto | 18 | -3.04 EUR | 0% | 50% |
| liquidez | bajo | 16 | -4.67 EUR | 0% | 69% |
| liquidez | medio | 16 | -4.67 EUR | 0% | 69% |
| liquidez | alto | 18 | -4.55 EUR | 0% | 67% |
| distancia max 52s | bajo | 16 | -4.67 EUR | 0% | 62% |
| distancia max 52s | medio | 16 | -4.11 EUR | 0% | 69% |
| distancia max 52s | alto | 18 | -5.05 EUR | 0% | 72% |
| consenso | buy | 44 | -5.40 EUR | 0% | 80% |
| consenso | strong_buy | 20 | -2.05 EUR | 0% | 50% |
| tendencia tecnica | alcista | 40 | -4.16 EUR | 0% | 68% |
| tendencia tecnica | mixta | 15 | -4.45 EUR | 0% | 73% |
| tendencia tecnica | bajista | 9 | -5.05 EUR | 0% | 78% |
| tendencia analistas | mejorando | 36 | -4.30 EUR | 0% | 72% |
| tendencia analistas | estable | 19 | -6.03 EUR | 0% | 84% |
| regimen de mercado | favorable | 54 | -4.17 EUR | 0% | 70% |
| regimen de mercado | neutro | 10 | -5.36 EUR | 0% | 70% |
| catalizador | sin catalizador | 63 | -4.29 EUR | 0% | 70% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.49 | -2.60 | **+2.89 EUR** |
| volatilidad | -4.67 | -3.04 | **+1.64 EUR** |
| potencial hasta objetivo | -5.05 | -3.42 | **+1.63 EUR** |
| % compra fuerte | -5.81 | -4.77 | **+1.04 EUR** |
| momentum 30d | -3.76 | -3.54 | **+0.22 EUR** |
| liquidez | -4.67 | -4.55 | **+0.13 EUR** |
| distancia max 52s | -4.67 | -5.05 | **-0.38 EUR** |
| fuerza relativa | -3.32 | -3.95 | **-0.63 EUR** |
| volumen relativo | -4.11 | -5.05 | **-0.95 EUR** |
| RSI | -4.19 | -5.19 | **-1.00 EUR** |
| dispersion | -2.89 | -4.78 | **-1.89 EUR** |
| puesto en el ranking | -2.34 | -6.43 | **-4.09 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
