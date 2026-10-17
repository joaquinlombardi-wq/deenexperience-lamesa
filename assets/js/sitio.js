/* La Mesa by Deenex — la página. Compone la Edición 01 con los componentes de window.LaMesa.
   En el navegador hidrata el HTML pre-renderizado; en Node (fuentes/ssr.cjs) se usa para generarlo. */
(function () {
  var L = window.LaMesa, h = React.createElement, C = L.content;

  L.setAssets({
    logoInk: 'assets/img/deenex-wordmark-ink.png',
    logoPaper: 'assets/img/deenex-wordmark-paper.png',
    mesa: 'assets/img/fotos/mesa.webp',
    invitacion: 'assets/img/fotos/invitacion.webp',
    pantalla: 'assets/img/fotos/pantalla.webp',
    servilleta: 'assets/img/fotos/servilleta.webp',
    confesionario: 'assets/img/fotos/confesionario.webp',
    copas: 'assets/img/fotos/copas.webp',
    sala: 'assets/img/fotos/sala.webp',
    cocina: 'assets/img/fotos/cocina.webp'
  });

  // Each section is a labelled region; `head` holds the SectionHeader props.
  function Section(props) {
    var tid = props.id + '-t';
    return h('section', { className: 'lm-section' + (props.band ? ' lm-band' : ''), id: props.id, 'aria-labelledby': tid },
      h('div', { className: 'lm-wrap sitio-stack' },
        props.head ? h(L.SectionHeader, Object.assign({ layout: 'split', id: tid }, props.head)) : null,
        props.children));
  }

  function Page() {
    return h(React.Fragment, null,
      h('a', { className: 'sitio-skip', href: '#por-que' }, 'Saltar al contenido'),
      h('main', { className: 'lm-page sitio' },
        h(L.Hero, null),
        h(Section, { id: 'por-que' },
          h(L.Statement, null, C.pitch),
          h(L.FeatureSplit, { image: 'invitacion', ratio: '3 / 2', reverse: true },
            h(L.SectionHeader, { kicker: C.why.kicker, title: C.why.title, lede: C.why.lede, id: 'por-que-t' }))),
        h(Section, { id: 'reglas', band: true, head: C.rules },
          h(L.RuleGrid, null)),
        h(Section, { id: 'antes', head: C.steps },
          h(L.ProcessSteps, null)),
        h(Section, { id: 'relato', band: true, head: Object.assign({ size: 1 }, C.story) },
          h(L.NightStory, null)),
        h(Section, { id: 'cierre', head: C.closing },
          h(L.FeatureSplit, { image: 'servilleta', ratio: '3 / 2' }, h(L.NumberedList, null))),
        h(Section, { id: 'sala', band: true, head: C.room },
          h(L.SeatingPlan, { course: 0 }),
          h(L.CastGrid, null)),
        h(Section, { id: 'partners', head: C.partners },
          h(L.PartnerList, null)),
        h(Section, { id: 'rubros', band: true, head: C.tiers },
          h(L.CategoryTiers, null)),
        h(Section, { id: 'calendario', head: C.calendar },
          h(L.Timeline, null)),
        h(Section, { id: 'camaras', band: true, head: C.cameras },
          h(L.Photo, { name: 'cocina', ratio: '21 / 9', position: '50% 60%', viewfinder: { rec: true, timecode: '22:00', label: 'Cocina · cámara 02' }, framed: true }),
          h(L.CameraPolicy, null))),
      h(L.Footer, null));
  }

  window.LaMesaSitio = { Page: Page };
  var root = typeof document !== 'undefined' && document.getElementById('sitio');
  if (root) {
    if (root.firstElementChild) ReactDOM.hydrateRoot(root, h(Page));
    else ReactDOM.createRoot(root).render(h(Page));
  }
})();
