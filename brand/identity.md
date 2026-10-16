# Keelwright Studio — identity notes

Legal and display name **Keelwright Studio**; short form **Keelwright**; domain **keelwright.dev**; contact hello@keelwright.dev.
First offering: Swatchbuckler (repo `~/Sites/design-extractor-extension`).

## Idea

The keel is the part that keeps a hull true. A keelwright builds that part. The studio makes small, well-made tools:
local by default, open formats out, built to be read by people and by AI assistants.

## Mark

The K as chart dividers. The letter's stem is the instrument's handle (knurled knob on top), its arm and leg are the
two legs of a pair of navigator's dividers on a screw hinge, with needle points in cobalt. At 48 px and above a dotted
cobalt course arcs between the points — the bearing the dividers step off. Below 48 px the course is dropped and the
mark is the bare instrument, so it stays crisp as a favicon.

Files: `keelwright-mark.svg` (ink on paper badge, with course), `-dark` (paper badge, ink mark), `-bare` (no badge),
`-mono` (one colour, for print/engraving); `keelwright-mark-small*.svg` are the sub-48 px versions without the course.
Explored alternatives live in `concepts/` (A hull, B half-hull, C plain K; the wheel, compass and other K variants are
on the canvas): https://claude.ai/artifact/DChs4iSJckMFRQVG4eEtTG

Rules: the course appears only at 48 px and above, and only ever as dots, never a solid arc. Clear space: the width
of the hinge on every side. Minimum size 16 px. The needle tips are the only solid cobalt in the mark; don't colour
the stem or the legs. Never add a compass rose, a map or a second colour.

## Colour

| token | value | use |
|---|---|---|
| ink | `#14213D` | text, the mark, inverse surfaces |
| paper | `#FBF8F3` | page ground |
| cobalt | `#2D6AE3` | the one accent: the needle points and the plotted course in the mark; links, focus, primary buttons, the rule at the foot of each page |
| surface | `#FFFFFF` | cards |
| muted | `#5B6472` | secondary text (4.5:1 on paper) |
| border | `#E6E1D8` | hairlines |

Dark scheme: ink-tinted canvas `#121A2E`, surface `#1A2340`, text paper, accent lifted to `#4A80EA`.
The five Swatchbuckler swatch colours (vermilion, mustard, grass, cobalt, violet) belong to the product, not the studio;
the studio borrows them only when showing the product.

## Type

Bricolage Grotesque 800 for names and headings (tight tracking, -0.02em). Instrument Sans 400/500/600 for everything else.
Both vendored as woff2 under the SIL Open Font License (`site/assets/fonts/`). Mono: the system UI monospace stack.

## Voice

Plain, confident, a little dry. Short sentences. Says what a thing does and what it doesn't collect.
The pirate jokes stay on the Swatchbuckler side; the studio never says "plunder" about itself.

## Relationship to Swatchbuckler

Same ink, paper and type, so they read as siblings. The studio has one accent; the product has five.
Lockup: "Swatchbuckler · by Keelwright Studio". In the extension: a quiet "A Keelwright tool" byline.
