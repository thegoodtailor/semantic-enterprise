# Perishability policy — writing for 2030

The book is a classic text, not a market report. Every claim is classified and treated so the main prose never silently expires.

## Classification

| Class | What it is | Treatment |
|---|---|---|
| (i) Historical fact / citation date | "Snowflake shipped ASOF JOIN in May 2024", "DIN-SQL (2023) found…" | **Keep in prose.** Dated events age into history. |
| (ii) Current-state claim | "In 2026 most agents are pilots", "no semantic layer executes as-of natively", vendor caps/limits | **Rewrite as a timeless mechanism claim** where possible; otherwise **move to a dated snapshot sidebar**. |
| (iii) Forward prediction | "by 2027 X will…", market projections | **Sidebar or cut.** Predictions must never sit unattributed in main prose. |
| Model-pinned stat | "GPT-4o scores 55", "GPT-5.3 scored 100%" | **Sidebar** with model IDs + date; prose keeps the mechanism ("the same model, above declared joins, approaches the ceiling"). |
| Market size / analyst number | "$X billion by 20YY" | **Cut** unless load-bearing; if load-bearing, sidebar. |

## The sidebar convention

Volatile material lives in visually fenced, dated AsciiDoc sidebars — period pieces the reader knows are snapshots:

```
.The tooling, as of mid-2026
****
Native `ASOF JOIN`: Snowflake (GA May 2024), DuckDB. Absent from BigQuery and
Databricks SQL. No major semantic layer — LookML, dbt Semantic Layer, Cube —
executes an as-of predicate natively. Expect this table to age; the rule it
illustrates does not.
****
```

Rules:
- Title always carries the date: `.…, as of mid-2026` (or the trial date).
- The **last sentence names what will age and what will not.**
- Main prose above the sidebar must stand alone if the sidebar is deleted — it carries the principle ("declare the rule in the layer; implement it beneath wherever the engine lacks native support"), never the perishable specifics.
- Experiment results (TradeBench) use the same convention: date, n, model IDs, repo URL, one-sentence scope limit.

## Prose conventions that already work (keep, extend)

- "or whatever the acronym of the month is" (ch02) — self-dating by design.
- "MCP may be superseded within five years. The principle will survive every successor." (ch07) — the template sentence.
- The References standing note (ch16:73): confirm engineering figures against current published versions before press.

## What never changes

Claims about mechanism, incentive, and structure are the book's spine and need no dating: ambiguity in → wrong answers out; joins declared never inferred; meaning drifts when governance lives outside the pipeline; valid time from the business, system time from the pipeline. When in doubt, promote the claim to this altitude rather than fencing it in a sidebar.
