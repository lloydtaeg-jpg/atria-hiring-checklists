#!/usr/bin/env python3
"""Build an Atria staff training module from a content spec.

The engine (navigation, section rendering, quiz grading, certificate with
email/print/download) is shared with Care by the Book and Move Safe and lives
in tools/modules/. Each module supplies its own content and accent colour.

    python3 tools/build_module.py tools/modules/whmis.py

Writes training/<slug>/index.html.
"""
import io, json, os, re, sys, urllib.parse, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODS = os.path.join(ROOT, "tools", "modules")


def favicon(glyph, colour):
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
           '<rect width="32" height="32" rx="7" fill="%s"/>'
           '<g fill="none" stroke="#FAF8F2" stroke-width="2.1" stroke-linecap="round" '
           'stroke-linejoin="round">%s</g></svg>') % (colour, glyph)
    return "data:image/svg+xml," + urllib.parse.quote(svg, safe="")


def build(spec):
    base = io.open(os.path.join(MODS, "base.css"), encoding="utf-8").read()
    engine = io.open(os.path.join(MODS, "engine.js"), encoding="utf-8").read()
    logo = "data:image/png;base64," + io.open(
        os.path.join(ROOT, "tools", "atria-logo.b64"), encoding="utf-8").read().strip()

    sections = "const SECTIONS = " + json.dumps(spec.SECTIONS, ensure_ascii=False, indent=1) + ";"
    quiz = "QUIZQ = " + json.dumps(spec.QUIZQ, ensure_ascii=False, indent=1) + ";"
    js = (engine.replace("__SECTIONS__", sections).replace("__QUIZQ__", quiz)
                .replace('const MODULE_VERSION = "1.2";', 'const MODULE_VERSION = "%s";' % spec.VERSION)
                .replace("const PASS_MARK = 52;", "const PASS_MARK = %d;" % spec.PASS_MARK))

    identity = '''
/* ===== Module identity: shared Atria system, one accent per module ===== */
:root{ --module:%(light)s; --module-on:#FAF8F2;
  --brand:%(light)s; --brand-2:%(mid)s; --brand-ink:%(ink)s; }
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --module:%(dark)s; --brand:%(darkbg)s; --brand-2:%(light)s; --brand-ink:%(dark)s; } }
:root[data-theme="dark"]{
  --module:%(dark)s; --brand:%(darkbg)s; --brand-2:%(light)s; --brand-ink:%(dark)s; }
.brandbar{ background:var(--module); color:var(--module-on); }
.brandbar .brand{ font-size:.95rem; font-weight:600; letter-spacing:.14em;
  text-transform:uppercase; opacity:.82; }
.brandbar .tagline{ font-size:.7rem; letter-spacing:.12em; text-transform:uppercase; opacity:.62; }
.brandbar h1{ font-size:clamp(2.1rem,7vw,3.1rem); font-weight:700; line-height:1.04;
  letter-spacing:-.015em; margin:.55rem 0 0; text-wrap:balance; }
.brandbar p{ font-size:.95rem; opacity:.9; margin-top:.5rem; }
.brandbar .logo-mark{ width:56px; height:56px; }
@media(min-width:700px){ .brandbar .logo-mark{ width:62px; height:62px; } }
.meta-bar .field b{ color:var(--module); }
.stops span.now{ background:var(--module); }
.stops span.done{ background:color-mix(in srgb, var(--module) 45%%, transparent); }
.eyebrow, h3.section, .idx-sec{ color:var(--module); }
''' % spec.COLOUR

    toc_note = ('<p class="hint" style="margin:12px 0 0">%s</p>' % spec.TOC_NOTE) if spec.TOC_NOTE else ""

    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%(title)s</title>
<link rel="icon" href="%(favicon)s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>%(base)s</style>
<style>%(identity)s</style>
</head>
<body>

<header class="brandbar">
  <div class="brandbar-in">
    <div class="logo-mark"><img src="%(logo)s" alt="Atria Private Care logo"></div>
    <div class="brand">Atria</div>
    <div class="tagline">Private Care</div>
    <h1>%(title)s</h1>
    <p>%(subtitle)s</p>
  </div>
</header>
<div class="meta-bar"><div class="meta-bar-in">
  <div class="field"><b>Covers:</b>%(covers)s</div>
  <div class="field"><b>Time:</b>%(time)s</div>
  <div class="field"><b>Pass mark:</b>%(pass)d of %(total)d</div>
</div></div>
<div class="route" id="route" aria-hidden="true">
  <div class="route-in">
    <div class="route-top"><strong id="stepName">Welcome</strong><span id="stepCount"></span></div>
    <div class="stops" id="stops"></div>
  </div>
</div>
<main class="wrap" id="main">
<section class="step on" data-name="Welcome">
  <div class="intro" style="margin-top:22px">%(intro)s</div>
  <div class="panel stack">
    <div>
      <label class="field" for="staffName">Your full name</label>
      <input type="text" id="staffName" autocomplete="name" placeholder="As it should appear on your certificate">
    </div>
    <p class="hint">The check has %(total)d questions and you need %(pass)d to pass. You can retake it as many times as you need.</p>
    <div id="priorRecord" class="note hidden"></div>
    <button class="btn" id="startBtn" disabled>Start the module</button>
  </div>
  <div class="panel" style="margin-top:24px">
    <h3>What's covered</h3>
    <ol class="toc" id="toc"></ol>
    %(tocnote)s
  </div>
  <div id="adminPanel" class="panel hidden" style="margin-top:24px">
    <h3>Staff completions</h3>
    <div id="records"></div>
  </div>
</section>
<div id="sections"></div>
<section class="step" data-name="The check" id="quizStep">
  <p class="eyebrow">Final check</p>
  <h2>%(total)d questions</h2>
  <p>%(pass)d correct to pass. Pick the best answer for each one.</p>
  <div id="quiz"></div>
  <button class="btn" id="gradeBtn" style="width:100%%;margin-top:18px">Submit the check</button>
  <div id="result"></div>
</section>
</main>
<nav class="navbar no-print">
  <div class="navbar-in">
    <button class="btn ghost" id="backBtn">Back</button>
    <button class="btn" id="nextBtn">Next</button>
  </div>
</nav>
<script>%(js)s</script>
</body>
</html>
''' % dict(title=spec.TITLE, subtitle=spec.SUBTITLE, covers=spec.COVERS, time=spec.TIME,
           intro=spec.INTRO, tocnote=toc_note, base=base, identity=identity, js=js, logo=logo,
           favicon=favicon(spec.GLYPH, spec.COLOUR["light"]),
           pass_=spec.PASS_MARK, total=len(spec.QUIZQ), **{"pass": spec.PASS_MARK})


def main():
    path = sys.argv[1]
    name = os.path.splitext(os.path.basename(path))[0]
    sp = importlib.util.spec_from_file_location(name, path)
    spec = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(spec)

    out_dir = os.path.join(ROOT, "training", spec.SLUG)
    os.makedirs(out_dir, exist_ok=True)
    html = build(spec)
    io.open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8").write(html)
    print("training/%s/index.html: %d sections, %d questions, pass %d, %d bytes"
          % (spec.SLUG, len(spec.SECTIONS), len(spec.QUIZQ), spec.PASS_MARK, len(html)))


if __name__ == "__main__":
    main()
