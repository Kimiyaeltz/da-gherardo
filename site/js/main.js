(function () {
  "use strict";
  var I = window.DG_I18N || { it: {}, en: {} };
  var root = document.documentElement;
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };
  var params = new URLSearchParams(location.search);
  var lang = params.get("lang") || store.get("dg-lang") || "it";
  if (!I[lang]) lang = "it";

  /* ?bozza highlights everything still to confirm, for the whole session */
  try {
    if (params.has("bozza")) sessionStorage.setItem("dg-bozza", "1");
    if (sessionStorage.getItem("dg-bozza")) root.classList.add("bozza");
  } catch (e) { if (params.has("bozza")) root.classList.add("bozza"); }

  function t(key) { return (I[lang] && I[lang][key]) || I.it[key] || key; }

  function applyLang() {
    root.lang = lang;
    document.querySelectorAll("[data-t]").forEach(function (el) { el.textContent = t(el.getAttribute("data-t")); });
    document.querySelectorAll("[data-t-attr]").forEach(function (el) {
      el.getAttribute("data-t-attr").split(";").forEach(function (pair) {
        var p = pair.split(":"); if (p.length === 2) el.setAttribute(p[0].trim(), t(p[1].trim()));
      });
    });
    var page = document.body.getAttribute("data-page");
    if (page) {
      document.title = t("meta." + page + ".title");
      var d = document.querySelector('meta[name="description"]');
      if (d && I[lang]["meta." + page + ".desc"]) d.setAttribute("content", t("meta." + page + ".desc"));
    }
    document.querySelectorAll("[data-lang]").forEach(function (b) {
      b.setAttribute("aria-pressed", b.getAttribute("data-lang") === lang ? "true" : "false");
    });
    if (window.DG_renderMenu) window.DG_renderMenu();
  }
  window.DG_t = t;
  window.DG_lang = function () { return lang; };

  document.querySelectorAll("[data-lang]").forEach(function (b) {
    b.addEventListener("click", function () {
      lang = b.getAttribute("data-lang"); store.set("dg-lang", lang); applyLang();
    });
  });

  /* Mobile navigation */
  var toggle = document.querySelector(".dg-nav-toggle");
  var nav = document.getElementById("dg-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") !== "true";
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.setAttribute("aria-label", t(open ? "nav.close" : "nav.open"));
      root.classList.toggle("nav-open", open);
    });
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { root.classList.remove("nav-open"); toggle.setAttribute("aria-expanded", "false"); });
    });
  }

  /* Header gets a hairline after scrolling */
  var header = document.querySelector(".dg-header");
  function onScroll() { if (header) header.classList.toggle("is-scrolled", window.scrollY > 8); }
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();

  /* Menu: tabs, and page-through so each tab fits one screen */
  var menuEl = document.getElementById("dg-menu");
  if (menuEl && window.DG_MENU) {
    var tabsEl = menuEl.querySelector(".dg-tabs");
    var listEl = menuEl.querySelector(".dg-dishes");
    var pagerEl = menuEl.querySelector(".dg-pager");
    var introEl = menuEl.querySelector(".dg-menu__intro");
    var photoEl = document.getElementById("dg-menu-photo");
    var current = (location.hash || "").replace("#", "");
    if (!window.DG_MENU.some(function (c) { return c.id === current; })) current = window.DG_MENU[0].id;
    var page = 0, pages = [];

    function price(p) {
      var it = lang === "it";
      function one(v) {
        if (v.charAt(0) === "+") { var n = v.slice(2); return it ? "+ " + n + " €" : "+ €" + n.replace(",", "."); }
        return it ? v + " €" : "€" + v.replace(",", ".");
      }
      if (Array.isArray(p) && Array.isArray(p[0])) return p.map(function (s) { return s[0] + " " + one(s[1]); }).join(" · ");
      if (Array.isArray(p)) return one(p[0]) + "/" + p[1];
      return one(p);
    }

    function buildTabs() {
      tabsEl.innerHTML = "";
      window.DG_MENU.forEach(function (c) {
        var li = document.createElement("li");
        var b = document.createElement("button");
        b.type = "button"; b.className = "dg-tab"; b.id = "tab-" + c.id;
        b.setAttribute("role", "tab"); b.setAttribute("aria-controls", "dg-panel");
        b.setAttribute("aria-selected", c.id === current ? "true" : "false");
        b.tabIndex = c.id === current ? 0 : -1;
        b.textContent = lang === "it" ? c.it : c.en;
        b.addEventListener("click", function () { select(c.id, true); });
        b.addEventListener("keydown", function (e) {
          var i = window.DG_MENU.findIndex(function (x) { return x.id === current; });
          if (e.key === "ArrowRight" || e.key === "ArrowLeft") {
            e.preventDefault();
            var n = (i + (e.key === "ArrowRight" ? 1 : -1) + window.DG_MENU.length) % window.DG_MENU.length;
            select(window.DG_MENU[n].id, true);
            document.getElementById("tab-" + window.DG_MENU[n].id).focus();
          }
        });
        li.appendChild(b); tabsEl.appendChild(li);
      });
    }

    function rows(cat) {
      var out = [];
      cat.groups.forEach(function (g) {
        if (cat.groups.length > 1) out.push({ head: lang === "it" ? g.it : g.en });
        g.items.forEach(function (it) { out.push({ item: it }); });
      });
      return out;
    }

    function rowEl(r) {
      var li = document.createElement("li");
      if (r.head) { li.className = "dg-dish-head"; li.textContent = r.head; return li; }
      var it = r.item, flags = it[4] || "";
      li.className = "dg-dish";
      var name = document.createElement("span"); name.className = "dg-dish__name";
      name.textContent = it[0] + (flags.indexOf("f") > -1 ? " *" : "");
      if (flags.indexOf("gf") > -1) { var tag = document.createElement("span"); tag.className = "dg-tag"; tag.textContent = "GF"; name.appendChild(tag); }
      var pr = document.createElement("span"); pr.className = "dg-dish__price"; pr.textContent = price(it[3]);
      li.appendChild(name); li.appendChild(pr);
      var desc = lang === "it" ? it[1] : (it[2] || it[1]);
      if (desc) { var d = document.createElement("span"); d.className = "dg-dish__desc"; d.textContent = desc; li.appendChild(d); }
      return li;
    }

    /* Split rows into pages that fit the list's available height */
    function paginate(cat) {
      var all = rows(cat); pages = []; listEl.innerHTML = "";
      /* reserve the pager's height while measuring, so pages are sized for the final layout */
      pagerEl.innerHTML = '<button class="dg-pager__btn" type="button" tabindex="-1">' + t("menu.prev") + '</button><span class="dg-pager__info">' + t("menu.page") + ' 88 ' + t("menu.of") + ' 88</span><button class="dg-pager__btn dg-pager__btn--next" type="button" tabindex="-1">' + t("menu.more") + '</button>';
      var maxH = listEl.clientHeight;
      var cur = [];
      for (var i = 0; i < all.length; i++) {
        var el = rowEl(all[i]); listEl.appendChild(el);
        if ((listEl.scrollHeight > maxH + 1 || listEl.scrollWidth > listEl.clientWidth + 1) && cur.length) {
          listEl.removeChild(el);
          if (cur.length && cur[cur.length - 1].head) { cur.pop(); i--; }
          pages.push(cur); cur = []; listEl.innerHTML = ""; i--;
          continue;
        }
        cur.push(all[i]);
      }
      if (cur.length) pages.push(cur);
      listEl.innerHTML = "";
    }

    function drawPage() {
      listEl.innerHTML = "";
      (pages[page] || []).forEach(function (r) { listEl.appendChild(rowEl(r)); });
      pagerEl.innerHTML = "";
      if (pages.length > 1) {
        var prev = document.createElement("button"); prev.type = "button"; prev.className = "dg-pager__btn";
        prev.textContent = t("menu.prev"); prev.disabled = page === 0;
        prev.addEventListener("click", function () { page--; drawPage(); });
        var info = document.createElement("span"); info.className = "dg-pager__info";
        info.textContent = t("menu.page") + " " + (page + 1) + " " + t("menu.of") + " " + pages.length;
        var next = document.createElement("button"); next.type = "button"; next.className = "dg-pager__btn dg-pager__btn--next";
        next.textContent = t("menu.more"); next.disabled = page === pages.length - 1;
        next.addEventListener("click", function () { page++; drawPage(); });
        pagerEl.appendChild(prev); pagerEl.appendChild(info); pagerEl.appendChild(next);
      }
    }

    function select(id, push) {
      current = id; page = 0;
      var cat = window.DG_MENU.find(function (c) { return c.id === id; });
      tabsEl.querySelectorAll(".dg-tab").forEach(function (b) {
        var on = b.id === "tab-" + id; b.setAttribute("aria-selected", on ? "true" : "false"); b.tabIndex = on ? 0 : -1;
      });
      introEl.textContent = lang === "it" ? cat.introIt : cat.introEn;
      if (photoEl) {
        var img = photoEl.querySelector("img");
        if (cat.photo) { photoEl.hidden = false; img.src = "images/" + cat.photo + ".webp"; img.alt = lang === "it" ? cat.it : cat.en; }
        else photoEl.hidden = true;
        menuEl.classList.toggle("no-photo", !cat.photo);
      }
      paginate(cat); drawPage();
      if (push) { try { history.replaceState(null, "", "#" + id); } catch (e) {} }
    }

    window.DG_renderMenu = function () { buildTabs(); select(current, false); };
    var rt; window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(function () { select(current, false); }, 150); });
    window.addEventListener("hashchange", function () {
      var h = location.hash.replace("#", ""); if (h && h !== current && window.DG_MENU.some(function (c) { return c.id === h; })) select(h, false);
    });
  }

  applyLang();
  if (document.fonts && document.fonts.ready && window.DG_renderMenu) document.fonts.ready.then(function () { window.DG_renderMenu(); });
})();
