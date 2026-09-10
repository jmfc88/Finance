# Simulacion en paralelo

Actualizado: 2026-09-10 23:13 · dia 18 de ejecucion
Proxima revision de ponderacion en 12 dias.

- Operaciones cerradas: **47**
- Operaciones abiertas: 61

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 16 | 34% | +1.16 EUR |
| plano | 0 | - | - |
| perdida | 14 | 30% | -7.43 EUR |
| nefasta | 17 | 36% | -4.88 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 15 | -1.86% | 0/15 (0%) | 4/15 | 7 |
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
| LA REAL (escalera 25/08) | -168.38 EUR | -3.58% | 0/47 | -8.08 EUR |
| stop corto (5%) | -189.00 EUR | -7.00% | 0/27 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.58%**
- Aciertos (>= 5 EUR limpios): 0/47 (0%)
- Resultado acumulado ficticio: -168.38 EUR sobre 47 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 15 | -5.05 EUR | 0% | 67% |
| nota global | medio | 15 | -3.24 EUR | 0% | 80% |
| nota global | alto | 17 | -2.59 EUR | 0% | 53% |
| puesto en el ranking | bajo | 15 | -1.86 EUR | 0% | 40% |
| puesto en el ranking | medio | 15 | -2.63 EUR | 0% | 67% |
| puesto en el ranking | alto | 17 | -5.94 EUR | 0% | 88% |
| potencial hasta objetivo | bajo | 15 | -3.24 EUR | 0% | 67% |
| potencial hasta objetivo | medio | 15 | -4.45 EUR | 0% | 73% |
| potencial hasta objetivo | alto | 17 | -3.12 EUR | 0% | 59% |
| dispersion | bajo | 15 | -2.03 EUR | 0% | 47% |
| dispersion | medio | 15 | -5.66 EUR | 0% | 80% |
| dispersion | alto | 17 | -3.12 EUR | 0% | 71% |
| % compra fuerte | bajo | 14 | -4.19 EUR | 0% | 64% |
| % compra fuerte | medio | 14 | -2.24 EUR | 0% | 71% |
| % compra fuerte | alto | 16 | -4.52 EUR | 0% | 69% |
| momentum 30d | bajo | 15 | -3.24 EUR | 0% | 60% |
| momentum 30d | medio | 15 | -4.28 EUR | 0% | 73% |
| momentum 30d | alto | 17 | -3.27 EUR | 0% | 65% |
| fuerza relativa | bajo | 15 | -3.24 EUR | 0% | 60% |
| fuerza relativa | medio | 15 | -4.28 EUR | 0% | 73% |
| fuerza relativa | alto | 17 | -3.27 EUR | 0% | 65% |
| RSI | bajo | 15 | -4.45 EUR | 0% | 67% |
| RSI | medio | 15 | -2.46 EUR | 0% | 60% |
| RSI | alto | 17 | -3.81 EUR | 0% | 71% |
| volumen relativo | bajo | 11 | -3.13 EUR | 0% | 55% |
| volumen relativo | medio | 11 | -3.95 EUR | 0% | 73% |
| volumen relativo | alto | 12 | -4.30 EUR | 0% | 58% |
| volatilidad | bajo | 11 | -3.95 EUR | 0% | 64% |
| volatilidad | medio | 11 | -4.78 EUR | 0% | 73% |
| volatilidad | alto | 12 | -2.78 EUR | 0% | 50% |
| liquidez | bajo | 11 | -3.95 EUR | 0% | 64% |
| liquidez | medio | 11 | -3.13 EUR | 0% | 64% |
| liquidez | alto | 12 | -4.30 EUR | 0% | 58% |
| distancia max 52s | bajo | 11 | -4.78 EUR | 0% | 64% |
| distancia max 52s | medio | 11 | -3.95 EUR | 0% | 73% |
| distancia max 52s | alto | 12 | -2.78 EUR | 0% | 50% |
| consenso | buy | 30 | -4.75 EUR | 0% | 77% |
| consenso | strong_buy | 17 | -1.52 EUR | 0% | 47% |
| tendencia tecnica | alcista | 30 | -3.15 EUR | 0% | 60% |
| tendencia tecnica | mixta | 11 | -3.95 EUR | 0% | 73% |
| tendencia tecnica | bajista | 6 | -5.05 EUR | 0% | 83% |
| tendencia analistas | mejorando | 25 | -3.36 EUR | 0% | 68% |
| tendencia analistas | estable | 16 | -5.65 EUR | 0% | 81% |
| regimen de mercado | favorable | 43 | -3.38 EUR | 0% | 65% |
| catalizador | sin catalizador | 47 | -3.58 EUR | 0% | 66% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.05 | -2.59 | **+2.46 EUR** |
| distancia max 52s | -4.78 | -2.78 | **+1.99 EUR** |
| volatilidad | -3.95 | -2.78 | **+1.17 EUR** |
| RSI | -4.45 | -3.81 | **+0.64 EUR** |
| potencial hasta objetivo | -3.24 | -3.12 | **+0.11 EUR** |
| momentum 30d | -3.24 | -3.27 | **-0.04 EUR** |
| fuerza relativa | -3.24 | -3.27 | **-0.04 EUR** |
| % compra fuerte | -4.19 | -4.52 | **-0.33 EUR** |
| liquidez | -3.95 | -4.30 | **-0.34 EUR** |
| dispersion | -2.03 | -3.12 | **-1.10 EUR** |
| volumen relativo | -3.13 | -4.30 | **-1.17 EUR** |
| puesto en el ranking | -1.86 | -5.94 | **-4.09 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
