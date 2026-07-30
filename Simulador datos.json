
// VERSION: 1 (29/07/2026) - lógica compartida entre simulador.html e historial.html
// Se guarda en un archivo aparte para que ambas páginas usen EXACTAMENTE el
// mismo cálculo (evita que se desincronicen si se edita solo una).
 
const COMISION_COMPRA = 1.0;
const COMISION_VENTA = 1.0;
const TAX_RATE = 0.19;
const AHORRO_RATE = 0.10;
 
async function cargarLedger() {
  try {
    const guardado = localStorage.getItem('ledger-operaciones');
    return guardado ? JSON.parse(guardado) : [];
  } catch (e) { return []; }
}
 
async function guardarLedger(ledger) {
  try { localStorage.setItem('ledger-operaciones', JSON.stringify(ledger)); } catch (e) { console.error('No se pudo guardar el ledger', e); }
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
