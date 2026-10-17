#!/bin/bash
# Renders every scene in order, then finishes each image into ../../assets/img/fotos/<name>.webp
# Usage: ./render-all.sh [scene ...]   (default: all)   ·   add --preview to a single scene for a quick 1/3-size check.
cd "$(dirname "$0")"
PY=${BLENDER_PY:-python3}
SCENES=${@:-servilleta invitacion copas confesionario mesa pantalla sala cocina}
for s in $SCENES; do
  echo "== $s"; $PY s_$s.py || exit 1
  $PY post.py out/$s.png ../../assets/img/fotos/$s.webp 2000
done
