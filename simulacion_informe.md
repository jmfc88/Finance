# Simulacion en paralelo

Actualizado: 2026-10-08 07:19 · dia 46 de ejecucion
**Revision nº3 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **167**
- Operaciones abiertas: 50

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 50 | 30% | +1.25 EUR |
| plano | 12 | 7% | -1.75 EUR |
| perdida | 64 | 38% | -7.27 EUR |
| nefasta | 36 | 22% | -6.57 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 42 | -2.37% | 2/42 (5%) | 8/42 | 9 |
| 11-20 | 46 | -3.26% | 2/46 (4%) | 3/46 | 9 |
| 21-30 | 79 | -4.50% | 1/79 (1%) | 3/79 | 9 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 28 operaciones, media -3.35%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -166.37 EUR | -3.14% | 3/53 | -10.00 EUR |
| arranca despues (+8%) | -186.10 EUR | -4.23% | 3/44 | -10.00 EUR |
| actual (8% / +5% / 5%) | -186.10 EUR | -4.23% | 3/44 | -10.00 EUR |
| arranca antes (+3%) | -202.98 EUR | -4.06% | 3/50 | -10.00 EUR |
| trailing suelto (7%) | -209.24 EUR | -4.98% | 2/42 | -10.00 EUR |
| sin trailing, solo stop | -221.30 EUR | -5.40% | 1/41 | -10.00 EUR |
| LA REAL (escalera 25/08) | -605.48 EUR | -3.63% | 5/167 | -8.08 EUR |
| stop corto (5%) | -649.14 EUR | -5.69% | 3/114 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.63%**
- Aciertos (>= 5 EUR limpios): 5/167 (3%)
- Resultado acumulado ficticio: -605.48 EUR sobre 167 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 55 | -4.30 EUR | 0% | 58% |
| nota global | medio | 55 | -3.82 EUR | 4% | 65% |
| nota global | alto | 57 | -2.78 EUR | 5% | 56% |
| puesto en el ranking | bajo | 55 | -2.63 EUR | 5% | 53% |
| puesto en el ranking | medio | 55 | -3.74 EUR | 4% | 64% |
| puesto en el ranking | alto | 57 | -4.47 EUR | 0% | 63% |
| potencial hasta objetivo | bajo | 55 | -4.20 EUR | 4% | 60% |
| potencial hasta objetivo | medio | 55 | -3.94 EUR | 0% | 65% |
| potencial hasta objetivo | alto | 57 | -2.76 EUR | 5% | 54% |
| dispersion | bajo | 55 | -2.42 EUR | 5% | 51% |
| dispersion | medio | 55 | -5.08 EUR | 2% | 73% |
| dispersion | alto | 57 | -3.39 EUR | 2% | 56% |
| % compra fuerte | bajo | 52 | -4.59 EUR | 2% | 65% |
| % compra fuerte | medio | 52 | -3.04 EUR | 2% | 60% |
| % compra fuerte | alto | 53 | -3.61 EUR | 4% | 57% |
| momentum 30d | bajo | 55 | -3.09 EUR | 4% | 53% |
| momentum 30d | medio | 55 | -4.25 EUR | 2% | 67% |
| momentum 30d | alto | 57 | -3.54 EUR | 4% | 60% |
| fuerza relativa | bajo | 55 | -3.43 EUR | 4% | 60% |
| fuerza relativa | medio | 55 | -3.99 EUR | 0% | 58% |
| fuerza relativa | alto | 57 | -3.46 EUR | 5% | 61% |
| RSI | bajo | 55 | -2.98 EUR | 5% | 55% |
| RSI | medio | 55 | -3.47 EUR | 2% | 58% |
| RSI | alto | 57 | -4.40 EUR | 2% | 67% |
| volumen relativo | bajo | 50 | -4.03 EUR | 4% | 66% |
| volumen relativo | medio | 50 | -2.96 EUR | 0% | 46% |
| volumen relativo | alto | 50 | -4.08 EUR | 4% | 62% |
| volatilidad | bajo | 50 | -4.05 EUR | 0% | 58% |
| volatilidad | medio | 50 | -4.84 EUR | 2% | 66% |
| volatilidad | alto | 50 | -2.17 EUR | 6% | 50% |
| liquidez | bajo | 50 | -3.65 EUR | 2% | 58% |
| liquidez | medio | 50 | -3.80 EUR | 4% | 62% |
| liquidez | alto | 50 | -3.61 EUR | 2% | 54% |
| distancia max 52s | bajo | 50 | -2.65 EUR | 6% | 52% |
| distancia max 52s | medio | 50 | -4.01 EUR | 2% | 62% |
| distancia max 52s | alto | 50 | -4.40 EUR | 0% | 60% |
| consenso | buy | 117 | -4.08 EUR | 3% | 62% |
| consenso | strong_buy | 50 | -2.56 EUR | 4% | 54% |
| tendencia tecnica | alcista | 97 | -3.75 EUR | 3% | 60% |
| tendencia tecnica | mixta | 43 | -3.09 EUR | 2% | 56% |
| tendencia tecnica | bajista | 27 | -4.05 EUR | 4% | 67% |
| tendencia analistas | mejorando | 81 | -3.52 EUR | 4% | 59% |
| tendencia analistas | estable | 51 | -4.54 EUR | 2% | 71% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 97 | -3.45 EUR | 4% | 62% |
| regimen de mercado | neutro | 70 | -3.87 EUR | 1% | 57% |
| catalizador | sin catalizador | 166 | -3.60 EUR | 3% | 60% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.05 | -2.17 | **+1.89 EUR** |
| nota global | -4.30 | -2.78 | **+1.52 EUR** |
| potencial hasta objetivo | -4.20 | -2.76 | **+1.44 EUR** |
| % compra fuerte | -4.59 | -3.61 | **+0.98 EUR** |
| liquidez | -3.65 | -3.61 | **+0.04 EUR** |
| fuerza relativa | -3.43 | -3.46 | **-0.04 EUR** |
| volumen relativo | -4.03 | -4.08 | **-0.05 EUR** |
| momentum 30d | -3.09 | -3.54 | **-0.45 EUR** |
| dispersion | -2.42 | -3.39 | **-0.97 EUR** |
| RSI | -2.98 | -4.40 | **-1.42 EUR** |
| distancia max 52s | -2.65 | -4.40 | **-1.75 EUR** |
| puesto en el ranking | -2.63 | -4.47 | **-1.83 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
