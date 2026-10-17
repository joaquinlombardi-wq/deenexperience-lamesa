# Local replica of the page-generated tokens.css, for testing previews only (never published).
import json, sys
src, out, fontbase = sys.argv[1], sys.argv[2], sys.argv[3]
t = json.load(open(src))
themes = [th['id'] for th in t['color']['themes']]
def val(v, th):
    if isinstance(v, str): v2 = v
    else: v2 = v.get(th, v.get(themes[0]))
    if v2.startswith('{') and v2.endswith('}'): return 'var(--%s)' % v2[1:-1]
    return v2
L = []
first = themes[0]
L.append(':root, [data-theme="%s"] {' % first)
for c in t['color']['tokens']: L.append('  --%s: %s;' % (c['name'], val(c['value'], first)))
for s in t.get('shadow', {}).get('tokens', []): L.append('  --%s: %s;' % (s['name'], val(s['value'], first)))
L.append('}')
for th in themes[1:]:
    L.append('[data-theme="%s"] {' % th)
    for c in t['color']['tokens']: L.append('  --%s: %s;' % (c['name'], val(c['value'], th)))
    for s in t.get('shadow', {}).get('tokens', []): L.append('  --%s: %s;' % (s['name'], val(s['value'], th)))
    L.append('}')
L.append(':root {')
for fam in ('spacing', 'radius', 'layout'):
    for s in t.get(fam, {}).get('tokens', []): L.append('  --%s: %s;' % (s['name'], s['value']))
for k, v in t['type']['families'].items(): L.append('  --font-%s: %s;' % (k, v))
L.append('}')
for g in t['type']['groups']:
    for st in g['styles']:
        fam = st.get('family', g['family'])
        lh = st['lineHeight']; lh = lh if isinstance(lh, str) else str(lh)
        props = ['font-family: var(--font-%s)' % fam, 'font-size: %s' % st['fontSize'], 'line-height: %s' % lh, 'font-weight: %s' % st['fontWeight']]
        if 'letterSpacing' in st: props.append('letter-spacing: %s' % st['letterSpacing'])
        if 'fontStyle' in st: props.append('font-style: %s' % st['fontStyle'])
        L.append('.%s { %s; }' % (st['name'], '; '.join(props)))
for f in t['type']['fonts']:
    L.append('@font-face { font-family: "%s"; src: url("%s/%s") format("woff2"); font-weight: %s; font-style: %s; font-display: swap; }' % (f['family'], fontbase, f['file'], f['weight'], f.get('style', 'normal')))
open(out, 'w').write('/* La Mesa by Deenex — generated from tokens.json */\n' + '\n'.join(L) + '\n'); print('tokens.css lines', len(L))
