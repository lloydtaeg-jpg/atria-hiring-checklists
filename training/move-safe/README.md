# Move Safe — public build

Deployed to <https://atria-move-safe.netlify.app> (Netlify project
`atria-move-safe`, site id `6cea5cff-f4ee-453f-ba5b-6365bae4fe99`).

This folder was created by pulling the already-deployed page down from
Netlify — the site had no source in version control before — and then
rebranding it to match Care by the Book.

Unlike that module, Move Safe never used the Claude runtime: it is already
standalone and keeps its result in `localStorage`, so it needed no
off-platform patching.

## Rebrand (presentation only)

The module's JavaScript is untouched, byte for byte: same 26 questions,
same 21/26 pass mark, same certificate. Only the shell changed.

1. **Fonts** — Atkinson Hyperlegible + Bricolage Grotesque replaced with
   Lora + Inter.
2. **Brand layers** — Care by the Book's two trailing `<style>` blocks (the
   Atria brand layer and the layout layer) appended so they win over the
   base styles. These carry the teal/sage palette, the serif headings and
   the card treatments.
3. **Branded header** — the `brandbar` (logo, "Atria Private Care", "Home &
   Community Care", module title, one-line description) and the `meta-bar`
   (Covers / Time / Pass mark), matching Care by the Book.
4. **Hero removed** — the old hero repeated the title now in the brandbar,
   and the amber hazard `stripe` clashed with the palette. Replaced with the
   same `intro` block Care by the Book uses.
5. **Module identity** — the rebrand made the two modules nearly
   indistinguishable in a browser tab. Move Safe now carries a deeper olive
   `--module` accent (drawn from the Atria palette's olive) against Care by
   the Book's teal, its own SVG favicon, a short `<title>` of just the module
   name, and a strip of three line illustrations under the header: walkers
   and equipment, transfers and handling, if a client falls. The module title
   is now the largest thing in the header; the company wordmark sits above it
   as a smaller caps line. The text tokens (`--ink`, `--muted`, `--faint`,
   `--brand-ink`) are olive-biased too, so the page reads as one colour
   rather than teal writing in an olive frame. They are olive-leaning
   neutrals rather than literal olive, and every one clears WCAG AA on the
   page background — body 11.5:1, headings 6.0:1, the small uppercase labels
   4.8:1. Check the ratios if you change them.
6. **Certificate branded** — the on-screen and downloaded certificates still
   used the old palette with no logo. Both now carry the Atria mark and the
   teal treatment, the same certificate Care by the Book issues.

The **Email my certificate** button was already here and still works: a
`mailto:` to `RETURN_EMAIL` carrying name, module, version, score and date.
Care by the Book now has the same three buttons. That email is the only
record of a completion, so do not remove it.

Keep the two modules' brand layers in step: they are copied, not shared, so
a change to Care by the Book's does not reach this one.

## Deploy

    cd training/move-safe
    netlify deploy --prod --dir . --site 6cea5cff-f4ee-453f-ba5b-6365bae4fe99

The folder is not linked, so the site id is required; `--site atria-move-safe`
by name fails with "Error while running build".

## Falls: who owns what

Falls are split between the two modules deliberately:

- **SOP 31 / Care by the Book** own the *response*: checking breathing, the
  red flags, the 911 decision, reporting and monitoring.
- **Move Safe** owns the *mechanics*: guiding a fall down, never lifting off
  the floor, covering without rolling, coaching the floor-recovery sequence,
  and why getting up outside the home is usually unsafe.

The six response-procedure questions that used to end this quiz were replaced
with six mechanical ones. Keep it that way: a question about what to look for
or who to call belongs in Care by the Book, not here.

## Not synced

The Claude artifact <https://claude.ai/artifact/4TH3mb7ErMjmw5Bxy75GFp> still
has the old branding and the old falls content.

It also declares the `user`, `db` and `downloads` capabilities and carries a
"Staff completions" admin panel recording who has passed. The public build
has none of that — whoever made it stripped the Claude runtime out — so
publishing this file over the artifact would remove the panel.

Taegan confirmed on 2026-10-15 that completion tracking is not wanted, so
that is not a reason to hold back: the artifact can simply be overwritten
with this file when someone wants the two to match. Completions are tracked
on paper instead — staff send in the certificate the module generates.
