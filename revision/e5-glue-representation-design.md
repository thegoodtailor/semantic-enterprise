# E5 Design — Glue Representations: How Should a Pushout Be Written for an LLM?

**Status: DRAFT — sleeping on it (Iman, 27 Aug evening). No freeze, no spend, until
sign-off. OpenRouter needs a top-up (~$6 left) before any run.**

## The question

At matched token budgets, which representation of a two-domain composition (a pushout:
shared identity, renamed polysemes, hidden concepts, partial maps, temporal alignment)
lets an LLM answer cross-domain questions correctly — and does the answer reflect the
*form* of the representation or merely the model's *training exposure* to it?

Origin: Iman — "wouldn't it be good to have a version of CASL... in a world of free
text understood by an AI"; then: "it hasn't been TRAINED on creole... who's to say with
the right training it would manage properly — like with Python"; then: "testing against
OWL would be more interesting — even if it's replicating — as it IS training. or
comments against schemas." All three shape the design below.

## Testbed

Extend the existing seed-42 TradeBench DuckDB (`data/tradedesk.duckdb`, ~230k rows,
public repo, `trap_assertions.py` proves traps live before any run). Add a genuine
Finance domain — GL accounts, booked positions with leg detail, journal linkage —
sharing trade/account identity with the trade side (`fee_rev_jnl` and `fiscal_cal`
already exist as the seed of it). Five seeded composition traps, one per failure class:

1. **Shared identity** — trade_id/acct_cd is the only legal glue (the pushout apex).
2. **Polysemy** — "position": trading open position (pos_eod) vs finance booked balance.
3. **Hidden concept** — gl_leg_detail has no mapping; cross-domain leg questions must
   be refused, not improvised.
4. **Partial map** — desk → cost_center covers 6 of 8 desks.
5. **Temporal misalignment** — fiscal calendar vs UTC; raw date equality is the trap.

~24 cross-domain trap questions with gold SQL + per-trap foil signatures (E1 method:
wrong answers are fingerprinted, not just counted), plus ~8 sanity questions.
Single-domain contexts IDENTICAL across arms; only the glue text varies.

## Arms (each must state all five facts — completeness checklist verified at freeze)

| Arm | Representation | What it tests |
|----|----|----|
| A  | **Creole, semantic core** (`glue/along/rename/hide/partial` + prose defs) | the book's candidate notation, zero-shot |
| A+ | **Creole + grammar card** (one-page reference + 2 worked examples in-context) | exposure-vs-form: in-context learning as the stand-in for training |
| B  | **Config style** (genuine LookML/MetricFlow idiom: joins, dimensions, hints) | the semantic-layer-tool answer |
| C  | **Light markup** (bullets anyone could write) | the low-ceremony baseline |
| D  | **Literary pushout** (pure essay narrating the composition; no structure) | prose as semantic carrier; anaphora risk |
| E  | **Hybrid** (essay + 6-line glue block carrying only the bindings) | the predicted winner: prose for meaning, structure for binding |
| F  | **OWL/RDF** (imports, equivalentProperty/subPropertyOf, annotations carrying the five facts) | **Iman's addition**: the IN-TRAINING formalism — separates familiarity from form; replication anchor to the published raw-OWL result (F1 0.323 < no-file 0.431, LLMs-for-ontology-engineering SLR) |
| G  | **Commented DDL** (CREATE TABLE + `--`/COMMENT ON lines carrying the five facts) | **Iman's addition**: the industry default — what every reader already does |

Token parity: arms padded or reported at both raw and parity budgets (E3 method).
Single-author bias (all arms written by one hand) stated in the pre-registration;
arm B and G written in genuine tool idiom, not caricature.

## Pre-registered hypotheses & interpretation rules

- **H5a (ordering):** E ≥ A+ ≥ A > D > C ≥ G > B > F on trap accuracy.
- **H5b:** essay (D) failures concentrate in BINDING classes (wrong-sense, phantom
  sharing); **H5c:** config (B) and DDL (G) failures concentrate in MEANING classes
  (loss-ignorance, calendar).
- **H5d (exposure vs form, the Python objection):** if A loses to D bare but A+ closes
  the gap → deficit is exposure, curable by shipping the card. If A and A+ both lose →
  deficit is form; redesign goes literary. If A wins bare → the creole's
  ~90%-in-distribution design bet holds.
- **H5e (the OWL cross-check, Iman's):** F underperforms C despite maximal training
  exposure → familiarity does not rescue a form hostile to attention — the strongest
  available answer to "it's just training." If F performs well, the replication fails
  interestingly and the prose-over-OWL chapter claim needs re-scoping.
- **H5f:** G (commented DDL) beats B (bare config) — comments carry meaning — but
  loses to E on binding traps.

## Grid & cost

32 questions × 8 arms × 3 models (GPT-5.6-terra, Claude Sonnet 5, Gemini Flash as
mid-tier control) × 3 runs ≈ 2,300 calls at ~3–4k in / ~0.5–1k out.
July's E1–E3 ran ~3,084 calls for ~$30–45 → **envelope $40–60** including the $2
single-model pilot (mandatory — July's pilot caught a fatal design flaw), deterministic
foil-grading plus a small LLM-judge pass for refusal scoring, and one re-run's headroom.
Trim to 2 runs × 2 models ≈ $25–35 at the cost of the mid-tier control.

## Process

1. Iman signs off on this design (post-sleep). 2. OpenRouter top-up. 3. Build generator
extension + questions + arms; completeness checklist; PRE-REGISTRATION FREEZE commit.
4. $2 pilot (1 model × 1 run) → fix design flaws only. 5. Full run. 6. Numbers enter
the book only on Iman's approval (standing rule). Results decide the gated creole
redesign (revision/brief-creole-redesign.md) with evidence.

## What it feeds

- The creole redesign (gated brief) — grammar chosen by measurement, not taste.
- An E5 sidebar at ch4's creole section (and ammunition for the prose-over-OWL claim,
  which the literature already supports: raw OWL scoring below no-context at all).
- The paper: the literature review (27 Aug) found no study of representation format
  for LLM comprehension of vocabulary COMPOSITION — schema serialization, ontology
  verbalization, and format-sensitivity are all studied; the pushout is not. This
  slots into Iman's old field's new territory (CASL lineage, sentences-in-English,
  two-interpreter semantics), with E5 as its empirical core and the fine-tuned-model
  ceiling question (the Python point) as future work.
