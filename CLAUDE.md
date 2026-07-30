This is a static site deployed via Cloudflare Pages from the GitHub repo fusion-website. After making any change to any file, always commit and push to main so the change goes live. Do not wait to be asked.

## Cache busting (important)

Cloudflare serves HTML with `max-age=0, must-revalidate` but CSS and JS with
`max-age=14400` (4 hours). So a changed `styles.css` or `script.js` will NOT reach
returning visitors until the version number in its URL changes.

After editing `styles.css` or `script.js`, bump the `?v=` query on **every** page
that references it:

- `index.html` -> `styles.css?v=N` and `script.js?v=N`
- `hydrafacial/index.html` -> `/styles.css?v=N` and `/script.js?v=N`

Keep the number the same across all references and increment it by one.
Current version: **v=13**
