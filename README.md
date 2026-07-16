# The Semantic Enterprise

*Data Architecture for the Agentic Era* — book source (AsciiDoc).

**Canonical source:** the chapter files in [`chapters/`](chapters/) (`01-introduction.adoc` … `16-references.adoc`). The master file [`the-semantic-enterprise.adoc`](the-semantic-enterprise.adoc) only assembles them via `include::` — edit the chapters, never the master, and never edit `the-semantic-enterprise-merged.adoc` (a generated artifact with a DO-NOT-EDIT banner; regenerate with `python3 merge_book.py`).

## Editing

Edit the files in `chapters/` — via GitHub's web editor, or a local clone (VS Code's AsciiDoc extension gives live preview; open the master file's preview to see all 16 chapters assembled). Commit and push; the GitHub Action rebuilds the PDF and self-contained HTML on every push to `main` (download from the Actions tab — build artifacts are not committed).

> AsciiDoc, not LaTeX — this is the format O'Reilly's authoring platform uses. Overleaf won't render it; edit on GitHub or locally.

## Layout

| Path | What |
|---|---|
| `chapters/` | the book: 14 chapters + No Walls coda + Engineer's Appendix + References |
| `figures/` | 28 inline figures + `cover.png` (Scarfe-register cartoons + clean diagrams) |
| `figure-map.md` | which figure is which register, and where each lands |
| `revision/` | editorial conventions (`//@ TAG:` markup), perishability policy, AI-tells scanner, fact-check record |
| `proposal/` | the O'Reilly book proposal |
| `audiobook/` | spoken-edition rig — ElevenLabs two-register + ambient bed |
| `*.py` (top level) | figure-generation + build scripts |

The formal treatment of the colimit results (consistency ≡ commutativity, soundness of gluing, finishability) is developed **in the book itself** — "The Living Colimit," § The Formal Spine. The earlier standalone draft paper ([thegoodtailor/enterprise-colimit](https://github.com/thegoodtailor/enterprise-colimit)) has been subsumed by that section and is retained only as an archive. A companion experiments repo (TradeBench) is in preparation and will be linked here.

## Outstanding

- (none — the AI-added "SCARFE" signatures were stripped from all six affected cartoons in July 2026; pre-cleanup originals are archived locally outside the repo.)
