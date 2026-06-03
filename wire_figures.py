"""Insert figure blocks into the adoc after the paragraph containing each anchor.
Idempotent: skips a figure whose id is already present."""
from pathlib import Path
import shutil, datetime

ADOC = Path("/home/iman/data-management/the-semantic-enterprise.adoc")

# (anchor substring, fig-id, figures/<name>.png, caption, width)
FIGS = [
 ("It amplifies it.", "old-vs-new-consumer", "old-vs-new-consumer",
  "The old consumer compensated for ambiguity; the new one amplifies it. Build for the consumer that cannot squint.", 600),
 ("It is automated confusion. It is your existing mess", "chatbot-confusion", "chatbot-confusion",
  "A chatbot on ungoverned data is not conversational analytics — it is automated confusion, delivered faster, to more people.", 600),
 ("they are having two different conversations with the same word", "polysemy-position", "polysemy-position",
  "Polysemy: “position” means three different things to three domains. Without a semantic layer the warehouse joins them into nonsense.", 600),
 ("Most data platforms are warehouses with loading docks.", "restaurant-no-menu", "restaurant-no-menu",
  "A warehouse with a loading dock and no menu: ingredients pile up, but nobody has decided what the platform serves.", 600),
 ("Bronze is the sworn testimony.", "bronze-witness", "bronze-witness",
  "Bronze is sworn testimony — the producer’s record, taken down verbatim and never edited.", 600),
 ("Wall Street is populated with failed data lakes", "data-swamp", "data-swamp",
  "Uncatalogued Gold becomes a swamp: hundreds of tables, nobody knows what half of them hold, nobody trusts the numbers.", 600),
 ("achieved a 300x reduction.", "tax-300x", "tax-300x",
  "The 300× tax: a physical star schema makes the agent reason through joins on every query. Flatten Gold and the tax disappears.", 640),
 ("two structurally different questions, and the architecture must answer both", "two-questions", "two-questions",
  "Two questions, one fact: what was ‘true’ versus what was ‘reported.’ The architecture must answer both and keep them distinct.", 600),
 ("that is the fearful answer", "bitemporal-overkill", "bitemporal-overkill",
  "Two clocks on every row, always, is overkill. Tier it — full history only where a regulator will actually ask.", 640),
 ("But the structure of the problem is always the same.", "forty-workbooks", "forty-workbooks",
  "Forty workbooks, forty definitions of ‘revenue,’ each copied from the last, none reconcilable. Move the definition out of the workbook.", 640),
 ("Without grounding: ten to thirty-one percent.", "guess-vs-reason", "guess-vs-reason",
  "Grounded, an agent reasons (94–99%); ungrounded, it guesses (10–31%). The difference is infrastructure, not intelligence.", 600),
 ("amplify errors by a factor of 17.2", "multiagent-amplify", "multiagent-amplify",
  "Multi-agent without shared semantics amplifies error 17×: collaborative confusion, not collaborative intelligence.", 600),
 ("does not get bored, does not lose context", "curator-vs-committee", "curator-vs-committee",
  "Governance at human speed loses to a machine that never sleeps: continuous curation, not the quarterly committee.", 600),
 ("a security gate on the front door of a building with no walls", "gate-no-walls", "gate-no-walls",
  "Govern only the chatbot and you have a security gate on a building with no walls — every other consumer walks in around the side.", 600),
 ("We call it **Dev Gold**.", "dev-gold-nursery", "dev-gold-nursery",
  "Dev Gold: exploratory data is let loose to play, but every result is tagged with provisional, AI-authored semantics — feral, never lawless.", 640),
 ("Your board needs three sentences.", "board-three-sentences", "board-three-sentences",
  "If your strategy needs fifty slides, it is not a strategy. The board needs three sentences.", 600),
 ("FIBO is a beautiful corpse", "metadata-graveyard", "metadata-graveyard",
  "The graveyard of grand unified models, standalone MDRs, and beautiful dead ontologies. The failure was maintenance, not design.", 640),
 ("Three tiers, connected by a single principle: upstream always wins.", "three-tier-vocab", "three-tier-vocab",
  "The three-tier vocabulary: glossary governs schema governs semantic layer. Upstream always wins.", 600),
 ("Skip a layer and the stack collapses.", "intelligence-stack", "intelligence-stack",
  "The intelligence stack: each layer depends on the one below. Skip a layer and it collapses.", 460),
 ("Three things you already have, wired into one loop.", "living-colimit-mesh", "living-colimit-mesh",
  "The living colimit: verification agents and a coordinator continuously re-check the bridges; a broken span raises a witness, and colimit-health is watched like uptime.", 640),
]

def block(figid, name, caption, w):
    return f"\n[#fig-{figid}]\n.{caption}\nimage::figures/{name}.png[{figid.replace('-',' ')},width={w},align=\"center\"]\n"

text = ADOC.read_text(encoding="utf-8")
shutil.copy(ADOC, ADOC.with_suffix(ADOC.suffix + ".pre-figures-2026-06-01"))
lines = text.split("\n")

inserted = 0
for anchor, figid, name, caption, w in FIGS:
    if f"[#fig-{figid}]" in text:
        print(f"  skip {figid} (already present)"); continue
    # find the line containing the anchor
    idx = next((i for i, ln in enumerate(lines) if anchor in ln), None)
    if idx is None:
        print(f"  !! anchor not found for {figid}"); continue
    # advance to end of this paragraph (next blank line)
    j = idx
    while j < len(lines) and lines[j].strip() != "":
        j += 1
    # insert block (as its own lines) right after the blank line
    blk = block(figid, name, caption, w).split("\n")
    lines[j+1:j+1] = blk
    inserted += 1
    print(f"  wired {figid} after line {idx+1}")

ADOC.write_text("\n".join(lines), encoding="utf-8")
print(f"\ninserted {inserted} figure blocks")
