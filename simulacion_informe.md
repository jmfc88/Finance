# Simulacion en paralelo

Actualizado: 2026-10-05 18:28 · dia 43 de ejecucion
Proxima revision de ponderacion en 2 dias.

- Operaciones cerradas: **150**
- Operaciones abiertas: 53

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 42 | 28% | +1.24 EUR |
| plano | 11 | 7% | -1.73 EUR |
| perdida | 59 | 39% | -7.22 EUR |
| nefasta | 33 | 22% | -6.43 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 38 | -2.49% | 2/38 (5%) | 8/38 | 10 |
| 11-20 | 40 | -2.92% | 2/40 (5%) | 3/40 | 9 |
| 21-30 | 72 | -4.71% | 1/72 (1%) | 2/72 | 10 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 26 operaciones, media -3.26%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -133.41 EUR | -2.90% | 2/46 | -10.00 EUR |
| arranca despues (+8%) | -150.45 EUR | -3.96% | 3/38 | -10.00 EUR |
| actual (8% / +5% / 5%) | -150.45 EUR | -3.96% | 3/38 | -10.00 EUR |
| arranca antes (+3%) | -164.45 EUR | -3.82% | 3/43 | -10.00 EUR |
| trailing suelto (7%) | -170.21 EUR | -4.60% | 2/37 | -10.00 EUR |
| sin trailing, solo stop | -182.27 EUR | -5.06% | 1/36 | -10.00 EUR |
| LA REAL (escalera 25/08) | -550.42 EUR | -3.67% | 5/150 | -8.08 EUR |
| stop corto (5%) | -594.59 EUR | -5.72% | 3/104 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.67%**
- Aciertos (>= 5 EUR limpios): 5/150 (3%)
- Resultado acumulado ficticio: -550.42 EUR sobre 150 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 50 | -4.49 EUR | 0% | 60% |
| nota global | medio | 50 | -3.93 EUR | 4% | 68% |
| nota global | alto | 50 | -2.59 EUR | 6% | 56% |
| puesto en el ranking | bajo | 50 | -2.63 EUR | 6% | 54% |
| puesto en el ranking | medio | 50 | -3.80 EUR | 4% | 66% |
| puesto en el ranking | alto | 50 | -4.58 EUR | 0% | 64% |
| potencial hasta objetivo | bajo | 50 | -4.12 EUR | 4% | 60% |
| potencial hasta objetivo | medio | 50 | -3.89 EUR | 0% | 66% |
| potencial hasta objetivo | alto | 50 | -2.99 EUR | 6% | 58% |
| dispersion | bajo | 50 | -1.85 EUR | 6% | 46% |
| dispersion | medio | 50 | -5.69 EUR | 2% | 80% |
| dispersion | alto | 50 | -3.47 EUR | 2% | 58% |
| % compra fuerte | bajo | 47 | -4.80 EUR | 2% | 68% |
| % compra fuerte | medio | 47 | -3.21 EUR | 2% | 62% |
| % compra fuerte | alto | 48 | -3.60 EUR | 4% | 58% |
| momentum 30d | bajo | 50 | -3.62 EUR | 4% | 60% |
| momentum 30d | medio | 50 | -4.14 EUR | 2% | 66% |
| momentum 30d | alto | 50 | -3.25 EUR | 4% | 58% |
| fuerza relativa | bajo | 50 | -3.55 EUR | 4% | 64% |
| fuerza relativa | medio | 50 | -4.22 EUR | 0% | 62% |
| fuerza relativa | alto | 50 | -3.23 EUR | 6% | 58% |
| RSI | bajo | 50 | -3.34 EUR | 6% | 60% |
| RSI | medio | 50 | -3.19 EUR | 2% | 56% |
| RSI | alto | 50 | -4.48 EUR | 2% | 68% |
| volumen relativo | bajo | 44 | -3.89 EUR | 5% | 66% |
| volumen relativo | medio | 44 | -3.16 EUR | 0% | 48% |
| volumen relativo | alto | 45 | -4.17 EUR | 4% | 64% |
| volatilidad | bajo | 44 | -4.08 EUR | 0% | 57% |
| volatilidad | medio | 44 | -5.43 EUR | 2% | 75% |
| volatilidad | alto | 45 | -1.77 EUR | 7% | 47% |
| liquidez | bajo | 44 | -3.68 EUR | 2% | 59% |
| liquidez | medio | 44 | -3.57 EUR | 5% | 61% |
| liquidez | alto | 45 | -3.98 EUR | 2% | 58% |
| distancia max 52s | bajo | 44 | -2.82 EUR | 7% | 55% |
| distancia max 52s | medio | 44 | -4.13 EUR | 2% | 66% |
| distancia max 52s | alto | 45 | -4.28 EUR | 0% | 58% |
| consenso | buy | 108 | -4.34 EUR | 3% | 66% |
| consenso | strong_buy | 42 | -1.94 EUR | 5% | 50% |
| tendencia tecnica | alcista | 90 | -3.64 EUR | 3% | 59% |
| tendencia tecnica | mixta | 37 | -3.18 EUR | 3% | 59% |
| tendencia tecnica | bajista | 23 | -4.58 EUR | 4% | 74% |
| tendencia analistas | mejorando | 74 | -3.66 EUR | 4% | 62% |
| tendencia analistas | estable | 47 | -4.70 EUR | 2% | 72% |
| tendencia analistas | empeorando | 7 | -4.19 EUR | 0% | 71% |
| regimen de mercado | favorable | 95 | -3.45 EUR | 4% | 62% |
| regimen de mercado | neutro | 55 | -4.05 EUR | 2% | 60% |
| catalizador | sin catalizador | 149 | -3.64 EUR | 3% | 61% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.08 | -1.77 | **+2.31 EUR** |
| nota global | -4.49 | -2.59 | **+1.90 EUR** |
| % compra fuerte | -4.80 | -3.60 | **+1.20 EUR** |
| potencial hasta objetivo | -4.12 | -2.99 | **+1.13 EUR** |
| momentum 30d | -3.62 | -3.25 | **+0.37 EUR** |
| fuerza relativa | -3.55 | -3.23 | **+0.32 EUR** |
| volumen relativo | -3.89 | -4.17 | **-0.28 EUR** |
| liquidez | -3.68 | -3.98 | **-0.30 EUR** |
| RSI | -3.34 | -4.48 | **-1.14 EUR** |
| distancia max 52s | -2.82 | -4.28 | **-1.46 EUR** |
| dispersion | -1.85 | -3.47 | **-1.62 EUR** |
| puesto en el ranking | -2.63 | -4.58 | **-1.94 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
