// Empaqueta fuentes/componentes/src en assets/js/la-mesa.js (script clásico que define window.LaMesa).
const esbuild = require('esbuild'); const fs = require('fs'); const path = require('path');
const ORDER = ['Kicker','Hashtag','Logo','Button','StatusPill','Photo','Viewfinder','SectionHeader','Statement','Callout','TopBar','Hero','StatRow',
  'RuleGrid','ProcessSteps','NumberedList','FeatureSplit','CastGrid','NightStory','SeatingPlan','PartnerList','CategoryTiers','Timeline','CameraPolicy','Footer'];
(async () => {
  const r = await esbuild.build({ entryPoints: [path.join(__dirname, 'componentes/src/index.jsx')], bundle: true, format: 'iife', write: false,
    jsx: 'transform', jsxFactory: 'React.createElement', jsxFragment: 'React.Fragment', target: 'es2018', charset: 'utf8', legalComments: 'none' });
  const header = '/* @ds-bundle: ' + JSON.stringify({ format: 4, namespace: 'LaMesa', components: ORDER.map(name => ({ name })) }) + ' */\n' +
    '/* La Mesa by Deenex — componentes del sistema de diseño (fuente: fuentes/componentes/src). */\n';
  const js = header + r.outputFiles[0].text;
  if (/<\/script|<!--/i.test(js)) throw new Error('el bundle contiene </script o <!--');
  fs.writeFileSync(path.join(__dirname, '../assets/js/la-mesa.js'), js);
  console.log('assets/js/la-mesa.js', js.length, 'bytes');
})().catch(e => { console.error(e.message); process.exit(1); });
