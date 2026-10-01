# Simulacion en paralelo

Actualizado: 2026-10-01 16:28 · dia 39 de ejecucion
Proxima revision de ponderacion en 6 dias.

- Operaciones cerradas: **142**
- Operaciones abiertas: 50

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 41 | 29% | +1.25 EUR |
| plano | 11 | 8% | -1.73 EUR |
| perdida | 54 | 38% | -7.14 EUR |
| nefasta | 31 | 22% | -6.32 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 37 | -2.34% | 2/37 (5%) | 8/37 | 10 |
| 11-20 | 36 | -2.35% | 2/36 (6%) | 3/36 | 9 |
| 21-30 | 69 | -4.69% | 1/69 (1%) | 2/69 | 10 |

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
| LA REAL (escalera 25/08) | -494.86 EUR | -3.48% | 5/142 | -8.08 EUR |
| stop corto (5%) | -545.59 EUR | -5.62% | 3/97 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.48%**
- Aciertos (>= 5 EUR limpios): 5/142 (4%)
- Resultado acumulado ficticio: -494.86 EUR sobre 142 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 47 | -4.46 EUR | 0% | 60% |
| nota global | medio | 47 | -3.66 EUR | 4% | 66% |
| nota global | alto | 48 | -2.36 EUR | 6% | 54% |
| puesto en el ranking | bajo | 47 | -2.29 EUR | 6% | 51% |
| puesto en el ranking | medio | 47 | -3.53 EUR | 4% | 64% |
| puesto en el ranking | alto | 48 | -4.62 EUR | 0% | 65% |
| potencial hasta objetivo | bajo | 47 | -3.87 EUR | 4% | 57% |
| potencial hasta objetivo | medio | 47 | -3.82 EUR | 0% | 66% |
| potencial hasta objetivo | alto | 48 | -2.78 EUR | 6% | 56% |
| dispersion | bajo | 47 | -1.45 EUR | 6% | 43% |
| dispersion | medio | 47 | -5.54 EUR | 2% | 79% |
| dispersion | alto | 48 | -3.47 EUR | 2% | 58% |
| % compra fuerte | bajo | 45 | -4.66 EUR | 2% | 67% |
| % compra fuerte | medio | 45 | -3.40 EUR | 2% | 64% |
| % compra fuerte | alto | 45 | -3.10 EUR | 4% | 53% |
| momentum 30d | bajo | 47 | -3.34 EUR | 4% | 57% |
| momentum 30d | medio | 47 | -4.08 EUR | 2% | 66% |
| momentum 30d | alto | 48 | -3.05 EUR | 4% | 56% |
| fuerza relativa | bajo | 47 | -3.26 EUR | 4% | 62% |
| fuerza relativa | medio | 47 | -4.17 EUR | 0% | 60% |
| fuerza relativa | alto | 48 | -3.03 EUR | 6% | 58% |
| RSI | bajo | 47 | -3.03 EUR | 6% | 57% |
| RSI | medio | 47 | -3.08 EUR | 2% | 55% |
| RSI | alto | 48 | -4.33 EUR | 2% | 67% |
| volumen relativo | bajo | 41 | -3.80 EUR | 5% | 66% |
| volumen relativo | medio | 41 | -2.81 EUR | 0% | 44% |
| volumen relativo | alto | 43 | -3.99 EUR | 5% | 63% |
| volatilidad | bajo | 41 | -3.97 EUR | 0% | 56% |
| volatilidad | medio | 41 | -5.06 EUR | 2% | 71% |
| volatilidad | alto | 43 | -1.69 EUR | 7% | 47% |
| liquidez | bajo | 41 | -3.36 EUR | 2% | 56% |
| liquidez | medio | 41 | -3.46 EUR | 5% | 61% |
| liquidez | alto | 43 | -3.79 EUR | 2% | 56% |
| distancia max 52s | bajo | 41 | -2.58 EUR | 7% | 54% |
| distancia max 52s | medio | 41 | -4.00 EUR | 2% | 63% |
| distancia max 52s | alto | 43 | -4.02 EUR | 0% | 56% |
| consenso | buy | 102 | -4.21 EUR | 3% | 65% |
| consenso | strong_buy | 40 | -1.64 EUR | 5% | 48% |
| tendencia tecnica | alcista | 85 | -3.48 EUR | 4% | 58% |
| tendencia tecnica | mixta | 36 | -3.04 EUR | 3% | 58% |
| tendencia tecnica | bajista | 21 | -4.24 EUR | 5% | 71% |
| tendencia analistas | mejorando | 70 | -3.54 EUR | 4% | 61% |
| tendencia analistas | estable | 45 | -4.55 EUR | 2% | 71% |
| tendencia analistas | empeorando | 6 | -3.54 EUR | 0% | 67% |
| regimen de mercado | favorable | 93 | -3.35 EUR | 4% | 61% |
| regimen de mercado | neutro | 49 | -3.74 EUR | 2% | 57% |
| catalizador | sin catalizador | 141 | -3.45 EUR | 4% | 60% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -3.97 | -1.69 | **+2.28 EUR** |
| nota global | -4.46 | -2.36 | **+2.10 EUR** |
| % compra fuerte | -4.66 | -3.10 | **+1.56 EUR** |
| potencial hasta objetivo | -3.87 | -2.78 | **+1.09 EUR** |
| momentum 30d | -3.34 | -3.05 | **+0.29 EUR** |
| fuerza relativa | -3.26 | -3.03 | **+0.23 EUR** |
| volumen relativo | -3.80 | -3.99 | **-0.19 EUR** |
| liquidez | -3.36 | -3.79 | **-0.43 EUR** |
| RSI | -3.03 | -4.33 | **-1.29 EUR** |
| distancia max 52s | -2.58 | -4.02 | **-1.43 EUR** |
| dispersion | -1.45 | -3.47 | **-2.01 EUR** |
| puesto en el ranking | -2.29 | -4.62 | **-2.33 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
