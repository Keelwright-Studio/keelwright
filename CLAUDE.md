# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Keelwright Studio (keelwright.dev): a hand-written static site (`site/`). There is no build, test or lint tooling.

`brand/`, `.sync/` and `Claude outputs/` exist only on the owner's machine: they are gitignored and not in the repo. Never `git add` them. If `brand/` is absent (e.g. a fresh clone), skip the mark-regeneration command and the `brand/identity.md` checks below.

## Commands

- Preview: `python3 -m http.server 8000` inside `site/`, then open http://localhost:8000. Don't open files via `file://`; internal links are root-relative (`/swatchbuckler/`, `/privacy.html`) and break.
- Regenerate the mark: from `brand/generator`, run `python3 -c "from marks3 import k_final; print(k_final(256,'light'))" > ../keelwright-mark.svg`, then add the `xmlns` attribute to the `<svg>` tag by hand. `k_final(size, ground, badge, accent, course)` is the chosen mark.

## Deploy

Hosted on GitHub Pages. `.github/workflows/pages.yml` publishes `site/` on every push to `main`; there is no build step. The site must be served from the domain root (custom domain keelwright.dev), because internal links are root-relative.

## Rules

- Follow `brand/identity.md` for colour, type, voice and mark usage. Key points:
  - One studio accent only: cobalt `#2D6AE3` (`#4A80EA` in dark). Swatchbuckler's five swatch colours appear only when showing the product.
  - Headings Bricolage Grotesque 800 at -0.02em tracking; body Instrument Sans. Colours come from the CSS custom properties in `site/assets/site.css`; don't hardcode hex values in pages.
  - Mark: the dotted "course" appears only at 48px and above, and only as dots. Minimum size 16px. Never add a compass rose, a map or a second colour.
  - Voice is plain, confident, a little dry, short sentences. Pirate jokes belong to Swatchbuckler only; the studio never says "plunder" about itself.
- No external dependencies on the site: no JS build, CDNs, third-party scripts or hosted fonts. Fonts are vendored woff2 in `site/assets/fonts/`.
- Ask before editing `site/privacy.html`. It covers the site and Swatchbuckler, and the store listings link to it.
- Never modify `.sync/` (archive snapshot) or `Claude outputs/` (generated review screenshots).

## Cross-repo

Swatchbuckler lives in `~/Sites/design-extractor-extension`. `site/swatchbuckler/popup-light.png` and `popup-dark.png` are rendered from its built popup, and `icon-128.png` is a copy of its `src/icons/icon-128.png`.
