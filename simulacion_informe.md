# Simulacion en paralelo

Actualizado: 2026-09-15 11:39 · dia 23 de ejecucion
Proxima revision de ponderacion en 7 dias.

- Operaciones cerradas: **59**
- Operaciones abiertas: 62

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 17 | 29% | +1.15 EUR |
| plano | 0 | - | - |
| perdida | 20 | 34% | -7.63 EUR |
| nefasta | 22 | 37% | -5.60 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 16 | -2.25% | 0/16 (0%) | 4/16 | 6 |
| 11-20 | 18 | -3.04% | 0/18 (0%) | 1/18 | 6 |
| 21-30 | 25 | -6.63% | 0/25 (0%) | 0/25 | 6 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida


## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -24.73 EUR | -3.53% | 0/7 | -10.00 EUR |
| trailing suelto (7%) | -30.00 EUR | -10.00% | 0/3 | -10.00 EUR |
| sin trailing, solo stop | -30.00 EUR | -10.00% | 0/3 | -10.00 EUR |
| arranca despues (+8%) | -30.00 EUR | -10.00% | 0/3 | -10.00 EUR |
| actual (8% / +5% / 5%) | -30.00 EUR | -10.00% | 0/3 | -10.00 EUR |
| arranca antes (+3%) | -40.41 EUR | -6.74% | 0/6 | -10.00 EUR |
| LA REAL (escalera 25/08) | -256.26 EUR | -4.34% | 0/59 | -8.08 EUR |
| stop corto (5%) | -266.00 EUR | -7.00% | 0/38 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-4.34%**
- Aciertos (>= 5 EUR limpios): 0/59 (0%)
- Resultado acumulado ficticio: -256.26 EUR sobre 59 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 19 | -5.69 EUR | 0% | 74% |
| nota global | medio | 19 | -5.21 EUR | 0% | 89% |
| nota global | alto | 21 | -2.34 EUR | 0% | 52% |
| puesto en el ranking | bajo | 19 | -2.21 EUR | 0% | 47% |
| puesto en el ranking | medio | 19 | -3.78 EUR | 0% | 74% |
| puesto en el ranking | alto | 21 | -6.78 EUR | 0% | 90% |
| potencial hasta objetivo | bajo | 19 | -4.73 EUR | 0% | 74% |
| potencial hasta objetivo | medio | 19 | -4.73 EUR | 0% | 79% |
| potencial hasta objetivo | alto | 21 | -3.64 EUR | 0% | 62% |
| dispersion | bajo | 19 | -2.82 EUR | 0% | 53% |
| dispersion | medio | 19 | -5.56 EUR | 0% | 79% |
| dispersion | alto | 21 | -4.62 EUR | 0% | 81% |
| % compra fuerte | bajo | 18 | -5.56 EUR | 0% | 78% |
| % compra fuerte | medio | 18 | -3.04 EUR | 0% | 72% |
| % compra fuerte | alto | 19 | -5.08 EUR | 0% | 74% |
| momentum 30d | bajo | 19 | -4.26 EUR | 0% | 68% |
| momentum 30d | medio | 19 | -5.56 EUR | 0% | 79% |
| momentum 30d | alto | 21 | -3.32 EUR | 0% | 67% |
| fuerza relativa | bajo | 19 | -3.78 EUR | 0% | 63% |
| fuerza relativa | medio | 19 | -5.56 EUR | 0% | 84% |
| fuerza relativa | alto | 21 | -3.76 EUR | 0% | 67% |
| RSI | bajo | 19 | -4.73 EUR | 0% | 68% |
| RSI | medio | 19 | -3.17 EUR | 0% | 68% |
| RSI | alto | 21 | -5.05 EUR | 0% | 76% |
| volumen relativo | bajo | 15 | -3.84 EUR | 0% | 60% |
| volumen relativo | medio | 15 | -5.05 EUR | 0% | 80% |
| volumen relativo | alto | 16 | -5.24 EUR | 0% | 69% |
| volatilidad | bajo | 15 | -5.05 EUR | 0% | 73% |
| volatilidad | medio | 15 | -6.26 EUR | 0% | 87% |
| volatilidad | alto | 16 | -2.97 EUR | 0% | 50% |
| liquidez | bajo | 15 | -4.45 EUR | 0% | 67% |
| liquidez | medio | 15 | -5.66 EUR | 0% | 80% |
| liquidez | alto | 16 | -4.11 EUR | 0% | 62% |
| distancia max 52s | bajo | 15 | -5.05 EUR | 0% | 67% |
| distancia max 52s | medio | 15 | -4.45 EUR | 0% | 73% |
| distancia max 52s | alto | 16 | -4.67 EUR | 0% | 69% |
| consenso | buy | 39 | -5.52 EUR | 0% | 82% |
| consenso | strong_buy | 20 | -2.05 EUR | 0% | 50% |
| tendencia tecnica | alcista | 37 | -3.84 EUR | 0% | 65% |
| tendencia tecnica | mixta | 14 | -4.84 EUR | 0% | 79% |
| tendencia tecnica | bajista | 8 | -5.81 EUR | 0% | 88% |
| tendencia analistas | mejorando | 31 | -4.27 EUR | 0% | 74% |
| tendencia analistas | estable | 19 | -6.03 EUR | 0% | 84% |
| regimen de mercado | favorable | 50 | -4.03 EUR | 0% | 70% |
| regimen de mercado | neutro | 9 | -6.06 EUR | 0% | 78% |
| catalizador | sin catalizador | 58 | -4.28 EUR | 0% | 71% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.69 | -2.34 | **+3.35 EUR** |
| volatilidad | -5.05 | -2.97 | **+2.08 EUR** |
| potencial hasta objetivo | -4.73 | -3.64 | **+1.10 EUR** |
| momentum 30d | -4.26 | -3.32 | **+0.93 EUR** |
| % compra fuerte | -5.56 | -5.08 | **+0.48 EUR** |
| distancia max 52s | -5.05 | -4.67 | **+0.38 EUR** |
| liquidez | -4.45 | -4.11 | **+0.34 EUR** |
| fuerza relativa | -3.78 | -3.76 | **+0.02 EUR** |
| RSI | -4.73 | -5.05 | **-0.32 EUR** |
| volumen relativo | -3.84 | -5.24 | **-1.40 EUR** |
| dispersion | -2.82 | -4.62 | **-1.80 EUR** |
| puesto en el ranking | -2.21 | -6.78 | **-4.57 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
