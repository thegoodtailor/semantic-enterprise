# Book Proposal — *The Semantic Enterprise: Data Architecture for the Agentic Era*

**Author:** Iman Poernomo
**Submission to:** proposals@oreilly.com
**Status:** Complete first draft (~90,000 words, 18 chapters incl. appendix), written in AsciiDoc/Atlas-ready format, with 32 original figures. Manuscript and CI build available on request.

---

## 1. The one-line pitch

Your data platform was built for a consumer who should no longer exist — the human analyst who could squint at a messy dashboard and figure it out. The new primary consumer is an AI agent that cannot squint, cannot call a colleague, and answers wrong with perfect confidence when your semantics are ambiguous. This book is the architecture for the consumer that cannot compensate.

## 2. Summary

For thirty years data architecture was optimized for a smart human who compensated for bad infrastructure. That compensation is gone. The agentic consumer reads your column names, your definitions, and your documentation literally, and operationalizes every ambiguity at machine speed and four decimal places of false confidence.

*The Semantic Enterprise* is the practitioner's architecture for that shift. It is opinionated, argued, and immediately buildable: it tells a data leader what to build Monday, what to stop funding, and why. Its spine is a claim most "AI + data" books miss — that the binding constraint on an agentic data platform is not context-window size but **information density per token**, and that everything else (how you model tables, document domains, expose data, govern meaning) is downstream of optimizing that one quantity.

The book resolves into rules and no-no's: the patterns that become mandatory once your reader is a machine, and the decades-old industry-standard patterns that turn actively harmful in its hands. The rules consolidate into **numbered Laws** a reader can tape to the wall, resting on a formal spine — domain vocabularies composed as a **colimit** from category theory, treated not as the static "unified enterprise model" that has failed for thirty years, but as a living, gap-aware, agent-maintained eval target. It closes with a worked engineer's appendix: a bitemporal Silver table shown whole, a semantic model shown once, and the CI gates that make "governance by construction" literal rather than aspirational.

## 3. Why now, why this book

- **The shift is live and unevenly understood.** In 2026 most enterprise agents are still pilots; all are headed for production. Leaders know they need "AI-ready data" and have almost no concrete architecture for it. Gartner's 2024 projection — 60% of AI projects abandoned through 2026 for want of AI-ready data — is expiring on schedule.
- **The market is consolidating around the thesis.** The semantic layer went from niche to table stakes; the Open Semantic Interchange standard shipped v1.0 in January 2026; MCP moved to the Linux Foundation's Agentic AI Foundation. The debate is over *how*, not *whether* — which is exactly where this book lives.
- **It engages the orthodoxy instead of dodging it.** It names its disagreements (Kimball star schemas in Gold, Collibra-as-overlay, data mesh without a semantic core, "just add a chatbot") and dismantles them on the record — and credits what it inherits from each.

## 4. Audience

**Primary:** data platform leaders, heads of data engineering, data architects, and CDOs at mid-to-large enterprises — especially in regulated, semantically dense domains (financial services, healthcare, insurance). Readers fluent in dbt, semantic layers, and the Bronze/Silver/Gold convention. Agreement is assumed nowhere; the book argues every position.

**Secondary:** senior data engineers and analytics engineers moving into modeling/architecture; ML and AI-platform engineers building agentic systems who hit the "the model is fine, the data isn't" wall; technical product leaders scoping conversational-analytics and agent programs.

**Prerequisite:** working familiarity with a modern lakehouse stack. Not an introduction to data engineering — a senior architecture argument.

## 5. What makes it different (key selling points)

1. **A real thesis, not a survey.** "Information density per token is the binding constraint" reframes the whole problem and yields non-obvious, falsifiable architectural calls.
2. **Buildable, not aspirational.** The Laws, the diagnostic, the four investments, the engineer's appendix (Silver DDL, semantic-model YAML, CI gates, Gold-publication spec) — a reader can act this week.
3. **A formal spine, made practitioner-accessible.** Category-theoretic composition (colimits, morphisms with honest losses) and bitemporality (Snodgrass, SQL:2011) translated into operations, never math for its own sake.
4. **Manifesto voice.** Dense, blunt, and argued against named foils — not a hedged seminar. It is a book with positions.
5. **Fact-checked to press standard.** Every external statistic verified against primary sources; benchmarks dated with trajectories; nothing from SEO content farms.
6. **Empirical claims ship with a public, reproducible harness.** The book's key results (semantic density, governed-topology contamination) were measured on TradeBench — a pre-registered, open experiment suite (github.com/thegoodtailor/semantic-enterprise-experiments) — and reported in dated sidebars. And the book's declarations are written in its own vendor-neutral notation, the creole, which compiles mechanically onto whatever stack the reader runs.

## 6. Author

**Iman Poernomo** has spent two decades running enterprise data and AI at institutions where getting meaning wrong is most expensive — currently **Head of AI and Data at Bullish**, and previously **VP and Head of Enterprise Data & Analytics at AstraZeneca**, **Chief Data Officer at Preqin**, and at **JP Morgan** both **Chief Data Officer for Enterprise Data Science** and **Chief Information Architect for the Corporate & Investment Bank**.

He is also the rare practitioner who built this book's formal foundations before he had to apply them. On the computer science faculty at **King's College London (2004–2011)**, he worked in formal methods, constructive type theory, and the categorical composition of specifications — the same pushout-and-colimit calculus (developed with Crossley and Wirsing; WADT'99 and a 2005 monograph) that this book repurposes from program specification to the integration of data models. PhD in Computer Science, BSc in Mathematics, and BA in Philosophy, Monash University; earlier a senior research scientist at Australia's DSTC.

That combination is the book's authority claim. Most data-architecture books are written either by practitioners without the formal grounding or by theorists without the operational scars. This one is written by the person who proved the theorems and then ran the platforms — across pharmaceuticals, investment banking, alternative-assets data, and a digital-asset exchange.

*The book's case studies and worked definitions are deliberately illustrative composites — reasonable industry conventions, not any employer's proprietary practice — which keeps it publishable without disclosure constraints.*

## 7. Competitive and complementary titles

- **Kimball & Ross, *The Data Warehouse Toolkit*** — the dimensional canon. This book inherits grain discipline, conformed dimensions, and SCD2, but relocates them (Silver, not a physical Gold star) for columnar engines and AI consumers. Complementary foundation; different consumption layer.
- **Inmon, *Building the Data Warehouse*** — subject-oriented integration. Acknowledged ancestor; this book rejects the monolithic central model for a federated colimit.
- **Dehghani, *Data Mesh*** — domain ownership as structure. This book agrees on ownership and argues mesh underspecifies the semantic layer, producing "federation without composition." The most direct conceptual neighbor; this book supplies the missing semantic core.
- **Reis & Housley, *Fundamentals of Data Engineering* (O'Reilly)** — the lifecycle survey. This is the opinionated architecture *on top of* that foundation; complementary, more senior, more polemical.
- **Majors et al. / observability and *Designing Data-Intensive Applications* (Kleppmann)** — adjacent infrastructure classics. This book is narrower and more current: meaning and governance for the agentic consumer specifically.

**The gap it fills:** there is no current book on *data architecture designed for AI agents as the primary consumer* — the semantic layer, governance-by-construction, and agentic intelligence treated as one architecture. The AI-data shelf is mostly RAG/LLM-app how-to; the data-architecture shelf predates the agentic consumer. This sits exactly between them.

## 8. Specs

- **Length:** ~90,000 words (complete draft).
- **Chapters:** 18 (16 chapters + No Walls coda + Engineer's Appendix + a Foundations and Sources essay), plus References.
- **Figures:** 32 original (editorial cartoons + architecture diagrams), already produced.
- **Format:** AsciiDoc, include-based master — directly compatible with O'Reilly Atlas. Automated PDF/HTML build (CI) already in place.
- **Schedule:** **Complete first draft exists now.** Realistic path: developmental edit + technical review over ~3 months from contract; revisions ~2 months; production-ready ~6 months from contract. (The usual write-the-book risk is already retired.)

## 9. Annotated table of contents

1. **Introduction** — The consumer that should no longer exist; the eight convictions; the intellectual foundations (category theory, bitemporality, why prose over OWL).
2. **The Shift** — The 1% problem; *information density per token* as the binding constraint; the strategies that fail; the new primary consumer; six changes to make this week.
3. **Language is the Material** — Naming as construction; the metadata graveyard; documentation as onboarding; the three-tier vocabulary; data engineering as applied linguistics.
4. **The Architecture** — Bronze/Silver/Gold re-derived for columnar engines and AI; *joins are declared, never inferred*; where serious people disagree; multi-domain composition as colimit; the MDR of the future.
5. **Exploring the Glued Ontology** — One cross-domain session; security on joined cells; who this is for.
6. **Time** — The two questions ("what was true" vs "what was reported"); bitemporality without overkill; correction events; the query vocabulary; the right to be forgotten.
7. **The Intelligence Stack** — The five layers in one view: governed data, semantic layer, conversation, agents, autonomous research; why the stack is strict; the three positions that stop organizations seeing it whole; the map of the book's second half.
8. **The Death of the Dashboard** — The 40-workbook problem; what conversational analytics actually looks like; the positions worth fighting; one layer, every consumer.
9. **Agentic Intelligence** — The knowledge loop: agents observe through standing questions, conjecture into a bitemporal belief table, survive adversarial refutation, publish graded answers — and grow the estate, drafting the new measures, standing questions, and population contracts that humans adjudicate. The verification oracle an enterprise must build; multi-agent topology as refutation machinery; what the loop reads is fenced.
10. **Building with AI** — Why traditional information architecture failed; AI as always-on curator; continuous morphism verification; governance by construction; the team shape.
11. **The Sandpit** — ML feature engineering and training pipelines under the same ontology; there is no ungoverned tier, only a provisional one.
12. **By Any Means Necessary** — Population is a policy: AI as builder and populator of the estate, not only its reader. Declared contracts populated agentically; witness by evidence, not by copy; trust grades in the schema; grafting curated knowledge onto governed Gold; the estate as an organism rather than a refinery.
13. **The Living Colimit** — The whole assembled into one self-verifying system; shipping it this year; the formal spine.
14. **The Reflexive Loop** — Four loops of self-correction; falsification by design; the brain that knows when it was wrong.
15. **The Playbook** — **The Laws** (the tape-to-the-wall page); the diagnostic; four investments (vocabulary, semantic layer, agent infrastructure, the builder's estate); what to stop spending on; the board presentation.
16. **No Walls** — Coda: the platform as a place you think.
17. **The Engineer's Appendix** — Anatomy of a Silver table (shown whole); the semantic model shown once; the creole reference card; the evidence bundle; the context budget; the shared-key registry; the CI gates; the Gold-publication spec.
18. **Foundations and Sources** — the intellectual lineage as an essay, followed by **References**.

## 10. Sample chapter

**Recommended: Chapter 2, "The Shift."** It is self-contained, states the central thesis (information density per token) with the trading-desk worked example, lands the foils, and ends on concrete actions — it shows the book's argument, altitude, and voice in one read. **Alternate:** Chapter 6, "Time," to showcase the practitioner depth and the bitemporal rigor.

---

*Full manuscript, the CI-built PDF, and the figure set are available immediately on request.*
