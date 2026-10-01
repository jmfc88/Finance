# Simulacion en paralelo

Actualizado: 2026-10-01 13:06 · dia 39 de ejecucion
Proxima revision de ponderacion en 6 dias.

- Operaciones cerradas: **140**
- Operaciones abiertas: 47

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 41 | 29% | +1.25 EUR |
| plano | 11 | 8% | -1.73 EUR |
| perdida | 53 | 38% | -7.12 EUR |
| nefasta | 30 | 21% | -6.26 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 37 | -2.34% | 2/37 (5%) | 8/37 | 10 |
| 11-20 | 35 | -2.18% | 2/35 (6%) | 3/35 | 9 |
| 21-30 | 68 | -4.64% | 1/68 (1%) | 2/68 | 10 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 26 operaciones, media -3.26%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -113.41 EUR | -2.58% | 2/44 | -10.00 EUR |
| arranca despues (+8%) | -130.45 EUR | -3.62% | 3/36 | -10.00 EUR |
| actual (8% / +5% / 5%) | -130.45 EUR | -3.62% | 3/36 | -10.00 EUR |
| arranca antes (+3%) | -144.45 EUR | -3.52% | 3/41 | -10.00 EUR |
| trailing suelto (7%) | -150.21 EUR | -4.29% | 2/35 | -10.00 EUR |
| sin trailing, solo stop | -162.27 EUR | -4.77% | 1/34 | -10.00 EUR |
| LA REAL (escalera 25/08) | -478.70 EUR | -3.42% | 5/140 | -8.08 EUR |
| stop corto (5%) | -531.59 EUR | -5.60% | 3/95 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.42%**
- Aciertos (>= 5 EUR limpios): 5/140 (4%)
- Resultado acumulado ficticio: -478.70 EUR sobre 140 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 46 | -4.38 EUR | 0% | 59% |
| nota global | medio | 46 | -3.57 EUR | 4% | 65% |
| nota global | alto | 48 | -2.36 EUR | 6% | 54% |
| puesto en el ranking | bajo | 46 | -2.16 EUR | 7% | 50% |
| puesto en el ranking | medio | 46 | -3.43 EUR | 4% | 63% |
| puesto en el ranking | alto | 48 | -4.62 EUR | 0% | 65% |
| potencial hasta objetivo | bajo | 46 | -3.78 EUR | 4% | 57% |
| potencial hasta objetivo | medio | 46 | -3.92 EUR | 0% | 67% |
| potencial hasta objetivo | alto | 48 | -2.59 EUR | 6% | 54% |
| dispersion | bajo | 46 | -1.31 EUR | 7% | 41% |
| dispersion | medio | 46 | -5.48 EUR | 2% | 78% |
| dispersion | alto | 48 | -3.47 EUR | 2% | 58% |
| % compra fuerte | bajo | 44 | -4.58 EUR | 2% | 66% |
| % compra fuerte | medio | 44 | -3.46 EUR | 2% | 66% |
| % compra fuerte | alto | 46 | -3.05 EUR | 4% | 52% |
| momentum 30d | bajo | 46 | -3.23 EUR | 4% | 57% |
| momentum 30d | medio | 46 | -4.12 EUR | 2% | 67% |
| momentum 30d | alto | 48 | -2.93 EUR | 4% | 54% |
| fuerza relativa | bajo | 46 | -3.16 EUR | 4% | 61% |
| fuerza relativa | medio | 46 | -4.09 EUR | 0% | 59% |
| fuerza relativa | alto | 48 | -3.03 EUR | 6% | 58% |
| RSI | bajo | 46 | -2.92 EUR | 7% | 57% |
| RSI | medio | 46 | -3.16 EUR | 2% | 57% |
| RSI | alto | 48 | -4.14 EUR | 2% | 65% |
| volumen relativo | bajo | 41 | -3.80 EUR | 5% | 66% |
| volumen relativo | medio | 41 | -2.81 EUR | 0% | 44% |
| volumen relativo | alto | 41 | -3.79 EUR | 5% | 61% |
| volatilidad | bajo | 41 | -3.97 EUR | 0% | 56% |
| volatilidad | medio | 41 | -4.55 EUR | 2% | 66% |
| volatilidad | alto | 41 | -1.88 EUR | 7% | 49% |
| liquidez | bajo | 41 | -3.36 EUR | 2% | 56% |
| liquidez | medio | 41 | -3.46 EUR | 5% | 61% |
| liquidez | alto | 41 | -3.58 EUR | 2% | 54% |
| distancia max 52s | bajo | 41 | -2.58 EUR | 7% | 54% |
| distancia max 52s | medio | 41 | -3.79 EUR | 2% | 63% |
| distancia max 52s | alto | 41 | -4.02 EUR | 0% | 54% |
| consenso | buy | 101 | -4.17 EUR | 3% | 64% |
| consenso | strong_buy | 39 | -1.47 EUR | 5% | 46% |
| tendencia tecnica | alcista | 84 | -3.43 EUR | 4% | 57% |
| tendencia tecnica | mixta | 36 | -3.04 EUR | 3% | 58% |
| tendencia tecnica | bajista | 20 | -4.05 EUR | 5% | 70% |
| tendencia analistas | mejorando | 69 | -3.47 EUR | 4% | 61% |
| tendencia analistas | estable | 45 | -4.55 EUR | 2% | 71% |
| tendencia analistas | empeorando | 6 | -3.54 EUR | 0% | 67% |
| regimen de mercado | favorable | 93 | -3.35 EUR | 4% | 61% |
| regimen de mercado | neutro | 47 | -3.56 EUR | 2% | 55% |
| catalizador | sin catalizador | 139 | -3.39 EUR | 4% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -3.97 | -1.88 | **+2.09 EUR** |
| nota global | -4.38 | -2.36 | **+2.02 EUR** |
| % compra fuerte | -4.58 | -3.05 | **+1.53 EUR** |
| potencial hasta objetivo | -3.78 | -2.59 | **+1.19 EUR** |
| momentum 30d | -3.23 | -2.93 | **+0.30 EUR** |
| fuerza relativa | -3.16 | -3.03 | **+0.13 EUR** |
| volumen relativo | -3.80 | -3.79 | **+0.01 EUR** |
| liquidez | -3.36 | -3.58 | **-0.22 EUR** |
| RSI | -2.92 | -4.14 | **-1.21 EUR** |
| distancia max 52s | -2.58 | -4.02 | **-1.44 EUR** |
| dispersion | -1.31 | -3.47 | **-2.16 EUR** |
| puesto en el ranking | -2.16 | -4.62 | **-2.46 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
