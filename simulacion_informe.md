# Simulacion en paralelo

Actualizado: 2026-10-07 23:05 · dia 45 de ejecucion
**Revision nº3 disponible.** Pega este informe en el chat para decidir la ponderacion.

- Operaciones cerradas: **161**
- Operaciones abiertas: 56

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 1% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 49 | 30% | +1.26 EUR |
| plano | 12 | 7% | -1.75 EUR |
| perdida | 61 | 38% | -7.23 EUR |
| nefasta | 34 | 21% | -6.48 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 41 | -2.24% | 2/41 (5%) | 8/41 | 9 |
| 11-20 | 44 | -3.04% | 2/44 (5%) | 3/44 | 9 |
| 21-30 | 76 | -4.48% | 1/76 (1%) | 3/76 | 10 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 28 operaciones, media -3.35%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -146.37 EUR | -2.87% | 3/51 | -10.00 EUR |
| arranca despues (+8%) | -166.10 EUR | -3.95% | 3/42 | -10.00 EUR |
| actual (8% / +5% / 5%) | -166.10 EUR | -3.95% | 3/42 | -10.00 EUR |
| arranca antes (+3%) | -180.10 EUR | -3.83% | 3/47 | -10.00 EUR |
| trailing suelto (7%) | -189.24 EUR | -4.73% | 2/40 | -10.00 EUR |
| sin trailing, solo stop | -201.30 EUR | -5.16% | 1/39 | -10.00 EUR |
| LA REAL (escalera 25/08) | -566.08 EUR | -3.52% | 5/161 | -8.08 EUR |
| stop corto (5%) | -614.14 EUR | -5.63% | 3/109 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.52%**
- Aciertos (>= 5 EUR limpios): 5/161 (3%)
- Resultado acumulado ficticio: -566.08 EUR sobre 161 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 53 | -4.33 EUR | 0% | 58% |
| nota global | medio | 53 | -3.66 EUR | 4% | 64% |
| nota global | alto | 55 | -2.59 EUR | 5% | 55% |
| puesto en el ranking | bajo | 53 | -2.43 EUR | 6% | 51% |
| puesto en el ranking | medio | 53 | -3.58 EUR | 4% | 62% |
| puesto en el ranking | alto | 55 | -4.50 EUR | 0% | 64% |
| potencial hasta objetivo | bajo | 53 | -4.06 EUR | 4% | 58% |
| potencial hasta objetivo | medio | 53 | -3.67 EUR | 0% | 62% |
| potencial hasta objetivo | alto | 55 | -2.84 EUR | 5% | 56% |
| dispersion | bajo | 53 | -2.03 EUR | 6% | 47% |
| dispersion | medio | 53 | -5.14 EUR | 2% | 74% |
| dispersion | alto | 55 | -3.38 EUR | 2% | 56% |
| % compra fuerte | bajo | 50 | -4.58 EUR | 2% | 66% |
| % compra fuerte | medio | 50 | -2.89 EUR | 2% | 58% |
| % compra fuerte | alto | 52 | -3.52 EUR | 4% | 56% |
| momentum 30d | bajo | 53 | -2.91 EUR | 4% | 51% |
| momentum 30d | medio | 53 | -4.27 EUR | 2% | 68% |
| momentum 30d | alto | 55 | -3.38 EUR | 4% | 58% |
| fuerza relativa | bajo | 53 | -3.33 EUR | 4% | 60% |
| fuerza relativa | medio | 53 | -3.93 EUR | 0% | 57% |
| fuerza relativa | alto | 55 | -3.30 EUR | 5% | 60% |
| RSI | bajo | 53 | -2.96 EUR | 6% | 55% |
| RSI | medio | 53 | -3.30 EUR | 2% | 57% |
| RSI | alto | 55 | -4.26 EUR | 2% | 65% |
| volumen relativo | bajo | 48 | -3.86 EUR | 4% | 67% |
| volumen relativo | medio | 48 | -2.93 EUR | 0% | 44% |
| volumen relativo | alto | 48 | -3.91 EUR | 4% | 60% |
| volatilidad | bajo | 48 | -3.94 EUR | 0% | 56% |
| volatilidad | medio | 48 | -4.84 EUR | 2% | 67% |
| volatilidad | alto | 48 | -1.92 EUR | 6% | 48% |
| liquidez | bajo | 48 | -3.65 EUR | 2% | 58% |
| liquidez | medio | 48 | -3.63 EUR | 4% | 60% |
| liquidez | alto | 48 | -3.43 EUR | 2% | 52% |
| distancia max 52s | bajo | 48 | -2.62 EUR | 6% | 52% |
| distancia max 52s | medio | 48 | -3.84 EUR | 2% | 60% |
| distancia max 52s | alto | 48 | -4.25 EUR | 0% | 58% |
| consenso | buy | 115 | -4.09 EUR | 3% | 63% |
| consenso | strong_buy | 46 | -2.08 EUR | 4% | 50% |
| tendencia tecnica | alcista | 94 | -3.61 EUR | 3% | 59% |
| tendencia tecnica | mixta | 41 | -2.84 EUR | 2% | 54% |
| tendencia tecnica | bajista | 26 | -4.25 EUR | 4% | 69% |
| tendencia analistas | mejorando | 78 | -3.46 EUR | 4% | 59% |
| tendencia analistas | estable | 50 | -4.47 EUR | 2% | 70% |
| tendencia analistas | empeorando | 8 | -4.67 EUR | 0% | 75% |
| regimen de mercado | favorable | 95 | -3.45 EUR | 4% | 62% |
| regimen de mercado | neutro | 66 | -3.61 EUR | 2% | 55% |
| catalizador | sin catalizador | 160 | -3.49 EUR | 3% | 59% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| volatilidad | -3.94 | -1.92 | **+2.02 EUR** |
| nota global | -4.33 | -2.59 | **+1.74 EUR** |
| potencial hasta objetivo | -4.06 | -2.84 | **+1.21 EUR** |
| % compra fuerte | -4.58 | -3.52 | **+1.06 EUR** |
| liquidez | -3.65 | -3.43 | **+0.22 EUR** |
| fuerza relativa | -3.33 | -3.30 | **+0.03 EUR** |
| volumen relativo | -3.86 | -3.91 | **-0.05 EUR** |
| momentum 30d | -2.91 | -3.38 | **-0.47 EUR** |
| RSI | -2.96 | -4.26 | **-1.31 EUR** |
| dispersion | -2.03 | -3.38 | **-1.35 EUR** |
| distancia max 52s | -2.62 | -4.25 | **-1.63 EUR** |
| puesto en el ranking | -2.43 | -4.50 | **-2.07 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
