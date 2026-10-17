#!/usr/bin/env bash
# Build de Render: publica solo el sitio (no fuentes/) en dist/.
# Si Render expone la URL pública del servicio, la usa para que la imagen al compartir el link sea absoluta.
set -euo pipefail
rm -rf dist && mkdir -p dist
cp -r index.html favicon.svg assets dist/
if [ -n "${RENDER_EXTERNAL_URL:-}" ]; then
  sed -i "s#content=\"assets/img/og-la-mesa.jpg\"#content=\"${RENDER_EXTERNAL_URL}/assets/img/og-la-mesa.jpg\"#" dist/index.html
  sed -i "s#<meta property=\"og:type\" content=\"website\">#<meta property=\"og:type\" content=\"website\">\n<meta property=\"og:url\" content=\"${RENDER_EXTERNAL_URL}/\">#" dist/index.html
fi
echo "dist/ listo: $(find dist -type f | wc -l) archivos"
