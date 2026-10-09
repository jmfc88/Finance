# Simulacion en paralelo

Actualizado: 2026-10-09 07:21 · dia 47 de ejecucion
**Revision nº3 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **170**
- Operaciones abiertas: 55

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 52 | 31% | +1.29 EUR |
| plano | 12 | 7% | -1.75 EUR |
| perdida | 65 | 38% | -7.28 EUR |
| nefasta | 36 | 21% | -6.57 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 43 | -2.30% | 2/43 (5%) | 8/43 | 9 |
| 11-20 | 46 | -3.26% | 2/46 (4%) | 3/46 | 9 |
| 21-30 | 81 | -4.45% | 1/81 (1%) | 4/81 | 9 |

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
| LA REAL (escalera 25/08) | -609.03 EUR | -3.58% | 5/170 | -8.08 EUR |
| stop corto (5%) | -656.14 EUR | -5.71% | 3/115 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.58%**
- Aciertos (>= 5 EUR limpios): 5/170 (3%)
- Resultado acumulado ficticio: -609.03 EUR sobre 170 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 56 | -4.17 EUR | 0% | 57% |
| nota global | medio | 56 | -3.89 EUR | 4% | 66% |
| nota global | alto | 58 | -2.72 EUR | 5% | 55% |
| puesto en el ranking | bajo | 56 | -2.57 EUR | 5% | 52% |
| puesto en el ranking | medio | 56 | -3.66 EUR | 4% | 62% |
| puesto en el ranking | alto | 58 | -4.49 EUR | 0% | 64% |
| potencial hasta objetivo | bajo | 56 | -4.18 EUR | 4% | 59% |
| potencial hasta objetivo | medio | 56 | -3.91 EUR | 0% | 66% |
| potencial hasta objetivo | alto | 58 | -2.70 EUR | 5% | 53% |
| dispersion | bajo | 56 | -2.36 EUR | 5% | 50% |
| dispersion | medio | 56 | -4.93 EUR | 2% | 71% |
| dispersion | alto | 58 | -3.47 EUR | 2% | 57% |
| % compra fuerte | bajo | 53 | -4.39 EUR | 2% | 64% |
| % compra fuerte | medio | 53 | -3.01 EUR | 2% | 58% |
| % compra fuerte | alto | 54 | -3.69 EUR | 4% | 57% |
| momentum 30d | bajo | 56 | -3.02 EUR | 4% | 52% |
| momentum 30d | medio | 56 | -4.15 EUR | 2% | 66% |
| momentum 30d | alto | 58 | -3.58 EUR | 3% | 60% |
| fuerza relativa | bajo | 56 | -3.35 EUR | 4% | 59% |
| fuerza relativa | medio | 56 | -4.06 EUR | 0% | 59% |
| fuerza relativa | alto | 58 | -3.34 EUR | 5% | 60% |
| RSI | bajo | 56 | -2.91 EUR | 5% | 54% |
| RSI | medio | 56 | -3.56 EUR | 2% | 59% |
| RSI | alto | 58 | -4.26 EUR | 2% | 66% |
| volumen relativo | bajo | 51 | -3.88 EUR | 4% | 65% |
| volumen relativo | medio | 51 | -2.88 EUR | 0% | 45% |
| volumen relativo | alto | 51 | -4.16 EUR | 4% | 63% |
| volatilidad | bajo | 51 | -4.13 EUR | 0% | 59% |
| volatilidad | medio | 51 | -4.50 EUR | 2% | 63% |
| volatilidad | alto | 51 | -2.28 EUR | 6% | 51% |
| liquidez | bajo | 51 | -3.34 EUR | 2% | 55% |
| liquidez | medio | 51 | -3.88 EUR | 4% | 63% |
| liquidez | alto | 51 | -3.70 EUR | 2% | 55% |
| distancia max 52s | bajo | 51 | -2.53 EUR | 6% | 51% |
| distancia max 52s | medio | 51 | -3.91 EUR | 2% | 61% |
| distancia max 52s | alto | 51 | -4.48 EUR | 0% | 61% |
| consenso | buy | 119 | -4.05 EUR | 3% | 62% |
| consenso | strong_buy | 51 | -2.49 EUR | 4% | 53% |
| tendencia tecnica | alcista | 97 | -3.75 EUR | 3% | 60% |
| tendencia tecnica | mixta | 45 | -3.05 EUR | 2% | 56% |
| tendencia tecnica | bajista | 28 | -3.87 EUR | 4% | 64% |
| tendencia analistas | mejorando | 82 | -3.43 EUR | 4% | 59% |
| tendencia analistas | estable | 52 | -4.60 EUR | 2% | 71% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 97 | -3.45 EUR | 4% | 62% |
| regimen de mercado | neutro | 73 | -3.76 EUR | 1% | 56% |
| catalizador | sin catalizador | 169 | -3.56 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.13 | -2.28 | **+1.85 EUR** |
| potencial hasta objetivo | -4.18 | -2.70 | **+1.48 EUR** |
| nota global | -4.17 | -2.72 | **+1.45 EUR** |
| % compra fuerte | -4.39 | -3.69 | **+0.70 EUR** |
| fuerza relativa | -3.35 | -3.34 | **+0.00 EUR** |
| volumen relativo | -3.88 | -4.16 | **-0.28 EUR** |
| liquidez | -3.34 | -3.70 | **-0.36 EUR** |
| momentum 30d | -3.02 | -3.58 | **-0.56 EUR** |
| dispersion | -2.36 | -3.47 | **-1.11 EUR** |
| RSI | -2.91 | -4.26 | **-1.35 EUR** |
| puesto en el ranking | -2.57 | -4.49 | **-1.92 EUR** |
| distancia max 52s | -2.53 | -4.48 | **-1.94 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
