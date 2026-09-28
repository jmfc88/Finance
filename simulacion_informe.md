# Simulacion en paralelo

Actualizado: 2026-09-28 06:48 · dia 36 de ejecucion
Proxima revision de ponderacion en 9 dias.

- Operaciones cerradas: **104**
- Operaciones abiertas: 58

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 1 | 1% | +16.67 EUR |
| beneficio | 2 | 2% | +7.32 EUR |
| flojo | 35 | 34% | +1.22 EUR |
| plano | 5 | 5% | -1.87 EUR |
| perdida | 35 | 34% | -7.16 EUR |
| nefasta | 26 | 25% | -5.98 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 25 | -1.91% | 0/25 (0%) | 5/25 | 8 |
| 11-20 | 28 | -1.96% | 2/28 (7%) | 3/28 | 8 |
| 21-30 | 51 | -4.69% | 1/51 (2%) | 2/51 | 9 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 12 operaciones, media -2.44%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -62.74 EUR | -2.51% | 1/25 | -10.00 EUR |
| arranca despues (+8%) | -72.14 EUR | -3.80% | 2/19 | -10.00 EUR |
| actual (8% / +5% / 5%) | -72.14 EUR | -3.80% | 2/19 | -10.00 EUR |
| trailing suelto (7%) | -74.59 EUR | -3.93% | 2/19 | -10.00 EUR |
| sin trailing, solo stop | -86.65 EUR | -4.81% | 1/18 | -10.00 EUR |
| arranca antes (+3%) | -88.67 EUR | -3.86% | 2/23 | -10.00 EUR |
| LA REAL (escalera 25/08) | -341.72 EUR | -3.29% | 3/104 | -8.08 EUR |
| stop corto (5%) | -392.34 EUR | -5.94% | 2/66 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.29%**
- Aciertos (>= 5 EUR limpios): 3/104 (3%)
- Resultado acumulado ficticio: -341.72 EUR sobre 104 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 34 | -4.67 EUR | 0% | 65% |
| nota global | medio | 34 | -3.19 EUR | 6% | 65% |
| nota global | alto | 36 | -2.07 EUR | 3% | 47% |
| puesto en el ranking | bajo | 34 | -1.78 EUR | 3% | 41% |
| puesto en el ranking | medio | 34 | -3.13 EUR | 6% | 65% |
| puesto en el ranking | alto | 36 | -4.86 EUR | 0% | 69% |
| potencial hasta objetivo | bajo | 34 | -4.06 EUR | 3% | 62% |
| potencial hasta objetivo | medio | 34 | -3.36 EUR | 0% | 62% |
| potencial hasta objetivo | alto | 36 | -2.49 EUR | 6% | 53% |
| dispersion | bajo | 34 | -1.06 EUR | 6% | 38% |
| dispersion | medio | 34 | -5.22 EUR | 0% | 74% |
| dispersion | alto | 36 | -3.56 EUR | 3% | 64% |
| % compra fuerte | bajo | 33 | -4.27 EUR | 3% | 67% |
| % compra fuerte | medio | 33 | -2.98 EUR | 3% | 64% |
| % compra fuerte | alto | 33 | -3.46 EUR | 0% | 52% |
| momentum 30d | bajo | 34 | -3.15 EUR | 3% | 53% |
| momentum 30d | medio | 34 | -3.35 EUR | 3% | 59% |
| momentum 30d | alto | 36 | -3.35 EUR | 3% | 64% |
| fuerza relativa | bajo | 34 | -3.06 EUR | 3% | 56% |
| fuerza relativa | medio | 34 | -3.90 EUR | 0% | 59% |
| fuerza relativa | alto | 36 | -2.92 EUR | 6% | 61% |
| RSI | bajo | 34 | -3.01 EUR | 6% | 56% |
| RSI | medio | 34 | -2.61 EUR | 0% | 53% |
| RSI | alto | 36 | -4.18 EUR | 3% | 67% |
| volumen relativo | bajo | 29 | -2.76 EUR | 7% | 59% |
| volumen relativo | medio | 29 | -3.21 EUR | 0% | 52% |
| volumen relativo | alto | 29 | -4.01 EUR | 0% | 55% |
| volatilidad | bajo | 29 | -3.88 EUR | 0% | 59% |
| volatilidad | medio | 29 | -4.25 EUR | 0% | 62% |
| volatilidad | alto | 29 | -1.85 EUR | 7% | 45% |
| liquidez | bajo | 29 | -3.85 EUR | 0% | 59% |
| liquidez | medio | 29 | -2.83 EUR | 3% | 59% |
| liquidez | alto | 29 | -3.30 EUR | 3% | 48% |
| distancia max 52s | bajo | 29 | -2.24 EUR | 7% | 48% |
| distancia max 52s | medio | 29 | -3.52 EUR | 0% | 59% |
| distancia max 52s | alto | 29 | -4.22 EUR | 0% | 59% |
| consenso | buy | 73 | -4.22 EUR | 3% | 67% |
| consenso | strong_buy | 31 | -1.08 EUR | 3% | 39% |
| tendencia tecnica | alcista | 64 | -3.40 EUR | 3% | 59% |
| tendencia tecnica | mixta | 27 | -2.38 EUR | 4% | 52% |
| tendencia tecnica | bajista | 13 | -4.59 EUR | 0% | 69% |
| tendencia analistas | mejorando | 53 | -3.02 EUR | 4% | 57% |
| tendencia analistas | estable | 37 | -4.98 EUR | 0% | 73% |
| tendencia analistas | empeorando | 5 | -2.63 EUR | 0% | 60% |
| regimen de mercado | favorable | 79 | -3.18 EUR | 4% | 61% |
| regimen de mercado | neutro | 25 | -3.62 EUR | 0% | 52% |
| catalizador | sin catalizador | 103 | -3.24 EUR | 3% | 58% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.67 | -2.07 | **+2.60 EUR** |
| volatilidad | -3.88 | -1.85 | **+2.03 EUR** |
| potencial hasta objetivo | -4.06 | -2.49 | **+1.57 EUR** |
| % compra fuerte | -4.27 | -3.46 | **+0.81 EUR** |
| liquidez | -3.85 | -3.30 | **+0.55 EUR** |
| fuerza relativa | -3.06 | -2.92 | **+0.13 EUR** |
| momentum 30d | -3.15 | -3.35 | **-0.20 EUR** |
| RSI | -3.01 | -4.18 | **-1.17 EUR** |
| volumen relativo | -2.76 | -4.01 | **-1.24 EUR** |
| distancia max 52s | -2.24 | -4.22 | **-1.99 EUR** |
| dispersion | -1.06 | -3.56 | **-2.50 EUR** |
| puesto en el ranking | -1.78 | -4.86 | **-3.08 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
