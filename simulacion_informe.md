# Simulacion en paralelo

Actualizado: 2026-09-16 21:18 · dia 24 de ejecucion
Proxima revision de ponderacion en 6 dias.

- Operaciones cerradas: **63**
- Operaciones abiertas: 64

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 18 | 29% | +1.14 EUR |
| plano | 0 | - | - |
| perdida | 22 | 35% | -7.67 EUR |
| nefasta | 23 | 37% | -5.71 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 17 | -2.59% | 0/17 (0%) | 4/17 | 7 |
| 11-20 | 20 | -3.09% | 0/20 (0%) | 1/20 | 6 |
| 21-30 | 26 | -6.68% | 0/26 (0%) | 0/26 | 6 |

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
| LA REAL (escalera 25/08) | -279.50 EUR | -4.44% | 0/63 | -8.08 EUR |
| stop corto (5%) | -287.00 EUR | -7.00% | 0/41 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-4.44%**
- Aciertos (>= 5 EUR limpios): 0/63 (0%)
- Resultado acumulado ficticio: -279.50 EUR sobre 63 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 21 | -5.49 EUR | 0% | 71% |
| nota global | medio | 21 | -5.05 EUR | 0% | 90% |
| nota global | alto | 21 | -2.77 EUR | 0% | 52% |
| puesto en el ranking | bajo | 21 | -2.34 EUR | 0% | 52% |
| puesto en el ranking | medio | 21 | -4.19 EUR | 0% | 71% |
| puesto en el ranking | alto | 21 | -6.78 EUR | 0% | 90% |
| potencial hasta objetivo | bajo | 21 | -5.05 EUR | 0% | 76% |
| potencial hasta objetivo | medio | 21 | -5.05 EUR | 0% | 81% |
| potencial hasta objetivo | alto | 21 | -3.20 EUR | 0% | 57% |
| dispersion | bajo | 21 | -2.89 EUR | 0% | 52% |
| dispersion | medio | 21 | -5.36 EUR | 0% | 76% |
| dispersion | alto | 21 | -5.05 EUR | 0% | 86% |
| % compra fuerte | bajo | 19 | -5.69 EUR | 0% | 79% |
| % compra fuerte | medio | 19 | -2.82 EUR | 0% | 68% |
| % compra fuerte | alto | 21 | -5.36 EUR | 0% | 76% |
| momentum 30d | bajo | 21 | -4.19 EUR | 0% | 67% |
| momentum 30d | medio | 21 | -5.36 EUR | 0% | 76% |
| momentum 30d | alto | 21 | -3.76 EUR | 0% | 71% |
| fuerza relativa | bajo | 21 | -3.76 EUR | 0% | 62% |
| fuerza relativa | medio | 21 | -5.36 EUR | 0% | 81% |
| fuerza relativa | alto | 21 | -4.19 EUR | 0% | 71% |
| RSI | bajo | 21 | -4.62 EUR | 0% | 67% |
| RSI | medio | 21 | -3.64 EUR | 0% | 71% |
| RSI | alto | 21 | -5.05 EUR | 0% | 76% |
| volumen relativo | bajo | 16 | -4.11 EUR | 0% | 62% |
| volumen relativo | medio | 16 | -4.67 EUR | 0% | 75% |
| volumen relativo | alto | 17 | -5.41 EUR | 0% | 71% |
| volatilidad | bajo | 16 | -5.24 EUR | 0% | 75% |
| volatilidad | medio | 16 | -6.38 EUR | 0% | 88% |
| volatilidad | alto | 17 | -2.74 EUR | 0% | 47% |
| liquidez | bajo | 16 | -4.67 EUR | 0% | 69% |
| liquidez | medio | 16 | -4.67 EUR | 0% | 75% |
| liquidez | alto | 17 | -4.88 EUR | 0% | 65% |
| distancia max 52s | bajo | 16 | -4.67 EUR | 0% | 62% |
| distancia max 52s | medio | 16 | -4.11 EUR | 0% | 69% |
| distancia max 52s | alto | 17 | -5.41 EUR | 0% | 76% |
| consenso | buy | 43 | -5.55 EUR | 0% | 81% |
| consenso | strong_buy | 20 | -2.05 EUR | 0% | 50% |
| tendencia tecnica | alcista | 40 | -4.16 EUR | 0% | 68% |
| tendencia tecnica | mixta | 14 | -4.84 EUR | 0% | 79% |
| tendencia tecnica | bajista | 9 | -5.05 EUR | 0% | 78% |
| tendencia analistas | mejorando | 35 | -4.45 EUR | 0% | 74% |
| tendencia analistas | estable | 19 | -6.03 EUR | 0% | 84% |
| regimen de mercado | favorable | 54 | -4.17 EUR | 0% | 70% |
| regimen de mercado | neutro | 9 | -6.06 EUR | 0% | 78% |
| catalizador | sin catalizador | 62 | -4.38 EUR | 0% | 71% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.49 | -2.77 | **+2.72 EUR** |
| volatilidad | -5.24 | -2.74 | **+2.50 EUR** |
| potencial hasta objetivo | -5.05 | -3.20 | **+1.85 EUR** |
| momentum 30d | -4.19 | -3.76 | **+0.43 EUR** |
| % compra fuerte | -5.69 | -5.36 | **+0.33 EUR** |
| liquidez | -4.67 | -4.88 | **-0.20 EUR** |
| RSI | -4.62 | -5.05 | **-0.43 EUR** |
| fuerza relativa | -3.76 | -4.19 | **-0.43 EUR** |
| distancia max 52s | -4.67 | -5.41 | **-0.73 EUR** |
| volumen relativo | -4.11 | -5.41 | **-1.30 EUR** |
| dispersion | -2.89 | -5.05 | **-2.16 EUR** |
| puesto en el ranking | -2.34 | -6.78 | **-4.44 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
