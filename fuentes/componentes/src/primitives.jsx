import { cx, rich } from './util.jsx';
import { asset, photos } from './assets.js';
const React = window.React;

export function Kicker({ children, tone = 'accent', rule = true, as: Tag = 'span', className }) {
  return <Tag className={cx('lm-kicker', 'kicker', `lm-kicker--${tone}`, rule && 'lm-kicker--rule', className)}>{children}</Tag>;
}

export function Hashtag({ className }) {
  return <span className={cx('lm-hashtag', className)}>#Deene<b>X</b>perience</span>;
}

export function Logo({ height = 22, tone = 'auto', className }) {
  const s = { height };
  if (tone === 'ink') return <img className={cx('lm-logo', className)} src={asset('logoInk')} alt="Deenex" style={s} />;
  if (tone === 'paper') return <img className={cx('lm-logo', className)} src={asset('logoPaper')} alt="Deenex" style={s} />;
  return (
    <span className={cx('lm-logo', 'lm-logo--auto', className)} style={s}>
      <img className="lm-logo__paper" src={asset('logoPaper')} alt="Deenex" style={s} />
      <img className="lm-logo__ink" src={asset('logoInk')} alt="" aria-hidden="true" style={s} />
    </span>
  );
}

export function Button({ variant = 'primary', arrow, href, children, className, ...rest }) {
  const body = <>
    {arrow === 'left' && <span className="lm-btn__arrow" aria-hidden="true">←</span>}
    <span>{children}</span>
    {arrow === 'right' && <span className="lm-btn__arrow" aria-hidden="true">→</span>}
  </>;
  const cls = cx('lm-btn', `lm-btn--${variant}`, className);
  return href ? <a className={cls} href={href} {...rest}>{body}</a> : <button type="button" className={cls} {...rest}>{body}</button>;
}

export function StatusPill({ tone = 'accent', live = false, boxed = false, children, className }) {
  return (
    <span className={cx('lm-pill', `lm-pill--${tone}`, live && 'lm-pill--live', boxed && 'lm-pill--boxed', className)}>
      <i className="lm-pill__dot" aria-hidden="true" />
      <span>{children}</span>
    </span>
  );
}

export function Viewfinder({ rec = true, timecode, label }) {
  return (
    <div className="lm-vf" aria-hidden="true">
      <span className="lm-vf__c lm-vf__c--tl" /><span className="lm-vf__c lm-vf__c--tr" />
      <span className="lm-vf__c lm-vf__c--bl" /><span className="lm-vf__c lm-vf__c--br" />
      <div className="lm-vf__top">
        {rec ? <span className="lm-vf__rec"><i />REC</span> : <span className="lm-vf__off"><i />Sin audio · desde afuera</span>}
        {timecode && <span className="lm-vf__tc">{timecode}</span>}
      </div>
      {label && <div className="lm-vf__bottom">{label}</div>}
    </div>
  );
}

export function Photo({ src, name, alt, ratio = '16 / 9', caption, position = '50% 50%', viewfinder, bleed = false, framed = false, overlay, loading = 'eager', className, children }) {
  const meta = name ? photos[name] : null;
  const img = asset(src || name);
  const cap = caption === false ? null : (caption || meta);
  return (
    <figure className={cx('lm-photo', bleed && 'lm-photo--bleed', framed && 'lm-photo--framed', className)}>
      <div className="lm-photo__frame" style={{ aspectRatio: ratio }}>
        <img src={img} alt={alt || (meta && meta.alt) || ''} style={{ objectPosition: position }} loading={loading} decoding="async" />
        {viewfinder && <Viewfinder {...viewfinder} />}
        {overlay}
        {children}
      </div>
      {cap && (
        <figcaption className="lm-photo__cap meta">
          {cap.n && <span className="lm-photo__n">{cap.n}</span>}
          <span className="lm-photo__t">{cap.title}</span>
          {cap.detail && <span className="lm-photo__d">{cap.detail}</span>}
        </figcaption>
      )}
    </figure>
  );
}

export function SectionHeader({ kicker, title, lede, layout = 'stack', size = 2, as: Tag = 'h2', id, className }) {
  return (
    <header className={cx('lm-sh', `lm-sh--${layout}`, className)}>
      <div className="lm-sh__main">
        {kicker && <Kicker>{kicker}</Kicker>}
        <Tag id={id} className={cx('lm-sh__title', 'lm-rich', size === 1 ? 'display-1' : 'display-2')}>{rich(title)}</Tag>
      </div>
      {lede && <p className="lm-sh__lede lede">{rich(lede)}</p>}
    </header>
  );
}

export function Statement({ children, cite, className }) {
  return (
    <blockquote className={cx('lm-statement', className)}>
      <p className="lm-statement__text quote-1 lm-rich">{rich(children)}</p>
      {cite && <cite className="lm-statement__cite meta">{cite}</cite>}
    </blockquote>
  );
}

export function Callout({ children, className }) {
  return <p className={cx('lm-callout', 'quote-2', 'lm-rich', className)}>{rich(children)}</p>;
}
