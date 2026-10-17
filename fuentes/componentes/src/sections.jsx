import { cx, rich } from './util.jsx';
import { Kicker, Logo, Hashtag, Photo, Callout, StatusPill } from './primitives.jsx';
import { content } from './content.js';
const React = window.React;

export function RuleGrid({ items = content.rules.items, keyIndex = -1, className }) {
  return (
    <ol className={cx('lm-rules', className)}>
      {items.map((r, i) => {
        const [label, num] = r.n.split(' ');
        return (
          <li key={i} className={cx('lm-rules__item', i === keyIndex && 'is-key')}>
            <div className="lm-rules__n"><span className="kicker">{label}</span><span className="numeral">{num}</span></div>
            <h3 className="title-3">{r.title}</h3>
            <p className="body-s">{rich(r.body)}</p>
            {r.why && <p className="lm-rules__why">{rich(r.why)}</p>}
          </li>
        );
      })}
    </ol>
  );
}

export function ProcessSteps({ items = content.steps.items, note = content.steps.note, className }) {
  return (
    <div className={cx('lm-steps', className)}>
      <ol className="lm-steps__list">
        {items.map((s, i) => (
          <li key={i} className="lm-steps__item">
            <span className="lm-steps__v display-1">{s.value}</span>
            {i < items.length - 1 && <span className="lm-steps__arrow" aria-hidden="true">→</span>}
            <h3 className="title-3">{s.title}</h3>
            <p className="body-s">{rich(s.body)}</p>
          </li>
        ))}
      </ol>
      {note && <Callout className="lm-steps__note">{note}</Callout>}
    </div>
  );
}

export function NumberedList({ items = content.closing.items, className }) {
  return (
    <ol className={cx('lm-nlist', className)}>
      {items.map((s, i) => (
        <li key={i} className="lm-nlist__item">
          <span className="lm-nlist__n numeral">{s.n}</span>
          <div><h3 className="title-3">{s.title}</h3><p className="body-s">{rich(s.body)}</p></div>
        </li>
      ))}
    </ol>
  );
}

export function FeatureSplit({ image, ratio = '3 / 2', caption, viewfinder, position, reverse = false, children, className }) {
  return (
    <div className={cx('lm-split', reverse && 'lm-split--reverse', className)}>
      <div className="lm-split__media"><Photo name={image} ratio={ratio} caption={caption} viewfinder={viewfinder} position={position} framed /></div>
      <div className="lm-split__body">{children}</div>
    </div>
  );
}

export function CastGrid({ items = content.room.cast, className }) {
  return (
    <ul className={cx('lm-cast', className)}>
      {items.map((c, i) => (
        <li key={i} className={cx('lm-cast__item', /Experto/.test(c.role) && 'is-expert')}>
          <Kicker rule={false}>{c.role}</Kicker>
          <h3 className="lm-cast__name display-3">{c.name}</h3>
          <p className="body-s">{rich(c.body)}</p>
        </li>
      ))}
    </ul>
  );
}

export function PartnerList({ rows = content.partners.rows, images = true, className }) {
  return (
    <ul className={cx('lm-partners', className)}>
      {rows.map((p, i) => (
        <li key={i} className={cx('lm-partners__row', p.host && 'is-host', p.after && 'is-after')}>
          <div className="lm-partners__who">
            <h3 className="lm-partners__name display-3">{p.name}</h3>
            <Kicker rule={false} tone={p.host || p.after ? 'accent' : 'muted'}>{p.role}</Kicker>
            {p.host && <StatusPill tone="accent" boxed>Anfitrión</StatusPill>}
          </div>
          <p className="lm-partners__text body">
            <strong>{p.lead}</strong> {rich(p.body)}{p.strong && <> <strong>{p.strong}</strong></>}
          </p>
          {images && p.image ? <div className="lm-partners__img"><Photo name={p.image} ratio="4 / 3" caption={false} /></div> : <div className="lm-partners__img lm-partners__img--empty" aria-hidden="true" />}
        </li>
      ))}
    </ul>
  );
}

export function CategoryTiers({ groups = content.tiers.groups, note = content.tiers.note, className }) {
  return (
    <div className={cx('lm-tiers', className)}>
      <div className="lm-tiers__cols">
        {groups.map((g, i) => (
          <section key={i} className="lm-tiers__col">
            <header className="lm-tiers__head">
              <Kicker>{g.title}</Kicker>
              <p className="body-s">{g.note}</p>
            </header>
            <ul>
              {g.items.map((it, j) => (
                <li key={j} className="lm-tiers__item">
                  <h3 className="title-3">{it.name}</h3>
                  <span className="lm-tiers__brands meta">{it.brands}</span>
                  <p className="body-s">{rich(it.body)}</p>
                </li>
              ))}
            </ul>
          </section>
        ))}
      </div>
      {note && <Callout className="lm-tiers__note">{note}</Callout>}
    </div>
  );
}

export function Timeline({ rows = content.calendar.rows, className }) {
  return (
    <ol className={cx('lm-timeline', className)}>
      {rows.map((r, i) => (
        <li key={i} className={cx('lm-timeline__row', r.mark && 'is-mark', r.final && 'is-final')}>
          <span className="lm-timeline__dot" aria-hidden="true" />
          <span className="lm-timeline__date meta">{r.date}</span>
          <p className={cx('lm-timeline__text', r.final ? 'display-3' : 'body')}>{rich(r.text)}</p>
        </li>
      ))}
    </ol>
  );
}

export function CameraPolicy({ filmed = content.cameras.filmed, never = content.cameras.never, note = content.cameras.note, className }) {
  return (
    <div className={cx('lm-cams', className)}>
      <section className="lm-cams__col">
        <h3 className="lm-cams__h"><StatusPill tone="rec" live>Lo que se filma</StatusPill></h3>
        <ul>{filmed.map((t, i) => <li key={i} className="body-s">{rich(t)}</li>)}</ul>
      </section>
      <section className="lm-cams__col lm-cams__col--never">
        <h3 className="lm-cams__h"><StatusPill tone="off">Lo que no sale nunca</StatusPill></h3>
        <ul>{never.map((t, i) => <li key={i} className="body-s">{rich(t)}</li>)}</ul>
        {note && <Callout>{note}</Callout>}
      </section>
    </div>
  );
}

export function Footer({ line = content.footer.line, disclaimer = content.footer.disclaimer, className }) {
  return (
    <footer className={cx('lm-footer', className)}>
      <Logo height={18} />
      <p className="lm-footer__tag"><Hashtag /></p>
      <p className="lm-footer__line meta">{line}</p>
      {disclaimer && <p className="lm-footer__disc body-s">{disclaimer}</p>}
    </footer>
  );
}
