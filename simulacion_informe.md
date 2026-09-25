# Simulacion en paralelo

Actualizado: 2026-09-25 11:46 · dia 33 de ejecucion
Proxima revision de ponderacion en 12 dias.

- Operaciones cerradas: **101**
- Operaciones abiertas: 56

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 1 | 1% | +16.67 EUR |
| beneficio | 2 | 2% | +7.32 EUR |
| flojo | 34 | 34% | +1.22 EUR |
| plano | 5 | 5% | -1.87 EUR |
| perdida | 34 | 34% | -7.14 EUR |
| nefasta | 25 | 25% | -5.90 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 25 | -1.91% | 0/25 (0%) | 5/25 | 8 |
| 11-20 | 28 | -1.96% | 2/28 (7%) | 3/28 | 8 |
| 21-30 | 48 | -4.67% | 1/48 (2%) | 2/48 | 9 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 12 operaciones, media -2.44%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -52.74 EUR | -2.20% | 1/24 | -10.00 EUR |
| arranca despues (+8%) | -62.14 EUR | -3.45% | 2/18 | -10.00 EUR |
| actual (8% / +5% / 5%) | -62.14 EUR | -3.45% | 2/18 | -10.00 EUR |
| trailing suelto (7%) | -64.59 EUR | -3.59% | 2/18 | -10.00 EUR |
| sin trailing, solo stop | -76.65 EUR | -4.51% | 1/17 | -10.00 EUR |
| arranca antes (+3%) | -78.67 EUR | -3.58% | 2/22 | -10.00 EUR |
| LA REAL (escalera 25/08) | -326.56 EUR | -3.23% | 3/101 | -8.08 EUR |
| stop corto (5%) | -378.34 EUR | -5.91% | 2/64 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.23%**
- Aciertos (>= 5 EUR limpios): 3/101 (3%)
- Resultado acumulado ficticio: -326.56 EUR sobre 101 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 33 | -4.05 EUR | 3% | 61% |
| nota global | medio | 33 | -3.84 EUR | 3% | 70% |
| nota global | alto | 35 | -1.89 EUR | 3% | 46% |
| puesto en el ranking | bajo | 33 | -1.59 EUR | 3% | 39% |
| puesto en el ranking | medio | 33 | -3.08 EUR | 6% | 64% |
| puesto en el ranking | alto | 35 | -4.93 EUR | 0% | 71% |
| potencial hasta objetivo | bajo | 33 | -3.94 EUR | 3% | 61% |
| potencial hasta objetivo | medio | 33 | -3.22 EUR | 0% | 61% |
| potencial hasta objetivo | alto | 35 | -2.59 EUR | 6% | 54% |
| dispersion | bajo | 33 | -1.12 EUR | 6% | 39% |
| dispersion | medio | 33 | -5.14 EUR | 0% | 73% |
| dispersion | alto | 35 | -3.43 EUR | 3% | 63% |
| % compra fuerte | bajo | 32 | -4.15 EUR | 3% | 66% |
| % compra fuerte | medio | 32 | -3.10 EUR | 3% | 66% |
| % compra fuerte | alto | 32 | -3.31 EUR | 0% | 50% |
| momentum 30d | bajo | 33 | -3.00 EUR | 3% | 55% |
| momentum 30d | medio | 33 | -3.49 EUR | 3% | 58% |
| momentum 30d | alto | 35 | -3.21 EUR | 3% | 63% |
| fuerza relativa | bajo | 33 | -3.18 EUR | 3% | 58% |
| fuerza relativa | medio | 33 | -3.50 EUR | 0% | 55% |
| fuerza relativa | alto | 35 | -3.04 EUR | 6% | 63% |
| RSI | bajo | 33 | -2.78 EUR | 6% | 55% |
| RSI | medio | 33 | -2.80 EUR | 0% | 55% |
| RSI | alto | 35 | -4.07 EUR | 3% | 66% |
| volumen relativo | bajo | 28 | -2.90 EUR | 7% | 57% |
| volumen relativo | medio | 28 | -3.04 EUR | 0% | 54% |
| volumen relativo | alto | 28 | -3.86 EUR | 0% | 54% |
| volatilidad | bajo | 28 | -3.73 EUR | 0% | 57% |
| volatilidad | medio | 28 | -4.44 EUR | 0% | 64% |
| volatilidad | alto | 28 | -1.63 EUR | 7% | 43% |
| liquidez | bajo | 28 | -3.70 EUR | 0% | 57% |
| liquidez | medio | 28 | -2.64 EUR | 4% | 57% |
| liquidez | alto | 28 | -3.46 EUR | 4% | 50% |
| distancia max 52s | bajo | 28 | -2.35 EUR | 7% | 50% |
| distancia max 52s | medio | 28 | -3.36 EUR | 0% | 57% |
| distancia max 52s | alto | 28 | -4.09 EUR | 0% | 57% |
| consenso | buy | 70 | -4.18 EUR | 3% | 67% |
| consenso | strong_buy | 31 | -1.08 EUR | 3% | 39% |
| tendencia tecnica | alcista | 62 | -3.25 EUR | 3% | 58% |
| tendencia tecnica | mixta | 26 | -2.51 EUR | 4% | 54% |
| tendencia tecnica | bajista | 13 | -4.59 EUR | 0% | 69% |
| tendencia analistas | mejorando | 52 | -3.10 EUR | 4% | 58% |
| tendencia analistas | estable | 35 | -4.80 EUR | 0% | 71% |
| tendencia analistas | empeorando | 5 | -2.63 EUR | 0% | 60% |
| regimen de mercado | favorable | 78 | -3.23 EUR | 4% | 62% |
| regimen de mercado | neutro | 23 | -3.23 EUR | 0% | 48% |
| catalizador | sin catalizador | 100 | -3.18 EUR | 3% | 58% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.05 | -1.89 | **+2.15 EUR** |
| volatilidad | -3.73 | -1.63 | **+2.10 EUR** |
| potencial hasta objetivo | -3.94 | -2.59 | **+1.35 EUR** |
| % compra fuerte | -4.15 | -3.31 | **+0.84 EUR** |
| liquidez | -3.70 | -3.46 | **+0.24 EUR** |
| fuerza relativa | -3.18 | -3.04 | **+0.14 EUR** |
| momentum 30d | -3.00 | -3.21 | **-0.21 EUR** |
| volumen relativo | -2.90 | -3.86 | **-0.96 EUR** |
| RSI | -2.78 | -4.07 | **-1.29 EUR** |
| distancia max 52s | -2.35 | -4.09 | **-1.73 EUR** |
| dispersion | -1.12 | -3.43 | **-2.31 EUR** |
| puesto en el ranking | -1.59 | -4.93 | **-3.34 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
