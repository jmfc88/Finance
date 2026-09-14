# Simulacion en paralelo

Actualizado: 2026-09-14 12:39 · dia 22 de ejecucion
Proxima revision de ponderacion en 8 dias.

- Operaciones cerradas: **50**
- Operaciones abiertas: 66

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 16 | 32% | +1.16 EUR |
| plano | 0 | - | - |
| perdida | 16 | 32% | -7.51 EUR |
| nefasta | 18 | 36% | -5.05 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 16 | -2.25% | 0/16 (0%) | 4/16 | 6 |
| 11-20 | 17 | -2.74% | 0/17 (0%) | 1/17 | 6 |
| 21-30 | 17 | -6.48% | 0/17 (0%) | 0/17 | 5 |

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
| arranca antes (+3%) | -36.95 EUR | -7.39% | 0/5 | -10.00 EUR |
| LA REAL (escalera 25/08) | -192.62 EUR | -3.85% | 0/50 | -8.08 EUR |
| stop corto (5%) | -210.00 EUR | -7.00% | 0/30 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.85%**
- Aciertos (>= 5 EUR limpios): 0/50 (0%)
- Resultado acumulado ficticio: -192.62 EUR sobre 50 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 16 | -5.24 EUR | 0% | 69% |
| nota global | medio | 16 | -3.54 EUR | 0% | 81% |
| nota global | alto | 18 | -2.89 EUR | 0% | 56% |
| puesto en el ranking | bajo | 16 | -2.25 EUR | 0% | 44% |
| puesto en el ranking | medio | 16 | -2.97 EUR | 0% | 69% |
| puesto en el ranking | alto | 18 | -6.06 EUR | 0% | 89% |
| potencial hasta objetivo | bajo | 16 | -4.11 EUR | 0% | 69% |
| potencial hasta objetivo | medio | 16 | -4.11 EUR | 0% | 75% |
| potencial hasta objetivo | alto | 18 | -3.40 EUR | 0% | 61% |
| dispersion | bajo | 16 | -2.40 EUR | 0% | 50% |
| dispersion | medio | 16 | -5.08 EUR | 0% | 75% |
| dispersion | alto | 18 | -4.04 EUR | 0% | 78% |
| % compra fuerte | bajo | 15 | -4.45 EUR | 0% | 67% |
| % compra fuerte | medio | 15 | -2.63 EUR | 0% | 73% |
| % compra fuerte | alto | 17 | -4.73 EUR | 0% | 71% |
| momentum 30d | bajo | 16 | -3.54 EUR | 0% | 62% |
| momentum 30d | medio | 16 | -5.08 EUR | 0% | 75% |
| momentum 30d | alto | 18 | -3.04 EUR | 0% | 67% |
| fuerza relativa | bajo | 16 | -2.97 EUR | 0% | 56% |
| fuerza relativa | medio | 16 | -5.08 EUR | 0% | 81% |
| fuerza relativa | alto | 18 | -3.54 EUR | 0% | 67% |
| RSI | bajo | 16 | -4.11 EUR | 0% | 62% |
| RSI | medio | 16 | -2.81 EUR | 0% | 69% |
| RSI | alto | 18 | -4.55 EUR | 0% | 72% |
| volumen relativo | bajo | 12 | -3.54 EUR | 0% | 58% |
| volumen relativo | medio | 12 | -4.30 EUR | 0% | 75% |
| volumen relativo | alto | 13 | -4.59 EUR | 0% | 62% |
| volatilidad | bajo | 12 | -4.30 EUR | 0% | 67% |
| volatilidad | medio | 12 | -5.05 EUR | 0% | 75% |
| volatilidad | alto | 13 | -3.19 EUR | 0% | 54% |
| liquidez | bajo | 12 | -4.30 EUR | 0% | 67% |
| liquidez | medio | 12 | -4.30 EUR | 0% | 67% |
| liquidez | alto | 13 | -3.89 EUR | 0% | 62% |
| distancia max 52s | bajo | 12 | -5.05 EUR | 0% | 67% |
| distancia max 52s | medio | 12 | -3.54 EUR | 0% | 67% |
| distancia max 52s | alto | 13 | -3.89 EUR | 0% | 62% |
| consenso | buy | 32 | -4.96 EUR | 0% | 78% |
| consenso | strong_buy | 18 | -1.89 EUR | 0% | 50% |
| tendencia tecnica | alcista | 32 | -3.46 EUR | 0% | 62% |
| tendencia tecnica | mixta | 12 | -4.30 EUR | 0% | 75% |
| tendencia tecnica | bajista | 6 | -5.05 EUR | 0% | 83% |
| tendencia analistas | mejorando | 28 | -3.86 EUR | 0% | 71% |
| tendencia analistas | estable | 16 | -5.65 EUR | 0% | 81% |
| regimen de mercado | favorable | 46 | -3.68 EUR | 0% | 67% |
| catalizador | sin catalizador | 50 | -3.85 EUR | 0% | 68% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.24 | -2.89 | **+2.35 EUR** |
| distancia max 52s | -5.05 | -3.89 | **+1.16 EUR** |
| volatilidad | -4.30 | -3.19 | **+1.11 EUR** |
| potencial hasta objetivo | -4.11 | -3.40 | **+0.71 EUR** |
| momentum 30d | -3.54 | -3.04 | **+0.50 EUR** |
| liquidez | -4.30 | -3.89 | **+0.41 EUR** |
| % compra fuerte | -4.45 | -4.73 | **-0.28 EUR** |
| RSI | -4.11 | -4.55 | **-0.44 EUR** |
| fuerza relativa | -2.97 | -3.54 | **-0.57 EUR** |
| volumen relativo | -3.54 | -4.59 | **-1.05 EUR** |
| dispersion | -2.40 | -4.04 | **-1.64 EUR** |
| puesto en el ranking | -2.25 | -6.06 | **-3.82 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
