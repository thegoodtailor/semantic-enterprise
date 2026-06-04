# The Semantic Enterprise

*Data Architecture for the Agentic Era* — book source (AsciiDoc).

**Canonical source:** [`the-semantic-enterprise.adoc`](the-semantic-enterprise.adoc). Edit that file; everything else is figures, build scripts, and a companion paper.

## Editing

Edit `the-semantic-enterprise.adoc` directly — via GitHub's web editor, or a local clone in any editor (VS Code's AsciiDoc extension gives live preview). Commit your changes; the PDF is rebuilt from this source (not committed — it's a build artifact).

> AsciiDoc, not LaTeX — this is the format O'Reilly's authoring platform uses. Overleaf won't render it; edit on GitHub or locally.

## Building the PDF

```bash
asciidoctor-pdf -a front-cover-image=figures/cover.png \
  -o the-semantic-enterprise.pdf "the-semantic-enterprise.adoc"
```

Needs `asciidoctor-pdf` (Ruby gem). All 27 inline figures live in `figures/` and are referenced as `image::figures/*.png`; the cover is `figures/cover.png`, applied via the `front-cover-image` attribute. An HTML build: `asciidoctor -a data-uri -a allow-uri-read the-semantic-enterprise.adoc`.

## Layout

| Path | What |
|---|---|
| `the-semantic-enterprise.adoc` | the book (13 chapters + No Walls coda + References) |
| `figures/` | 27 inline figures + `cover.png` (Scarfe-register cartoons + slick diagrams) |
| `figure-map.md` | which figure is which register, and where each lands |
| *(moved)* | companion academic paper *The Enterprise Model Is a Colimit* (the formal spine) now lives in its own repo: [thegoodtailor/enterprise-colimit](https://github.com/thegoodtailor/enterprise-colimit) |
| `the-semantic-enterprise-review.md`, `*-reviewiman.md`, `pdf-vs-adoc-comparison.md` | editorial review + provenance notes |
| `audiobook/` | spoken-edition rig — ElevenLabs two-register (cosmic narrator + Maher flame) + ambient bed; `scripts/{segment,tts,music}.py` |
| `*.py` (top level) | figure-generation + one-shot transform scripts (archival) |

## Outstanding

- A few interior cartoons still carry an AI-added "SCARFE" signature — to be stripped (drop cleaned PNGs into `figures/`, same filenames, then rebuild).
