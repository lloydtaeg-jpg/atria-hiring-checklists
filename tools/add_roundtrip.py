#!/usr/bin/env python3
"""Give a template a text PDF export and the ability to refill itself from
that PDF. Shared code lives in tools/pdf-roundtrip.js; this injects it.

Run from the repo root:  python3 tools/add_roundtrip.py
Re-running is safe: a template that already carries the block is refreshed."""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULE = io.open(os.path.join(ROOT, 'tools', 'pdf-roundtrip.js'), encoding='utf-8').read()

PDFJS = (
 '<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>\n'
 '<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js"></script>\n')

PANEL = """<div class="atria-import no-print" id="atriaImport">
  <div class="atria-import-title">Fill this form from a saved PDF</div>
  <div class="atria-import-hint">Upload a PDF this template produced and every field comes back. The file is read in your browser and is never uploaded anywhere.</div>
  <div class="atria-drop" id="atriaDrop">
    <input type="file" id="atriaFile" accept="application/pdf,.pdf" hidden />
    <button type="button" class="atria-btn" id="atriaPick">Choose PDF</button>
    <span class="atria-drop-hint">or drop it here</span>
  </div>
  <div class="atria-status" id="atriaStatus"></div>
</div>
"""

BLOCK = ('<div class="atria-data" id="atriaDataWrap"><h4>This PDF carries its own answers: upload it to the template to fill the form back in.</h4>'
         '<div id="atriaData"></div></div>\n')

CSS = """
/* --- Atria PDF round-trip (tools/add_roundtrip.py) --- */
.atria-import{background:#fff;border:1px solid rgba(44,62,62,.12);border-left:3px solid ACCENT;
  border-radius:0 8px 8px 0;padding:.85rem 1rem;margin:0 0 1rem;font-family:inherit;
  box-shadow:0 1px 3px rgba(44,62,62,.05)}
.atria-import-title{font-weight:600;color:ACCENT;font-size:.95rem;margin-bottom:.2rem}
.atria-import-hint{font-size:.76rem;color:#5a6a6a;margin-bottom:.55rem;line-height:1.5}
.atria-drop{display:flex;align-items:center;gap:.6rem;flex-wrap:wrap;
  border:1px dashed rgba(44,62,62,.28);border-radius:8px;padding:.6rem .7rem}
.atria-drop.over{border-color:ACCENT;background:rgba(0,0,0,.02)}
.atria-btn{font:inherit;font-size:.78rem;font-weight:600;color:#fff;background:ACCENT;border:none;
  border-radius:7px;padding:.4rem .8rem;cursor:pointer}
.atria-btn:hover{filter:brightness(.93)}
.atria-drop-hint{font-size:.76rem;color:#6b7a7a}
.atria-status{font-size:.76rem;margin-top:.45rem;line-height:1.5;color:#5a6a6a}
.atria-status.ok{color:#3f7a4f}
.atria-status.warn{color:#9a5a2a}
.atria-data{display:none}
@media print{
  .atria-import{display:none!important}
  .atria-data{display:block;margin-top:10px;padding-top:5px;border-top:1px solid #ececec;
    font-family:Helvetica,Arial,sans-serif}
  .atria-data h4{font-family:Helvetica,Arial,sans-serif;font-size:5.5pt;font-weight:400;
    margin:0;color:#c0c0c0;letter-spacing:.01em}
  /* The answers sit in the PDF's text layer so the file can be read back in,
     printed white on white at a hair's height: there is nothing to see. */
  .atria-data .adl{font-size:3.2pt;line-height:1;color:#fff;white-space:normal;
    overflow-wrap:anywhere;letter-spacing:0;margin:0}
}
"""

START = '<!-- atria-roundtrip:start -->'
END = '<!-- atria-roundtrip:end -->'


def strip_existing(s):
    """Remove a previously injected block so re-running is idempotent."""
    s = re.sub(re.escape(START) + r'.*?' + re.escape(END), '', s, flags=re.S)
    s = re.sub(r'\n?/\* --- Atria PDF round-trip.*?\n\}\n', '\n', s, flags=re.S)
    for frag in (PANEL, BLOCK):
        s = s.replace(frag, '')
    return s


def inject(name, accent, anchor, where, adapter, need_pdfjs=True):
    path = os.path.join(ROOT, 'templates', name + '.html')
    s = io.open(path, encoding='utf-8').read()
    before = s
    s = strip_existing(s)

    if s.count(anchor) != 1:
        raise SystemExit('%s: anchor %r appears %d times' % (name, anchor, s.count(anchor)))

    # the panel, next to the form
    s = s.replace(anchor, anchor + '\n' + PANEL if where == 'after' else PANEL + anchor, 1)

    # the styles
    k = s.rindex('</style>')
    s = s[:k] + CSS.replace('ACCENT', accent) + s[k:]

    # the block the PDF carries, and the code
    scripts = START + '\n'
    if need_pdfjs and 'pdf.js/3.11.174/pdf.min.js' not in s:
        scripts += PDFJS
    scripts += '<script>\n' + MODULE + '\n</script>\n<script>\n' + adapter + '\n</script>\n' + END + '\n'
    k = s.rindex('</body>')
    s = s[:k] + BLOCK + scripts + s[k:]

    io.open(path, 'w', encoding='utf-8').write(s)
    return len(s) - len(before)


def to_print(name, extra=''):
    """Replace an html2pdf export with a real print. html2pdf draws the page to
    a canvas, so the saved file is an image: no text, nothing to read back."""
    path = os.path.join(ROOT, 'templates', name + '.html')
    s = io.open(path, encoding='utf-8').read()
    i = s.index('function downloadPDF')
    j = s.index('\n}', i) + 2
    body = s[i:j]
    if 'html2pdf' not in body:
        return False
    opens = ''
    if '.card' in body:
        opens = "  document.querySelectorAll('.card').forEach(function(c){c.classList.add('open');});\n"
    new = ('function downloadPDF(){\n' + opens + extra +
           '  /* print, not html2pdf: html2pdf rasterises the page, so the saved\n'
           '     file holds no text and cannot be read back in. */\n'
           '  if(typeof atriaBuildData===\'function\') atriaBuildData();\n'
           '  setTimeout(function(){ window.print(); }, 60);\n}\n')
    s = s[:i] + new + s[j:]
    s = re.sub(r'\s*<script src="https://cdnjs\.cloudflare\.com/ajax/libs/html2pdf\.js/[^"]*"></script>', '', s)
    io.open(path, 'w', encoding='utf-8').write(s)
    return True


GENERIC = ("window.atriaCollect=window.atriaGenericCollect;\n"
           "window.atriaApply=window.atriaGenericApply;")

AEGEAN = '#5A8282'
BROWN = '#8b7155'

PLAIN = [
    # name,                      accent,  anchor,                                          where
    ('consent-form',             AEGEAN, '<div class="cards">',                            'after'),
    ('service-agreement',        AEGEAN, '<div class="cards">',                            'after'),
    ('job-offer',                BROWN,  '<div class="toolbar no-print">',                 'before'),
    ('orientation-record',       BROWN,  '<div class="toolbar no-print">',                 'before'),
    ('staff-acknowledgement',    BROWN,  '<div class="toolbar no-print">',                 'before'),
    ('supervisory-visit',        BROWN,  '<div class="toolbar no-print">',                 'before'),
]


def main():
    for name in ('consent-form', 'service-agreement'):
        print('%-24s export -> print: %s' % (name, to_print(name)))
    for name, accent, anchor, where in PLAIN:
        d = inject(name, accent, anchor, where, GENERIC)
        print('%-24s round-trip injected (+%d bytes)' % (name, d))


if __name__ == '__main__':
    main()


def refresh_module():
    """Push the current tools/pdf-roundtrip.js into every template that has it."""
    import glob
    paths = sorted(glob.glob(os.path.join(ROOT, 'templates', '*.html')))
    paths += [os.path.join(ROOT, n + '.html') for n, _ in ROOT_DOCS]
    for path in paths:
        s = io.open(path, encoding='utf-8').read()
        if START not in s:
            continue
        blk = s[s.index(START):s.index(END) + len(END)]
        m = re.search(r'(<script>\n)(.*?)(\n</script>)', blk, re.S)
        if not m:
            continue
        s = s.replace(blk, blk[:m.start(2)] + MODULE + blk[m.end(2):], 1)
        io.open(path, 'w', encoding='utf-8').write(s)
        print('%-24s module refreshed' % os.path.basename(path))


ROOT_DOCS = [('psw-checklist', BROWN), ('rn-checklist', BROWN), ('rpn-checklist', BROWN)]


def inject_root(name, accent, anchor='<div class="toolbar no-print">'):
    """Same as inject(), for the role checklists at the repo root."""
    path = os.path.join(ROOT, name + '.html')
    s = io.open(path, encoding='utf-8').read()
    s = strip_existing(s)
    if s.count(anchor) != 1:
        raise SystemExit('%s: anchor %r appears %d times' % (name, anchor, s.count(anchor)))
    s = s.replace(anchor, PANEL + anchor, 1)
    k = s.rindex('</style>')
    s = s[:k] + CSS.replace('ACCENT', accent) + s[k:]
    scripts = (START + '\n' + PDFJS + '<script>\n' + MODULE + '\n</script>\n<script>\n'
               + GENERIC + '\n</script>\n' + END + '\n')
    k = s.rindex('</body>')
    s = s[:k] + BLOCK + scripts + s[k:]
    io.open(path, 'w', encoding='utf-8').write(s)
