# Simulacion en paralelo

Actualizado: 2026-10-08 13:21 · dia 46 de ejecucion
**Revision nº3 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **169**
- Operaciones abiertas: 51

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 51 | 30% | +1.25 EUR |
| plano | 12 | 7% | -1.75 EUR |
| perdida | 65 | 38% | -7.28 EUR |
| nefasta | 36 | 21% | -6.57 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 43 | -2.30% | 2/43 (5%) | 8/43 | 9 |
| 11-20 | 46 | -3.26% | 2/46 (4%) | 3/46 | 9 |
| 21-30 | 80 | -4.55% | 1/80 (1%) | 3/80 | 10 |

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
| LA REAL (escalera 25/08) | -612.56 EUR | -3.62% | 5/169 | -8.08 EUR |
| stop corto (5%) | -656.14 EUR | -5.71% | 3/115 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.62%**
- Aciertos (>= 5 EUR limpios): 5/169 (3%)
- Resultado acumulado ficticio: -612.56 EUR sobre 169 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 56 | -4.37 EUR | 0% | 59% |
| nota global | medio | 56 | -3.89 EUR | 4% | 66% |
| nota global | alto | 57 | -2.62 EUR | 5% | 54% |
| puesto en el ranking | bajo | 56 | -2.57 EUR | 5% | 52% |
| puesto en el ranking | medio | 56 | -3.66 EUR | 4% | 62% |
| puesto en el ranking | alto | 57 | -4.63 EUR | 0% | 65% |
| potencial hasta objetivo | bajo | 56 | -4.18 EUR | 4% | 59% |
| potencial hasta objetivo | medio | 56 | -4.00 EUR | 0% | 66% |
| potencial hasta objetivo | alto | 57 | -2.71 EUR | 5% | 54% |
| dispersion | bajo | 56 | -2.36 EUR | 5% | 50% |
| dispersion | medio | 56 | -5.13 EUR | 2% | 73% |
| dispersion | alto | 57 | -3.39 EUR | 2% | 56% |
| % compra fuerte | bajo | 53 | -4.48 EUR | 2% | 64% |
| % compra fuerte | medio | 53 | -3.14 EUR | 2% | 60% |
| % compra fuerte | alto | 53 | -3.61 EUR | 4% | 57% |
| momentum 30d | bajo | 56 | -3.02 EUR | 4% | 52% |
| momentum 30d | medio | 56 | -4.31 EUR | 2% | 68% |
| momentum 30d | alto | 57 | -3.54 EUR | 4% | 60% |
| fuerza relativa | bajo | 56 | -3.35 EUR | 4% | 59% |
| fuerza relativa | medio | 56 | -4.06 EUR | 0% | 59% |
| fuerza relativa | alto | 57 | -3.46 EUR | 5% | 61% |
| RSI | bajo | 56 | -2.91 EUR | 5% | 54% |
| RSI | medio | 56 | -3.56 EUR | 2% | 59% |
| RSI | alto | 57 | -4.40 EUR | 2% | 67% |
| volumen relativo | bajo | 50 | -4.03 EUR | 4% | 66% |
| volumen relativo | medio | 50 | -2.78 EUR | 0% | 44% |
| volumen relativo | alto | 52 | -4.23 EUR | 4% | 63% |
| volatilidad | bajo | 50 | -4.11 EUR | 0% | 58% |
| volatilidad | medio | 50 | -4.79 EUR | 2% | 66% |
| volatilidad | alto | 52 | -2.22 EUR | 6% | 50% |
| liquidez | bajo | 50 | -3.47 EUR | 2% | 56% |
| liquidez | medio | 50 | -3.98 EUR | 4% | 62% |
| liquidez | alto | 52 | -3.61 EUR | 2% | 56% |
| distancia max 52s | bajo | 50 | -2.65 EUR | 6% | 52% |
| distancia max 52s | medio | 50 | -3.83 EUR | 2% | 60% |
| distancia max 52s | alto | 52 | -4.55 EUR | 0% | 62% |
| consenso | buy | 118 | -4.11 EUR | 3% | 63% |
| consenso | strong_buy | 51 | -2.49 EUR | 4% | 53% |
| tendencia tecnica | alcista | 97 | -3.75 EUR | 3% | 60% |
| tendencia tecnica | mixta | 44 | -3.20 EUR | 2% | 57% |
| tendencia tecnica | bajista | 28 | -3.87 EUR | 4% | 64% |
| tendencia analistas | mejorando | 81 | -3.52 EUR | 4% | 59% |
| tendencia analistas | estable | 52 | -4.60 EUR | 2% | 71% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 97 | -3.45 EUR | 4% | 62% |
| regimen de mercado | neutro | 72 | -3.86 EUR | 1% | 57% |
| catalizador | sin catalizador | 168 | -3.60 EUR | 3% | 60% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.11 | -2.22 | **+1.89 EUR** |
| nota global | -4.37 | -2.62 | **+1.75 EUR** |
| potencial hasta objetivo | -4.18 | -2.71 | **+1.47 EUR** |
| % compra fuerte | -4.48 | -3.61 | **+0.87 EUR** |
| fuerza relativa | -3.35 | -3.46 | **-0.12 EUR** |
| liquidez | -3.47 | -3.61 | **-0.14 EUR** |
| volumen relativo | -4.03 | -4.23 | **-0.20 EUR** |
| momentum 30d | -3.02 | -3.54 | **-0.52 EUR** |
| dispersion | -2.36 | -3.39 | **-1.03 EUR** |
| RSI | -2.91 | -4.40 | **-1.49 EUR** |
| distancia max 52s | -2.65 | -4.55 | **-1.89 EUR** |
| puesto en el ranking | -2.57 | -4.63 | **-2.06 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
