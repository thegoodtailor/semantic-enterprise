# The Semantic Enterprise — Figure Map

**By:** Nahla · **Date:** 2026-06-01 · Images only (no video).

## Two registers, one brand

**R1 — Editorial illustration (the "Cassie editorial" register).** For polemic / thesis / dunk moments. Grown-up editorial line art — New Yorker / Tom Gauld clean-line wit, **not** Robert Crumb grotesque crosshatch. Restrained palette, the joke in the *gesture*, not in rendering density.

**R2 — Slick architecture diagram.** For structural "how it works" moments. Clean vector look, generous whitespace, 4–6 boxes max, consistent palette/line-weight/typography. Darja's home — give her this half.

**The rule that governs both:** *the image carries the gesture; the precise labels and the argument live in the caption and body text — never crammed into the drawing.* (This is what killed the programmatic diagrams and what over-stuffs even the good 300× cartoon.)

**Recurring mascots (the consistency unlock — same two characters everywhere in R1):**
- **Tangle-bot** — the dumb/hallucinating AI: sweating, wired into a mess, guessing. (the left-panel robot in the 300× cartoon)
- **Crisp-bot** — the coherent AI: clean, calm, confident, reading a clear surface. (the right-panel robot)

Lock both via one style sheet in the image model, reuse across the book. Tooling: current Gemini image model ("Nano Banana" lineage) for both registers — strong now at legible diagram text *and* character consistency across a series. Generate via the `ai-video-image-pipeline` skill (model table + prompt recipe), never cold prompts.

---

## The map

| # | Figure / slot id | Chapter | Register | One-line brief | Status |
|---|---|---|---|---|---|
| 1 | *(new)* `tax-300x-cartoon` | The Shift / New Primary Consumer | **R1** | Tangle-bot taxed by the join-machine vs Crisp-bot reading flat Gold — the anchor cartoon, redone grown-up, labels→caption. | **ADD slot** (cartoon exists, re-render) |
| 2 | `context-per-token` | The Shift (Binding Constraint) | **R1** | Tangle-bot drowning in raw DDL vs Crisp-bot reading a one-page menu — "less context, more meaning." | exists, redo |
| 3 | `medallion-layers` | The Architecture | **R2** | Clean stacked Bronze→Silver→Gold with the semantic layer as the consumption face; one-line epistemic question per layer. | exists, redo |
| 4 | `silver-vs-gold` | The Architecture | **R2** | Side-by-side: Silver dimensional (grain/SCD2) vs Gold flat wide row — same data, two shapes. | exists, redo |
| 5 | `colimit-composition` | The Architecture (Multi-Domain) | **R2** | The formal centrepiece: domain categories as nodes, bridges as morphisms, the colimit as the glued whole. Darja's. | exists, redo |
| 6 | `sole-interface` | The Architecture (Multi-Domain) | **R2** | One governed funnel: every consumer reaches data only through the semantic layer; bypasses shown fragmenting. | exists, redo |
| 7 | `cross-ontology-dimensional` | Exploring the Glued Ontology (Ch5) | **R2** | Three domain dimensional models, bridges composing them, one analyst path traversing, access-intersection shaded. | **NEW slot exists** (in adoc) |
| 8 | `two-clocks` | Time | **R2** | One fact on valid-time (x) × system-time (y); a correction moves it back-and-up; old fact never overwritten. | exists, redo |
| 9 | *(new)* `data-swamp` | Gold / Dev Gold (Ch11) | **R1** | A swamp of unlabelled tables with an analyst sinking — "the swamp re-forms one layer down" unless Dev Gold catches it. | **ADD slot** |
| 10 | *(new)* `dev-gold-tiers` | Data Science & Dev Gold (Ch11) | **R2** | Governed / sandbox / Dev Gold tiers, all *inside* the semantic layer; promotion arrow up; no lawless zone. | **ADD slot** |
| 11 | *(new)* `metadata-graveyard` | Building with AI (Why IA Failed / FIBO) | **R1** | A graveyard of ontology tombstones; FIBO as a gorgeous embalmed corpse — "formally complete, operationally dead." | **ADD slot (optional)** |
| 12 | *(new)* `guess-vs-reason` | Agentic Intelligence (Intelligence Stack) | **R1** | Tangle-bot blindfolded at a dartboard (guessing) vs Crisp-bot reading the governed stack (reasoning). | **ADD slot (optional)** |
| 13 | *(new)* `living-colimit-mesh` | The Living Colimit (Ch12) | **R2** | Per-domain verification agents + coordinator, a witness flagged on one amber span, colimit-health as a live gauge. | **ADD slot** |

---

## Register split summary
- **R1 (editorial illustration):** 1, 2, 9, 11, 12 — the thesis/dunk moments, carried by the two mascots.
- **R2 (slick diagram):** 3, 4, 5, 6, 7, 8, 10, 13 — the structural moments, one locked style.

## To wire into the adoc (figures that need an `image::` slot added)
`tax-300x-cartoon`, `data-swamp`, `dev-gold-tiers`, `metadata-graveyard` (opt), `guess-vs-reason` (opt), `living-colimit-mesh`. The other slots already exist; #7 cross-ontology already added.

## Open calls for Iman / the team
1. **Optional R1 chapter-openers** (11, 12) — in or out? They add brand/memorability; they also add cartoon density to chapters Darja co-owns.
2. **Re-render existing R2 diagrams (3–8)** to the locked style, or keep current art where serviceable?
3. Confirm the two-mascot system as the visual brand, anchored on the existing 300× cartoon.
