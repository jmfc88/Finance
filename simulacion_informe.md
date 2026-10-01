# Simulacion en paralelo

Actualizado: 2026-10-01 07:18 · dia 39 de ejecucion
Proxima revision de ponderacion en 6 dias.

- Operaciones cerradas: **131**
- Operaciones abiertas: 51

## Como acabaron

| Estado | Ops | % del total | Media |
|---|---|---|---|
| top | 2 | 2% | +16.67 EUR |
| beneficio | 3 | 2% | +7.07 EUR |
| flojo | 40 | 31% | +1.25 EUR |
| plano | 10 | 8% | -1.72 EUR |
| perdida | 47 | 36% | -7.09 EUR |
| nefasta | 29 | 22% | -6.20 EUR |

## Por tramo del ranking

| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |
|---|---|---|---|---|---|
| 1-10 | 34 | -1.83% | 2/34 (6%) | 8/34 | 10 |
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
| trailing pegado (3%) | -99.55 EUR | -2.43% | 2/41 | -10.00 EUR |
| arranca despues (+8%) | -116.59 EUR | -3.53% | 3/33 | -10.00 EUR |
| actual (8% / +5% / 5%) | -116.59 EUR | -3.53% | 3/33 | -10.00 EUR |
| arranca antes (+3%) | -130.59 EUR | -3.44% | 3/38 | -10.00 EUR |
| trailing suelto (7%) | -136.35 EUR | -4.26% | 2/32 | -10.00 EUR |
| sin trailing, solo stop | -148.41 EUR | -4.79% | 1/31 | -10.00 EUR |
| LA REAL (escalera 25/08) | -425.44 EUR | -3.25% | 5/131 | -8.08 EUR |
| stop corto (5%) | -482.53 EUR | -5.55% | 3/87 | -7.00 EUR |

**Como leerlo:** la de arriba es la que mas habria ganado con tus
propias candidatas. Mira tambien la columna `Peor`: una regla que gana
mas pero con perdidas maximas muy grandes puede no compensar.

## Conjunto

- Media neta: **-3.25%**
- Aciertos (>= 5 EUR limpios): 5/131 (4%)
- Resultado acumulado ficticio: -425.44 EUR sobre 131 x 100 EUR

## Analisis por factor

Cada factor se parte en tres grupos segun su valor y se compara como
acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no
predice; si va peor, esta restando.

| Factor | Grupo | Ops | Media | Buenas | Malas |
|---|---|---|---|---|---|
| nota global | bajo | 43 | -4.36 EUR | 0% | 58% |
| nota global | medio | 43 | -3.46 EUR | 5% | 65% |
| nota global | alto | 45 | -1.98 EUR | 7% | 51% |
| puesto en el ranking | bajo | 43 | -1.75 EUR | 7% | 47% |
| puesto en el ranking | medio | 43 | -3.28 EUR | 5% | 60% |
| puesto en el ranking | alto | 45 | -4.65 EUR | 0% | 67% |
| potencial hasta objetivo | bajo | 43 | -3.69 EUR | 5% | 56% |
| potencial hasta objetivo | medio | 43 | -3.66 EUR | 0% | 65% |
| potencial hasta objetivo | alto | 45 | -2.43 EUR | 7% | 53% |
| dispersion | bajo | 43 | -0.73 EUR | 7% | 37% |
| dispersion | medio | 43 | -5.40 EUR | 2% | 77% |
| dispersion | alto | 45 | -3.59 EUR | 2% | 60% |
| % compra fuerte | bajo | 41 | -4.47 EUR | 2% | 66% |
| % compra fuerte | medio | 41 | -3.41 EUR | 2% | 66% |
| % compra fuerte | alto | 43 | -2.73 EUR | 5% | 49% |
| momentum 30d | bajo | 43 | -3.14 EUR | 5% | 56% |
| momentum 30d | medio | 43 | -3.58 EUR | 2% | 60% |
| momentum 30d | alto | 45 | -3.03 EUR | 4% | 58% |
| fuerza relativa | bajo | 43 | -3.14 EUR | 5% | 60% |
| fuerza relativa | medio | 43 | -3.94 EUR | 0% | 58% |
| fuerza relativa | alto | 45 | -2.69 EUR | 7% | 56% |
| RSI | bajo | 43 | -2.78 EUR | 7% | 56% |
| RSI | medio | 43 | -3.00 EUR | 2% | 56% |
| RSI | alto | 45 | -3.94 EUR | 2% | 62% |
| volumen relativo | bajo | 38 | -3.71 EUR | 5% | 66% |
| volumen relativo | medio | 38 | -2.99 EUR | 0% | 47% |
| volumen relativo | alto | 38 | -3.12 EUR | 5% | 53% |
| volatilidad | bajo | 38 | -3.56 EUR | 0% | 50% |
| volatilidad | medio | 38 | -4.37 EUR | 3% | 68% |
| volatilidad | alto | 38 | -1.89 EUR | 8% | 47% |
| liquidez | bajo | 38 | -2.99 EUR | 3% | 53% |
| liquidez | medio | 38 | -3.57 EUR | 5% | 61% |
| liquidez | alto | 38 | -3.26 EUR | 3% | 53% |
| distancia max 52s | bajo | 38 | -2.73 EUR | 8% | 55% |
| distancia max 52s | medio | 38 | -3.72 EUR | 0% | 61% |
| distancia max 52s | alto | 38 | -3.37 EUR | 3% | 50% |
| consenso | buy | 94 | -4.09 EUR | 3% | 64% |
| consenso | strong_buy | 37 | -1.12 EUR | 5% | 43% |
| tendencia tecnica | alcista | 78 | -3.19 EUR | 4% | 55% |
| tendencia tecnica | mixta | 34 | -2.78 EUR | 3% | 56% |
| tendencia tecnica | bajista | 19 | -4.32 EUR | 5% | 74% |
| tendencia analistas | mejorando | 67 | -3.47 EUR | 4% | 61% |
| tendencia analistas | estable | 41 | -4.23 EUR | 2% | 68% |
| tendencia analistas | empeorando | 5 | -2.63 EUR | 0% | 60% |
| regimen de mercado | favorable | 89 | -3.25 EUR | 4% | 61% |
| regimen de mercado | neutro | 42 | -3.24 EUR | 2% | 52% |
| catalizador | sin catalizador | 130 | -3.21 EUR | 4% | 58% |

### Que factor separa mas

Diferencia entre el grupo alto y el bajo. Positivo = mas valor
es mejor. Negativo = el factor esta al reves y penaliza acertar.

| Factor | Bajo | Alto | Diferencia |
|---|---|---|---|
| nota global | -4.36 | -1.98 | **+2.38 EUR** |
| % compra fuerte | -4.47 | -2.73 | **+1.74 EUR** |
| volatilidad | -3.56 | -1.89 | **+1.67 EUR** |
| potencial hasta objetivo | -3.69 | -2.43 | **+1.26 EUR** |
| volumen relativo | -3.71 | -3.12 | **+0.58 EUR** |
| fuerza relativa | -3.14 | -2.69 | **+0.45 EUR** |
| momentum 30d | -3.14 | -3.03 | **+0.10 EUR** |
| liquidez | -2.99 | -3.26 | **-0.27 EUR** |
| distancia max 52s | -2.73 | -3.37 | **-0.64 EUR** |
| RSI | -2.78 | -3.94 | **-1.16 EUR** |
| dispersion | -0.73 | -3.59 | **-2.86 EUR** |
| puesto en el ranking | -1.75 | -4.65 | **-2.90 EUR** |

Los de arriba merecen MAS peso; los de abajo, menos o al reves.
