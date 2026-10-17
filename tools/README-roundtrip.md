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
  being mistaken for payload.
- **One element per line.** A single `white-space: pre-wrap` block gets reflowed
  on print and the lines run together.

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

If a document's fields are reordered or added to, PDFs saved by the older
version restore by position and will land in the wrong boxes. Change the
`ATRIA-DATA-V1` marker when that happens.
