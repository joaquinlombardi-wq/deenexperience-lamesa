# La Mesa by Deenex — sitio de la Edición 01

La landing de **La Mesa**, la cena privada de Deenex con quince CEOs de las cadenas gastronómicas más grandes del país (sábado 21 de noviembre de 2026, Buenos Aires), rediseñada como experiencia: la noche como superficie, el violeta de Deenex como luz y los objetos de la noche fotografiados como prueba.

Es un sitio estático: no necesita build para publicarse.

## Verlo en tu compu

```bash
python3 -m http.server 8000   # o: npx serve .
```

Abrí http://localhost:8000.

## Publicarlo en Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/joaquinlombardi-wq/deenexperience-lamesa)

El botón lee `render.yaml` y crea un *Static Site* llamado `la-mesa-deenex`; Render le da una URL del tipo `https://la-mesa-deenex.onrender.com`. El build (`render-build.sh`) publica solo el sitio, no `fuentes/`, y usa esa URL para la imagen al compartir. Cada push a la rama vuelve a desplegar.

A mano: en Render, **New → Static Site**, elegí este repo y la rama `main`, poné `bash render-build.sh` como *Build Command* y `dist` como *Publish Directory*.

## Publicarlo en otro lado

También se puede subir la carpeta tal cual a Netlify (arrastrar y soltar), Vercel, Cloudflare Pages o GitHub Pages. El único recurso externo es React 18.3.1 desde cdnjs; las tipografías y las imágenes van incluidas.

Antes de hacerlo público:

- **Indexación.** El `index.html` lleva `<meta name="robots" content="noindex, nofollow">` porque el contenido es un documento interno de trabajo (marcas candidatas, partners a definir). Sacalo de `index.html` y de `fuentes/index.template.html` cuando quieras que aparezca en buscadores.
- **Imagen para compartir.** En Render se completa sola. En otro hosting, cambiá la ruta relativa de `og:image` (`assets/img/og-la-mesa.jpg`) por la URL absoluta del dominio final para que se vea al compartir el link.
- **Fotografía.** Las imágenes son renders de referencia, no fotos de la noche: las firmas de la servilleta y los platos de la pantalla son ficticios. Cuando haya fotografía real, reemplazá los archivos de `assets/img/fotos/` con los mismos nombres.

## Qué hay en cada lugar

```
index.html                 la página, con el contenido pre-renderizado (se lee sin JavaScript)
favicon.svg
render.yaml                configuración del Static Site en Render
render-build.sh            build de Render: copia el sitio a dist/
assets/css/tokens.css      colores, tipografía, espacios (generado desde fuentes/tokens.json)
assets/css/la-mesa.css     estilos de los componentes
assets/css/sitio.css       ajustes propios de la página
assets/js/la-mesa.js       los componentes (generado desde fuentes/componentes/src)
assets/js/sitio.js         el orden de las secciones; hidrata el HTML en el navegador
assets/img/fotos/          las ocho fotografías de la noche
assets/fonts/              Archivo, Archivo Expanded, Instrument Serif y DM Mono (SIL Open Font License)
fuentes/                   lo necesario para regenerar todo lo anterior
```

## Cambiar textos o estilos

Toda la copia de la Edición 01 está en `fuentes/componentes/src/content.js`. Los estilos de componentes están en `assets/css/la-mesa.css` y los colores y tipografías en `fuentes/tokens.json`. Después de editar:

```bash
cd fuentes
npm install
npm run build   # regenera assets/js/la-mesa.js, assets/css/tokens.css e index.html
```

El orden de las secciones se cambia en `assets/js/sitio.js`; corré `npm run build` igual, para que el `index.html` pre-renderizado coincida.

## Accesibilidad

- El contenido completo está en el HTML; JavaScript solo agrega la interacción.
- El relato se recorre con clic o con las flechas ← → del teclado.
- Cada sección es una región con su título.
- Las animaciones se apagan con `prefers-reduced-motion`.
- Los textos cumplen 4.5:1 de contraste.
