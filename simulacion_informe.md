# Simulacion en paralelo

Actualizado: 2026-10-08 01:02 · dia 46 de ejecucion
**Revision nº3 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **163**
- Operaciones abiertas: 54

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 50 | 31% | +1.25 EUR |
| plano | 12 | 7% | -1.75 EUR |
| perdida | 62 | 38% | -7.24 EUR |
| nefasta | 34 | 21% | -6.48 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 42 | -2.37% | 2/42 (5%) | 8/42 | 9 |
| 11-20 | 44 | -3.04% | 2/44 (5%) | 3/44 | 9 |
| 21-30 | 77 | -4.41% | 1/77 (1%) | 3/77 | 10 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 28 operaciones, media -3.35%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -156.37 EUR | -3.01% | 3/52 | -10.00 EUR |
| arranca despues (+8%) | -176.10 EUR | -4.10% | 3/43 | -10.00 EUR |
| actual (8% / +5% / 5%) | -176.10 EUR | -4.10% | 3/43 | -10.00 EUR |
| arranca antes (+3%) | -192.98 EUR | -3.94% | 3/49 | -10.00 EUR |
| trailing suelto (7%) | -199.24 EUR | -4.86% | 2/41 | -10.00 EUR |
| sin trailing, solo stop | -211.30 EUR | -5.28% | 1/40 | -10.00 EUR |
| LA REAL (escalera 25/08) | -573.16 EUR | -3.52% | 5/163 | -8.08 EUR |
| stop corto (5%) | -621.14 EUR | -5.65% | 3/110 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.52%**
- Aciertos (>= 5 EUR limpios): 5/163 (3%)
- Resultado acumulado ficticio: -573.16 EUR sobre 163 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 54 | -4.24 EUR | 0% | 57% |
| nota global | medio | 54 | -3.74 EUR | 4% | 65% |
| nota global | alto | 55 | -2.59 EUR | 5% | 55% |
| puesto en el ranking | bajo | 54 | -2.53 EUR | 6% | 52% |
| puesto en el ranking | medio | 54 | -3.50 EUR | 4% | 61% |
| puesto en el ranking | alto | 55 | -4.50 EUR | 0% | 64% |
| potencial hasta objetivo | bajo | 54 | -4.03 EUR | 4% | 57% |
| potencial hasta objetivo | medio | 54 | -3.53 EUR | 2% | 63% |
| potencial hasta objetivo | alto | 55 | -2.99 EUR | 4% | 56% |
| dispersion | bajo | 54 | -2.14 EUR | 6% | 48% |
| dispersion | medio | 54 | -5.19 EUR | 2% | 74% |
| dispersion | alto | 55 | -3.22 EUR | 2% | 55% |
| % compra fuerte | bajo | 51 | -4.52 EUR | 2% | 65% |
| % compra fuerte | medio | 51 | -2.95 EUR | 2% | 59% |
| % compra fuerte | alto | 52 | -3.52 EUR | 4% | 56% |
| momentum 30d | bajo | 54 | -3.00 EUR | 4% | 52% |
| momentum 30d | medio | 54 | -4.17 EUR | 2% | 67% |
| momentum 30d | alto | 55 | -3.38 EUR | 4% | 58% |
| fuerza relativa | bajo | 54 | -3.25 EUR | 4% | 59% |
| fuerza relativa | medio | 54 | -4.01 EUR | 0% | 57% |
| fuerza relativa | alto | 55 | -3.30 EUR | 5% | 60% |
| RSI | bajo | 54 | -2.88 EUR | 6% | 54% |
| RSI | medio | 54 | -3.39 EUR | 2% | 57% |
| RSI | alto | 55 | -4.26 EUR | 2% | 65% |
| volumen relativo | bajo | 48 | -3.86 EUR | 4% | 65% |
| volumen relativo | medio | 48 | -2.74 EUR | 0% | 44% |
| volumen relativo | alto | 50 | -4.08 EUR | 4% | 62% |
| volatilidad | bajo | 48 | -3.94 EUR | 0% | 56% |
| volatilidad | medio | 48 | -4.84 EUR | 2% | 67% |
| volatilidad | alto | 50 | -1.99 EUR | 6% | 48% |
| liquidez | bajo | 48 | -3.46 EUR | 2% | 56% |
| liquidez | medio | 48 | -3.63 EUR | 4% | 60% |
| liquidez | alto | 50 | -3.61 EUR | 2% | 54% |
| distancia max 52s | bajo | 48 | -2.80 EUR | 6% | 54% |
| distancia max 52s | medio | 48 | -3.77 EUR | 0% | 58% |
| distancia max 52s | alto | 50 | -4.11 EUR | 2% | 58% |
| consenso | buy | 116 | -4.05 EUR | 3% | 62% |
| consenso | strong_buy | 47 | -2.21 EUR | 4% | 51% |
| tendencia tecnica | alcista | 95 | -3.66 EUR | 3% | 59% |
| tendencia tecnica | mixta | 41 | -2.84 EUR | 2% | 54% |
| tendencia tecnica | bajista | 27 | -4.05 EUR | 4% | 67% |
| tendencia analistas | mejorando | 80 | -3.46 EUR | 4% | 59% |
| tendencia analistas | estable | 50 | -4.47 EUR | 2% | 70% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 97 | -3.45 EUR | 4% | 62% |
| regimen de mercado | neutro | 66 | -3.61 EUR | 2% | 55% |
| catalizador | sin catalizador | 162 | -3.49 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -3.94 | -1.99 | **+1.95 EUR** |
| nota global | -4.24 | -2.59 | **+1.64 EUR** |
| potencial hasta objetivo | -4.03 | -2.99 | **+1.04 EUR** |
| % compra fuerte | -4.52 | -3.52 | **+1.00 EUR** |
| fuerza relativa | -3.25 | -3.30 | **-0.05 EUR** |
| liquidez | -3.46 | -3.61 | **-0.15 EUR** |
| volumen relativo | -3.86 | -4.08 | **-0.22 EUR** |
| momentum 30d | -3.00 | -3.38 | **-0.37 EUR** |
| dispersion | -2.14 | -3.22 | **-1.07 EUR** |
| distancia max 52s | -2.80 | -4.11 | **-1.31 EUR** |
| RSI | -2.88 | -4.26 | **-1.38 EUR** |
| puesto en el ranking | -2.53 | -4.50 | **-1.97 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
