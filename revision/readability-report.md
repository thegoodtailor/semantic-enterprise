# Readability & waffle report — full-manuscript pass, 17 July 2026

Eleven parallel close-reads of chapters 1–16, in waffle-detector mode per the author's brief:
circular/redundant sentences, and especially **over-justified motivation** (the creole intro as
type specimen). House rules applied: manifesto voice, antithesis rule, perishability policy,
"used confidently, fussed over never". Line numbers are as-of the 16–17 July files.

---

## Executive summary

1. **The dominant defect is not sentence-level waffle — it is cross-section repetition.**
   Almost every chapter is tight paragraph by paragraph but makes its core points 2–6 times
   across sections. The fix is de-duplication (keep the best telling, cut or pointer the rest),
   not sentence surgery. Estimated trim: **10–18% per chapter, roughly 10–12k words book-wide,
   with no loss of argument.**

2. **The creole intro is found and diagnosed** — ch04 lines 217–245. Five sentences of
   linguistics theory (pidgin vs. creole, communities living together, native speakers) plus a
   second apology at 245 ("It is pseudocode, nothing grander..."). The *actual* reasons —
   platform neutrality, not dating the book — are never stated. Two-sentence replacement drafted
   (§ch04 below).

3. **The same over-justification pattern recurs in seven other places** (the "creole pattern"):
   - ch01 34–36: eight sentences defending prose-over-OWL
   - ch03 227–233: pushout defended with credentials + name-etymology + triple recap
   - ch06 111–123: "name the three temporal modes" justified four separate times
   - ch07 88–90: nine sentences of MCP history for a protocol the next paragraph calls a detail
   - ch09 205–209 and 217–221: three paragraphs defending "the schema file is the LDM", three
     more anticipating the vendor objection
   - ch13 33+57–59: "you don't need consultants" made three times
   - ch15 117: the compile-down mapping re-justified after the card already demonstrated it
   Each has a drafted one-to-two-sentence confident replacement below.

4. **Structural findings worth deciding before the edit pass:**
   - **ch07 ends three times** (213, 219, 221–223); the bypass-erosion paragraphs land after the
     emotional close and kill it — move the VP vignette up to line 145 and cut from the ending.
   - **ch12 worked example (approved item 3b)**: the planned Monday→Thursday incident already
     exists in fragments at lines 110, 118, 154, 162. Write it as the **consolidated replay of the
     same April `net_revenue` incident** (slot: after line 176, before "Prior Art, Honestly") and
     compress 110/118 to pointers — a new incident would be a fifth telling.
   - **ch01 Intellectual Foundations is nine paragraphs, not seven** (lines 22–38; 36 and 38
     continue 34's prose-vs-OWL position and must travel together). The pointer paragraph left
     behind must carry the *conclusion* (domain essays, not OWL; the consumer shifted from
     symbolic reasoners to LLMs), since the book uses that position later.
   - **Foundations and Sources essay slot: between ch15 and ch16** (ch14 must stay the last word
     of the argument). Once it exists, ch16's long annotations on the Crossley/Poernomo entries
     should shrink to bare citations, and it should absorb the Vos/Snodgrass sourcing note.
   - **Pushout analogy (approved item 3a)**: primary insertion ch04 between lines 315 and 317
     (opening the formal run, so category→functor→colimit lands on a familiar picture), with a
     callback at 339; in ch03, open line 231 with it, replacing the etymology walkthrough.
   - **ch11 witness figure (approved item 2b)**: belongs immediately after line 47, before the
     "Gluing schemas glues instances" theorem at 49.

5. **Hard bugs found incidentally** (fix regardless of the waffle pass) — see final section:
   meaning-inversion in ch02, broken hyphenation inside ch12's creole block, a three-vs-four
   inconsistency in ch03, a stats contradiction in ch07, citation defects in ch16, British vs
   American spelling split (ch05 vs ch01).

6. **Perishability violations in prose** (policy: dated sidebars for volatile claims):
   ch08 lines 186/211/243 (HAL numbers, dbt/AtScale/Snowflake percentages, SWE-bench arc,
   Wolters Kluwer, Karpathy); ch09 lines 99/103 ("maps lineage in minutes — accurately",
   "mid-nineties as of this writing").

Per-chapter trim estimates: ch01 ~10% outside the relocating section · ch02 10–12% · ch03 15–18%
· ch04 10–14% · ch05 ~10% · ch06 12–15% · ch07 12–18% · ch08 15–20% · ch09 15–20% · ch10 8–10%
· ch11 3–4% · ch12 ~5% · ch13 8–12% · ch14 ~10% · ch15 ~5% · ch16 prose-clean (structural fixes only).
Tightest: ch11, ch12, ch15. Heaviest: ch03, ch08, ch09.

---

## ch01 — Introduction

Verdict: manifesto frame (3–18) and close (40–50) strong; the problem is Intellectual
Foundations, which is dense *and* internally redundant. The approved relocation fixes pacing at
a stroke.

- [34–36] OVER-JUSTIFIED + ANTITHESIS — eight sentences defending prose-over-OWL, incl. "This is
  not a regression... It is a format shift". Replace with: *"The dominant machine consumer of
  documentation has shifted from symbolic reasoners, which process OWL, to LLMs, which process
  natural language. OWL was correct for its consumer; prose is correct for this one — the same
  consumer-shift argument this book makes everywhere else."*
- [22–24] CIRCULAR — pushout-gluing explained three times; keep 22's plain-language statement,
  open 24 at "This is the construction I developed with Crossley and Wirsing..." (fix in the essay).
- [24] DENSITY — the ~200-word lineage paragraph (WADT'99, Spivak); split at Spivak in the essay.
- [7] HEDGE — three defenses of uneven adoption where one suffices: *"Adoption is arriving
  unevenly — pilots in most organizations, production in a few — but the direction is one-way:
  the organization not building for the agentic consumer is on the wrong side of an existential
  threat."*
- [26] (essay version) trim to "The relabeling into practitioner language is deliberate."
- [5] "built for or 'self-served' by her" → *"built for her — or self-served by her."*

## ch02 — The Shift (O'Reilly sample chapter — highest bar)

Verdict: strong; three core arguments each made three times: (1) humans compensate / agents
don't, (2) density beats volume, (3) the economics flipped both directions. 10–12% trimmable.

- [16] keep first sentence of "In every case, the fix was the same..."; cut sentences 2–3.
- [93] repeats line 36's economics → *"Context cost is measured in reasoning quality per token,
  not in tokens — and those economics run in one direction, hard."* (or cut entirely).
- [158–166] human-compensates contrast ×3: keep the 158–160 dramatization; at 162 cut last two
  sentences; at 166 keep only "Every ambiguity... becomes a potential hallucination" + final sentence.
- [181] end at "Epistemic honesty... is a feature of the infrastructure, not of the model." Cut
  the sentences before and after.
- [217] cost-exceeded-benefit ×3 → *"This is the kind of infrastructure that has been on every
  Chief Data Officer's roadmap for a decade — and it kept losing the quarterly prioritization
  meeting for a rational reason: while the primary consumer was a human who could squint, the
  cost was not justified by the benefit."*
- [235 vs 219–221] → *"Information architects have been arguing for governed vocabularies for
  decades. They were right. They were also right to be ignored — until AI broke the calculation
  in both directions. The lines have crossed."*
- [72] scenario recap replay → *"Same model. Seven hundred fewer tokens, dramatically more
  meaning per token. The difference between wrong and right was better context, not more of it."*
- [87] cut the 200,000-token sentence (restates 34's illustration).
- [34] degradation asserted ×3 → *"The model does not process its hundredth token with the
  fidelity it applies to its tenth; long-context degradation is well-attested. Denser context
  beats more context."*
- [91] cut "The deficit does not degrade gracefully. It becomes failure."; trim final clause.
- [9] → *"The model was smart enough. The failing terms were not obscure; nobody had written a
  definition and put it where the AI could read it."*
- [25] cut "The model is the same model. The infrastructure changed." (pre-empts 72's punch).
- [36] cut "Density is the hinge of that argument too."
- [221] cut "That changes the prioritization calculus dramatically."
- [213] muddle ("postman"; "data *is* the deep thought" is circular) → *"Any intelligence —
  human or frontier model — needs memory. In an enterprise, data is that memory: the
  precondition of thought, not raw material thought acts on afterward."*
- [257] cut "You cannot skip it because the system will not let..."
- [269] cut "If a machine cannot reason about it, it is incomplete."
- [7] cut ", with no canned responses, no tricks".
- Note: the creole over-justification is **not** in ch02.

## ch03 — Language Is the Material

Verdict: sentences strong; architectural echo — every major point made 2–4×. Pushout passage is
the ch03 analogue of the creole problem. 15–18% trimmable. (The creole notation itself does not
appear here.)

- [227–233] OVER-JUSTIFIED — three ~200–250-word paragraphs re-establish trading/finance
  polysemy (4th occurrence) around the pushout, with credential drop + etymology + closing recap.
  Open 231 with the org-chart analogy: *"When two companies merge, nobody unions the org charts —
  you identify the people both charts already name, pin them down once, and let each side's
  structure fan out from that shared spine. That construction has a name: the pushout."* Cut the
  etymology sentence and 233's closing recap; keep the credential drop OR "not reaching for a
  metaphor", not both. ("draws blood" already used at 178.)
- [128–131, 151, 167–171] "Upstream always wins" stated **six times** (130, 134, 151, 165, 167,
  169, 297); 130 internally circular (four castings of one rule). Keep 130's first two sentences
  + "nowhere to drift to"; in 151 cut after "the same definition" except the enforcement
  sentence; cut 169 entirely; keep 171's "Governance by committee is governance by nostalgia."
- [128] compress $14M/position re-narration to callbacks; **reconcile position = three meanings
  (29, 128) vs four desks (227)**.
- [184–196] linguistics subsection re-defines synonymy/polysemy/compounding from 178; 196's
  job-posting remakes 182's hiring point. Cut 186–192 to one paragraph (keep only the "pick one
  and rename" mistake + German-noun gloss); merge 194–196.
- [85–95] osmosis/"the book"/three-revenue-definitions repeated across 76, 85, 89, 93. Cut 89
  entirely; in 93 keep only "the cross", the 4pm snapshot, and the plateau sentence.
- [74–78] same rhetorical move ten lines apart; keep 78's anaphora, compress 74 and 76.
- [97–99, 163–165] anchors-index-essay stated ×4; fold 99 into 97; merge 163+165.
- [35] cut (restates 33); at 190 keep only the compounding gloss + "not individually addressable".
- [145–149] separate-artifacts-diverge ×3; keep 145's story + 149's objection; cut 147's second sentence.
- [206–210] knowledge-in-heads ×4; keep 206's Ask Sam/Ask Keith + 208's quote; cut 208's final
  sentence and 210's first two.
- [58] cut the whole paragraph ("not a niche problem" corrects nobody).
- [237, 255] four-register enumeration twice in full; keep 255, compress 237 to one sentence.
- [264] cut the self-referential type-system parenthetical.
- [243] → *"Definitional broadening — 'position: a quantity of an asset held or owed by an
  entity' — covers everything and means nothing."*
- [155] cut the final label sentence.
- [286] fourth statement of agent-has-only-what-you-give → *"Always true; AI makes it undeniable.
  A human asks someone — an AI either guesses or fails, and if the name misleads it is
  confidently wrong."*
- [295] end the item at "or delete it."

## ch04 — The Architecture

Verdict: set pieces tight; waffle is structural — doctrines restated in full across sections,
plus a paragraph-ending habit of restating the point in a second summary sentence. 10–14%.

**THE CREOLE INTRO (lines 217–245).** Line 219: five sentences of linguistics theory; line 245
re-apologizes ("It is pseudocode, nothing grander; the point is only that..."). Platform
neutrality and not-dating are never stated. Replace 219 with:

> *"Declarations need a notation, and tying it to any vendor's syntax would date this book, so
> declarations here are written in pseudocode in the algebraic-specification style, English
> definitions inline — call it the creole: algebra supplies the grammar, English the vocabulary.
> It maps mechanically onto whatever transformation tool and semantic layer you actually run."*

At 245 delete "It is pseudocode, nothing grander; the point is only that" → keep as *"The
engineer who reviews it, the mesh that checks it, and the agent that loads it as context all
read the same text."* Keep the rest of 245 (reading guide + sketch/arrow/cone mapping) — content,
not fuss.

- [89, 158, 187] two-surface Gold doctrine stated in full ×3; keep 187, compress 89 to a
  forward pointer, keep only desk-level concreteness at 158.
- [61, 73, 75] SCD2 defined three times in fifteen lines; define once at 61.
- [63 vs 148–150] Kimball row-store-era rationale argued twice; keep 148–150, compress 63 to one
  sentence.
- [341–345, 388–392, 451–459] unified-model-fails-structurally ×3; Finishability internally
  circular → *"Information architects were trying to build a colimit — one model capturing all
  domain vocabularies with a canonical resolution for every shared concept. It never shipped
  because a colimit over a moving target cannot be computed manually. The goal was correct; the
  maintenance model was lethal."*
- [154 vs 303] engineer-star-schema anecdote told twice; at 303 use a back-reference.
- [331 vs 467] ten-incompatible-joins claim twice; keep 467.
- [267 vs 512–538] Collibra dissent pre-delivers the entire MDR section; at 267 keep only a pointer.
- [179 vs 181] feature-store warning closes both paragraphs; cut the 181 version.
- [123–125] easy/hard formula restated; replace 125's restatement with the consequence.
- [136 vs 175] "If you cannot state the question..." verbatim twice; cut at 136.
- [167–171] explore mandate ×3; merge 167+169, let 171's code-without-tests line carry it.
- [317–319] category theory reassured three times; cut "The result is the same." and "The term
  sounds intimidating; the idea is not."
- [362–364] two back-to-back antithesis pairs; keep "One is a query. The other is architecture."
- [366 vs 313] bespoke-integration claim verbatim; cut 366's first sentence.
- [273–275, 384] mesh-lacks-composition re-argued; end 275 on "That is a damning self-assessment."
- [341, 345, 443] acquisition/regulation triple ×3; cut the examples at 345.
- [144–146] double wind-up; cut "This contradicts what most practitioners learned..."
- [30, 53, 117, 392, 398, 34, 87] single-sentence cuts (closing-sentence restatements, empty
  intensifiers) — see agent notes; all mechanical.
- Dedupe targets vs ch01 relocation: lines 57–67 (Kimball/Inmon), 251–257 (Reis/Kaminsky/Tabb),
  275 (Dehghani self-assessment).
- Pushout analogy insertion: between 315 and 317; callback at 339.

## ch05 — Exploring the Glued Ontology

Verdict: tight; waffle localized. ~10%.

- [30] full paragraph re-justifying live composition; cut to its last sentence, relocated to
  close the intro (line 7): *"Live composition of the colimit means no pre-built mart and no
  rogue join — every hop through machinery that already knows what the words mean and who may
  see them."*
- [32] re-runs the line-11 session; fold the register switch into 11 and the `restricted` cell
  into 28; cut 32.
- [28] rule stated ×3 in one paragraph; cut the final restatement (or keep only "The system says
  so out loud rather than guessing").
- [5] cut "Both are real and both are covered."
- [7] "has a name in this architecture" drumroll → *"That capability is the consumption face of
  the colimit."*
- [32, 38] "earns its keep" twice in six lines; keep one.

## ch06 — Time

Verdict: core sections strong; waffle in three places. 12–15%, mostly paragraph merges.

- [111, 119, 121, 123] **creole pattern**: "name the three modes" justified four times. Keep 111
  + 119's first two sentences; cut 121 except grafting *"Naming is an epistemic commitment: the
  system declares what it is claiming"* onto 119; cut 123's final clause.
- [65–67] dbt/snapshot point at full length twice; merge (keep 65's framing, 67's dbt evidence +
  bolded principle; cut the aphorism, the KYC replay, and the dbt Discourse citation). ~40% of
  the two paragraphs.
- [168–172] confident-wrong-answer remade ×3 after 36+40 already landed it; keep the anecdote
  (172), cut 170's second half and 172's closing caption.
- [148–150] example re-run; merge the market-data instance into 148, keep only 150's closing
  sentence (replacing "Space is cheap").
- [81–83] → keep 81's epigraph; compress 83 to *"The scaffolding earns its cost the first time a
  correction flows through without losing history, without rewriting published outputs, and
  without confusing any consumer about which truth they are looking at."*
- [27, 36, 97] regulator/risk mapping ×3; keep 36 and 97; compress 27 to one sentence.
- [29–31 vs 85] compress 85 to a two-line pointer + the April 2 specifics.
- [93 vs 107] merge 107's cost specifics into 93; cut 107; let line 190 own the letterhead question.
- [97, 101] cut 101's repeated cadence; [115] cut the two meta-restatements; [75] end on "the
  answer is gone."; [174, 176] morphism glossed ×3 — keep 174's; [180] cut middle sentence;
  [18] cut the fragment; [59, 61] "storage is cheap" twice — compress per agent text; [73] cut
  the announcing first sentence.

## ch07 — The Death of the Dashboard

Verdict: strong momentum; ~6 major points each made fully twice; platform-neutrality defended
three times; **the chapter ends three times**. 12–18%.

- [215–217] STRUCTURAL: bypass-erosion duplicates 145 and lands after the emotional close at
  213. Move the VP-with-a-deadline vignette up to replace the abstract version at 145 (keep
  "political will is the scarcest resource" there too); cut both paragraphs from the ending so
  213 flows into 219.
- [88–90] **creole pattern**: nine sentences of MCP history → *"MCP — Anthropic's open standard
  for connecting models to tools and data, adopted across the industry within eighteen months —
  validates the pattern: the agent reaches through a governed layer for exactly what it needs,
  when it needs it. But the protocol is a detail. MCP may be superseded within five years; the
  principle — agents access data through a governed semantic layer, never through raw SQL — will
  survive every successor."* Also cut 86's protocol-interchangeability sentence.
- [54 + 159] self-service ~30% stats near-verbatim twice → at 159: *"'Self-service BI will get
  better.' Twenty years of dramatically better tools have not moved adoption past thirty
  percent. The tooling was never the problem; the assumption was."* (Also: 159's "single-digit
  percentages" contradicts 54's "thirty-two percent of executives" — cut the fragment.)
- [119 + 171] text-to-SQL rebuttal twice; at 119 keep one sentence ("The semantic layer converts
  an unreliable technology into a reliable one."), 171 carries the full version.
- [58–60] widget knowledge-trap twice; keep 58; in 60 keep opener + vacation line only.
- [32–36] analyst-bypass ×3; in 36 cut after "Always locally correct and globally destructive."
- [74 + 92] flat-Gold territory re-covered; merge 92's new content (head/tail routing as cost
  decision) into 74.
- [155–157] third airing of chatbot-on-dashboard → one paragraph (position quote + "automated
  confusion" + carriage image).
- [70] → "Three components replace the dashboard-centric model." Cut the stack-agnostic defense.
- [169 + 209] doom loop twice; keep 169, compress 209 to one sentence.
- [9 + 207] same closer twice; cut at 207.
- [129] "not an afterthought" → *"Provenance is an architectural requirement."*
- [54, 131, 62, 20] single-sentence circularity cuts per agent notes; fix 131's "squinting at a
  chart" echo of 123 ("reverse-engineering a filter").

## ch08 — Agentic Intelligence (recently rebuilt — heaviest load)

Verdict: spine strong (DDL sidebar, newsroom, closing section); middle and last third heavy with
repetition — warehouse-is-memory, confidently-wrong, FSB/FINRA, guessing-vs-grounding, virtuous
cycle each made 2–6×. 15–20%.

- [74, 285] FSB 2026 / FINRA / "synthetic employees" / "know your agent" — **a full duplicated
  paragraph**. Keep 74; at 285 open with *"The regulatory pressure described earlier — documented
  agent identifiers, audit trails, 'know your agent' — lands here."* Keep the EU AI Act material
  (285 only).
- [211, 263–265] same OpenAI hallucination paper cited twice with the same takeaway; keep at
  265; at 211 keep only the tenured-professor closer.
- [247, 259, 289] "AI doesn't work → your data isn't ready" beat run three times; keep 247's
  full version, compress the others.
- [108–110] register-is-cognitive-configuration ×5 → one sentence: *"The register is a cognitive
  configuration, not a filter: an agent in the Finance register and the same agent in the
  Trading register are different reasoners."*
- [118–122] system-prompt equation ×3 → *"A domain's Gold definitions, tutorial documentation,
  quality signals, and heuristics function as a system prompt for the agent — literally, not as
  a metaphor. Garbage definitions in, garbage reasoning out."* 122 stands as payoff minus its tail.
- [29–33] two consecutive "Memory means..." paragraphs; merge; RAG treatment belongs at 76.
- [33, 70, 76, 283] vector-store-is-not-memory ×4; keep 76 (cache/mind) + 283's clause.
- [235, 295] virtuous-cycle formula twice; keep 295 (paired with the doom loop).
- [80–82] two consecutive metaphors for MCP-is-mechanism; keep the plumbing triplet, cut
  microservices.
- [186, 211, 243] PERISHABILITY: benchmark clusters in prose (HAL, dbt/AtScale/Snowflake,
  SWE-bench, Wolters Kluwer, Karpathy) → move to dated sidebars, one mechanism sentence each in
  prose.
- [90/92, 188/190, 78, 269, 114, 15, 138/142, 255/7, 257, 265, 281, 287, 23, 233, 198–200]
  mechanical cuts and compressions per agent notes (closing-sentence restatements, re-derived
  definitions, hedge pileups, stacked antitheses).
- Motif note: "confidently wrong" appears ≥6 times; keep the tenured-professor (211) and
  silent-failure (90) instances, lean the rest on them.

## ch09 — Building with AI

Verdict: paragraphs tight; same half-dozen points made 2–4×. 15–20%, almost all de-dup.

- [205–209 + 217–221] **creole pattern ×2**: three paragraphs defending "the schema file is the
  LDM" against the dbt community + three more anticipating the vendor objection. Cut 205; open
  207 with the three-tier statement; compress 217–221 to: *"Unity Catalog, Snowflake Horizon,
  and Google's catalog embed governance into the platform — but they retrofit it: governance by
  integration, not by construction. Governance by construction is a property of how you
  structure your project, what standards you apply, and what AI monitors — it lives in your
  architecture, not your vendor's feature set."*
- [127 + 215] schema-can't-carry-tacit-knowledge ×3 in 127, remade at 215 → compress 127
  (*"Essays are not generated from schemas: a schema-generated essay is, by construction, no
  better than the schema. AI can draft, structure, and flag staleness, but the knowledge is
  human..."*); at 215 keep only the revenue example.
- [129 vs 139] morphism essay previewed then delivered ten lines later; cut the preview's middle.
- [97–101 + 241–243] consultants/pattern-recognition ×3; cut 101 (also fixes the
  minutes-vs-weeks inconsistency); trim 243.
- [85–95] failed-dictionary story retold; cut 95 except its final sentence appended to 93.
- [251, 255, 257, 259, 267] judgment-over-labor ×4 + leader-keeps-teeth ×3; keep "The scarce
  resource is quality of thinking... hands to heads", merge 257 into 259, compress 255.
- [7 + 21 + 66] thesis sentence ×3 near-verbatim; keep 7; end 21 at "formally complete,
  operationally dead."; cut 66.
- [5, 187, 277] ANTITHESIS TIC — recurring "not because the people were bad / negligent /
  committees bad"; rewrite per agent notes (drift is the natural state; the environment outgrew
  committee speed).
- [121] cut the "To our knowledge no practitioner book..." novelty hedge.
- [99 + 103] PERISHABILITY: lineage-accuracy capability claims in prose → mechanism-level
  phrasing; move the mid-nineties figure to a dated sidebar or cut.
- [78/151/271] "never sleeps" ×3 — keep caption + 151; [167/263/271] definitions-bound-your-AI
  ×3 — keep 167 + the guesses/grounds sentence; [32] "intrinsically unfinishable" ×3 → single
  formulation; [143 + 177] cut both drumroll openers; [183/187, 233–237] cut retellings.

## ch10 — The Sandpit

Verdict: strong voice; the middle circles. 8–10%, almost all from lines 14–38.

- [20–24] feature-metadata inventory enumerated ×3 (questions, published metadata, registration
  fields); keep 20 + 24, compress 22.
- [30–34] "layer documents but doesn't mediate training" ×3; cut 34 except the latency clause,
  folded into 32.
- [36, 16, 38, 52, 62–66] cut announcing openers, restated distinctions, and the third
  speed-or-bypass telling per agent notes.

## ch11 — The Living Colimit (tightest chapter)

Verdict: formal spine reads as intended. 3–4%.

- [3, 29, 57] buildability sold four times; in 3 cut "— and it is open to be built now, with the
  tools already on the shelf." (Shipping It Within a Year owns the claim); end on "category
  difference, not a feature difference."
- [20] four phrasings of mesh-is-real-infrastructure → *"The mesh is load-bearing infrastructure
  — large, failure-prone, and needing its own operations and observability. Designed, not waved
  at:"*
- Witness figure (approved item): after line 47, before the theorem at 49.

## ch12 — The Reflexive Loop (best-voiced; creole used exactly per house rule)

Verdict: ~5% trimmable; echo-repetition only. **Two hard text bugs.**

- [45–46, 65–66] BUG: broken hyphenation inside the creole source block — "mark-to-m arket" and
  "wind-d own" will typeset literally. Rejoin and rewrap.
- [108] excellent paragraph with three closers; keep two at most (end at "...re-created the
  failure the whole architecture is built to prevent").
- [36] indictment contrast stated twice in one paragraph; keep the sharper second version.
- [122–124] re-argues line 24's external-and-plural principle; invoke, don't re-establish.
- [150–152] certification-vs-survival made twice; keep 152's aphorism.
- [158] near-verbatim repeat of line 9 → lean on the loss: *"Refutations land; definitions are
  revised; overwrite them in place and the system destroys the evidence of its own learning."*
- [22] "queryable, calibrated, bitemporal" repeats line 9 within 13 lines; vary.
- [34] trim to "Data tests guard the pipeline while nothing guards the meaning." (low severity).
- **Worked example (approved item)**: consolidated Monday→Thursday replay of the existing April
  `net_revenue` incident, after line 176; compress 110 and 118 to pointers into it (162 stays).

## ch13 — The Playbook

Verdict: Laws and checklists tight; the closing sections re-argue what the body argued. 8–12%.

- [330–336 + 407] ISO-catalogue verdict run twice near-verbatim 70 lines apart; keep 330–336;
  compress 407 to one sentence.
- [213–217 + 401] slow-intake-breeds-bypasses ×4; cut 217 to its last sentence; trim 401.
- [168–176 + 444–446] Regulatory Case repeats Defensive/Offensive point-for-point; shrink
  444–446 to the EU AI Act dates + one pointer sentence.
- [33 + 57–59] **creole pattern**: "you don't need consultants" ×3; cut 57 entirely — 59's
  Gartner/McKinsey/Deloitte roll call carries it.
- [425–433, 458] fifty-slide line ×4 (incl. verbatim figure caption); rewrite the caption as a
  label ("The board presentation: three sentences, one page."); keep 427 + 458.
- [120, 176, 314, 438] months-compress-to-weeks ×4; keep at 120 (has the specifics) and 438.
- [92, 231, 254–256, 152–156, 342–348+403, 409, 360–364, 370–372+393, 262, 65+72, 462, 110]
  mechanical compressions per agent notes (triple-stated theses, repeated jokes — the holiday
  joke told twice dies — softened restatements, the 190-word mitigation paragraph at 409 cut to
  two sentences).

## ch14 — No Walls (coda)

Verdict: close to earning it line by line. ~10%.

- [3] one-answer-vs-all-answers made ×3 → *"Solve it, and the real question arrives: what is
  more interesting than one answer? A thousand — every pathway of interconnected data, the
  models, the sandpits, all the knowledge at once. One answer is the floor; a mind turned loose
  on the whole estate is the ceiling."*
- [5–7] caption pre-states the body's climax formula and ends on a dangling "not a gate" →
  *"'No walls': fencing the chatbot while every other consumer walks straight in is theatre. The
  estate is open by design."*

## ch15 — The Engineer's Appendix

Verdict: genuinely disciplined; the creole card intro (94) obeys the house rule perfectly. ~5%.

- [117] **creole re-justification** — "Nothing in the mapping is clever. That is the point..."
  after the mapping already demonstrated it; the causal opener is also logically backwards
  (more meaning makes compile-down lossy, not mechanical). Open with *"The compile-down is
  mechanical."*, keep the list, close with only *"The thinking happened in the creole, once,
  where all three readers — engineer, mesh, agent — could see it."* Also shrink the duplicated
  asof-rule parenthetical to "(equality-key where the tool supports only that; `asof` per the
  rule above)".
- [90] four sentences saying two things; compress per agent text (authored once in the MDR;
  build-verified copies, never paraphrased).
- [3] two clauses defending printed dated numbers → *"One dating note before the numbers: every
  vendor limit, engine capability, and product figure below is the state of the tooling as of
  mid-2026. The disciplines they illustrate are not dated."*
- [121] "not a heuristic awaiting a benchmark" — invented antithesis → *"...the same constraint
  published as product limits: context per token is a budget both platforms already enforce."*

## ch16 — References

Verdict: prose-clean; four structural fixes.

- Implicit thematic order with no headers reads as no order — either alphabetize or add thematic
  subheads (dovetails with the Foundations and Sources essay).
- [73] "confirm each against its current published version before press" is an author-facing
  production instruction in reader-facing text — move to a TODO comment / production checklist.
- [47] Stojanovic entry lacks venue; [65] Anthropic (2026) lacks a locator.
- Missing entry: Roelant Vos (load-bearing in ch15 line 44).
- Cross-file: ch15 says Strategy benchmark **2025**, ch16 says **2026** — reconcile to the real year.
- Once the essay exists: shrink the Crossley/Poernomo annotations (lines 9–13) to bare citations.

---

## Bugs & inconsistencies (fix regardless of the waffle pass)

1. **ch02:166** — "the dashboard could tolerate the mess because the human using it could not"
   inverts the meaning → "because the human using it compensated." (Probable typo.)
2. **ch02:213** — "human, postman, or frontier model" — typo or private joke; rewrite.
3. **ch03** — "position" fractured into *three* meanings (29, 128) vs *four* desks (227): reconcile.
4. **ch07:159** — "single-digit percentages" contradicts 54's "thirty-two percent of executives".
5. **ch09:99/101** — lineage mapping "minutes" vs "weeks" in adjacent paragraphs.
6. **ch12:45–46, 65–66** — broken hyphenation inside creole source strings ("mark-to-m arket",
   "wind-d own") — will typeset literally.
7. **ch05:38** — stray closing quotation mark after "write."
8. **Spelling split** — ch05 (and possibly others) British ("materialise", "organisation") vs
   ch01/ch02 American ("optimized", "organizations"). O'Reilly will force one; pick now (suggest
   American).
9. **ch15 vs ch16** — Strategy benchmark dated 2025 in one file, 2026 in the other.
10. **ch16** — production instruction in reader-facing text; incomplete citations; missing Vos entry.
