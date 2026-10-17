// Pre-renderiza la página con los mismos componentes y escribe index.html (contenido legible sin JavaScript; el navegador lo hidrata).
const fs = require('fs'); const path = require('path'); const vm = require('vm');
const React = require('react'); const ReactDOMServer = require('react-dom/server');
global.React = React; global.window = global; global.window.React = React;
const root = path.join(__dirname, '..');
for (const f of ['assets/js/la-mesa.js', 'assets/js/sitio.js']) vm.runInThisContext(fs.readFileSync(path.join(root, f), 'utf8'), { filename: f });
const html = ReactDOMServer.renderToString(React.createElement(window.LaMesaSitio.Page));
const tpl = fs.readFileSync(path.join(__dirname, 'index.template.html'), 'utf8');
if (!tpl.includes('<!--SSR-->')) throw new Error('falta <!--SSR--> en la plantilla');
fs.writeFileSync(path.join(root, 'index.html'), tpl.replace('<!--SSR-->', html));
console.log('index.html', html.length, 'bytes de marcado pre-renderizado');
