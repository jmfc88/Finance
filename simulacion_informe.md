# Simulacion en paralelo

Actualizado: 2026-09-30 18:27 · dia 38 de ejecucion
Proxima revision de ponderacion en 7 dias.

- Operaciones cerradas: **130**
- Operaciones abiertas: 52

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 2% | +16.67 EUR |
| beneficio | 2 | 2% | +7.32 EUR |
| flojo | 40 | 31% | +1.25 EUR |
| plano | 10 | 8% | -1.72 EUR |
| perdida | 47 | 36% | -7.09 EUR |
| nefasta | 29 | 22% | -6.20 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 33 | -2.09% | 1/33 (3%) | 7/33 | 10 |
| 11-20 | 35 | -2.18% | 2/35 (6%) | 3/35 | 9 |
| 21-30 | 62 | -4.62% | 1/62 (2%) | 2/62 | 10 |

**Como leerlo:** si la fila `top` no supera claramente a `media` y
`cola`, el score NO esta ordenando bien y hay que revisar los pesos.

## Por motivo de salida

- **plazo maximo**: 23 operaciones, media -3.09%

## Comparacion de reglas de salida

Todas sobre las MISMAS operaciones y los mismos dias.

| Regla | Total | Media | Aciertos | Peor |
|---|---|---|---|---|
| trailing pegado (3%) | -101.78 EUR | -2.54% | 2/40 | -10.00 EUR |
| arranca despues (+8%) | -116.59 EUR | -3.53% | 3/33 | -10.00 EUR |
| actual (8% / +5% / 5%) | -116.59 EUR | -3.53% | 3/33 | -10.00 EUR |
| arranca antes (+3%) | -130.59 EUR | -3.44% | 3/38 | -10.00 EUR |
| trailing suelto (7%) | -136.35 EUR | -4.26% | 2/32 | -10.00 EUR |
| sin trailing, solo stop | -148.41 EUR | -4.79% | 1/31 | -10.00 EUR |
| LA REAL (escalera 25/08) | -432.00 EUR | -3.32% | 4/130 | -8.08 EUR |
| stop corto (5%) | -482.53 EUR | -5.55% | 3/87 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.32%**
- Aciertos (>= 5 EUR limpios): 4/130 (3%)
- Resultado acumulado ficticio: -432.00 EUR sobre 130 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 43 | -4.36 EUR | 0% | 58% |
| nota global | medio | 43 | -3.46 EUR | 5% | 65% |
| nota global | alto | 44 | -2.17 EUR | 5% | 52% |
| puesto en el ranking | bajo | 43 | -2.09 EUR | 5% | 49% |
| puesto en el ranking | medio | 43 | -3.20 EUR | 5% | 60% |
| puesto en el ranking | alto | 44 | -4.65 EUR | 0% | 66% |
| potencial hasta objetivo | bajo | 43 | -3.98 EUR | 2% | 58% |
| potencial hasta objetivo | medio | 43 | -3.50 EUR | 0% | 63% |
| potencial hasta objetivo | alto | 44 | -2.51 EUR | 7% | 55% |
| dispersion | bajo | 43 | -0.73 EUR | 7% | 37% |
| dispersion | medio | 43 | -5.74 EUR | 0% | 79% |
| dispersion | alto | 44 | -3.49 EUR | 2% | 59% |
| % compra fuerte | bajo | 41 | -4.47 EUR | 2% | 66% |
| % compra fuerte | medio | 41 | -3.41 EUR | 2% | 66% |
| % compra fuerte | alto | 42 | -2.95 EUR | 2% | 50% |
| momentum 30d | bajo | 43 | -3.14 EUR | 5% | 56% |
| momentum 30d | medio | 43 | -3.58 EUR | 2% | 60% |
| momentum 30d | alto | 44 | -3.25 EUR | 2% | 59% |
| fuerza relativa | bajo | 43 | -3.14 EUR | 5% | 60% |
| fuerza relativa | medio | 43 | -3.94 EUR | 0% | 58% |
| fuerza relativa | alto | 44 | -2.90 EUR | 5% | 57% |
| RSI | bajo | 43 | -2.78 EUR | 7% | 56% |
| RSI | medio | 43 | -3.13 EUR | 0% | 56% |
| RSI | alto | 44 | -4.05 EUR | 2% | 64% |
| volumen relativo | bajo | 37 | -3.67 EUR | 5% | 65% |
| volumen relativo | medio | 37 | -3.01 EUR | 0% | 49% |
| volumen relativo | alto | 39 | -3.39 EUR | 3% | 54% |
| volatilidad | bajo | 37 | -3.64 EUR | 0% | 51% |
| volatilidad | medio | 37 | -4.60 EUR | 0% | 68% |
| volatilidad | alto | 39 | -1.92 EUR | 8% | 49% |
| liquidez | bajo | 37 | -2.85 EUR | 3% | 51% |
| liquidez | medio | 37 | -4.09 EUR | 3% | 65% |
| liquidez | alto | 39 | -3.15 EUR | 3% | 51% |
| distancia max 52s | bajo | 37 | -2.59 EUR | 8% | 54% |
| distancia max 52s | medio | 37 | -3.60 EUR | 0% | 59% |
| distancia max 52s | alto | 39 | -3.87 EUR | 0% | 54% |
| consenso | buy | 93 | -4.20 EUR | 2% | 65% |
| consenso | strong_buy | 37 | -1.12 EUR | 5% | 43% |
| tendencia tecnica | alcista | 77 | -3.32 EUR | 3% | 56% |
| tendencia tecnica | mixta | 34 | -2.78 EUR | 3% | 56% |
| tendencia tecnica | bajista | 19 | -4.32 EUR | 5% | 74% |
| tendencia analistas | mejorando | 66 | -3.62 EUR | 3% | 62% |
| tendencia analistas | estable | 41 | -4.23 EUR | 2% | 68% |
| tendencia analistas | empeorando | 5 | -2.63 EUR | 0% | 60% |
| regimen de mercado | favorable | 88 | -3.36 EUR | 3% | 61% |
| regimen de mercado | neutro | 42 | -3.24 EUR | 2% | 52% |
| catalizador | sin catalizador | 129 | -3.29 EUR | 3% | 58% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.36 | -2.17 | **+2.19 EUR** |
| volatilidad | -3.64 | -1.92 | **+1.71 EUR** |
| % compra fuerte | -4.47 | -2.95 | **+1.52 EUR** |
| potencial hasta objetivo | -3.98 | -2.51 | **+1.48 EUR** |
| volumen relativo | -3.67 | -3.39 | **+0.28 EUR** |
| fuerza relativa | -3.14 | -2.90 | **+0.23 EUR** |
| momentum 30d | -3.14 | -3.25 | **-0.12 EUR** |
| liquidez | -2.85 | -3.15 | **-0.30 EUR** |
| RSI | -2.78 | -4.05 | **-1.28 EUR** |
| distancia max 52s | -2.59 | -3.87 | **-1.28 EUR** |
| puesto en el ranking | -2.09 | -4.65 | **-2.56 EUR** |
| dispersion | -0.73 | -3.49 | **-2.76 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
