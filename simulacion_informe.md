# Simulacion en paralelo

Actualizado: 2026-09-21 21:59 · dia 29 de ejecucion
Proxima revision de ponderacion en 1 dia.

- Operaciones cerradas: **78**
- Operaciones abiertas: 59

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 1 | 1% | +5.55 EUR |
| flojo | 22 | 28% | +1.12 EUR |
| plano | 4 | 5% | -1.70 EUR |
| perdida | 28 | 36% | -7.09 EUR |
| nefasta | 23 | 29% | -5.71 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 20 | -2.31% | 0/20 (0%) | 4/20 | 8 |
| 11-20 | 26 | -2.79% | 1/26 (4%) | 2/26 | 8 |
| 21-30 | 32 | -5.87% | 0/32 (0%) | 0/32 | 7 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 10 operaciones, media -2.31%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -61.04 EUR | -3.39% | 0/18 | -10.00 EUR |
| trailing suelto (7%) | -63.06 EUR | -4.50% | 1/14 | -10.00 EUR |
| sin trailing, solo stop | -63.06 EUR | -4.50% | 1/14 | -10.00 EUR |
| arranca despues (+8%) | -63.06 EUR | -4.50% | 1/14 | -10.00 EUR |
| actual (8% / +5% / 5%) | -63.06 EUR | -4.50% | 1/14 | -10.00 EUR |
| arranca antes (+3%) | -79.59 EUR | -4.42% | 1/18 | -10.00 EUR |
| LA REAL (escalera 25/08) | -306.64 EUR | -3.93% | 1/78 | -8.08 EUR |
| stop corto (5%) | -327.30 EUR | -6.18% | 1/53 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.93%**
- Aciertos (>= 5 EUR limpios): 1/78 (1%)
- Resultado acumulado ficticio: -306.64 EUR sobre 78 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 26 | -5.29 EUR | 0% | 69% |
| nota global | medio | 26 | -4.21 EUR | 0% | 81% |
| nota global | alto | 26 | -2.30 EUR | 4% | 46% |
| puesto en el ranking | bajo | 26 | -1.95 EUR | 4% | 46% |
| puesto en el ranking | medio | 26 | -4.13 EUR | 0% | 69% |
| puesto en el ranking | alto | 26 | -5.71 EUR | 0% | 81% |
| potencial hasta objetivo | bajo | 26 | -4.08 EUR | 4% | 65% |
| potencial hasta objetivo | medio | 26 | -4.27 EUR | 0% | 73% |
| potencial hasta objetivo | alto | 26 | -3.44 EUR | 0% | 58% |
| dispersion | bajo | 26 | -2.18 EUR | 0% | 42% |
| dispersion | medio | 26 | -5.78 EUR | 0% | 85% |
| dispersion | alto | 26 | -3.84 EUR | 4% | 69% |
| % compra fuerte | bajo | 24 | -5.03 EUR | 4% | 75% |
| % compra fuerte | medio | 24 | -3.29 EUR | 0% | 71% |
| % compra fuerte | alto | 26 | -3.92 EUR | 0% | 58% |
| momentum 30d | bajo | 26 | -3.89 EUR | 0% | 62% |
| momentum 30d | medio | 26 | -4.49 EUR | 0% | 69% |
| momentum 30d | alto | 26 | -3.41 EUR | 4% | 65% |
| fuerza relativa | bajo | 26 | -3.93 EUR | 0% | 65% |
| fuerza relativa | medio | 26 | -3.88 EUR | 0% | 62% |
| fuerza relativa | alto | 26 | -3.99 EUR | 4% | 69% |
| RSI | bajo | 26 | -3.84 EUR | 0% | 62% |
| RSI | medio | 26 | -3.71 EUR | 0% | 65% |
| RSI | alto | 26 | -4.25 EUR | 4% | 69% |
| volumen relativo | bajo | 20 | -3.83 EUR | 0% | 60% |
| volumen relativo | medio | 20 | -3.95 EUR | 0% | 65% |
| volumen relativo | alto | 21 | -4.71 EUR | 0% | 62% |
| volatilidad | bajo | 20 | -4.48 EUR | 0% | 65% |
| volatilidad | medio | 20 | -5.20 EUR | 0% | 75% |
| volatilidad | alto | 21 | -2.89 EUR | 0% | 48% |
| liquidez | bajo | 20 | -4.11 EUR | 0% | 60% |
| liquidez | medio | 20 | -4.43 EUR | 0% | 70% |
| liquidez | alto | 21 | -3.98 EUR | 0% | 57% |
| distancia max 52s | bajo | 20 | -4.45 EUR | 0% | 60% |
| distancia max 52s | medio | 20 | -3.29 EUR | 0% | 60% |
| distancia max 52s | alto | 21 | -4.75 EUR | 0% | 67% |
| consenso | buy | 55 | -4.82 EUR | 2% | 75% |
| consenso | strong_buy | 23 | -1.81 EUR | 0% | 43% |
| tendencia tecnica | alcista | 52 | -3.78 EUR | 2% | 63% |
| tendencia tecnica | mixta | 16 | -4.11 EUR | 0% | 69% |
| tendencia tecnica | bajista | 10 | -4.45 EUR | 0% | 70% |
| tendencia analistas | mejorando | 41 | -3.79 EUR | 2% | 66% |
| tendencia analistas | estable | 28 | -5.07 EUR | 0% | 75% |
| regimen de mercado | favorable | 65 | -3.80 EUR | 2% | 66% |
| regimen de mercado | neutro | 13 | -4.59 EUR | 0% | 62% |
| catalizador | sin catalizador | 77 | -3.88 EUR | 1% | 65% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.29 | -2.30 | **+2.99 EUR** |
| volatilidad | -4.48 | -2.89 | **+1.59 EUR** |
| % compra fuerte | -5.03 | -3.92 | **+1.10 EUR** |
| potencial hasta objetivo | -4.08 | -3.44 | **+0.64 EUR** |
| momentum 30d | -3.89 | -3.41 | **+0.48 EUR** |
| liquidez | -4.11 | -3.98 | **+0.13 EUR** |
| fuerza relativa | -3.93 | -3.99 | **-0.06 EUR** |
| distancia max 52s | -4.45 | -4.75 | **-0.30 EUR** |
| RSI | -3.84 | -4.25 | **-0.41 EUR** |
| volumen relativo | -3.83 | -4.71 | **-0.88 EUR** |
| dispersion | -2.18 | -3.84 | **-1.66 EUR** |
| puesto en el ranking | -1.95 | -5.71 | **-3.77 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
