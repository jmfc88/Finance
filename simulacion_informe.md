# Simulacion en paralelo

Actualizado: 2026-09-23 14:16 · dia 31 de ejecucion
**Revision nº2 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **88**
- Operaciones abiertas: 58

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 1 | 1% | +16.67 EUR |
| beneficio | 1 | 1% | +5.55 EUR |
| flojo | 29 | 33% | +1.09 EUR |
| plano | 4 | 5% | -1.70 EUR |
| perdida | 29 | 33% | -6.97 EUR |
| nefasta | 24 | 27% | -5.81 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 22 | -2.01% | 0/22 (0%) | 4/22 | 8 |
| 11-20 | 27 | -2.07% | 2/27 (7%) | 3/27 | 8 |
| 21-30 | 39 | -4.99% | 0/39 (0%) | 0/39 | 8 |

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
| LA REAL (escalera 25/08) | -294.70 EUR | -3.35% | 2/88 | -8.08 EUR |
| stop corto (5%) | -333.79 EUR | -5.86% | 2/57 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.35%**
- Aciertos (>= 5 EUR limpios): 2/88 (2%)
- Resultado acumulado ficticio: -294.70 EUR sobre 88 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 29 | -4.17 EUR | 0% | 59% |
| nota global | medio | 29 | -4.07 EUR | 3% | 76% |
| nota global | alto | 30 | -1.86 EUR | 3% | 47% |
| puesto en el ranking | bajo | 29 | -1.72 EUR | 3% | 41% |
| puesto en el ranking | medio | 29 | -3.30 EUR | 3% | 66% |
| puesto en el ranking | alto | 30 | -4.97 EUR | 0% | 73% |
| potencial hasta objetivo | bajo | 29 | -3.87 EUR | 3% | 62% |
| potencial hasta objetivo | medio | 29 | -3.26 EUR | 0% | 62% |
| potencial hasta objetivo | alto | 30 | -2.93 EUR | 3% | 57% |
| dispersion | bajo | 29 | -1.16 EUR | 3% | 38% |
| dispersion | medio | 29 | -5.17 EUR | 0% | 76% |
| dispersion | alto | 30 | -3.71 EUR | 3% | 67% |
| % compra fuerte | bajo | 27 | -4.19 EUR | 4% | 67% |
| % compra fuerte | medio | 27 | -3.15 EUR | 0% | 67% |
| % compra fuerte | alto | 29 | -3.73 EUR | 0% | 55% |
| momentum 30d | bajo | 29 | -3.38 EUR | 0% | 55% |
| momentum 30d | medio | 29 | -3.44 EUR | 3% | 59% |
| momentum 30d | alto | 30 | -3.23 EUR | 3% | 67% |
| fuerza relativa | bajo | 29 | -3.73 EUR | 0% | 62% |
| fuerza relativa | medio | 29 | -3.22 EUR | 0% | 55% |
| fuerza relativa | alto | 30 | -3.10 EUR | 7% | 63% |
| RSI | bajo | 29 | -3.11 EUR | 3% | 59% |
| RSI | medio | 29 | -2.91 EUR | 0% | 55% |
| RSI | alto | 30 | -4.00 EUR | 3% | 67% |
| volumen relativo | bajo | 23 | -2.91 EUR | 4% | 57% |
| volumen relativo | medio | 23 | -3.48 EUR | 0% | 61% |
| volumen relativo | alto | 25 | -3.82 EUR | 0% | 52% |
| volatilidad | bajo | 23 | -3.57 EUR | 0% | 52% |
| volatilidad | medio | 23 | -4.00 EUR | 0% | 65% |
| volatilidad | alto | 25 | -2.73 EUR | 4% | 52% |
| liquidez | bajo | 23 | -3.65 EUR | 0% | 57% |
| liquidez | medio | 23 | -2.64 EUR | 4% | 57% |
| liquidez | alto | 25 | -3.91 EUR | 0% | 56% |
| distancia max 52s | bajo | 23 | -2.86 EUR | 4% | 52% |
| distancia max 52s | medio | 23 | -3.12 EUR | 0% | 57% |
| distancia max 52s | alto | 25 | -4.19 EUR | 0% | 60% |
| consenso | buy | 62 | -4.38 EUR | 2% | 69% |
| consenso | strong_buy | 26 | -0.88 EUR | 4% | 38% |
| tendencia tecnica | alcista | 56 | -3.16 EUR | 4% | 59% |
| tendencia tecnica | mixta | 20 | -3.32 EUR | 0% | 60% |
| tendencia tecnica | bajista | 12 | -4.30 EUR | 0% | 67% |
| tendencia analistas | mejorando | 45 | -3.57 EUR | 2% | 62% |
| tendencia analistas | estable | 30 | -4.82 EUR | 0% | 73% |
| regimen de mercado | favorable | 69 | -3.36 EUR | 3% | 64% |
| regimen de mercado | neutro | 19 | -3.30 EUR | 0% | 47% |
| catalizador | sin catalizador | 87 | -3.29 EUR | 2% | 60% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.17 | -1.86 | **+2.31 EUR** |
| potencial hasta objetivo | -3.87 | -2.93 | **+0.94 EUR** |
| volatilidad | -3.57 | -2.73 | **+0.84 EUR** |
| fuerza relativa | -3.73 | -3.10 | **+0.63 EUR** |
| % compra fuerte | -4.19 | -3.73 | **+0.47 EUR** |
| momentum 30d | -3.38 | -3.23 | **+0.15 EUR** |
| liquidez | -3.65 | -3.91 | **-0.27 EUR** |
| RSI | -3.11 | -4.00 | **-0.89 EUR** |
| volumen relativo | -2.91 | -3.82 | **-0.91 EUR** |
| distancia max 52s | -2.86 | -4.19 | **-1.33 EUR** |
| dispersion | -1.16 | -3.71 | **-2.56 EUR** |
| puesto en el ranking | -1.72 | -4.97 | **-3.25 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
