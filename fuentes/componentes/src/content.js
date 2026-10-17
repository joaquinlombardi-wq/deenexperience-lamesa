// Edición 01 — every line of copy from the source page, as data.
// Markup convention inside strings: *acento* → serif italic in text-accent; **fuerte** → strong.
export const EXPERTS = ['Datos e IA', 'Tech corporativo', 'Alan Tapia'];
export const THEMES = ['Margen', 'Plataformas', 'Gente'];

export const content = {
  edition: 'Edición 01',
  hero: {
    sub: 'Sentate a la mesa con los CEOs de las cadenas gastronómicas más grandes del país y los referentes tech del sector.',
    stats: [
      { value: '15', label: 'CEOs' },
      { value: '3', label: 'Mesas' },
      { value: '3', label: 'Expertos tech' },
      { value: '1', label: 'Noche' }
    ],
    meta: ['Sábado 21 de noviembre de 2026', 'Buenos Aires', 'Una sola noche', 'Por invitación']
  },
  pitch: 'Los CEOs de las cadenas más grandes del país no tienen dónde hablar entre ellos. *Esta noche existe para eso.*',
  why: {
    kicker: 'Por qué existe',
    title: 'Las decisiones de tecnología más difíciles *se toman solas*.',
    lede: 'Los CEOs de las cadenas más grandes del país toman todos los días decisiones de tecnología que mueven millones, y casi siempre las toman solos. Tienen proveedores que les venden, consultores que les cobran y eventos donde los miran, pero no tienen un lugar donde sentarse con otros que están viviendo lo mismo. La Mesa existe para eso: cada uno llega con el desafío que hoy tiene su compañía y se va habiéndolo trabajado con quienes mejor lo pueden entender.'
  },
  rules: {
    kicker: 'Las tres reglas',
    title: 'Todo lo demás se construye sobre *estas tres cosas*.',
    lede: 'No son detalles de producción. Si alguna se cae, la noche deja de funcionar.',
    items: [
      { n: 'Regla 01', title: 'Nadie compite con nadie', body: 'Una sola marca por categoría. No hay dos cadenas de hamburguesas, ni dos de café, en la misma sala.', why: 'Es lo que permite que digan números reales. Con un competidor enfrente, nadie habla.' },
      { n: 'Regla 02', title: 'Tres expertos que rotan', body: 'Tres referentes de tecnología, elegidos para estos desafíos. Uno por mesa, y cambian de mesa con cada plato.', why: 'Al final de la noche, cada CEO trabajó su desafío con los tres.' },
      { n: 'Regla 03', title: 'Cada uno trae su desafío', body: 'Una semana antes, cada CEO nos manda el desafío de tecnología que hoy tiene por delante su compañía.', why: 'Con esos quince desafíos armamos las mesas. Se habla de sus problemas, no de un temario nuestro.' }
    ]
  },
  steps: {
    kicker: 'Una semana antes',
    title: 'Los temas de la noche *los escriben ellos*.',
    lede: 'La cena no se diseña en un escritorio. Se diseña con los quince desafíos que mandan una semana antes.',
    items: [
      { value: '15', title: 'Desafíos que entran', body: 'Cada CEO manda uno, en una frase: el problema de tecnología que hoy tiene su compañía. No teoría ni tendencias. Lo que le está costando plata.' },
      { value: '1', title: 'Una lectura, buscando patrones', body: 'Las leemos todas juntas y vemos qué se repite. Donde tres cadenas distintas coinciden, hay un tema de mesa. Donde alguien está solo, le buscamos el experto que mejor le sirve.' },
      { value: '3', title: 'Temas que salen', body: 'De esos patrones salen los tres temas de las mesas, qué experto va a cada una y quién se sienta al lado de quién. Cuando llegan, la conversación ya está diseñada sobre lo que ellos mismos plantearon.' }
    ],
    note: 'Y de nuestro lado queda un mapa de lo que la industria no sabe resolver, escrito por los quince CEOs que más locales manejan del país.'
  },
  story: {
    kicker: 'El relato',
    title: 'Cómo pasa *la noche*.',
    lede: 'Nueve momentos, en orden. Tocá cualquiera para ver qué está pasando en el salón.',
    scenes: [
      { h: '20:00', k: 'La puerta', image: 'invitacion',
        t: 'Entran de a uno y la cámara ya está grabando. **Tomás Fonzi los recibe en la puerta**, los saluda por su nombre y los va presentando entre ellos. Nadie llega y se queda parado solo con una copa: desde el primer minuto hay alguien conectando gente.',
        pin: 'La llegada no se deja librada al azar. Es la primera escena de toda la pieza.',
        note: 'El salón espera con los nombres puestos y el menú de cada uno en su lugar.', cam: 1, open: 0, voice: 'Tomás Fonzi', course: -1 },
      { h: '20:30', k: 'Cada uno a su lugar', image: 'mesa',
        t: 'Pasan al salón y buscan su nombre. **Nadie elige dónde se sienta.** Las tres mesas están armadas por nosotros a partir de los desafíos que mandaron: cinco CEOs y un experto en cada una, ningún competidor compartiendo mantel, y los desafíos parecidos cerca. **La cena se pide desde el sistema de Deenex**, y en el menú de cada mesa están impresos los desafíos que se van a trabajar.',
        pin: 'Quién se sienta al lado de quién es la mitad del valor de la noche.',
        note: 'Tres mesas de seis. Los temas salen de los desafíos que mandaron.', cam: 1, open: 0, voice: 'Tomás Fonzi', course: 0 },
      { h: '20:45', k: 'Primer plato', image: 'sala',
        t: 'Arranca la cena y, con ella, la conversación. **Acá se apagan las cámaras de adentro.** Se filma desde afuera, sin audio: planos del salón, las manos, los platos, el clima. Lo que se dice en la mesa no se graba, y eso lo saben desde que confirmaron.',
        pin: 'Es la única parte de la noche que no existe en video. Por eso se habla en serio.',
        note: 'Cámaras solo desde afuera. Sin audio de mesas.', cam: 0, open: 0, voice: 'Las mesas', course: 0 },
      { h: '21:15', k: 'El confesionario', image: 'confesionario',
        t: 'De a uno se levantan y pasan a una sala aparte. **Noventa segundos, una silla, una sola pregunta que nadie conoce hasta que se sienta:** “¿Qué hace toda la industria que a vos te parece una locura?”. Del otro lado está Fonzi. La misma pregunta para los quince: el valor no está en cada respuesta, está en la comparación.',
        pin: 'Quince respuestas a la misma pregunta son un documento sobre el estado del rubro.',
        note: 'La cena sigue. El confesionario corre en paralelo toda la noche.', cam: 1, open: 0, voice: 'Tomás Fonzi', course: 0 },
      { h: '21:40', k: 'Segundo plato', image: 'sala',
        t: 'Cambia el plato y **rotan los expertos**. El de datos pasa a la mesa que tenía al de corporativo, y así. Cada mesa estrena interlocutor y tema sin moverse de su silla.',
        pin: 'Los CEOs se quedan. Lo que rota es la tecnología.',
        note: 'Primera rotación. Cada mesa cambia de experto y de tema.', cam: 0, open: 0, voice: 'Las mesas', course: 1 },
      { h: '22:00', k: 'La cocina, a todo ritmo', image: 'cocina',
        t: 'En paralelo a todo, la cocina abierta no para. **Un chef de primera categoría, cocinando a la vista de la mesa.** Esta es la parte que se filma como documental: el pase, el reloj, la presión, los platos saliendo. Es lo que hace que todo se vea caro.',
        pin: 'El ritmo y la tensión que se ven en cámara los pone la cocina, no la mesa.',
        note: 'La cocina es escenografía y es contenido al mismo tiempo.', cam: 1, open: 0, voice: 'El chef', course: 1 },
      { h: '22:30', k: 'Tercer plato', image: 'sala',
        t: 'Última rotación. **Al terminar este plato, cada CEO pasó por los tres expertos y los tres temas**, sin haberse levantado de la silla. Los quince desafíos ya pasaron por los tres expertos.',
        pin: 'Tres conversaciones distintas, una sola cena.',
        note: 'Segunda rotación. Se completa el circuito.', cam: 0, open: 0, voice: 'Las mesas', course: 2 },
      { h: '23:00', k: 'La servilleta', image: 'servilleta',
        t: 'Antes del postre, cada mesa tiene cinco minutos para ponerse de acuerdo en una conclusión. **La escriben en una servilleta y la firman los seis.** Después, un abanderado por mesa se para, lee lo que firmaron y cuenta por qué llegaron a eso. Las tres servilletas son lo único de la conversación que se publica.',
        pin: 'Tres servilletas firmadas, tres abanderados. Es la pieza que cierra la noche.',
        note: 'Cinco minutos por mesa. La cámara vuelve a entrar para los abanderados.', cam: 1, open: 0, voice: 'Tomás Fonzi', course: 2 },
      { h: '23:30', k: 'Se abre la sala', image: 'copas',
        t: 'Se levantan las mesas y baja un DJ de música chill. Todos de pie, con una copa. **Recién acá entran los representantes de los partners** y hablan con los quince, sin haber interrumpido a nadie durante toda la cena.',
        pin: 'Es el momento que los partners se ganaron justamente por no molestar antes.',
        note: 'Networking abierto. Noventa minutos, con alguien del equipo presentando gente a propósito.', cam: 1, open: 1, voice: 'DJ · todos con todos', course: -1 }
    ]
  },
  closing: {
    kicker: 'El cierre',
    title: 'Tres servilletas. *Tres conclusiones firmadas.*',
    lede: 'Es lo único de la conversación de las mesas que se publica. Y es la imagen que cierra la noche.',
    napkin: { label: 'La Mesa · Mesa 02 · 21.11.26', quote: 'Antes de comprar cualquier tecnología, primero hay que ordenar los datos de venta.' },
    items: [
      { n: '5′', title: 'Una conclusión por mesa', body: 'Antes del postre, cada mesa tiene cinco minutos para ponerse de acuerdo en una sola frase.' },
      { n: '6', title: 'La escriben y la firman', body: 'En una servilleta de tela con el logo de La Mesa. Firman los cinco CEOs y el experto de esa mesa.' },
      { n: '1', title: 'Un abanderado', body: 'La mesa elige a uno. Se para, lee lo que firmaron y cuenta por qué llegaron a eso. Acá la cámara vuelve a entrar.' },
      { n: '3', title: 'Tres piezas', body: 'Cada servilleta con su abanderado es una pieza publicada. Después, las servilletas se enmarcan y se le regalan a cada mesa.' }
    ]
  },
  room: {
    kicker: 'La sala',
    title: 'Dieciocho sillas. *Tres mesas de seis*, exactas.',
    lede: 'Quince CEOs y tres expertos en tecnología. Cinco CEOs y un experto por mesa. El experto rota con cada plato, así que al final de la noche cada CEO pasó por los tres. Los temas de cada mesa no los elegimos nosotros: salen de los desafíos que mandaron la semana anterior.',
    cast: [
      { role: 'Experto 01', name: 'Datos e IA', body: 'Ve por dentro lo que pasa en cientos de locales. Trae números agregados y benchmarks, no opiniones.' },
      { role: 'Experto 02', name: 'Tecnología corporativa', body: 'Viene del mundo corpo y de otras industrias. Dice en diez minutos algo que en gastronomía nadie escuchó nunca.' },
      { role: 'Experto 03', name: 'Alan Tapia · Deenex', body: 'Canales propios e infraestructura. La mirada de quien construye el sistema sobre el que venden las cadenas.' },
      { role: 'Anfitrión', name: 'Tomás Fonzi', body: 'Recibe en la puerta, presenta a cada uno y hace las entrevistas del confesionario. Finalista de MasterChef Celebrity.' },
      { role: 'Cocina', name: 'Un chef de primera', body: 'Cocina a la vista toda la noche. La mesa son quince personas que viven de la comida: el plato no se discute.' },
      { role: 'Invitados', name: 'Quince CEOs', body: 'CEOs de las cadenas gastronómicas más grandes del país. Uno por categoría. El lugar en la mesa lo asignamos nosotros.' }
    ]
  },
  partners: {
    kicker: 'Partners',
    title: 'No hay activaciones. Hay cosas que *simplemente funcionan*.',
    lede: 'La regla es una sola: si el producto del partner es cómo funciona la noche, entra. Si hay que mostrárselo a alguien, no entra. Nadie da un speech, nadie reparte nada, no hay un solo rollup.',
    rows: [
      { name: 'Deenex', role: 'El sistema de la noche', lead: 'Así se pide la cena.', body: 'Cada mesa tiene su pantalla y todos eligen sus platos desde el sistema de Deenex. Quince CEOs de cadenas usando el producto durante tres horas, sin que nadie se los presente y sin una sola diapositiva.', strong: 'Este lugar no se vende.', host: true, image: 'pantalla' },
      { name: 'AQA', role: 'Partner de experiencia', lead: 'Así se toma el agua.', body: 'Sus equipos a la vista, botellas de vidrio en cada mesa y en el set del confesionario. Está en la mano de todos toda la noche.', image: 'copas' },
      { name: 'Dos lugares', role: 'A definir', lead: 'Mismo criterio para los que faltan.', body: 'Pagos que se resuelven sin un solo papel, el maridaje, los equipos de la cocina. Se busca la marca que encaje en el flow, no la que quiera pantalla.' },
      { name: 'El after', role: 'Su momento real', lead: 'Acá cobran lo que pagaron.', body: 'Durante la cena los partners no interrumpen a nadie. Cuando se abre la sala, entran sus representantes y hablan con los quince, de pie y con una copa en la mano. Es el mejor momento posible y se lo ganaron no molestando antes.', after: true }
    ]
  },
  tiers: {
    kicker: 'En evaluación',
    title: 'Rubros que *encajan*.',
    lede: 'Candidatos para los lugares que faltan, ordenados por qué tan natural es su presencia en la noche. Ninguno está confirmado.',
    groups: [
      { title: 'Son la noche', note: 'Su producto es indistinguible de la experiencia. Nadie tiene que explicar qué hacen.', items: [
        { name: 'Equipamiento de cocina', brands: 'Rational · Unox · Winterhalter · Electrolux Pro', body: 'El chef cocina en sus hornos, a la vista de la mesa. Un chef de primera usando su equipo adelante de los CEOs de quince cadenas que compran exactamente eso.' },
        { name: 'Una bodega', brands: 'Catena · Rutini · Zuccardi · Susana Balbo', body: 'El maridaje de la cena, con sommelier presentando cada copa. Las cadenas arman cartas de vinos; una cena es literalmente su canal.' },
        { name: 'Pagos', brands: 'Mercado Pago · MODO · Getnet', body: 'La noche no tiene un solo papel. Todo lo que se cobra corre por su rail, incluida la barra del after.' },
        { name: 'Café', brands: 'Proveedor B2B, no una cadena', body: 'El cierre de la cena con un barista. Una cadena de cafeterías sería competencia de un invitado.' },
        { name: 'Cristalería', brands: 'Riedel', body: 'Las copas del maridaje. Difícil de conseguir, impecable en cámara.' }
      ]},
      { title: 'Tocan la noche', note: 'Están presentes sin ser el centro. Funcionan si se integran de verdad.', items: [
        { name: 'Insumos', brands: 'Mastellone · McCain · Arcor foodservice', body: 'Un ingrediente del menú, siempre que el chef lo haya elegido. Si se nota el chivo, se cae.' },
        { name: 'Packaging', brands: 'El regalo de despedida', body: 'Lo que cada uno se lleva sale en su packaging. Chico, pero es el rubro que más necesita estar frente a estas quince personas.' },
        { name: 'Traslados', brands: 'Audi · BMW · Volvo', body: 'Llevan y traen a los quince. Las automotrices premium hacen esto para cenas de CEOs y tienen partida asignada.' },
        { name: 'La sede', brands: 'Un hotel', body: 'Pone el salón a cambio de ser el escenario. Te ahorra el costo más grande de la producción. Un grupo gastronómico no, porque compite con la mesa.' }
      ]},
      { title: 'Compran la silla', note: 'Su producto no está en la sala: lo que compran es el acceso. Es una sola silla.', items: [
        { name: 'Banco de empresas', brands: 'Galicia · Santander · Macro', body: 'Tienen presupuesto de relacionamiento y buscan exactamente este perfil. Suele ser el cheque más grande y el más fácil de justificar internamente.' },
        { name: 'Consultora', brands: 'Práctica de consumo y retail', body: 'Mismo razonamiento que el banco: pagan por sentarse entre pares, no por mostrar nada.' },
        { name: 'Gestión de personal', brands: 'Software de turnos y equipos', body: 'Conecta con uno de los tres temas de la mesa, así que su presencia se justifica sola.' }
      ]}
    ],
    note: 'La regla de no competir también corre para los partners: si entra una marca de café, no puede haber una cadena de cafeterías sentada a la mesa.'
  },
  calendar: {
    kicker: 'Calendario',
    title: 'De hoy al *21 de noviembre*.',
    lede: 'Es sábado, y muchos CEOs reservan el fin de semana. Conviene invitar a un par de más contando con algunos que no van a poder.',
    rows: [
      { date: 'Hasta el 30 de octubre', text: '**Invitaciones, una por una y por teléfono.** Primero dos o tres anclas de peso; con esos nombres se invita al resto.' },
      { date: 'Hasta el 6 de noviembre', text: '**Partners cerrados** y chef, sede y DJ confirmados.' },
      { date: 'Viernes 13 de noviembre', text: '**Fecha límite de los desafíos.** Cada CEO manda el suyo en una frase. Se persigue a los que falten.', mark: true },
      { date: '14 y 15 de noviembre', text: '**Lectura de los quince desafíos.** Salen los temas de cada mesa, qué experto va a cada una y quién se sienta al lado de quién.' },
      { date: 'Semana del 16', text: '**Briefing a los expertos**, impresión de menús, servilletas y ajustes de producción.' },
      { date: 'Sábado 21 de noviembre', text: '**La Mesa.**', mark: true, final: true }
    ]
  },
  cameras: {
    kicker: 'Las cámaras',
    title: 'Todo se graba. Menos *lo único que no puede salir*.',
    lede: 'La noche entera se filma como documental: la llegada, la cocina, el confesionario, el after. Lo único que nunca tiene una cámara adentro es la conversación de las mesas.',
    filmed: ['La llegada y las presentaciones en la puerta', 'Fonzi recibiendo a cada uno', 'La cocina, a todo ritmo, como documental', 'El confesionario: quince piezas de noventa segundos', 'Las tres servilletas firmadas y el abanderado de cada mesa explicando su conclusión', 'El after, el brindis y el DJ', 'Las mesas, desde afuera y sin audio: planos generales, manos, platos, clima'],
    never: ['Quién dijo qué en las mesas', 'Los números que alguien tire, con nombre y apellido', 'De qué compañía es cada desafío', 'Cualquier cosa que un invitado no apruebe sobre sí mismo'],
    note: 'No mostrar la conversación es lo que hace que quieran estar sentados la próxima vez.'
  },
  footer: {
    line: 'La Mesa · Edición 01 · Buenos Aires, 21 de noviembre de 2026',
    disclaimer: 'Documento interno de trabajo. Nombre, fecha, sede, chef y partners sujetos a confirmación.'
  }
};
