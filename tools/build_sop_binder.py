#!/usr/bin/env python3
"""Rebuild sop-binder.html from the Atria SOP Binder Claude Doc.

Input:  the XML chunks of a Claude Docs `read` of the binder, saved as
        tools/doc-cache/01.xml, 02.xml, ... (one file per read, in the order
        the reads were made -- see .claude/skills/update-sop-binder/SKILL.md).
Output: sop-binder.html in the repo root.

Run:    python3 tools/build_sop_binder.py
"""
import xml.etree.ElementTree as ET
import re, html, json, sys, glob, os, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, "tools", "doc-cache")
OVERRIDES = os.path.join(ROOT, "tools", "sop-overrides")
LOGO_FILE = os.path.join(ROOT, "tools", "atria-logo.b64")
OUT = os.path.join(ROOT, "sop-binder.html")


# --------------------------------------------------------------- ids ----
def expand_ids(xml: str) -> str:
    """Block ids print full once per session prefix, then short ('.90').

    Expand every short id using the most recent full id above it, so ids stay
    unique and stable even after the doc is edited (edits add new prefixes).
    """
    state = {"prefix": None}

    def fix(m):
        attr, val = m.group(1), m.group(2)
        if val.startswith("."):
            if state["prefix"]:
                val = state["prefix"] + val
        elif "." in val:
            state["prefix"] = val.split(".", 1)[0]
        return "%s='%s'" % (attr, val)

    xml = re.sub(r"\b(id|from|parent)='([^']*)'", fix, xml)

    def fix_href(m):
        val = m.group(1)
        if val.startswith("#.") and state["prefix"]:
            val = "#" + state["prefix"] + val[1:]
        return "href='%s'" % val

    return re.sub(r"href='([^']*)'", fix_href, xml)


def anchor(i):
    return "b-" + (i or "").replace(".", "-")


# ------------------------------------------------------------- merge ----
def load_chunks():
    files = sorted(glob.glob(os.path.join(CACHE, "*.xml")))
    if not files:
        sys.exit("No doc chunks in tools/doc-cache/ -- see the update-sop-binder skill.")
    roots = []
    for f in files:
        raw = open(f, encoding="utf-8").read().strip()
        # accept either a raw <doc> or the whole JSON reply with a .data.xml
        if raw.startswith("{"):
            raw = json.loads(raw)["data"]["xml"]
        roots.append((f, ET.fromstring(expand_ids(raw))))
    return roots


def merge(roots):
    """Splice the chunks into one ordered block list, filling <gap/>s."""
    blocks, by_id = [], {}

    def add(el):
        blocks.append(el)
        if el.get("id"):
            by_id[el.get("id")] = el

    for fname, root in roots:
        parent = root.get("parent")
        if parent:
            # this chunk supplies the children of an earlier, truncated block
            target = by_id.get(parent)
            if target is None:
                sys.exit("chunk %s continues unknown block %s" % (fname, parent))
            src = root.find("*")  # the re-sent block itself
            if src is None:
                continue
            kept = [c for c in target if c.tag != "gap"]
            new = [c for c in src if c.tag != "gap"]
            seen = {c.get("id") for c in kept}
            for c in new:
                if c.get("id") not in seen:
                    kept.append(c)
            for c in list(target):
                target.remove(c)
            for c in kept:
                target.append(c)
        else:
            for el in root:
                if el.tag == "gap":
                    continue
                add(el)

    leftover = sum(len(b.findall(".//gap")) for b in blocks)
    if leftover:
        print("warning: %d unfilled gap(s) -- a read was not continued to the end"
              % leftover, file=sys.stderr)
    return blocks


# ------------------------------------------------------------ inline ----
def inline(el):
    out = []
    if el.text:
        out.append(html.escape(el.text))
    for ch in el:
        if ch.tag == "text":
            out.append(inline(ch))
        elif ch.tag == "bold":
            out.append("<strong>%s</strong>" % inline(ch))
        elif ch.tag == "italic":
            out.append("<em>%s</em>" % inline(ch))
        elif ch.tag == "link":
            href = ch.get("href", "")
            if href.startswith("#"):
                href = "#" + anchor(href[1:])
            out.append('<a href="%s">%s</a>' % (html.escape(href), inline(ch)))
        elif ch.tag == "date":
            out.append(html.escape(ch.get("value", "")))
        elif ch.tag == "mention":
            out.append(html.escape(ch.get("label", "")))
        elif ch.tag == "comment":
            pass
        else:
            out.append(inline(ch))
        if ch.tail:
            out.append(html.escape(ch.tail))
    return "".join(out)


def plain(el):
    return re.sub(r"<[^>]+>", "", inline(el))


def strip_tags(h):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h)).strip()


def render_table(t):
    rows = [r for r in t if r.tag == "row"]
    if not rows:
        return ""
    head = all(c.get("header") == "true" for c in rows[0] if c.tag == "cell")
    out = ['<div class="tablewrap"><table>']
    for n, r in enumerate(rows):
        tag = "th" if (n == 0 and head) else "td"
        if n == 0 and head:
            out.append("<thead>")
        out.append("<tr>")
        for c in [c for c in r if c.tag == "cell"]:
            body = " ".join(inline(p) for p in c if p.tag == "paragraph")
            out.append("<%s>%s</%s>" % (tag, body, tag))
        out.append("</tr>")
        if n == 0 and head:
            out.append("</thead><tbody>")
    out.append("</tbody></table></div>")
    return "".join(out)


def render_list(l):
    tag = "ol" if l.get("kind") == "ordered" else "ul"
    out = ["<%s>" % tag]
    for li in l:
        if li.tag != "listItem":
            continue
        body = "".join(inline(p) for p in li if p.tag == "paragraph")
        nested = "".join(render_list(x) for x in li if x.tag == "list")
        out.append("<li>%s%s</li>" % (body, nested))
    out.append("</%s>" % tag)
    return "".join(out)


def style_fragments(frags):
    """A paragraph that is entirely bold is a sub-heading, not body text."""
    out = []
    for f in frags:
        if re.match(r"^<p><strong>[^<]+</strong></p>$", f):
            t = strip_tags(f)
            out.append('<p class="%s">%s</p>' % ("lbl" if len(t) <= 25 else "sublbl", t))
        elif f.startswith("<p><strong>Documentation:</strong>"):
            out.append('<p class="doc-note">%s</p>' % f[3:-4])
        else:
            out.append(f)
    return "".join(out)


def load_overrides():
    """Local replacements for individual SOPs, merged over what the doc says.

    tools/sop-overrides/<number>.html holds the body of one SOP exactly as the
    builder emits it: paragraphs, .lbl/.sublbl labels, .tablewrap tables, lists
    and a .doc-note. An optional leading "<!-- title: ... -->" comment renames
    the SOP.

    These exist only because the binder's Claude Doc could not be edited at the
    time. Each one is a divergence from the doc: fold it back into the doc and
    delete the file once the Docs connector is available.
    """
    out = {}
    if not os.path.isdir(OVERRIDES):
        return out
    for f in sorted(glob.glob(os.path.join(OVERRIDES, "*.html"))):
        num = os.path.splitext(os.path.basename(f))[0]
        body = open(f, encoding="utf-8").read()
        t = re.search(r"<!--\s*title:\s*(.+?)\s*-->", body)
        body = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()
        out[num] = {"title": t.group(1) if t else None, "html": body}
    return out


# ------------------------------------------------------------- parse ----
SOP_RE = re.compile(r"^SOP\s+([0-9]+[A-Z]?)\s*:\s*(.+)$")


def parse(blocks):
    # the doc's own index tables are the authority on which section a SOP is in
    index_section = {}
    for el in blocks:
        if el.tag != "table":
            continue
        rows = [r for r in el if r.tag == "row"]
        if not rows:
            continue
        hdr = [plain(c).strip() for c in rows[0] if c.tag == "cell"]
        if hdr[:3] != ["No.", "SOP", "Section"]:
            continue
        for r in rows[1:]:
            cells = [c for c in r if c.tag == "cell"]
            if len(cells) >= 3 and plain(cells[0]).strip():
                index_section[plain(cells[0]).strip()] = plain(cells[2]).strip()

    front, body = [], []
    cur_sop = None
    seen_part = False
    cur_section = ""

    def flush():
        nonlocal cur_sop
        if cur_sop:
            body.append(cur_sop)
            cur_sop = None

    for el in blocks:
        h = el.get("heading") if el.tag == "paragraph" else None
        txt = plain(el) if el.tag == "paragraph" else ""

        if h == "1" and txt.startswith("Part "):
            flush(); seen_part = True
            body.append({"kind": "part", "id": anchor(el.get("id")), "text": txt})
            continue
        if h == "2" and txt.startswith("Section "):
            flush()
            cur_section = txt.split(":", 1)[1].strip() if ":" in txt else txt
            body.append({"kind": "section", "id": anchor(el.get("id")), "text": txt})
            continue
        # SOP headings sit at level 2 or 3 in the source -- accept both
        if h in ("2", "3"):
            m = SOP_RE.match(txt)
            if m:
                flush()
                num = m.group(1)
                want = index_section.get(num)
                if want and want.lower() not in cur_section.lower():
                    body.append({"kind": "section", "from_index": True, "text": want,
                                 "id": "sec-" + re.sub(r"[^a-z0-9]+", "-", want.lower()).strip("-")})
                    cur_section = want
                cur_sop = {"kind": "sop", "id": anchor(el.get("id")),
                           "num": num, "title": m.group(2), "html": []}
                continue

        if el.tag == "paragraph":
            frag = ('<h4 id="%s">%s</h4>' % (anchor(el.get("id")), inline(el))) if h \
                else ("<p>%s</p>" % inline(el))
        elif el.tag == "table":
            frag = render_table(el)
        elif el.tag == "list":
            frag = render_list(el)
        else:
            continue

        if cur_sop is not None:
            cur_sop["html"].append(frag)
        elif not seen_part:
            front.append(frag)
        else:
            body.append({"kind": "raw", "html": frag})
    flush()
    return front, body


# ------------------------------------------------------------ render ----
def build_index(body):
    parts, pending = [], False
    for b in body:
        if b["kind"] == "part":
            if pending:
                parts.append("</ul>"); pending = False
            if parts:
                parts.append("</div>")
            parts.append('<div class="idx-part"><h3>%s</h3>' % html.escape(b["text"]))
        elif b["kind"] == "section":
            if pending:
                parts.append("</ul>")
            parts.append('<p class="idx-sec">%s</p><ul class="idx-list">' % html.escape(b["text"]))
            pending = True
        elif b["kind"] == "sop":
            parts.append('<li><a href="#%s"><span class="idx-num">%s</span><span>%s</span></a></li>'
                         % (b["id"], html.escape(b["num"]), html.escape(b["title"])))
    if pending:
        parts.append("</ul>")
    if parts:
        parts.append("</div>")
    return "".join(parts)


def build_body(body):
    out, open_sec = [], False
    for b in body:
        if b["kind"] == "part":
            if open_sec:
                out.append("</div>"); open_sec = False
            out.append('<h2 class="part" id="%s">%s</h2>' % (b["id"], html.escape(b["text"])))
        elif b["kind"] == "section":
            if open_sec:
                out.append("</div>")
            out.append('<div class="secgroup"><h3 class="section" id="%s">%s</h3>'
                       % (b["id"], html.escape(b["text"])))
            open_sec = True
        elif b["kind"] == "raw":
            out.append('<div class="partlede">%s</div>' % b["html"])
        elif b["kind"] == "sop":
            hay = html.escape("sop %s %s %s" % (b["num"], b["title"],
                                                strip_tags("".join(b["html"]))), quote=True).lower()
            out.append(
                '<article class="sop" id="%s" data-s="%s">'
                '<header class="sop-head"><span class="sop-num">SOP %s</span><h4>%s</h4></header>'
                '%s<a class="totop" href="#top">Back to index &uarr;</a></article>'
                % (b["id"], hay, html.escape(b["num"]), html.escape(b["title"]),
                   style_fragments(b["html"])))
    if open_sec:
        out.append("</div>")
    return "".join(out)


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>SOP Binder</title>
<!-- Generated by tools/build_sop_binder.py from the Atria SOP Binder Claude Doc.
     Do not edit this file by hand: edit the doc, then rebuild. -->
<link rel="icon" href="__FAVICON__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:wght@400;500;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg:#f7f3eb; --card:#fff; --ink:#2f2a24; --ink-strong:#201b16;
    --muted:#6f675d; --faint:#a49a8b; --accent:#8b7155; --accent-dk:#7a6249;
    --line:rgba(47,42,36,.12); --soft:#faf7f0;
    color:var(--ink); background:var(--bg);
    font-family:'Inter', system-ui, -apple-system, sans-serif;
  }
  h1, h2.part, .sop h4, .idx-part h3, .wm-name, .cert .who{
    font-family:'Lora', Georgia, 'Times New Roman', serif;
  }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--bg); padding:0 0 64px; -webkit-text-size-adjust:100%; }
  .wrap { max-width:820px; margin:0 auto; padding:0 18px; }
  .topbar { position:sticky; top:0; z-index:20; background:rgba(247,243,235,.94);
    backdrop-filter:saturate(140%) blur(8px); border-bottom:1px solid var(--line); }
  .topbar-in { max-width:820px; margin:0 auto; padding:10px 18px;
    display:flex; align-items:center; gap:12px; flex-wrap:wrap; }
  .wm { display:flex; align-items:center; gap:9px; min-width:0; }
  .wm-logo { width:34px; height:34px; flex:none; border-radius:50%; overflow:hidden;
    background:var(--soft); border:2px solid rgba(139,113,85,.22);
    display:flex; align-items:center; justify-content:center; }
  .wm-logo img { width:130%; height:130%; object-fit:contain; }
  .wm-name { font-size:1rem; font-weight:700; color:var(--accent);
    letter-spacing:.2px; white-space:nowrap; }
  @media (max-width:560px){ .wm-name { display:none; } }
  .search { flex:1 1 200px; min-width:0; }
  .search input { width:100%; font:inherit; font-size:.88rem; padding:9px 12px;
    border:1px solid var(--line); border-radius:10px; background:#fff; color:var(--ink); }
  .search input:focus { outline:2px solid var(--accent); outline-offset:-1px; border-color:var(--accent); }
  .back { font-size:.8rem; text-decoration:none; color:var(--accent); font-weight:600; white-space:nowrap; }
  .back:hover { text-decoration:underline; }
  .card { background:var(--card); border:1px solid var(--line); border-radius:20px;
    box-shadow:0 16px 44px rgba(47,42,36,.09); padding:30px 30px 26px; margin-top:22px; }
  .eyebrow { font-size:10px; text-transform:uppercase; letter-spacing:.28em;
    color:var(--accent); margin:0 0 10px; font-weight:700; }
  h1 { font-size:1.7rem; line-height:1.15; color:var(--ink-strong); margin:0 0 10px; }
  .lede { color:var(--muted); font-size:.92rem; margin:0; line-height:1.6; }
  .meta { display:flex; flex-wrap:wrap; gap:8px; margin-top:16px; }
  .chip { font-size:11px; letter-spacing:.04em; background:var(--soft); border:1px solid var(--line);
    border-radius:999px; padding:5px 11px; color:var(--muted); }
  h2.part { font-size:1.15rem; color:var(--ink-strong); margin:40px 0 0;
    padding:0 0 10px; border-bottom:2px solid var(--accent); letter-spacing:.01em; }
  .partlede p { color:var(--muted); font-size:.88rem; margin:12px 0 0; }
  h3.section { font-size:.72rem; text-transform:uppercase; letter-spacing:.16em;
    color:var(--accent); margin:30px 0 0; font-weight:700; }
  .sop { background:var(--card); border:1px solid var(--line); border-left:4px solid var(--accent);
    border-radius:12px; padding:22px 24px 18px; margin-top:14px; }
  .sop-head { display:flex; align-items:baseline; gap:12px; flex-wrap:wrap; margin-bottom:10px; }
  .sop-num { font-size:10px; font-weight:700; letter-spacing:.14em; text-transform:uppercase;
    background:var(--accent); color:#fff; border-radius:6px; padding:4px 9px; white-space:nowrap; }
  .sop h4 { font-size:1.05rem; color:var(--ink-strong); margin:0; line-height:1.25; }
  .sop > p { font-size:.92rem; line-height:1.6; margin:10px 0; }
  .lbl { font-size:10px !important; text-transform:uppercase; letter-spacing:.16em;
    color:var(--accent); font-weight:700; margin:20px 0 6px !important; }
  .sublbl { font-size:.93rem !important; font-weight:700; color:var(--accent-dk);
    margin:22px 0 6px !important; line-height:1.4; }
  .doc-note { background:var(--soft); border:1px solid var(--line); border-radius:9px;
    padding:11px 14px; font-size:.86rem !important; color:var(--muted); margin-top:16px !important; }
  .doc-note strong { color:var(--ink-strong); }
  .sop ul, .sop ol { margin:8px 0; padding-left:22px; }
  .sop li { font-size:.92rem; line-height:1.6; margin:7px 0; }
  .sop li::marker { color:var(--accent); font-weight:700; }
  .totop { display:inline-block; margin-top:16px; font-size:11px; color:var(--faint);
    text-decoration:none; letter-spacing:.04em; }
  .totop:hover { color:var(--accent); }
  .tablewrap { overflow-x:auto; margin:12px 0; border:1px solid var(--line); border-radius:10px; }
  table { border-collapse:collapse; width:100%; font-size:.86rem; min-width:420px; }
  th, td { text-align:left; padding:9px 12px; border-bottom:1px solid var(--line); vertical-align:top; line-height:1.5; }
  th { background:var(--soft); font-size:10px; text-transform:uppercase;
    letter-spacing:.12em; color:var(--accent); font-weight:700; }
  tbody tr:last-child td { border-bottom:0; }
  td:first-child { font-weight:600; color:var(--ink-strong); white-space:nowrap; }
  table a { color:var(--accent); font-weight:600; }
  .idx-part { margin-top:20px; }
  .idx-part h3 { font-size:.95rem; color:var(--ink-strong); margin:0 0 4px; }
  .idx-sec { font-size:10px; text-transform:uppercase; letter-spacing:.16em;
    color:var(--accent); font-weight:700; margin:16px 0 6px; }
  .idx-list { list-style:none; margin:0; padding:0; }
  .idx-list li { margin:0 0 4px; }
  .idx-list a { display:flex; gap:10px; align-items:baseline; text-decoration:none;
    color:var(--ink); font-size:.88rem; padding:5px 8px; border-radius:7px; }
  .idx-list a:hover { background:var(--soft); color:var(--accent-dk); }
  .idx-num { font-size:10px; font-weight:700; color:var(--accent); min-width:26px; letter-spacing:.04em; }
  .noresults { display:none; color:var(--muted); font-size:.9rem; padding:20px 2px; }
  .foot { margin-top:30px; font-size:11px; color:var(--faint); letter-spacing:.03em; text-align:center; }
  .hidden { display:none !important; }
  @media (max-width:520px) {
    .card { padding:22px 18px 18px; border-radius:16px; }
    .sop { padding:18px 16px 14px; }
    h1 { font-size:1.4rem; }
    td:first-child { white-space:normal; }
  }
  @media print {
    .topbar, .totop, .noresults { display:none !important; }
    body { background:#fff; padding:0; }
    .card, .sop { box-shadow:none; break-inside:avoid; page-break-inside:avoid; }
    .sop { border:1px solid #ccc; }
    h2.part { break-before:page; page-break-before:always; }
  }
</style>
</head>
<body>
<a id="top"></a>
<div class="topbar">
  <div class="topbar-in">
    <div class="wm"><span class="wm-logo"><img src="__LOGO__" alt="Atria Private Care logo"></span><span class="wm-name">Atria Private Care</span></div>
    <div class="search">
      <input id="q" type="search" placeholder="Search the binder — e.g. falls, hand hygiene, 911"
             aria-label="Search the SOP binder" autocomplete="off" />
    </div>
    <a class="back" href="index.html">All documents</a>
  </div>
</div>
<div class="wrap">
  <div class="card">
    <p class="eyebrow">Administration Documents</p>
    <h1>__TITLE__</h1>
    <p class="lede">__LEDE__</p>
    <div class="meta">__CHIPS__</div>
  </div>
  <div class="card" id="about">
    <p class="eyebrow">About this binder</p>
    __ABOUT__
  </div>
  <div class="card" id="index">
    <p class="eyebrow">Index</p>
    __INDEX__
  </div>
  <div id="content">__BODY__</div>
  <p class="noresults" id="noresults">No SOPs match that search.</p>
  <div class="foot">Atria Private Care — Internal reference. Where an SOP and a client's care plan differ,
  follow the care plan and tell the RN. Where an SOP and the law differ, the law wins.</div>
</div>
<script>
(function () {
  var q = document.getElementById('q');
  var sops = Array.prototype.slice.call(document.querySelectorAll('.sop'));
  var groups = Array.prototype.slice.call(document.querySelectorAll('.secgroup'));
  var parts = Array.prototype.slice.call(document.querySelectorAll('h2.part, .partlede'));
  var idxCard = document.getElementById('index');
  var aboutCard = document.getElementById('about');
  var none = document.getElementById('noresults');
  function apply() {
    var t = q.value.trim().toLowerCase();
    if (!t) {
      sops.forEach(function (s) { s.classList.remove('hidden'); });
      groups.forEach(function (g) { g.classList.remove('hidden'); });
      parts.forEach(function (p) { p.classList.remove('hidden'); });
      idxCard.classList.remove('hidden');
      aboutCard.classList.remove('hidden');
      none.style.display = 'none';
      return;
    }
    var words = t.split(/\s+/);
    var hits = 0;
    sops.forEach(function (s) {
      var hay = s.getAttribute('data-s') || '';
      var ok = words.every(function (w) { return hay.indexOf(w) !== -1; });
      s.classList.toggle('hidden', !ok);
      if (ok) hits++;
    });
    groups.forEach(function (g) { g.classList.toggle('hidden', !g.querySelector('.sop:not(.hidden)')); });
    parts.forEach(function (p) { p.classList.add('hidden'); });
    idxCard.classList.add('hidden');
    aboutCard.classList.add('hidden');
    none.style.display = hits ? 'none' : 'block';
  }
  q.addEventListener('input', apply);
  q.addEventListener('keydown', function (e) { if (e.key === 'Escape') { q.value = ''; apply(); } });
})();
</script>
</body>
</html>
"""

MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def main():
    blocks = merge(load_chunks())
    front, body = parse(blocks)

    overrides = load_overrides()
    applied = []
    for b in body:
        if b["kind"] == "sop" and b["num"] in overrides:
            ov = overrides[b["num"]]
            b["html"] = [ov["html"]]
            if ov["title"]:
                b["title"] = ov["title"]
            applied.append(b["num"])
    unused = sorted(set(overrides) - set(applied))
    if applied:
        print("local overrides applied to SOP %s" % ", ".join(applied), file=sys.stderr)
    if unused:
        print("warning: overrides with no matching SOP: %s" % ", ".join(unused), file=sys.stderr)

    sops = [b for b in body if b["kind"] == "sop"]
    if not sops:
        sys.exit("no SOPs parsed -- the doc's structure changed; check build_sop_binder.py")

    # front matter: title, date, lede, then the About table and notes.
    # Everything from the doc's own "Index" heading on is replaced by a
    # generated index, so its links always resolve.
    title = strip_tags(front[1]) if len(front) > 1 else "Standard Operating Procedures Binder"
    date_raw = strip_tags(front[2]) if len(front) > 2 else ""
    lede = strip_tags(front[4]) if len(front) > 4 else ""
    cut = next((i for i, f in enumerate(front) if ">Index<" in f), len(front))
    about = style_fragments(front[5:cut])

    chips = []
    tbl = " ".join(front[5:cut])
    ver = re.search(r"<td>Version</td><td>([^<]*)</td>", tbl)
    app = re.search(r"<td>Approved by</td><td>([^<]*)</td>", tbl)
    if ver:
        chips.append("Version %s" % ver.group(1).strip())
    if app:
        chips.append("Approved by %s" % app.group(1).strip().split(",")[0].strip()
                     + (", RN" if "RN" in app.group(1) else ""))
    stated = re.search(r"holds the (\d+) standard operating procedures", lede)
    chips.append("%s SOPs" % (stated.group(1) if stated else len(sops)))
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", date_raw)
    if m:
        chips.append("Updated %s %d, %s" % (MONTHS[int(m.group(2)) - 1], int(m.group(3)), m.group(1)))

    logo = "data:image/png;base64," + open(LOGO_FILE, encoding="utf-8").read().strip()
    fav = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
           '<rect width="32" height="32" rx="7" fill="#8b7155"/>'
           '<g fill="none" stroke="#FAF7F0" stroke-width="2.1" stroke-linecap="round">'
           '<path d="M10 9h12v14H10z"/><path d="M13 14h6M13 18h6"/></g></svg>')
    favicon = "data:image/svg+xml," + urllib.parse.quote(fav, safe="")

    page = (TEMPLATE
            .replace("__LOGO__", logo)
            .replace("__FAVICON__", favicon)
            .replace("__TITLE__", html.escape(title))
            .replace("__LEDE__", html.escape(lede))
            .replace("__CHIPS__", "".join('<span class="chip">%s</span>' % html.escape(c) for c in chips))
            .replace("__ABOUT__", about)
            .replace("__INDEX__", build_index(body))
            .replace("__BODY__", build_body(body)))

    open(OUT, "w", encoding="utf-8").write(page)
    print("sop-binder.html: %d SOPs, %d parts, %d sections, %d tables, %d bytes"
          % (len(sops),
             len([b for b in body if b["kind"] == "part"]),
             len([b for b in body if b["kind"] == "section"]),
             page.count("<table>"), len(page)))


if __name__ == "__main__":
    main()
