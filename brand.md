# Da Gherardo brand guideline (v1)

Live version: the Da Gherardo design system on claude.ai. This file is a copy for Claude in VS Code. `brand-tokens.json` has every value, `brand-components.css` the ready-made styles (prefix `dg-`). Photos: `photos-originals/`. Inspiration: `inspiration/` with its README.

## Colours

| Token | Giorno (light) | Sera (dark) | Use |
|---|---|---|---|
| `crema` | #fcf7ee | #18120f | Page background. The cream of their paper placemats by day; the night sky over the piazza in the Sera theme. |
| `carta` | #f4ead8 | #261c17 | Paper panels: menu cards, the hours card, form fields, the text side of a split. Never a whole page. |
| `bianco` | #fffdf8 | #fffdf8 | The white border of a cartolina (postcard photo) and the light stripe of the tenda. Same in both themes, like a real postcard. |
| `inchiostro` | #1f1915 | #f6ecdd | Headlines and body text on `crema` and `carta`. The black ink of the engraved logo. |
| `inchiostro-muted` | #62564c | #c4b4a3 | Dish descriptions, captions, secondary lines on `crema` and `carta`. |
| `filo` | #e6d9c3 | #3a2e27 | Hairline dividers between menu items and sections. Never for controls. |
| `rosso` | #c1141e | #c1141e | Pomodoro red, the brand colour. Full-bleed hero and poster bands, the tenda stripes, the primary button, giant headline type on `crema`. Each page gets at least one big `rosso` moment. |
| `vino` | #7a0e16 | #5c0a10 | Deep wine red. One poster band per page at most, the footer, the menu page ground on dark. Text on it is `on-rosso`; small gold accents are `senape`. |
| `rosso-text` | #c1141e | #ff8e80 | Red text and links on `crema` and `carta`: prices, the italic accent word, hover. 5.8:1 on `crema` (light), 8.3:1 (dark). |
| `on-rosso` | #fcf7ee | #fcf7ee | Text, icons and focus rings on `rosso` and `vino` fills (5.8:1 on `rosso`). |
| `cielo` | #bcd6ec | #2b4964 | Summer sky blue. The holiday accent: one band or block per page (the Senza glutine section, the map, a postcard stamp). Text on it is `inchiostro`. `rosso` type on `cielo` only at 24px and larger (4.1:1). |
| `senape` | #eab53e | #eab53e | Mustard, from their placemats and the sun on the piazza. Stamps, the francobollo, one small block on the cover, small labels on `vino`. Decorative: text on it is always the light-theme `inchiostro` #1f1915, never white. |
| `on-senape` | #1f1915 | #1f1915 | Text on `senape` and on `cielo` in the light theme (9.2:1 on senape). |
| `focus` | #1f1915 | #f6ecdd | Keyboard focus ring on `crema` and `carta`: 2px solid, 3px offset. On `rosso` and `vino` bands use `on-rosso` instead. |

## Fonts (Google Fonts)

- Display: **Instrument Serif** 400, regular and italic. Headlines and the giant name.
- Label: **Antonio** 600, 700. Uppercase labels, buttons, nav, tabs, menu categories.
- Sans: **Figtree** 400, 500, 600, 400 italic. Everything else.

| Style | Size / line height | Use |
|---|---|---|
| `display-poster` (display) | 240px / 0.86 | Giant poster type, edge to edge, on a `rosso` ground (home hero) or in `rosso` on `crema`. clamp(96px, 17vw, 260px). Once per page. |
| `display-xl` (display) | 128px / 0.9 | Page titles. clamp(64px, 10vw, 144px). Sentence case, one word may be italic. |
| `display-l` (display) | 72px / 0.96 | Section headlines, sentence case, at most one italic word in `rosso-text`. clamp(44px, 6vw, 84px). |
| `display-m` (display) | 40px / 1.05 | Card titles, postcard captions on big cards, the price of the moment. |
| `display-italic` (display) | 72px / 0.96 | The italic accent word inside a headline, always in `rosso-text` on light grounds or `senape` on `vino`. |
| `label-l` (label) | 30px / 1 | Menu category titles, ticket headings, the big word on a stamp. Uppercase, in `rosso-text`. |
| `eyebrow` (label) | 15px / 18px | Uppercase labels above headlines and in poster corners. |
| `button` (label) | 16px / 18px | Buttons, nav links, menu tabs. Uppercase. |
| `lede` (sans) | 21px / 31px | One or two intro sentences. Max 42 characters wide. |
| `body` (sans) | 17px / 28px | Running text. Max 62 characters wide. |
| `menu-item` (sans) | 19px / 26px | Dish names, wine names, list items. |
| `price` (sans) | 18px / 26px | Prices, with tabular numbers, in `rosso-text`. `15 €` in Italian, `€15` in English. |
| `small` (sans) | 15px / 22px | Dish descriptions and captions in `inchiostro-muted`. |

## Spacing, radius, shadow

- `space-1` 4px: Icon to label.
- `space-2` 8px: Eyebrow to headline; dish name to description.
- `space-3` 16px: Between menu items; inside buttons (vertical); the mobile side gutter.
- `space-4` 24px: Headline to lede; between buttons; card padding; the tenda scallop width is 2 of these.
- `space-5` 40px: Lede to buttons or content; desktop column gap.
- `space-6` 64px: Section padding on mobile; desktop side gutter.
- `space-7` 104px: Section padding on desktop: clamp(56px, 9vh, 104px). Never more.
- `header-h` 76px: Fixed header height. Sections fit calc(100svh - header-h); anchors use it as scroll-margin-top.
- `tenda-h` 56px: Height of the tenda (awning) edge: 32px stripes plus 24px scallops.
- `measure` 62ch: Max width of running text.
- `radius-none` 0: Bands, poster blocks, menu frames, full-bleed photos.
- `radius-xs` 2px: Cartolina photos inside their white border, form fields, tabs.
- `radius-pill` 999px: Buttons and the language switch: round like a sun lounger cushion. The only round controls.
- `radius-ellisse` 50%: The ellisse: a photo cut to the oval of Piazza Anfiteatro, and round stamps.
- `shadow-cartolina` 0 14px 28px rgba(31, 25, 21, 0.18): Only on a cartolina (postcard photo), so it lifts off the page like a postcard on a table. Nothing else has a shadow.

## Components (previews in the live design system)

### Button

Pill buttons in the condensed label face, uppercase: `dg-btn` (primary, `rosso`), `dg-btn--ghost` (ink outline) on light grounds; `dg-btn--crema` and `dg-btn--outline-crema` on `rosso` and `vino` bands.

- The consumer provides the label and the link. Labels say what happens: "Prenota un tavolo", "Il menu", "Scrivici su WhatsApp", "Chiama 0583 49 21 16".
- At most two per section, one primary and one secondary. Never two buttons to the same place.
- Phone and WhatsApp are real `tel:` and `https://wa.me/393929581765` links, styled like any button, never browser blue.
- Focus: 2px solid `focus` ring at 3px offset; inside `.dg-on-red` the ring is `on-rosso`.

### Cartolina

A photo printed like a holiday postcard: a `bianco` border with a deeper bottom edge, a short italic caption, a small tilt (`--tilt`, between -3deg and 3deg) and `shadow-cartolina`. An optional `dg-francobollo` (perforated stamp in `senape` or `cielo`) sits on the corner.

- The consumer provides the photo, a caption of two or three words ("Dal forno", "Porcini freschi") and the tilt.
- Use them in a row of three or four, in a horizontal strip that scrolls sideways on phones, on `cielo` or `crema`. Alternate the tilt direction.
- At most one stamp per two postcards. Stamps carry one or two words, never a sentence.
- The only element in the system with a shadow.

### Disegni

Single-stroke line drawings in `inchiostro` (or `on-rosso` inside `.dg-on-red`), 1.5px, round caps, in the spirit of the engraved logo: a fiasco and calice, a fork twirling tagliatelle, the oval piazza.

- Placeholders until the real thing: ideally commission or hand-draw a small set in the same ink style as the logo. Never AI-generated images.
- At most one drawing per page, small, beside a headline or in a corner of a band. Never competing with a photo.

### Ellisse

A photo cut to a 4:3 oval, the shape of Piazza Anfiteatro, the Roman amphitheatre square the restaurant sits on and the shape of its engraved logo. A thin `inchiostro` ring sits around it, with an optional dotted inner ring and the address running around the edge.

- The consumer provides one photo and, optionally, the running text (address and what they serve; no slogans).
- Once per page, on `crema`, `carta` or (with `--ring: var(--on-rosso)`) on `rosso`.
- Best photos: plates from above or close (tortelli, pizza, aperitivo spread). Never a photo with a sponsor logo at its centre.

### Logo

Two forms. The engraving: their own logo, a black ink drawing of the oval Piazza Anfiteatro seen from above with "Da Gherardo" in script in the middle. The wordmark: "Da Gherardo" in italic `display` plus "TRATTORIA · PIZZERIA · LUCCA" in the label face at 0.26em tracking, stacked.

- The engraving is only a crop from a screenshot of their old site. Use it only on paper grounds (`bianco`, `crema`, `carta`) with `mix-blend-mode: multiply`, at most 320px wide, until they send the original file. Never redraw, recolour or trace it.
- Use the wordmark in the header and anywhere the logo would sit on `rosso`, `vino` or dark grounds.

### MenuCard

The menu as a printed card on `carta`, edged with a solid `rosso` hairline and a dotted inner line (like Brasserie Lolita's printed menus). Tabs across the top, the category title in `label-l`, dishes in two columns.

- The consumer provides the tabs (Antipasti, Primi di terra, Primi di mare, Secondi, Pizze, Senza glutine, Vini e bar, Dolci e caffè), and for each dish: the name as on their menu, the price (`15 €` IT, `€15` EN, per hg prices as `4,50 €/hg`) and a short description.
- Never cut a dish to make a tab fit. Two columns on desktop; on phones one column with a "Mostra altri / Show more" page-through inside the tab.
- A `dg-tag` "GF" (on `cielo`) marks dishes also made gluten free; `*` marks frozen products, explained once at the foot of the card with the coperto (1,50 € a persona).
- The tabs are visible in the first screen of the menu page.

### OrariCard

Address, phone, WhatsApp, email, seats and hours on a `carta` card with the same double `rosso` rule as the menu. Labels in the condensed face, values in the sans, links in `rosso-text`.

- The consumer provides the rows. Hours are not on their current site: until the restaurant confirms them, show "Pranzo e cena" and mark the row `data-tbc`.
- Phone and WhatsApp are real links. Groups (birthdays, communions, school trips) get one line under the card.

### PosterHero

The home hero: "Da" and "Gherardo" in `display-poster` on a full-bleed `rosso` ground, with a top-down plate photo cut into the ellisse between the two words, the tenda along the top edge and four small corner labels.

- The consumer provides one plate photo (tortelli 01, pizza 06 or grigliata 09), the four corner labels and the two buttons.
- "Gherardo" is set in italic. The ring around the plate is `on-rosso`; the plate sits on an 8px `rosso` collar so it cuts into the letters cleanly.
- The two buttons sit centred under the name: `dg-btn--crema` "Prenota un tavolo" and `dg-btn--outline-crema` "Il menu". Both are fully visible in the first screen at 1280x720 and 390x844.
- On phones the right-hand corner labels hide and the name shrinks with the clamp.
- Once per site. This is the only full-screen section.

### SectionHeader

Eyebrow, headline and one short lede: the opening of every section.

- The consumer provides the eyebrow (uppercase, 2 to 5 words), the headline (sentence case, at most one word in `<em>`, which turns italic and `rosso-text`) and one or two lede sentences.
- Use the italic accent word on the hero and section openers only, not on every heading.
- The headline is `display-l` and should fill most of its column. If it looks small in its space, the space is too big.

### Tenda

The striped, scalloped edge of the awnings over the tables on Piazza Anfiteatro ("all'ombra delle nostre tende"): `rosso` and `bianco` stripes 48px wide with a half-round scallop under each. `dg-tenda` is 56px tall (`tenda-h`), `dg-tenda--sm` 28px.

- Purely decorative: `role="presentation"`, no text on it.
- Use it full-width along the top of the home hero, under the header on inner pages, or above the footer. At most twice per page.
- It always runs edge to edge; never inside a card.

### Timbro

A round rubber-stamp mark in `rosso-text`, tilted -8deg: "Senza glutine" in the centre and "Laboratorio certificato AIC · Lucca" around the ring. It carries their strongest fact: a separate gluten-free kitchen certified by AIC (Associazione Italiana Celiachia).

- The consumer provides only the words, from the content doc. Never invent a claim or a year.
- Use it once per page at most: on the home Senza glutine section, the Senza glutine page and the menu's Senza glutine tab. It overlaps a photo or block edge.
- It does not replace the real AIC, Gluto and Find Me Gluten Free badges: those appear as images in the footer, unchanged.


---

Trattoria Pizzeria Da Gherardo sits on Piazza Anfiteatro in Lucca, the oval square built on a Roman amphitheatre, with 100 seats under red awnings in the piazza and 80 inside. It serves Lucchese and Tuscan cooking, pizza at lunch and dinner, and has a separate gluten-free kitchen certified by AIC. The brand should feel like a summer holiday in Italy, done properly: a classic trattoria, red and cheerful, with the polish of a good hotel. Simple, modern, fun, easy to find your way around.

The house wine label already says it: **"Un'atmosfera intrappolata nel tempo."**

## Inspiration

Three Amsterdam sites set the direction. Take the moves, not the layouts.

- **Brasserie Lolita** (brasserielolita.nl): cream paper ground, brick red type, the printed-menu look with a double red rule, hand-drawn ink illustrations, letterspaced capitals, a sticky "Reserve a table" pill. Source of the MenuCard and OrariCard.
- **Ilario** (ilario.nl): full-bleed red bands alternating with white, chunky condensed capitals, white-bordered photos tilted like polaroids, white line doodles on red, an illustrated "Dove trovarci" map. Source of the Cartolina, the red bands and the label face.
- **Linguini** (linguini.nl): an engraving-style illustration set that matches Da Gherardo's own engraved logo, a soft blue band, italic serif headings, a video hero of the kitchen. Source of the Disegni, the `cielo` accent and the italic accent word.

## Voice

- Italian first, English with the switch. Address guests as *tu*: "Prenota il tuo tavolo", "Ti aspettiamo in piazza".
- Say what is on the plate, in their words: "Tortelli lucchesi casalinghi al ragù", "pici cacio e pepe", "la zuppa toscana".
- Lean on the place: "in piazza Anfiteatro", "all'ombra delle nostre tende", "aperitivo in piazza".
- Gluten free is a fact, said plainly: "Pane, pasta e impasti per la pizza preparati nel nostro laboratorio senza glutine, certificato da AIC."
- Do: one or two sentences per section, dish names exactly as on the menu, prices as `15 €` (IT) and `€15` (EN).
- Don't: emoji, em dashes, exclamation marks in headlines, superlatives, marketing words ("esperienza unica", "eccellenza").

## Colour

- `rosso` carries the brand. Every page gets at least one big `rosso` moment: a full-bleed band, giant `display-poster` type, or the tenda. Use it boldly and in large areas, not as a trace.
- `crema` is the page, `carta` the paper of cards and menus. Keep about half of every page light so the red reads as deliberate.
- `vino` is the deep note: the footer and at most one poster band per page. On `vino`, accents are `senape`.
- `cielo` is the holiday: one band or block per page, usually behind the postcards or the Senza glutine section. `inchiostro` text on it; `rosso` type on `cielo` only at 24px and up.
- `senape` is the sun and the placemats: stamps and small labels only. Text on it is always `on-senape`.
- `inchiostro` is the engraving: body text, ink drawings, the ellisse ring.
- Nothing is ever browser blue. Links are `rosso-text`; phone, WhatsApp and email links are styled like everything else.

## Type

- **Instrument Serif** (`display`): headlines, page titles and the giant name. Sentence case. One word per headline may be italic in `rosso-text` (`display-italic`): on the hero and section openers only.
- **Antonio** (`label`): uppercase labels, buttons, nav, menu tabs and menu category titles (`label-l`). Never for sentences.
- **Figtree** (`sans`): everything else: `lede`, `body`, `menu-item`, `price`, `small`.
- Menus, lists and prices are always Figtree. Prices use tabular numbers.
- Headlines fill most of their column. Body 17px, ledes 21px, menu items 19px, buttons 16px.
- Load from Google Fonts: Instrument Serif (regular and italic), Antonio 600 and 700, Figtree 400, 500, 600 and 400 italic.

## Layout

- No section is taller than one screen, and none is stretched to fill one: height comes from content plus `space-7` padding (clamp(56px, 9vh, 104px)). The home hero is the only full-screen section.
- Home page: the PosterHero plus at most three sections and the footer.
- Mix the layouts: a full-bleed red band, a split with a photo in the ellisse, a strip of postcards on `cielo`, the printed menu card. Never three identical splits in a row.
- Square corners on bands, cards and photos. Pills for buttons. Ovals only for the ellisse and stamps. The only shadow is `shadow-cartolina`.
- The header is 76px (`header-h`), crema, with the wordmark left, at most five links, the IT / EN switch and a `rosso` "Prenota" pill. A sticky "Prenota" pill also floats bottom right on phones, like Lolita's.
- Long content (the menu, the wine list) sits in one screen with tabs, never one endless page.

## The signature moves

1. **La tenda** (the awning): the striped, scalloped edge of their awnings in the piazza, full-width at the top of the hero, under the header on inner pages or above the footer.
2. **L'ellisse** (the piazza): a photo cut to the oval of Piazza Anfiteatro, with a thin ink ring and the address running around it. Once per page.
3. **La cartolina** (the postcard): photos with a white border, a small tilt, a caption and sometimes a stamp, in a strip of three or four on `cielo`.
4. **Il menu stampato** (the printed menu): `carta` card with a solid `rosso` hairline and a dotted inner rule, for the menu, the hours and the gluten-free card.
5. **Il timbro** (the stamp): the round "Senza glutine, laboratorio certificato AIC" stamp, tilted over a photo edge.

Use two or three per page, never all five. Motion: the tenda's stripes slide in once on load, postcards straighten slightly on hover, sections fade up 16px. Respect `prefers-reduced-motion`.

## Photography

- Use the restaurant's own professional photos: bright daylight on the piazza, red tablecloths, mustard placemats, dark speckled stoneware, hands twirling pasta, the house wine bottle.
- Crop out sponsor branding (Coca-Cola, Sprite, Fanta placemats) wherever it distracts.
- Plates from above or close (tortelli 01, astice 04, grigliata 09) go in the ellisse. Hands and tables (porcini 02, crostini 11, aperitivo 12) go in postcards and splits. The pizza in the oven (06) is the most dramatic image: use it big, on a dark or red band.
- Still missing and worth asking for or shooting: the piazza and terrace with the awnings, the interior, the gluten-free kitchen.
- No stock photos and no AI-generated images.

## Illustration and icons

- One small single-stroke ink drawing per page at most (`Disegni`), in the spirit of the engraved logo.
- Icons: thin line icons, 1.5px stroke, Phosphor Light or Lucide, in `inchiostro` or `on-rosso`.

## Logo

- The real mark is the engraving of the oval piazza with "Da Gherardo" in script. Only a crop from a screenshot of the old site exists (`Logos/logo-anfiteatro.png`): use it on paper grounds only, never on red, never redrawn. Ask the restaurant for the original file.
- Everywhere else, set the wordmark as text: "Da Gherardo" in italic `display`, "TRATTORIA · PIZZERIA · LUCCA" under it in `label` at 0.26em tracking.
- The AIC, Gluto and Find Me Gluten Free badges are their own marks: show them unchanged in the footer.

## Accessibility

- Every text pair holds 4.5:1 in both themes; giant poster type is decorative and never carries information alone.
- Focus: 2px solid ring, 3px offset, in `focus` on light grounds and `on-rosso` on red and wine.
- Phone and WhatsApp numbers are real links in brand colours.
