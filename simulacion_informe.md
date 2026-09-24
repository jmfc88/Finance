# Simulacion en paralelo

Actualizado: 2026-09-24 11:40 · dia 32 de ejecucion
**Revision nº2 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **96**
- Operaciones abiertas: 54

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 1 | 1% | +16.67 EUR |
| beneficio | 1 | 1% | +5.55 EUR |
| flojo | 33 | 34% | +1.23 EUR |
| plano | 4 | 4% | -1.70 EUR |
| perdida | 32 | 33% | -7.08 EUR |
| nefasta | 25 | 26% | -5.90 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 24 | -2.03% | 0/24 (0%) | 5/24 | 8 |
| 11-20 | 28 | -1.96% | 2/28 (7%) | 3/28 | 8 |
| 21-30 | 44 | -4.87% | 0/44 (0%) | 1/44 | 8 |

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
| LA REAL (escalera 25/08) | -317.94 EUR | -3.31% | 2/96 | -8.08 EUR |
| stop corto (5%) | -361.79 EUR | -5.93% | 2/61 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.31%**
- Aciertos (>= 5 EUR limpios): 2/96 (2%)
- Resultado acumulado ficticio: -317.94 EUR sobre 96 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 32 | -4.17 EUR | 0% | 59% |
| nota global | medio | 32 | -3.88 EUR | 3% | 72% |
| nota global | alto | 32 | -1.88 EUR | 3% | 47% |
| puesto en el ranking | bajo | 32 | -1.67 EUR | 3% | 41% |
| puesto en el ranking | medio | 32 | -3.46 EUR | 3% | 66% |
| puesto en el ranking | alto | 32 | -4.80 EUR | 0% | 72% |
| potencial hasta objetivo | bajo | 32 | -3.98 EUR | 3% | 62% |
| potencial hasta objetivo | medio | 32 | -3.35 EUR | 0% | 62% |
| potencial hasta objetivo | alto | 32 | -2.61 EUR | 3% | 53% |
| dispersion | bajo | 32 | -1.44 EUR | 3% | 41% |
| dispersion | medio | 32 | -4.87 EUR | 0% | 72% |
| dispersion | alto | 32 | -3.62 EUR | 3% | 66% |
| % compra fuerte | bajo | 30 | -3.89 EUR | 3% | 63% |
| % compra fuerte | medio | 30 | -3.34 EUR | 0% | 67% |
| % compra fuerte | alto | 31 | -3.63 EUR | 0% | 55% |
| momentum 30d | bajo | 32 | -3.10 EUR | 0% | 53% |
| momentum 30d | medio | 32 | -3.51 EUR | 3% | 59% |
| momentum 30d | alto | 32 | -3.32 EUR | 3% | 66% |
| fuerza relativa | bajo | 32 | -3.28 EUR | 0% | 56% |
| fuerza relativa | medio | 32 | -3.52 EUR | 0% | 59% |
| fuerza relativa | alto | 32 | -3.13 EUR | 6% | 62% |
| RSI | bajo | 32 | -3.09 EUR | 3% | 56% |
| RSI | medio | 32 | -2.87 EUR | 0% | 56% |
| RSI | alto | 32 | -3.98 EUR | 3% | 66% |
| volumen relativo | bajo | 26 | -3.16 EUR | 4% | 58% |
| volumen relativo | medio | 26 | -3.21 EUR | 0% | 58% |
| volumen relativo | alto | 27 | -3.70 EUR | 0% | 52% |
| volatilidad | bajo | 26 | -3.74 EUR | 0% | 54% |
| volatilidad | medio | 26 | -4.02 EUR | 0% | 65% |
| volatilidad | alto | 27 | -2.36 EUR | 4% | 48% |
| liquidez | bajo | 26 | -3.36 EUR | 0% | 54% |
| liquidez | medio | 26 | -2.92 EUR | 4% | 58% |
| liquidez | alto | 27 | -3.79 EUR | 0% | 56% |
| distancia max 52s | bajo | 26 | -2.57 EUR | 4% | 50% |
| distancia max 52s | medio | 26 | -3.35 EUR | 0% | 58% |
| distancia max 52s | alto | 27 | -4.14 EUR | 0% | 59% |
| consenso | buy | 66 | -4.29 EUR | 2% | 68% |
| consenso | strong_buy | 30 | -1.15 EUR | 3% | 40% |
| tendencia tecnica | alcista | 59 | -3.25 EUR | 3% | 59% |
| tendencia tecnica | mixta | 25 | -2.98 EUR | 0% | 56% |
| tendencia tecnica | bajista | 12 | -4.30 EUR | 0% | 67% |
| tendencia analistas | mejorando | 49 | -3.33 EUR | 2% | 59% |
| tendencia analistas | estable | 33 | -4.77 EUR | 0% | 73% |
| tendencia analistas | empeorando | 5 | -2.63 EUR | 0% | 60% |
| regimen de mercado | favorable | 74 | -3.40 EUR | 3% | 64% |
| regimen de mercado | neutro | 22 | -3.01 EUR | 0% | 45% |
| catalizador | sin catalizador | 95 | -3.26 EUR | 2% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.17 | -1.88 | **+2.29 EUR** |
| volatilidad | -3.74 | -2.36 | **+1.38 EUR** |
| potencial hasta objetivo | -3.98 | -2.61 | **+1.37 EUR** |
| % compra fuerte | -3.89 | -3.63 | **+0.26 EUR** |
| fuerza relativa | -3.28 | -3.13 | **+0.15 EUR** |
| momentum 30d | -3.10 | -3.32 | **-0.23 EUR** |
| liquidez | -3.36 | -3.79 | **-0.43 EUR** |
| volumen relativo | -3.16 | -3.70 | **-0.55 EUR** |
| RSI | -3.09 | -3.98 | **-0.89 EUR** |
| distancia max 52s | -2.57 | -4.14 | **-1.57 EUR** |
| dispersion | -1.44 | -3.62 | **-2.18 EUR** |
| puesto en el ranking | -1.67 | -4.80 | **-3.13 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
