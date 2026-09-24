# Simulacion en paralelo

Actualizado: 2026-09-24 14:14 · dia 32 de ejecucion
**Revision nº2 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **99**
- Operaciones abiertas: 55

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 1 | 1% | +16.67 EUR |
| beneficio | 2 | 2% | +7.32 EUR |
| flojo | 34 | 34% | +1.22 EUR |
| plano | 4 | 4% | -1.70 EUR |
| perdida | 33 | 33% | -7.11 EUR |
| nefasta | 25 | 25% | -5.90 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 25 | -1.91% | 0/25 (0%) | 5/25 | 8 |
| 11-20 | 28 | -1.96% | 2/28 (7%) | 3/28 | 8 |
| 21-30 | 46 | -4.64% | 1/46 (2%) | 2/46 | 8 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 11 operaciones, media -2.43%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -50.19 EUR | -2.18% | 1/23 | -10.00 EUR |
| arranca despues (+8%) | -59.59 EUR | -3.51% | 2/17 | -10.00 EUR |
| actual (8% / +5% / 5%) | -59.59 EUR | -3.51% | 2/17 | -10.00 EUR |
| trailing suelto (7%) | -62.04 EUR | -3.65% | 2/17 | -10.00 EUR |
| sin trailing, solo stop | -74.10 EUR | -4.63% | 1/16 | -10.00 EUR |
| arranca antes (+3%) | -76.12 EUR | -3.62% | 2/21 | -10.00 EUR |
| LA REAL (escalera 25/08) | -315.93 EUR | -3.19% | 3/99 | -8.08 EUR |
| stop corto (5%) | -368.79 EUR | -5.95% | 2/62 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.19%**
- Aciertos (>= 5 EUR limpios): 3/99 (3%)
- Resultado acumulado ficticio: -315.93 EUR sobre 99 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 33 | -4.05 EUR | 3% | 61% |
| nota global | medio | 33 | -3.73 EUR | 3% | 70% |
| nota global | alto | 33 | -1.79 EUR | 3% | 45% |
| puesto en el ranking | bajo | 33 | -1.59 EUR | 3% | 39% |
| puesto en el ranking | medio | 33 | -3.08 EUR | 6% | 64% |
| puesto en el ranking | alto | 33 | -4.90 EUR | 0% | 73% |
| potencial hasta objetivo | bajo | 33 | -4.04 EUR | 3% | 64% |
| potencial hasta objetivo | medio | 33 | -3.00 EUR | 0% | 58% |
| potencial hasta objetivo | alto | 33 | -2.53 EUR | 6% | 55% |
| dispersion | bajo | 33 | -1.12 EUR | 6% | 39% |
| dispersion | medio | 33 | -4.97 EUR | 0% | 73% |
| dispersion | alto | 33 | -3.48 EUR | 3% | 64% |
| % compra fuerte | bajo | 31 | -4.03 EUR | 3% | 65% |
| % compra fuerte | medio | 31 | -2.94 EUR | 3% | 65% |
| % compra fuerte | alto | 32 | -3.49 EUR | 0% | 53% |
| momentum 30d | bajo | 33 | -3.00 EUR | 3% | 55% |
| momentum 30d | medio | 33 | -3.38 EUR | 3% | 58% |
| momentum 30d | alto | 33 | -3.19 EUR | 3% | 64% |
| fuerza relativa | bajo | 33 | -3.18 EUR | 3% | 58% |
| fuerza relativa | medio | 33 | -3.39 EUR | 0% | 58% |
| fuerza relativa | alto | 33 | -3.01 EUR | 6% | 61% |
| RSI | bajo | 33 | -2.78 EUR | 6% | 55% |
| RSI | medio | 33 | -2.69 EUR | 0% | 55% |
| RSI | alto | 33 | -4.10 EUR | 3% | 67% |
| volumen relativo | bajo | 27 | -2.71 EUR | 7% | 56% |
| volumen relativo | medio | 27 | -3.06 EUR | 0% | 56% |
| volumen relativo | alto | 28 | -3.86 EUR | 0% | 54% |
| volatilidad | bajo | 27 | -3.57 EUR | 0% | 56% |
| volatilidad | medio | 27 | -4.51 EUR | 0% | 67% |
| volatilidad | alto | 28 | -1.63 EUR | 7% | 43% |
| liquidez | bajo | 27 | -3.54 EUR | 0% | 56% |
| liquidez | medio | 27 | -3.11 EUR | 4% | 59% |
| liquidez | alto | 28 | -3.01 EUR | 4% | 50% |
| distancia max 52s | bajo | 27 | -2.14 EUR | 7% | 48% |
| distancia max 52s | medio | 27 | -3.52 EUR | 0% | 59% |
| distancia max 52s | alto | 28 | -3.96 EUR | 0% | 57% |
| consenso | buy | 68 | -4.15 EUR | 3% | 68% |
| consenso | strong_buy | 31 | -1.08 EUR | 3% | 39% |
| tendencia tecnica | alcista | 60 | -3.18 EUR | 3% | 58% |
| tendencia tecnica | mixta | 26 | -2.51 EUR | 4% | 54% |
| tendencia tecnica | bajista | 13 | -4.59 EUR | 0% | 69% |
| tendencia analistas | mejorando | 52 | -3.10 EUR | 4% | 58% |
| tendencia analistas | estable | 33 | -4.77 EUR | 0% | 73% |
| tendencia analistas | empeorando | 5 | -2.63 EUR | 0% | 60% |
| regimen de mercado | favorable | 76 | -3.18 EUR | 4% | 62% |
| regimen de mercado | neutro | 23 | -3.23 EUR | 0% | 48% |
| catalizador | sin catalizador | 98 | -3.14 EUR | 3% | 58% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.05 | -1.79 | **+2.25 EUR** |
| volatilidad | -3.57 | -1.63 | **+1.94 EUR** |
| potencial hasta objetivo | -4.04 | -2.53 | **+1.52 EUR** |
| % compra fuerte | -4.03 | -3.49 | **+0.54 EUR** |
| liquidez | -3.54 | -3.01 | **+0.53 EUR** |
| fuerza relativa | -3.18 | -3.01 | **+0.17 EUR** |
| momentum 30d | -3.00 | -3.19 | **-0.19 EUR** |
| volumen relativo | -2.71 | -3.86 | **-1.16 EUR** |
| RSI | -2.78 | -4.10 | **-1.32 EUR** |
| distancia max 52s | -2.14 | -3.96 | **-1.82 EUR** |
| dispersion | -1.12 | -3.48 | **-2.36 EUR** |
| puesto en el ranking | -1.59 | -4.90 | **-3.31 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
