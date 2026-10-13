/* Phnom Penh minisite: Chaktomuk rivers, Lady Penh's hill, Royal Ballet hands, kuy teav. Every drawing answers a tap. */
(function () {
  'use strict';
  var LANG = document.documentElement.lang;
  var RM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var T = function (en, th, km) { return LANG === 'th' ? th : LANG === 'km' ? (km || en) : en; };
  var TAU = Math.PI * 2;
  var WORDS = {};
  try { WORDS = JSON.parse(document.getElementById('toywords').textContent); } catch (e) {}
  function W(k) { var v = WORDS[k]; return v ? (v[LANG] || v.en) : k; }

  function fit(cv) {
    var r = cv.getBoundingClientRect(), d = Math.min(window.devicePixelRatio || 1, 2);
    cv.width = Math.round(r.width * d); cv.height = Math.round(r.height * d);
    var c = cv.getContext('2d'); c.setTransform(d, 0, 0, d, 0, 0);
    return { c: c, w: r.width, h: r.height };
  }
  function pt(cv, e) { var r = cv.getBoundingClientRect(); return { x: e.clientX - r.left, y: e.clientY - r.top }; }
  function rnd(a, b) { return a + Math.random() * (b - a); }
  function ppHour() { var m = /[?&]t=(\d+)/.exec(location.search); if (m) return +m[1]; var d = new Date(); return (d.getUTCHours() + 7 + d.getUTCMinutes() / 60) % 24; }
  function ppMonth() { return new Date(Date.now() + 7 * 3600e3).getUTCMonth() + 1; }
  function loop(fn, cv) {
    var on = true, last = 0;
    if ('IntersectionObserver' in window) new IntersectionObserver(function (e) { on = e[0].isIntersecting; if (on) requestAnimationFrame(tick); }).observe(cv);
    function tick(t) { if (!on) return; var dt = Math.min(0.05, (t - (last || t)) / 1000); last = t; fn(dt, t / 1000); requestAnimationFrame(tick); }
    requestAnimationFrame(tick);
  }
  function q(p0, p1, p2, t) { var u = 1 - t; return { x: u * u * p0.x + 2 * u * t * p1.x + t * t * p2.x, y: u * u * p0.y + 2 * u * t * p1.y + t * t * p2.y }; }

  /* ------------------------------------------------------------ Chaktomuk */
  function rivers() {
    var cv = document.getElementById('river'); if (!cv) return;
    var S = fit(cv), parts = [], boats = [], sparks = [], wet = ppMonth() >= 6 && ppMonth() <= 10, raced = 0;
    var out = document.getElementById('boatcount'), sw = document.getElementById('season');
    function arms() {
      var w = S.w, h = S.h, C = { x: w * 0.6, y: h * 0.52 };
      return [
        { k: 'tonlesap', a: { x: w * 0.36, y: -20 }, m: { x: w * 0.5, y: h * 0.25 }, b: C, wd: Math.max(26, w * 0.045), dir: wet ? -1 : 1 },
        { k: 'mekong', a: { x: w + 20, y: h * 0.02 }, m: { x: w * 0.72, y: h * 0.3 }, b: C, wd: Math.max(44, w * 0.08), dir: 1 },
        { k: 'lower', a: C, m: { x: w * 0.74, y: h * 0.78 }, b: { x: w + 20, y: h + 20 }, wd: Math.max(44, w * 0.085), dir: 1 },
        { k: 'bassac', a: C, m: { x: w * 0.56, y: h * 0.8 }, b: { x: w * 0.48, y: h + 20 }, wd: Math.max(22, w * 0.04), dir: 1 }
      ];
    }
    function seed() { parts = []; arms().forEach(function (A, i) { for (var k = 0; k < 60; k++) parts.push({ i: i, t: Math.random(), o: rnd(-0.4, 0.4), s: rnd(0.04, 0.08) }); }); }
    seed();
    function label() {
      if (sw) sw.textContent = wet ? W('season_dry') : W('season_wet');
      var r = document.getElementById('seasonread');
      if (r) r.textContent = wet ? W('flow_wet') : W('flow_dry');
    }
    label();
    function palace(c, x, y, t, night) {
      c.save(); c.translate(x, y);
      c.fillStyle = night ? '#2a1f12' : '#7a2a22';
      c.fillRect(-26, -6, 52, 10);
      c.fillStyle = night ? '#4a3418' : '#c9962a';
      for (var k = 0; k < 3; k++) { c.beginPath(); c.moveTo(-22 + k * 4, -6 - k * 7); c.lineTo(0, -16 - k * 8); c.lineTo(22 - k * 4, -6 - k * 7); c.fill(); }
      c.strokeStyle = night ? '#f2c230' : '#e9b949'; c.lineWidth = 2; c.beginPath(); c.moveTo(0, -38); c.lineTo(0, -56); c.stroke();
      if (night) for (var j = -24; j <= 24; j += 6) { c.fillStyle = 'rgba(255,214,120,' + (0.6 + 0.4 * Math.sin(t * 3 + j)) + ')'; c.fillRect(j, -7, 2, 2); }
      c.restore();
    }
    loop(function (dt, t) {
      var c = S.c, w = S.w, h = S.h, hr = ppHour(), night = hr < 6 || hr > 18.6, dusk = (hr > 17.2 && hr <= 18.6) || (hr >= 5.4 && hr < 6.6);
      var land = night ? '#1b2a22' : dusk ? '#6d5a3e' : '#8fa36a';
      c.fillStyle = land; c.fillRect(0, 0, w, h);
      // streets of the old town on the west bank
      c.strokeStyle = night ? 'rgba(255,214,120,.12)' : 'rgba(255,255,255,.18)'; c.lineWidth = 1;
      for (var gx = 0; gx < w * 0.52; gx += 22) { c.beginPath(); c.moveTo(gx, 0); c.lineTo(gx - 30, h); c.stroke(); }
      for (var gy = 0; gy < h; gy += 22) { c.beginPath(); c.moveTo(0, gy); c.lineTo(w * 0.5 - gy * 0.1, gy); c.stroke(); }
      var A = arms();
      A.forEach(function (a) {
        c.strokeStyle = night ? '#173c4a' : dusk ? '#b07a52' : '#7b6b45'; c.lineWidth = a.wd + 6; c.lineCap = 'round';
        c.beginPath(); c.moveTo(a.a.x, a.a.y); c.quadraticCurveTo(a.m.x, a.m.y, a.b.x, a.b.y); c.stroke();
      });
      A.forEach(function (a) {
        c.strokeStyle = night ? '#24566a' : dusk ? '#c98f62' : '#a68a55'; c.lineWidth = a.wd;
        c.beginPath(); c.moveTo(a.a.x, a.a.y); c.quadraticCurveTo(a.m.x, a.m.y, a.b.x, a.b.y); c.stroke();
      });
      // silt lines carried by the current
      parts.forEach(function (p) {
        var a = A[p.i]; p.t += p.s * dt * a.dir; if (p.t > 1) p.t -= 1; if (p.t < 0) p.t += 1;
        var P = q(a.a, a.m, a.b, p.t), P2 = q(a.a, a.m, a.b, Math.min(1, Math.max(0, p.t + 0.01)));
        var nx = -(P2.y - P.y), ny = P2.x - P.x, nl = Math.hypot(nx, ny) || 1;
        var x = P.x + nx / nl * p.o * a.wd, y = P.y + ny / nl * p.o * a.wd;
        c.strokeStyle = 'rgba(255,248,230,.45)'; c.lineWidth = 1.4;
        c.beginPath(); c.moveTo(x, y); c.lineTo(x - (P2.x - P.x) * 6 * a.dir, y - (P2.y - P.y) * 6 * a.dir); c.stroke();
      });
      // Wat Phnom's hill and stupa, then the palace at the meeting
      var wx = w * 0.3, wy = h * 0.34;
      c.fillStyle = night ? '#16301f' : '#4f7a3a'; c.beginPath(); c.ellipse(wx, wy, 18, 10, 0, 0, TAU); c.fill();
      c.fillStyle = night ? '#d9c79a' : '#f1ead6'; c.beginPath(); c.moveTo(wx - 6, wy - 4); c.lineTo(wx, wy - 22); c.lineTo(wx + 6, wy - 4); c.fill();
      palace(c, w * 0.47, h * 0.5, t, night || dusk);
      // dragon boats
      boats = boats.filter(function (b) { b.t += b.v * dt; return b.t >= 0 && b.t <= 1; });
      boats.forEach(function (b) {
        var a = A[b.i], P = q(a.a, a.m, a.b, b.t), P2 = q(a.a, a.m, a.b, Math.min(1, Math.max(0, b.t + 0.01 * Math.sign(b.v))));
        var ang = Math.atan2(P2.y - P.y, P2.x - P.x);
        c.save(); c.translate(P.x + b.off, P.y); c.rotate(ang);
        c.fillStyle = b.col; c.beginPath(); c.moveTo(-34, -3); c.lineTo(30, -3); c.quadraticCurveTo(40, 0, 30, 3); c.lineTo(-34, 3); c.closePath(); c.fill();
        c.fillStyle = '#f2c230'; c.beginPath(); c.moveTo(30, -3); c.lineTo(42, -9); c.lineTo(36, 0); c.fill(); // the naga head
        for (var k = -28; k < 26; k += 4) {
          var s = Math.sin(t * 14 + k * 0.5);
          c.fillStyle = '#fff'; c.beginPath(); c.arc(k, 0, 1.4, 0, TAU); c.fill();
          c.strokeStyle = 'rgba(255,255,255,.7)'; c.lineWidth = 1; c.beginPath(); c.moveTo(k, -3); c.lineTo(k - 3 * s, -7); c.moveTo(k, 3); c.lineTo(k - 3 * s, 7); c.stroke();
        }
        c.restore();
      });
      sparks = sparks.filter(function (s) { s.vy += 40 * dt; s.x += s.vx * dt; s.y += s.vy * dt; s.a -= dt * 0.7; return s.a > 0; });
      sparks.forEach(function (s) { c.fillStyle = 'hsla(' + s.h + ',95%,65%,' + s.a + ')'; c.beginPath(); c.arc(s.x, s.y, 2, 0, TAU); c.fill(); });
      c.font = '600 12px "Kantumruy Pro",Prompt,sans-serif'; c.textAlign = 'center';
      [['tonlesap', w * 0.43, h * 0.16], ['mekong', w * 0.82, h * 0.16], ['lower', w * 0.82, h * 0.86], ['bassac', w * 0.5, h * 0.9]].forEach(function (L) {
        var s = W(L[0]); c.fillStyle = 'rgba(11,24,30,.6)'; var tw = c.measureText(s).width; c.fillRect(L[1] - tw / 2 - 6, L[2] - 13, tw + 12, 18); c.fillStyle = '#fff4dc'; c.fillText(s, L[1], L[2]);
      });
    }, cv);
    cv.addEventListener('pointerdown', function (e) {
      var p = pt(cv, e), w = S.w, h = S.h;
      if (Math.hypot(p.x - w * 0.47, p.y - h * 0.47) < 40) { // fireworks over the palace
        for (var k = 0; k < 60; k++) { var a = rnd(0, TAU), v = rnd(30, 120); sparks.push({ x: w * 0.47, y: h * 0.3, vx: Math.cos(a) * v, vy: Math.sin(a) * v, a: 1, h: rnd(20, 60) }); }
        return;
      }
      var A = arms(), best = 0, bd = 1e9, bt = 0;
      A.forEach(function (a, i) { for (var s = 0; s <= 1; s += 0.02) { var P = q(a.a, a.m, a.b, s), d = Math.hypot(P.x - p.x, P.y - p.y); if (d < bd) { bd = d; best = i; bt = s; } } });
      var dir = A[best].dir;
      boats.push({ i: best, t: dir > 0 ? Math.max(0, bt - 0.15) : Math.min(1, bt + 0.15), v: dir * rnd(0.12, 0.18), off: rnd(-6, 6), col: ['#9e2a2b', '#1f5f8b', '#2f6b2a', '#6b3fa0'][raced % 4] });
      raced++;
      if (out) out.textContent = raced + ' ' + (raced === 1 ? W('boat1') : W('boats'));
    });
    if (sw) sw.onclick = function () { wet = !wet; label(); };
    window.addEventListener('resize', function () { S = fit(cv); });
  }

  /* ------------------------------------------------------- Lady Penh's hill */
  function penh() {
    var cv = document.getElementById('penh'); if (!cv) return;
    var S = fit(cv), st = 0, x = 0, baskets = 0, H = 0, glow = 0, out = document.getElementById('penhread');
    function reset() { st = 0; x = S.w + 60; baskets = 0; H = 0; glow = 0; say(W('penh0')); }
    function say(s) { if (out) out.textContent = s; }
    reset();
    loop(function (dt, t) {
      var c = S.c, w = S.w, h = S.h, bank = w * 0.48, wl = h * 0.62;
      var g = c.createLinearGradient(0, 0, 0, h); g.addColorStop(0, '#f3c98b'); g.addColorStop(0.6, '#f7e3bd'); c.fillStyle = g; c.fillRect(0, 0, w, h);
      c.fillStyle = '#7a8b4e'; c.fillRect(0, wl, bank, h - wl);
      c.fillStyle = '#a68a55'; c.fillRect(bank, wl + 6, w - bank, h - wl);
      c.strokeStyle = 'rgba(255,255,255,.3)'; for (var yy = wl + 14; yy < h; yy += 10) { c.beginPath(); for (var xx = bank; xx < w; xx += 10) c.lineTo(xx, yy + Math.sin(xx * 0.05 + t * 2) * 1.5); c.stroke(); }
      // the hill Penh raised
      var hx = bank * 0.45, hw = bank * 0.42;
      if (H > 0) {
        c.fillStyle = '#5f7a36'; c.beginPath(); c.moveTo(hx - hw, wl); c.quadraticCurveTo(hx, wl - H * 2, hx + hw, wl); c.fill();
        if (H > 70) { // the shrine on top
          var ty = wl - H;
          c.fillStyle = '#f1ead6'; c.fillRect(hx - 16, ty - 18, 32, 18);
          c.fillStyle = '#9e2a2b'; c.beginPath(); c.moveTo(hx - 22, ty - 18); c.lineTo(hx, ty - 36); c.lineTo(hx + 22, ty - 18); c.fill();
          c.fillStyle = '#e9b949'; c.beginPath(); c.moveTo(hx - 4, ty - 36); c.lineTo(hx, ty - 52); c.lineTo(hx + 4, ty - 36); c.fill();
          if (glow > 0) { c.fillStyle = 'rgba(255,220,120,' + glow * 0.5 + ')'; c.beginPath(); c.arc(hx, ty - 24, 40, 0, TAU); c.fill(); glow -= dt * 0.4; }
        }
      }
      // Penh, at the water's edge
      var px = bank - 22, py = wl;
      c.fillStyle = '#9e2a2b'; c.fillRect(px - 6, py - 26, 12, 18);
      c.fillStyle = '#f0f0f0'; c.fillRect(px - 6, py - 34, 12, 8);
      c.fillStyle = '#8a5a3a'; c.beginPath(); c.arc(px, py - 40, 6, 0, TAU); c.fill();
      c.fillStyle = '#e8e2d6'; c.beginPath(); c.arc(px, py - 43, 5, Math.PI, TAU); c.fill(); // grey hair
      // the koki tree in the flood
      if (st === 0) { x -= dt * 40; if (x < bank + 30) x = S.w + 60; }
      if (st === 1) { x += (bank + 20 - x) * dt * 3; if (Math.abs(x - bank - 20) < 2) { st = 2; say(W('penh1')); } }
      if (st <= 2) {
        var ty2 = wl + 6 + Math.sin(t * 2) * 2;
        c.save(); c.translate(x, ty2); c.rotate(Math.sin(t) * 0.05);
        c.fillStyle = '#6b4a2a'; c.fillRect(-50, -7, 100, 14);
        c.strokeStyle = '#4a3218'; c.lineWidth = 3; c.beginPath(); c.moveTo(40, -5); c.lineTo(58, -16); c.moveTo(-40, 4); c.lineTo(-58, 12); c.stroke();
        if (st === 2) for (var k = 0; k < 5; k++) { // what was inside
          var bx = -36 + k * 18;
          c.fillStyle = k === 4 ? '#9a9a90' : '#e9b949'; c.beginPath(); c.arc(bx, -14, 4, 0, TAU); c.fill(); c.fillRect(bx - 4, -10, 8, 8);
          c.fillStyle = 'rgba(255,230,150,' + (0.3 + 0.3 * Math.sin(t * 4 + k)) + ')'; c.beginPath(); c.arc(bx, -12, 9, 0, TAU); c.fill();
        }
        c.restore();
      }
    }, cv);
    cv.addEventListener('pointerdown', function () {
      if (st === 0) { st = 1; return; }
      if (st === 2) { st = 3; }
      if (st === 3) {
        baskets++; H = Math.min(110, baskets * 11);
        if (H >= 110 && glow <= 0) { glow = 1; say(W('penh3')); } else say(baskets + ' ' + W('penh2'));
      }
    });
    var b = document.getElementById('penhreset'); if (b) b.onclick = reset;
    window.addEventListener('resize', function () { S = fit(cv); });
  }

  /* --------------------------------------------------- Royal Ballet hands */
  function hands() {
    var cv = document.getElementById('hands'); if (!cv) return;
    var S = fit(cv), poses = [], cur = 0, from = null, k = 1, petals = [], out = document.getElementById('handread');
    try { poses = JSON.parse(document.getElementById('handposes').textContent); } catch (e) {}
    if (!poses.length) return;
    function lerp(a, b, t) { return a.map(function (v, i) { return v + (b[i] - v) * t; }); }
    function say() { if (out) out.textContent = poses[cur].name[LANG] || poses[cur].name.en; }
    say();
    function joints(len, angs) { // points along a finger: three segments, each turned by its joint angle
      var p = [{ x: 0, y: 0 }], a = 0, x = 0, y = 0, parts = [0.44, 0.32, 0.24];
      for (var s = 0; s < 3; s++) { a += angs[s]; x += Math.sin(a) * len * parts[s]; y -= Math.cos(a) * len * parts[s]; p.push({ x: x, y: y }); }
      return p;
    }
    function finger(c, len, w, angs, pass) {
      var p = joints(len, angs);
      for (var s = 0; s < 3; s++) {
        var ww = w * [1, 0.9, 0.78][s];
        c.lineCap = 'round'; c.lineJoin = 'round';
        c.strokeStyle = pass ? '#dba574' : '#a8714a'; c.lineWidth = pass ? ww : ww + 2.5;
        c.beginPath(); c.moveTo(p[s].x, p[s].y); c.lineTo(p[s + 1].x, p[s + 1].y); c.stroke();
      }
      if (pass) { // the nail
        var e = p[3], d = p[2], ang = Math.atan2(e.y - d.y, e.x - d.x);
        c.save(); c.translate(e.x - Math.cos(ang) * w * 0.15, e.y - Math.sin(ang) * w * 0.15); c.rotate(ang);
        c.fillStyle = '#f3e1cf'; c.beginPath(); c.ellipse(0, 0, w * 0.3, w * 0.24, 0, 0, TAU); c.fill(); c.restore();
      }
    }
    loop(function (dt, t) {
      var c = S.c, w = S.w, h = S.h; c.clearRect(0, 0, w, h);
      var g = c.createRadialGradient(w / 2, h * 0.55, 10, w / 2, h * 0.55, w * 0.6); g.addColorStop(0, '#3a1f2b'); g.addColorStop(1, '#120a10'); c.fillStyle = g; c.fillRect(0, 0, w, h);
      if (k < 1) k = Math.min(1, k + dt * 2.2);
      var P = from ? lerp(from, poses[cur].a, k * k * (3 - 2 * k)) : poses[cur].a;
      var sc = Math.min(w / 300, h / 270);
      c.save(); c.translate(w / 2, h * 0.92); c.scale(sc, sc); c.rotate(P[15] || 0);
      c.fillStyle = '#dba574'; c.fillRect(-28, -14, 56, 64); // wrist
      c.fillStyle = '#e9b949'; c.fillRect(-29, -2, 58, 9); c.fillRect(-29, 12, 58, 5); // bracelets
      c.translate(0, -10);
      var base = [[-27, -76], [-9, -84], [9, -82], [26, -72]], lens = [74, 96, 104, 94];
      for (var pass = 0; pass < 2; pass++) {
        if (pass) { c.fillStyle = '#dba574'; c.beginPath(); c.ellipse(0, -40, 40, 46, 0, 0, TAU); c.fill(); } // palm over the outlines
        else { c.fillStyle = '#a8714a'; c.beginPath(); c.ellipse(0, -40, 41.5, 47.5, 0, 0, TAU); c.fill(); }
        for (var f = 0; f < 4; f++) { c.save(); c.translate(base[f][0], base[f][1]); c.rotate((f - 1.5) * 0.07); finger(c, lens[f], 20, [P[f * 3], P[f * 3 + 1], P[f * 3 + 2]], pass); c.restore(); }
        c.save(); c.translate(32, -32); c.rotate(0.85); finger(c, 66, 22, [P[12], P[13], P[14]], pass); c.restore(); // thumb
      }
      c.strokeStyle = 'rgba(140,90,60,.35)'; c.lineWidth = 1.5; c.beginPath(); c.arc(4, -30, 26, 2.4, 3.6); c.stroke(); // a palm line
      c.restore();
      petals = petals.filter(function (p) { p.y += p.v * dt; p.x += Math.sin(t * 2 + p.ph) * 0.5; p.r += dt; return p.y < h + 10; });
      petals.forEach(function (p) { c.save(); c.translate(p.x, p.y); c.rotate(p.r); c.fillStyle = p.c; c.beginPath(); c.ellipse(0, 0, 4, 7, 0, 0, TAU); c.fill(); c.restore(); });
    }, cv);
    cv.addEventListener('pointerdown', function () {
      from = poses[cur].a.slice(); cur = (cur + 1) % poses.length; k = RM ? 1 : 0; say();
      for (var i = 0; i < 14; i++) petals.push({ x: rnd(0, S.w), y: rnd(-60, 0), v: rnd(30, 70), r: rnd(0, 3), ph: rnd(0, 6), c: ['#f2c230', '#f6b3c8', '#ffffff'][i % 3] });
    });
    window.addEventListener('resize', function () { S = fit(cv); });
  }

  /* ---------------------------------------------------------------- kuy teav */
  function bowl() {
    var cv = document.getElementById('bowl'); if (!cv) return;
    var S = fit(cv), items = [], drops = [], steam = [], eaten = 0, out = document.getElementById('bowlread');
    var steps = [];
    try { steps = JSON.parse(document.getElementById('bowlsteps').textContent); } catch (e) {}
    var n = 0;
    function draw(c, it, t) {
      c.save(); c.translate(it.x, it.y); c.rotate(it.r);
      var k = it.k;
      if (k === 'noodles') { c.strokeStyle = '#f4efe2'; c.lineWidth = 2.2; for (var i = 0; i < 26; i++) { c.beginPath(); c.arc(rnd(-2, 2), 0, 10 + i * 2.2, i, i + 2.2); c.stroke(); } }
      else if (k === 'broth') { c.fillStyle = 'rgba(214,170,90,.35)'; c.beginPath(); c.arc(0, 0, it.R, 0, TAU); c.fill(); }
      else if (k === 'mince') { c.fillStyle = '#8a5a3a'; for (var j = 0; j < 14; j++) { c.beginPath(); c.arc(Math.cos(j) * 10, Math.sin(j * 1.7) * 10, 3, 0, TAU); c.fill(); } }
      else if (k === 'pork') { c.fillStyle = '#e0b6a0'; c.fillRect(-14, -6, 28, 12); c.fillStyle = '#c98d78'; c.fillRect(-14, -6, 28, 3); }
      else if (k === 'shrimp') { c.strokeStyle = '#f08a5d'; c.lineWidth = 6; c.lineCap = 'round'; c.beginPath(); c.arc(0, 0, 9, 0.3, 4.6); c.stroke(); }
      else if (k === 'garlic') { c.fillStyle = '#d9a441'; for (var g2 = 0; g2 < 30; g2++) { c.fillRect(Math.cos(g2 * 2.1) * 16 * Math.random(), Math.sin(g2 * 2.1) * 16 * Math.random(), 2, 2); } }
      else if (k === 'onion') { c.fillStyle = '#5fae3a'; for (var o = 0; o < 10; o++) { c.beginPath(); c.arc(Math.cos(o) * 14, Math.sin(o * 1.3) * 14, 2.5, 0, TAU); c.fill(); } }
      else if (k === 'sprouts') { c.strokeStyle = '#f2f0dc'; c.lineWidth = 2; for (var s = 0; s < 8; s++) { c.beginPath(); c.moveTo(s * 3 - 12, -8); c.quadraticCurveTo(s * 3 - 8, 0, s * 3 - 12, 10); c.stroke(); } }
      else if (k === 'lime') { c.fillStyle = '#9bd04a'; c.beginPath(); c.arc(0, 0, 10, 0, Math.PI); c.fill(); c.fillStyle = '#e6f6c4'; c.beginPath(); c.arc(0, 0, 7.5, 0, Math.PI); c.fill(); }
      else if (k === 'chili') { c.fillStyle = '#d6301f'; for (var ch = 0; ch < 6; ch++) { c.beginPath(); c.ellipse(Math.cos(ch) * 8, Math.sin(ch) * 8, 3, 2, ch, 0, TAU); c.fill(); } }
      c.restore();
    }
    loop(function (dt, t) {
      var c = S.c, w = S.w, h = S.h, cx = w / 2, cy = h / 2, R = Math.min(w, h) * 0.38;
      c.fillStyle = '#5a2b1c'; c.fillRect(0, 0, w, h);
      c.strokeStyle = 'rgba(0,0,0,.18)'; for (var y = 0; y < h; y += 16) { c.beginPath(); c.moveTo(0, y); c.lineTo(w, y + 6); c.stroke(); } // the table
      c.fillStyle = '#eef0ea'; c.beginPath(); c.arc(cx, cy, R + 16, 0, TAU); c.fill();
      c.strokeStyle = '#2f6aa3'; c.lineWidth = 4; c.beginPath(); c.arc(cx, cy, R + 9, 0, TAU); c.stroke();
      c.fillStyle = '#e8dcc0'; c.beginPath(); c.arc(cx, cy, R, 0, TAU); c.fill();
      c.save(); c.beginPath(); c.arc(cx, cy, R, 0, TAU); c.clip();
      items.forEach(function (it) { it.y += (it.ty - it.y) * Math.min(1, dt * 8); draw(c, it, t); });
      c.restore();
      drops = drops.filter(function (d) { d.r += dt * 60; d.a -= dt * 1.4; return d.a > 0; });
      drops.forEach(function (d) { c.strokeStyle = 'rgba(255,255,255,' + d.a + ')'; c.lineWidth = 2; c.beginPath(); c.arc(d.x, d.y, d.r, 0, TAU); c.stroke(); });
      if (items.length && Math.random() < 0.15) steam.push({ x: cx + rnd(-R * 0.6, R * 0.6), y: cy, a: 0.6 });
      steam = steam.filter(function (s) { s.y -= 26 * dt; s.a -= dt * 0.35; return s.a > 0; });
      steam.forEach(function (s) { c.strokeStyle = 'rgba(255,255,255,' + s.a + ')'; c.lineWidth = 3; c.beginPath(); c.moveTo(s.x, s.y); c.quadraticCurveTo(s.x + 8 * Math.sin(t + s.x), s.y - 12, s.x, s.y - 24); c.stroke(); });
    }, cv);
    cv.addEventListener('pointerdown', function (e) {
      var p = pt(cv, e), cx = S.w / 2, cy = S.h / 2, R = Math.min(S.w, S.h) * 0.38;
      if (n < steps.length) {
        var st = steps[n], many = st.k === 'noodles' || st.k === 'broth' ? 1 : 3;
        for (var i = 0; i < many; i++) {
          var a = rnd(0, TAU), r = many === 1 ? 0 : rnd(R * 0.15, R * 0.7);
          items.push({ k: st.k, x: cx + Math.cos(a) * r, ty: cy + Math.sin(a) * r, y: cy + Math.sin(a) * r - 80, r: rnd(0, TAU), R: R });
        }
        drops.push({ x: p.x, y: p.y, r: 4, a: 1 });
        if (out) out.textContent = (st[LANG] || st.en) + (n === steps.length - 1 ? ' · ' + W('bowl_done') : '');
        n++;
      } else {
        items.splice(0, Math.max(1, Math.ceil(items.length / 4)));
        if (!items.length) { n = 0; eaten++; if (out) out.textContent = eaten + ' ' + W('bowl_eaten'); }
      }
    });
    window.addEventListener('resize', function () { S = fit(cv); });
  }

  /* ------------------------------------------------- calendar, numbers, faces, pictures */
  function calendar() {
    var box = document.getElementById('evlist'), data = document.getElementById('evdata'); if (!box || !data) return;
    var rows = JSON.parse(data.textContent), now = Date.now() + 7 * 3600e3, today = new Date(now).toISOString().slice(0, 10);
    var lim = new Date(now + 90 * 864e5).toISOString().slice(0, 10);
    var M = { en: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], th: ['ม.ค.', 'ก.พ.', 'มี.ค.', 'เม.ย.', 'พ.ค.', 'มิ.ย.', 'ก.ค.', 'ส.ค.', 'ก.ย.', 'ต.ค.', 'พ.ย.', 'ธ.ค.'],
      km: ['មករា', 'កុម្ភៈ', 'មីនា', 'មេសា', 'ឧសភា', 'មិថុនា', 'កក្កដា', 'សីហា', 'កញ្ញា', 'តុលា', 'វិច្ឆិកា', 'ធ្នូ'] }[LANG] || [];
    var shown = rows.filter(function (r) { return (r.end || r.start) >= today && r.start <= lim; });
    if (!shown.length) { box.innerHTML = '<p class="empty">' + W('cal_empty') + '</p>'; return; }
    box.innerHTML = shown.map(function (r) {
      var d = r.start < today ? today : r.start, m = +d.slice(5, 7) - 1, dd = +d.slice(8, 10);
      var span = r.end && r.end !== r.start ? ' – ' + (+r.end.slice(8, 10)) + ' ' + M[+r.end.slice(5, 7) - 1] : '';
      return '<div class="ev ' + (r.kind || '') + '"><div class="d" role="button" tabindex="0">' + dd + '<small>' + M[m] + '</small></div><div><b>' + r.t + '</b><span>' + r.w + span + '</span>' +
        (r.u ? '<a href="' + r.u + '" rel="noopener">' + r.s + '</a>' : '') + '</div></div>';
    }).join('');
    box.addEventListener('click', function (e) { var d = e.target.closest('.d'); if (d && !RM) d.animate([{ transform: 'rotate(0)' }, { transform: 'rotate(-12deg) scale(1.15)' }, { transform: 'rotate(8deg)' }, { transform: 'rotate(0)' }], { duration: 500 }); });
  }
  function bits() {
    document.querySelectorAll('.num').forEach(function (n) { n.addEventListener('click', function () { n.classList.remove('pop'); void n.offsetWidth; n.classList.add('pop'); }); });
    document.querySelectorAll('.face').forEach(function (f) { f.addEventListener('click', function () { if (!RM) f.animate([{ transform: 'rotate(0)' }, { transform: 'rotate(360deg) scale(1.2)' }, { transform: 'rotate(360deg)' }], { duration: 700, easing: 'ease-out' }); }); });
    var lb = document.getElementById('lb');
    if (lb && lb.showModal) document.addEventListener('click', function (e) {
      var im = e.target.closest('img[data-full]'); if (!im) return;
      lb.querySelector('img').src = im.getAttribute('data-full'); lb.querySelector('img').alt = im.alt; lb.querySelector('p').innerHTML = im.getAttribute('data-cap') || ''; lb.showModal();
    });
    if (lb) lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
  }
  function start() { rivers(); penh(); hands(); bowl(); calendar(); bits(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
