This is a static site deployed via Cloudflare Pages from the GitHub repo fusion-website. After making any change to any file, always commit and push to main so the change goes live. Do not wait to be asked.

## Cache busting (important)

Cloudflare serves HTML with `max-age=0, must-revalidate` but CSS and JS with
`max-age=14400` (4 hours). So a changed `styles.css` or `script.js` will NOT reach
returning visitors until the version number in its URL changes.

After editing `styles.css` or `script.js`, bump the `?v=` query on **every** page
that references it:

- `index.html` -> `styles.css?v=N` and `script.js?v=N`
- `hydrafacial/index.html` -> `/styles.css?v=N` and `/script.js?v=N`
- the seven generated service pages -> set `ASSET_VERSION` in
  `tools/build_service_pages.py` and re-run it

Keep the number the same across all references and increment it by one.
Current version: **v=14**

## Editing files from PowerShell (important)

Do NOT round-trip these files through `Get-Content -Raw` + `WriteAllText`.
PowerShell 5.1 reads as ANSI and writes as UTF-8, which double-encodes every
em dash and curly quote into mojibake. Use the Edit tool, or read/write with an
explicit UTF-8 encoding.

## Service pages

The seven service pages (`/laser-hair-removal`, `/waxing-threading`,
`/skincare-facials`, `/microneedling-peel`, `/massage`, `/eyes-brows`, `/makeup`)
are GENERATED. Do not hand-edit `<slug>/index.html` - the next build overwrites it.

Edit the copy or layout in `tools/build_service_pages.py`, then run:

    python tools/build_service_pages.py

`/hydrafacial` is hand-built and is NOT generated - edit that one directly.
