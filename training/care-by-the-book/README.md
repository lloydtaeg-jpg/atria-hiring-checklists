# Care by the Book — public build

Deployed to <https://atria-care-by-the-book.netlify.app> (Netlify project
`atria-care-by-the-book`), so staff can take the test without a Claude
account.

`index.html` is the Claude artifact
<https://claude.ai/artifact/4t1Unmg65skY3fFnx8F5c1> with four changes that
let it run off-platform. To re-export after editing the artifact, re-apply
these:

1. **Certificate download.** The artifact saves the certificate through
   Claude's `downloads` capability, which does not exist here. Falls back to
   a Blob + `<a download>`, then to opening it in a new tab.
2. **Download button.** Was shown only when that capability resolved, so it
   never appeared off-platform. Now always shown on a pass.
3. **Result saving.** No shared database here, so the result is written to
   `localStorage` and the on-screen message tells the staff member to send
   their certificate to the office.
4. **Prior attempt.** Reads that `localStorage` record so someone returning
   on the same device sees their last score.

The `claude.use()` calls are left in place — they no-op off-platform, so the
same file still works if opened on claude.ai.

## Deploy

    cd training/care-by-the-book
    netlify deploy --prod --dir .

Note: this Netlify account now creates sites with SSO protection on by
default, which returns 401 to staff. Sites must have `sso_login` set to
false to be publicly reachable.

## Local additions (not in the artifact)

Section 11, **Travel with clients** (SOPs 51 and 52: Pilatus PC-12 air
travel and vacation travel), plus its six quiz questions, were added here.
Module version bumped to 1.2 so anyone who passed 1.1 is asked to retake it,
and the pass mark moved from 47/50 to 53/56 — still three wrong allowed.

The claude.ai artifact does **not** have this section. Either republish this
file to it, or re-apply the four off-platform changes above after editing
there, or the two will keep drifting apart.

## Limitation

Results are **not** recorded centrally — `localStorage` is per-device and
per-browser. The office gets a record only when the staff member sends in
their certificate. Netlify Forms could capture completions automatically if
that becomes a requirement.
