/* VERSION: 10 (23/08/2026) - enlace entre el cuaderno y el simulador. Nuevo:
cargarTarjetasDisponibles() lee historial_tarjetas.json del repo (la ventana
deslizante de 5 dias que genera fase3) y devuelve las tarjetas listas para
elegir al registrar una compra; guardarEnlaceTarjeta() escribe el enlace en
tarjetas_compras.json, que NO se borra nunca — ahi queda para siempre que
decia el sistema el dia que se compro, junto a la posicion en el ranking y
los dias que pasaron entre la tarjeta y la compra. guardarArchivoRepo() se
ha extraido de guardarLedger() para no repetir la misma subida a GitHub dos
veces. TODOS los comentarios siguen siendo de bloque, por lo de la v9. */

/* VERSION: 9 (22/08/2026) - CORRECCIÓN CRÍTICA DE VERDAD: se detectó el
archivo subido a GitHub sin saltos de línea (copia-pega en vez de "Upload
files"), lo que en JavaScript comenta sin querer TODO el código que viene
detrás del primer comentario de una línea — el archivo entero quedaba sin
ninguna función definida. Se han eliminado TODOS los comentarios de una
sola línea del archivo y se han convertido a bloque, que termina siempre
en su propio cierre pase lo que pase con los saltos de línea. Probado de
verdad: simulando la pérdida completa de saltos de línea, todas las
funciones (cargarLedger, guardarLedger, recalcularFIFO, comisionEfectivaOp,
totalOperacion, etc.) se mantienen definidas. SUBE ESTE ARCHIVO SIEMPRE
CON "UPLOAD FILES", NUNCA COPIA-PEGA.

VERSION: 8 (21/08/2026) - añade comisionEfectivaOp() y totalOperacion(),
compartidas entre simulador.html e historial.html, para mostrar el
desglose completo en cada tarjeta (precio × acciones + / − comisión =
total) — antes la comisión se guardaba pero no se veía en ningún sitio.

VERSION: 7 (21/08/2026) - añade comisión de compra/venta CONFIGURABLE
(obtenerComisionCompraConfigurada/obtenerComisionVentaConfigurada), para
precargar el campo del registro con el valor correcto sin tener que
escribirlo cada vez. Las constantes COMISION_COMPRA/VENTA se quedan
como respaldo fijo histórico, solo para operaciones antiguas guardadas
antes de que existiera el campo "comisión" — no se tocan nunca.

VERSION: 6 (21/08/2026) - calcularNetoVenta() usa ahora la comisión real
guardada en cada operación (compra y venta), en vez de asumir siempre la
constante global — con respaldo a la constante para operaciones antiguas
que no tengan ese dato todavía.

VERSION: 5 (05/08/2026) - CORRECCIÓN CRÍTICA: cargarLedger() ya no deja que
la copia de GitHub borre sin más lo que hay en local — ahora FUSIONA
ambas (sin duplicar) y sube la fusión de vuelta si hacía falta. Antes,
si un dispositivo guardaba algo local antes de tener el token puesto,
una recarga posterior con GitHub desactualizado podía borrar esos datos.

NOTA DE SEGURIDAD: este archivo ya no usa comentarios de una sola línea
en ningún sitio, a propósito — todos son de bloque, autoprotegidos. */

/* COMISION_COMPRA y COMISION_VENTA: histórico fijo — respaldo SOLO para
operaciones antiguas guardadas antes de que existiera el campo "comisión";
no tocar nunca. */
const COMISION_COMPRA = 1.0;
const COMISION_VENTA = 1.0;

function obtenerComisionCompraConfigurada() {
  try {
    const valor = localStorage.getItem('comision-compra-defecto');
    return valor !== null ? parseFloat(valor) : COMISION_COMPRA;
  } catch (e) { return COMISION_COMPRA; }
}

function guardarComisionCompraConfigurada(valor) {
  try { localStorage.setItem('comision-compra-defecto', String(valor)); } catch (e) { console.error('No se pudo guardar la comisión de compra', e); }
}

function obtenerComisionVentaConfigurada() {
  try {
    const valor = localStorage.getItem('comision-venta-defecto');
    return valor !== null ? parseFloat(valor) : COMISION_VENTA;
  } catch (e) { return COMISION_VENTA; }
}

function guardarComisionVentaConfigurada(valor) {
  try { localStorage.setItem('comision-venta-defecto', String(valor)); } catch (e) { console.error('No se pudo guardar la comisión de venta', e); }
}

const TAX_RATE = 0.19;
const AHORRO_RATE = 0.10;
const COSTE_FX_PCT_DEFECTO = 1.2;
/* % estimado de coste de cambio de divisa (Trade Republic no lo publica
como línea aparte, va dentro del margen de ejecución; fuentes externas lo
sitúan entre 0,14% y 0,5-1% según el caso. Se usa 1% por defecto como
colchón de seguridad, ajustable por el usuario.) */

function obtenerCosteFXConfigurado() {
  try {
    const valor = localStorage.getItem('coste-fx-pct');
    return valor !== null ? parseFloat(valor) : COSTE_FX_PCT_DEFECTO;
  } catch (e) { return COSTE_FX_PCT_DEFECTO; }
}

function guardarCosteFXConfigurado(pct) {
  try { localStorage.setItem('coste-fx-pct', String(pct)); } catch (e) { console.error('No se pudo guardar el coste FX', e); }
}
const LEDGER_PATH = 'ledger.json';

function obtenerRepoConfigurado() {
  try { return localStorage.getItem('github-repo') || ''; } catch (e) { return ''; }
}

function obtenerTokenConfigurado() {
  try { return localStorage.getItem('github-token') || ''; } catch (e) { return ''; }
}

function guardarTokenConfigurado(token) {
  try {
    if (token) localStorage.setItem('github-token', token);
    else localStorage.removeItem('github-token');
  } catch (e) { console.error('No se pudo guardar el token', e); }
}

function claveOperacion(op) {
  /* Identifica una operación de forma única, para poder fusionar sin duplicar */
  return `${op.tipo}|${op.ticker}|${op.fecha}|${op.precio}|${op.acciones}`;
}

function fusionarLedgers(local, remoto) {
  const mapa = new Map();
  [...local, ...remoto].forEach(op => mapa.set(claveOperacion(op), op));
  return Array.from(mapa.values());
}

async function cargarLedger() {
  let local = [];
  try {
    const guardado = localStorage.getItem('ledger-operaciones');
    local = guardado ? JSON.parse(guardado) : [];
  } catch (e) { /* no pasa nada */ }

  const repo = obtenerRepoConfigurado();
  if (repo) {
    try {
      const resp = await fetch(`https://raw.githubusercontent.com/${repo}/main/${LEDGER_PATH}?t=${Date.now()}`, { cache: 'no-store' });
      if (resp.ok) {
        const remoto = await resp.json();
        const fusionado = fusionarLedgers(local, remoto);
        recalcularFIFO(fusionado);
        try { localStorage.setItem('ledger-operaciones', JSON.stringify(fusionado)); } catch (e) { /* no pasa nada */ }
        /* Si local tenía algo que GitHub no tenía todavía, subimos la fusión
        para que quede sincronizado — así ningún dispositivo pierde datos. */
        if (fusionado.length !== remoto.length) {
          await guardarLedger(fusionado);
        }
        return fusionado;
      }
      /* 404 = todavía no existe el archivo en el repo (normal la primera vez), sigue con lo local */
    } catch (e) { /* sin conexión: sigue con la copia local de respaldo */ }
  }
  return local;
}

/* Sube cualquier archivo JSON al repo. Extraido de guardarLedger() en la v10
porque ahora hay dos archivos que subir (ledger.json y tarjetas_compras.json)
y no tiene sentido tener el mismo bloque de codigo duplicado. */
async function guardarArchivoRepo(ruta, contenido, mensaje) {
  const repo = obtenerRepoConfigurado();
  const token = obtenerTokenConfigurado();
  if (!repo || !token) return false; /* sin sincronizacion configurada, se queda solo en local */

  try {
    const contenidoBase64 = btoa(unescape(encodeURIComponent(JSON.stringify(contenido, null, 2))));
    const cabeceras = { Authorization: `Bearer ${token}`, Accept: 'application/vnd.github+json' };

    let sha = null;
    const actual = await fetch(`https://api.github.com/repos/${repo}/contents/${ruta}`, { headers: cabeceras });
    if (actual.ok) {
      const data = await actual.json();
      sha = data.sha;
    }

    const cuerpo = { message: mensaje, content: contenidoBase64 };
    if (sha) cuerpo.sha = sha;

    const resp = await fetch(`https://api.github.com/repos/${repo}/contents/${ruta}`, {
      method: 'PUT',
      headers: cabeceras,
      body: JSON.stringify(cuerpo),
    });
    if (!resp.ok) {
      console.error(`No se pudo subir ${ruta} a GitHub (revisa el token/permisos). Se queda guardado en local.`, await resp.text());
      return false;
    }
    return true;
  } catch (e) {
    console.error(`No se pudo subir ${ruta} a GitHub, se queda guardado solo en local`, e);
    return false;
  }
}

async function guardarLedger(ledger) {
  /* Copia local siempre, rápida y funciona sin conexión */
  try { localStorage.setItem('ledger-operaciones', JSON.stringify(ledger)); } catch (e) { console.error('No se pudo guardar local', e); }
  await guardarArchivoRepo(LEDGER_PATH, ledger, 'actualiza ledger de operaciones');
}

function comisionEfectivaOp(op) {
  return op.comision !== undefined && op.comision !== null
    ? op.comision
    : (op.tipo === 'venta' ? COMISION_VENTA : COMISION_COMPRA);
}

function totalOperacion(op) {
  const bruto = op.precio * op.acciones;
  const comision = comisionEfectivaOp(op);
  return op.tipo === 'compra' ? bruto + comision : bruto - comision;
}

function calcularNetoVenta(compra, venta, acciones, comisionCompra, comisionVenta) {
  const cComp = comisionCompra !== undefined && comisionCompra !== null ? comisionCompra : COMISION_COMPRA;
  const cVent = comisionVenta !== undefined && comisionVenta !== null ? comisionVenta : COMISION_VENTA;
  const bruto = (venta - compra) * acciones;
  const gananciaAntesImp = bruto - (cComp + cVent);
  const impuesto = Math.max(gananciaAntesImp, 0) * TAX_RATE;
  return gananciaAntesImp - impuesto;
}

/** Recorre el ledger en orden de fecha y vuelve a emparejar ventas con
 * compras FIFO desde cero. Se usa tras registrar, editar o borrar
 * cualquier operación, para que las cifras nunca queden descuadradas. */
function recalcularFIFO(ledger) {
  const ordenado = ledger.slice().sort((a, b) => (a.fecha || '').localeCompare(b.fecha || ''));
  ordenado.forEach(op => {
    if (op.tipo === 'compra') op.acciones_restantes = op.acciones;
    else op.neto = null;
  });
  ordenado.forEach(venta => {
    if (venta.tipo !== 'venta') return;
    let restante = venta.acciones;
    let neto = null;
    for (const compra of ordenado) {
      if (compra.tipo === 'compra' && compra.ticker === venta.ticker && compra.acciones_restantes > 0 && restante > 0) {
        const usar = Math.min(compra.acciones_restantes, restante);
        compra.acciones_restantes -= usar;
        restante -= usar;
        const parcial = calcularNetoVenta(compra.precio, venta.precio, usar, compra.comision, venta.comision);
        neto = (neto || 0) + parcial;
      }
    }
    venta.neto = neto !== null ? Number(neto.toFixed(2)) : null;
  });
  return ledger;
}


/* ==========================================================================
   ENLACE CUADERNO <-> SIMULADOR  (v10)
   --------------------------------------------------------------------------
   historial_tarjetas.json  = ventana deslizante de 5 dias, la genera fase3 en
                              cada ejecucion. Es TEMPORAL: lo de hace 6 dias ya
                              no esta.
   tarjetas_compras.json    = PERMANENTE. Cuando se registra una compra, la
                              tarjeta elegida se copia aqui y ya no se borra
                              nunca. Es el unico sitio donde queda constancia
                              de que decia el sistema el dia de la compra.
   ========================================================================== */

const TARJETAS_PATH = 'historial_tarjetas.json';
const COMPRAS_TARJETAS_PATH = 'tarjetas_compras.json';

/* Aplana la ventana de 5 dias en una lista plana ordenada de mas reciente a
mas antigua, lista para pintar en el desplegable. Cada elemento es una version
concreta de una tarjeta: si una candidata cambio de contenido a media manana,
apareceran las dos versiones y se podra elegir la que se vio. */
async function cargarTarjetasDisponibles() {
  const repo = obtenerRepoConfigurado();
  if (!repo) return [];

  try {
    const resp = await fetch(`https://raw.githubusercontent.com/${repo}/main/${TARJETAS_PATH}?t=${Date.now()}`, { cache: 'no-store' });
    if (!resp.ok) return []; /* 404 = fase3 todavia no ha corrido con la v11 */
    const datos = await resp.json();

    const lista = [];
    (datos.dias || []).forEach(dia => {
      (dia.tarjetas || []).forEach(t => {
        const apariciones = t.apariciones || [];
        const posiciones = apariciones.map(a => a.posicion).filter(p => p != null);
        const scores = apariciones.map(a => a.score).filter(x => x != null);
        lista.push({
          fecha: dia.fecha,
          ticker: t.ticker,
          nombre: t.nombre_empresa || t.ticker,
          huella: t.huella,
          apariciones: apariciones,
          hora_primera: apariciones.length ? apariciones[0].hora : null,
          hora_ultima: apariciones.length ? apariciones[apariciones.length - 1].hora : null,
          mejor_posicion: posiciones.length ? Math.min.apply(null, posiciones) : null,
          score: scores.length ? scores[scores.length - 1] : (t.tarjeta || {}).score,
          tarjeta: t.tarjeta || {},
        });
      });
    });

    lista.sort((a, b) => {
      if (a.fecha !== b.fecha) return a.fecha < b.fecha ? 1 : -1;
      return (a.mejor_posicion || 999) - (b.mejor_posicion || 999);
    });
    return lista;
  } catch (e) {
    console.error('No se pudieron cargar las tarjetas del cuaderno', e);
    return [];
  }
}

/* Normaliza un ticker para comparar: Trade Republic y Yahoo Finance no siempre
usan el mismo sufijo de mercado (FM en Toronto puede ser FM.TO en Yahoo), asi
que para preseleccionar se compara solo la raiz, antes del punto. */
function raizTicker(ticker) {
  return (ticker || '').toUpperCase().split('.')[0].trim();
}

/* Devuelve el indice de la tarjeta que MEJOR encaja con lo que se esta
registrando, o -1 si ninguna encaja. Solo preselecciona; la ultima palabra
siempre la tiene la persona, porque el emparejamiento automatico por ticker
falla justo en los casos de empresas con varias cotizaciones. */
function sugerirTarjeta(listaTarjetas, ticker, nombre) {
  const raiz = raizTicker(ticker);
  const nombreLimpio = (nombre || '').toLowerCase().trim();

  let mejor = -1;
  listaTarjetas.forEach((t, i) => {
    if (mejor !== -1) return; /* la lista ya viene ordenada por reciente, el primero que encaje vale */
    const coincideTicker = raiz && raizTicker(t.ticker) === raiz;
    const coincideNombre = nombreLimpio.length > 3 && (t.nombre || '').toLowerCase().includes(nombreLimpio);
    if (coincideTicker || coincideNombre) mejor = i;
  });
  return mejor;
}

function diasEntre(fechaTarjeta, fechaCompra) {
  try {
    const a = new Date(fechaTarjeta + 'T00:00:00');
    const b = new Date(fechaCompra + 'T00:00:00');
    return Math.round((b - a) / 86400000);
  } catch (e) { return null; }
}

async function cargarTarjetasCompras() {
  let local = [];
  try {
    const guardado = localStorage.getItem('tarjetas-compras');
    local = guardado ? JSON.parse(guardado) : [];
  } catch (e) { /* no pasa nada */ }

  const repo = obtenerRepoConfigurado();
  if (repo) {
    try {
      const resp = await fetch(`https://raw.githubusercontent.com/${repo}/main/${COMPRAS_TARJETAS_PATH}?t=${Date.now()}`, { cache: 'no-store' });
      if (resp.ok) {
        const remoto = await resp.json();
        /* Fusion sin duplicar: la clave de operacion identifica cada compra */
        const mapa = new Map();
        [].concat(local, remoto).forEach(e => mapa.set(e.clave_operacion, e));
        const fusionado = Array.from(mapa.values());
        try { localStorage.setItem('tarjetas-compras', JSON.stringify(fusionado)); } catch (e) { /* no pasa nada */ }
        return fusionado;
      }
    } catch (e) { /* sin conexion: sigue con la copia local */ }
  }
  return local;
}

/* Guarda de forma PERMANENTE el enlace entre una compra y la tarjeta que la
motivo. Se llama una sola vez, justo al registrar la compra. */
async function guardarEnlaceTarjeta(operacion, tarjetaElegida) {
  if (!tarjetaElegida) return null;

  const registros = await cargarTarjetasCompras();
  const clave = claveOperacion(operacion);
  if (registros.some(r => r.clave_operacion === clave)) return null; /* ya estaba enlazada */

  const entrada = {
    clave_operacion: clave,
    ticker: operacion.ticker,
    nombre: operacion.nombre || tarjetaElegida.nombre,
    isin: operacion.isin || null,
    fecha_compra: operacion.fecha,
    precio_compra: operacion.precio,
    acciones: operacion.acciones,
    comision: operacion.comision,
    tarjeta_fecha: tarjetaElegida.fecha,
    tarjeta_hora_primera: tarjetaElegida.hora_primera,
    tarjeta_hora_ultima: tarjetaElegida.hora_ultima,
    /* Dos datos que salen gratis y valen mucho al analizar despues: en que
    puesto del ranking estaba, y cuanto se tardo en decidir desde que salio */
    posicion_ranking: tarjetaElegida.mejor_posicion,
    dias_desde_tarjeta: diasEntre(tarjetaElegida.fecha, operacion.fecha),
    score_tarjeta: tarjetaElegida.score,
    precio_en_tarjeta: (tarjetaElegida.tarjeta || {}).precio_actual,
    version_scoring: (tarjetaElegida.tarjeta || {}).version_scoring || null,
    apariciones: tarjetaElegida.apariciones,
    registrado: new Date().toISOString(),
    tarjeta: tarjetaElegida.tarjeta,
  };

  registros.push(entrada);
  try { localStorage.setItem('tarjetas-compras', JSON.stringify(registros)); } catch (e) { console.error('No se pudo guardar local', e); }
  await guardarArchivoRepo(COMPRAS_TARJETAS_PATH, registros, `enlaza tarjeta del cuaderno con la compra de ${operacion.ticker}`);
  return entrada;
}
