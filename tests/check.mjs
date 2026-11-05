import { chromium } from '/opt/npm-tools/node_modules/playwright/index.mjs';
const BASE = process.argv[2] || 'http://localhost:8765/';
const OUT = process.argv[3] || '/tmp/shots';
const sizes = [[1440,900],[1366,768],[1280,720],[768,1024],[390,844]];
const pages = ['index.html','menu.html','senza-glutine.html','contatti.html','404.html'];
const b = await chromium.launch();
const problems = [];
for (const lang of ['it','en']) for (const [w,h] of sizes) for (const pg of pages) {
  const ctx = await b.newContext({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
  const p = await ctx.newPage();
  const bad = [];
  p.on('requestfailed', r => bad.push('failed ' + r.url()));
  p.on('response', r => { if (r.status() >= 400) bad.push(r.status() + ' ' + r.url()); });
  p.on('pageerror', e => bad.push('js ' + e.message));
  await p.goto(BASE + pg + '?lang=' + lang, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(400);
  const r = await p.evaluate(() => {
    const out = [];
    const hh = document.querySelector('.dg-header').getBoundingClientRect().height;
    const avail = innerHeight - hh;
    if (document.documentElement.scrollWidth > innerWidth + 1) out.push('sideways scroll ' + document.documentElement.scrollWidth);
    document.querySelectorAll('main > section, main > .msec').forEach((s, i) => {
      const r = s.getBoundingClientRect();
      if (r.height > avail + 1) out.push(`section ${i} (${s.className}) ${Math.round(r.height)} > ${Math.round(avail)}`);
      // clipped content: any descendant whose bottom is outside the section
      const kids = [...s.querySelectorAll('h1,h2,p,a.dg-btn,li,img,figure,.dg-frame,svg.mappa__svg')];
      for (const k of kids) { const kr = k.getBoundingClientRect(); if (kr.height && getComputedStyle(k).display!=='none' && k.offsetParent!==null && (kr.bottom > r.bottom + 2 || kr.top < r.top - 2) && !k.closest('.cards') ) { out.push(`clipped in section ${i}: ${k.tagName}.${k.className} ${Math.round(kr.bottom)} > ${Math.round(r.bottom)}`); break; } }
      // empty bands: vertical gaps > 120px inside the section with no content
      const ys = kids.filter(k=>k.offsetParent!==null).map(k=>k.getBoundingClientRect()).filter(x=>x.height>0).map(x=>[x.top,x.bottom]).sort((a,b)=>a[0]-b[0]);
      let cur = r.top; let gap = 0;
      for (const [t,bt] of ys) { if (t - cur > gap) gap = t - cur; cur = Math.max(cur, bt); }
      if (r.bottom - cur > gap) gap = r.bottom - cur;
      if (gap > 150 && !s.classList.contains('hero')) out.push(`empty band ${Math.round(gap)}px in section ${i} (${s.className})`);
    });
    // hero buttons visible in first screen
    const hb = document.querySelectorAll('.hero__btns .dg-btn');
    hb.forEach(x => { const r = x.getBoundingClientRect(); if (r.bottom > innerHeight || r.top < hh) out.push('hero button not fully visible'); });
    // raw keys and blue text
    const txt = document.body.innerText;
    if (/\b(nav|btn|hero|meta|sg|sgp|c|menu|foot|piazza|cucina)\.[a-z0-9.]+\b/.test(txt.replace(/info@dagherardo\.com|dagherardo\.com/g,''))) out.push('raw key in text: ' + txt.match(/\b(nav|btn|hero|meta|sg|sgp|c|menu|foot|piazza|cucina)\.[a-z0-9.]+\b/)[0]);
    document.querySelectorAll('a, button').forEach(a => { const c = getComputedStyle(a).color; const m = c.match(/\d+/g).map(Number); if (m[2] > 150 && m[0] < 90 && m[1] < 160) out.push('blue: ' + a.textContent.trim().slice(0,30)); });
    document.querySelectorAll('img').forEach(i => { if (i.complete && i.naturalWidth === 0 && getComputedStyle(i).display !== 'none' && i.closest('[hidden]') === null) out.push('broken img ' + i.getAttribute('src')); });
    if (document.body.innerHTML.includes('—')) out.push('em dash');
    return out;
  });
  // anchors land under header? check menu#senza-glutine and internal links handled by scroll-margin
  if (pg === 'index.html' && lang === 'it') await p.screenshot({ path: `${OUT}/home-${w}x${h}.png`, fullPage: true });
  if (lang === 'it' && pg !== 'index.html' && pg !== '404.html') await p.screenshot({ path: `${OUT}/${pg.replace('.html','')}-${w}x${h}.png`, fullPage: true });
  if (lang === 'en' && w === 1280) await p.screenshot({ path: `${OUT}/en-${pg.replace('.html','')}-${w}x${h}.png`, fullPage: true });
  [...r, ...bad].forEach(x => problems.push(`${lang} ${w}x${h} ${pg}: ${x}`));
  await ctx.close();
}
// menu: every dish reachable through tabs and pages
{
  const ctx = await b.newContext({ viewport: { width: 1280, height: 720 } }); const p = await ctx.newPage();
  await p.goto(BASE + 'menu.html', { waitUntil: 'networkidle' }); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  const res = await p.evaluate(async () => {
    let seen = 0; const total = window.DG_MENU.reduce((n,c)=>n+c.groups.reduce((m,g)=>m+g.items.length,0),0);
    for (const c of window.DG_MENU) {
      document.getElementById('tab-'+c.id).click(); await new Promise(r=>setTimeout(r,50));
      while (true) { seen += document.querySelectorAll('.dg-dishes .dg-dish').length; const n = document.querySelector('.dg-pager__btn--next'); if (!n || n.disabled) break; n.click(); await new Promise(r=>setTimeout(r,30)); }
    }
    return { seen, total };
  });
  if (res.seen !== res.total) problems.push(`menu shows ${res.seen} of ${res.total} items`); else console.log(`menu: all ${res.total} items reachable at 1280x720`);
  await ctx.close();
}
for (const [w,h] of [[390,844],[1440,900]]) {
  const ctx = await b.newContext({ viewport: { width: w, height: h } }); const p = await ctx.newPage();
  await p.goto(BASE + 'menu.html#senza-glutine', { waitUntil: 'networkidle' }); await p.waitForTimeout(500);
  await p.screenshot({ path: `${OUT}/menu-sg-${w}.png` });
  const ok = await p.evaluate(() => document.querySelector('#tab-senza-glutine').getAttribute('aria-selected'));
  if (ok !== 'true') problems.push('menu#senza-glutine did not open the tab');
  await ctx.close();
}
await b.close();
console.log(problems.length ? problems.join('\n') : 'ALL CHECKS PASSED');
