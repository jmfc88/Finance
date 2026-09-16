# Simulacion en paralelo

Actualizado: 2026-09-16 17:38 · dia 24 de ejecucion
Proxima revision de ponderacion en 6 dias.

- Operaciones cerradas: **61**
- Operaciones abiertas: 66

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 18 | 30% | +1.14 EUR |
| plano | 0 | - | - |
| perdida | 21 | 34% | -7.65 EUR |
| nefasta | 22 | 36% | -5.60 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 16 | -2.25% | 0/16 (0%) | 4/16 | 6 |
| 11-20 | 20 | -3.09% | 0/20 (0%) | 1/20 | 6 |
| 21-30 | 25 | -6.63% | 0/25 (0%) | 0/25 | 6 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida


## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -24.73 EUR | -3.53% | 0/7 | -10.00 EUR |
| trailing suelto (7%) | -30.00 EUR | -10.00% | 0/3 | -10.00 EUR |
| sin trailing, solo stop | -30.00 EUR | -10.00% | 0/3 | -10.00 EUR |
| arranca despues (+8%) | -30.00 EUR | -10.00% | 0/3 | -10.00 EUR |
| actual (8% / +5% / 5%) | -30.00 EUR | -10.00% | 0/3 | -10.00 EUR |
| arranca antes (+3%) | -40.41 EUR | -6.74% | 0/6 | -10.00 EUR |
| LA REAL (escalera 25/08) | -263.34 EUR | -4.32% | 0/61 | -8.08 EUR |
| stop corto (5%) | -273.00 EUR | -7.00% | 0/39 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-4.32%**
- Aciertos (>= 5 EUR limpios): 0/61 (0%)
- Resultado acumulado ficticio: -263.34 EUR sobre 61 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 20 | -5.36 EUR | 0% | 70% |
| nota global | medio | 20 | -5.36 EUR | 0% | 90% |
| nota global | alto | 21 | -2.34 EUR | 0% | 52% |
| puesto en el ranking | bajo | 20 | -2.05 EUR | 0% | 50% |
| puesto en el ranking | medio | 20 | -3.99 EUR | 0% | 70% |
| puesto en el ranking | alto | 21 | -6.78 EUR | 0% | 90% |
| potencial hasta objetivo | bajo | 20 | -4.90 EUR | 0% | 75% |
| potencial hasta objetivo | medio | 20 | -4.90 EUR | 0% | 80% |
| potencial hasta objetivo | alto | 21 | -3.20 EUR | 0% | 57% |
| dispersion | bajo | 20 | -2.63 EUR | 0% | 50% |
| dispersion | medio | 20 | -5.23 EUR | 0% | 75% |
| dispersion | alto | 21 | -5.05 EUR | 0% | 86% |
| % compra fuerte | bajo | 19 | -5.69 EUR | 0% | 79% |
| % compra fuerte | medio | 19 | -2.82 EUR | 0% | 68% |
| % compra fuerte | alto | 19 | -5.08 EUR | 0% | 74% |
| momentum 30d | bajo | 20 | -3.99 EUR | 0% | 65% |
| momentum 30d | medio | 20 | -5.68 EUR | 0% | 80% |
| momentum 30d | alto | 21 | -3.32 EUR | 0% | 67% |
| fuerza relativa | bajo | 20 | -3.54 EUR | 0% | 60% |
| fuerza relativa | medio | 20 | -5.68 EUR | 0% | 85% |
| fuerza relativa | alto | 21 | -3.76 EUR | 0% | 67% |
| RSI | bajo | 20 | -4.45 EUR | 0% | 65% |
| RSI | medio | 20 | -3.41 EUR | 0% | 70% |
| RSI | alto | 21 | -5.05 EUR | 0% | 76% |
| volumen relativo | bajo | 16 | -4.11 EUR | 0% | 62% |
| volumen relativo | medio | 16 | -4.11 EUR | 0% | 69% |
| volumen relativo | alto | 16 | -5.81 EUR | 0% | 75% |
| volatilidad | bajo | 16 | -5.24 EUR | 0% | 75% |
| volatilidad | medio | 16 | -5.81 EUR | 0% | 81% |
| volatilidad | alto | 16 | -2.97 EUR | 0% | 50% |
| liquidez | bajo | 16 | -4.67 EUR | 0% | 69% |
| liquidez | medio | 16 | -4.67 EUR | 0% | 75% |
| liquidez | alto | 16 | -4.67 EUR | 0% | 62% |
| distancia max 52s | bajo | 16 | -4.67 EUR | 0% | 62% |
| distancia max 52s | medio | 16 | -4.11 EUR | 0% | 69% |
| distancia max 52s | alto | 16 | -5.24 EUR | 0% | 75% |
| consenso | buy | 41 | -5.42 EUR | 0% | 80% |
| consenso | strong_buy | 20 | -2.05 EUR | 0% | 50% |
| tendencia tecnica | alcista | 38 | -3.95 EUR | 0% | 66% |
| tendencia tecnica | mixta | 14 | -4.84 EUR | 0% | 79% |
| tendencia tecnica | bajista | 9 | -5.05 EUR | 0% | 78% |
| tendencia analistas | mejorando | 33 | -4.23 EUR | 0% | 73% |
| tendencia analistas | estable | 19 | -6.03 EUR | 0% | 84% |
| regimen de mercado | favorable | 52 | -4.02 EUR | 0% | 69% |
| regimen de mercado | neutro | 9 | -6.06 EUR | 0% | 78% |
| catalizador | sin catalizador | 60 | -4.25 EUR | 0% | 70% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.36 | -2.34 | **+3.02 EUR** |
| volatilidad | -5.24 | -2.97 | **+2.27 EUR** |
| potencial hasta objetivo | -4.90 | -3.20 | **+1.70 EUR** |
| momentum 30d | -3.99 | -3.32 | **+0.67 EUR** |
| % compra fuerte | -5.69 | -5.08 | **+0.61 EUR** |
| liquidez | -4.67 | -4.67 | **+0.00 EUR** |
| fuerza relativa | -3.54 | -3.76 | **-0.22 EUR** |
| distancia max 52s | -4.67 | -5.24 | **-0.57 EUR** |
| RSI | -4.45 | -5.05 | **-0.61 EUR** |
| volumen relativo | -4.11 | -5.81 | **-1.70 EUR** |
| dispersion | -2.63 | -5.05 | **-2.42 EUR** |
| puesto en el ranking | -2.05 | -6.78 | **-4.73 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
