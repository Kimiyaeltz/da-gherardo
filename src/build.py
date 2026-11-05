"""Builds Da Gherardo's static pages into ../site from shared header/footer templates.
Run: python3 -I src/build.py  (from the Da-Gherardo project folder)"""
import os, re, json, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, "..", "site")
I = json.loads(subprocess.check_output(["node", "-e", "global.window={};require(process.argv[1]);process.stdout.write(JSON.stringify(window.DG_I18N.it))", os.path.join(SITE, "js/i18n.js")]))

WA = "https://wa.me/393929581765"
TEL = "tel:+390583492116"
CELL = "tel:+393929581765"
MAIL = "mailto:info@dagherardo.com"
MAPS = "https://www.google.com/maps/search/?api=1&query=Trattoria+Pizzeria+Da+Gherardo+Piazza+dell%27Anfiteatro+9+Lucca"
IG = "https://www.instagram.com/ristorantedagherardo/"
FB = "https://www.facebook.com/p/Ristorante-Da-Gherardo-100026806793154"

def T(key, tag="span", cls="", extra=""):
    c = f' class="{cls}"' if cls else ""
    return f'<{tag}{c} data-t="{key}"{extra}>{I[key]}</{tag}>'

def head(page):
    return f"""<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="google" content="notranslate">
<meta name="format-detection" content="telephone=no">
<title>{I['meta.' + page + '.title']}</title>
<meta name="description" content="{I.get('meta.' + page + '.desc', '')}">
<meta property="og:title" content="{I['meta.' + page + '.title']}">
<meta property="og:description" content="{I.get('meta.' + page + '.desc', '')}">
<meta property="og:image" content="images/og-da-gherardo.jpg">
<meta name="theme-color" content="#fcf7ee">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preload" href="fonts/instrument-serif-latin-400-italic.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="css/fonts.css">
<link rel="stylesheet" href="css/styles.css">
</head>
<body data-page="{page}">
"""

def header(active):
    def link(href, key, name):
        cur = ' aria-current="page"' if name == active else ""
        return f'<a href="{href}"{cur} data-t="{key}">{I[key]}</a>'
    return f"""<a class="skip" href="#main" data-t="skip">{I['skip']}</a>
<header class="dg-header">
  <div class="wrap">
    <a class="dg-wordmark" href="index.html" aria-label="Da Gherardo, home">
      <span class="dg-wordmark__name">Da Gherardo</span>
      <span class="dg-wordmark__sub" data-t="wordmark.sub">{I['wordmark.sub']}</span>
    </a>
    <nav class="dg-nav" id="dg-nav" aria-label="Menu principale">
      {link('menu.html', 'nav.menu', 'menu')}
      {link('senza-glutine.html', 'nav.sg', 'sg')}
      {link('contatti.html', 'nav.contatti', 'contatti')}
      <div class="dg-lang" role="group" data-t-attr="aria-label:lang.label" aria-label="{I['lang.label']}">
        <button type="button" data-lang="it" aria-pressed="true">IT</button>
        <button type="button" data-lang="en" aria-pressed="false">EN</button>
      </div>
    </nav>
    <a class="dg-btn dg-btn--head" href="{WA}" target="_blank" rel="noopener" data-t="nav.prenota">{I['nav.prenota']}</a>
    <button class="dg-nav-toggle" type="button" aria-controls="dg-nav" aria-expanded="false" data-t-attr="aria-label:nav.open" aria-label="{I['nav.open']}"><span></span></button>
  </div>
</header>
"""

def footer():
    return f"""<div class="dg-tenda dg-tenda--sm" role="presentation"></div>
<footer class="dg-footer">
  <div class="wrap">
    <div class="dg-footer__grid">
      <div class="dg-footer__brand">
        <a class="dg-wordmark" href="index.html"><span class="dg-wordmark__name">Da Gherardo</span><span class="dg-wordmark__sub" data-t="wordmark.sub">{I['wordmark.sub']}</span></a>
        <div class="dg-badges" role="group" data-t-attr="aria-label:foot.badges" aria-label="{I['foot.badges']}">
          <img src="images/badge-aic-2026.png" alt="AIC, Alimentazione Fuori Casa 2026" width="232" height="180" loading="lazy">
          <img src="images/badge-gluto-2025.png" alt="Gluto, vincitore 2025" width="239" height="241" loading="lazy">
          <img src="images/badge-find-me-gluten-free.png" alt="Find Me Gluten Free" width="236" height="218" loading="lazy">
        </div>
      </div>
      <div>
        <h2 data-t="foot.dove">{I['foot.dove']}</h2>
        <p>Piazza Anfiteatro 9<br>55100 Lucca (LU)</p>
        <p><a href="{MAPS}" target="_blank" rel="noopener" data-t="btn.mappa">{I['btn.mappa']}</a></p>
      </div>
      <div>
        <h2 data-t="foot.contatti">{I['foot.contatti']}</h2>
        <ul>
          <li><a href="{TEL}">0583 49 21 16</a></li>
          <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp 392 95 81 765</a></li>
          <li><a href="{MAIL}">info@dagherardo.com</a></li>
        </ul>
      </div>
      <div>
        <h2 data-t="foot.orari">{I['foot.orari']}</h2>
        <p data-tbc data-t="foot.orari.val">{I['foot.orari.val']}</p>
        <p class="dg-footer__groups" data-t="foot.gruppi">{I['foot.gruppi']}</p>
        <h2 style="margin-top:14px" data-t="foot.seguici">{I['foot.seguici']}</h2>
        <p><a href="{IG}" target="_blank" rel="noopener">Instagram</a> · <a href="{FB}" target="_blank" rel="noopener">Facebook</a></p>
      </div>
    </div>
    <div class="dg-footer__base">
      <span>© 2026 Trattoria Pizzeria Da Gherardo · <span data-t="foot.piva">{I['foot.piva']}</span></span>
      <a href="https://dagherardo.com/privacy-e-cookie-policy/" target="_blank" rel="noopener" data-t="foot.privacy">{I['foot.privacy']}</a>
    </div>
  </div>
</footer>
<a class="dg-btn dg-fab" href="{WA}" target="_blank" rel="noopener" data-t="nav.prenota">{I['nav.prenota']}</a>
"""

def tail(extra_js=""):
    return f"""<script src="js/i18n.js"></script>
{extra_js}<script src="js/main.js"></script>
</body>
</html>
"""

def ellisse(img, alt_key, ring_text=None, cls="", eager=False):
    ring = ""
    if ring_text:
        ring = f'<defs><path id="ep-{img}" d="M 200 8 A 192 142 0 1 1 199.9 8"/></defs><ellipse cx="200" cy="150" rx="180" ry="130" stroke-dasharray="2 5"/><text><textPath href="#ep-{img}" startOffset="2%">{ring_text}</textPath></text>'
    lazy = "" if eager else ' loading="lazy"'
    return f"""<div class="dg-ellisse {cls}">
  <div class="dg-ellisse__photo"><img src="images/{img}.webp" data-t-attr="alt:{alt_key}" alt="{I[alt_key]}"{lazy}></div>
  <svg class="dg-ellisse__ring" viewBox="0 0 400 300" aria-hidden="true"><ellipse cx="200" cy="150" rx="196" ry="146"/>{ring}</svg>
</div>"""

def card(img, cap_key, tilt, stamp=None):
    s = f'<span class="dg-francobollo" aria-hidden="true" data-t="{stamp}">{I[stamp]}</span>' if stamp else ""
    return f'<figure class="dg-cartolina" style="--tilt:{tilt}"><img src="images/{img}.webp" alt="" loading="lazy"><figcaption data-t="{cap_key}">{I[cap_key]}</figcaption>{s}</figure>'

def headline(k1, k2, cls="dg-display--l", tag="h2"):
    return f'<{tag} class="dg-display {cls}"><span data-t="{k1}">{I[k1]}</span> <em data-t="{k2}">{I[k2]}</em></{tag}>'

TIMBRO = """<svg class="dg-timbro" viewBox="0 0 168 168" role="img" aria-label="Senza glutine, laboratorio certificato AIC">
  <defs><path id="tc" d="M84 84 m-64 0 a64 64 0 1 1 128 0 a64 64 0 1 1 -128 0"/></defs>
  <circle cx="84" cy="84" r="80" stroke-width="2"/><circle cx="84" cy="84" r="50" stroke-width="1"/>
  <text font-size="13" letter-spacing="3"><textPath href="#tc">Laboratorio certificato AIC · Lucca ·</textPath></text>
  <text x="84" y="80" text-anchor="middle" font-size="22">Senza</text><text x="84" y="102" text-anchor="middle" font-size="22">glutine</text>
</svg>"""

PIAZZA_DRAW = """<svg viewBox="0 0 160 110" aria-hidden="true"><ellipse class="dg-ink" cx="80" cy="62" rx="70" ry="40"/><ellipse class="dg-ink" cx="80" cy="62" rx="46" ry="22"/><path class="dg-ink" d="M18 48v-10l8-6 8 4v-8l10-4 8 6 10-8 10 4 10-6 10 6 10-4 10 8 8-4 8 8v10M80 40v-10"/></svg>"""

pages = {}

pages["index.html"] = head("home") + header("home") + f"""<main id="main">
<section class="hero dg-on-red" aria-labelledby="hero-title">
  <div class="dg-tenda" role="presentation"></div>
  {T('hero.c1', cls='hero__corner hero__corner--tl')}
  {T('hero.c2', cls='hero__corner hero__corner--tr')}
  {T('hero.c3', cls='hero__corner hero__corner--bl')}
  {T('hero.c4', cls='hero__corner hero__corner--br')}
  <div class="hero__body">
    <h1 id="hero-title" class="hero__word rise">Da</h1>
    <div class="hero__plate rise rise-2">{ellisse('tortelli-lucchesi-al-ragu', 'hero.alt', eager=True)}</div>
    <p class="hero__word rise rise-2" aria-hidden="true"><em>Gherardo</em></p>
    <div class="dg-row hero__btns rise rise-3">
      <a class="dg-btn dg-btn--crema" href="{WA}" target="_blank" rel="noopener" data-t="btn.prenota">{I['btn.prenota']}</a>
      <a class="dg-btn dg-btn--outline-crema" href="menu.html" data-t="btn.menu">{I['btn.menu']}</a>
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="cucina-title">
  <div class="wrap cucina__grid">
    <div class="cucina__text dg-head">
      {T('cucina.eyebrow', 'p', 'dg-eyebrow')}
      <h2 id="cucina-title" class="dg-display dg-display--l"><span data-t="cucina.h1">{I['cucina.h1']}</span> <em data-t="cucina.h2">{I['cucina.h2']}</em></h2>
      {T('cucina.lede', 'p', 'dg-lede')}
      <div class="dg-row"><a class="dg-btn" href="menu.html" data-t="btn.menu">{I['btn.menu']}</a></div>
    </div>
    <div class="cards">
      {card('pizza-nel-forno', 'card.forno', '-3deg', 'stamp.lucca')}
      {card('tagliatelle-porcini', 'card.porcini', '2deg')}
      {card('grigliata-mista-carne', 'card.grigliata', '-1.5deg')}
    </div>
  </div>
</section>

<section class="sec sg-band dg-on-red" aria-labelledby="sg-title">
  <div class="wrap sg-band__grid">
    <div class="sg-band__photo"><img src="images/pizza-giuditta-senza-glutine.webp" data-t-attr="alt:sg.photo.alt" alt="{I['sg.photo.alt']}" loading="lazy"></div>
    <div class="dg-head">
      {T('sg.eyebrow', 'p', 'dg-eyebrow')}
      <h2 id="sg-title" class="dg-display dg-display--l"><span data-t="sg.h1">{I['sg.h1']}</span> <em data-t="sg.h2">{I['sg.h2']}</em></h2>
      {T('sg.lede', 'p', 'dg-lede')}
      <div class="dg-badges" role="img" data-t-attr="aria-label:sg.badges" aria-label="{I['sg.badges']}">
        <img src="images/badge-aic-2026.png" alt="" width="232" height="180" loading="lazy"><img src="images/badge-gluto-2025.png" alt="" width="239" height="241" loading="lazy"><img src="images/badge-find-me-gluten-free.png" alt="" width="236" height="218" loading="lazy">
      </div>
      <div class="dg-row"><a class="dg-btn dg-btn--crema" href="senza-glutine.html" data-t="btn.sg">{I['btn.sg']}</a></div>
    </div>
  </div>
</section>

<section class="sec piazza" aria-labelledby="piazza-title">
  <div class="wrap piazza__grid">
    <div class="dg-head">
      {T('piazza.eyebrow', 'p', 'dg-eyebrow')}
      <h2 id="piazza-title" class="dg-display dg-display--l"><span data-t="piazza.h1">{I['piazza.h1']}</span> <em data-t="piazza.h2">{I['piazza.h2']}</em></h2>
      {T('piazza.lede', 'p', 'dg-lede')}
      <div class="piazza__draw">{PIAZZA_DRAW}{T('piazza.spritz', 'p', 'piazza__spritz')}</div>
      <div class="dg-row" style="margin-top:24px"><a class="dg-btn dg-btn--ghost" href="contatti.html" data-t="btn.arrivare">{I['btn.arrivare']}</a></div>
    </div>
    <div class="piazza__photo"><img src="images/aperitivo-in-piazza.webp" data-t-attr="alt:piazza.alt" alt="{I['piazza.alt']}" loading="lazy"></div>
  </div>
</section>
</main>
""" + footer() + tail()

pages["menu.html"] = head("menu") + header("menu") + f"""<main id="main">
<section class="msec" aria-labelledby="menu-title">
  <div class="wrap mpage">
    <div class="mtitle mtitle__grid">
      <h1 id="menu-title" class="dg-display dg-display--xl"><span data-t="menu.h1">{I['menu.h1']}</span> <em data-t="menu.h2">{I['menu.h2']}</em></h1>
      <div class="mtitle__side">
        {T('menu.lede', 'p', 'dg-lede')}
        <div class="dg-row"><a class="dg-btn" href="{WA}" target="_blank" rel="noopener" data-t="btn.prenota">{I['btn.prenota']}</a><a class="dg-link" href="#senza-glutine" data-t="btn.menu.sg">{I['btn.menu.sg']}</a></div>
      </div>
    </div>
    <div class="dg-frame dg-menu" id="dg-menu">
      <ul class="dg-tabs" role="tablist" data-t-attr="aria-label:menu.tabs" aria-label="{I['menu.tabs']}"></ul>
      <div class="dg-panel" id="dg-panel" role="tabpanel">
        <p class="dg-menu__intro"></p>
        <ul class="dg-dishes"></ul>
        <div class="dg-pager"></div>
      </div>
      <div class="dg-menu__side" id="dg-menu-photo">
        <div class="dg-ellisse"><div class="dg-ellisse__photo"><img src="images/tagliatelle-porcini.webp" alt=""></div><svg class="dg-ellisse__ring" viewBox="0 0 400 300" aria-hidden="true"><ellipse cx="200" cy="150" rx="196" ry="146"/><ellipse cx="200" cy="150" rx="180" ry="130" stroke-dasharray="2 5"/></svg></div>
      </div>
      {T('menu.note', 'p', 'dg-menu__note')}
    </div>
  </div>
</section>
</main>
""" + footer() + tail('<script src="js/menu-data.js"></script>\n')

pages["senza-glutine.html"] = head("sg") + header("sg") + f"""<main id="main">
<section class="sec sgh" aria-labelledby="sg-title">
  <div class="sgh__grid">
    <div class="sgh__text dg-on-red">
      {T('sgp.eyebrow', 'p', 'dg-eyebrow')}
      <h1 id="sg-title" class="dg-display dg-display--xl"><span data-t="sgp.h1">{I['sgp.h1']}</span> <em data-t="sgp.h2">{I['sgp.h2']}</em></h1>
      {T('sgp.lede', 'p', 'dg-lede')}
      <div class="dg-row"><a class="dg-btn dg-btn--crema" href="menu.html#senza-glutine" data-t="btn.menu.sg">{I['btn.menu.sg']}</a><a class="dg-btn dg-btn--outline-crema" href="{WA}" target="_blank" rel="noopener" data-t="btn.prenota">{I['btn.prenota']}</a></div>
      {TIMBRO}
    </div>
    <div class="sgh__photo"><img src="images/pizza-giuditta-senza-glutine.webp" data-t-attr="alt:sgp.alt2" alt="{I['sgp.alt2']}"></div>
  </div>
</section>

<section class="sec" aria-labelledby="lab-title">
  <div class="wrap lab__grid">
    <div class="lab__text dg-head">
      {T('sgp.lab.eyebrow', 'p', 'dg-eyebrow')}
      <h2 id="lab-title" class="dg-display dg-display--l"><span data-t="sgp.lab.h1">{I['sgp.lab.h1']}</span> <em data-t="sgp.lab.h2">{I['sgp.lab.h2']}</em></h2>
      {T('sgp.lab.p1', 'p', 'dg-body dg-lede')}
      {T('sgp.lab.p2', 'p', 'dg-body')}
      <ul class="lab__list"><li data-t="sgp.lab.c1">{I['sgp.lab.c1']}</li><li data-t="sgp.lab.c2">{I['sgp.lab.c2']}</li><li data-t="sgp.lab.c3">{I['sgp.lab.c3']}</li></ul>
      <div class="dg-row" style="margin-top:8px"><a class="dg-btn" href="menu.html#senza-glutine" data-t="btn.menu.sg">{I['btn.menu.sg']}</a></div>
    </div>
    <div class="lab__cards">
      {card('aperitivo-in-piazza', 'sgp.card1', '-2.5deg', 'sgp.stamp')}
      {card('pizza-nel-forno', 'sgp.card2', '2deg')}
    </div>
  </div>
</section>

</main>
""" + footer() + tail()

MAP = f"""<svg class="mappa__svg" viewBox="0 0 560 400" role="img" data-tbc data-t-attr="aria-label:c.map.alt" aria-label="{I['c.map.alt']}">
  <path class="road" stroke-width="26" d="M150 -10 C 160 90 150 160 168 230 S 190 330 176 410"/>
  <path class="road" stroke-width="14" d="M168 200 C 230 196 260 190 300 192"/>
  <path class="road" stroke-width="14" d="M420 120 C 470 90 520 70 570 60"/>
  <path class="road" stroke-width="14" d="M360 300 C 380 340 400 370 410 410"/>
  <ellipse class="oval" cx="380" cy="200" rx="138" ry="96"/>
  <ellipse class="ring" cx="380" cy="200" rx="112" ry="72"/>
  <text class="lbl" x="380" y="196" text-anchor="middle" font-size="16" data-t="c.map.label">{I['c.map.label']}</text>
  <circle class="pin" cx="290" cy="138" r="9"/>
  <text class="us" x="262" y="104" font-size="24" data-t="c.map.us">{I['c.map.us']}</text>
  <text class="lbl" x="122" y="120" font-size="14" transform="rotate(-84 122 120)" text-anchor="middle" data-t="c.map.fillungo">{I['c.map.fillungo']}</text>
</svg>"""

pages["contatti.html"] = head("contatti") + header("contatti") + f"""<main id="main">
<section class="sec ch" aria-labelledby="c-title">
  <div class="wrap ch__grid">
    <div>
      <div class="dg-head">
        {T('c.eyebrow', 'p', 'dg-eyebrow')}
        <h1 id="c-title" class="dg-display dg-display--l"><span data-t="c.h1">{I['c.h1']}</span> <em data-t="c.h2">{I['c.h2']}</em></h1>
        {T('c.lede', 'p', 'dg-lede')}
      </div>
      <div class="dg-row"><a class="dg-btn" href="{WA}" target="_blank" rel="noopener" data-t="btn.whatsapp">{I['btn.whatsapp']}</a><a class="dg-btn dg-btn--ghost" href="{TEL}"><span data-t="btn.chiama">{I['btn.chiama']}</span>&nbsp;0583 49 21 16</a></div>
      <div class="dg-frame">
        <dl>
          <dt data-t="c.dove">{I['c.dove']}</dt><dd><a href="{MAPS}" target="_blank" rel="noopener" data-t="c.dove.val">{I['c.dove.val']}</a></dd>
          <dt data-t="c.cell">{I['c.cell']}</dt><dd><a href="{CELL}">392 95 81 765</a></dd>
          <dt data-t="c.email">{I['c.email']}</dt><dd><a href="{MAIL}">info@dagherardo.com</a></dd>
          <dt data-t="c.posti">{I['c.posti']}</dt><dd data-t="c.posti.val">{I['c.posti.val']}</dd>
          <dt data-t="c.orari">{I['c.orari']}</dt><dd data-tbc data-t="c.orari.val">{I['c.orari.val']}</dd>
        </dl>
      </div>
    </div>
    <div class="ch__side">{ellisse('tagliere-salumi-formaggi', 'piazza.alt', 'Piazza Anfiteatro 9 · Lucca · Trattoria Pizzeria · Aperitivo in piazza ·')}</div>
  </div>
</section>

<section class="sec mappa" aria-labelledby="map-title">
  <div class="wrap mappa__grid">
    <div class="dg-head">
      {T('c.map.eyebrow', 'p', 'dg-eyebrow')}
      <h2 id="map-title" class="dg-display dg-display--l"><span data-t="c.map.h1">{I['c.map.h1']}</span> <em data-t="c.map.h2">{I['c.map.h2']}</em></h2>
      {T('c.map.lede', 'p', 'dg-lede')}
      <div class="dg-row"><a class="dg-btn dg-btn--ghost" href="{MAPS}" target="_blank" rel="noopener" data-t="btn.mappa">{I['btn.mappa']}</a></div>
    </div>
    {MAP}
  </div>
</section>

<section class="sec gruppi dg-on-red" aria-labelledby="g-title">
  <div class="wrap gruppi__grid">
    <div class="gruppi__text dg-head">
      {T('c.gruppi.eyebrow', 'p', 'dg-eyebrow')}
      <h2 id="g-title" class="dg-display dg-display--l"><span data-t="c.gruppi.h1">{I['c.gruppi.h1']}</span> <em data-t="c.gruppi.h2">{I['c.gruppi.h2']}</em></h2>
      {T('c.gruppi.lede', 'p', 'dg-lede')}
      <div class="dg-row gruppi__btns"><a class="dg-btn dg-btn--crema" href="{TEL}"><span data-t="btn.chiama">{I['btn.chiama']}</span>&nbsp;0583 49 21 16</a><a class="dg-btn dg-btn--outline-crema" href="{MAIL}" data-t="btn.email">{I['btn.email']}</a></div>
    </div>
    <div class="gruppi__photo"><img src="images/grigliata-mista-carne.webp" data-t-attr="alt:c.gruppi.alt" alt="{I['c.gruppi.alt']}" width="1358" height="1250" loading="lazy"></div>
  </div>
</section>
</main>
""" + footer() + tail()

pages["404.html"] = head("404") + header("") + f"""<main id="main">
<section class="nf dg-on-red">
  <div class="wrap">
    <h1 class="dg-display dg-display--xl"><span data-t="nf.h1">{I['nf.h1']}</span> <em data-t="nf.h2">{I['nf.h2']}</em></h1>
    {T('nf.lede', 'p', 'dg-lede')}
    <div class="dg-row"><a class="dg-btn dg-btn--crema" href="index.html" data-t="nf.home">{I['nf.home']}</a><a class="dg-btn dg-btn--outline-crema" href="menu.html" data-t="btn.menu">{I['btn.menu']}</a></div>
  </div>
</section>
</main>
""" + footer() + tail()

css = open(os.path.join(SITE, "css/tokens.css")).read() + "\n" + open(os.path.join(HERE, "components.css")).read() + "\n" + open(os.path.join(HERE, "pages.css")).read()
open(os.path.join(SITE, "css/styles.css"), "w").write(css)
for name, html in pages.items():
    open(os.path.join(SITE, name), "w").write(html)
print("built", ", ".join(pages))
