# Simulacion en paralelo

Actualizado: 2026-09-23 21:30 · dia 31 de ejecucion
**Revision nº2 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **89**
- Operaciones abiertas: 59

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 1 | 1% | +16.67 EUR |
| beneficio | 1 | 1% | +5.55 EUR |
| flojo | 29 | 33% | +1.09 EUR |
| plano | 4 | 4% | -1.70 EUR |
| perdida | 30 | 34% | -7.01 EUR |
| nefasta | 24 | 27% | -5.81 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 22 | -2.01% | 0/22 (0%) | 4/22 | 8 |
| 11-20 | 27 | -2.07% | 2/27 (7%) | 3/27 | 8 |
| 21-30 | 40 | -5.07% | 0/40 (0%) | 0/40 | 8 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 11 operaciones, media -2.43%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -47.73 EUR | -2.39% | 1/20 | -10.00 EUR |
| arranca despues (+8%) | -52.20 EUR | -3.26% | 2/16 | -10.00 EUR |
| actual (8% / +5% / 5%) | -52.20 EUR | -3.26% | 2/16 | -10.00 EUR |
| trailing suelto (7%) | -54.65 EUR | -3.42% | 2/16 | -10.00 EUR |
| sin trailing, solo stop | -66.71 EUR | -4.45% | 1/15 | -10.00 EUR |
| arranca antes (+3%) | -68.73 EUR | -3.44% | 2/20 | -10.00 EUR |
| LA REAL (escalera 25/08) | -302.78 EUR | -3.40% | 2/89 | -8.08 EUR |
| stop corto (5%) | -340.79 EUR | -5.88% | 2/58 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.40%**
- Aciertos (>= 5 EUR limpios): 2/89 (2%)
- Resultado acumulado ficticio: -302.78 EUR sobre 89 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 29 | -4.48 EUR | 0% | 62% |
| nota global | medio | 29 | -3.76 EUR | 3% | 72% |
| nota global | alto | 31 | -2.06 EUR | 3% | 48% |
| puesto en el ranking | bajo | 29 | -1.72 EUR | 3% | 41% |
| puesto en el ranking | medio | 29 | -3.30 EUR | 3% | 66% |
| puesto en el ranking | alto | 31 | -5.07 EUR | 0% | 74% |
| potencial hasta objetivo | bajo | 29 | -3.87 EUR | 3% | 62% |
| potencial hasta objetivo | medio | 29 | -3.26 EUR | 0% | 62% |
| potencial hasta objetivo | alto | 31 | -3.10 EUR | 3% | 58% |
| dispersion | bajo | 29 | -1.16 EUR | 3% | 38% |
| dispersion | medio | 29 | -5.17 EUR | 0% | 76% |
| dispersion | alto | 31 | -3.85 EUR | 3% | 68% |
| % compra fuerte | bajo | 28 | -4.33 EUR | 4% | 68% |
| % compra fuerte | medio | 28 | -3.33 EUR | 0% | 68% |
| % compra fuerte | alto | 28 | -3.57 EUR | 0% | 54% |
| momentum 30d | bajo | 29 | -3.38 EUR | 0% | 55% |
| momentum 30d | medio | 29 | -3.44 EUR | 3% | 59% |
| momentum 30d | alto | 31 | -3.39 EUR | 3% | 68% |
| fuerza relativa | bajo | 29 | -3.73 EUR | 0% | 62% |
| fuerza relativa | medio | 29 | -3.22 EUR | 0% | 55% |
| fuerza relativa | alto | 31 | -3.26 EUR | 6% | 65% |
| RSI | bajo | 29 | -3.11 EUR | 3% | 59% |
| RSI | medio | 29 | -2.91 EUR | 0% | 55% |
| RSI | alto | 31 | -4.14 EUR | 3% | 68% |
| volumen relativo | bajo | 24 | -3.13 EUR | 4% | 58% |
| volumen relativo | medio | 24 | -3.29 EUR | 0% | 58% |
| volumen relativo | alto | 24 | -4.02 EUR | 0% | 54% |
| volatilidad | bajo | 24 | -3.76 EUR | 0% | 54% |
| volatilidad | medio | 24 | -4.17 EUR | 0% | 67% |
| volatilidad | alto | 24 | -2.51 EUR | 4% | 50% |
| liquidez | bajo | 24 | -3.83 EUR | 0% | 58% |
| liquidez | medio | 24 | -2.87 EUR | 4% | 58% |
| liquidez | alto | 24 | -3.74 EUR | 0% | 54% |
| distancia max 52s | bajo | 24 | -3.08 EUR | 4% | 54% |
| distancia max 52s | medio | 24 | -3.33 EUR | 0% | 58% |
| distancia max 52s | alto | 24 | -4.03 EUR | 0% | 58% |
| consenso | buy | 63 | -4.44 EUR | 2% | 70% |
| consenso | strong_buy | 26 | -0.88 EUR | 4% | 38% |
| tendencia tecnica | alcista | 57 | -3.24 EUR | 4% | 60% |
| tendencia tecnica | mixta | 20 | -3.32 EUR | 0% | 60% |
| tendencia tecnica | bajista | 12 | -4.30 EUR | 0% | 67% |
| tendencia analistas | mejorando | 45 | -3.57 EUR | 2% | 62% |
| tendencia analistas | estable | 31 | -4.93 EUR | 0% | 74% |
| regimen de mercado | favorable | 70 | -3.43 EUR | 3% | 64% |
| regimen de mercado | neutro | 19 | -3.30 EUR | 0% | 47% |
| catalizador | sin catalizador | 88 | -3.35 EUR | 2% | 60% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.48 | -2.06 | **+2.43 EUR** |
| volatilidad | -3.76 | -2.51 | **+1.25 EUR** |
| potencial hasta objetivo | -3.87 | -3.10 | **+0.77 EUR** |
| % compra fuerte | -4.33 | -3.57 | **+0.76 EUR** |
| fuerza relativa | -3.73 | -3.26 | **+0.47 EUR** |
| liquidez | -3.83 | -3.74 | **+0.09 EUR** |
| momentum 30d | -3.38 | -3.39 | **-0.00 EUR** |
| volumen relativo | -3.13 | -4.02 | **-0.89 EUR** |
| distancia max 52s | -3.08 | -4.03 | **-0.95 EUR** |
| RSI | -3.11 | -4.14 | **-1.02 EUR** |
| dispersion | -1.16 | -3.85 | **-2.70 EUR** |
| puesto en el ranking | -1.72 | -5.07 | **-3.35 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
