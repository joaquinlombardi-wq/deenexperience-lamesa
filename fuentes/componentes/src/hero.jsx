import { cx, rich } from './util.jsx';
import { Logo, Hashtag, Photo } from './primitives.jsx';
import { content } from './content.js';
const React = window.React;

export function TopBar({ edition = content.edition, className }) {
  return (
    <div className={cx('lm-topbar', className)}>
      <Logo height={20} />
      <span className="lm-topbar__hair" aria-hidden="true" />
      <Hashtag />
      <span className="lm-topbar__ed meta">{edition}</span>
    </div>
  );
}

export function StatRow({ items = content.hero.stats, className }) {
  return (
    <dl className={cx('lm-stats', className)}>
      {items.map((it, i) => (
        <div className="lm-stats__cell" key={i}>
          <dt className="lm-stats__v numeral">{it.value}</dt>
          <dd className="lm-stats__l meta">{it.label}</dd>
        </div>
      ))}
    </dl>
  );
}

export function Hero({ image = 'mesa', sub = content.hero.sub, stats = content.hero.stats, meta = content.hero.meta, edition = content.edition,
  position = '58% 50%', timecode = '20:30', className }) {
  return (
    <section className={cx('lm-hero', className)}>
      <div className="lm-hero__copy">
        <TopBar edition={edition} />
        <div className="lm-hero__body">
          <h1 className="lm-hero__title" aria-label="La Mesa">
            <span className="lm-hero__la serif-hero">La</span>
            <span className="lm-hero__mesa display-hero">Mesa</span>
          </h1>
          <p className="lm-hero__sub lede">{rich(sub)}</p>
          <StatRow items={stats} />
          <ul className="lm-hero__meta meta">{meta.map((m, i) => <li key={i}>{m}</li>)}</ul>
        </div>
      </div>
      <div className="lm-hero__media">
        <Photo name={image} ratio="auto" caption={false} position={position} viewfinder={{ rec: true, timecode, label: 'Mesa 02 · Lugar 04' }} />
      </div>
    </section>
  );
}
