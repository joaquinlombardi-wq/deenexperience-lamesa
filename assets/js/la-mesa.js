/* @ds-bundle: {"format":4,"namespace":"LaMesa","components":[{"name":"Kicker"},{"name":"Hashtag"},{"name":"Logo"},{"name":"Button"},{"name":"StatusPill"},{"name":"Photo"},{"name":"Viewfinder"},{"name":"SectionHeader"},{"name":"Statement"},{"name":"Callout"},{"name":"TopBar"},{"name":"Hero"},{"name":"StatRow"},{"name":"RuleGrid"},{"name":"ProcessSteps"},{"name":"NumberedList"},{"name":"FeatureSplit"},{"name":"CastGrid"},{"name":"NightStory"},{"name":"SeatingPlan"},{"name":"PartnerList"},{"name":"CategoryTiers"},{"name":"Timeline"},{"name":"CameraPolicy"},{"name":"Footer"}]} */
/* La Mesa by Deenex — componentes del sistema de diseño (fuente: fuentes/componentes/src). */
(() => {
  // componentes/src/util.jsx
  var React = window.React;
  var cx = (...a) => a.filter(Boolean).join(" ");
  function rich(str) {
    if (typeof str !== "string") return str;
    const out = [];
    const re = /\*\*(.+?)\*\*|\*(.+?)\*/g;
    let m;
    let last = 0;
    let k = 0;
    while (m = re.exec(str)) {
      if (m.index > last) out.push(str.slice(last, m.index));
      out.push(m[1] != null ? /* @__PURE__ */ React.createElement("strong", { key: k++ }, m[1]) : /* @__PURE__ */ React.createElement("em", { key: k++ }, m[2]));
      last = re.lastIndex;
    }
    if (last < str.length) out.push(str.slice(last));
    return out;
  }
  function useReducedMotion() {
    const [r, setR] = React.useState(false);
    React.useEffect(() => {
      if (!window.matchMedia) return;
      const q = window.matchMedia("(prefers-reduced-motion: reduce)");
      const f = () => setR(q.matches);
      f();
      q.addEventListener ? q.addEventListener("change", f) : q.addListener(f);
      return () => q.removeEventListener ? q.removeEventListener("change", f) : q.removeListener(f);
    }, []);
    return r;
  }

  // componentes/src/content.js
  var EXPERTS = ["Datos e IA", "Tech corporativo", "Alan Tapia"];
  var THEMES = ["Margen", "Plataformas", "Gente"];
  var content = {
    edition: "Edición 01",
    hero: {
      sub: "Sentate a la mesa con los CEOs de las cadenas gastronómicas más grandes del país y los referentes tech del sector.",
      stats: [
        { value: "15", label: "CEOs" },
        { value: "3", label: "Mesas" },
        { value: "3", label: "Expertos tech" },
        { value: "1", label: "Noche" }
      ],
      meta: ["Sábado 21 de noviembre de 2026", "Buenos Aires", "Una sola noche", "Por invitación"]
    },
    pitch: "Los CEOs de las cadenas más grandes del país no tienen dónde hablar entre ellos. *Esta noche existe para eso.*",
    why: {
      kicker: "Por qué existe",
      title: "Las decisiones de tecnología más difíciles *se toman solas*.",
      lede: "Los CEOs de las cadenas más grandes del país toman todos los días decisiones de tecnología que mueven millones, y casi siempre las toman solos. Tienen proveedores que les venden, consultores que les cobran y eventos donde los miran, pero no tienen un lugar donde sentarse con otros que están viviendo lo mismo. La Mesa existe para eso: cada uno llega con el desafío que hoy tiene su compañía y se va habiéndolo trabajado con quienes mejor lo pueden entender."
    },
    rules: {
      kicker: "Las tres reglas",
      title: "Todo lo demás se construye sobre *estas tres cosas*.",
      lede: "No son detalles de producción. Si alguna se cae, la noche deja de funcionar.",
      items: [
        { n: "Regla 01", title: "Nadie compite con nadie", body: "Una sola marca por categoría. No hay dos cadenas de hamburguesas, ni dos de café, en la misma sala.", why: "Es lo que permite que digan números reales. Con un competidor enfrente, nadie habla." },
        { n: "Regla 02", title: "Tres expertos que rotan", body: "Tres referentes de tecnología, elegidos para estos desafíos. Uno por mesa, y cambian de mesa con cada plato.", why: "Al final de la noche, cada CEO trabajó su desafío con los tres." },
        { n: "Regla 03", title: "Cada uno trae su desafío", body: "Una semana antes, cada CEO nos manda el desafío de tecnología que hoy tiene por delante su compañía.", why: "Con esos quince desafíos armamos las mesas. Se habla de sus problemas, no de un temario nuestro." }
      ]
    },
    steps: {
      kicker: "Una semana antes",
      title: "Los temas de la noche *los escriben ellos*.",
      lede: "La cena no se diseña en un escritorio. Se diseña con los quince desafíos que mandan una semana antes.",
      items: [
        { value: "15", title: "Desafíos que entran", body: "Cada CEO manda uno, en una frase: el problema de tecnología que hoy tiene su compañía. No teoría ni tendencias. Lo que le está costando plata." },
        { value: "1", title: "Una lectura, buscando patrones", body: "Las leemos todas juntas y vemos qué se repite. Donde tres cadenas distintas coinciden, hay un tema de mesa. Donde alguien está solo, le buscamos el experto que mejor le sirve." },
        { value: "3", title: "Temas que salen", body: "De esos patrones salen los tres temas de las mesas, qué experto va a cada una y quién se sienta al lado de quién. Cuando llegan, la conversación ya está diseñada sobre lo que ellos mismos plantearon." }
      ],
      note: "Y de nuestro lado queda un mapa de lo que la industria no sabe resolver, escrito por los quince CEOs que más locales manejan del país."
    },
    story: {
      kicker: "El relato",
      title: "Cómo pasa *la noche*.",
      lede: "Nueve momentos, en orden. Tocá cualquiera para ver qué está pasando en el salón.",
      scenes: [
        {
          h: "20:00",
          k: "La puerta",
          image: "invitacion",
          t: "Entran de a uno y la cámara ya está grabando. **Tomás Fonzi los recibe en la puerta**, los saluda por su nombre y los va presentando entre ellos. Nadie llega y se queda parado solo con una copa: desde el primer minuto hay alguien conectando gente.",
          pin: "La llegada no se deja librada al azar. Es la primera escena de toda la pieza.",
          note: "El salón espera con los nombres puestos y el menú de cada uno en su lugar.",
          cam: 1,
          open: 0,
          voice: "Tomás Fonzi",
          course: -1
        },
        {
          h: "20:30",
          k: "Cada uno a su lugar",
          image: "mesa",
          t: "Pasan al salón y buscan su nombre. **Nadie elige dónde se sienta.** Las tres mesas están armadas por nosotros a partir de los desafíos que mandaron: cinco CEOs y un experto en cada una, ningún competidor compartiendo mantel, y los desafíos parecidos cerca. **La cena se pide desde el sistema de Deenex**, y en el menú de cada mesa están impresos los desafíos que se van a trabajar.",
          pin: "Quién se sienta al lado de quién es la mitad del valor de la noche.",
          note: "Tres mesas de seis. Los temas salen de los desafíos que mandaron.",
          cam: 1,
          open: 0,
          voice: "Tomás Fonzi",
          course: 0
        },
        {
          h: "20:45",
          k: "Primer plato",
          image: "sala",
          t: "Arranca la cena y, con ella, la conversación. **Acá se apagan las cámaras de adentro.** Se filma desde afuera, sin audio: planos del salón, las manos, los platos, el clima. Lo que se dice en la mesa no se graba, y eso lo saben desde que confirmaron.",
          pin: "Es la única parte de la noche que no existe en video. Por eso se habla en serio.",
          note: "Cámaras solo desde afuera. Sin audio de mesas.",
          cam: 0,
          open: 0,
          voice: "Las mesas",
          course: 0
        },
        {
          h: "21:15",
          k: "El confesionario",
          image: "confesionario",
          t: "De a uno se levantan y pasan a una sala aparte. **Noventa segundos, una silla, una sola pregunta que nadie conoce hasta que se sienta:** “¿Qué hace toda la industria que a vos te parece una locura?”. Del otro lado está Fonzi. La misma pregunta para los quince: el valor no está en cada respuesta, está en la comparación.",
          pin: "Quince respuestas a la misma pregunta son un documento sobre el estado del rubro.",
          note: "La cena sigue. El confesionario corre en paralelo toda la noche.",
          cam: 1,
          open: 0,
          voice: "Tomás Fonzi",
          course: 0
        },
        {
          h: "21:40",
          k: "Segundo plato",
          image: "sala",
          t: "Cambia el plato y **rotan los expertos**. El de datos pasa a la mesa que tenía al de corporativo, y así. Cada mesa estrena interlocutor y tema sin moverse de su silla.",
          pin: "Los CEOs se quedan. Lo que rota es la tecnología.",
          note: "Primera rotación. Cada mesa cambia de experto y de tema.",
          cam: 0,
          open: 0,
          voice: "Las mesas",
          course: 1
        },
        {
          h: "22:00",
          k: "La cocina, a todo ritmo",
          image: "cocina",
          t: "En paralelo a todo, la cocina abierta no para. **Un chef de primera categoría, cocinando a la vista de la mesa.** Esta es la parte que se filma como documental: el pase, el reloj, la presión, los platos saliendo. Es lo que hace que todo se vea caro.",
          pin: "El ritmo y la tensión que se ven en cámara los pone la cocina, no la mesa.",
          note: "La cocina es escenografía y es contenido al mismo tiempo.",
          cam: 1,
          open: 0,
          voice: "El chef",
          course: 1
        },
        {
          h: "22:30",
          k: "Tercer plato",
          image: "sala",
          t: "Última rotación. **Al terminar este plato, cada CEO pasó por los tres expertos y los tres temas**, sin haberse levantado de la silla. Los quince desafíos ya pasaron por los tres expertos.",
          pin: "Tres conversaciones distintas, una sola cena.",
          note: "Segunda rotación. Se completa el circuito.",
          cam: 0,
          open: 0,
          voice: "Las mesas",
          course: 2
        },
        {
          h: "23:00",
          k: "La servilleta",
          image: "servilleta",
          t: "Antes del postre, cada mesa tiene cinco minutos para ponerse de acuerdo en una conclusión. **La escriben en una servilleta y la firman los seis.** Después, un abanderado por mesa se para, lee lo que firmaron y cuenta por qué llegaron a eso. Las tres servilletas son lo único de la conversación que se publica.",
          pin: "Tres servilletas firmadas, tres abanderados. Es la pieza que cierra la noche.",
          note: "Cinco minutos por mesa. La cámara vuelve a entrar para los abanderados.",
          cam: 1,
          open: 0,
          voice: "Tomás Fonzi",
          course: 2
        },
        {
          h: "23:30",
          k: "Se abre la sala",
          image: "copas",
          t: "Se levantan las mesas y baja un DJ de música chill. Todos de pie, con una copa. **Recién acá entran los representantes de los partners** y hablan con los quince, sin haber interrumpido a nadie durante toda la cena.",
          pin: "Es el momento que los partners se ganaron justamente por no molestar antes.",
          note: "Networking abierto. Noventa minutos, con alguien del equipo presentando gente a propósito.",
          cam: 1,
          open: 1,
          voice: "DJ · todos con todos",
          course: -1
        }
      ]
    },
    closing: {
      kicker: "El cierre",
      title: "Tres servilletas. *Tres conclusiones firmadas.*",
      lede: "Es lo único de la conversación de las mesas que se publica. Y es la imagen que cierra la noche.",
      napkin: { label: "La Mesa · Mesa 02 · 21.11.26", quote: "Antes de comprar cualquier tecnología, primero hay que ordenar los datos de venta." },
      items: [
        { n: "5′", title: "Una conclusión por mesa", body: "Antes del postre, cada mesa tiene cinco minutos para ponerse de acuerdo en una sola frase." },
        { n: "6", title: "La escriben y la firman", body: "En una servilleta de tela con el logo de La Mesa. Firman los cinco CEOs y el experto de esa mesa." },
        { n: "1", title: "Un abanderado", body: "La mesa elige a uno. Se para, lee lo que firmaron y cuenta por qué llegaron a eso. Acá la cámara vuelve a entrar." },
        { n: "3", title: "Tres piezas", body: "Cada servilleta con su abanderado es una pieza publicada. Después, las servilletas se enmarcan y se le regalan a cada mesa." }
      ]
    },
    room: {
      kicker: "La sala",
      title: "Dieciocho sillas. *Tres mesas de seis*, exactas.",
      lede: "Quince CEOs y tres expertos en tecnología. Cinco CEOs y un experto por mesa. El experto rota con cada plato, así que al final de la noche cada CEO pasó por los tres. Los temas de cada mesa no los elegimos nosotros: salen de los desafíos que mandaron la semana anterior.",
      cast: [
        { role: "Experto 01", name: "Datos e IA", body: "Ve por dentro lo que pasa en cientos de locales. Trae números agregados y benchmarks, no opiniones." },
        { role: "Experto 02", name: "Tecnología corporativa", body: "Viene del mundo corpo y de otras industrias. Dice en diez minutos algo que en gastronomía nadie escuchó nunca." },
        { role: "Experto 03", name: "Alan Tapia · Deenex", body: "Canales propios e infraestructura. La mirada de quien construye el sistema sobre el que venden las cadenas." },
        { role: "Anfitrión", name: "Tomás Fonzi", body: "Recibe en la puerta, presenta a cada uno y hace las entrevistas del confesionario. Finalista de MasterChef Celebrity." },
        { role: "Cocina", name: "Un chef de primera", body: "Cocina a la vista toda la noche. La mesa son quince personas que viven de la comida: el plato no se discute." },
        { role: "Invitados", name: "Quince CEOs", body: "CEOs de las cadenas gastronómicas más grandes del país. Uno por categoría. El lugar en la mesa lo asignamos nosotros." }
      ]
    },
    partners: {
      kicker: "Partners",
      title: "No hay activaciones. Hay cosas que *simplemente funcionan*.",
      lede: "La regla es una sola: si el producto del partner es cómo funciona la noche, entra. Si hay que mostrárselo a alguien, no entra. Nadie da un speech, nadie reparte nada, no hay un solo rollup.",
      rows: [
        { name: "Deenex", role: "El sistema de la noche", lead: "Así se pide la cena.", body: "Cada mesa tiene su pantalla y todos eligen sus platos desde el sistema de Deenex. Quince CEOs de cadenas usando el producto durante tres horas, sin que nadie se los presente y sin una sola diapositiva.", strong: "Este lugar no se vende.", host: true, image: "pantalla" },
        { name: "AQA", role: "Partner de experiencia", lead: "Así se toma el agua.", body: "Sus equipos a la vista, botellas de vidrio en cada mesa y en el set del confesionario. Está en la mano de todos toda la noche.", image: "copas" },
        { name: "Dos lugares", role: "A definir", lead: "Mismo criterio para los que faltan.", body: "Pagos que se resuelven sin un solo papel, el maridaje, los equipos de la cocina. Se busca la marca que encaje en el flow, no la que quiera pantalla." },
        { name: "El after", role: "Su momento real", lead: "Acá cobran lo que pagaron.", body: "Durante la cena los partners no interrumpen a nadie. Cuando se abre la sala, entran sus representantes y hablan con los quince, de pie y con una copa en la mano. Es el mejor momento posible y se lo ganaron no molestando antes.", after: true }
      ]
    },
    tiers: {
      kicker: "En evaluación",
      title: "Rubros que *encajan*.",
      lede: "Candidatos para los lugares que faltan, ordenados por qué tan natural es su presencia en la noche. Ninguno está confirmado.",
      groups: [
        { title: "Son la noche", note: "Su producto es indistinguible de la experiencia. Nadie tiene que explicar qué hacen.", items: [
          { name: "Equipamiento de cocina", brands: "Rational · Unox · Winterhalter · Electrolux Pro", body: "El chef cocina en sus hornos, a la vista de la mesa. Un chef de primera usando su equipo adelante de los CEOs de quince cadenas que compran exactamente eso." },
          { name: "Una bodega", brands: "Catena · Rutini · Zuccardi · Susana Balbo", body: "El maridaje de la cena, con sommelier presentando cada copa. Las cadenas arman cartas de vinos; una cena es literalmente su canal." },
          { name: "Pagos", brands: "Mercado Pago · MODO · Getnet", body: "La noche no tiene un solo papel. Todo lo que se cobra corre por su rail, incluida la barra del after." },
          { name: "Café", brands: "Proveedor B2B, no una cadena", body: "El cierre de la cena con un barista. Una cadena de cafeterías sería competencia de un invitado." },
          { name: "Cristalería", brands: "Riedel", body: "Las copas del maridaje. Difícil de conseguir, impecable en cámara." }
        ] },
        { title: "Tocan la noche", note: "Están presentes sin ser el centro. Funcionan si se integran de verdad.", items: [
          { name: "Insumos", brands: "Mastellone · McCain · Arcor foodservice", body: "Un ingrediente del menú, siempre que el chef lo haya elegido. Si se nota el chivo, se cae." },
          { name: "Packaging", brands: "El regalo de despedida", body: "Lo que cada uno se lleva sale en su packaging. Chico, pero es el rubro que más necesita estar frente a estas quince personas." },
          { name: "Traslados", brands: "Audi · BMW · Volvo", body: "Llevan y traen a los quince. Las automotrices premium hacen esto para cenas de CEOs y tienen partida asignada." },
          { name: "La sede", brands: "Un hotel", body: "Pone el salón a cambio de ser el escenario. Te ahorra el costo más grande de la producción. Un grupo gastronómico no, porque compite con la mesa." }
        ] },
        { title: "Compran la silla", note: "Su producto no está en la sala: lo que compran es el acceso. Es una sola silla.", items: [
          { name: "Banco de empresas", brands: "Galicia · Santander · Macro", body: "Tienen presupuesto de relacionamiento y buscan exactamente este perfil. Suele ser el cheque más grande y el más fácil de justificar internamente." },
          { name: "Consultora", brands: "Práctica de consumo y retail", body: "Mismo razonamiento que el banco: pagan por sentarse entre pares, no por mostrar nada." },
          { name: "Gestión de personal", brands: "Software de turnos y equipos", body: "Conecta con uno de los tres temas de la mesa, así que su presencia se justifica sola." }
        ] }
      ],
      note: "La regla de no competir también corre para los partners: si entra una marca de café, no puede haber una cadena de cafeterías sentada a la mesa."
    },
    calendar: {
      kicker: "Calendario",
      title: "De hoy al *21 de noviembre*.",
      lede: "Es sábado, y muchos CEOs reservan el fin de semana. Conviene invitar a un par de más contando con algunos que no van a poder.",
      rows: [
        { date: "Hasta el 30 de octubre", text: "**Invitaciones, una por una y por teléfono.** Primero dos o tres anclas de peso; con esos nombres se invita al resto." },
        { date: "Hasta el 6 de noviembre", text: "**Partners cerrados** y chef, sede y DJ confirmados." },
        { date: "Viernes 13 de noviembre", text: "**Fecha límite de los desafíos.** Cada CEO manda el suyo en una frase. Se persigue a los que falten.", mark: true },
        { date: "14 y 15 de noviembre", text: "**Lectura de los quince desafíos.** Salen los temas de cada mesa, qué experto va a cada una y quién se sienta al lado de quién." },
        { date: "Semana del 16", text: "**Briefing a los expertos**, impresión de menús, servilletas y ajustes de producción." },
        { date: "Sábado 21 de noviembre", text: "**La Mesa.**", mark: true, final: true }
      ]
    },
    cameras: {
      kicker: "Las cámaras",
      title: "Todo se graba. Menos *lo único que no puede salir*.",
      lede: "La noche entera se filma como documental: la llegada, la cocina, el confesionario, el after. Lo único que nunca tiene una cámara adentro es la conversación de las mesas.",
      filmed: ["La llegada y las presentaciones en la puerta", "Fonzi recibiendo a cada uno", "La cocina, a todo ritmo, como documental", "El confesionario: quince piezas de noventa segundos", "Las tres servilletas firmadas y el abanderado de cada mesa explicando su conclusión", "El after, el brindis y el DJ", "Las mesas, desde afuera y sin audio: planos generales, manos, platos, clima"],
      never: ["Quién dijo qué en las mesas", "Los números que alguien tire, con nombre y apellido", "De qué compañía es cada desafío", "Cualquier cosa que un invitado no apruebe sobre sí mismo"],
      note: "No mostrar la conversación es lo que hace que quieran estar sentados la próxima vez."
    },
    footer: {
      line: "La Mesa · Edición 01 · Buenos Aires, 21 de noviembre de 2026",
      disclaimer: "Documento interno de trabajo. Nombre, fecha, sede, chef y partners sujetos a confirmación."
    }
  };

  // componentes/src/assets.js
  var assets = {
    logoInk: "/_blob/c63cd71aafe45f1e412fae1f8ad170b7",
    logoPaper: "/_blob/0db91ef2892150991fbbb542a4512882",
    mesa: "/_blob/94440a1db7e0127808bfc1ccf2175a18",
    invitacion: "/_blob/ad5d61aeeec4cf7c24e86cdb667695b1",
    servilleta: "/_blob/f77379931bae1c70c02150def849e149",
    sala: "/_blob/aef96384484ae4a6c5c27a3343efcf90",
    confesionario: "/_blob/4db26ec2756ca40ef30e60fbc1c5400a",
    cocina: "/_blob/2193403ddf276ce780aa8783a90058da",
    copas: "/_blob/66828f2d00bce08f8061c9f17dcfd692",
    pantalla: "/_blob/840dd0a618162eded4cfa5f9b2c5e41c"
  };
  function setAssets(map) {
    Object.assign(assets, map || {});
    return assets;
  }
  function asset(key) {
    return key && assets[key] || key;
  }
  var photos = {
    mesa: { alt: "El cubierto de la Mesa 02 servido de noche: plato de porcelana sobre bajo plato de gres negro, el menú impreso apoyado en el plato, servilleta violeta con tenedor de bronce, copas de cristal, la tarjeta de lugar “Café” y, al fondo, velas y la pantalla de Deenex encendida.", n: "Objeto 01", title: "El cubierto", detail: "Mesa 02 · lugar 04" },
    invitacion: { alt: "Invitación de cartulina negra con “La Mesa” estampado en foil lila y canto pintado violeta, apoyada sobre un sobre lila cerrado con lacre violeta, sobre terciopelo.", n: "Objeto 02", title: "La invitación", detail: "Algodón 1,7 mm · foil lila · canto violeta" },
    pantalla: { alt: "La pantalla de la mesa en su soporte de bronce, mostrando el sistema de Deenex para elegir el segundo plato, con velas desenfocadas detrás.", n: "Objeto 03", title: "La pantalla de la mesa", detail: "Sistema Deenex" },
    servilleta: { alt: "Servilleta de lino blanca vista desde arriba con la conclusión de la Mesa 02 escrita a mano, seis firmas y “La Mesa” bordado en violeta; al lado, una lapicera negra y una copa con vino.", n: "Objeto 04", title: "La servilleta firmada", detail: "Lino · bordado violeta · 46 × 46 cm" },
    confesionario: { alt: "Un sillón de terciopelo violeta solo, bajo un cenital que dibuja un cono de luz en la bruma, junto a una mesa auxiliar con un vaso de agua.", n: "Objeto 05", title: "El confesionario", detail: "Una silla · noventa segundos" },
    copas: { alt: "Botella de vidrio con agua, un vaso y una copa con vino tinto sobre mármol negro, recortados contra una luz violeta.", n: "Objeto 06", title: "Agua y maridaje", detail: "Vidrio · cristal · mármol" },
    sala: { alt: "Planta cenital del salón: tres mesas redondas de seis con mantel oscuro, sillas de terciopelo violeta, cubiertos servidos y una pantalla encendida en el centro de cada mesa.", n: "Planta", title: "Tres mesas de seis", detail: "18 sillas" },
    cocina: { alt: "El pase de la cocina: platos bajo campanas de acero en una mesada, lámparas de calor encendidas y las comandas de las tres mesas colgadas del riel.", n: "Objeto 07", title: "El pase", detail: "Cocina a la vista" }
  };
  var plan = {
    tables: [
      { id: "01", x: 18.55, y: 46.34, r: 9.15, seat: { x: 19, y: 27.76 } },
      { id: "02", x: 50, y: 54.47, r: 9.15, seat: { x: 44.76, y: 38.27 } },
      { id: "03", x: 81.45, y: 46.34, r: 9.15, seat: { x: 81, y: 27.76 } }
    ]
  };

  // componentes/src/primitives.jsx
  var React2 = window.React;
  function Kicker({ children, tone = "accent", rule = true, as: Tag = "span", className }) {
    return /* @__PURE__ */ React2.createElement(Tag, { className: cx("lm-kicker", "kicker", `lm-kicker--${tone}`, rule && "lm-kicker--rule", className) }, children);
  }
  function Hashtag({ className }) {
    return /* @__PURE__ */ React2.createElement("span", { className: cx("lm-hashtag", className) }, "#Deene", /* @__PURE__ */ React2.createElement("b", null, "X"), "perience");
  }
  function Logo({ height = 22, tone = "auto", className }) {
    const s = { height };
    if (tone === "ink") return /* @__PURE__ */ React2.createElement("img", { className: cx("lm-logo", className), src: asset("logoInk"), alt: "Deenex", style: s });
    if (tone === "paper") return /* @__PURE__ */ React2.createElement("img", { className: cx("lm-logo", className), src: asset("logoPaper"), alt: "Deenex", style: s });
    return /* @__PURE__ */ React2.createElement("span", { className: cx("lm-logo", "lm-logo--auto", className), style: s }, /* @__PURE__ */ React2.createElement("img", { className: "lm-logo__paper", src: asset("logoPaper"), alt: "Deenex", style: s }), /* @__PURE__ */ React2.createElement("img", { className: "lm-logo__ink", src: asset("logoInk"), alt: "", "aria-hidden": "true", style: s }));
  }
  function Button({ variant = "primary", arrow, href, children, className, ...rest }) {
    const body = /* @__PURE__ */ React2.createElement(React2.Fragment, null, arrow === "left" && /* @__PURE__ */ React2.createElement("span", { className: "lm-btn__arrow", "aria-hidden": "true" }, "←"), /* @__PURE__ */ React2.createElement("span", null, children), arrow === "right" && /* @__PURE__ */ React2.createElement("span", { className: "lm-btn__arrow", "aria-hidden": "true" }, "→"));
    const cls = cx("lm-btn", `lm-btn--${variant}`, className);
    return href ? /* @__PURE__ */ React2.createElement("a", { className: cls, href, ...rest }, body) : /* @__PURE__ */ React2.createElement("button", { type: "button", className: cls, ...rest }, body);
  }
  function StatusPill({ tone = "accent", live = false, boxed = false, children, className }) {
    return /* @__PURE__ */ React2.createElement("span", { className: cx("lm-pill", `lm-pill--${tone}`, live && "lm-pill--live", boxed && "lm-pill--boxed", className) }, /* @__PURE__ */ React2.createElement("i", { className: "lm-pill__dot", "aria-hidden": "true" }), /* @__PURE__ */ React2.createElement("span", null, children));
  }
  function Viewfinder({ rec = true, timecode, label }) {
    return /* @__PURE__ */ React2.createElement("div", { className: "lm-vf", "aria-hidden": "true" }, /* @__PURE__ */ React2.createElement("span", { className: "lm-vf__c lm-vf__c--tl" }), /* @__PURE__ */ React2.createElement("span", { className: "lm-vf__c lm-vf__c--tr" }), /* @__PURE__ */ React2.createElement("span", { className: "lm-vf__c lm-vf__c--bl" }), /* @__PURE__ */ React2.createElement("span", { className: "lm-vf__c lm-vf__c--br" }), /* @__PURE__ */ React2.createElement("div", { className: "lm-vf__top" }, rec ? /* @__PURE__ */ React2.createElement("span", { className: "lm-vf__rec" }, /* @__PURE__ */ React2.createElement("i", null), "REC") : /* @__PURE__ */ React2.createElement("span", { className: "lm-vf__off" }, /* @__PURE__ */ React2.createElement("i", null), "Sin audio · desde afuera"), timecode && /* @__PURE__ */ React2.createElement("span", { className: "lm-vf__tc" }, timecode)), label && /* @__PURE__ */ React2.createElement("div", { className: "lm-vf__bottom" }, label));
  }
  function Photo({ src, name, alt, ratio = "16 / 9", caption, position = "50% 50%", viewfinder, bleed = false, framed = false, overlay, loading = "eager", className, children }) {
    const meta = name ? photos[name] : null;
    const img = asset(src || name);
    const cap = caption === false ? null : caption || meta;
    return /* @__PURE__ */ React2.createElement("figure", { className: cx("lm-photo", bleed && "lm-photo--bleed", framed && "lm-photo--framed", className) }, /* @__PURE__ */ React2.createElement("div", { className: "lm-photo__frame", style: { aspectRatio: ratio } }, /* @__PURE__ */ React2.createElement("img", { src: img, alt: alt || meta && meta.alt || "", style: { objectPosition: position }, loading, decoding: "async" }), viewfinder && /* @__PURE__ */ React2.createElement(Viewfinder, { ...viewfinder }), overlay, children), cap && /* @__PURE__ */ React2.createElement("figcaption", { className: "lm-photo__cap meta" }, cap.n && /* @__PURE__ */ React2.createElement("span", { className: "lm-photo__n" }, cap.n), /* @__PURE__ */ React2.createElement("span", { className: "lm-photo__t" }, cap.title), cap.detail && /* @__PURE__ */ React2.createElement("span", { className: "lm-photo__d" }, cap.detail)));
  }
  function SectionHeader({ kicker, title, lede, layout = "stack", size = 2, as: Tag = "h2", id, className }) {
    return /* @__PURE__ */ React2.createElement("header", { className: cx("lm-sh", `lm-sh--${layout}`, className) }, /* @__PURE__ */ React2.createElement("div", { className: "lm-sh__main" }, kicker && /* @__PURE__ */ React2.createElement(Kicker, null, kicker), /* @__PURE__ */ React2.createElement(Tag, { id, className: cx("lm-sh__title", "lm-rich", size === 1 ? "display-1" : "display-2") }, rich(title))), lede && /* @__PURE__ */ React2.createElement("p", { className: "lm-sh__lede lede" }, rich(lede)));
  }
  function Statement({ children, cite, className }) {
    return /* @__PURE__ */ React2.createElement("blockquote", { className: cx("lm-statement", className) }, /* @__PURE__ */ React2.createElement("p", { className: "lm-statement__text quote-1 lm-rich" }, rich(children)), cite && /* @__PURE__ */ React2.createElement("cite", { className: "lm-statement__cite meta" }, cite));
  }
  function Callout({ children, className }) {
    return /* @__PURE__ */ React2.createElement("p", { className: cx("lm-callout", "quote-2", "lm-rich", className) }, rich(children));
  }

  // componentes/src/hero.jsx
  var React3 = window.React;
  function TopBar({ edition = content.edition, className }) {
    return /* @__PURE__ */ React3.createElement("div", { className: cx("lm-topbar", className) }, /* @__PURE__ */ React3.createElement(Logo, { height: 20 }), /* @__PURE__ */ React3.createElement("span", { className: "lm-topbar__hair", "aria-hidden": "true" }), /* @__PURE__ */ React3.createElement(Hashtag, null), /* @__PURE__ */ React3.createElement("span", { className: "lm-topbar__ed meta" }, edition));
  }
  function StatRow({ items = content.hero.stats, className }) {
    return /* @__PURE__ */ React3.createElement("dl", { className: cx("lm-stats", className) }, items.map((it, i) => /* @__PURE__ */ React3.createElement("div", { className: "lm-stats__cell", key: i }, /* @__PURE__ */ React3.createElement("dt", { className: "lm-stats__v numeral" }, it.value), /* @__PURE__ */ React3.createElement("dd", { className: "lm-stats__l meta" }, it.label))));
  }
  function Hero({
    image = "mesa",
    sub = content.hero.sub,
    stats = content.hero.stats,
    meta = content.hero.meta,
    edition = content.edition,
    position = "58% 50%",
    timecode = "20:30",
    className
  }) {
    return /* @__PURE__ */ React3.createElement("section", { className: cx("lm-hero", className) }, /* @__PURE__ */ React3.createElement("div", { className: "lm-hero__copy" }, /* @__PURE__ */ React3.createElement(TopBar, { edition }), /* @__PURE__ */ React3.createElement("div", { className: "lm-hero__body" }, /* @__PURE__ */ React3.createElement("h1", { className: "lm-hero__title", "aria-label": "La Mesa" }, /* @__PURE__ */ React3.createElement("span", { className: "lm-hero__la serif-hero" }, "La"), /* @__PURE__ */ React3.createElement("span", { className: "lm-hero__mesa display-hero" }, "Mesa")), /* @__PURE__ */ React3.createElement("p", { className: "lm-hero__sub lede" }, rich(sub)), /* @__PURE__ */ React3.createElement(StatRow, { items: stats }), /* @__PURE__ */ React3.createElement("ul", { className: "lm-hero__meta meta" }, meta.map((m, i) => /* @__PURE__ */ React3.createElement("li", { key: i }, m))))), /* @__PURE__ */ React3.createElement("div", { className: "lm-hero__media" }, /* @__PURE__ */ React3.createElement(Photo, { name: image, ratio: "auto", caption: false, position, viewfinder: { rec: true, timecode, label: "Mesa 02 · Lugar 04" } })));
  }

  // componentes/src/sections.jsx
  var React4 = window.React;
  function RuleGrid({ items = content.rules.items, keyIndex = -1, className }) {
    return /* @__PURE__ */ React4.createElement("ol", { className: cx("lm-rules", className) }, items.map((r, i) => {
      const [label, num] = r.n.split(" ");
      return /* @__PURE__ */ React4.createElement("li", { key: i, className: cx("lm-rules__item", i === keyIndex && "is-key") }, /* @__PURE__ */ React4.createElement("div", { className: "lm-rules__n" }, /* @__PURE__ */ React4.createElement("span", { className: "kicker" }, label), /* @__PURE__ */ React4.createElement("span", { className: "numeral" }, num)), /* @__PURE__ */ React4.createElement("h3", { className: "title-3" }, r.title), /* @__PURE__ */ React4.createElement("p", { className: "body-s" }, rich(r.body)), r.why && /* @__PURE__ */ React4.createElement("p", { className: "lm-rules__why" }, rich(r.why)));
    }));
  }
  function ProcessSteps({ items = content.steps.items, note = content.steps.note, className }) {
    return /* @__PURE__ */ React4.createElement("div", { className: cx("lm-steps", className) }, /* @__PURE__ */ React4.createElement("ol", { className: "lm-steps__list" }, items.map((s, i) => /* @__PURE__ */ React4.createElement("li", { key: i, className: "lm-steps__item" }, /* @__PURE__ */ React4.createElement("span", { className: "lm-steps__v display-1" }, s.value), i < items.length - 1 && /* @__PURE__ */ React4.createElement("span", { className: "lm-steps__arrow", "aria-hidden": "true" }, "→"), /* @__PURE__ */ React4.createElement("h3", { className: "title-3" }, s.title), /* @__PURE__ */ React4.createElement("p", { className: "body-s" }, rich(s.body))))), note && /* @__PURE__ */ React4.createElement(Callout, { className: "lm-steps__note" }, note));
  }
  function NumberedList({ items = content.closing.items, className }) {
    return /* @__PURE__ */ React4.createElement("ol", { className: cx("lm-nlist", className) }, items.map((s, i) => /* @__PURE__ */ React4.createElement("li", { key: i, className: "lm-nlist__item" }, /* @__PURE__ */ React4.createElement("span", { className: "lm-nlist__n numeral" }, s.n), /* @__PURE__ */ React4.createElement("div", null, /* @__PURE__ */ React4.createElement("h3", { className: "title-3" }, s.title), /* @__PURE__ */ React4.createElement("p", { className: "body-s" }, rich(s.body))))));
  }
  function FeatureSplit({ image, ratio = "3 / 2", caption, viewfinder, position, reverse = false, children, className }) {
    return /* @__PURE__ */ React4.createElement("div", { className: cx("lm-split", reverse && "lm-split--reverse", className) }, /* @__PURE__ */ React4.createElement("div", { className: "lm-split__media" }, /* @__PURE__ */ React4.createElement(Photo, { name: image, ratio, caption, viewfinder, position, framed: true })), /* @__PURE__ */ React4.createElement("div", { className: "lm-split__body" }, children));
  }
  function CastGrid({ items = content.room.cast, className }) {
    return /* @__PURE__ */ React4.createElement("ul", { className: cx("lm-cast", className) }, items.map((c, i) => /* @__PURE__ */ React4.createElement("li", { key: i, className: cx("lm-cast__item", /Experto/.test(c.role) && "is-expert") }, /* @__PURE__ */ React4.createElement(Kicker, { rule: false }, c.role), /* @__PURE__ */ React4.createElement("h3", { className: "lm-cast__name display-3" }, c.name), /* @__PURE__ */ React4.createElement("p", { className: "body-s" }, rich(c.body)))));
  }
  function PartnerList({ rows = content.partners.rows, images = true, className }) {
    return /* @__PURE__ */ React4.createElement("ul", { className: cx("lm-partners", className) }, rows.map((p, i) => /* @__PURE__ */ React4.createElement("li", { key: i, className: cx("lm-partners__row", p.host && "is-host", p.after && "is-after") }, /* @__PURE__ */ React4.createElement("div", { className: "lm-partners__who" }, /* @__PURE__ */ React4.createElement("h3", { className: "lm-partners__name display-3" }, p.name), /* @__PURE__ */ React4.createElement(Kicker, { rule: false, tone: p.host || p.after ? "accent" : "muted" }, p.role), p.host && /* @__PURE__ */ React4.createElement(StatusPill, { tone: "accent", boxed: true }, "Anfitrión")), /* @__PURE__ */ React4.createElement("p", { className: "lm-partners__text body" }, /* @__PURE__ */ React4.createElement("strong", null, p.lead), " ", rich(p.body), p.strong && /* @__PURE__ */ React4.createElement(React4.Fragment, null, " ", /* @__PURE__ */ React4.createElement("strong", null, p.strong))), images && p.image ? /* @__PURE__ */ React4.createElement("div", { className: "lm-partners__img" }, /* @__PURE__ */ React4.createElement(Photo, { name: p.image, ratio: "4 / 3", caption: false })) : /* @__PURE__ */ React4.createElement("div", { className: "lm-partners__img lm-partners__img--empty", "aria-hidden": "true" }))));
  }
  function CategoryTiers({ groups = content.tiers.groups, note = content.tiers.note, className }) {
    return /* @__PURE__ */ React4.createElement("div", { className: cx("lm-tiers", className) }, /* @__PURE__ */ React4.createElement("div", { className: "lm-tiers__cols" }, groups.map((g, i) => /* @__PURE__ */ React4.createElement("section", { key: i, className: "lm-tiers__col" }, /* @__PURE__ */ React4.createElement("header", { className: "lm-tiers__head" }, /* @__PURE__ */ React4.createElement(Kicker, null, g.title), /* @__PURE__ */ React4.createElement("p", { className: "body-s" }, g.note)), /* @__PURE__ */ React4.createElement("ul", null, g.items.map((it, j) => /* @__PURE__ */ React4.createElement("li", { key: j, className: "lm-tiers__item" }, /* @__PURE__ */ React4.createElement("h3", { className: "title-3" }, it.name), /* @__PURE__ */ React4.createElement("span", { className: "lm-tiers__brands meta" }, it.brands), /* @__PURE__ */ React4.createElement("p", { className: "body-s" }, rich(it.body)))))))), note && /* @__PURE__ */ React4.createElement(Callout, { className: "lm-tiers__note" }, note));
  }
  function Timeline({ rows = content.calendar.rows, className }) {
    return /* @__PURE__ */ React4.createElement("ol", { className: cx("lm-timeline", className) }, rows.map((r, i) => /* @__PURE__ */ React4.createElement("li", { key: i, className: cx("lm-timeline__row", r.mark && "is-mark", r.final && "is-final") }, /* @__PURE__ */ React4.createElement("span", { className: "lm-timeline__dot", "aria-hidden": "true" }), /* @__PURE__ */ React4.createElement("span", { className: "lm-timeline__date meta" }, r.date), /* @__PURE__ */ React4.createElement("p", { className: cx("lm-timeline__text", r.final ? "display-3" : "body") }, rich(r.text)))));
  }
  function CameraPolicy({ filmed = content.cameras.filmed, never = content.cameras.never, note = content.cameras.note, className }) {
    return /* @__PURE__ */ React4.createElement("div", { className: cx("lm-cams", className) }, /* @__PURE__ */ React4.createElement("section", { className: "lm-cams__col" }, /* @__PURE__ */ React4.createElement("h3", { className: "lm-cams__h" }, /* @__PURE__ */ React4.createElement(StatusPill, { tone: "rec", live: true }, "Lo que se filma")), /* @__PURE__ */ React4.createElement("ul", null, filmed.map((t, i) => /* @__PURE__ */ React4.createElement("li", { key: i, className: "body-s" }, rich(t))))), /* @__PURE__ */ React4.createElement("section", { className: "lm-cams__col lm-cams__col--never" }, /* @__PURE__ */ React4.createElement("h3", { className: "lm-cams__h" }, /* @__PURE__ */ React4.createElement(StatusPill, { tone: "off" }, "Lo que no sale nunca")), /* @__PURE__ */ React4.createElement("ul", null, never.map((t, i) => /* @__PURE__ */ React4.createElement("li", { key: i, className: "body-s" }, rich(t)))), note && /* @__PURE__ */ React4.createElement(Callout, null, note)));
  }
  function Footer({ line = content.footer.line, disclaimer = content.footer.disclaimer, className }) {
    return /* @__PURE__ */ React4.createElement("footer", { className: cx("lm-footer", className) }, /* @__PURE__ */ React4.createElement(Logo, { height: 18 }), /* @__PURE__ */ React4.createElement("p", { className: "lm-footer__tag" }, /* @__PURE__ */ React4.createElement(Hashtag, null)), /* @__PURE__ */ React4.createElement("p", { className: "lm-footer__line meta" }, line), disclaimer && /* @__PURE__ */ React4.createElement("p", { className: "lm-footer__disc body-s" }, disclaimer));
  }

  // componentes/src/story.jsx
  var React5 = window.React;
  var { useState, useEffect, useRef } = React5;
  var COURSES = [
    { v: -1, label: "Llegada" },
    { v: 0, label: "Primer plato" },
    { v: 1, label: "Segundo plato" },
    { v: 2, label: "Tercer plato" }
  ];
  function tableState(k, course, tableId) {
    return course < 0 ? { theme: "Mesa " + tableId, who: "5 CEOs + 1 experto" } : { theme: THEMES[k], who: EXPERTS[(k + course) % 3] };
  }
  function PlanOverlay({ course = 0, tables = plan.tables }) {
    return /* @__PURE__ */ React5.createElement("div", { className: "lm-plan__ov" }, tables.map((t, k) => {
      const st = tableState(k, course, t.id);
      return /* @__PURE__ */ React5.createElement(React5.Fragment, { key: t.id }, /* @__PURE__ */ React5.createElement("span", { className: "lm-plan__ring", style: { left: t.x + "%", top: t.y + "%", width: (t.r || 9) * 2 + "%" } }), t.seat && /* @__PURE__ */ React5.createElement("span", { className: "lm-plan__seat", style: { left: t.seat.x + "%", top: t.seat.y + "%" }, title: "Experto" }), /* @__PURE__ */ React5.createElement("div", { className: cx("lm-plan__label", t.label === "above" && "is-above"), style: { left: t.x + "%", top: (t.label === "above" ? t.y - (t.r || 9) * 1.78 - 2 : t.y + (t.r || 9) * 1.78 + 2) + "%" } }, /* @__PURE__ */ React5.createElement("span", { className: "kicker" }, "Mesa ", t.id), /* @__PURE__ */ React5.createElement("b", null, st.theme), /* @__PURE__ */ React5.createElement("span", { className: "lm-plan__who" }, st.who)));
    }));
  }
  function SeatingPlan({ image = "sala", course: initial = 0, interactive = true, caption, tables = plan.tables, className }) {
    const [course, setCourse] = useState(initial);
    useEffect(() => setCourse(initial), [initial]);
    return /* @__PURE__ */ React5.createElement("div", { className: cx("lm-plan", className) }, /* @__PURE__ */ React5.createElement(Photo, { name: image, ratio: "16 / 9", caption, overlay: /* @__PURE__ */ React5.createElement(PlanOverlay, { course, tables }), framed: true }), interactive && /* @__PURE__ */ React5.createElement("div", { className: "lm-plan__tabs", role: "tablist", "aria-label": "Momento de la cena" }, COURSES.map((c) => /* @__PURE__ */ React5.createElement("button", { key: c.v, type: "button", role: "tab", "aria-selected": c.v === course, className: cx("lm-plan__tab", c.v === course && "is-on"), onClick: () => setCourse(c.v) }, c.label)), /* @__PURE__ */ React5.createElement("span", { className: "lm-plan__legend meta" }, /* @__PURE__ */ React5.createElement("i", { className: "lm-plan__dot", "aria-hidden": "true" }), "Silla del experto · rota con cada plato")), /* @__PURE__ */ React5.createElement("ul", { className: "lm-plan__list" }, tables.map((t, k) => {
      const st = tableState(k, course, t.id);
      return /* @__PURE__ */ React5.createElement("li", { key: t.id }, /* @__PURE__ */ React5.createElement("span", { className: "kicker" }, "Mesa ", t.id), " ", /* @__PURE__ */ React5.createElement("b", null, st.theme), " · ", st.who);
    })));
  }
  function NightStory({ scenes = content.story.scenes, start = 0, className }) {
    const [cur, setCur] = useState(start);
    const reduced = useReducedMotion();
    const root = useRef(null);
    const sc = scenes[cur];
    const go = (i) => setCur(Math.max(0, Math.min(scenes.length - 1, i)));
    const images = Array.from(new Set(scenes.map((s) => s.image)));
    const onKey = (e) => {
      if (e.key === "ArrowRight") {
        e.preventDefault();
        go(cur + 1);
      }
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        go(cur - 1);
      }
    };
    return /* @__PURE__ */ React5.createElement("div", { className: cx("lm-story", reduced && "is-reduced", className), ref: root, onKeyDown: onKey }, /* @__PURE__ */ React5.createElement("div", { className: "lm-story__scrub", role: "tablist", "aria-label": "Momentos de la noche" }, /* @__PURE__ */ React5.createElement("span", { className: "lm-story__track", "aria-hidden": "true" }, /* @__PURE__ */ React5.createElement("span", { style: { width: cur / (scenes.length - 1) * 100 + "%" } })), scenes.map((s, i) => /* @__PURE__ */ React5.createElement(
      "button",
      {
        key: i,
        type: "button",
        role: "tab",
        "aria-selected": i === cur,
        tabIndex: i === cur ? 0 : -1,
        className: cx("lm-story__stop", i === cur && "is-on", i < cur && "is-past"),
        onClick: () => go(i)
      },
      /* @__PURE__ */ React5.createElement("i", { "aria-hidden": "true" }),
      /* @__PURE__ */ React5.createElement("span", { className: "lm-story__h timecode" }, s.h),
      /* @__PURE__ */ React5.createElement("span", { className: "lm-story__k" }, s.k)
    ))), /* @__PURE__ */ React5.createElement("div", { className: "lm-story__grid" }, /* @__PURE__ */ React5.createElement("div", { className: "lm-story__stage" }, images.map((key) => /* @__PURE__ */ React5.createElement(
      "img",
      {
        key,
        src: asset(key),
        alt: key === sc.image ? photos[key] ? photos[key].alt : "" : "",
        "aria-hidden": key === sc.image ? void 0 : "true",
        className: cx("lm-story__img", key === sc.image && "is-on")
      }
    )), sc.image === "sala" && /* @__PURE__ */ React5.createElement(PlanOverlay, { course: sc.course }), /* @__PURE__ */ React5.createElement(Viewfinder, { rec: sc.cam === 1, timecode: sc.h, label: "Momento " + String(cur + 1).padStart(2, "0") + " / " + String(scenes.length).padStart(2, "0") })), /* @__PURE__ */ React5.createElement("div", { className: "lm-story__panel", role: "tabpanel", "aria-live": "polite" }, /* @__PURE__ */ React5.createElement("span", { className: "lm-story__count meta" }, "Momento ", cur + 1, " de ", scenes.length, " · ", sc.h), /* @__PURE__ */ React5.createElement("h3", { className: "lm-story__title display-3" }, sc.k), /* @__PURE__ */ React5.createElement("p", { className: "lm-story__text body" }, rich(sc.t)), /* @__PURE__ */ React5.createElement("p", { className: "lm-story__pin quote-2" }, sc.pin), /* @__PURE__ */ React5.createElement("div", { className: "lm-story__status" }, /* @__PURE__ */ React5.createElement(StatusPill, { tone: sc.cam ? "rec" : "off", live: !!sc.cam }, sc.cam ? "Cámaras grabando" : "Cámaras solo desde afuera"), /* @__PURE__ */ React5.createElement(StatusPill, { tone: sc.open ? "accent" : "muted" }, sc.open ? "Abierta · entran los partners" : "A puertas cerradas"), /* @__PURE__ */ React5.createElement(StatusPill, { tone: "accent" }, sc.voice)), /* @__PURE__ */ React5.createElement("p", { className: "lm-story__note body-s" }, sc.note), /* @__PURE__ */ React5.createElement("div", { className: "lm-story__nav" }, /* @__PURE__ */ React5.createElement(Button, { variant: "ghost", arrow: "left", disabled: cur === 0, onClick: () => go(cur - 1) }, "Antes"), /* @__PURE__ */ React5.createElement(Button, { variant: "ghost", arrow: "right", disabled: cur === scenes.length - 1, onClick: () => go(cur + 1) }, "Después")))));
  }

  // componentes/src/index.jsx
  window.LaMesa = {
    Kicker,
    Hashtag,
    Logo,
    Button,
    StatusPill,
    Viewfinder,
    Photo,
    SectionHeader,
    Statement,
    Callout,
    TopBar,
    StatRow,
    Hero,
    RuleGrid,
    ProcessSteps,
    NightStory,
    NumberedList,
    FeatureSplit,
    SeatingPlan,
    CastGrid,
    PartnerList,
    CategoryTiers,
    Timeline,
    CameraPolicy,
    Footer,
    PlanOverlay,
    rich,
    content,
    EXPERTS,
    THEMES,
    assets,
    setAssets,
    asset,
    photos,
    plan
  };
})();
