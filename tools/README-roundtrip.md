# PDF round-trip

Every fillable document saves a real text PDF (`window.print()`), and that same
PDF can be uploaded back into the document to restore every field.

- `tools/pdf-roundtrip.js` — the shared module. **Edit here, never in a template.**
- `tools/add_roundtrip.py` — injects it. `refresh_module()` pushes a change into
  every document that already carries the block.

```
python3 -c "import sys; sys.path.insert(0,'tools'); import add_roundtrip as a; a.refresh_module()"
```

## How it works

Printing writes the form's answers into the last page of the PDF: base64 inside
`ATRIA-DATA-V1 … ATRIA-DATA-END`, one line per 96 characters, each framed with
`~`. Uploading reads the PDF's text, pulls those framed runs out, and hands the
decoded object to the document.

Three things that broke earlier attempts, and why it is built this way:

- **html2pdf rasterises.** It draws the page to a canvas, so the saved file is a
  picture with no text in it. Nothing can be read back. Every document prints now.
- **Base64 and the `~` frames** survive whatever the PDF reader does to spacing,
  and let a browser's own print header or page number sit on those pages without
  being mistaken for payload. Each chunk is short enough that it cannot wrap at
  the printed size: a wrapped line puts its closing `~` on the next row and the
  reader pairs the wrong tildes. The reader checks every chunk is a full
  `WIDTH` and gives up rather than restore half a form.
- **One element per line.** A single `white-space: pre-wrap` block gets reflowed
  on print and the lines run together.

The answers print white on white at 3.2pt, so there is nothing to see on the
page: only a grey line saying the file carries its own answers. They are still
in the PDF's text layer, which is what makes the upload work, so Select All in a
PDF reader will find them.

## Two things the browser does to a printed page

**It prints its own header and footer** into the margin: the page title and time
at the top, the address and "Page 3 of 18" at the bottom. To a PDF reader those
are ordinary text, so without `atriaStripRunningHeads` they are read as part of
the record and land inside a findings or contact field. Worse, a page break in
the middle of a wrapped cell leaves the furniture between the two halves, so the
two halves never rejoin and every row after it is lost.

**Safari prints with background graphics off by default.** A ticked box drawn as
a coloured square with a white tick prints blank: the square's colour is a
background and the tick is white on white. Every document therefore draws a
ticked box on paper as a dark tick in an outlined box, which needs no colour.

## Adding it to a new document

Each document supplies two hooks:

```js
window.atriaCollect = function(){ /* -> a plain object of the answers */ };
window.atriaApply   = function(data){ /* write it back; return a count */ };
```

A document with no state model of its own uses `atriaGenericCollect` and
`atriaGenericApply`, which walk the contenteditable fields, inputs, textareas and
checkboxes in document order. A document whose answers live in JavaScript
(vitals, labs, client, clinical, quarterly-review) points the hooks at its own
collect/apply, so the JSON export and the PDF stay in step.

Elements inside `.import-panel`, `.atria-import`, `.import-wrap` or anything
marked `data-atria-skip` are page furniture, not form, and are left out.

The fields are restored by position, so reordering a form would put every
answer from an older PDF in the wrong box. The form's shape — how many
contenteditable fields, inputs, textareas, checkboxes and `.box` spans it has —
travels with the answers as `sig` and is checked before anything is written.
A mismatch writes nothing and says so; Medical History falls back to reading the
PDF as text. A PDF saved before `sig` existed carries none, and still restores.
