# Simulacion en paralelo

Actualizado: 2026-09-24 06:09 · dia 32 de ejecucion
**Revision nº2 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **91**
- Operaciones abiertas: 57

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 1 | 1% | +16.67 EUR |
| beneficio | 1 | 1% | +5.55 EUR |
| flojo | 31 | 34% | +1.16 EUR |
| plano | 4 | 4% | -1.70 EUR |
| perdida | 30 | 33% | -7.01 EUR |
| nefasta | 24 | 26% | -5.81 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 23 | -1.77% | 0/23 (0%) | 5/23 | 8 |
| 11-20 | 28 | -1.96% | 2/28 (7%) | 3/28 | 8 |
| 21-30 | 40 | -5.07% | 0/40 (0%) | 0/40 | 8 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 11 operaciones, media -2.43%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -47.10 EUR | -2.24% | 1/21 | -10.00 EUR |
| arranca despues (+8%) | -52.20 EUR | -3.26% | 2/16 | -10.00 EUR |
| actual (8% / +5% / 5%) | -52.20 EUR | -3.26% | 2/16 | -10.00 EUR |
| trailing suelto (7%) | -54.65 EUR | -3.42% | 2/16 | -10.00 EUR |
| sin trailing, solo stop | -66.71 EUR | -4.45% | 1/15 | -10.00 EUR |
| arranca antes (+3%) | -68.73 EUR | -3.44% | 2/20 | -10.00 EUR |
| LA REAL (escalera 25/08) | -298.24 EUR | -3.28% | 2/91 | -8.08 EUR |
| stop corto (5%) | -340.79 EUR | -5.88% | 2/58 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.28%**
- Aciertos (>= 5 EUR limpios): 2/91 (2%)
- Resultado acumulado ficticio: -298.24 EUR sobre 91 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 30 | -4.30 EUR | 0% | 60% |
| nota global | medio | 30 | -3.90 EUR | 3% | 73% |
| nota global | alto | 31 | -1.68 EUR | 3% | 45% |
| puesto en el ranking | bajo | 30 | -1.47 EUR | 3% | 40% |
| puesto en el ranking | medio | 30 | -3.23 EUR | 3% | 63% |
| puesto en el ranking | alto | 31 | -5.07 EUR | 0% | 74% |
| potencial hasta objetivo | bajo | 30 | -4.01 EUR | 3% | 63% |
| potencial hasta objetivo | medio | 30 | -3.03 EUR | 0% | 60% |
| potencial hasta objetivo | alto | 31 | -2.81 EUR | 3% | 55% |
| dispersion | bajo | 30 | -1.00 EUR | 3% | 37% |
| dispersion | medio | 30 | -4.96 EUR | 0% | 73% |
| dispersion | alto | 31 | -3.85 EUR | 3% | 68% |
| % compra fuerte | bajo | 28 | -4.33 EUR | 4% | 68% |
| % compra fuerte | medio | 28 | -3.00 EUR | 0% | 64% |
| % compra fuerte | alto | 30 | -3.48 EUR | 0% | 53% |
| momentum 30d | bajo | 30 | -2.85 EUR | 0% | 50% |
| momentum 30d | medio | 30 | -3.59 EUR | 3% | 60% |
| momentum 30d | alto | 31 | -3.39 EUR | 3% | 68% |
| fuerza relativa | bajo | 30 | -3.18 EUR | 0% | 57% |
| fuerza relativa | medio | 30 | -3.38 EUR | 0% | 57% |
| fuerza relativa | alto | 31 | -3.26 EUR | 6% | 65% |
| RSI | bajo | 30 | -2.76 EUR | 3% | 53% |
| RSI | medio | 30 | -2.91 EUR | 0% | 57% |
| RSI | alto | 31 | -4.14 EUR | 3% | 68% |
| volumen relativo | bajo | 24 | -3.13 EUR | 4% | 58% |
| volumen relativo | medio | 24 | -3.29 EUR | 0% | 58% |
| volumen relativo | alto | 26 | -3.54 EUR | 0% | 50% |
| volatilidad | bajo | 24 | -3.76 EUR | 0% | 54% |
| volatilidad | medio | 24 | -4.17 EUR | 0% | 67% |
| volatilidad | alto | 26 | -2.14 EUR | 4% | 46% |
| liquidez | bajo | 24 | -3.35 EUR | 0% | 54% |
| liquidez | medio | 24 | -2.49 EUR | 4% | 54% |
| liquidez | alto | 26 | -4.07 EUR | 0% | 58% |
| distancia max 52s | bajo | 24 | -2.60 EUR | 4% | 50% |
| distancia max 52s | medio | 24 | -3.33 EUR | 0% | 58% |
| distancia max 52s | alto | 26 | -3.99 EUR | 0% | 58% |
| consenso | buy | 63 | -4.44 EUR | 2% | 70% |
| consenso | strong_buy | 28 | -0.66 EUR | 4% | 36% |
| tendencia tecnica | alcista | 57 | -3.24 EUR | 4% | 60% |
| tendencia tecnica | mixta | 22 | -2.81 EUR | 0% | 55% |
| tendencia tecnica | bajista | 12 | -4.30 EUR | 0% | 67% |
| tendencia analistas | mejorando | 47 | -3.32 EUR | 2% | 60% |
| tendencia analistas | estable | 31 | -4.93 EUR | 0% | 74% |
| regimen de mercado | favorable | 72 | -3.27 EUR | 3% | 62% |
| regimen de mercado | neutro | 19 | -3.30 EUR | 0% | 47% |
| catalizador | sin catalizador | 90 | -3.22 EUR | 2% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.30 | -1.68 | **+2.62 EUR** |
| volatilidad | -3.76 | -2.14 | **+1.62 EUR** |
| potencial hasta objetivo | -4.01 | -2.81 | **+1.20 EUR** |
| % compra fuerte | -4.33 | -3.48 | **+0.85 EUR** |
| fuerza relativa | -3.18 | -3.26 | **-0.08 EUR** |
| volumen relativo | -3.13 | -3.54 | **-0.41 EUR** |
| momentum 30d | -2.85 | -3.39 | **-0.54 EUR** |
| liquidez | -3.35 | -4.07 | **-0.72 EUR** |
| RSI | -2.76 | -4.14 | **-1.38 EUR** |
| distancia max 52s | -2.60 | -3.99 | **-1.39 EUR** |
| dispersion | -1.00 | -3.85 | **-2.86 EUR** |
| puesto en el ranking | -1.47 | -5.07 | **-3.60 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
