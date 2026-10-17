// usage: node tex.cjs page.html out.png W H [transparent=1] [scale=1]
const { chromium } = require('playwright');
(async () => {
  const [,, src, out, w, h, tr='1', sc='1'] = process.argv;
  const b = await chromium.launch({ args: ['--allow-file-access-from-files'] });
  const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: +sc });
  await p.goto('file://' + src, { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  const bad = await p.evaluate(() => [...document.fonts].filter(f => f.status !== 'loaded').map(f => f.family + ':' + f.status));
  if (bad.length) console.log('font status', bad.join(', '));
  await p.screenshot({ path: out, omitBackground: tr === '1', clip:{x:0,y:0,width:+w,height:+h} });
  console.log('ok', out);
  await b.close();
})();
