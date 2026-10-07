# Simulacion en paralelo

Actualizado: 2026-10-07 13:15 · dia 45 de ejecucion
**Revision nº3 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **158**
- Operaciones abiertas: 51

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 47 | 30% | +1.22 EUR |
| plano | 12 | 8% | -1.75 EUR |
| perdida | 61 | 39% | -7.23 EUR |
| nefasta | 33 | 21% | -6.43 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 41 | -2.24% | 2/41 (5%) | 8/41 | 9 |
| 11-20 | 43 | -2.93% | 2/43 (5%) | 3/43 | 9 |
| 21-30 | 74 | -4.66% | 1/74 (1%) | 2/74 | 10 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 28 operaciones, media -3.35%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -141.96 EUR | -2.90% | 2/49 | -10.00 EUR |
| arranca despues (+8%) | -159.48 EUR | -3.99% | 3/40 | -10.00 EUR |
| actual (8% / +5% / 5%) | -159.48 EUR | -3.99% | 3/40 | -10.00 EUR |
| arranca antes (+3%) | -173.48 EUR | -3.86% | 3/45 | -10.00 EUR |
| trailing suelto (7%) | -179.24 EUR | -4.60% | 2/39 | -10.00 EUR |
| sin trailing, solo stop | -191.30 EUR | -5.03% | 1/38 | -10.00 EUR |
| LA REAL (escalera 25/08) | -562.53 EUR | -3.56% | 5/158 | -8.08 EUR |
| stop corto (5%) | -610.52 EUR | -5.71% | 3/107 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.56%**
- Aciertos (>= 5 EUR limpios): 5/158 (3%)
- Resultado acumulado ficticio: -562.53 EUR sobre 158 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 52 | -4.44 EUR | 0% | 60% |
| nota global | medio | 52 | -3.80 EUR | 4% | 65% |
| nota global | alto | 54 | -2.49 EUR | 6% | 54% |
| puesto en el ranking | bajo | 52 | -2.32 EUR | 6% | 50% |
| puesto en el ranking | medio | 52 | -3.72 EUR | 4% | 63% |
| puesto en el ranking | alto | 54 | -4.60 EUR | 0% | 65% |
| potencial hasta objetivo | bajo | 52 | -4.12 EUR | 4% | 60% |
| potencial hasta objetivo | medio | 52 | -3.57 EUR | 0% | 62% |
| potencial hasta objetivo | alto | 54 | -3.02 EUR | 6% | 57% |
| dispersion | bajo | 52 | -1.92 EUR | 6% | 46% |
| dispersion | medio | 52 | -5.08 EUR | 2% | 73% |
| dispersion | alto | 54 | -3.68 EUR | 2% | 59% |
| % compra fuerte | bajo | 50 | -4.68 EUR | 2% | 66% |
| % compra fuerte | medio | 50 | -3.03 EUR | 2% | 60% |
| % compra fuerte | alto | 50 | -3.52 EUR | 4% | 56% |
| momentum 30d | bajo | 52 | -2.98 EUR | 4% | 52% |
| momentum 30d | medio | 52 | -4.20 EUR | 2% | 67% |
| momentum 30d | alto | 54 | -3.50 EUR | 4% | 59% |
| fuerza relativa | bajo | 52 | -3.41 EUR | 4% | 62% |
| fuerza relativa | medio | 52 | -3.85 EUR | 0% | 56% |
| fuerza relativa | alto | 54 | -3.42 EUR | 6% | 61% |
| RSI | bajo | 52 | -3.03 EUR | 6% | 56% |
| RSI | medio | 52 | -3.38 EUR | 2% | 58% |
| RSI | alto | 54 | -4.24 EUR | 2% | 65% |
| volumen relativo | bajo | 47 | -3.77 EUR | 4% | 66% |
| volumen relativo | medio | 47 | -3.26 EUR | 0% | 47% |
| volumen relativo | alto | 47 | -3.82 EUR | 4% | 60% |
| volatilidad | bajo | 47 | -3.93 EUR | 0% | 55% |
| volatilidad | medio | 47 | -5.09 EUR | 2% | 70% |
| volatilidad | alto | 47 | -1.84 EUR | 6% | 47% |
| liquidez | bajo | 47 | -3.56 EUR | 2% | 57% |
| liquidez | medio | 47 | -3.73 EUR | 4% | 62% |
| liquidez | alto | 47 | -3.57 EUR | 2% | 53% |
| distancia max 52s | bajo | 47 | -2.75 EUR | 6% | 53% |
| distancia max 52s | medio | 47 | -3.94 EUR | 2% | 62% |
| distancia max 52s | alto | 47 | -4.17 EUR | 0% | 57% |
| consenso | buy | 113 | -4.20 EUR | 3% | 64% |
| consenso | strong_buy | 45 | -1.95 EUR | 4% | 49% |
| tendencia tecnica | alcista | 92 | -3.64 EUR | 3% | 59% |
| tendencia tecnica | mixta | 41 | -2.84 EUR | 2% | 54% |
| tendencia tecnica | bajista | 25 | -4.46 EUR | 4% | 72% |
| tendencia analistas | mejorando | 78 | -3.46 EUR | 4% | 59% |
| tendencia analistas | estable | 49 | -4.63 EUR | 2% | 71% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 95 | -3.45 EUR | 4% | 62% |
| regimen de mercado | neutro | 63 | -3.73 EUR | 2% | 56% |
| catalizador | sin catalizador | 157 | -3.53 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -3.93 | -1.84 | **+2.08 EUR** |
| nota global | -4.44 | -2.49 | **+1.95 EUR** |
| % compra fuerte | -4.68 | -3.52 | **+1.16 EUR** |
| potencial hasta objetivo | -4.12 | -3.02 | **+1.10 EUR** |
| fuerza relativa | -3.41 | -3.42 | **-0.01 EUR** |
| liquidez | -3.56 | -3.57 | **-0.02 EUR** |
| volumen relativo | -3.77 | -3.82 | **-0.05 EUR** |
| momentum 30d | -2.98 | -3.50 | **-0.52 EUR** |
| RSI | -3.03 | -4.24 | **-1.21 EUR** |
| distancia max 52s | -2.75 | -4.17 | **-1.42 EUR** |
| dispersion | -1.92 | -3.68 | **-1.76 EUR** |
| puesto en el ranking | -2.32 | -4.60 | **-2.28 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
