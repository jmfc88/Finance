# Simulacion en paralelo

Actualizado: 2026-09-22 23:37 · dia 30 de ejecucion
**Revision nº2 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **80**
- Operaciones abiertas: 60

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 1 | 1% | +5.55 EUR |
| flojo | 23 | 29% | +1.11 EUR |
| plano | 4 | 5% | -1.70 EUR |
| perdida | 28 | 35% | -7.09 EUR |
| nefasta | 24 | 30% | -5.81 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 20 | -2.31% | 0/20 (0%) | 4/20 | 8 |
| 11-20 | 26 | -2.79% | 1/26 (4%) | 2/26 | 8 |
| 21-30 | 34 | -5.74% | 0/34 (0%) | 0/34 | 7 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 10 operaciones, media -2.31%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -61.04 EUR | -3.39% | 0/18 | -10.00 EUR |
| trailing suelto (7%) | -63.06 EUR | -4.50% | 1/14 | -10.00 EUR |
| sin trailing, solo stop | -63.06 EUR | -4.50% | 1/14 | -10.00 EUR |
| arranca despues (+8%) | -63.06 EUR | -4.50% | 1/14 | -10.00 EUR |
| actual (8% / +5% / 5%) | -63.06 EUR | -4.50% | 1/14 | -10.00 EUR |
| arranca antes (+3%) | -79.59 EUR | -4.42% | 1/18 | -10.00 EUR |
| LA REAL (escalera 25/08) | -313.72 EUR | -3.92% | 1/80 | -8.08 EUR |
| stop corto (5%) | -334.30 EUR | -6.19% | 1/54 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.92%**
- Aciertos (>= 5 EUR limpios): 1/80 (1%)
- Resultado acumulado ficticio: -313.72 EUR sobre 80 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 26 | -4.94 EUR | 0% | 65% |
| nota global | medio | 26 | -4.91 EUR | 0% | 81% |
| nota global | alto | 28 | -2.06 EUR | 4% | 50% |
| puesto en el ranking | bajo | 26 | -1.95 EUR | 4% | 46% |
| puesto en el ranking | medio | 26 | -4.13 EUR | 0% | 69% |
| puesto en el ranking | alto | 28 | -5.56 EUR | 0% | 79% |
| potencial hasta objetivo | bajo | 26 | -4.08 EUR | 4% | 65% |
| potencial hasta objetivo | medio | 26 | -3.92 EUR | 0% | 69% |
| potencial hasta objetivo | alto | 28 | -3.77 EUR | 0% | 61% |
| dispersion | bajo | 26 | -2.18 EUR | 0% | 42% |
| dispersion | medio | 26 | -5.88 EUR | 0% | 85% |
| dispersion | alto | 28 | -3.73 EUR | 4% | 68% |
| % compra fuerte | bajo | 25 | -4.78 EUR | 4% | 72% |
| % compra fuerte | medio | 25 | -3.48 EUR | 0% | 72% |
| % compra fuerte | alto | 26 | -3.92 EUR | 0% | 58% |
| momentum 30d | bajo | 26 | -3.89 EUR | 0% | 62% |
| momentum 30d | medio | 26 | -4.94 EUR | 0% | 69% |
| momentum 30d | alto | 28 | -3.01 EUR | 4% | 64% |
| fuerza relativa | bajo | 26 | -3.93 EUR | 0% | 65% |
| fuerza relativa | medio | 26 | -3.88 EUR | 0% | 62% |
| fuerza relativa | alto | 28 | -3.96 EUR | 4% | 68% |
| RSI | bajo | 26 | -4.04 EUR | 0% | 62% |
| RSI | medio | 26 | -3.51 EUR | 0% | 65% |
| RSI | alto | 28 | -4.20 EUR | 4% | 68% |
| volumen relativo | bajo | 21 | -4.03 EUR | 0% | 62% |
| volumen relativo | medio | 21 | -3.71 EUR | 0% | 62% |
| volumen relativo | alto | 21 | -4.71 EUR | 0% | 62% |
| volatilidad | bajo | 21 | -4.22 EUR | 0% | 62% |
| volatilidad | medio | 21 | -5.34 EUR | 0% | 76% |
| volatilidad | alto | 21 | -2.89 EUR | 0% | 48% |
| liquidez | bajo | 21 | -3.87 EUR | 0% | 57% |
| liquidez | medio | 21 | -4.60 EUR | 0% | 71% |
| liquidez | alto | 21 | -3.98 EUR | 0% | 57% |
| distancia max 52s | bajo | 21 | -4.19 EUR | 0% | 57% |
| distancia max 52s | medio | 21 | -3.52 EUR | 0% | 62% |
| distancia max 52s | alto | 21 | -4.75 EUR | 0% | 67% |
| consenso | buy | 57 | -4.77 EUR | 2% | 74% |
| consenso | strong_buy | 23 | -1.81 EUR | 0% | 43% |
| tendencia tecnica | alcista | 52 | -3.78 EUR | 2% | 63% |
| tendencia tecnica | mixta | 17 | -3.81 EUR | 0% | 65% |
| tendencia tecnica | bajista | 11 | -4.78 EUR | 0% | 73% |
| tendencia analistas | mejorando | 43 | -3.78 EUR | 2% | 65% |
| tendencia analistas | estable | 28 | -5.07 EUR | 0% | 75% |
| regimen de mercado | favorable | 65 | -3.80 EUR | 2% | 66% |
| regimen de mercado | neutro | 15 | -4.45 EUR | 0% | 60% |
| catalizador | sin catalizador | 79 | -3.87 EUR | 1% | 65% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.94 | -2.06 | **+2.88 EUR** |
| volatilidad | -4.22 | -2.89 | **+1.33 EUR** |
| momentum 30d | -3.89 | -3.01 | **+0.88 EUR** |
| % compra fuerte | -4.78 | -3.92 | **+0.86 EUR** |
| potencial hasta objetivo | -4.08 | -3.77 | **+0.31 EUR** |
| fuerza relativa | -3.93 | -3.96 | **-0.03 EUR** |
| liquidez | -3.87 | -3.98 | **-0.11 EUR** |
| RSI | -4.04 | -4.20 | **-0.16 EUR** |
| distancia max 52s | -4.19 | -4.75 | **-0.56 EUR** |
| volumen relativo | -4.03 | -4.71 | **-0.68 EUR** |
| dispersion | -2.18 | -3.73 | **-1.55 EUR** |
| puesto en el ranking | -1.95 | -5.56 | **-3.61 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
