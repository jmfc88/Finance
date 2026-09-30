# Simulacion en paralelo

Actualizado: 2026-09-30 06:40 · dia 38 de ejecucion
Proxima revision de ponderacion en 7 dias.

- Operaciones cerradas: **119**
- Operaciones abiertas: 57

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 2% | +16.67 EUR |
| beneficio | 2 | 2% | +7.32 EUR |
| flojo | 38 | 32% | +1.27 EUR |
| plano | 7 | 6% | -1.83 EUR |
| perdida | 42 | 35% | -7.17 EUR |
| nefasta | 28 | 24% | -6.13 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 32 | -2.04% | 1/32 (3%) | 7/32 | 9 |
| 11-20 | 33 | -2.04% | 2/33 (6%) | 3/33 | 8 |
| 21-30 | 54 | -4.76% | 1/54 (2%) | 2/54 | 9 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 17 operaciones, media -2.99%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -81.56 EUR | -2.40% | 2/34 | -10.00 EUR |
| arranca despues (+8%) | -96.37 EUR | -3.57% | 3/27 | -10.00 EUR |
| actual (8% / +5% / 5%) | -96.37 EUR | -3.57% | 3/27 | -10.00 EUR |
| arranca antes (+3%) | -106.67 EUR | -3.44% | 3/31 | -10.00 EUR |
| trailing suelto (7%) | -116.13 EUR | -4.47% | 2/26 | -10.00 EUR |
| sin trailing, solo stop | -128.19 EUR | -5.13% | 1/25 | -10.00 EUR |
| LA REAL (escalera 25/08) | -389.54 EUR | -3.27% | 4/119 | -8.08 EUR |
| stop corto (5%) | -437.92 EUR | -5.61% | 3/78 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.27%**
- Aciertos (>= 5 EUR limpios): 4/119 (3%)
- Resultado acumulado ficticio: -389.54 EUR sobre 119 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 39 | -4.27 EUR | 3% | 62% |
| nota global | medio | 39 | -3.78 EUR | 3% | 67% |
| nota global | alto | 41 | -1.85 EUR | 5% | 49% |
| puesto en el ranking | bajo | 39 | -1.76 EUR | 5% | 46% |
| puesto en el ranking | medio | 39 | -3.03 EUR | 5% | 59% |
| puesto en el ranking | alto | 41 | -4.95 EUR | 0% | 71% |
| potencial hasta objetivo | bajo | 39 | -3.86 EUR | 3% | 59% |
| potencial hasta objetivo | medio | 39 | -3.66 EUR | 0% | 64% |
| potencial hasta objetivo | alto | 41 | -2.35 EUR | 7% | 54% |
| dispersion | bajo | 39 | -0.74 EUR | 8% | 38% |
| dispersion | medio | 39 | -5.55 EUR | 0% | 77% |
| dispersion | alto | 41 | -3.52 EUR | 2% | 61% |
| % compra fuerte | bajo | 37 | -4.33 EUR | 3% | 65% |
| % compra fuerte | medio | 37 | -3.28 EUR | 3% | 65% |
| % compra fuerte | alto | 39 | -3.15 EUR | 3% | 54% |
| momentum 30d | bajo | 39 | -3.14 EUR | 5% | 56% |
| momentum 30d | medio | 39 | -3.42 EUR | 3% | 59% |
| momentum 30d | alto | 41 | -3.26 EUR | 2% | 61% |
| fuerza relativa | bajo | 39 | -3.06 EUR | 5% | 59% |
| fuerza relativa | medio | 39 | -3.89 EUR | 0% | 59% |
| fuerza relativa | alto | 41 | -2.89 EUR | 5% | 59% |
| RSI | bajo | 39 | -2.93 EUR | 8% | 59% |
| RSI | medio | 39 | -2.85 EUR | 0% | 54% |
| RSI | alto | 41 | -4.01 EUR | 2% | 63% |
| volumen relativo | bajo | 34 | -3.36 EUR | 6% | 62% |
| volumen relativo | medio | 34 | -3.10 EUR | 0% | 50% |
| volumen relativo | alto | 34 | -3.46 EUR | 3% | 56% |
| volatilidad | bajo | 34 | -3.94 EUR | 0% | 56% |
| volatilidad | medio | 34 | -4.28 EUR | 0% | 65% |
| volatilidad | alto | 34 | -1.70 EUR | 9% | 47% |
| liquidez | bajo | 34 | -2.61 EUR | 3% | 50% |
| liquidez | medio | 34 | -3.94 EUR | 3% | 65% |
| liquidez | alto | 34 | -3.37 EUR | 3% | 53% |
| distancia max 52s | bajo | 34 | -2.37 EUR | 9% | 53% |
| distancia max 52s | medio | 34 | -3.86 EUR | 0% | 62% |
| distancia max 52s | alto | 34 | -3.70 EUR | 0% | 53% |
| consenso | buy | 84 | -4.29 EUR | 2% | 67% |
| consenso | strong_buy | 35 | -0.85 EUR | 6% | 40% |
| tendencia tecnica | alcista | 70 | -3.25 EUR | 3% | 57% |
| tendencia tecnica | mixta | 31 | -2.79 EUR | 3% | 55% |
| tendencia tecnica | bajista | 18 | -4.18 EUR | 6% | 72% |
| tendencia analistas | mejorando | 63 | -3.48 EUR | 3% | 60% |
| tendencia analistas | estable | 40 | -4.36 EUR | 2% | 70% |
| tendencia analistas | empeorando | 5 | -2.63 EUR | 0% | 60% |
| regimen de mercado | favorable | 86 | -3.36 EUR | 3% | 62% |
| regimen de mercado | neutro | 33 | -3.05 EUR | 3% | 52% |
| catalizador | sin catalizador | 118 | -3.23 EUR | 3% | 58% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.27 | -1.85 | **+2.42 EUR** |
| volatilidad | -3.94 | -1.70 | **+2.25 EUR** |
| potencial hasta objetivo | -3.86 | -2.35 | **+1.50 EUR** |
| % compra fuerte | -4.33 | -3.15 | **+1.17 EUR** |
| fuerza relativa | -3.06 | -2.89 | **+0.17 EUR** |
| volumen relativo | -3.36 | -3.46 | **-0.09 EUR** |
| momentum 30d | -3.14 | -3.26 | **-0.12 EUR** |
| liquidez | -2.61 | -3.37 | **-0.76 EUR** |
| RSI | -2.93 | -4.01 | **-1.08 EUR** |
| distancia max 52s | -2.37 | -3.70 | **-1.33 EUR** |
| dispersion | -0.74 | -3.52 | **-2.78 EUR** |
| puesto en el ranking | -1.76 | -4.95 | **-3.18 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
