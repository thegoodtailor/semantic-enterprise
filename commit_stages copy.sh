#!/usr/bin/env bash
# Creates three clean commits from the current working tree:
#   1. Stage 0 — mechanical fixes + chapter split (from snapshot)
#   2. Revision campaign — review + agent briefs
#   3. Stage 1 — corrections + de-crypto (current state)
# Run from the repo root on your Mac:  bash commit_stages.sh
set -euo pipefail
cd "$(dirname "$0")"

[ -d .revision-snapshots/stage0 ] || { echo "ERROR: .revision-snapshots/stage0 missing"; exit 1; }
rm -f .git/index.lock

# Preserve the current (Stage 1) state
mkdir -p .revision-snapshots/stage1
rm -rf .revision-snapshots/stage1/chapters
cp -r chapters .revision-snapshots/stage1/chapters
cp the-semantic-enterprise.adoc .revision-snapshots/stage1/

# --- Commit 1: Stage 0 ---
rm -rf chapters
cp -r .revision-snapshots/stage0/chapters chapters
cp .revision-snapshots/stage0/the-semantic-enterprise.adoc the-semantic-enterprise.adoc
git add the-semantic-enterprise.adoc chapters merge_book.py .gitignore
git commit -m "Stage 0: mechanical fixes + chapter split

- Fix 415 malformed em-dashes (em-dash+hyphen artifact), typos
- Split monolith into chapters/01-14; master becomes include-based
  (reconstruction verified byte-identical; anchors travel with chapters;
  all 27 figure refs resolve)
- merge_book.py flattens includes for legacy tooling"

# --- Commit 2: review + briefs ---
git add review-2026-06-11-technical-depth-and-style.md revision/ commit_stages.sh
git commit -m "Revision campaign: technical review + agent briefs 00-06

- Full technical-depth & style review (fact-check with sources)
- Briefs: plan, style charter, corrections, governed-joins doctrine,
  de-crypto + GDPR rebuild, multi-agent v2, reflexive loop (new chapter)"

# --- Commit 3: Stage 1 ---
rm -rf chapters
cp -r .revision-snapshots/stage1/chapters chapters
cp .revision-snapshots/stage1/the-semantic-enterprise.adoc the-semantic-enterprise.adoc
git add chapters the-semantic-enterprise.adoc
git commit -m "Stage 1: corrections + de-crypto (8 chapters, parallel agents)

- dbt-snapshots valid/system-time inversion corrected (Time chapter)
- Benchmarks refreshed (Spider 2.0, BIRD, dbt 2026); fabricated stats cut
  (MIT 34%, \$67B, 84%, 200-400% pods); Gartner wordings exact
- EU AI Act updated for May 2026 Digital Omnibus
- Crypto/employer references recast as generic trading venue (incl. Bullish ref);
  MiCA -> MiFID II recategorisation / IBOR transition
- 3 TODO(author) markers for items needing author input
- Untouched by design: 300x/joins passages, multi-agent section,
  erasure section (Stage 2 rewrites per briefs 03/04/05)"

rm -rf .revision-snapshots
echo "=== Done:"
git log --oneline -3
