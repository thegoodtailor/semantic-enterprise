# Revision Campaign — Master Plan

**Date:** 2026-06-11 · **Decisions locked:** whole-book crypto scrub → generic trading venue / capital-markets firm; staged execution with git review between stages.
**Companion docs:** `../review-2026-06-11-technical-depth-and-style.md` (the audit), `01–05` briefs in this directory (agent-ready instructions). Where this plan conflicts with the review, this plan wins — specifically: review §1.2's "flatten Gold" framing of the 300x fix is superseded by the governed-joins philosophy (brief 03), and review §1.5's GDPR fix is superseded by the de-crypto rewrite (brief 04).

## Format & workflow (the LaTeX question)

Stay in AsciiDoc — no LaTeX bridge. AsciiDoc is natively multi-file: the master `the-semantic-enterprise.adoc` keeps the doc header and becomes a list of `include::chapters/NN-name.adoc[]` directives; Asciidoctor builds it identically to the monolith. This gives you everything LaTeX would have (per-chapter files, parallel agents without merge conflicts, small reviewable diffs) with zero conversion loss and no publisher friction. `merge_book.py` (added in Stage 0) flattens the includes back into a single file for any of your existing scripts that expect the monolith.

## Stages (one git review between each)

**Stage 0 — Mechanical + split (today).**
Safe-only fixes on the monolith: `—-` → `—` (415 sites), unambiguous typos. Then split into `chapters/01…14`, master becomes includes, reconstruction verified byte-for-byte, build checked. No prose changes.

**Stage 1 — Corrections + de-crypto (one agent per chapter, parallel).**
Each agent gets: its chapter, brief `02-corrections.md` (facts, numbers, citations — line-keyed) and brief `04-decrypto-and-gdpr.md` (replacement mapping). Output: corrected chapter, no style changes yet. A continuity agent then sweeps for missed references and broken cross-chapter numbers.

**Stage 2 — Structural rewrites (targeted agents, not per-chapter).**
- The governed-joins philosophy integrated (brief 03): new doctrine section in The Architecture; rewrites of the flat-Gold passages in The Shift, Death of the Dashboard, and the Playbook to the "joins declared, never inferred" claim; the camps/battle-map section replacing "Where Serious People Disagree" §star-schemas.
- Multi-agent section rebuilt — celebratory framing, falsification argument, topology law (brief 05 v2).
- **NEW CHAPTER: The Reflexive Loop** (brief 06) — falsifiability as architecture; definitions as conjectures; semantic assertions, postmortems, refutation panels, calibration ledger, belief-revision record. Placed between The Living Colimit and The Playbook; absorbs "When AI-Maintained Definitions Go Wrong"; extends Core Position #7; adds Playbook diagnostic question #5 and feedback-event/pre-flight-calibration items. This is the revision's novel contribution — novelty verified against prior art June 2026 (see brief 06 §4).
- GDPR/erasure section rebuilt (brief 04, part B).
- The Laws page added (review Part 2); Engineer's Appendix added (review Part 3: Silver DDL, semantic-model YAML, context-budget vendor numbers, shared-key registry, CI gates, Gold publication spec).
- De-duplication: flat-Gold argument told once in full (Architecture) + cross-references; FIBO autopsies merged into Building with AI; domain essay defined once; one "interning" sentence kept.
- Fix the Silver physical-shape contradiction (brief 03 §5).

**Stage 3 — Style pass (one agent per chapter, parallel, against brief 01).**
Voice only; no factual or structural changes. Continuity agent checks terminology discipline (bridge = span; morphism vs relationship), repetition across chapters, and that each chapter's kill-shot construction count ≤ 1–2.

**Stage 4 — Verification.**
Fresh fact-check agent re-audits every number + URL against the live web; build the PDF; a cold-read agent flags anything that still reads as hedge or repeat. Figures audit: `tax-300x.png` is now orphaned (claim removed — replace with a "joins above / joins below" figure, brief 03 §6); `multiagent-amplify.png` needs recaption (17.2x independent vs 4.4x centralized, not "17x vs single agent").

**New-ideas track (runs alongside, separate agents, output to `revision/ideas/`):**
candidate topics queued, not yet commissioned — (a) the context-budget chapter upgrade using vendor hard limits as evidence; (b) an "economics of the question distribution" section (head = flat marts, tail = explores, fail-closed beats silently-wrong); (c) the tooling-gap register (as-of joins, bitemporal SQL, OSI spec trajectory) as a "what to demand from vendors" appendix; (d) worked micro-colimit example with real schemas; (e) the multi-agent afterword — the book as existence proof of editor-coordinated, reflexive-loop knowledge production (brief 06 §5, author's call). *(Graduated from this track to Stage 2: the reflexive loop, now brief 06.)*

## Figure debt

| Figure | Action |
|---|---|
| `tax-300x.png` | Retire or redraw as "the agent picks; the engine joins" (brief 03 §6) |
| `multiagent-amplify.png` | Recaption/redraw: topology, not headcount, determines amplification (17.2x uncoordinated vs 4.4x orchestrated; pair with the +81% upside) |
| *(new)* reflexive-loop figure | Four loops as recursive cycle around the semantic layer — observed system → observing system (brief 06 §5) |
| `silver-vs-gold.png` | Check consistency with resolved Silver physical-shape position |
| All captions | Stage 4 audit against corrected claims |

## Risks

Chapter split may break `render_full_set.py` / `wire_figures.py` / `restructure_ch10.py` if they regex the monolith — `merge_book.py` is the shim; check each script in Stage 0. The de-crypto pass touches ~30 sites across 10 chapters; the continuity agent must re-grep (`crypto|BTC|wallet|MiCA|Bullish|staking|on-chain|coin`) after Stage 1 — note "crypto-shredding" is a cryptography term and **stays** (it's key destruction, not cryptocurrency), but its surrounding framing changes per brief 04.
