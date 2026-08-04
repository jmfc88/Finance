// VERSION: 2 (29/07/2026) - añade sincronización opcional entre dispositivos:
// si hay un repo + token de GitHub configurados, cada guardado sube también
// un archivo ledger.json al repo, y cada carga lo trae primero de ahí (con
// copia local de respaldo por si no hay conexión). Sin token, funciona
// exactamente igual que antes (solo local, por dispositivo).
// (Base: v1 lógica compartida entre simulador.html e historial.html)

const COMISION_COMPRA = 1.0;
const COMISION_VENTA = 1.0;
const TAX_RATE = 0.19;
const AHORRO_RATE = 0.10;
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

async function cargarLedger() {
  const repo = obtenerRepoConfigurado();
  if (repo) {
    try {
      const resp = await fetch(`https://raw.githubusercontent.com/${repo}/main/${LEDGER_PATH}?t=${Date.now()}`, { cache: 'no-store' });
      if (resp.ok) {
        const remoto = await resp.json();
        try { localStorage.setItem('ledger-operaciones', JSON.stringify(remoto)); } catch (e) { /* no pasa nada, se queda la copia anterior */ }
        return remoto;
      }
      // 404 = todavía no existe el archivo en el repo (normal la primera vez), sigue con lo local
    } catch (e) { /* sin conexión: sigue con la copia local de respaldo */ }
  }
  try {
    const guardado = localStorage.getItem('ledger-operaciones');
    return guardado ? JSON.parse(guardado) : [];
  } catch (e) { return []; }
}

async function guardarLedger(ledger) {
  // Copia local siempre, rápida y funciona sin conexión
  try { localStorage.setItem('ledger-operaciones', JSON.stringify(ledger)); } catch (e) { console.error('No se pudo guardar local', e); }

  const repo = obtenerRepoConfigurado();
  const token = obtenerTokenConfigurado();
  if (!repo || !token) return; // sin sincronización configurada, se queda solo en local

  try {
    const contenidoBase64 = btoa(unescape(encodeURIComponent(JSON.stringify(ledger, null, 2))));
    const cabeceras = { Authorization: `Bearer ${token}`, Accept: 'application/vnd.github+json' };

    let sha = null;
    const actual = await fetch(`https://api.github.com/repos/${repo}/contents/${LEDGER_PATH}`, { headers: cabeceras });
    if (actual.ok) {
      const data = await actual.json();
      sha = data.sha;
    }

    const cuerpo = { message: 'actualiza ledger de operaciones', content: contenidoBase64 };
    if (sha) cuerpo.sha = sha;

    const resp = await fetch(`https://api.github.com/repos/${repo}/contents/${LEDGER_PATH}`, {
      method: 'PUT',
      headers: cabeceras,
      body: JSON.stringify(cuerpo),
    });
    if (!resp.ok) {
      console.error('No se pudo sincronizar con GitHub (revisa el token/permisos). Se queda guardado en local.', await resp.text());
    }
  } catch (e) {
    console.error('No se pudo sincronizar con GitHub, se queda guardado solo en local', e);
  }
}

function calcularNetoVenta(compra, venta, acciones) {
  const bruto = (venta - compra) * acciones;
  const gananciaAntesImp = bruto - (COMISION_COMPRA + COMISION_VENTA);
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
        const parcial = calcularNetoVenta(compra.precio, venta.precio, usar);
        neto = (neto || 0) + parcial;
      }
    }
    venta.neto = neto !== null ? Number(neto.toFixed(2)) : null;
  });
  return ledger;
}
