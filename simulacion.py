"""
VERSION: 12 (31/08/2026) - la regla POR DEFECTO pasa a ser la escalera real.
En la v11 se anadio como variante de comparacion, pero el bucle principal
seguia usando el trailing continuo que se elimino del bot el 25/08: las
operaciones abiertas se evaluaban con reglas que ya no existen.

VERSION: 11 (26/08/2026) - la simulacion mide por fin las reglas REALES.
Hasta ahora comparaba variantes de trailing continuo, que es lo que hacia el
bot antes del 25/08. Ese dia se quito el trailing y se puso la escalera de
avisos que diseño Jose Manuel en papel, asi que la simulacion estaba midiendo
un sistema que ya no existe. Se anade "LA REAL (escalera 25/08)" como primera
variante; las demas se quedan como comparacion.

VERSION: 10 (23/08/2026) - INFORME DE PONDERACION. Cada 15 dias Jose Manuel
pega el informe en el chat para decidir que pesos cambiar. Para eso hacia
falta algo que el informe anterior no tenia: el analisis FACTOR POR FACTOR.

Lo que hace: por cada factor del score (potencial, dispersion, momentum,
fuerza relativa, RSI, volumen, volatilidad, liquidez, distancia al maximo,
consenso, catalizador...) parte las operaciones cerradas en tres grupos
segun el valor que tenia ese factor, y compara como acabaron. Si el grupo
"alto" no va mejor que el "bajo", ese factor no esta prediciendo nada por
mucho que pese 16 puntos. Y si va PEOR, esta restando en vez de sumar.

Tambien marca la revision (nº1, nº2...) contando desde la primera operacion,
para que quede claro cada cuanto toca mirarlo.

El informe esta pensado para caber en un mensaje: tablas cortas, sin adornos.

VERSION: 9 (23/08/2026) - el diseño completo que describio Jose Manuel.
Cinco cambios sobre la v8:

(1) LAS 30 CANDIDATAS del cuaderno, no 9 repartidas en tres franjas. El tramo
    del ranking (1-10, 11-20, 21-30) se deduce de la posicion, asi que la
    comparacion entre tramos se conserva y ademas se triplica la muestra.

(2) 20 DIAS de plazo maximo en vez de 30.

(3) LA TARJETA ENTERA se copia dentro de la operacion y NO SE BORRA NUNCA.
    historial_tarjetas.json tiene ventana de 5 dias, asi que dentro de tres
    meses ya no existiria la tarjeta que motivo una entrada de hoy — y esa
    tarjeta es justo lo que hay que cruzar con el resultado para saber que
    factores puntuan bien.

(4) ESTADO DE RESULTADO en palabras, no solo un numero:
      nefasta   - salto el stop en 5 sesiones o menos: la entrada estaba mal
                  desde el principio, la recomendacion fallo de raiz
      perdida   - salto el stop mas tarde: la tesis tardo en romperse
      plano     - llego a los 20 dias sin moverse. NO es neutro: con 2 EUR de
                  comisiones sobre 100, estar plano es perder
      flojo     - acaba en positivo pero por debajo de los 5 EUR limpios
      beneficio - 5 EUR limpios o mas
      top       - 15 EUR limpios o mas
    Distinguir "nefasta" de "perdida" importa: si una candidata con nota alta
    sale nefasta, el problema es el scoring; si sale perdida, puede ser
    simplemente que el mercado se giro.

(5) Se guarda tambien cuantas sesiones aguanto y si llego a armar el trailing.

VERSION: 8 (23/08/2026) - participaciones en vez de acciones enteras. Antes
se exigia poder comprar al menos 1 accion entera con 100 EUR, igual que en la
operativa real, y eso dejaba fuera TODO lo que costara mas de 100 EUR por
accion: en la primera ejecucion se cayeron AI.PA (167), ANET (188) y DG.PA
(119), y la franja media se quedo con UNA sola operacion.

Ese filtro sesgaba la muestra hacia los valores baratos justo cuando lo que
se quiere medir es el ranking entero. Y no hace falta: la simulacion no tiene
que ser ejecutable, tiene que medir si el score predice la direccion del
precio. Ahora invierte 100 EUR exactos en cada candidata, con participaciones
fraccionadas, y ninguna se queda fuera por precio.

La operativa REAL sigue siendo de acciones enteras. Esto es solo el banco de
pruebas.

VERSION: 7 (23/08/2026) - guarda tambien los cuatro factores mas pesados del
score que faltaban: potencial hasta el objetivo, dispersion, consenso real y
tendencia de analistas. Sin ellos el historico podria decir SI el score
ordena bien, pero no QUE factor falla — y esa es justo la pregunta que Jose
Manuel quiere que respondan los datos en vez de mi opinion. Con esto, cuando
haya unas decenas de operaciones cerradas se podra cruzar cada factor por
separado contra el resultado real.

VERSION: 6 (23/08/2026) - VARIANTES EN PARALELO. Jose Manuel pregunto cuanto
conviene subir el stop cuando empieza a ganar. En vez de contestar con una
opinion, cada operacion se evalua con VARIAS reglas a la vez sobre exactamente
las mismas candidatas y los mismos dias. Al cabo de unas semanas el informe
dira cual gana con SUS datos, no con una regla general de internet.

Las variantes se diferencian en tres cosas: el stop inicial, cuanta subida
hace falta para que el trailing arranque, y cuanto sigue al precio despues.
La "actual" es la que reproduce su tabla dibujada a mano.

Coste: cero peticiones extra. El historico de cada operacion se descarga UNA
vez y se reconstruye tantas veces como variantes haya.

VERSION: 5 (23/08/2026) - regla afinada con la tabla de cuatro casos que
dibujo Jose Manuel a mano, con el stop apuntado dia a dia.

Lo que enseña esa tabla y ninguna version anterior hacia bien:

  El stop NO sube de forma continua. Arranca en -8% y se queda ahi QUIETO
  hasta que el precio llega al +5%. Solo a partir de ese momento empieza a
  seguir al precio, un 5% por debajo.

Lo demuestra su "Accion 2": sube hasta 104 (+4%) y el stop sigue en 92; luego
cae y vende a 92. Con un trailing continuo el stop habria subido a 95,7 y la
perdida habria sido menor — pero eso NO es lo que hace el.

Su "Accion 4" da el patron del tramo activo: precio 105 -> stop 98; 110 ->
105; 114 -> 108; 125 -> 119. Es un 5% por debajo del maximo alcanzado.

OJO, discrepancia con bot.py: el bot usa un trailing del 8% activo desde el
primer dia. La operativa real de Jose Manuel es un 5% activado a partir del
+5%. Son reglas distintas y aqui se simula LA SUYA, que es la que ejecuta a
mano en Trade Republic; el bot solo manda avisos.

VERSION: 4 (23/08/2026) - LA REGLA CORRECTA, explicada por Jose Manuel de
viva voz. Yo la habia entendido mal dos veces seguidas.

Lo que hace de verdad: compra a 100. Si el dia 1 cae a 97, mantiene (el stop
inicial esta muy por debajo). Cuando se pone en 105, o sea en verde, NO deja
el stop abajo: lo SUBE A SU PRECIO DE COMPRA. Su razon, literal: "yo ya no
pierdo dinero". Y de ahi en adelante lo va subiendo segun sube el precio.

Mi error en las v2 y v3: clavar el stop en el nivel de los 5 EUR limpios.
Los 5 EUR NO son un nivel de stop, son su medida de si la operacion merecio
la pena. Confundir las dos cosas hacia que toda operacion cerrara en +5,00
exactos y se perdiera cualquier recorrido largo.

Con la regla correcta, su ejemplo dibujado (100 -> 110 -> baja a 105 -> 120)
sale como el decia: la posicion aguanta la bajada y llega viva a 120.

VERSION: 3 (23/08/2026) - el suelo lleva HOLGURA y sube por escalones, segun
el ejemplo dibujado a mano por Jose Manuel:

  dia 1: compra a 100
  dia 2: 103 -> mantengo        dia 3: 110 -> stop en 105
  dia 10: 106  dia 15: 105  -> "la posicion se mantiene"
  dia 30: 120

Lo que ensena ese ejemplo y yo tenia mal en la v2: el stop NO se pone pegado
al objetivo. Con el pico en 110 el stop va a 105, cinco euros por debajo. Por
eso la caida hasta 105-106 no le saca, y la posicion llega viva a 120. Con el
suelo pegado (la v2) esa misma operacion cerraba el dia 8 con +5 EUR y se
perdia todo el recorrido hasta 120.

Ahora el suelo: (a) se arma al alcanzar el objetivo, (b) se coloca con una
holgura por debajo del maximo alcanzado, y (c) sube cuando el precio hace
maximos nuevos, nunca baja.

VERSION: 2 (23/08/2026) - corrige la regla de salida con la mecanica REAL de
Jose Manuel, que no era la que yo habia programado en la v1.

Lo que yo habia entendido mal: que el 7% era un numero fijo y que habia que
esperar semanas para saber el resultado.

Lo que hace de verdad: el umbral no es un porcentaje, son 5 EUR LIMPIOS. En
cuanto la operacion puede dejar esos 5 EUR ya limpios de comisiones, pone un
stop-loss que los GARANTIZA. A partir de ahi ya no puede acabar en perdida.
Si sigue subiendo, no vende: sube el stop para capturar mas. Y si el mismo
dia de la compra ya da esos 5 EUR, ese dia ya cuenta — no hay que esperar.

Consecuencia importante del cambio: como 5 EUR son un importe ABSOLUTO, el
liston en porcentaje depende del capital. Sobre 100 EUR hacen falta +7%
brutos; sobre 500 EUR bastan +1,4%. Esta simulacion a 100 EUR es por tanto
la version MAS EXIGENTE de la regla, no la mas comoda.

VERSION: 1 (23/08/2026) - SIMULACION EN PARALELO (papel, sin dinero real).

QUE ES: un programa independiente que hace lo que Jose Manuel describio —
"imagina que invierto 100 EUR en esta accion que me recomendaste, que
hubiera pasado". Abre operaciones ficticias a partir de las tarjetas del
cuaderno, las sigue con LAS MISMAS REGLAS de stop-loss del bot real, y
apunta como acabaron.

POR QUE HACE FALTA: con 1-4 posiciones reales y semanas de mantenimiento
salen unas 15-25 operaciones al ano. Para distinguir un sistema que
funciona de la suerte hacen falta cientos. Por la via de las compras
reales no se llega nunca. Por esta via salen decenas al mes.

LA PREGUNTA QUE RESPONDE, y es la que importa: ¿una candidata con score
alto acaba mejor que una con score medio? Si la respuesta es que no, hay
factores que sobran o que estan mal pesados, y esto lo dira con numeros
en vez de con opiniones.

POR ESO NO SOLO SIMULA EL TOP. Abre operaciones en TRES FRANJAS del
ranking (top, media y cola). Si solo simulara las mejores se sabria si el
top funciona, pero NO si el score sirve para ordenar — que es justo lo
que hay que averiguar para mejorar los pesos.

NO NECESITA EJECUTARSE A DIARIO. En vez de ir mirando el precio cada dia
y arriesgarse a perder dias si falla una ejecucion, cada vez que corre se
descarga el historico diario completo desde la fecha de entrada y
reconstruye sesion a sesion lo que HABRIA pasado. Da igual que pasen dias
sin ejecutarse: el resultado es identico.

NO TOCA NADA DEL SISTEMA REAL. Ni ledger.json, ni posiciones.json, ni el
bot. Escribe solo en simulacion_operaciones.json y simulacion_informe.md.
"""

import json
import time
from datetime import datetime, timedelta

import yfinance as yf

RANKING = "candidatos_rankeados.json"
OPERACIONES = "simulacion_operaciones.json"
INFORME = "simulacion_informe.md"

CAPITAL_POR_OPERACION = 100.0   # euros ficticios, como lo planteo Jose Manuel
COMISION_COMPRA = 1.0
COMISION_VENTA = 1.0

# Se simulan TODAS las candidatas del cuaderno. El tramo (1-10, 11-20, 21-30)
# se deduce de la posicion, y comparar los tramos entre si es lo que dira si
# el score de verdad ordena bien.
TOP_N_SIMULACION = 30   # se simulan TODAS las candidatas del cuaderno

# El tramo se deduce de la posicion, no hace falta elegir puestos sueltos.
def tramo_de(posicion):
    if posicion <= 10:
        return "1-10"
    if posicion <= 20:
        return "11-20"
    return "21-30"

# Umbrales de los estados, en euros limpios sobre los 100 invertidos.
UMBRAL_TOP = 15.0
UMBRAL_BENEFICIO = 5.0
SESIONES_NEFASTA = 5    # stop-loss en 5 sesiones o menos = entrada mal elegida
PLANO_MARGEN = 3.0      # +-3 EUR alrededor de cero se considera plano

# Reglas de salida: las MISMAS que bot.py, para que esto mida el sistema
# real y no un sistema parecido.
# Stop inicial: -8% sobre el PRECIO de entrada. Es el 92 que aparece en la
# columna del dia 1 de las cuatro acciones de la tabla dibujada. Coincide
# ademas con el efecto real de bot.py, cuyo trailing del 8% arranca desde el
# precio de compra y por tanto manda desde el primer dia sobre el calculo
# del -12,5% del capital (que daria 89,5 y nunca llega a aplicarse).
STOP_INICIAL_PCT = 8.0

# Variantes que compiten entre si. "actual" es la regla real de Jose Manuel,
# reconstruida a partir de su tabla; las demas cambian UNA cosa cada vez para
# que la comparacion diga algo. La pregunta que responden: ¿conviene subir el
# stop antes o despues, y pegado o suelto?
# NIVELES_ESCALERA: la operativa real, la que se diseño el 25/08 con Jose
# Manuel a base de dibujos en papel. Cada pareja es (ganancia alcanzada,
# ganancia que se asegura subiendo el stop). El hueco de 3,5 puntos lo eligio
# el: deja sitio para el vaiven normal del dia sin renunciar a lo ganado.
NIVELES_ESCALERA = [(7, 3.5), (10, 6.5), (12.5, 9.0), (15, 11.5),
                    (20, 16.5), (25, 21.5), (30, 26.5)]
# Al cruzar el equilibrio + este margen, el stop sube al precio que deja 1 EUR
# limpio. Es el aviso de [COMIENZAN GANANCIAS].
MARGEN_GANANCIAS_PCT = 2.0

VARIANTES = [
    {"nombre": "LA REAL (escalera 25/08)", "tipo": "escalera", "stop": 8.0},
    {"nombre": "actual (8% / +5% / 5%)",   "stop": 8.0, "activacion": 5.0, "trailing": 5.0},
    {"nombre": "trailing suelto (7%)",     "stop": 8.0, "activacion": 5.0, "trailing": 7.0},
    {"nombre": "trailing pegado (3%)",     "stop": 8.0, "activacion": 5.0, "trailing": 3.0},
    {"nombre": "arranca antes (+3%)",      "stop": 8.0, "activacion": 3.0, "trailing": 5.0},
    {"nombre": "arranca despues (+8%)",    "stop": 8.0, "activacion": 8.0, "trailing": 5.0},
    {"nombre": "stop corto (5%)",          "stop": 5.0, "activacion": 5.0, "trailing": 5.0},
    {"nombre": "sin trailing, solo stop",  "stop": 8.0, "activacion": 999.0, "trailing": 5.0},
]
# El trailing NO se activa hasta que el precio alcanza ACTIVACION_TRAILING_PCT.
# Antes de eso manda el stop inicial y no se mueve. Asi lo hace Jose Manuel.
TRAILING_PCT = 5.0            # % por debajo del maximo, una vez activado
ACTIVACION_TRAILING_PCT = 5.0 # subida necesaria para que el trailing arranque
ESCALON_PCT = 0.05        # metodo 2: escalones de +5% desde el punto de equilibrio

DIAS_MAXIMO = 20          # si no salta el stop, se cierra y se apunta igual
DIAS_REVISION = 7         # foto intermedia a los 7 dias

# El listón real: 5 EUR limpios en el bolsillo, comisiones ya descontadas.
# Es un importe absoluto a proposito, no un porcentaje: es como decide de
# verdad Jose Manuel. Sobre 100 EUR equivale a +7% bruto; sobre 500 EUR, a
# +1,4%. Cambiar CAPITAL_POR_OPERACION cambia por tanto la dificultad.
OBJETIVO_LIMPIO_EUR = 5.0

# OJO: OBJETIVO_LIMPIO_EUR NO es un nivel de stop. Es solo el liston para
# contar una operacion como acierto en el informe. El stop se rige por el
# punto de equilibrio y el trailing, mas abajo.


def cargar(ruta, defecto):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return defecto


def guardar(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=2, ensure_ascii=False, allow_nan=False)

def tarjeta_completa(c):
    """La tarjeta tal y como la vio Jose Manuel, copiada ENTERA y para
    siempre dentro de la operacion. historial_tarjetas.json solo guarda 5
    dias, asi que sin esta copia la tarjeta que motivo una entrada de hoy no
    existiria dentro de tres meses — y es justo lo que hay que cruzar con el
    resultado para saber que factores puntuan bien y cuales sobran."""
    campos = [
        "ticker", "nombre_empresa", "isin", "sector", "score", "version_scoring",
        "precio_actual", "consenso", "consenso_real", "precio_objetivo_medio",
        "dispersion_pct", "momentum_30d_pct", "momentum_5d_pct", "fuerza_relativa_pct",
        "regimen_mercado", "indice_referencia", "rsi_14", "tendencia_tecnica",
        "sma50", "sma200", "tendencia_analistas", "catalizador_resultados",
        "cotiza_en_euros", "liquidez_dia", "volumen_relativo", "volatilidad_diaria_pct",
        "sesiones_hasta_stop", "distancia_max_52s_pct", "metodo_datos",
        "noticias", "profundizacion", "resumen_negocio",
    ]
    return {k: c.get(k) for k in campos}


def abrir_operaciones(ranking, operaciones):
    """Abre una operacion ficticia de 100 EUR sobre CADA UNA de las 30
    candidatas del cuaderno.

    No se abre una segunda sobre un ticker que ya esta abierto: una candidata
    puede quedarse una semana en el top y contarla siete veces daria siete
    resultados casi identicos, inflando la muestra hacia lo que mas se repite
    en vez de hacia lo que mejor funciona."""
    abiertos = {o["ticker"] for o in operaciones if o["estado"] == "abierta"}
    hoy = datetime.now().strftime("%Y-%m-%d")
    nuevas = 0

    for posicion, c in enumerate(ranking[:TOP_N_SIMULACION], start=1):
        ticker = c.get("ticker")
        precio = c.get("precio_actual")
        if not ticker or not precio or precio <= 0 or ticker in abiertos:
            continue

        abiertos.add(ticker)
        acciones = round(CAPITAL_POR_OPERACION / precio, 6)
        pot = (round((c["precio_objetivo_medio"] / precio - 1) * 100, 1)
               if c.get("precio_objetivo_medio") else None)

        operaciones.append({
            "id": f"{ticker}-{hoy}",
            "ticker": ticker,
            "nombre": c.get("nombre_empresa"),
            "estado": "abierta",
            "fecha_entrada": hoy,
            "precio_entrada": precio,
            "acciones": acciones,
            "invertido": round(precio * acciones, 2),
            "posicion_ranking": posicion,
            "tramo": tramo_de(posicion),
            "score": c.get("score"),
            "potencial_pct": pot,
            # La tarjeta entera, permanente
            "tarjeta": tarjeta_completa(c),
        })
        nuevas += 1

    return nuevas

def descargar_historico(op):
    """Una sola descarga por operacion, reutilizada por todas las variantes."""
    entrada = datetime.strptime(op["fecha_entrada"], "%Y-%m-%d")
    try:
        hist = yf.Ticker(op["ticker"]).history(
            start=(entrada + timedelta(days=1)).strftime("%Y-%m-%d"),
            end=(datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
        )
    except Exception:
        return None
    if hist is None or len(hist) == 0 or "Close" not in hist.columns:
        return None
    hist = hist[hist["Close"].notna()]
    return hist if len(hist) else None


def reconstruir(op, hist=None, regla=None):
    """Reconstruye sesion a sesion lo que habria pasado desde la entrada,
    aplicando las reglas del bot real. Devuelve el resultado o None si
    sigue abierta.

    Se hace asi, y no mirando solo el precio de hoy, porque el stop-loss
    depende del CAMINO: una accion puede estar hoy en +3% habiendo pasado
    por un -14% la semana pasada, y en la operativa real esa posicion ya
    estaria cerrada. Mirar solo el precio final daria un resultado que
    nunca habria ocurrido."""
    # La regla POR DEFECTO es la escalera real, la que manda bot.py: stop del
    # -8%, al cruzar el equilibrio +2% se asegura 1 EUR, y en cada escalon de
    # ganancia el stop sube para asegurar 3,5 puntos menos.
    #
    # Estaba puesto el trailing continuo, que es lo que hacia el bot ANTES del
    # 25/08 y que ese dia se quito por completo. Resultado: las 45 operaciones
    # abiertas se estaban evaluando con unas reglas que ya no existen, y la
    # escalera solo aparecia como una variante mas de comparacion. La
    # simulacion no estaba midiendo el sistema real.
    regla = regla or {"tipo": "escalera", "stop": STOP_INICIAL_PCT}
    entrada = datetime.strptime(op["fecha_entrada"], "%Y-%m-%d")
    if hist is not None:
        return _recorrer(op, hist, regla)
    try:
        hist = yf.Ticker(op["ticker"]).history(
            start=(entrada + timedelta(days=1)).strftime("%Y-%m-%d"),
            end=(datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),
        )
    except Exception:
        return None
    if hist is None or len(hist) == 0 or "Close" not in hist.columns:
        return None
    hist = hist[hist["Close"].notna()]
    if len(hist) == 0:
        return None
    return _recorrer(op, hist, regla)
def _recorrer_escalera(op, hist, regla):
    """La operativa REAL, la que manda bot.py desde la v22.

    El stop empieza en el -8% SOBRE LO INVERTIDO (comisiones dentro, no sobre
    el precio a secas: no es lo mismo, y era un fallo que se corrigio el 25/08).
    A partir de ahi solo sube, y sube en los momentos exactos en que el bot
    manda un aviso:

      - al cruzar el equilibrio + 2%  -> stop al precio que deja 1 EUR limpio
      - al 7% de ganancia             -> stop al precio que asegura el 3,5%
      - al 10%                        -> asegura el 6,5%
      - ... y asi por NIVELES_ESCALERA

    Aqui no hay trailing continuo ni escalones automaticos: se quitaron del bot
    el 25/08 porque movian el stop por su cuenta y disparaban [VENDE] estando
    en ganancias. Esta funcion replica lo que Jose Manuel hace de verdad con el
    movil en la mano, que es lo unico que tiene sentido medir.
    """
    pe = op["precio_entrada"]
    acciones = op["acciones"]
    comisiones = COMISION_COMPRA + COMISION_VENTA
    invertido = pe * acciones + COMISION_COMPRA

    precio_equilibrio = pe + (comisiones / acciones)
    nivel_ganancias = precio_equilibrio * (1 + MARGEN_GANANCIAS_PCT / 100)

    def precio_para(ganancia_pct):
        """Precio al que la operacion deja esa ganancia neta sobre lo invertido."""
        return (invertido * (1 + ganancia_pct / 100) + COMISION_VENTA) / acciones

    # -8% sobre lo invertido, no sobre el precio
    stop = round((invertido * (1 - regla["stop"] / 100) + COMISION_VENTA) / acciones, 4)
    stop_inicial = stop

    precio_objetivo = pe + (OBJETIVO_LIMPIO_EUR + comisiones) / acciones
    maximo = pe
    precio_7d = None
    llego_5eur = False
    sesiones_hasta_armar = None
    ganancias_armadas = False
    niveles_hechos = set()

    for i, (fecha, cierre) in enumerate(hist, start=1):
        if cierre is None:
            continue
        maximo = max(maximo, cierre)
        if i == 7:
            precio_7d = cierre
        if not llego_5eur and cierre >= precio_objetivo:
            llego_5eur = True
            sesiones_hasta_armar = i

        # 1) Cruce del equilibrio + 2%: se asegura 1 EUR
        if not ganancias_armadas and cierre >= nivel_ganancias:
            ganancias_armadas = True
            stop = max(stop, round((invertido + COMISION_VENTA + 1.0) / acciones, 4))

        # 2) Escalones de ganancia
        for alcanzado, asegurado in NIVELES_ESCALERA:
            if alcanzado in niveles_hechos:
                continue
            if cierre >= precio_para(alcanzado):
                niveles_hechos.add(alcanzado)
                stop = max(stop, round(precio_para(asegurado), 4))

        # 3) ¿Salta?
        if cierre <= stop:
            motivo = "stop inicial" if abs(stop - stop_inicial) < 1e-9 else "stop subido"
            return cerrar(op, cierre, fecha, i, motivo, precio_7d, precio_equilibrio,
                          llego_5eur, sesiones_hasta_armar)

        if i >= DIAS_MAXIMO:
            return cerrar(op, cierre, fecha, i, "plazo maximo", precio_7d, precio_equilibrio,
                          llego_5eur, sesiones_hasta_armar)

    return None


def _recorrer(op, hist, regla):
    if regla.get("tipo") == "escalera":
        return _recorrer_escalera(op, hist, regla)
    pe = op["precio_entrada"]
    acciones = op["acciones"]
    comisiones = COMISION_COMPRA + COMISION_VENTA

    precio_equilibrio = pe + (comisiones / acciones)
    stop = round(pe * (1 - regla["stop"] / 100), 4)
    stop_inicial = stop

    # Precio al que la operacion deja exactamente OBJETIVO_LIMPIO_EUR limpios.
    # Cuando el precio lo toca, se arma un suelo que ya no baja de ahi.
    precio_objetivo = pe + (OBJETIVO_LIMPIO_EUR + comisiones) / acciones

    maximo = pe
    escalon = 0
    precio_7d = None
    suelo = None            # None = el stop aun no ha subido al equilibrio
    sesiones_hasta_armar = None
    llego_5eur = False

    for i, (fecha, fila) in enumerate(hist.iterrows(), start=1):
        cierre = float(fila["Close"])
        minimo_dia = float(fila["Low"]) if "Low" in hist.columns and fila["Low"] == fila["Low"] else cierre

        maximo_dia = float(fila["High"]) if "High" in hist.columns and fila["High"] == fila["High"] else cierre

        if i == DIAS_REVISION:
            precio_7d = cierre

        # --- PRIMERO: ¿salto el stop que estaba PUESTO al empezar el dia? ---
        # El orden importa mucho. El stop vigente durante la sesion es el que
        # quedo fijado al cerrar la sesion ANTERIOR, no uno que se coloque
        # hoy. Comprobarlo despues de armar el suelo hacia que casi toda
        # operacion cerrara en +5,00 exactos: el dia que el precio SUBE
        # atravesando el objetivo, el minimo de ese mismo dia queda por
        # debajo del objetivo casi siempre (el precio venia de mas abajo),
        # y se disparaba al instante un stop que en realidad todavia no
        # existia. Una accion que subia un 40% acababa apuntada como +5 EUR.
        if minimo_dia <= stop:
            motivo = "trailing" if suelo is not None else "stop-loss"
            return cerrar(op, stop, fecha, i, motivo, precio_7d, precio_equilibrio,
                          llego_5eur, sesiones_hasta_armar)

        # --- DESPUES: ¿se han alcanzado hoy los 5 EUR limpios? ---
        # Se mira el maximo del dia, no el cierre: basta con que el precio
        # pasara por ahi durante la sesion para colocar el stop de garantia.
        # A partir de MANANA la operacion ya no puede acabar por debajo.
        # --- LA REGLA DE JOSE MANUEL: en cuanto la posicion esta en verde, el
        # stop sube al punto de equilibrio. A partir de ese momento ya no se
        # puede perder dinero, pase lo que pase. ---
        # El disparador es el nivel de los 5 EUR ("ahi empiezo a vigilar"), pero
        # el stop se coloca en el EQUILIBRIO, mas abajo. Los dos niveles son
        # distintos y esa distancia es justo el aire que necesita la posicion:
        # en el ejemplo, el precio llega a 110 y el stop se pone en 100, no en
        # 110. Si el suelo se armara nada mas ponerse en verde quedaria pegado
        # al precio y el vaiven normal lo barreria al dia siguiente.
        if suelo is None and maximo_dia >= pe * (1 + regla["activacion"] / 100):
            suelo = stop_inicial  # marca de que el trailing ya esta activo
            sesiones_hasta_armar = i

        # Marca aparte, solo para el informe: si en algun momento la operacion
        # LLEGO a poder dar los 5 EUR limpios. No mueve el stop.
        if maximo_dia >= precio_objetivo:
            llego_5eur = True

        # Metodo 1: trailing sobre el maximo alcanzado, pero SOLO una vez que
        # el precio ha llegado al +5%. Por debajo de ahi el stop se queda
        # donde estaba: es la "Accion 2" de la tabla, que sube a 104 y aun
        # asi conserva el stop en 92.
        if cierre > maximo:
            maximo = cierre
        if maximo >= pe * (1 + regla["activacion"] / 100):
            stop_trailing = round(maximo * (1 - regla["trailing"] / 100), 4)
        else:
            stop_trailing = stop_inicial

        # Metodo 2: escalones de +5% desde el punto de equilibrio
        stop_escalones = stop
        if cierre > precio_equilibrio:
            calculado = int((cierre / precio_equilibrio - 1) // ESCALON_PCT)
            if calculado > escalon:
                escalon = calculado
                stop_escalones = round(stop_inicial * (1 + ESCALON_PCT * escalon), 4)

        # El stop real es el mas protector de todos, y nunca baja. El suelo
        # de los 5 EUR entra aqui: una vez armado, ninguna regla puede
        # devolver la operacion a perdidas.
        stop = max(stop, stop_trailing, stop_escalones)
        if suelo is not None:
            stop = max(stop, suelo)

        if i >= DIAS_MAXIMO:
            return cerrar(op, cierre, fecha, i, "plazo maximo", precio_7d, precio_equilibrio,
                          llego_5eur, sesiones_hasta_armar)

    return None  # sigue abierta


def clasificar(neto, sesiones, motivo, llego_al_objetivo):
    """Traduce el resultado a una palabra. Es lo que permitira, dentro de unas
    semanas, preguntar cosas como "¿que tienen en comun las tarjetas que
    acabaron NEFASTAS?" en vez de mirar una nube de porcentajes.

    Ojo con PLANO: no es neutro. Con 2 EUR de comisiones sobre 100 invertidos,
    quedarse veinte dias sin moverse ES perder — y ademas ocupa una de las
    pocas posiciones disponibles. Una candidata que acaba plana a menudo es
    peor que una que cae rapido y libera el dinero."""
    if neto >= UMBRAL_TOP:
        return "top", "Ganancia grande. Esta es la que compensa a todas las demas."
    if neto >= UMBRAL_BENEFICIO:
        return "beneficio", f"Dejo {neto:.2f} EUR limpios: por encima del liston de los 5 EUR."
    if neto > PLANO_MARGEN:
        return "flojo", "Acabo en positivo pero sin llegar a los 5 EUR limpios."
    if motivo == "plazo maximo" and abs(neto) <= PLANO_MARGEN:
        return "plano", ("Veinte dias sin moverse. Con las comisiones esto es perder, "
                         "y ademas tuvo bloqueada una posicion todo ese tiempo.")
    if motivo != "plazo maximo" and sesiones <= SESIONES_NEFASTA:
        return "nefasta", (f"El stop salto en solo {sesiones} sesion{'es' if sesiones != 1 else ''}. "
                           "La entrada estaba mal desde el principio: aqui falla la recomendacion, "
                           "no el mercado.")
    return "perdida", ("Aguanto un tiempo y acabo saltando el stop. La tesis tardo en romperse; "
                       "puede ser el mercado y no la seleccion.")


def cerrar(op, precio_salida, fecha, sesiones, motivo, precio_7d, precio_equilibrio,
           llego_al_objetivo=False, sesiones_hasta_armar=None):
    acciones = op["acciones"]
    bruto = (precio_salida - op["precio_entrada"]) * acciones
    neto = bruto - COMISION_COMPRA - COMISION_VENTA
    invertido = op["invertido"]
    estado, explicacion = clasificar(neto, sesiones, motivo, llego_al_objetivo)
    return {
        "precio_salida": round(float(precio_salida), 4),
        "fecha_salida": fecha.strftime("%Y-%m-%d") if hasattr(fecha, "strftime") else str(fecha),
        "sesiones": sesiones,
        "motivo_salida": motivo,
        # Bruto y neto por separado: con 100 EUR los 2 EUR de comisiones son
        # un 2%, y esa diferencia es justo lo que hay que ver.
        "rentabilidad_bruta_pct": round(bruto / invertido * 100, 2),
        "rentabilidad_neta_pct": round(neto / invertido * 100, 2),
        "resultado_neto_eur": round(neto, 2),
        "rentabilidad_7d_pct": (round((precio_7d - op["precio_entrada"]) / op["precio_entrada"] * 100, 2)
                                if precio_7d else None),
        # Exito = 5 EUR limpios o mas, que es como lo mide Jose Manuel
        "exito": bool(neto >= OBJETIVO_LIMPIO_EUR - 0.01),
        "llego_al_objetivo": llego_al_objetivo,
        "sesiones_hasta_equilibrio": sesiones_hasta_armar,
        "precio_equilibrio": round(precio_equilibrio, 4),
        "estado_resultado": estado,
        "explicacion": explicacion,
    }


def _valor_factor(op, ruta):
    """Saca el valor de un factor de la tarjeta guardada con la operacion."""
    t = op.get("tarjeta") or {}
    if ruta == "posicion_ranking":
        return op.get("posicion_ranking")
    if ruta == "potencial_pct":
        return op.get("potencial_pct")
    if ruta == "pct_strong_buy":
        cr = t.get("consenso_real") or {}
        return cr.get("pct_strong_buy")
    return t.get(ruta)


def _resumen_grupo(g):
    if not g:
        return None
    media = sum(o["resultado_neto_eur"] for o in g) / len(g)
    buenos = sum(1 for o in g if o.get("estado_resultado") in ("top", "beneficio"))
    malos = sum(1 for o in g if o.get("estado_resultado") in ("nefasta", "perdida"))
    return (media, buenos / len(g) * 100, malos / len(g) * 100, len(g))


FACTORES_NUMERICOS = [
    ("score", "score", "nota global"),
    ("posicion_ranking", "posicion_ranking", "puesto en el ranking"),
    ("potencial_pct", "potencial_pct", "potencial hasta objetivo"),
    ("dispersion_pct", "dispersion_pct", "dispersion"),
    ("pct_strong_buy", "pct_strong_buy", "% compra fuerte"),
    ("momentum_30d_pct", "momentum_30d_pct", "momentum 30d"),
    ("fuerza_relativa_pct", "fuerza_relativa_pct", "fuerza relativa"),
    ("rsi_14", "rsi_14", "RSI"),
    ("volumen_relativo", "volumen_relativo", "volumen relativo"),
    ("volatilidad_diaria_pct", "volatilidad_diaria_pct", "volatilidad"),
    ("liquidez_dia", "liquidez_dia", "liquidez"),
    ("distancia_max_52s_pct", "distancia_max_52s_pct", "distancia max 52s"),
]

FACTORES_CATEGORICOS = [
    ("consenso", "consenso", "consenso"),
    ("tendencia_tecnica", "tendencia_tecnica", "tendencia tecnica"),
    ("tendencia_analistas", "tendencia_analistas", "tendencia analistas"),
    ("regimen_mercado", "regimen_mercado", "regimen de mercado"),
]

MINIMO_PARA_ANALIZAR = 15


def informe_ponderacion(cerradas):
    """Analisis factor por factor, pensado para pegarlo en el chat."""
    lineas = []
    if len(cerradas) < MINIMO_PARA_ANALIZAR:
        lineas += ["## Analisis por factor", "",
                   f"Solo hay {len(cerradas)} operaciones cerradas. Hacen falta al menos",
                   f"{MINIMO_PARA_ANALIZAR} para que partir en grupos signifique algo.", ""]
        return lineas

    lineas += ["## Analisis por factor", "",
               "Cada factor se parte en tres grupos segun su valor y se compara como",
               "acabaron. Si el grupo ALTO no va mejor que el BAJO, ese factor no",
               "predice; si va peor, esta restando.", "",
               "| Factor | Grupo | Ops | Media | Buenas | Malas |",
               "|---|---|---|---|---|---|"]

    discriminacion = []
    for clave, ruta, etiqueta in FACTORES_NUMERICOS:
        con = [o for o in cerradas if _valor_factor(o, ruta) is not None]
        if len(con) < MINIMO_PARA_ANALIZAR:
            continue
        con.sort(key=lambda o: _valor_factor(o, ruta))
        n = len(con) // 3
        grupos = [("bajo", con[:n]), ("medio", con[n:2 * n]), ("alto", con[2 * n:])]
        medias = {}
        for nombre, g in grupos:
            r = _resumen_grupo(g)
            if not r:
                continue
            medias[nombre] = r[0]
            lineas.append(f"| {etiqueta} | {nombre} | {r[3]} | {r[0]:+.2f} EUR | {r[1]:.0f}% | {r[2]:.0f}% |")
        if "alto" in medias and "bajo" in medias:
            discriminacion.append((medias["alto"] - medias["bajo"], etiqueta, medias["bajo"], medias["alto"]))

    for clave, ruta, etiqueta in FACTORES_CATEGORICOS:
        grupos = {}
        for o in cerradas:
            v = _valor_factor(o, ruta)
            if v is None:
                continue
            grupos.setdefault(str(v), []).append(o)
        for v, g in sorted(grupos.items(), key=lambda x: -len(x[1])):
            if len(g) < 5:
                continue
            r = _resumen_grupo(g)
            lineas.append(f"| {etiqueta} | {v} | {r[3]} | {r[0]:+.2f} EUR | {r[1]:.0f}% | {r[2]:.0f}% |")

    # Catalizador (booleano)
    for valor, nombre in ((True, "con catalizador"), (False, "sin catalizador")):
        g = [o for o in cerradas if bool((o.get("tarjeta") or {}).get("catalizador_resultados")) is valor]
        if len(g) >= 5:
            r = _resumen_grupo(g)
            lineas.append(f"| catalizador | {nombre} | {r[3]} | {r[0]:+.2f} EUR | {r[1]:.0f}% | {r[2]:.0f}% |")

    lineas.append("")
    if discriminacion:
        discriminacion.sort(reverse=True)
        lineas += ["### Que factor separa mas", "",
                   "Diferencia entre el grupo alto y el bajo. Positivo = mas valor",
                   "es mejor. Negativo = el factor esta al reves y penaliza acertar.", "",
                   "| Factor | Bajo | Alto | Diferencia |", "|---|---|---|---|"]
        for dif, etiqueta, bajo, alto in discriminacion:
            lineas.append(f"| {etiqueta} | {bajo:+.2f} | {alto:+.2f} | **{dif:+.2f} EUR** |")
        lineas += ["", "Los de arriba merecen MAS peso; los de abajo, menos o al reves.", ""]
    return lineas

def escribir_informe(operaciones):
    cerradas = [o for o in operaciones if o["estado"] == "cerrada"]
    abiertas = [o for o in operaciones if o["estado"] == "abierta"]

    # Numero de revision: una cada 15 dias desde la primera operacion, que es
    # el ritmo al que Jose Manuel quiere ajustar la ponderacion.
    revision, dias = 0, 0
    if operaciones:
        inicio = min(o["fecha_entrada"] for o in operaciones)
        dias = (datetime.now() - datetime.strptime(inicio, "%Y-%m-%d")).days
        revision = dias // 15
    faltan = 15 - (dias % 15)

    lineas = [
        "# Simulacion en paralelo",
        "",
        f"Actualizado: {datetime.now().strftime('%Y-%m-%d %H:%M')} · dia {dias} de ejecucion",
        (f"**Revision nº{revision} disponible.** Pega este informe en el chat para decidir la ponderacion."
         if revision >= 1 and dias % 15 <= 2 else
         f"Proxima revision de ponderacion en {faltan} dia{'s' if faltan != 1 else ''}."),
        "",
        f"- Operaciones cerradas: **{len(cerradas)}**",
        f"- Operaciones abiertas: {len(abiertas)}",
        "",
    ]

    if len(cerradas) < 20:
        lineas += [
            f"> Con {len(cerradas)} operaciones cerradas todavia NO se puede concluir nada.",
            "> Hacen falta bastantes decenas por tramo para que la comparacion",
            "> signifique algo. Hasta entonces esto solo acumula datos.",
            "",
        ]

    if cerradas:
        lineas += ["## Como acabaron", "",
                   "| Estado | Ops | % del total | Media |", "|---|---|---|---|"]
        for est in ("top", "beneficio", "flojo", "plano", "perdida", "nefasta"):
            g = [o for o in cerradas if o.get("estado_resultado") == est]
            if not g:
                lineas.append(f"| {est} | 0 | - | - |")
                continue
            media = sum(o["resultado_neto_eur"] for o in g) / len(g)
            lineas.append(f"| {est} | {len(g)} | {len(g) / len(cerradas) * 100:.0f}% | {media:+.2f} EUR |")
        lineas.append("")

        lineas += ["## Por tramo del ranking", "",
                   "| Franja | Ops | Media neta | Con 5 EUR+ | Llegaron al suelo | Sesiones |",
                   "|---|---|---|---|---|---|"]
        for nombre in ("1-10", "11-20", "21-30"):
            g = [o for o in cerradas if o.get("tramo") == nombre]
            if not g:
                lineas.append(f"| {nombre} | 0 | - | - | - | - |")
                continue
            media = sum(o["rentabilidad_neta_pct"] for o in g) / len(g)
            exitos = sum(1 for o in g if o["exito"])
            ses = sum(o["sesiones"] for o in g) / len(g)
            armadas = sum(1 for o in g if o.get("llego_al_objetivo"))
            lineas.append(f"| {nombre} | {len(g)} | {media:+.2f}% | "
                          f"{exitos}/{len(g)} ({exitos / len(g) * 100:.0f}%) | "
                          f"{armadas}/{len(g)} | {ses:.0f} |")

        lineas += ["", "**Como leerlo:** si la fila `top` no supera claramente a `media` y",
                   "`cola`, el score NO esta ordenando bien y hay que revisar los pesos.", ""]

        lineas += ["## Por motivo de salida", ""]
        for motivo in ("trailing", "stop-loss", "plazo maximo"):
            g = [o for o in cerradas if o.get("motivo_salida") == motivo]
            if g:
                media = sum(o["rentabilidad_neta_pct"] for o in g) / len(g)
                lineas.append(f"- **{motivo}**: {len(g)} operaciones, media {media:+.2f}%")
        lineas.append("")

        con_var = [o for o in cerradas if o.get("variantes")]
        if con_var:
            lineas += ["## Comparacion de reglas de salida", "",
                       "Todas sobre las MISMAS operaciones y los mismos dias.",
                       "",
                       "| Regla | Total | Media | Aciertos | Peor |",
                       "|---|---|---|---|---|"]
            filas = []
            for regla in VARIANTES:
                n = regla["nombre"]
                vals = [o["variantes"][n] for o in con_var if n in o["variantes"]]
                if not vals:
                    continue
                total_v = sum(v["neto_eur"] for v in vals)
                media_v = sum(v["neto_pct"] for v in vals) / len(vals)
                aciertos = sum(1 for v in vals if v["neto_eur"] >= OBJETIVO_LIMPIO_EUR - 0.01)
                peor = min(v["neto_eur"] for v in vals)
                filas.append((total_v, n, media_v, aciertos, len(vals), peor))
            for total_v, n, media_v, aciertos, cuantos, peor in sorted(filas, reverse=True):
                lineas.append(f"| {n} | {total_v:+.2f} EUR | {media_v:+.2f}% | "
                              f"{aciertos}/{cuantos} | {peor:+.2f} EUR |")
            lineas += ["", "**Como leerlo:** la de arriba es la que mas habria ganado con tus",
                       "propias candidatas. Mira tambien la columna `Peor`: una regla que gana",
                       "mas pero con perdidas maximas muy grandes puede no compensar.", ""]

        total = sum(o["resultado_neto_eur"] for o in cerradas)
        media_total = sum(o["rentabilidad_neta_pct"] for o in cerradas) / len(cerradas)
        exitos = sum(1 for o in cerradas if o["exito"])
        lineas += ["## Conjunto", "",
                   f"- Media neta: **{media_total:+.2f}%**",
                   f"- Aciertos (>= {OBJETIVO_LIMPIO_EUR:.0f} EUR limpios): {exitos}/{len(cerradas)} "
                   f"({exitos / len(cerradas) * 100:.0f}%)",
                   f"- Resultado acumulado ficticio: {total:+.2f} EUR "
                   f"sobre {len(cerradas)} x {CAPITAL_POR_OPERACION:.0f} EUR", ""]

    lineas += informe_ponderacion(cerradas)

    with open(INFORME, "w", encoding="utf-8") as f:
        f.write("\n".join(lineas))


def ejecutar():
    datos = cargar(RANKING, {})
    ranking = datos.get("ranking", [])
    operaciones = cargar(OPERACIONES, [])

    nuevas = abrir_operaciones(ranking, operaciones)
    print(f"Operaciones ficticias nuevas: {nuevas}")

    cerradas_ahora = 0
    for op in operaciones:
        if op["estado"] != "abierta":
            continue

        # UNA sola descarga por operacion; todas las variantes se reconstruyen
        # sobre el mismo historico.
        hist = descargar_historico(op)
        time.sleep(1.5)
        if hist is None:
            continue

        resultado = reconstruir(op, hist)
        if not resultado:
            continue

        op.update(resultado)
        op["estado"] = "cerrada"
        cerradas_ahora += 1

        # Mismas candidatas, mismos dias, reglas distintas: asi la comparacion
        # entre variantes no puede achacarse a la suerte de la seleccion.
        op["variantes"] = {}
        for regla in VARIANTES:
            r = reconstruir(op, hist, regla)
            if r:
                op["variantes"][regla["nombre"]] = {
                    "neto_eur": r["resultado_neto_eur"],
                    "neto_pct": r["rentabilidad_neta_pct"],
                    "sesiones": r["sesiones"],
                    "motivo": r["motivo_salida"],
                }

        print(f"  cerrada {op['ticker']:12} {resultado['rentabilidad_neta_pct']:+6.2f}% "
              f"en {resultado['sesiones']:2} sesiones por {resultado['motivo_salida']}")

    print(f"Cerradas en esta pasada: {cerradas_ahora}")
    guardar(OPERACIONES, operaciones)
    escribir_informe(operaciones)
    print(f"Total acumulado: {sum(1 for o in operaciones if o['estado'] == 'cerrada')} cerradas, "
          f"{sum(1 for o in operaciones if o['estado'] == 'abierta')} abiertas")


if __name__ == "__main__":
    ejecutar()
