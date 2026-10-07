# Simulacion en paralelo

Actualizado: 2026-10-07 07:12 · dia 45 de ejecucion
**Revision nº3 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **152**
- Operaciones abiertas: 56

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 44 | 29% | +1.23 EUR |
| plano | 11 | 7% | -1.73 EUR |
| perdida | 59 | 39% | -7.22 EUR |
| nefasta | 33 | 22% | -6.43 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 40 | -2.32% | 2/40 (5%) | 8/40 | 9 |
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
| LA REAL (escalera 25/08) | -548.42 EUR | -3.61% | 5/152 | -8.08 EUR |
| stop corto (5%) | -594.59 EUR | -5.72% | 3/104 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.61%**
- Aciertos (>= 5 EUR limpios): 5/152 (3%)
- Resultado acumulado ficticio: -548.42 EUR sobre 152 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 50 | -4.49 EUR | 0% | 60% |
| nota global | medio | 50 | -3.93 EUR | 4% | 68% |
| nota global | alto | 52 | -2.45 EUR | 6% | 54% |
| puesto en el ranking | bajo | 50 | -2.27 EUR | 6% | 50% |
| puesto en el ranking | medio | 50 | -3.80 EUR | 4% | 66% |
| puesto en el ranking | alto | 52 | -4.71 EUR | 0% | 65% |
| potencial hasta objetivo | bajo | 50 | -4.12 EUR | 4% | 60% |
| potencial hasta objetivo | medio | 50 | -3.71 EUR | 0% | 64% |
| potencial hasta objetivo | alto | 52 | -3.01 EUR | 6% | 58% |
| dispersion | bajo | 50 | -1.85 EUR | 6% | 46% |
| dispersion | medio | 50 | -5.32 EUR | 2% | 76% |
| dispersion | alto | 52 | -3.65 EUR | 2% | 60% |
| % compra fuerte | bajo | 48 | -4.87 EUR | 2% | 69% |
| % compra fuerte | medio | 48 | -2.94 EUR | 2% | 58% |
| % compra fuerte | alto | 48 | -3.60 EUR | 4% | 58% |
| momentum 30d | bajo | 50 | -3.28 EUR | 4% | 56% |
| momentum 30d | medio | 50 | -4.23 EUR | 2% | 68% |
| momentum 30d | alto | 52 | -3.33 EUR | 4% | 58% |
| fuerza relativa | bajo | 50 | -3.55 EUR | 4% | 64% |
| fuerza relativa | medio | 50 | -4.04 EUR | 0% | 58% |
| fuerza relativa | alto | 52 | -3.24 EUR | 6% | 60% |
| RSI | bajo | 50 | -3.34 EUR | 6% | 60% |
| RSI | medio | 50 | -3.19 EUR | 2% | 56% |
| RSI | alto | 52 | -4.27 EUR | 2% | 65% |
| volumen relativo | bajo | 45 | -3.78 EUR | 4% | 64% |
| volumen relativo | medio | 45 | -3.27 EUR | 0% | 49% |
| volumen relativo | alto | 45 | -3.97 EUR | 4% | 62% |
| volatilidad | bajo | 45 | -3.97 EUR | 0% | 56% |
| volatilidad | medio | 45 | -5.29 EUR | 2% | 73% |
| volatilidad | alto | 45 | -1.77 EUR | 7% | 47% |
| liquidez | bajo | 45 | -3.58 EUR | 2% | 58% |
| liquidez | medio | 45 | -3.67 EUR | 4% | 62% |
| liquidez | alto | 45 | -3.78 EUR | 2% | 56% |
| distancia max 52s | bajo | 45 | -2.73 EUR | 7% | 53% |
| distancia max 52s | medio | 45 | -4.11 EUR | 2% | 67% |
| distancia max 52s | alto | 45 | -4.18 EUR | 0% | 56% |
| consenso | buy | 108 | -4.34 EUR | 3% | 66% |
| consenso | strong_buy | 44 | -1.81 EUR | 5% | 48% |
| tendencia tecnica | alcista | 91 | -3.59 EUR | 3% | 58% |
| tendencia tecnica | mixta | 37 | -3.18 EUR | 3% | 59% |
| tendencia tecnica | bajista | 24 | -4.35 EUR | 4% | 71% |
| tendencia analistas | mejorando | 76 | -3.54 EUR | 4% | 61% |
| tendencia analistas | estable | 47 | -4.70 EUR | 2% | 72% |
| tendencia analistas | empeorando | 7 | -4.19 EUR | 0% | 71% |
| regimen de mercado | favorable | 95 | -3.45 EUR | 4% | 62% |
| regimen de mercado | neutro | 57 | -3.88 EUR | 2% | 58% |
| catalizador | sin catalizador | 151 | -3.58 EUR | 3% | 60% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -3.97 | -1.77 | **+2.20 EUR** |
| nota global | -4.49 | -2.45 | **+2.04 EUR** |
| % compra fuerte | -4.87 | -3.60 | **+1.27 EUR** |
| potencial hasta objetivo | -4.12 | -3.01 | **+1.11 EUR** |
| fuerza relativa | -3.55 | -3.24 | **+0.31 EUR** |
| momentum 30d | -3.28 | -3.33 | **-0.04 EUR** |
| volumen relativo | -3.78 | -3.97 | **-0.19 EUR** |
| liquidez | -3.58 | -3.78 | **-0.20 EUR** |
| RSI | -3.34 | -4.27 | **-0.93 EUR** |
| distancia max 52s | -2.73 | -4.18 | **-1.45 EUR** |
| dispersion | -1.85 | -3.65 | **-1.80 EUR** |
| puesto en el ranking | -2.27 | -4.71 | **-2.44 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
