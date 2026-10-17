import { cx, rich, useReducedMotion } from './util.jsx';
import { Button, StatusPill, Viewfinder, Photo, Kicker } from './primitives.jsx';
import { content, EXPERTS, THEMES } from './content.js';
import { asset, plan, photos } from './assets.js';
const React = window.React;
const { useState, useEffect, useRef } = React;

const COURSES = [
  { v: -1, label: 'Llegada' },
  { v: 0, label: 'Primer plato' },
  { v: 1, label: 'Segundo plato' },
  { v: 2, label: 'Tercer plato' }
];

export function tableState(k, course, tableId) {
  return course < 0
    ? { theme: 'Mesa ' + tableId, who: '5 CEOs + 1 experto' }
    : { theme: THEMES[k], who: EXPERTS[(k + course) % 3] };
}

export function PlanOverlay({ course = 0, tables = plan.tables }) {
  return (
    <div className="lm-plan__ov">
      {tables.map((t, k) => {
        const st = tableState(k, course, t.id);
        return (
          <React.Fragment key={t.id}>
            <span className="lm-plan__ring" style={{ left: t.x + '%', top: t.y + '%', width: (t.r || 9) * 2 + '%' }} />
            {t.seat && <span className="lm-plan__seat" style={{ left: t.seat.x + '%', top: t.seat.y + '%' }} title="Experto" />}
            <div className={cx('lm-plan__label', t.label === 'above' && 'is-above')} style={{ left: t.x + '%', top: (t.label === 'above' ? t.y - (t.r || 9) * 1.78 - 2 : t.y + (t.r || 9) * 1.78 + 2) + '%' }}>
              <span className="kicker">Mesa {t.id}</span>
              <b>{st.theme}</b>
              <span className="lm-plan__who">{st.who}</span>
            </div>
          </React.Fragment>
        );
      })}
    </div>
  );
}

export function SeatingPlan({ image = 'sala', course: initial = 0, interactive = true, caption, tables = plan.tables, className }) {
  const [course, setCourse] = useState(initial);
  useEffect(() => setCourse(initial), [initial]);
  return (
    <div className={cx('lm-plan', className)}>
      <Photo name={image} ratio="16 / 9" caption={caption} overlay={<PlanOverlay course={course} tables={tables} />} framed />
      {interactive && (
        <div className="lm-plan__tabs" role="tablist" aria-label="Momento de la cena">
          {COURSES.map(c => (
            <button key={c.v} type="button" role="tab" aria-selected={c.v === course} className={cx('lm-plan__tab', c.v === course && 'is-on')} onClick={() => setCourse(c.v)}>{c.label}</button>
          ))}
          <span className="lm-plan__legend meta"><i className="lm-plan__dot" aria-hidden="true" />Silla del experto · rota con cada plato</span>
        </div>
      )}
      <ul className="lm-plan__list">
        {tables.map((t, k) => { const st = tableState(k, course, t.id); return <li key={t.id}><span className="kicker">Mesa {t.id}</span> <b>{st.theme}</b> · {st.who}</li>; })}
      </ul>
    </div>
  );
}

export function NightStory({ scenes = content.story.scenes, start = 0, className }) {
  const [cur, setCur] = useState(start);
  const reduced = useReducedMotion();
  const root = useRef(null);
  const sc = scenes[cur];
  const go = i => setCur(Math.max(0, Math.min(scenes.length - 1, i)));
  const images = Array.from(new Set(scenes.map(s => s.image)));
  const onKey = e => {
    if (e.key === 'ArrowRight') { e.preventDefault(); go(cur + 1); }
    if (e.key === 'ArrowLeft') { e.preventDefault(); go(cur - 1); }
  };
  return (
    <div className={cx('lm-story', reduced && 'is-reduced', className)} ref={root} onKeyDown={onKey}>
      <div className="lm-story__scrub" role="tablist" aria-label="Momentos de la noche">
        <span className="lm-story__track" aria-hidden="true"><span style={{ width: (cur / (scenes.length - 1)) * 100 + '%' }} /></span>
        {scenes.map((s, i) => (
          <button key={i} type="button" role="tab" aria-selected={i === cur} tabIndex={i === cur ? 0 : -1}
            className={cx('lm-story__stop', i === cur && 'is-on', i < cur && 'is-past')} onClick={() => go(i)}>
            <i aria-hidden="true" />
            <span className="lm-story__h timecode">{s.h}</span>
            <span className="lm-story__k">{s.k}</span>
          </button>
        ))}
      </div>
      <div className="lm-story__grid">
        <div className="lm-story__stage">
          {images.map(key => (
            <img key={key} src={asset(key)} alt={key === sc.image ? (photos[key] ? photos[key].alt : '') : ''} aria-hidden={key === sc.image ? undefined : 'true'}
              className={cx('lm-story__img', key === sc.image && 'is-on')} />
          ))}
          {sc.image === 'sala' && <PlanOverlay course={sc.course} />}
          <Viewfinder rec={sc.cam === 1} timecode={sc.h} label={'Momento ' + String(cur + 1).padStart(2, '0') + ' / ' + String(scenes.length).padStart(2, '0')} />
        </div>
        <div className="lm-story__panel" role="tabpanel" aria-live="polite">
          <span className="lm-story__count meta">Momento {cur + 1} de {scenes.length} · {sc.h}</span>
          <h3 className="lm-story__title display-3">{sc.k}</h3>
          <p className="lm-story__text body">{rich(sc.t)}</p>
          <p className="lm-story__pin quote-2">{sc.pin}</p>
          <div className="lm-story__status">
            <StatusPill tone={sc.cam ? 'rec' : 'off'} live={!!sc.cam}>{sc.cam ? 'Cámaras grabando' : 'Cámaras solo desde afuera'}</StatusPill>
            <StatusPill tone={sc.open ? 'accent' : 'muted'}>{sc.open ? 'Abierta · entran los partners' : 'A puertas cerradas'}</StatusPill>
            <StatusPill tone="accent">{sc.voice}</StatusPill>
          </div>
          <p className="lm-story__note body-s">{sc.note}</p>
          <div className="lm-story__nav">
            <Button variant="ghost" arrow="left" disabled={cur === 0} onClick={() => go(cur - 1)}>Antes</Button>
            <Button variant="ghost" arrow="right" disabled={cur === scenes.length - 1} onClick={() => go(cur + 1)}>Después</Button>
          </div>
        </div>
      </div>
    </div>
  );
}
