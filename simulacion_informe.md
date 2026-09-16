# Simulacion en paralelo

Actualizado: 2026-09-16 11:27 · dia 24 de ejecucion
Proxima revision de ponderacion en 6 dias.

- Operaciones cerradas: **60**
- Operaciones abiertas: 65

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 0 | - | - |
| beneficio | 0 | - | - |
| flojo | 18 | 30% | +1.14 EUR |
| plano | 0 | - | - |
| perdida | 20 | 33% | -7.63 EUR |
| nefasta | 22 | 37% | -5.60 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 16 | -2.25% | 0/16 (0%) | 4/16 | 6 |
| 11-20 | 19 | -2.82% | 0/19 (0%) | 1/19 | 6 |
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
| LA REAL (escalera 25/08) | -255.26 EUR | -4.25% | 0/60 | -8.08 EUR |
| stop corto (5%) | -266.00 EUR | -7.00% | 0/38 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-4.25%**
- Aciertos (>= 5 EUR limpios): 0/60 (0%)
- Resultado acumulado ficticio: -255.26 EUR sobre 60 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 20 | -5.36 EUR | 0% | 70% |
| nota global | medio | 20 | -4.90 EUR | 0% | 90% |
| nota global | alto | 20 | -2.50 EUR | 0% | 50% |
| puesto en el ranking | bajo | 20 | -2.05 EUR | 0% | 50% |
| puesto en el ranking | medio | 20 | -3.99 EUR | 0% | 70% |
| puesto en el ranking | alto | 20 | -6.72 EUR | 0% | 90% |
| potencial hasta objetivo | bajo | 20 | -4.90 EUR | 0% | 75% |
| potencial hasta objetivo | medio | 20 | -4.32 EUR | 0% | 75% |
| potencial hasta objetivo | alto | 20 | -3.54 EUR | 0% | 60% |
| dispersion | bajo | 20 | -2.63 EUR | 0% | 50% |
| dispersion | medio | 20 | -5.23 EUR | 0% | 75% |
| dispersion | alto | 20 | -4.90 EUR | 0% | 85% |
| % compra fuerte | bajo | 18 | -5.56 EUR | 0% | 78% |
| % compra fuerte | medio | 18 | -2.53 EUR | 0% | 67% |
| % compra fuerte | alto | 20 | -5.23 EUR | 0% | 75% |
| momentum 30d | bajo | 20 | -3.99 EUR | 0% | 65% |
| momentum 30d | medio | 20 | -5.23 EUR | 0% | 75% |
| momentum 30d | alto | 20 | -3.54 EUR | 0% | 70% |
| fuerza relativa | bajo | 20 | -3.54 EUR | 0% | 60% |
| fuerza relativa | medio | 20 | -5.23 EUR | 0% | 80% |
| fuerza relativa | alto | 20 | -3.99 EUR | 0% | 70% |
| RSI | bajo | 20 | -4.45 EUR | 0% | 65% |
| RSI | medio | 20 | -3.41 EUR | 0% | 70% |
| RSI | alto | 20 | -4.90 EUR | 0% | 75% |
| volumen relativo | bajo | 15 | -3.84 EUR | 0% | 60% |
| volumen relativo | medio | 15 | -4.45 EUR | 0% | 73% |
| volumen relativo | alto | 17 | -5.41 EUR | 0% | 71% |
| volatilidad | bajo | 15 | -5.05 EUR | 0% | 73% |
| volatilidad | medio | 15 | -6.26 EUR | 0% | 87% |
| volatilidad | alto | 17 | -2.74 EUR | 0% | 47% |
| liquidez | bajo | 15 | -4.45 EUR | 0% | 67% |
| liquidez | medio | 15 | -5.66 EUR | 0% | 80% |
| liquidez | alto | 17 | -3.81 EUR | 0% | 59% |
| distancia max 52s | bajo | 15 | -5.05 EUR | 0% | 67% |
| distancia max 52s | medio | 15 | -4.45 EUR | 0% | 73% |
| distancia max 52s | alto | 17 | -4.34 EUR | 0% | 65% |
| consenso | buy | 40 | -5.36 EUR | 0% | 80% |
| consenso | strong_buy | 20 | -2.05 EUR | 0% | 50% |
| tendencia tecnica | alcista | 37 | -3.84 EUR | 0% | 65% |
| tendencia tecnica | mixta | 14 | -4.84 EUR | 0% | 79% |
| tendencia tecnica | bajista | 9 | -5.05 EUR | 0% | 78% |
| tendencia analistas | mejorando | 32 | -4.11 EUR | 0% | 72% |
| tendencia analistas | estable | 19 | -6.03 EUR | 0% | 84% |
| regimen de mercado | favorable | 51 | -3.94 EUR | 0% | 69% |
| regimen de mercado | neutro | 9 | -6.06 EUR | 0% | 78% |
| catalizador | sin catalizador | 59 | -4.19 EUR | 0% | 69% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -5.36 | -2.50 | **+2.85 EUR** |
| volatilidad | -5.05 | -2.74 | **+2.31 EUR** |
| potencial hasta objetivo | -4.90 | -3.54 | **+1.36 EUR** |
| distancia max 52s | -5.05 | -4.34 | **+0.71 EUR** |
| liquidez | -4.45 | -3.81 | **+0.64 EUR** |
| momentum 30d | -3.99 | -3.54 | **+0.45 EUR** |
| % compra fuerte | -5.56 | -5.23 | **+0.33 EUR** |
| fuerza relativa | -3.54 | -3.99 | **-0.45 EUR** |
| RSI | -4.45 | -4.90 | **-0.45 EUR** |
| volumen relativo | -3.84 | -5.41 | **-1.57 EUR** |
| dispersion | -2.63 | -4.90 | **-2.27 EUR** |
| puesto en el ranking | -2.05 | -6.72 | **-4.67 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
