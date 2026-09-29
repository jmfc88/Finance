# Simulacion en paralelo

Actualizado: 2026-09-29 12:46 · dia 37 de ejecucion
Proxima revision de ponderacion en 8 dias.

- Operaciones cerradas: **118**
- Operaciones abiertas: 48

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 2% | +16.67 EUR |
| beneficio | 2 | 2% | +7.32 EUR |
| flojo | 38 | 32% | +1.27 EUR |
| plano | 7 | 6% | -1.83 EUR |
| perdida | 42 | 36% | -7.17 EUR |
| nefasta | 27 | 23% | -6.06 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 31 | -1.85% | 1/31 (3%) | 7/31 | 10 |
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
| trailing pegado (3%) | -71.56 EUR | -2.17% | 2/33 | -10.00 EUR |
| arranca despues (+8%) | -86.37 EUR | -3.32% | 3/26 | -10.00 EUR |
| actual (8% / +5% / 5%) | -86.37 EUR | -3.32% | 3/26 | -10.00 EUR |
| arranca antes (+3%) | -96.67 EUR | -3.22% | 3/30 | -10.00 EUR |
| trailing suelto (7%) | -106.13 EUR | -4.25% | 2/25 | -10.00 EUR |
| sin trailing, solo stop | -118.19 EUR | -4.92% | 1/24 | -10.00 EUR |
| LA REAL (escalera 25/08) | -381.46 EUR | -3.23% | 4/118 | -8.08 EUR |
| stop corto (5%) | -430.92 EUR | -5.60% | 3/77 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.23%**
- Aciertos (>= 5 EUR limpios): 4/118 (3%)
- Resultado acumulado ficticio: -381.46 EUR sobre 118 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 39 | -4.27 EUR | 3% | 62% |
| nota global | medio | 39 | -3.78 EUR | 3% | 67% |
| nota global | alto | 40 | -1.69 EUR | 5% | 48% |
| puesto en el ranking | bajo | 39 | -1.59 EUR | 5% | 44% |
| puesto en el ranking | medio | 39 | -3.20 EUR | 5% | 62% |
| puesto en el ranking | alto | 40 | -4.87 EUR | 0% | 70% |
| potencial hasta objetivo | bajo | 39 | -3.86 EUR | 3% | 59% |
| potencial hasta objetivo | medio | 39 | -3.66 EUR | 0% | 64% |
| potencial hasta objetivo | alto | 40 | -2.21 EUR | 8% | 52% |
| dispersion | bajo | 39 | -0.74 EUR | 8% | 38% |
| dispersion | medio | 39 | -5.55 EUR | 0% | 77% |
| dispersion | alto | 40 | -3.40 EUR | 2% | 60% |
| % compra fuerte | bajo | 37 | -4.33 EUR | 3% | 65% |
| % compra fuerte | medio | 37 | -3.28 EUR | 3% | 65% |
| % compra fuerte | alto | 38 | -3.02 EUR | 3% | 53% |
| momentum 30d | bajo | 39 | -2.91 EUR | 5% | 54% |
| momentum 30d | medio | 39 | -3.42 EUR | 3% | 59% |
| momentum 30d | alto | 40 | -3.37 EUR | 2% | 62% |
| fuerza relativa | bajo | 39 | -3.06 EUR | 5% | 59% |
| fuerza relativa | medio | 39 | -3.66 EUR | 0% | 56% |
| fuerza relativa | alto | 40 | -2.99 EUR | 5% | 60% |
| RSI | bajo | 39 | -2.93 EUR | 8% | 59% |
| RSI | medio | 39 | -2.85 EUR | 0% | 54% |
| RSI | alto | 40 | -3.91 EUR | 2% | 62% |
| volumen relativo | bajo | 33 | -3.22 EUR | 6% | 61% |
| volumen relativo | medio | 33 | -2.95 EUR | 0% | 48% |
| volumen relativo | alto | 35 | -3.59 EUR | 3% | 57% |
| volatilidad | bajo | 33 | -3.82 EUR | 0% | 55% |
| volatilidad | medio | 33 | -4.44 EUR | 0% | 67% |
| volatilidad | alto | 35 | -1.62 EUR | 9% | 46% |
| liquidez | bajo | 33 | -2.45 EUR | 3% | 48% |
| liquidez | medio | 33 | -3.81 EUR | 3% | 64% |
| liquidez | alto | 35 | -3.50 EUR | 3% | 54% |
| distancia max 52s | bajo | 33 | -2.19 EUR | 9% | 52% |
| distancia max 52s | medio | 33 | -4.00 EUR | 0% | 64% |
| distancia max 52s | alto | 35 | -3.56 EUR | 0% | 51% |
| consenso | buy | 84 | -4.29 EUR | 2% | 67% |
| consenso | strong_buy | 34 | -0.63 EUR | 6% | 38% |
| tendencia tecnica | alcista | 70 | -3.25 EUR | 3% | 57% |
| tendencia tecnica | mixta | 31 | -2.79 EUR | 3% | 55% |
| tendencia tecnica | bajista | 17 | -3.95 EUR | 6% | 71% |
| tendencia analistas | mejorando | 62 | -3.41 EUR | 3% | 60% |
| tendencia analistas | estable | 40 | -4.36 EUR | 2% | 70% |
| tendencia analistas | empeorando | 5 | -2.63 EUR | 0% | 60% |
| regimen de mercado | favorable | 86 | -3.36 EUR | 3% | 62% |
| regimen de mercado | neutro | 32 | -2.89 EUR | 3% | 50% |
| catalizador | sin catalizador | 117 | -3.19 EUR | 3% | 58% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.27 | -1.69 | **+2.58 EUR** |
| volatilidad | -3.82 | -1.62 | **+2.20 EUR** |
| potencial hasta objetivo | -3.86 | -2.21 | **+1.65 EUR** |
| % compra fuerte | -4.33 | -3.02 | **+1.30 EUR** |
| fuerza relativa | -3.06 | -2.99 | **+0.07 EUR** |
| volumen relativo | -3.22 | -3.59 | **-0.37 EUR** |
| momentum 30d | -2.91 | -3.37 | **-0.46 EUR** |
| RSI | -2.93 | -3.91 | **-0.98 EUR** |
| liquidez | -2.45 | -3.50 | **-1.06 EUR** |
| distancia max 52s | -2.19 | -3.56 | **-1.37 EUR** |
| dispersion | -0.74 | -3.40 | **-2.67 EUR** |
| puesto en el ranking | -1.59 | -4.87 | **-3.28 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
