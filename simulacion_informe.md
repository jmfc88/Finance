# Simulacion en paralelo

Actualizado: 2026-10-05 06:59 · dia 43 de ejecucion
Proxima revision de ponderacion en 2 dias.

- Operaciones cerradas: **148**
- Operaciones abiertas: 54

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 42 | 28% | +1.24 EUR |
| plano | 11 | 7% | -1.73 EUR |
| perdida | 57 | 39% | -7.19 EUR |
| nefasta | 33 | 22% | -6.43 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 38 | -2.49% | 2/38 (5%) | 8/38 | 10 |
| 11-20 | 38 | -2.65% | 2/38 (5%) | 3/38 | 9 |
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
| LA REAL (escalera 25/08) | -534.26 EUR | -3.61% | 5/148 | -8.08 EUR |
| stop corto (5%) | -580.59 EUR | -5.69% | 3/102 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.61%**
- Aciertos (>= 5 EUR limpios): 5/148 (3%)
- Resultado acumulado ficticio: -534.26 EUR sobre 148 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 49 | -4.42 EUR | 0% | 59% |
| nota global | medio | 49 | -3.84 EUR | 4% | 67% |
| nota global | alto | 50 | -2.59 EUR | 6% | 56% |
| puesto en el ranking | bajo | 49 | -2.52 EUR | 6% | 53% |
| puesto en el ranking | medio | 49 | -3.71 EUR | 4% | 65% |
| puesto en el ranking | alto | 50 | -4.58 EUR | 0% | 64% |
| potencial hasta objetivo | bajo | 49 | -4.04 EUR | 4% | 59% |
| potencial hasta objetivo | medio | 49 | -3.81 EUR | 0% | 65% |
| potencial hasta objetivo | alto | 50 | -2.99 EUR | 6% | 58% |
| dispersion | bajo | 49 | -1.91 EUR | 6% | 47% |
| dispersion | medio | 49 | -5.45 EUR | 2% | 78% |
| dispersion | alto | 50 | -3.47 EUR | 2% | 58% |
| % compra fuerte | bajo | 46 | -4.73 EUR | 2% | 67% |
| % compra fuerte | medio | 46 | -3.31 EUR | 2% | 63% |
| % compra fuerte | alto | 48 | -3.41 EUR | 4% | 56% |
| momentum 30d | bajo | 49 | -3.53 EUR | 4% | 59% |
| momentum 30d | medio | 49 | -4.17 EUR | 2% | 67% |
| momentum 30d | alto | 50 | -3.14 EUR | 4% | 56% |
| fuerza relativa | bajo | 49 | -3.46 EUR | 4% | 63% |
| fuerza relativa | medio | 49 | -4.15 EUR | 0% | 61% |
| fuerza relativa | alto | 50 | -3.23 EUR | 6% | 58% |
| RSI | bajo | 49 | -3.24 EUR | 6% | 59% |
| RSI | medio | 49 | -3.28 EUR | 2% | 57% |
| RSI | alto | 50 | -4.30 EUR | 2% | 66% |
| volumen relativo | bajo | 43 | -3.79 EUR | 5% | 65% |
| volumen relativo | medio | 43 | -3.05 EUR | 0% | 47% |
| volumen relativo | alto | 45 | -4.17 EUR | 4% | 64% |
| volatilidad | bajo | 43 | -4.16 EUR | 0% | 58% |
| volatilidad | medio | 43 | -5.20 EUR | 2% | 72% |
| volatilidad | alto | 45 | -1.77 EUR | 7% | 47% |
| liquidez | bajo | 43 | -3.58 EUR | 2% | 58% |
| liquidez | medio | 43 | -3.46 EUR | 5% | 60% |
| liquidez | alto | 45 | -3.98 EUR | 2% | 58% |
| distancia max 52s | bajo | 43 | -2.70 EUR | 7% | 53% |
| distancia max 52s | medio | 43 | -4.04 EUR | 2% | 65% |
| distancia max 52s | alto | 45 | -4.28 EUR | 0% | 58% |
| consenso | buy | 106 | -4.27 EUR | 3% | 65% |
| consenso | strong_buy | 42 | -1.94 EUR | 5% | 50% |
| tendencia tecnica | alcista | 89 | -3.59 EUR | 3% | 58% |
| tendencia tecnica | mixta | 37 | -3.18 EUR | 3% | 59% |
| tendencia tecnica | bajista | 22 | -4.42 EUR | 5% | 73% |
| tendencia analistas | mejorando | 72 | -3.54 EUR | 4% | 61% |
| tendencia analistas | estable | 47 | -4.70 EUR | 2% | 72% |
| tendencia analistas | empeorando | 7 | -4.19 EUR | 0% | 71% |
| regimen de mercado | favorable | 94 | -3.40 EUR | 4% | 62% |
| regimen de mercado | neutro | 54 | -3.98 EUR | 2% | 59% |
| catalizador | sin catalizador | 147 | -3.58 EUR | 3% | 61% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.16 | -1.77 | **+2.39 EUR** |
| nota global | -4.42 | -2.59 | **+1.83 EUR** |
| % compra fuerte | -4.73 | -3.41 | **+1.32 EUR** |
| potencial hasta objetivo | -4.04 | -2.99 | **+1.05 EUR** |
| momentum 30d | -3.53 | -3.14 | **+0.39 EUR** |
| fuerza relativa | -3.46 | -3.23 | **+0.23 EUR** |
| volumen relativo | -3.79 | -4.17 | **-0.38 EUR** |
| liquidez | -3.58 | -3.98 | **-0.40 EUR** |
| RSI | -3.24 | -4.30 | **-1.06 EUR** |
| dispersion | -1.91 | -3.47 | **-1.56 EUR** |
| distancia max 52s | -2.70 | -4.28 | **-1.58 EUR** |
| puesto en el ranking | -2.52 | -4.58 | **-2.05 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
