# Simulacion en paralelo

Actualizado: 2026-10-12 15:15 · dia 50 de ejecucion
Proxima revision de ponderacion en 10 dias.

- Operaciones cerradas: **173**
- Operaciones abiertas: 54

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 54 | 31% | +1.28 EUR |
| plano | 12 | 7% | -1.75 EUR |
| perdida | 66 | 38% | -7.22 EUR |
| nefasta | 36 | 21% | -6.57 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|---|
| 1-10 | 43 | -2.30% | 2/43 (5%) | 8/43 | 9 |
| 11-20 | 46 | -3.26% | 2/46 (4%) | 3/46 | 9 |
| 21-30 | 84 | -4.31% | 1/84 (1%) | 4/84 | 10 |

## Contra el indice

Lo unico que dice si la seleccion vale. Perder un 2% con el indice
cayendo un 4% es GANARLE al mercado; perderlo con el indice subiendo
un 3% es un desastre. El numero suelto no significa nada.

| Franja | Ops | Operacion | Indice | Diferencia | Ganan al indice |
|---|---|---|---|---|---|
| 1-10 | 0 | - | - | - | - |
| 11-20 | 0 | - | - | - | - |
| 21-30 | 0 | - | - | - | - |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 29 operaciones, media -3.36%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Media | Ops | Total | Aciertos | Peor |
|---|---|---|---|---|---|
| trailing pegado (3%) | -3.14% | 54 | -169.79 EUR | 3/54 | -10.00 EUR |
| LA REAL (escalera 25/08) | -3.53% | 173 | -610.45 EUR | 5/173 | -8.08 EUR |
| arranca antes (+3%) | -4.05% | 51 | -206.40 EUR | 3/51 | -10.00 EUR |
| arranca despues (+8%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| actual (8% / +5% / 5%) | -4.21% | 45 | -189.52 EUR | 3/45 | -10.00 EUR |
| trailing suelto (7%) | -4.95% | 43 | -212.66 EUR | 2/43 | -10.00 EUR |
| sin trailing, solo stop | -5.35% | 42 | -224.72 EUR | 1/42 | -10.00 EUR |
| stop corto (5%) | -5.69% | 116 | -659.56 EUR | 3/116 | -7.00 EUR |

**Como leerlo:** se ordena por MEDIA por operacion, que es lo unico
comparable: cada regla cierra un numero distinto de operaciones, asi
que la que mas aguanta acumula menos total aunque sea mejor. La
columna `Ops` dice sobre cuantas se calcula cada fila. Mira tambien
`Peor`: una regla que gana mas pero con caidas grandes puede no
compensar.

## Conjunto

- Media neta: **-3.53%**
- Aciertos (>= 5 EUR limpios): 5/173 (3%)
- Resultado acumulado ficticio: -610.45 EUR sobre 173 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|---|
| nota global | bajo | 57 | -3.85 EUR | 0% | 54% |
| nota global | medio | 57 | -3.95 EUR | 4% | 67% |
| nota global | alto | 59 | -2.81 EUR | 5% | 56% |
| puesto en el ranking | bajo | 57 | -2.67 EUR | 5% | 53% |
| puesto en el ranking | medio | 57 | -3.68 EUR | 4% | 63% |
| puesto en el ranking | alto | 59 | -4.22 EUR | 0% | 61% |
| potencial hasta objetivo | bajo | 57 | -4.09 EUR | 4% | 58% |
| potencial hasta objetivo | medio | 57 | -3.82 EUR | 0% | 65% |
| potencial hasta objetivo | alto | 59 | -2.71 EUR | 5% | 54% |
| dispersion | bajo | 57 | -2.30 EUR | 5% | 49% |
| dispersion | medio | 57 | -4.74 EUR | 2% | 70% |
| dispersion | alto | 59 | -3.55 EUR | 2% | 58% |
| % compra fuerte | bajo | 54 | -4.29 EUR | 2% | 63% |
| % compra fuerte | medio | 54 | -3.02 EUR | 2% | 59% |
| % compra fuerte | alto | 55 | -3.61 EUR | 4% | 56% |
| momentum 30d | bajo | 57 | -2.99 EUR | 4% | 53% |
| momentum 30d | medio | 57 | -4.09 EUR | 2% | 65% |
| momentum 30d | alto | 59 | -3.50 EUR | 3% | 59% |
| fuerza relativa | bajo | 57 | -3.35 EUR | 4% | 60% |
| fuerza relativa | medio | 57 | -3.97 EUR | 0% | 58% |
| fuerza relativa | alto | 59 | -3.27 EUR | 5% | 59% |
| RSI | bajo | 57 | -2.76 EUR | 5% | 53% |
| RSI | medio | 57 | -3.48 EUR | 2% | 58% |
| RSI | alto | 59 | -4.33 EUR | 2% | 66% |
| volumen relativo | bajo | 52 | -3.96 EUR | 4% | 65% |
| volumen relativo | medio | 52 | -2.54 EUR | 0% | 42% |
| volumen relativo | alto | 52 | -4.23 EUR | 4% | 63% |
| volatilidad | bajo | 52 | -4.21 EUR | 0% | 60% |
| volatilidad | medio | 52 | -4.30 EUR | 2% | 62% |
| volatilidad | alto | 52 | -2.22 EUR | 6% | 50% |
| liquidez | bajo | 52 | -3.43 EUR | 2% | 56% |
| liquidez | medio | 52 | -3.70 EUR | 4% | 62% |
| liquidez | alto | 52 | -3.61 EUR | 2% | 54% |
| distancia max 52s | bajo | 52 | -2.55 EUR | 6% | 52% |
| distancia max 52s | medio | 52 | -3.64 EUR | 2% | 58% |
| distancia max 52s | alto | 52 | -4.55 EUR | 0% | 62% |
| consenso | buy | 122 | -3.96 EUR | 2% | 61% |
| consenso | strong_buy | 51 | -2.49 EUR | 4% | 53% |
| tendencia tecnica | alcista | 98 | -3.70 EUR | 3% | 59% |
| tendencia tecnica | mixta | 46 | -2.96 EUR | 2% | 54% |
| tendencia tecnica | bajista | 29 | -3.86 EUR | 3% | 66% |
| tendencia analistas | mejorando | 83 | -3.43 EUR | 4% | 59% |
| tendencia analistas | estable | 53 | -4.50 EUR | 2% | 70% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 97 | -3.45 EUR | 4% | 62% |
| regimen de mercado | neutro | 76 | -3.63 EUR | 1% | 55% |
| catalizador | sin catalizador | 172 | -3.50 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.21 | -2.22 | **+1.99 EUR** |
| potencial hasta objetivo | -4.09 | -2.71 | **+1.38 EUR** |
| nota global | -3.85 | -2.81 | **+1.04 EUR** |
| % compra fuerte | -4.29 | -3.61 | **+0.68 EUR** |
| fuerza relativa | -3.35 | -3.27 | **+0.08 EUR** |
| liquidez | -3.43 | -3.61 | **-0.18 EUR** |
| volumen relativo | -3.96 | -4.23 | **-0.27 EUR** |
| momentum 30d | -2.99 | -3.50 | **-0.51 EUR** |
| dispersion | -2.30 | -3.55 | **-1.25 EUR** |
| puesto en el ranking | -2.67 | -4.22 | **-1.55 EUR** |
| RSI | -2.76 | -4.33 | **-1.57 EUR** |
| distancia max 52s | -2.55 | -4.55 | **-2.00 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
