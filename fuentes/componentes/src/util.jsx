const React = window.React;

export const cx = (...a) => a.filter(Boolean).join(' ');

// *acento* → <em>, **fuerte** → <strong>
export function rich(str) {
  if (typeof str !== 'string') return str;
  const out = []; const re = /\*\*(.+?)\*\*|\*(.+?)\*/g; let m; let last = 0; let k = 0;
  while ((m = re.exec(str))) {
    if (m.index > last) out.push(str.slice(last, m.index));
    out.push(m[1] != null ? <strong key={k++}>{m[1]}</strong> : <em key={k++}>{m[2]}</em>);
    last = re.lastIndex;
  }
  if (last < str.length) out.push(str.slice(last));
  return out;
}

export function useReducedMotion() {
  const [r, setR] = React.useState(false);
  React.useEffect(() => {
    if (!window.matchMedia) return;
    const q = window.matchMedia('(prefers-reduced-motion: reduce)');
    const f = () => setR(q.matches); f();
    q.addEventListener ? q.addEventListener('change', f) : q.addListener(f);
    return () => (q.removeEventListener ? q.removeEventListener('change', f) : q.removeListener(f));
  }, []);
  return r;
}
