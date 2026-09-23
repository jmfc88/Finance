# Simulacion en paralelo

Actualizado: 2026-09-23 05:56 · dia 31 de ejecucion
**Revision nº2 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **81**
- Operaciones abiertas: 59

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 1 | 1% | +16.67 EUR |
| beneficio | 1 | 1% | +5.55 EUR |
| flojo | 23 | 28% | +1.11 EUR |
| plano | 4 | 5% | -1.70 EUR |
| perdida | 28 | 35% | -7.09 EUR |
| nefasta | 24 | 30% | -5.81 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 20 | -2.31% | 0/20 (0%) | 4/20 | 8 |
| 11-20 | 27 | -2.07% | 2/27 (7%) | 3/27 | 8 |
| 21-30 | 34 | -5.74% | 0/34 (0%) | 0/34 | 7 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 10 operaciones, media -2.31%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -44.08 EUR | -2.32% | 1/19 | -10.00 EUR |
| arranca despues (+8%) | -48.55 EUR | -3.24% | 2/15 | -10.00 EUR |
| actual (8% / +5% / 5%) | -48.55 EUR | -3.24% | 2/15 | -10.00 EUR |
| trailing suelto (7%) | -51.00 EUR | -3.40% | 2/15 | -10.00 EUR |
| sin trailing, solo stop | -63.06 EUR | -4.50% | 1/14 | -10.00 EUR |
| arranca antes (+3%) | -65.08 EUR | -3.43% | 2/19 | -10.00 EUR |
| LA REAL (escalera 25/08) | -297.05 EUR | -3.67% | 2/81 | -8.08 EUR |
| stop corto (5%) | -319.79 EUR | -5.81% | 2/55 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.67%**
- Aciertos (>= 5 EUR limpios): 2/81 (2%)
- Resultado acumulado ficticio: -297.05 EUR sobre 81 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 27 | -5.05 EUR | 0% | 67% |
| nota global | medio | 27 | -3.78 EUR | 4% | 78% |
| nota global | alto | 27 | -2.17 EUR | 4% | 48% |
| puesto en el ranking | bajo | 27 | -1.92 EUR | 4% | 44% |
| puesto en el ranking | medio | 27 | -3.61 EUR | 4% | 70% |
| puesto en el ranking | alto | 27 | -5.46 EUR | 0% | 78% |
| potencial hasta objetivo | bajo | 27 | -4.23 EUR | 4% | 67% |
| potencial hasta objetivo | medio | 27 | -4.08 EUR | 0% | 70% |
| potencial hasta objetivo | alto | 27 | -2.70 EUR | 4% | 56% |
| dispersion | bajo | 27 | -1.48 EUR | 4% | 41% |
| dispersion | medio | 27 | -5.53 EUR | 0% | 81% |
| dispersion | alto | 27 | -3.99 EUR | 4% | 70% |
| % compra fuerte | bajo | 25 | -4.78 EUR | 4% | 72% |
| % compra fuerte | medio | 25 | -3.48 EUR | 0% | 72% |
| % compra fuerte | alto | 26 | -3.92 EUR | 0% | 58% |
| momentum 30d | bajo | 27 | -4.04 EUR | 0% | 63% |
| momentum 30d | medio | 27 | -3.71 EUR | 4% | 63% |
| momentum 30d | alto | 27 | -3.25 EUR | 4% | 67% |
| fuerza relativa | bajo | 27 | -4.08 EUR | 0% | 67% |
| fuerza relativa | medio | 27 | -3.96 EUR | 0% | 63% |
| fuerza relativa | alto | 27 | -2.96 EUR | 7% | 63% |
| RSI | bajo | 27 | -3.27 EUR | 4% | 59% |
| RSI | medio | 27 | -3.68 EUR | 0% | 67% |
| RSI | alto | 27 | -4.05 EUR | 4% | 67% |
| volumen relativo | bajo | 21 | -2.85 EUR | 5% | 57% |
| volumen relativo | medio | 21 | -4.15 EUR | 0% | 67% |
| volumen relativo | alto | 22 | -4.45 EUR | 0% | 59% |
| volatilidad | bajo | 21 | -4.22 EUR | 0% | 62% |
| volatilidad | medio | 21 | -5.34 EUR | 0% | 76% |
| volatilidad | alto | 22 | -2.00 EUR | 5% | 45% |
| liquidez | bajo | 21 | -3.12 EUR | 5% | 57% |
| liquidez | medio | 21 | -4.60 EUR | 0% | 71% |
| liquidez | alto | 22 | -3.76 EUR | 0% | 55% |
| distancia max 52s | bajo | 21 | -3.01 EUR | 5% | 52% |
| distancia max 52s | medio | 21 | -3.52 EUR | 0% | 62% |
| distancia max 52s | alto | 22 | -4.90 EUR | 0% | 68% |
| consenso | buy | 57 | -4.77 EUR | 2% | 74% |
| consenso | strong_buy | 24 | -1.04 EUR | 4% | 42% |
| tendencia tecnica | alcista | 53 | -3.39 EUR | 4% | 62% |
| tendencia tecnica | mixta | 17 | -3.81 EUR | 0% | 65% |
| tendencia tecnica | bajista | 11 | -4.78 EUR | 0% | 73% |
| tendencia analistas | mejorando | 43 | -3.78 EUR | 2% | 65% |
| tendencia analistas | estable | 28 | -5.07 EUR | 0% | 75% |
| regimen de mercado | favorable | 66 | -3.49 EUR | 3% | 65% |
| regimen de mercado | neutro | 15 | -4.45 EUR | 0% | 60% |
| catalizador | sin catalizador | 80 | -3.61 EUR | 2% | 64% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.05 | -2.17 | **+2.88 EUR** |
| volatilidad | -4.22 | -2.00 | **+2.22 EUR** |
| potencial hasta objetivo | -4.23 | -2.70 | **+1.53 EUR** |
| fuerza relativa | -4.08 | -2.96 | **+1.12 EUR** |
| % compra fuerte | -4.78 | -3.92 | **+0.86 EUR** |
| momentum 30d | -4.04 | -3.25 | **+0.79 EUR** |
| liquidez | -3.12 | -3.76 | **-0.63 EUR** |
| RSI | -3.27 | -4.05 | **-0.78 EUR** |
| volumen relativo | -2.85 | -4.45 | **-1.60 EUR** |
| distancia max 52s | -3.01 | -4.90 | **-1.89 EUR** |
| dispersion | -1.48 | -3.99 | **-2.52 EUR** |
| puesto en el ranking | -1.92 | -5.46 | **-3.54 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
