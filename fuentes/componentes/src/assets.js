// Uploaded assets of this design system (served on the system's origin as /_blob/<id>).
// Outside the system, call LaMesa.setAssets({ key: url }) with your own copies.
export const assets = {
  logoInk: '/_blob/c63cd71aafe45f1e412fae1f8ad170b7',
  logoPaper: '/_blob/0db91ef2892150991fbbb542a4512882',
  mesa: '/_blob/94440a1db7e0127808bfc1ccf2175a18',
  invitacion: '/_blob/ad5d61aeeec4cf7c24e86cdb667695b1',
  servilleta: '/_blob/f77379931bae1c70c02150def849e149',
  sala: '/_blob/aef96384484ae4a6c5c27a3343efcf90',
  confesionario: '/_blob/4db26ec2756ca40ef30e60fbc1c5400a',
  cocina: '/_blob/2193403ddf276ce780aa8783a90058da',
  copas: '/_blob/66828f2d00bce08f8061c9f17dcfd692',
  pantalla: '/_blob/840dd0a618162eded4cfa5f9b2c5e41c'
};
export function setAssets(map) { Object.assign(assets, map || {}); return assets; }
export function asset(key) { return (key && assets[key]) || key; }

// Ficha (object label) and alt text for every photograph.
export const photos = {
  mesa: { alt: 'El cubierto de la Mesa 02 servido de noche: plato de porcelana sobre bajo plato de gres negro, el menú impreso apoyado en el plato, servilleta violeta con tenedor de bronce, copas de cristal, la tarjeta de lugar “Café” y, al fondo, velas y la pantalla de Deenex encendida.', n: 'Objeto 01', title: 'El cubierto', detail: 'Mesa 02 · lugar 04' },
  invitacion: { alt: 'Invitación de cartulina negra con “La Mesa” estampado en foil lila y canto pintado violeta, apoyada sobre un sobre lila cerrado con lacre violeta, sobre terciopelo.', n: 'Objeto 02', title: 'La invitación', detail: 'Algodón 1,7 mm · foil lila · canto violeta' },
  pantalla: { alt: 'La pantalla de la mesa en su soporte de bronce, mostrando el sistema de Deenex para elegir el segundo plato, con velas desenfocadas detrás.', n: 'Objeto 03', title: 'La pantalla de la mesa', detail: 'Sistema Deenex' },
  servilleta: { alt: 'Servilleta de lino blanca vista desde arriba con la conclusión de la Mesa 02 escrita a mano, seis firmas y “La Mesa” bordado en violeta; al lado, una lapicera negra y una copa con vino.', n: 'Objeto 04', title: 'La servilleta firmada', detail: 'Lino · bordado violeta · 46 × 46 cm' },
  confesionario: { alt: 'Un sillón de terciopelo violeta solo, bajo un cenital que dibuja un cono de luz en la bruma, junto a una mesa auxiliar con un vaso de agua.', n: 'Objeto 05', title: 'El confesionario', detail: 'Una silla · noventa segundos' },
  copas: { alt: 'Botella de vidrio con agua, un vaso y una copa con vino tinto sobre mármol negro, recortados contra una luz violeta.', n: 'Objeto 06', title: 'Agua y maridaje', detail: 'Vidrio · cristal · mármol' },
  sala: { alt: 'Planta cenital del salón: tres mesas redondas de seis con mantel oscuro, sillas de terciopelo violeta, cubiertos servidos y una pantalla encendida en el centro de cada mesa.', n: 'Planta', title: 'Tres mesas de seis', detail: '18 sillas' },
  cocina: { alt: 'El pase de la cocina: platos bajo campanas de acero en una mesada, lámparas de calor encendidas y las comandas de las tres mesas colgadas del riel.', n: 'Objeto 07', title: 'El pase', detail: 'Cocina a la vista' }
};

// Table centres and expert seats in the plan photograph, as % of the image (filled from the render).
export const plan = {
  tables: [
    { id: '01', x: 18.55, y: 46.34, r: 9.15, seat: { x: 19.0, y: 27.76 } },
    { id: '02', x: 50.0, y: 54.47, r: 9.15, seat: { x: 44.76, y: 38.27 } },
    { id: '03', x: 81.45, y: 46.34, r: 9.15, seat: { x: 81.0, y: 27.76 } }
  ]
};
