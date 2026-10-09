# Simulacion en paralelo

Actualizado: 2026-10-09 22:38 · dia 47 de ejecucion
**Revision nº3 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **172**
- Operaciones abiertas: 53

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 54 | 31% | +1.28 EUR |
| plano | 12 | 7% | -1.75 EUR |
| perdida | 65 | 38% | -7.28 EUR |
| nefasta | 36 | 21% | -6.57 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 43 | -2.30% | 2/43 (5%) | 8/43 | 9 |
| 11-20 | 46 | -3.26% | 2/46 (4%) | 3/46 | 9 |
| 21-30 | 83 | -4.32% | 1/83 (1%) | 4/83 | 9 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 28 operaciones, media -3.35%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -166.37 EUR | -3.14% | 3/53 | -10.00 EUR |
| arranca despues (+8%) | -186.10 EUR | -4.23% | 3/44 | -10.00 EUR |
| actual (8% / +5% / 5%) | -186.10 EUR | -4.23% | 3/44 | -10.00 EUR |
| arranca antes (+3%) | -202.98 EUR | -4.06% | 3/50 | -10.00 EUR |
| trailing suelto (7%) | -209.24 EUR | -4.98% | 2/42 | -10.00 EUR |
| sin trailing, solo stop | -221.30 EUR | -5.40% | 1/41 | -10.00 EUR |
| LA REAL (escalera 25/08) | -607.03 EUR | -3.53% | 5/172 | -8.08 EUR |
| stop corto (5%) | -656.14 EUR | -5.71% | 3/115 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.53%**
- Aciertos (>= 5 EUR limpios): 5/172 (3%)
- Resultado acumulado ficticio: -607.03 EUR sobre 172 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 57 | -3.93 EUR | 0% | 54% |
| nota global | medio | 57 | -3.95 EUR | 4% | 67% |
| nota global | alto | 58 | -2.72 EUR | 5% | 55% |
| puesto en el ranking | bajo | 57 | -2.67 EUR | 5% | 53% |
| puesto en el ranking | medio | 57 | -3.68 EUR | 4% | 63% |
| puesto en el ranking | alto | 58 | -4.23 EUR | 0% | 60% |
| potencial hasta objetivo | bajo | 57 | -4.09 EUR | 4% | 58% |
| potencial hasta objetivo | medio | 57 | -3.82 EUR | 0% | 65% |
| potencial hasta objetivo | alto | 58 | -2.70 EUR | 5% | 53% |
| dispersion | bajo | 57 | -2.30 EUR | 5% | 49% |
| dispersion | medio | 57 | -4.82 EUR | 2% | 70% |
| dispersion | alto | 58 | -3.47 EUR | 2% | 57% |
| % compra fuerte | bajo | 54 | -4.29 EUR | 2% | 63% |
| % compra fuerte | medio | 54 | -3.11 EUR | 2% | 59% |
| % compra fuerte | alto | 54 | -3.52 EUR | 4% | 56% |
| momentum 30d | bajo | 57 | -2.95 EUR | 4% | 51% |
| momentum 30d | medio | 57 | -4.06 EUR | 2% | 65% |
| momentum 30d | alto | 58 | -3.58 EUR | 3% | 60% |
| fuerza relativa | bajo | 57 | -3.35 EUR | 4% | 60% |
| fuerza relativa | medio | 57 | -3.86 EUR | 0% | 56% |
| fuerza relativa | alto | 58 | -3.39 EUR | 5% | 60% |
| RSI | bajo | 57 | -2.84 EUR | 5% | 53% |
| RSI | medio | 57 | -3.48 EUR | 2% | 58% |
| RSI | alto | 58 | -4.26 EUR | 2% | 66% |
| volumen relativo | bajo | 51 | -3.88 EUR | 4% | 65% |
| volumen relativo | medio | 51 | -2.57 EUR | 0% | 41% |
| volumen relativo | alto | 53 | -4.26 EUR | 4% | 64% |
| volatilidad | bajo | 51 | -4.13 EUR | 0% | 59% |
| volatilidad | medio | 51 | -4.50 EUR | 2% | 63% |
| volatilidad | alto | 53 | -2.16 EUR | 6% | 49% |
| liquidez | bajo | 51 | -3.34 EUR | 2% | 55% |
| liquidez | medio | 51 | -3.88 EUR | 4% | 61% |
| liquidez | alto | 53 | -3.52 EUR | 2% | 55% |
| distancia max 52s | bajo | 51 | -2.53 EUR | 6% | 51% |
| distancia max 52s | medio | 51 | -3.73 EUR | 2% | 59% |
| distancia max 52s | alto | 53 | -4.44 EUR | 0% | 60% |
| consenso | buy | 121 | -3.97 EUR | 2% | 61% |
| consenso | strong_buy | 51 | -2.49 EUR | 4% | 53% |
| tendencia tecnica | alcista | 98 | -3.70 EUR | 3% | 59% |
| tendencia tecnica | mixta | 46 | -2.96 EUR | 2% | 54% |
| tendencia tecnica | bajista | 28 | -3.87 EUR | 4% | 64% |
| tendencia analistas | mejorando | 82 | -3.43 EUR | 4% | 59% |
| tendencia analistas | estable | 53 | -4.50 EUR | 2% | 70% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 97 | -3.45 EUR | 4% | 62% |
| regimen de mercado | neutro | 75 | -3.63 EUR | 1% | 55% |
| catalizador | sin catalizador | 171 | -3.50 EUR | 3% | 58% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -4.13 | -2.16 | **+1.97 EUR** |
| potencial hasta objetivo | -4.09 | -2.70 | **+1.39 EUR** |
| nota global | -3.93 | -2.72 | **+1.21 EUR** |
| % compra fuerte | -4.29 | -3.52 | **+0.77 EUR** |
| fuerza relativa | -3.35 | -3.39 | **-0.04 EUR** |
| liquidez | -3.34 | -3.52 | **-0.19 EUR** |
| volumen relativo | -3.88 | -4.26 | **-0.38 EUR** |
| momentum 30d | -2.95 | -3.58 | **-0.63 EUR** |
| dispersion | -2.30 | -3.47 | **-1.17 EUR** |
| RSI | -2.84 | -4.26 | **-1.42 EUR** |
| puesto en el ranking | -2.67 | -4.23 | **-1.57 EUR** |
| distancia max 52s | -2.53 | -4.44 | **-1.91 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
