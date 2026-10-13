---
name: update-sop-binder
description: Rebuild and republish the staff-facing SOP binder page from the Atria SOP Binder Claude Doc. Use when the user has edited the binder doc and wants the published page at lloydtaeg-jpg.github.io/atria-hiring-checklists/sop-binder.html to match, or says things like "update the SOP binder", "push my SOP changes live", or "the binder page is out of date".
---

# Update the published SOP binder

The binder's single source of truth is a **Claude Doc**, not the HTML page.
Taegan (RN, clinical lead) edits the doc; this skill regenerates the
read-only staff page from it and publishes it.

Never hand-edit `sop-binder.html` — it is generated and will be overwritten.
A wording fix belongs in the doc.

**Doc:** `https://claude.ai/artifact/0b1f15f9-9f66-42f5-8fa7-d7c82a2d6735`
- doc id: `0b1f15f9-9f66-42f5-8fa7-d7c82a2d6735`
- tab body node id: `0576d302-cef3` (re-read the project if this ever fails)

## Steps

1. **Clear the cache** so a shortened doc cannot leave stale blocks behind:
   `rm -f tools/doc-cache/*.xml`

2. **Read the whole doc** through the Claude Docs connector:

   ```
   read( ref       = {"object":"node","id":"0576d302-cef3"},
         engine    = "prose",
         container = {"kind":"project","id":"0b1f15f9-9f66-42f5-8fa7-d7c82a2d6735"},
         payload   = {"kind":"view"} )
   ```

   The reply is capped. While it says `complete: false`, send its `next`
   value back **verbatim** as the next `payload` (keeping `kind: "view"`),
   and repeat until a reply has no `next`.

3. **Save every chunk in the order read** to `tools/doc-cache/01.xml`,
   `02.xml`, ... Save the `data.xml` string, or the whole JSON reply — the
   build script accepts either. Large replies are written to a file
   automatically; extract `.data.xml` from that file rather than pasting it
   through the conversation.

4. **Build:** `python3 tools/build_sop_binder.py`

   It prints the SOP/part/section/table counts. It warns on unfilled gaps,
   which means a read was not continued to the end — go back to step 2.

5. **Verify before publishing:**
   - SOP count matches the doc (54 entries as of Oct 2026: SOPs 1–52, plus
     26A, 28A, 28B — the doc calls this "52 SOPs" because 28 splits in two).
   - No broken anchors:
     ```
     python3 -c "import re;s=open('sop-binder.html').read();ids=set(re.findall(r'id=\"([^\"]+)\"',s));print([h for h in re.findall(r'href=\"#([^\"]+)\"',s) if h not in ids and h!='top'] or 'ok')"
     ```
   - Skim a diff of the rendered text (`git diff`) and confirm the changes
     are the ones the user actually made in the doc. This is a clinical
     document: an unexpected deletion is a bug, not noise.

6. **Commit and push.** The page is only live once pushed — GitHub Pages
   serves `main`. Then confirm:
   `curl -s -o /dev/null -w '%{http_code}' https://lloydtaeg-jpg.github.io/atria-hiring-checklists/sop-binder.html`
   Pages takes up to a few minutes; poll rather than assuming.

## Known quirks of the source doc

Both are handled by the build script, but say so if the user asks why the
page differs from the doc:

- **SOPs 51 and 52 are heading level 2**; every other SOP is level 3. The
  script accepts either, otherwise those two vanish from the page.
- **They have no section heading.** The script groups them under
  "Client travel", the section the doc's own index table assigns them.
- **The doc's index tables are replaced** by an index generated from the
  actual headings, so every link resolves.
