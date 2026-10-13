#!/bin/sh
# card.sh — card.jpg (1200×630): the four rivers at dusk with the title, shot by headless Chrome.
cd "$(dirname "$0")/.." || exit 1
OUT="../mot-dang/assets/sites/phnom-penh"
mkdir -p scratch
python3 - "$OUT" <<'PY'
import sys, pathlib
out = pathlib.Path(sys.argv[1])
css = (pathlib.Path("tools/style.css")).read_text()
fonts = (out / "index.html").read_text().split("<style>")[1].split(":root{")[0]
html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><style>{css}
html,body{{margin:0;width:1200px;height:630px;overflow:hidden}}.hero{{height:630px!important;min-height:0}}
.herotext{{padding:46px 56px}}.herotext h2{{font-size:118px;line-height:.95}}.herotext .th{{font:600 54px Prompt,sans-serif;color:#f6b3c8;margin:.2rem 0 .6rem}}.herotext p{{font-size:26px;max-width:640px}}
.scrim{{position:absolute;inset:0 0 40% 0;background:linear-gradient(rgba(8,30,36,.72),rgba(8,30,36,.35) 70%,transparent)}}.herotext{{z-index:2}}.mark{{position:absolute;right:40px;bottom:30px;font:600 22px Prompt,sans-serif;color:#fff;background:#0b2a31cc;padding:.3rem .9rem;border-radius:99px}}</style>
<link rel="stylesheet" href="data:text/css,"></head><body><div class="hero"><canvas id="river"></canvas><div class="scrim"></div><div class="herotext"><h2>Phnom Penh</h2><div class="th">ភ្នំពេញ · พนมเปญ</div><p>Four rivers, Lady Penh's hill, the palace, legends, food, a map and what's on.</p></div><div class="mark">motdang.net</div></div>
<script src="pp.js"></script></body></html>"""
html = html.replace("<style>", "<style>" + fonts, 1)
words = (out / "index.html").read_text().split('<script type="application/json" id="toywords">')[1].split("</script>")[0]
html = html.replace('<script src="pp.js">', '<script type="application/json" id="toywords">' + words + '</script><script src="pp.js">')
(out / "_card.html").write_text(html)
PY
python3 -I -c "import os,http.server;os.chdir('../mot-dang/assets');http.server.ThreadingHTTPServer(('127.0.0.1',8989),http.server.SimpleHTTPRequestHandler).serve_forever()" & S=$!
sleep 1
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
perl -e 'alarm 60; exec @ARGV' "$CH" --headless=new --disable-gpu --hide-scrollbars --window-size=1200,630 --force-device-scale-factor=1 \
  --screenshot=scratch/card.png --virtual-time-budget=5000 "http://127.0.0.1:8989/sites/phnom-penh/_card.html?t=18" 2>/dev/null
kill $S
rm -f "$OUT/_card.html"
sips -s format jpeg -s formatOptions 84 scratch/card.png --out card.jpg >/dev/null && echo "wrote card.jpg"
