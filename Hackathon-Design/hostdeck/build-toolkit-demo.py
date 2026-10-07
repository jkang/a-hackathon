#!/usr/bin/env python3
"""Build a standalone, self-contained Toolkit demo HTML.

Reads the SCENES + logo from host-deck.html, base64-embeds the 18 screenshots
from assets/video/, and writes toolkit-demo.html — one shareable file.

Usage:  python3 build-toolkit-demo.py
"""
import base64
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "host-deck.html")
OUT = os.path.join(HERE, "toolkit-demo.html")
VID = os.path.join(HERE, "assets", "video")


def data_uri(path):
    with open(path, "rb") as f:
        return "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("ascii")


src = open(SRC, encoding="utf-8").read()

# logo data URI (reuse the deck's inline logo)
logo = re.search(r'class="logo"><img src="(data:image/[^"]+)"', src).group(1)

# SCENES array from the deck demo engine
scenes = re.search(r"var SCENES = \[.*?\n  \];", src, re.S).group(0)

# embed each referenced image
def repl(m):
    fn = m.group(1)
    return "'" + data_uri(os.path.join(VID, fn)) + "'"

scenes = re.sub(r"P\+'(img-[\w.-]+\.jpg)'", repl, scenes)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>The Marketing AI Toolkit — Demo</title>
<style>
  :root{
    --org:#FF6611; --org1:#FFF0E7; --org2:#FFD1B8; --org3:#FFA370;
    --ink:#0F1514; --mut:#4A5553; --org-ink:#B24000;
  }
  *{margin:0;padding:0;box-sizing:border-box;}
  html,body{width:100%;height:100%;}
  body{font-family:"Poppins","Noto Sans SC","PingFang SC","Microsoft YaHei",Arial,sans-serif;
       background:#202524;color:var(--ink);overflow:hidden;-webkit-font-smoothing:antialiased;}
  .stage{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;background:#202524;}
  .deck{width:1000px;height:562px;position:relative;background:var(--ink);overflow:hidden;flex:none;
        border-radius:16px;box-shadow:0 20px 60px rgba(0,0,0,.45);transform-origin:center center;}
  .logo{position:absolute;top:20px;right:32px;z-index:6;line-height:0;}
  .logo img{height:30px;width:30px;border-radius:8px;display:block;}

  /* demo player */
  .demo-stage{position:absolute;inset:0;background:var(--ink);overflow:hidden;color:#fff;cursor:pointer;}
  .dscene{position:absolute;inset:0;display:flex;opacity:0;transition:opacity .45s ease;pointer-events:none;}
  .dscene.on{opacity:1;pointer-events:auto;}
  .dcopy{width:38%;flex:none;display:flex;flex-direction:column;justify-content:center;z-index:2;
         padding:52px 32px 74px 52px;background:linear-gradient(155deg,#0F1514 0%,#182120 100%);
         border-right:1px solid rgba(255,255,255,.07);}
  .deyebrow{display:inline-flex;align-items:center;gap:9px;font-size:12px;font-weight:800;
            letter-spacing:.17em;text-transform:uppercase;color:var(--org3);}
  .deyebrow::before{content:"";width:22px;height:3px;background:var(--org);border-radius:2px;}
  .dhead{font-size:30px;font-weight:700;line-height:1.13;letter-spacing:-.01em;margin-top:14px;color:#fff;}
  .dsub{font-size:14.5px;line-height:1.55;color:#C7CFCD;margin-top:12px;}
  .dchips{display:flex;flex-wrap:wrap;gap:7px;margin-top:18px;}
  .dchip{font-size:11.5px;font-weight:600;background:rgba(255,102,17,.16);
         border:1px solid rgba(255,102,17,.4);color:var(--org3);border-radius:999px;padding:4px 11px;}
  .dfig{flex:1;display:flex;align-items:center;justify-content:center;overflow:hidden;
        padding:46px 46px 46px 28px;background:radial-gradient(125% 125% at 78% 8%,#232c2b 0%,#0F1514 72%);}
  .dframe{width:100%;aspect-ratio:2520 / 1596;background:#fff;border-radius:11px;overflow:hidden;
          box-shadow:0 18px 50px rgba(0,0,0,.55);display:flex;}
  .dframe img{width:100%;height:100%;object-fit:contain;display:block;}
  .dmissing{display:flex;align-items:center;justify-content:center;width:70%;height:60%;
            border:2px dashed rgba(255,102,17,.5);border-radius:12px;color:var(--org3);
            font-size:14px;font-weight:700;letter-spacing:.08em;}
  .dscene.on .dfig img{animation:dzoom 12s ease-out both;}
  .dscene.on .dcopy{animation:dIn .5s ease both;}
  .dtop{position:absolute;top:24px;left:52px;right:96px;display:flex;align-items:center;gap:12px;
        z-index:6;pointer-events:none;}
  .dcount{font-size:12px;font-weight:700;letter-spacing:.1em;color:var(--org3);font-variant-numeric:tabular-nums;}
  .dcontrols{position:absolute;right:32px;bottom:20px;display:flex;align-items:center;gap:8px;z-index:8;cursor:default;}
  .dbtn{appearance:none;border:1.5px solid rgba(255,255,255,.22);background:rgba(255,255,255,.06);
        color:#fff;font:inherit;font-size:13px;font-weight:700;line-height:1;border-radius:9px;
        padding:8px 11px;cursor:pointer;transition:.15s;}
  .dbtn:hover{background:rgba(255,255,255,.14);border-color:rgba(255,255,255,.4);}
  .dbtn.wide{min-width:66px;}
  .dhint{position:absolute;left:52px;bottom:22px;z-index:8;font-size:11.5px;font-weight:600;
         letter-spacing:.04em;color:#8A9492;}
  .dhint b{color:#C7CFCD;font-weight:700;}
  .dbar{position:absolute;left:0;right:0;bottom:0;height:3px;background:rgba(255,255,255,.14);z-index:8;}
  .dbar i{display:block;height:100%;width:0;background:var(--org);}
  @keyframes dzoom{from{transform:scale(1);}to{transform:scale(1.05);}}
  @keyframes dIn{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:none;}}
</style>
</head>
<body>
<div class="stage">
  <div class="deck" id="deck">
    <div class="demo-stage" id="toolkitDemo" aria-label="Toolkit demo"></div>
    <div class="logo"><img src="__LOGO__" alt="Ascentium"></div>
  </div>
</div>

<script>
__SCENES__

(function(){
  var stage = document.getElementById('toolkitDemo');
  var deck  = document.getElementById('deck');
  var total = SCENES.reduce(function(a,s){ return a + s.dur; }, 0);

  function copyHTML(s){
    var chips = (s.skills && s.skills.length)
      ? '<div class="dchips">' + s.skills.map(function(k){ return '<span class="dchip">' + k + '</span>'; }).join('') + '</div>'
      : '';
    return '<div class="deyebrow">' + (s.eyebrow || '') + '</div>' +
           '<h3 class="dhead">' + s.head + '</h3>' +
           '<p class="dsub">' + s.sub + '</p>' + chips;
  }
  var els = SCENES.map(function(s){
    var el = document.createElement('div');
    el.className = 'dscene';
    el.innerHTML = '<div class="dcopy">' + copyHTML(s) + '</div><div class="dfig"><div class="dframe"><img src="' + s.img + '" alt="' + (s.alt || '') + '"></div></div>';
    var im = el.querySelector('img');
    if(im){ im.addEventListener('error', function(){ var b = document.createElement('div'); b.className='dmissing'; b.textContent=s.id; im.replaceWith(b); }); }
    stage.appendChild(el);
    return el;
  });

  var chrome = document.createElement('div');
  chrome.innerHTML =
    '<div class="dtop"><span class="dcount"></span></div>' +
    '<div class="dcontrols">' +
      '<button class="dbtn" data-d="restart" title="Restart">&#8635;</button>' +
      '<button class="dbtn" data-d="prev" title="Previous">&#8249;</button>' +
      '<button class="dbtn wide" data-d="play" title="Play / Pause">Pause</button>' +
      '<button class="dbtn" data-d="next" title="Next">&#8250;</button>' +
    '</div>' +
    '<div class="dhint"><b>&#8592;</b> <b>&#8594;</b> navigate &nbsp;·&nbsp; <b>Space</b> play/pause &nbsp;·&nbsp; <b>R</b> restart &nbsp;·&nbsp; <b>F</b> fullscreen</div>' +
    '<div class="dbar"><i></i></div>';
  stage.appendChild(chrome);
  var countEl = chrome.querySelector('.dcount');
  var barEl   = chrome.querySelector('.dbar i');
  var playBtn = chrome.querySelector('[data-d="play"]');

  var idx = 0, playing = false, elapsed = 0, raf = null, last = 0;
  function pad(n){ return (n < 10 ? '0' : '') + n; }
  function beforeDur(){ var t = 0; for(var k = 0; k < idx; k++) t += SCENES[k].dur; return t; }
  function render(){
    var overall = (beforeDur() + Math.min(elapsed, SCENES[idx].dur)) / total;
    barEl.style.width = (overall * 100) + '%';
  }
  function setScene(n, atStart){
    idx = ((n % SCENES.length) + SCENES.length) % SCENES.length;
    if(atStart !== false) elapsed = 0;
    els.forEach(function(e,k){ e.classList.toggle('on', k === idx); });
    countEl.textContent = pad(idx + 1) + ' / ' + pad(SCENES.length);
    render();
  }
  function play(){
    if(playing) return;
    playing = true; playBtn.textContent = 'Pause';
    last = (window.performance && performance.now) ? performance.now() : Date.now();
    raf = requestAnimationFrame(function step(now){
      if(!playing) return;
      var dt = (now - last) / 1000; last = now;
      elapsed += dt;
      if(elapsed >= SCENES[idx].dur){
        if(idx < SCENES.length - 1){ setScene(idx + 1, true); }
        else { elapsed = SCENES[idx].dur; render(); pause(); return; }
      }
      render();
      raf = requestAnimationFrame(step);
    });
  }
  function pause(){ playing = false; playBtn.textContent = 'Play'; if(raf) cancelAnimationFrame(raf); raf = null; }
  function toggle(){ playing ? pause() : play(); }
  function restart(){ setScene(0, true); play(); }

  chrome.addEventListener('click', function(e){
    var b = e.target.closest('[data-d]'); if(!b) return;
    var a = b.getAttribute('data-d');
    if(a === 'play') toggle();
    else if(a === 'prev') setScene(idx - 1, true);
    else if(a === 'next') setScene(idx + 1, true);
    else if(a === 'restart') restart();
  });
  stage.addEventListener('click', function(e){ if(e.target.closest('.dcontrols')) return; toggle(); });

  document.addEventListener('keydown', function(e){
    if(e.key === ' ' || e.code === 'Space'){ e.preventDefault(); toggle(); }
    else if(e.key === 'ArrowRight'){ e.preventDefault(); setScene(idx + 1, true); }
    else if(e.key === 'ArrowLeft'){ e.preventDefault(); setScene(idx - 1, true); }
    else if(e.key === 'r' || e.key === 'R'){ restart(); }
    else if(e.key === 'f' || e.key === 'F'){
      if(!document.fullscreenElement){ if(document.documentElement.requestFullscreen) document.documentElement.requestFullscreen(); }
      else { if(document.exitFullscreen) document.exitFullscreen(); }
    }
  });

  function fit(){
    var s = Math.min(window.innerWidth/1000, window.innerHeight/562);
    deck.style.transform = 'scale(' + s + ')';
  }
  window.addEventListener('resize', fit);

  fit();
  setScene(0, true);
  play();
})();
</script>
</body>
</html>
"""

out = HTML.replace("__LOGO__", logo).replace("__SCENES__", scenes)
open(OUT, "w", encoding="utf-8").write(out)
print("wrote", OUT, "({:.1f} MB)".format(os.path.getsize(OUT) / 1e6))
