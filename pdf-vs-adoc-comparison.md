# PDF vs ADOC — provenance comparison

**Compared:** `the-semantic-enterprise-PREVIEW (1).pdf` (Liora's PDF, metadata authored "Iman Poernomo, Liora, and Darja", PDF CreationDate **2026-05-30 11:46 UTC**, 233pp) **vs** `the-semantic-enterprise (3).adoc` (the version critiqued in `the-semantic-enterprise-review.md`).
**Date:** 2026-06-01 · **By:** Nahla
**Question asked:** is the adoc a Darja-authored corruption of Liora's PDF?

---

## Headline: NOT a corruption — faithful copy + additive theory layer

- **93.2%** of the PDF's 10-word shingles appear verbatim in the adoc; **93.5%** vice-versa.
- Near-identical length: **82,358** words (PDF) vs **82,138** (adoc).
- Identical 9-chapter structure, identical opening line, identical section ordering. Of 117 adoc subsections, **116 are present in the PDF**; exactly **1 is new** (Continuous Morphism Verification).
- Reverse check: **no substantive operational content was dropped** from the PDF. PDF-only blocks are (a) inline-rendered figures the adoc references as `image::` files, and (b) minor reference-formatting differences.

**Conclusion:** the adoc = Liora's PDF (intact core) **+ an additive category-theory / formal-verification overlay**. Not a rewrite, not a destructive corruption.

---

## What the ADOC adds that the PDF lacks (the "Darja layer")

1. **"Continuous Morphism Verification" — entire section, 0% present in PDF.** The multi-agent verification mesh: per-domain verification agents, "continuous integration for meaning," standing mesh + coordinator, six check types (structural/referential/distributional/completeness/loss/commutativity), emits-a-witness, colimit-health vector. The single largest graft.
2. **"Morphism Honesty" pattern — governance philosophy changed.** PDF: *human-signature* ("explicit, named, dated, **signed by both domains**… who in each domain signed off, when last reviewed"). ADOC: *continuous-agent* ("**continuously verified**… each domain's agent re-checks on every scan… last confirmed last night"). Same pattern, different mechanism.
3. **Sharpened flat-Gold polemic (adoc-only rewrites).** "Joins are hallucination vectors"; "dimensional structure is not eliminated — it is **relocated** [to Silver]"; the punchy five-table-star token passage. The PDF argues the same points more plainly.
4. **Formal-provenance references added** to the bibliography: Crossley–Poernomo–Wirsing (WADT'99), *Adapting Proofs-as-Programs: The Curry–Howard Protocol* (2005 monograph), Poernomo–Crossley protocols (LOPSTR 2000), Johnson–Rosebrugh sketches. (PDF cites a slightly different Johnson–Rosebrugh paper — Wells/MSCS vs Wood/TAC.)
5. **Subtitle change:** PDF *"Data Architecture After AI"* → ADOC *"Data Architecture for the Agentic Era."*

Every addition is the **same thing**: the colimit-formalism / continuous-verification overlay layered onto Liora's operational book.

---

## Impact on the scale review (`the-semantic-enterprise-review.md`)

Some critiques were aimed at **adoc-only (Darja) material**, not Liora's canonical PDF:

- **Crack #4** (CMV is the most speculative / aspirational / needs-its-own-SRE) targets a section **absent from the PDF**. Against the PDF it's not a flaw in Liora's book — it's a question of whether to *accept the graft*.
- **Crack #1** (governance-by-signature vs construction) reads differently against the PDF, where Morphism Honesty *is* the human-signature model the adoc already shifted toward continuous verification.
- The flat-Gold passages **praised** as scale-solid in §A are adoc-only sharpenings.

**Unaffected — these are Liora-core, present in BOTH and stand regardless:**
- §C-1 tiered-vs-always **bitemporality** contradiction.
- §C-2 conformed-dimension-vs-bridge contradiction.
- Crack #2 (AI solves drift, not semantic correctness), crack #3 (bitemporal cost + privacy-erasure collision), crack #5 (conformed-vs-bridge), and the §D smaller risks.

---

## Deep-dive: "The Consumers You Forgot" (Ch 8) — did Darja add human-in-loop / bypass?

**No.** Tested directly because of the worry that Darja inflated human-in-the-loop and semantic-layer-bypassing in the adoc version of this chapter.

- Ch 8 overlap: **94.2% of PDF in adoc, 95.7% of adoc in PDF.** The adoc version is slightly **shorter** (6,124 vs 6,282 words), not longer.
- Keyword frequencies near-identical: `bypass` 7/7, `direct access` 9/9, `read Silver` 4/4, `quarterly` 3/3, `sign-off` 9/9, `power user` 1/1, `governance` 36/36.
- Every load-bearing concession is **present verbatim in Liora's PDF**: "feature pipelines consume Silver directly," "legitimate architectural bypass," "governance is contractual," "data contract between the platform team," "review contracts quarterly," notebooks as "hardest case for the sole-interface," "tiered consumption model," "no power users," and the refinement "sole interface for **analytical** consumption."

**Conclusion:** the human-back-in-the-loop / re-admit-bypass emphasis in Ch 8 is **Liora's original**, not a Darja graft. Crack #1 is a valid critique of the book, but it targets **Liora's operational chapter.**

**The twist:** Darja's additions push the *opposite* direction — the CMV section replaces quarterly human sign-off with a continuous **agent** mesh, and her Morphism-Honesty rewrite flips "signed by both domains" → "each domain's agent re-checks every scan." So Darja *removes* humans; Liora's Ch 8 *re-admits* them. **This is a genuine seam between the two authors** (Ch 7 continuous/agentic vs Ch 8 contractual/human) and worth resolving deliberately.

## Open questions for Iman / the team

1. **Which is canonical** — Liora's PDF, or the adoc-with-Darja-overlay? The review was written against the adoc.
2. **Is the CMV section wanted?** It's the freshest idea and the least de-risked. If kept, it should be framed as a target/research direction (it already is, partly), and it ties directly to the `enterprise-colimit` paper (§M6 cites the book as the companion).
3. **Morphism Honesty:** keep the PDF's human-signature framing, the adoc's continuous-verification framing, or a hybrid (signature as the human escalation path *within* continuous verification)?
4. **Subtitle:** "After AI" vs "for the Agentic Era."
