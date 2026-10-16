# Keelwright Studio

Documents, brand assets and the website for Keelwright Studio (keelwright.dev).

```
brand/          the mark (SVG; with-course and small variants), explored concepts, identity.md (colour, type, voice, usage)
site/           keelwright.dev — static HTML/CSS, no build step
  index.html              the studio one-pager
  swatchbuckler/          product page for Swatchbuckler
  privacy.html            privacy policy for the site and for Swatchbuckler (linked from the store listings)
  assets/site.css         the one stylesheet (light + dark via prefers-color-scheme)
  assets/fonts/           Bricolage Grotesque + Instrument Sans, woff2, SIL OFL
  favicon.svg, apple-touch-icon.png, robots.txt
```

## Deploying the site

Upload the contents of `site/` to any static host (Cloudflare Pages, Netlify, GitHub Pages, a plain web server).
Internal links are root-relative (`/swatchbuckler/`, `/privacy.html`), so it must be served from the domain root.
There is nothing to build; to preview locally run `python3 -m http.server 8000` inside `site/` and open http://localhost:8000.

## Updating the Swatchbuckler screenshots

`site/swatchbuckler/popup-light.png` and `popup-dark.png` are rendered from the extension's built popup;
`site/swatchbuckler/icon-128.png` is a copy of `design-extractor-extension/src/icons/icon-128.png`.
