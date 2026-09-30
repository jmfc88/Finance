# Simulacion en paralelo

Actualizado: 2026-09-30 12:29 · dia 38 de ejecucion
Proxima revision de ponderacion en 7 dias.

- Operaciones cerradas: **127**
- Operaciones abiertas: 50

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 2% | +16.67 EUR |
| beneficio | 2 | 2% | +7.32 EUR |
| flojo | 39 | 31% | +1.26 EUR |
| plano | 10 | 8% | -1.72 EUR |
| perdida | 46 | 36% | -7.07 EUR |
| nefasta | 28 | 22% | -6.13 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 33 | -2.09% | 1/33 (3%) | 7/33 | 10 |
| 11-20 | 35 | -2.18% | 2/35 (6%) | 3/35 | 9 |
| 21-30 | 59 | -4.60% | 1/59 (2%) | 2/59 | 10 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 23 operaciones, media -3.09%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -101.78 EUR | -2.54% | 2/40 | -10.00 EUR |
| arranca despues (+8%) | -116.59 EUR | -3.53% | 3/33 | -10.00 EUR |
| actual (8% / +5% / 5%) | -116.59 EUR | -3.53% | 3/33 | -10.00 EUR |
| arranca antes (+3%) | -130.59 EUR | -3.44% | 3/38 | -10.00 EUR |
| trailing suelto (7%) | -136.35 EUR | -4.26% | 2/32 | -10.00 EUR |
| sin trailing, solo stop | -148.41 EUR | -4.79% | 1/31 | -10.00 EUR |
| LA REAL (escalera 25/08) | -416.84 EUR | -3.28% | 4/127 | -8.08 EUR |
| stop corto (5%) | -468.53 EUR | -5.51% | 3/85 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.28%**
- Aciertos (>= 5 EUR limpios): 4/127 (3%)
- Resultado acumulado ficticio: -416.84 EUR sobre 127 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 42 | -4.38 EUR | 0% | 60% |
| nota global | medio | 42 | -3.46 EUR | 5% | 64% |
| nota global | alto | 43 | -2.03 EUR | 5% | 51% |
| puesto en el ranking | bajo | 42 | -1.95 EUR | 5% | 48% |
| puesto en el ranking | medio | 42 | -3.38 EUR | 5% | 62% |
| puesto en el ranking | alto | 43 | -4.49 EUR | 0% | 65% |
| potencial hasta objetivo | bajo | 42 | -3.72 EUR | 2% | 55% |
| potencial hasta objetivo | medio | 42 | -3.56 EUR | 0% | 64% |
| potencial hasta objetivo | alto | 43 | -2.59 EUR | 7% | 56% |
| dispersion | bajo | 42 | -0.67 EUR | 7% | 36% |
| dispersion | medio | 42 | -5.58 EUR | 0% | 79% |
| dispersion | alto | 43 | -3.59 EUR | 2% | 60% |
| % compra fuerte | bajo | 40 | -4.61 EUR | 2% | 68% |
| % compra fuerte | medio | 40 | -3.11 EUR | 2% | 62% |
| % compra fuerte | alto | 41 | -3.00 EUR | 2% | 51% |
| momentum 30d | bajo | 42 | -3.02 EUR | 5% | 55% |
| momentum 30d | medio | 42 | -3.48 EUR | 2% | 60% |
| momentum 30d | alto | 43 | -3.35 EUR | 2% | 60% |
| fuerza relativa | bajo | 42 | -3.24 EUR | 5% | 62% |
| fuerza relativa | medio | 42 | -3.76 EUR | 0% | 57% |
| fuerza relativa | alto | 43 | -2.86 EUR | 5% | 56% |
| RSI | bajo | 42 | -2.65 EUR | 7% | 55% |
| RSI | medio | 42 | -3.22 EUR | 0% | 57% |
| RSI | alto | 43 | -3.96 EUR | 2% | 63% |
| volumen relativo | bajo | 36 | -3.55 EUR | 6% | 64% |
| volumen relativo | medio | 36 | -3.13 EUR | 0% | 50% |
| volumen relativo | alto | 38 | -3.27 EUR | 3% | 53% |
| volatilidad | bajo | 36 | -3.51 EUR | 0% | 50% |
| volatilidad | medio | 36 | -4.50 EUR | 0% | 67% |
| volatilidad | alto | 38 | -2.00 EUR | 8% | 50% |
| liquidez | bajo | 36 | -2.72 EUR | 3% | 50% |
| liquidez | medio | 36 | -3.97 EUR | 3% | 64% |
| liquidez | alto | 38 | -3.26 EUR | 3% | 53% |
| distancia max 52s | bajo | 36 | -2.68 EUR | 8% | 56% |
| distancia max 52s | medio | 36 | -3.48 EUR | 0% | 58% |
| distancia max 52s | alto | 38 | -3.76 EUR | 0% | 53% |
| consenso | buy | 90 | -4.17 EUR | 2% | 64% |
| consenso | strong_buy | 37 | -1.12 EUR | 5% | 43% |
| tendencia tecnica | alcista | 75 | -3.19 EUR | 3% | 55% |
| tendencia tecnica | mixta | 33 | -2.90 EUR | 3% | 58% |
| tendencia tecnica | bajista | 19 | -4.32 EUR | 5% | 74% |
| tendencia analistas | mejorando | 64 | -3.49 EUR | 3% | 61% |
| tendencia analistas | estable | 40 | -4.36 EUR | 2% | 70% |
| tendencia analistas | empeorando | 5 | -2.63 EUR | 0% | 60% |
| regimen de mercado | favorable | 88 | -3.36 EUR | 3% | 61% |
| regimen de mercado | neutro | 39 | -3.10 EUR | 3% | 51% |
| catalizador | sin catalizador | 126 | -3.24 EUR | 3% | 58% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.38 | -2.03 | **+2.35 EUR** |
| % compra fuerte | -4.61 | -3.00 | **+1.61 EUR** |
| volatilidad | -3.51 | -2.00 | **+1.51 EUR** |
| potencial hasta objetivo | -3.72 | -2.59 | **+1.13 EUR** |
| fuerza relativa | -3.24 | -2.86 | **+0.38 EUR** |
| volumen relativo | -3.55 | -3.27 | **+0.28 EUR** |
| momentum 30d | -3.02 | -3.35 | **-0.33 EUR** |
| liquidez | -2.72 | -3.26 | **-0.54 EUR** |
| distancia max 52s | -2.68 | -3.76 | **-1.07 EUR** |
| RSI | -2.65 | -3.96 | **-1.31 EUR** |
| puesto en el ranking | -1.95 | -4.49 | **-2.55 EUR** |
| dispersion | -0.67 | -3.59 | **-2.93 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
