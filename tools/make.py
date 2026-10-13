#!/usr/bin/env python3
"""Phnom Penh → mot-dang/assets/sites/phnom-penh/ (index.html, th/, km/, pp.js, img/, fonts/, card.json, icon.svg).

A city home page in the shape of motdang.net/sites/pathum-thani/: map and calendar on top, then the TL;DR.
The page's own files are relative and motdang.net pages absolute, so a city build can copy the folder to a subdomain root.

    python3 tools/make.py
"""
import datetime
import html
import json
import pathlib
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import content as C  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent
MD = HERE.parent / "mot-dang"
PSAR = HERE.parent / "phnom-penh"
OUT = MD / "assets" / "sites" / "phnom-penh"
URL = "https://motdang.net/sites/phnom-penh/"
MAP = "https://motdang.net/sites/doodle-phnom-penh/"
DIR = "https://nanobotco.github.io/phnom-penh/"
E = html.escape
PICS = json.loads((HERE / "research" / "pics.json").read_text())
LANGS = ("en", "km", "th")
LOCALE = {"en": "en_US", "km": "km_KH", "th": "th_TH"}
LANGNAME = {"en": "EN", "km": "ខ្មែរ", "th": "ไทย"}


def L(d, lang):
    if not isinstance(d, dict):
        return d
    return d.get(lang) or d.get("en")


def U(k, lang):
    return L(C.UI[k], lang)


# ------------------------------------------------------------------ calendar
def events():
    rows = []
    soon = json.loads((PSAR / "data" / "soon.json").read_text())
    for r in soon["items"]:
        rows.append({"start": r["start"], "end": r.get("end"), "t": {"en": r["en"], "th": r["th"], "km": r.get("km")},
                     "w": {"en": r["line_en"], "th": r["line_th"], "km": r.get("line_km")}, "u": r.get("src"),
                     "s": {"en": "National Bank of Cambodia: holidays", "th": "ธนาคารแห่งชาติกัมพูชา: วันหยุด", "km": "ធនាគារជាតិនៃកម្ពុជា៖ ថ្ងៃឈប់សម្រាក"}, "kind": "hol"})
    seen = {(r["start"]) for r in rows}
    src = MD / "_incoming" / "pt-pp-dates-2026-10-13.json"
    if src.exists():
        for r in json.loads(src.read_text()).get("pp", []):
            if r["start"] in seen:
                continue
            rows.append({"start": r["start"], "end": r.get("end"), "t": {"en": r["title_en"], "th": r.get("title_th"), "km": r.get("title_km")},
                         "w": {"en": r.get("venue_en") or "", "th": r.get("venue_th"), "km": None}, "u": r.get("source_url"), "s": r.get("source_name", ""), "kind": ""})
    for r in C.EXTRA_DATES:
        rows.append(r)
    rows.sort(key=lambda r: r["start"])
    return rows


def cal_json(lang):
    out = [{"start": r["start"], "end": r.get("end"), "t": L(r["t"], lang), "w": L(r["w"], lang) or "", "u": r.get("u"), "s": L(r.get("s", ""), lang), "kind": r.get("kind", "")} for r in events()]
    return json.dumps(out, ensure_ascii=False).replace("</", "<\\/")


# ------------------------------------------------------------------ pieces
def src_link(item, lang):
    if not item.get("src"):
        return ""
    return f'<a class="src" href="{E(item["src"])}" rel="noopener">{E(item.get("src_name") or U("source", lang))}</a>'


def credit(k):
    m = PICS[k]
    return f'{E(m["author"] or "Wikimedia Commons")} · <a href="{E(m["page"])}" rel="noopener">{E(m["lic"])}</a>'


def img(k, alt, cap):
    m = PICS[k]
    return (f'<img src="{{R}}img/{k}-800.jpg" srcset="{{R}}img/{k}-800.jpg 800w, {{R}}img/{k}-1600.jpg 1600w" sizes="(max-width:800px) 100vw, 50vw" '
            f'width="{m["w"]}" height="{m["h"]}" loading="lazy" decoding="async" alt="{E(alt)}" data-full="{{R}}img/{k}-1600.jpg" '
            f'data-cap="{E(cap + " · ")}{E(credit(k))}">')


def band(b, lang):
    k, cap = b["pic"], L(b["cap"], lang)
    return f'<figure class="band">{img(k, cap, cap)}<figcaption>{E(cap)}<small>{credit(k)}</small></figcaption></figure>'


def toy(t, lang):
    btns = "".join(f'<button id="{bid}"{" class=alt" if k else ""}>{E(L(lab, lang))}</button>' for k, (bid, lab) in enumerate(t.get("buttons", [])))
    return (f'<div class="toy"><h3>{E(L(t["h"], lang))}</h3><p>{E(L(t["p"], lang))}</p>'
            f'<canvas id="{t["id"]}" aria-label="{E(L(t["h"], lang))}"></canvas>'
            f'<div class="bar">{btns}<span class="read" id="{t["read"]}" aria-live="polite"></span></div></div>')


def face(name):
    """A drawn monogram: a ring of lotus petals and the first letter, spins on tap."""
    ch = E(name.strip()[0])
    petals = "".join(f'<ellipse cx="32" cy="9" rx="5" ry="9" transform="rotate({a} 32 32)" fill="#e9b949"/>' for a in range(0, 360, 45))
    return f'<svg class="face" viewBox="0 0 64 64" aria-hidden="true">{petals}<circle cx="32" cy="32" r="17" fill="#7a1f24"/><text x="32" y="39" text-anchor="middle" font-family="Prompt,sans-serif" font-size="20" fill="#fff">{ch}</text></svg>'


def cards(items, lang, kind=""):
    out = []
    for it in items:
        tag = f'<span class="tag">{E(L(it["tag"], lang))}</span>' if it.get("tag") else ""
        others = " · ".join(it["name"][x] for x in LANGS if x != lang and it["name"].get(x))
        fc = face(L(it["name"], "en")) if kind == "person" else ""
        out.append(f'<article class="card {kind}">{fc}{tag}<h3>{E(L(it["name"], lang))}</h3><p class="th">{E(others)}</p>'
                   f'<p>{E(L(it["text"], lang))}</p>{src_link(it, lang)}</article>')
    return f'<div class="cards">{"".join(out)}</div>'


def section(sid, k, body, lang, dek=True):
    d = C.UI.get(k + "_d")
    return (f'<section id="{sid}"><div class="wrap"><p class="kicker">{E(U(k + "_k", lang))}</p><h2>{E(U(k + "_h", lang))}</h2>'
            + (f'<p class="dek">{E(L(d, lang))}</p>' if d else "") + body + '</div></section>')


FONTS = [  # (family, weight, file stem, subset, source folder)
    ("Prompt", 600, "prompt-600-latin", "latin", "lanna"), ("Prompt", 600, "prompt-600-thai", "thai", "lanna"),
    ("Sarabun", 400, "sarabun-400-latin", "latin", "lanna"), ("Sarabun", 400, "sarabun-400-thai", "thai", "lanna"),
    ("Sarabun", 600, "sarabun-600-latin", "latin", "lanna"), ("Sarabun", 600, "sarabun-600-thai", "thai", "lanna"),
    ("Kantumruy Pro", 400, "KantumruyPro-400-khmer", "khmer", "psar"), ("Kantumruy Pro", 600, "KantumruyPro-600-khmer", "khmer", "psar"),
    ("Moul", 400, "Moul-400-khmer", "khmer", "psar"),
]
RANGES = {"thai": "U+0E01-0E5B,U+200C-200D,U+25CC", "khmer": "U+1780-17FF,U+19E0-19FF,U+200C-200D,U+25CC",
          "latin": "U+0000-00FF,U+0131,U+0152-0153,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2212,U+0E3F"}


def fonts_css(R):
    return "".join(f"@font-face{{font-family:'{fam}';font-style:normal;font-weight:{wt};font-display:swap;src:url({R}fonts/{stem}.woff2) format('woff2');unicode-range:{RANGES[sub]}}}"
                   for fam, wt, stem, sub, _ in FONTS)


def page(lang):
    R = "" if lang == "en" else "../"
    S = C.UI
    path = "" if lang == "en" else lang + "/"
    langs = "".join(f'<a class="lang" href="{R}{"" if x == "en" else x + "/"}" hreflang="{x}">{LANGNAME[x]}</a>' for x in LANGS if x != lang)
    nav = "".join(f'<a href="#{a}">{E(L(t, lang))}</a>' for a, t in C.NAV)
    canon = URL + path
    title, desc = U("title", lang), U("desc", lang)
    tldr = "".join(f'<li>{L(x, lang)}</li>' for x in C.TLDR)
    slab = "".join(f'<div class="num" role="button" tabindex="0"><b>{E(n["v"])}</b><span>{E(L(n["l"], lang))}</span></div>' for n in C.NUMBERS)
    tl = "".join(f'<li><b>{E(L(t["y"], lang))}</b>{E(L(t["text"], lang))} {src_link(t, lang)}</li>' for t in C.TIMELINE)
    pics = "".join(f'<figure>{img(p["pic"], L(p["cap"], lang), L(p["cap"], lang))}<figcaption>{E(L(p["cap"], lang))}</figcaption></figure>' for p in C.PICS)
    srcs = sorted({(it.get("src_name") or it["src"], it["src"]) for grp in (C.TIMELINE, C.LEGENDS, C.PEOPLE, C.SITES, C.CULTURE, C.FOOD, C.NUMBERS) for it in grp if it.get("src")})
    srcl = "".join(f'<li><a href="{E(u)}" rel="noopener">{E(n)}</a></li>' for n, u in srcs)
    soon = "".join(f"<li>{E(L(x, lang))}</li>" for x in C.SOON)
    T = C.TOYS
    jsdata = (f'<script type="application/json" id="evdata">{cal_json(lang)}</script>'
              f'<script type="application/json" id="toywords">{json.dumps(C.TOYWORDS, ensure_ascii=False)}</script>'
              f'<script type="application/json" id="handposes">{json.dumps(C.HANDS, ensure_ascii=False)}</script>'
              f'<script type="application/json" id="bowlsteps">{json.dumps(C.BOWL, ensure_ascii=False)}</script>')
    body = f"""
<nav class="top" aria-label="{E(U('sections', lang))}"><a class="home" href="https://motdang.net/">{E(U('home', lang))}</a>{nav}<span class="langs">{langs}</span></nav>
<header class="wrap mast"><h1>{E(U('h1', lang))}<small>{E(U('h1small', lang))}</small></h1><p>{E(U('lede', lang))}</p></header>
<div class="wrap top2" id="map">
<div class="mapbox"><iframe src="{MAP}?embed=1" title="{E(U('map_t', lang))}" loading="lazy" allow="geolocation"></iframe><a class="open" href="{MAP}">{E(U('map_open', lang))}</a></div>
<div class="cal" id="calendar"><h2>{E(U('cal_h', lang))}</h2><div id="evlist"><p class="empty">…</p></div><h2 class="soon">{E(U('soon_h', lang))}</h2><ul class="soonl">{soon}</ul></div>
</div>
{jsdata}
<div class="hero"><canvas id="river" aria-label="{E(U('river_a', lang))}"></canvas><div class="herotext"><p class="kicker">{E(U('river_k', lang))}</p><h2>{E(U('river_h', lang))}</h2><p>{E(U('river_p', lang))}</p><p class="count"><button id="season" class="seasonb"></button> <span id="seasonread"></span></p><p class="count" id="boatcount" aria-live="polite"></p></div></div>
{section('tldr', 'tldr', f'<ul class="tldr">{tldr}</ul><div class="slab">{slab}</div>', lang)}
{section('history', 'hist', f'<ol class="tl">{tl}</ol>', lang)}
{band(C.BANDS['history'], lang)}
{section('legends', 'leg', cards(C.LEGENDS, lang, 'legend') + toy(T['penh'], lang), lang)}
{band(C.BANDS['legends'], lang)}
{section('people', 'ppl', cards(C.PEOPLE, lang, 'person'), lang)}
{section('sites', 'site', cards(C.SITES, lang), lang)}
{band(C.BANDS['sites'], lang)}
{section('culture', 'cul', cards(C.CULTURE, lang) + toy(T['hands'], lang), lang)}
{band(C.BANDS['culture'], lang)}
{section('food', 'food', cards(C.FOOD, lang) + toy(T['bowl'], lang), lang)}
{section('pics', 'pic', f'<div class="pics">{pics}</div>', lang)}
{section('sources', 'src', f'<ul class="sources">{srcl}</ul>', lang)}
<footer><a href="https://motdang.net/">มดแดง · Mot Dang</a> · <a href="{DIR}">{E(U('dir', lang))}</a> · <a href="https://motdang.net/sites/">{E(U('all', lang))}</a></footer>
<dialog id="lb"><form method="dialog"><button class="x" aria-label="Close">×</button></form><img alt=""><p></p></dialog>
<script src="{R}pp.js" defer></script>"""
    body = body.replace("{R}", R)
    css = (HERE / "tools" / "style.css").read_text()
    alts = "".join(f'<link rel="alternate" hreflang="{x}" href="{URL}{"" if x == "en" else x + "/"}">' for x in LANGS)
    head = f"""<!doctype html><html lang="{lang}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#3a1218">
<link rel="canonical" href="{canon}">
{alts}<link rel="alternate" hreflang="x-default" href="{URL}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Mot Dang · มดแดง">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{URL}card.jpg"><meta property="og:image:alt" content="{E(U('card_alt', lang))}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:locale" content="{LOCALE[lang]}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{URL}card.jpg">
<link rel="icon" href="{R}icon.svg" type="image/svg+xml">
<style>{fonts_css(R)}{css}</style>
</head><body>"""
    return head + body + "\n</body></html>\n"


ICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#3a1218"/>'
        '<path d="M32 6 L35 20 L29 20Z" fill="#e9b949"/><path d="M14 34 L32 18 L50 34Z" fill="#e9b949"/><path d="M18 40 L32 28 L46 40Z" fill="#c9962a"/>'
        '<rect x="20" y="40" width="24" height="8" fill="#9e2a2b"/><path d="M6 54 Q20 48 32 54 T58 54" stroke="#6fb3c7" stroke-width="4" fill="none"/></svg>')


def main():
    for d in ("", "th", "km", "img", "fonts"):
        (OUT / d).mkdir(parents=True, exist_ok=True)
    srcs = {"lanna": MD / "assets" / "sites" / "lanna-craft" / "fonts", "psar": PSAR / "docs" / "fonts"}
    for _, _, stem, _, where in FONTS:
        f = srcs[where] / (stem + ".woff2")
        if not (OUT / "fonts" / f.name).exists():
            shutil.copy2(f, OUT / "fonts" / f.name)
    for lic in ("OFL-prompt.txt", "OFL-sarabun.txt"):
        shutil.copy2(srcs["lanna"] / lic, OUT / "fonts" / lic)
    (OUT / "fonts" / "OFL-kantumruy-moul.txt").write_text("Kantumruy Pro and Moul: SIL Open Font License 1.1, https://openfontlicense.org/open-font-license-official-text/\n")
    for f in (HERE / "src" / "img").iterdir():
        dst = OUT / "img" / f.name
        if not dst.exists() or dst.stat().st_mtime < f.stat().st_mtime:
            shutil.copy2(f, dst)
    shutil.copy2(HERE / "tools" / "pp.js", OUT / "pp.js")
    (OUT / "icon.svg").write_text(ICON)
    (OUT / "index.html").write_text(page("en"))
    for x in ("th", "km"):
        (OUT / x / "index.html").write_text(page(x))
    if (HERE / "card.jpg").exists():
        shutil.copy2(HERE / "card.jpg", OUT / "card.jpg")
    card = {"id": "phnom-penh", "th": C.UI["h1"]["th"], "en": C.UI["h1"]["en"], "km": C.UI["h1"]["km"],
            "line_th": C.UI["card_line"]["th"], "line_en": C.UI["card_line"]["en"], "icon": "i-map",
            "shipped": datetime.date.today().isoformat(), "group": "go", "where": "elsewhere", "served": "docs", "words": C.WORDS}
    (OUT / "card.json").write_text(json.dumps(card, ensure_ascii=False, indent=1))
    print("wrote", OUT)


if __name__ == "__main__":
    main()
