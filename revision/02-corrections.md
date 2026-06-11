# Corrections Brief — facts, numbers, citations (Stage 1)

Line numbers refer to the pre-split monolith (= post-split chapter files, content unchanged). Full evidence and URLs: `../review-2026-06-11-technical-depth-and-style.md` Parts 1.7–1.9. This brief is the actionable digest; agents apply, continuity agent verifies.

## A. Load-bearing rewrites (not find-replace — see briefs 03/05 for replacement content)

| Site | Problem | Replacement direction |
|---|---|---|
| ~288–297, ~311, fig tax-300x, ~456, ~1574 | Snowflake "300x / join-free" misreads Cortex AISQL optimizer research; "joins cost more in columnar" overstated | Brief 03: joins-declared-never-inferred doctrine + real economics (Strategy Mosaic 50%/98% token cuts; AtScale 20%→92.5% over declared joins; dbt SL 100%-in-scope) |
| ~1311 | dbt snapshots claim inverted: snapshots record detection/source-transaction time, NOT valid time; backdated corrections unrepresentable | Rewrite passage; add Law: "valid time comes from the business; system time comes from the pipeline"; cite dbt docs + Discourse 1067 + dbt-core #7018; mention v1.9 snapshot upgrades |
| ~1606–1610 | Spider 2.0 "6%" stale (June 2026 leaderboard: Snow 96.7 / Lite 73.1 / DBT 65.6); BIRD is 54.89% not 52, SOTA ~82; VLDB paper: 52.8% BIRD Mini-Dev, −7%..+31% *relative* | Use review §4.3(c) sample rewrite — trajectory framing + determinism argument |
| ~1920–1925, fig caption | "17.2x vs single-agent baselines" wrong | Brief 05 |
| ~1451–1469 | GDPR/erasure section legally wrong + crypto-framed | Brief 04 part B |

## B. Statistics to cut or re-source (straight edits)

- ~187 "84% of data teams… conflicting versions" — no source exists. Cut, or use Salesforce: 84% of data leaders say strategies need overhaul before AI succeeds.
- ~204 "67% chatbot deployments failed / 6% of IT leaders" — unsourced. Replace with Gartner 2023: 8% of customers used a chatbot in last service interaction; 25% of those would again.
- ~204 Klarna: "replaced 700 agents" → "AI did the equivalent work of 700 agents"; 2025 reversal was quality-driven rebalance to hybrid.
- ~1538 "73–88% data unused" → Forrester 60–73%.
- ~1552/1688 "self-service BI below 20% (Gartner)" → ~30%, or drop attribution.
- ~1770 "11% production / 2% scale" → re-anchor on PwC May 2025 (79% claim adoption) + flag unverified, or cut.
- ~1956 MIT "34% more confident when wrong" — fabricated (SEO farm). Cut; replace with OpenAI "Why Language Models Hallucinate" (arXiv 2509.04664): training/eval rewards confident guessing.
- ~1973 "44% of finance teams deployed agentic AI" → Wolters Kluwer: 6% using + 38% intending within 12 months.
- ~1993 "$67B hallucination losses" — fabricated. Cut.
- ~1995 "RAG reduces hallucinations 40–71% / KG 40%" — unsourced range. Cite specific studies or cut.
- ~2244 Google "25% of new code" → "AI-generated, reviewed by engineers" (Pichai, Oct 2024; >30% by Apr 2025 — date it).
- ~2246 Anthropic study: keep 50% vs 67%, add: speed gain ~2 min, not statistically significant; n=52.
- ~2244 BCG consultants: keep +12.2%/25.1%/+40%, add the other half: 19 points *worse* outside the capability frontier (supports the book's own frontier caveat).
- ~2585 "16% of engineering leaders" — not found. Cut or re-source.
- ~2900 "IBM/Microsoft/banks 200–400% pods" — unverifiable. Cut. "5-person team = 8–10 person team" — present as author's claim, not industry data.
- ~2910 "55% regret AI layoffs" → Orgvue: 39% made AI-driven redundancies; of those, 55% admit wrong decisions.
- ~1574 "flattening reduces tokens up to 69%" → 30–60% (TOON/ONTO); "CSV beats JSON 40–50%" → 56% fewer tokens with *higher* accuracy (GetCrux).
- ~2886 CDO 84%/12%: add caveat — survey covers Fortune-1000-scale firms.

## C. Gartner / institutional wordings

- ~377 "80% of governance initiatives fail by 2027 due to lack of connection to business outcomes" → "**due to a lack of a real or manufactured crisis**" (Feb 2024 release — and the corrected quote is better for the book; use it).
- ~248/~601/~2258 60%-AI-projects wording: standardize on "Through 2026, organizations will abandon 60% of AI projects **unsupported by AI-ready data**."
- ~266 "model accuracy by up to 80%" → "**agentic AI accuracy** by up to 80%" (Gartner, May 11 2026).
- ~266 "By 2028, 60% of agentic analytics projects without a consistent semantic layer will fail" → add the qualifier "**relying solely on the Model Context Protocol**" — and use it: it feeds the book's MCP-is-plumbing argument.
- ~1770 "40% of agentic AI projects canceled by 2027" → "over 40%… by **end of** 2027… escalating costs, **unclear business value** or inadequate risk controls."
- ~1179 "no metadata, no AI" → attribute properly: Gartner's slogan is "No data? No AI! No metadata? No data!"; MQ return Nov 2025 confirmed (Leaders: Atlan, Alation, Informatica, IBM, Collibra).
- ~2276 "scrapped the MQ in 2020" → last published Nov 2020, retired 2021. Forrester quote is Prukalpa Sankar's commentary, not Forrester — re-attribute.
- ~2015 EU AI Act: GPAI Aug 2025 correct; **update for May 2026 Digital Omnibus**: Annex III high-risk postponed to Dec 2, 2027 (Annex I to Aug 2028). "Mandates lineage and provenance" → soften: Art. 10 data-governance + origin-of-data, Annex IV provenance documentation; the Act never says "lineage".
- ~1939 MCP/A2A: A2A → Linux Foundation June 2025; MCP → donated Dec 2025 to the Agentic AI Foundation (LF directed fund). Counts: >10,000 public MCP servers, 97M+ monthly SDK downloads (Anthropic, Dec 2025).
- ~264 OSI: founders Sept 2025 = Snowflake, Salesforce/Tableau, dbt Labs, BlackRock +13; Databricks joined later; **v1.0 spec shipped Jan 27, 2026** — cite the spec.
- ~189 Google/Looker "two-thirds": keep, but mark as vendor-internal testing, "as much as" = upper bound.

## D. Small technical fixes

- ~492 "agglutination" → "compounding" (German compounds are compounding; agglutination is Turkish-style morpheme chaining).
- ~359 `fct_`/`dim_` prefixes: attribute to dbt-community convention, not Kimball.
- ~745/~816 "pre-2015 row-based world" → row-store era (Vertica 2005, BigQuery 2011, SQL Server columnstore 2012, Redshift 2013).
- ~745 "predicate pushdown vs join elimination" sentence — garbled; cut or rewrite as scan-pruning vs distributed-shuffle economics.
- ~1369 time travel: BigQuery 2–7 days (not 7–90); Snowflake 1 day default / 90 Enterprise+; Delta ~7d VACUUM / 30d log; Iceberg ~5d default. Frame as operational recovery, never audit.
- ~1417/~1425 as-of joins: declared in the semantic layer, **implemented beneath it** — no semantic layer (LookML/dbt SL/Cube) executes temporal joins natively today; native ASOF JOIN: Snowflake (GA May 2024), DuckDB; not BigQuery/Databricks SQL. Name the tooling gap explicitly.
- ~1135 "the -second window join" — missing value; AUTHOR INPUT NEEDED.
- ~299 "Five Changes to Make This Week" lists six — retitle ("Six Changes…") or merge items five/six.
- ~1139 `latexmath:[$\to$]` → plain `→` for consistency.
- ~1435 streaming: use the standard three clocks (event / ingestion / processing time) and Dataflow-model vocabulary (late data, allowed lateness, retractions); cite Akidau et al. VLDB 2015 / *Streaming Systems*.
- ~28 "consider mere hygine" → "considered mere hygiene"; ~66 "They don't fail when you've tracking clean metadata" → repair grammar (intent: platforms fail for lack of clean semantics, not pipelines) — AUTHOR CONFIRM; ~82 "Billions go to on larger models" → "Billions go on larger models".
- Terminology discipline (Stage 3 continuity check): bridge = **span through a shared sub-theory** everywhere ("bridge functor" only as defined shorthand, once); "morphism" reserved for inter-domain maps, "relationship" for intra-domain.
