# Simulacion en paralelo

Actualizado: 2026-09-11 20:59 · dia 19 de ejecucion
Proxima revision de ponderacion en 11 dias.

- Operaciones cerradas: **48**
- Operaciones abiertas: 66

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 16 | 33% | +1.16 EUR |
| plano | 0 | - | - |
| perdida | 14 | 29% | -7.43 EUR |
| nefasta | 18 | 38% | -5.05 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 16 | -2.25% | 0/16 (0%) | 4/16 | 6 |
| 11-20 | 16 | -2.40% | 0/16 (0%) | 1/16 | 6 |
| 21-30 | 16 | -6.38% | 0/16 (0%) | 0/16 | 5 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida


## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -14.73 EUR | -2.46% | 0/6 | -10.00 EUR |
| trailing suelto (7%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| sin trailing, solo stop | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| arranca despues (+8%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| actual (8% / +5% / 5%) | -20.00 EUR | -10.00% | 0/2 | -10.00 EUR |
| arranca antes (+3%) | -26.95 EUR | -6.74% | 0/4 | -10.00 EUR |
| LA REAL (escalera 25/08) | -176.46 EUR | -3.68% | 0/48 | -8.08 EUR |
| stop corto (5%) | -196.00 EUR | -7.00% | 0/28 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.68%**
- Aciertos (>= 5 EUR limpios): 0/48 (0%)
- Resultado acumulado ficticio: -176.46 EUR sobre 48 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 16 | -5.24 EUR | 0% | 69% |
| nota global | medio | 16 | -2.97 EUR | 0% | 75% |
| nota global | alto | 16 | -2.81 EUR | 0% | 56% |
| puesto en el ranking | bajo | 16 | -2.25 EUR | 0% | 44% |
| puesto en el ranking | medio | 16 | -2.40 EUR | 0% | 62% |
| puesto en el ranking | alto | 16 | -6.38 EUR | 0% | 94% |
| potencial hasta objetivo | bajo | 16 | -3.54 EUR | 0% | 69% |
| potencial hasta objetivo | medio | 16 | -3.95 EUR | 0% | 69% |
| potencial hasta objetivo | alto | 16 | -3.54 EUR | 0% | 62% |
| dispersion | bajo | 16 | -2.40 EUR | 0% | 50% |
| dispersion | medio | 16 | -5.08 EUR | 0% | 75% |
| dispersion | alto | 16 | -3.54 EUR | 0% | 75% |
| % compra fuerte | bajo | 15 | -4.45 EUR | 0% | 67% |
| % compra fuerte | medio | 15 | -2.03 EUR | 0% | 67% |
| % compra fuerte | alto | 15 | -4.88 EUR | 0% | 73% |
| momentum 30d | bajo | 16 | -3.54 EUR | 0% | 62% |
| momentum 30d | medio | 16 | -4.52 EUR | 0% | 75% |
| momentum 30d | alto | 16 | -2.97 EUR | 0% | 62% |
| fuerza relativa | bajo | 16 | -2.97 EUR | 0% | 56% |
| fuerza relativa | medio | 16 | -4.52 EUR | 0% | 75% |
| fuerza relativa | alto | 16 | -3.54 EUR | 0% | 69% |
| RSI | bajo | 16 | -4.11 EUR | 0% | 62% |
| RSI | medio | 16 | -2.81 EUR | 0% | 69% |
| RSI | alto | 16 | -4.11 EUR | 0% | 69% |
| volumen relativo | bajo | 11 | -3.13 EUR | 0% | 55% |
| volumen relativo | medio | 11 | -3.95 EUR | 0% | 73% |
| volumen relativo | alto | 13 | -4.59 EUR | 0% | 62% |
| volatilidad | bajo | 11 | -3.95 EUR | 0% | 64% |
| volatilidad | medio | 11 | -4.78 EUR | 0% | 73% |
| volatilidad | alto | 13 | -3.19 EUR | 0% | 54% |
| liquidez | bajo | 11 | -3.95 EUR | 0% | 64% |
| liquidez | medio | 11 | -3.95 EUR | 0% | 64% |
| liquidez | alto | 13 | -3.89 EUR | 0% | 62% |
| distancia max 52s | bajo | 11 | -4.78 EUR | 0% | 64% |
| distancia max 52s | medio | 11 | -3.95 EUR | 0% | 73% |
| distancia max 52s | alto | 13 | -3.19 EUR | 0% | 54% |
| consenso | buy | 30 | -4.75 EUR | 0% | 77% |
| consenso | strong_buy | 18 | -1.89 EUR | 0% | 50% |
| tendencia tecnica | alcista | 31 | -3.31 EUR | 0% | 61% |
| tendencia tecnica | mixta | 11 | -3.95 EUR | 0% | 73% |
| tendencia tecnica | bajista | 6 | -5.05 EUR | 0% | 83% |
| tendencia analistas | mejorando | 26 | -3.54 EUR | 0% | 69% |
| tendencia analistas | estable | 16 | -5.65 EUR | 0% | 81% |
| regimen de mercado | favorable | 44 | -3.48 EUR | 0% | 66% |
| catalizador | sin catalizador | 48 | -3.68 EUR | 0% | 67% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.24 | -2.81 | **+2.43 EUR** |
| distancia max 52s | -4.78 | -3.19 | **+1.59 EUR** |
| volatilidad | -3.95 | -3.19 | **+0.76 EUR** |
| momentum 30d | -3.54 | -2.97 | **+0.57 EUR** |
| liquidez | -3.95 | -3.89 | **+0.06 EUR** |
| potencial hasta objetivo | -3.54 | -3.54 | **+0.00 EUR** |
| RSI | -4.11 | -4.11 | **+0.00 EUR** |
| % compra fuerte | -4.45 | -4.88 | **-0.44 EUR** |
| fuerza relativa | -2.97 | -3.54 | **-0.57 EUR** |
| dispersion | -2.40 | -3.54 | **-1.13 EUR** |
| volumen relativo | -3.13 | -4.59 | **-1.46 EUR** |
| puesto en el ranking | -2.25 | -6.38 | **-4.13 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
