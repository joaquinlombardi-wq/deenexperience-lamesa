#!/usr/bin/env bash
# Build de Render: publica solo el sitio (no fuentes/) en dist/.
# Con la URL pública del sitio (SITE_URL, o la que expone Render) deja og:image y og:url absolutos,
# que es lo que necesitan WhatsApp, Slack o LinkedIn para mostrar la imagen al compartir el link.
set -euo pipefail
rm -rf dist && mkdir -p dist
cp -r index.html favicon.svg assets dist/
URL="${SITE_URL:-${RENDER_EXTERNAL_URL:-}}"
URL="${URL%/}"
if [ -n "$URL" ]; then
  sed -i "s#content=\"assets/img/og-la-mesa.jpg\"#content=\"${URL}/assets/img/og-la-mesa.jpg\"#" dist/index.html
  sed -i "s#<meta property=\"og:type\" content=\"website\">#<meta property=\"og:type\" content=\"website\">\n<meta property=\"og:url\" content=\"${URL}/\">#" dist/index.html
  echo "og:image y og:url apuntan a ${URL}"
else
  echo "sin SITE_URL: og:image queda con ruta relativa"
fi
echo "dist/ listo: $(find dist -type f | wc -l) archivos"
