#!/bin/bash
# Fonts used to print type onto the rendered objects (all SIL OFL / Apache, from github.com/google/fonts).
cd "$(dirname "$0")" && mkdir -p fonts && cd fonts
B=https://raw.githubusercontent.com/google/fonts/main
for p in "ofl/archivo/Archivo%5Bwdth%2Cwght%5D.ttf" "ofl/instrumentserif/InstrumentSerif-Regular.ttf" "ofl/instrumentserif/InstrumentSerif-Italic.ttf" \
  "ofl/dmmono/DMMono-Regular.ttf" "ofl/dmmono/DMMono-Medium.ttf" "ofl/dmmono/DMMono-Light.ttf" "ofl/caveat/Caveat%5Bwght%5D.ttf" \
  "ofl/nanumpenscript/NanumPenScript-Regular.ttf" "ofl/kalam/Kalam-Regular.ttf" "apache/homemadeapple/HomemadeApple-Regular.ttf" "ofl/reeniebeanie/ReenieBeanie.ttf" \
  "ofl/mrssaintdelafield/MrsSaintDelafield-Regular.ttf" "ofl/herrvonmuellerhoff/HerrVonMuellerhoff-Regular.ttf" "ofl/monsieurladoulaise/MonsieurLaDoulaise-Regular.ttf" \
  "ofl/alexbrush/AlexBrush-Regular.ttf" "ofl/pinyonscript/PinyonScript-Regular.ttf" "ofl/mrdehaviland/MrDeHaviland-Regular.ttf" "ofl/qwigley/Qwigley-Regular.ttf" \
  "ofl/kristi/Kristi-Regular.ttf" "ofl/zeyada/Zeyada.ttf" "ofl/dawningofanewday/DawningofaNewDay.ttf" "ofl/cedarvillecursive/Cedarville-Cursive.ttf" \
  "ofl/labelleaurore/LaBelleAurore.ttf" "ofl/sacramento/Sacramento-Regular.ttf"; do
  f=$(basename "$p" | python3 -c "import sys,urllib.parse;print(urllib.parse.unquote(sys.stdin.read().strip()))")
  curl -sSL --fail -o "$f" "$B/$p" && echo "ok $f"
done
