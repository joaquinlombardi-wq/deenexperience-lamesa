# Render de las fotografías

Las ocho imágenes de `assets/img/fotos/` son renders físicos (Blender Cycles) de escenas modeladas por código. Cada escena es un script `s_<nombre>.py`; `lib.py` tiene materiales, luces y cámara, y `props.py` los objetos de la mesa (platos, copas, cubiertos, velas, la pantalla).

## Preparar

```bash
python3 -m venv venv && ./venv/bin/pip install bpy==5.2.2 numpy pillow
./fetch-fonts.sh                     # tipografías para imprimir sobre los objetos
cd tex && npm i playwright && for f in napkin_ink napkin_emb; do node tex.cjs $PWD/$f.html $PWD/$f.png 4096 4096 0; done
node tex.cjs $PWD/invite_foil.html $PWD/invite_foil.png 2540 3560 0
node tex.cjs $PWD/menu.html $PWD/menu.png 2100 4200 1
node tex.cjs $PWD/placecard.html $PWD/placecard.png 1800 1000 1
node tex.cjs $PWD/tablet.html $PWD/tablet.png 2048 1536 0
node tex.cjs $PWD/tickets.html $PWD/tickets.png 4800 2200 1
../venv/bin/python gen_textures.py   # pliegues, máscaras, lacre, logo
node tex.cjs $PWD/invite_deboss.html $PWD/invite_deboss.png 2540 3560 0
cd ..
```

## Renderizar

```bash
BLENDER_PY=./venv/bin/python ./render-all.sh            # todas (≈1 h en 4 núcleos)
BLENDER_PY=./venv/bin/python ./render-all.sh servilleta # una sola
./venv/bin/python s_mesa.py --preview                   # prueba rápida a 1/3 de tamaño en out/
```

`post.py` aplica el acabado común (virado violeta en sombras, viñeta, brillo leve, grano) y exporta WebP. Los textos impresos (menú, invitación, servilleta, comandas, la pantalla de Deenex) están en las plantillas HTML de `tex/`.
