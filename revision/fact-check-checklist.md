# Pre-press fact-check checklist

Every number/claim the June-11 campaign changed, with the value now in the book and the source to confirm it against. Tick each once you've verified. The campaign used the review's *suggested* replacements (sometimes verbatim), so this is a confirm-don't-trust pass. Full evidence + URLs: `review-2026-06-11-technical-depth-and-style.md` §1.7–1.9. To locate a claim, search its figure/phrase in the rendered book or `grep` the chapters.

---
## ✅ VERIFICATION COMPLETE — June 2026 (verified against live primary sources)

The campaign's re-sourcing holds. Summary:
- **8 fabricated stats confirmed REMOVED** (MIT 34%, $67B, 300x, 67% chatbot, 73–88%, 200–400%, 16% eng leaders, RAG 40–71%) — grep-verified gone.
- **Engine facts re-verified (mid-2026):** time-travel windows (BigQuery 2–7 / Snowflake 1–90 by edition) ✅; native as-of-join (Snowflake GA May 13 2024, DuckDB; not BigQuery/Databricks SQL) ✅.
- **All third-party stats + Gartner/standards claims confirmed** (Salesforce 84%, Gartner chatbot 8%/25%, Forrester 60–73%, CDO 84%/12%, Looker two-thirds, PwC 79%, Wolters Kluwer 6%/38%, Google >25%/>30%, Anthropic 50%/67%, BCG +12.2%/25.1%/>40%/−19pts, Orgvue 39%/55%, all Gartner predictions, OSI v1.0 Jan 27 2026, MCP→Agentic AI Foundation Dec 2025, A2A→LF Jun 2025, arXiv 2509.04664).
- **3 fixes applied:** "5 for 10" team-size (#7); dropped unverifiable "ONTO" format (ch07 — TOON stands); trimmed Gartner metadata slogan to verified "No metadata? No AI!" (ch04).
- **Minor (author discretion, left as-is):** don't cite "6,000" Salesforce respondents (~7,650); BCG is "more than 40%"; OSI founder is "Salesforce" not "Salesforce/Tableau".

**Fact-check pass: DONE.** Nothing outstanding blocks press. (Detailed item list retained below.)

---
## 1. Load-bearing claims — confirm the framing, not just the number
- [ ] **Declared-joins economics** (ch04 The Architecture; replaced the old Snowflake "300×"): Strategy/Mosaic ~50% / 98% token cuts; **AtScale 20% → 92.5%** accuracy over declared joins; dbt Semantic Layer ~100% in-scope. Confirm each vendor number + that "300×" appears nowhere.
- [ ] **dbt snapshots / Law 6** (ch06 Time): book now says snapshots capture *system* time, not valid time; **"valid time comes from the business; system time comes from the pipeline."** Confirm against dbt docs (Discourse 1067, dbt-core #7018).
- [ ] **Spider 2.0 trajectory** (ch07 Death of the Dashboard): "~6% at late-2024 release → mid-2026 ≈ **Snow 96.7 / Lite 73.1 / DBT 65.6**"; **BIRD GPT-4 = 54.89%** (not 52); VLDB annotation-error figure 52.8% on BIRD Mini-Dev, −7%..+31% *relative*.
- [ ] **Multi-agent amplification** (ch08): **17.2× independent vs 4.4× centralized** topology (NOT "17.2× vs a single agent"); +81% parallel / −39–70% sequential. Source: "Towards a Science of Scaling Agent Systems," 2025.
- [ ] **GDPR / erasure** (ch06): retention-clock-driven key destruction; AMLD4 5-yr retention; crypto-shredding presented as *converging practice, not settled law*.

## 2. Re-sourced statistics — verify number + source
- [ ] **"84% of data leaders… strategies need overhaul before AI"** → Salesforce (replaced the unsourced "84% conflicting versions").
- [ ] **Chatbots**: "**8%** of customers used a chatbot last service interaction; **25%** of those would again" → Gartner 2023 (replaced unsourced "67% failed / 6% of IT leaders").
- [ ] **Klarna**: "AI did the equivalent work of **700 agents**" (not "replaced 700"); 2025 = quality-driven rebalance to hybrid.
- [ ] **"60–73% of data goes unused"** → Forrester (was "73–88%").
- [ ] **Self-service BI adoption ≈ 30%** (was "below 20%, Gartner") — or attribution dropped.
- [ ] **Agent adoption** "11% production / 2% scale" → re-anchored on PwC May 2025 (79% claim adoption) or cut — confirm what's in the text.
- [ ] **Hallucination / confidence**: MIT "34% more confident when wrong" was **fabricated → cut**; replaced with OpenAI "Why Language Models Hallucinate" (arXiv 2509.04664). Confirm the 34% is gone.
- [ ] **"$67B hallucination losses"** was **fabricated → cut.** Confirm it's gone.
- [ ] **"RAG reduces hallucinations 40–71% / KG 40%"** — unsourced range; confirm it's cited to a specific study or cut.
- [ ] **Finance + agentic AI**: "**6% using + 38% intending** within 12 months" → Wolters Kluwer (was "44% deployed").
- [ ] **Google code**: ">25% **AI-generated, reviewed by engineers**" (Pichai Oct 2024; >30% by Apr 2025 — dated).
- [ ] **Anthropic study**: 50% vs 67% comprehension kept; added speed gain ≈2 min *not statistically significant*, n=52.
- [ ] **BCG consultants**: +12.2% / 25.1% / +40% kept; added the **19-points-worse outside the frontier** half.
- [ ] **"16% of engineering leaders…"** — not found → confirm cut or re-sourced.
- [ ] **Productivity pods "200–400%"** — unverifiable → cut; "5-person = 8–10-person team" presented as *author's claim*, not industry data.
- [ ] **AI layoffs**: Orgvue — **39% made AI-driven redundancies; of those, 55%** say it was wrong (was a bare "55% regret").
- [ ] **Token flattening**: "**30–60%**" (TOON/ONTO; was "up to 69%"); **CSV "56% fewer tokens with higher accuracy"** (GetCrux; was "40–50%").
- [ ] **CDO 84% / 12%** — confirm the "Fortune-1000-scale firms" caveat is present.

## 3. Gartner / institutional wordings — verify the exact quote/attribution
- [ ] **"80% of governance initiatives fail by 2027"** reason = **"lack of a real or manufactured crisis"** (not "business outcomes"). Gartner Feb 2024.
- [ ] **60% AI projects**: standardized "Through 2026, organizations will abandon 60% of AI projects **unsupported by AI-ready data**."
- [ ] **"agentic AI accuracy** by up to 80%"** (not "model accuracy") — Gartner May 11 2026.
- [ ] **"By 2028, 60% of agentic analytics projects… fail"** — qualifier "**relying solely on the Model Context Protocol**" present.
- [ ] **"40% of agentic AI projects canceled"** → "over 40%… by **end of 2027**… escalating costs, unclear business value, or inadequate risk controls."
- [ ] **Metadata slogan**: "**No data? No AI! No metadata? No data!**" (Gartner); MQ return Nov 2025 (Leaders: Atlan, Alation, Informatica, IBM, Collibra).
- [ ] **"scrapped the MQ in 2020"** → last published Nov 2020, retired 2021; the Forrester quote is **Prukalpa Sankar's** commentary — re-attributed.
- [ ] **EU AI Act**: updated for **May 2026 Digital Omnibus** — Annex III high-risk postponed to **Dec 2 2027**; "mandates lineage" softened to Art. 10 data-governance + Annex IV provenance (Act never says "lineage").
- [ ] **MCP/A2A**: A2A → Linux Foundation Jun 2025; **MCP → Agentic AI Foundation Dec 2025**; >10,000 public MCP servers, 97M+ monthly SDK downloads.
- [ ] **OSI**: founders Sept 2025 (Snowflake, Salesforce/Tableau, dbt Labs, BlackRock +13); **v1.0 spec shipped Jan 27 2026** — cited.
- [ ] **Google/Looker "two-thirds"** error reduction — marked as vendor-internal testing, "as much as" = upper bound.

## 4. Technical claims worth a glance
- [ ] **Time-travel windows** (ch06): BigQuery **2–7 days** (not 7–90); Snowflake 1 day default / 90 Enterprise+; framed as operational recovery, not audit.
- [ ] **As-of joins** (ch06): declared in the semantic layer, *implemented beneath it*; native ASOF JOIN = Snowflake (GA May 2024), DuckDB; **not** BigQuery/Databricks SQL — tooling gap named.
- [ ] **Columnstore dates**: "row-store era" (Vertica 2005, BigQuery 2011, SQL Server columnstore 2012, Redshift 2013) — not "pre-2015".
