# Outstanding — as of 12 August 2026

## ⚡ ACTIVE CAMPAIGN — "By Any Means Necessary" (new ch10b) + book-wide energy pass

Opened 12 Aug 2026; **DRAFTED AND THREADED same night** (Iman delegated: "write
according to plan, fix according to plan").

**Done:**
- `chapters/10b-by-any-means-necessary.adoc` (~2,900 words, 7 sections): top-5-clients
  opening; contract-precedes-machinery + creole `trust`/`populated by` extensions;
  population spectrum + audition line; witness-by-evidence; trust grades as propagated
  taint; grafting onto governed Gold; "Not a Refinery. A Brain."; objection + E4 citation.
- Threading: ch02 (builder paragraph), ch04 (Bronze witness-transfer para), ch09 (scope
  sentence), ch10 (handoff ending), ch13 (Laws 22–25, "Full Ingest for Low-Stakes
  Insight" stop-spending entry, team-agents paragraph), ch15 (creole card `trust`/
  `populated by` + new "The Evidence Bundle" section w/ DDL), master include, proposal
  (89k words, 17 chapters, 25 Laws, new TOC entry, TradeBench/creole differentiator #6).
- Renders clean: 18 sect1, 0 warnings. AI-tells scan: in-family (17/1k dashes).

**Awaiting Iman's gates — all marked `//@ Q:` in the text:**
1. Title ruling (10b top) — "By Any Means Necessary" vs alternates.
2. Ops-flavored worked example (10b, after creole block) — confirm or re-dress.
3. One deliberate antithesis kept at "Not a Refinery. A Brain." — confirm per his rule.
4. hocolim question (ch11 Formal Spine) — riff or thesis; nothing written.
5. Laws 22–25 wording certification (ch13).
6. 10b figure (marker at top) — blocked on OpenRouter top-up like the other pictures.

**Still to run: the book-wide energy pass** — chapter-by-chapter close read with Iman
(no agent fleets; Rawiya + Iman directly), injecting his renewed conviction. Not started;
10b sets the register.

---

# Previously outstanding — as of 17 July 2026

The book was submission-ready as of this date. On 17 July a full-manuscript readability/waffle pass ran
(11 parallel close-reads → `revision/readability-report.md` → all findings applied): −5,673 words
(92,092 → 86,419) with no arguments lost, the creole intro re-cut to two confident sentences
(platform neutrality + not dating the book), seven other over-justified passages compressed,
cross-section repetition deduped book-wide, and a crop of real bugs fixed (meaning-inverting
typo in ch02, broken hyphenation inside ch12's creole block, three-vs-four "position"
inconsistency, ch07 stats contradiction, citation defects).

Also executed the same day (previously "approved in principle"):

- **ch01 formalism relocation — DONE.** "Intellectual Foundations" is now the
  **"Foundations and Sources"** essay (`chapters/15b-foundations-and-sources.adoc`, between the
  Engineer's Appendix and References); ch01 keeps one confident pointer paragraph carrying the
  prose-over-OWL conclusion. Kimball/Inmon/Dehghani deduped against ch04's "Where Serious People
  Disagree". Crossley/Poernomo reference annotations shrunk to bare citations (essay owns the
  narrative now).
- **Worked examples — DONE.** Pushout analogy (org charts merging after an acquisition) now
  opens the formal treatment in both ch03 and ch04, with a callback at the colimit definition;
  ch12 gained **"One Incident, End to End"** — the April `net_revenue` restatement replayed
  Monday→Thursday through all four loops, with the old fragments compressed to pointers.
- **Fact-checks — DONE.** Stojanovic 2004 completed (single-author Karlsruhe thesis; ch12 in-text
  cite fixed to match); Strategy benchmark reconciled to 2026 in both ch15 and ch16; Anthropic
  (2026) entry got its URL; Roelant Vos bitemporal source added to References.

Full build verified with asciidoctor after the pass.

## Open items

1. **Ontology pictures (2–3, R2 register)** — still blocked on OpenRouter top-up (~$36 left):
   - the pushout drawn (ch03/ch04) — the org-chart analogy in the text now gives the artist brief;
   - the prime-brokerage witness (ch11 — insert immediately after the commutativity worked
     failure, before the "Gluing schemas glues instances" theorem);
   - optional: bridge anatomy.
   Generate via `render_missing_figures.py` pattern.
2. ~~Spelling normalization~~ — **DONE 17 Jul**: normalized to American (73 conversions,
   curated word map, render verified).
3. **Small flags from the fact-check pass:**
   - ch16 Anthropic (2026) annotation says "Comprehension 50% vs 67%" while coverage describes a
     17% mastery drop — verify the gloss against the paper on the before-press pass.
   - ch16 carries `// TODO before press: confirm every entry against its current published version`.
   - ch16 ordering: implicit thematic order, no headers — alphabetize or add subheads (deferred).
4. **Author reads the fresh PDF cover to cover** — now doubly worthwhile: the waffle pass touched
   every chapter. Push triggers the Action build (Actions → newest run → Artifacts). Especially:
   ch12's new "One Incident, End to End", the new Foundations and Sources essay, the recut creole
   intro (ch04), the pushout analogy (ch03/ch04), ch07's rebuilt ending, ch08's two new dated
   sidebars.
5. **Top up OpenRouter** (~$36 remaining of $1,605 lifetime).
6. **O'Reilly submission** — `proposal/oreilly-proposal.md` is complete. Consider adding one §5
   differentiator line: *"the book's empirical claims ship with a public, reproducible experiment
   harness (TradeBench)"* — and arguably a line about the creole. Then: warm intro to an
   acquisitions editor if the network yields one; else proposals@oreilly.com with ch02 "The
   Shift" as the sample chapter.
7. **Team presentation** (the original second goal) — the Playbook + Laws + Appendix + TradeBench
   repo are the deck.

## Smaller / parked

8. **Creole conversions, remaining:** ch04/ch12/ch15 done; scan other chapters for stray
   conceptual notation on the next pass. Optional: add a `.creole` twin of TradeBench's
   `semantic_layer.yaml` to the public repo.
9. **Audiobook** — full cheap review render DONE 18 Jul (16 chapters incl. the new essay,
   ~10.6 h, `eleven_turbo_v2_5`, ~165k credits; MP3s in `audiobook/out/review/` + Desktop copy).
   Re-render after edits is incremental (chunk cache): `audiobook/scripts/render_review.sh`.
   The *production* audiobook (eleven_v3, two-voice cast, music beds) remains future work.
10. **Repo housekeeping:** old review docs (`the-semantic-enterprise-review*.md`,
    `pdf-vs-adoc-comparison.md`) could move into `revision/`; `figure-map.md` is slightly stale.
11. **PDF weight:** 32 MB (figure PNGs). A compressed sharing copy (~8–10 MB) is a 5-minute job
    on request.

## Standing editorial rules (apply to all future passes)

- Manifesto voice; intermediate-long phrases; filler/repetition hunt.
- **Antithesis rule:** the Y is the insight — cut the "not X" unless X is a genuinely held
  misconception being corrected.
- **Waffle rules (added 17 Jul):** state a design choice's motivation once, confidently — never
  paragraphs of justification; one telling per point per chapter — dedup cross-section
  restatements; no paragraph-ending sentence that restates the paragraph.
- **Perishability policy** (`revision/perishability-policy.md`): dated sidebars for volatile
  claims; mechanism-level claims in prose.
- **No draft-self-reference:** the reader's book has no history.
- **Register-match inventions:** the creole is pseudocode, used confidently, fussed over never.
- Em-dashes: settled at the principled-pass level (ch02); leave the rest.
- TradeBench numbers: any new figure entering the book needs a run in the committed harness
  and the author's sign-off.

## Where everything lives

- Book: `github.com/thegoodtailor/semantic-enterprise` (chapters/ is the source; Action
  builds PDF+HTML per push — Actions → newest run → Artifacts).
- Experiments: `github.com/thegoodtailor/semantic-enterprise-experiments` (public, reproducible).
- Companion paper: subsumed into ch11; `enterprise-colimit` repo is archival.
- Proposal: `proposal/oreilly-proposal.md`. Conventions: `revision/editorial-conventions.md`.
- Waffle pass: `revision/readability-report.md` (findings + what was applied).
