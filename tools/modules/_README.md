# Training modules

Each module is generated from a content spec by `tools/build_module.py`:

    python3 tools/build_module.py tools/modules/whmis.py

`base.css` and `engine.js` are the shared shell, lifted from Care by the Book:
navigation, section and quiz rendering, grading, and the certificate with its
email / print / download buttons. A spec supplies only content, colour and
pass mark, so every module behaves the same and a new one is a single file.

## Spec fields

| Field | What it is |
| --- | --- |
| `SLUG` | output folder under `training/` |
| `TITLE`, `SUBTITLE` | brandbar heading and the line under it |
| `COVERS`, `TIME` | the meta bar |
| `VERSION` | bump when content changes materially; staff who passed the old one are asked to retake |
| `PASS_MARK` | out of `len(QUIZQ)` |
| `GLYPH` | favicon path data, drawn on the accent colour |
| `COLOUR` | `light`, `mid`, `ink`, `dark`, `darkbg` |
| `SECTIONS` | `name`, `sops`, `lede`, `rules[]`, `scene{}` |
| `QUIZQ` | `s` (section index), `q`, `o[]`, `a` (index), `e` |

A rule is `[title, body, reference]`, with an optional 4th element `1` to
flag it red. A scene is `{h, t, c:[[choice, correct, why], ...]}` with exactly
one correct choice.

## Colours in use

| Module | Accent |
| --- | --- |
| Care by the Book | terracotta `#8C5243` |
| Move Safe | olive `#6E7444` |
| WHMIS | slate blue `#46617E` |
| Health & Safety Awareness | forest green `#3D6B4F` |
| Accessible Care (AODA) | plum `#6B4A63` |
| Violence & Harassment | charcoal `#4F535C` |

Teal is reserved for care planning and brown for administration documents, so
no module uses either.

## Before publishing a new module

    node /path/to/validate_mods.js     # or re-check by hand:

Every question's `s` points at a real section, every section has at least one
question, every scene has exactly one correct choice, and the pass mark does
not exceed the question count. Then create the Netlify site, set
`sso_login` to false (the account defaults it on, which 401s staff), deploy,
and add it to `directory.html`.

## Legislated modules

WHMIS, Health & Safety Awareness, Accessible Care and Violence & Harassment
exist to meet Ontario training duties. They are Atria-delivered education, not
a certificate from an accredited provider. WHMIS in particular must cover the
products actually in use, so the supervisor still walks through site-specific
products at orientation. Have someone qualified review the content before
relying on these for compliance.
