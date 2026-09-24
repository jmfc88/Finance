# Simulacion en paralelo

Actualizado: 2026-09-24 23:54 · dia 32 de ejecucion
**Revision nº2 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **100**
- Operaciones abiertas: 56

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 1 | 1% | +16.67 EUR |
| beneficio | 2 | 2% | +7.32 EUR |
| flojo | 34 | 34% | +1.22 EUR |
| plano | 4 | 4% | -1.70 EUR |
| perdida | 34 | 34% | -7.14 EUR |
| nefasta | 25 | 25% | -5.90 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 25 | -1.91% | 0/25 (0%) | 5/25 | 8 |
| 11-20 | 28 | -1.96% | 2/28 (7%) | 3/28 | 8 |
| 21-30 | 47 | -4.71% | 1/47 (2%) | 2/47 | 9 |

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
| LA REAL (escalera 25/08) | -324.01 EUR | -3.24% | 3/100 | -8.08 EUR |
| stop corto (5%) | -375.79 EUR | -5.96% | 2/63 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.24%**
- Aciertos (>= 5 EUR limpios): 3/100 (3%)
- Resultado acumulado ficticio: -324.01 EUR sobre 100 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 33 | -4.05 EUR | 3% | 61% |
| nota global | medio | 33 | -4.01 EUR | 3% | 73% |
| nota global | alto | 34 | -1.71 EUR | 3% | 44% |
| puesto en el ranking | bajo | 33 | -1.59 EUR | 3% | 39% |
| puesto en el ranking | medio | 33 | -3.08 EUR | 6% | 64% |
| puesto en el ranking | alto | 34 | -5.00 EUR | 0% | 74% |
| potencial hasta objetivo | bajo | 33 | -4.04 EUR | 3% | 64% |
| potencial hasta objetivo | medio | 33 | -3.28 EUR | 0% | 61% |
| potencial hasta objetivo | alto | 34 | -2.42 EUR | 6% | 53% |
| dispersion | bajo | 33 | -1.12 EUR | 6% | 39% |
| dispersion | medio | 33 | -5.03 EUR | 0% | 73% |
| dispersion | alto | 34 | -3.56 EUR | 3% | 65% |
| % compra fuerte | bajo | 31 | -4.03 EUR | 3% | 65% |
| % compra fuerte | medio | 31 | -2.94 EUR | 3% | 65% |
| % compra fuerte | alto | 33 | -3.63 EUR | 0% | 55% |
| momentum 30d | bajo | 33 | -3.00 EUR | 3% | 55% |
| momentum 30d | medio | 33 | -3.38 EUR | 3% | 58% |
| momentum 30d | alto | 34 | -3.34 EUR | 3% | 65% |
| fuerza relativa | bajo | 33 | -3.18 EUR | 3% | 58% |
| fuerza relativa | medio | 33 | -3.66 EUR | 0% | 58% |
| fuerza relativa | alto | 34 | -2.89 EUR | 6% | 62% |
| RSI | bajo | 33 | -2.78 EUR | 6% | 55% |
| RSI | medio | 33 | -2.69 EUR | 0% | 55% |
| RSI | alto | 34 | -4.22 EUR | 3% | 68% |
| volumen relativo | bajo | 27 | -2.71 EUR | 7% | 56% |
| volumen relativo | medio | 27 | -3.39 EUR | 0% | 59% |
| volumen relativo | alto | 29 | -3.69 EUR | 0% | 52% |
| volatilidad | bajo | 27 | -3.91 EUR | 0% | 56% |
| volatilidad | medio | 27 | -4.17 EUR | 0% | 67% |
| volatilidad | alto | 29 | -1.85 EUR | 7% | 45% |
| liquidez | bajo | 27 | -3.54 EUR | 0% | 56% |
| liquidez | medio | 27 | -3.11 EUR | 4% | 59% |
| liquidez | alto | 29 | -3.18 EUR | 3% | 52% |
| distancia max 52s | bajo | 27 | -2.14 EUR | 7% | 48% |
| distancia max 52s | medio | 27 | -3.86 EUR | 0% | 63% |
| distancia max 52s | alto | 29 | -3.79 EUR | 0% | 55% |
| consenso | buy | 69 | -4.21 EUR | 3% | 68% |
| consenso | strong_buy | 31 | -1.08 EUR | 3% | 39% |
| tendencia tecnica | alcista | 61 | -3.26 EUR | 3% | 59% |
| tendencia tecnica | mixta | 26 | -2.51 EUR | 4% | 54% |
| tendencia tecnica | bajista | 13 | -4.59 EUR | 0% | 69% |
| tendencia analistas | mejorando | 52 | -3.10 EUR | 4% | 58% |
| tendencia analistas | estable | 34 | -4.86 EUR | 0% | 74% |
| tendencia analistas | empeorando | 5 | -2.63 EUR | 0% | 60% |
| regimen de mercado | favorable | 77 | -3.24 EUR | 4% | 62% |
| regimen de mercado | neutro | 23 | -3.23 EUR | 0% | 48% |
| catalizador | sin catalizador | 99 | -3.19 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.05 | -1.71 | **+2.33 EUR** |
| volatilidad | -3.91 | -1.85 | **+2.06 EUR** |
| potencial hasta objetivo | -4.04 | -2.42 | **+1.62 EUR** |
| % compra fuerte | -4.03 | -3.63 | **+0.40 EUR** |
| liquidez | -3.54 | -3.18 | **+0.36 EUR** |
| fuerza relativa | -3.18 | -2.89 | **+0.29 EUR** |
| momentum 30d | -3.00 | -3.34 | **-0.33 EUR** |
| volumen relativo | -2.71 | -3.69 | **-0.99 EUR** |
| RSI | -2.78 | -4.22 | **-1.44 EUR** |
| distancia max 52s | -2.14 | -3.79 | **-1.65 EUR** |
| dispersion | -1.12 | -3.56 | **-2.44 EUR** |
| puesto en el ranking | -1.59 | -5.00 | **-3.41 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
