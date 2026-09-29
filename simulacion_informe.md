# Simulacion en paralelo

Actualizado: 2026-09-29 01:01 · dia 37 de ejecucion
Proxima revision de ponderacion en 8 dias.

- Operaciones cerradas: **107**
- Operaciones abiertas: 58

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 2% | +16.67 EUR |
| beneficio | 2 | 2% | +7.32 EUR |
| flojo | 36 | 34% | +1.28 EUR |
| plano | 5 | 5% | -1.87 EUR |
| perdida | 36 | 34% | -7.19 EUR |
| nefasta | 26 | 24% | -5.98 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 27 | -1.02% | 1/27 (4%) | 7/27 | 8 |
| 11-20 | 28 | -1.96% | 2/28 (7%) | 3/28 | 8 |
| 21-30 | 52 | -4.75% | 1/52 (2%) | 2/52 | 9 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 12 operaciones, media -2.44%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -40.02 EUR | -1.48% | 2/27 | -10.00 EUR |
| arranca despues (+8%) | -54.83 EUR | -2.74% | 3/20 | -10.00 EUR |
| actual (8% / +5% / 5%) | -54.83 EUR | -2.74% | 3/20 | -10.00 EUR |
| arranca antes (+3%) | -71.36 EUR | -2.97% | 3/24 | -10.00 EUR |
| trailing suelto (7%) | -74.59 EUR | -3.93% | 2/19 | -10.00 EUR |
| sin trailing, solo stop | -86.65 EUR | -4.81% | 1/18 | -10.00 EUR |
| LA REAL (escalera 25/08) | -329.60 EUR | -3.08% | 4/107 | -8.08 EUR |
| stop corto (5%) | -382.03 EUR | -5.62% | 3/68 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.08%**
- Aciertos (>= 5 EUR limpios): 4/107 (4%)
- Resultado acumulado ficticio: -329.60 EUR sobre 107 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 35 | -4.77 EUR | 0% | 66% |
| nota global | medio | 35 | -3.33 EUR | 6% | 66% |
| nota global | alto | 37 | -1.25 EUR | 5% | 43% |
| puesto en el ranking | bajo | 35 | -0.92 EUR | 6% | 37% |
| puesto en el ranking | medio | 35 | -3.37 EUR | 6% | 66% |
| puesto en el ranking | alto | 37 | -4.85 EUR | 0% | 70% |
| potencial hasta objetivo | bajo | 35 | -4.12 EUR | 3% | 63% |
| potencial hasta objetivo | medio | 35 | -3.29 EUR | 0% | 60% |
| potencial hasta objetivo | alto | 37 | -1.90 EUR | 8% | 51% |
| dispersion | bajo | 35 | -0.48 EUR | 9% | 37% |
| dispersion | medio | 35 | -5.04 EUR | 0% | 71% |
| dispersion | alto | 37 | -3.68 EUR | 3% | 65% |
| % compra fuerte | bajo | 33 | -4.27 EUR | 3% | 67% |
| % compra fuerte | medio | 33 | -2.98 EUR | 3% | 64% |
| % compra fuerte | alto | 35 | -3.02 EUR | 3% | 51% |
| momentum 30d | bajo | 35 | -2.59 EUR | 6% | 51% |
| momentum 30d | medio | 35 | -3.49 EUR | 3% | 60% |
| momentum 30d | alto | 37 | -3.16 EUR | 3% | 62% |
| fuerza relativa | bajo | 35 | -2.49 EUR | 6% | 54% |
| fuerza relativa | medio | 35 | -3.76 EUR | 0% | 57% |
| fuerza relativa | alto | 37 | -2.99 EUR | 5% | 62% |
| RSI | bajo | 35 | -2.45 EUR | 9% | 54% |
| RSI | medio | 35 | -2.77 EUR | 0% | 54% |
| RSI | alto | 37 | -3.97 EUR | 3% | 65% |
| volumen relativo | bajo | 30 | -2.94 EUR | 7% | 60% |
| volumen relativo | medio | 30 | -3.07 EUR | 0% | 50% |
| volumen relativo | alto | 30 | -3.23 EUR | 3% | 53% |
| volatilidad | bajo | 30 | -4.02 EUR | 0% | 60% |
| volatilidad | medio | 30 | -3.99 EUR | 0% | 60% |
| volatilidad | alto | 30 | -1.23 EUR | 10% | 43% |
| liquidez | bajo | 30 | -2.78 EUR | 3% | 53% |
| liquidez | medio | 30 | -3.31 EUR | 3% | 60% |
| liquidez | alto | 30 | -3.16 EUR | 3% | 50% |
| distancia max 52s | bajo | 30 | -1.91 EUR | 10% | 50% |
| distancia max 52s | medio | 30 | -3.29 EUR | 0% | 57% |
| distancia max 52s | alto | 30 | -4.05 EUR | 0% | 57% |
| consenso | buy | 74 | -4.27 EUR | 3% | 68% |
| consenso | strong_buy | 33 | -0.41 EUR | 6% | 36% |
| tendencia tecnica | alcista | 66 | -3.37 EUR | 3% | 59% |
| tendencia tecnica | mixta | 27 | -2.38 EUR | 4% | 52% |
| tendencia tecnica | bajista | 14 | -3.07 EUR | 7% | 64% |
| tendencia analistas | mejorando | 53 | -3.02 EUR | 4% | 57% |
| tendencia analistas | estable | 39 | -4.50 EUR | 3% | 72% |
| tendencia analistas | empeorando | 5 | -2.63 EUR | 0% | 60% |
| regimen de mercado | favorable | 79 | -3.18 EUR | 4% | 61% |
| regimen de mercado | neutro | 28 | -2.80 EUR | 4% | 50% |
| catalizador | sin catalizador | 106 | -3.03 EUR | 4% | 58% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.77 | -1.25 | **+3.52 EUR** |
| volatilidad | -4.02 | -1.23 | **+2.79 EUR** |
| potencial hasta objetivo | -4.12 | -1.90 | **+2.22 EUR** |
| % compra fuerte | -4.27 | -3.02 | **+1.26 EUR** |
| volumen relativo | -2.94 | -3.23 | **-0.29 EUR** |
| liquidez | -2.78 | -3.16 | **-0.38 EUR** |
| fuerza relativa | -2.49 | -2.99 | **-0.50 EUR** |
| momentum 30d | -2.59 | -3.16 | **-0.58 EUR** |
| RSI | -2.45 | -3.97 | **-1.52 EUR** |
| distancia max 52s | -1.91 | -4.05 | **-2.14 EUR** |
| dispersion | -0.48 | -3.68 | **-3.20 EUR** |
| puesto en el ranking | -0.92 | -4.85 | **-3.93 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
