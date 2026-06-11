#!/usr/bin/env bash
# Creates three clean commits — WITHOUT EVER DELETING YOUR CHAPTER FILES.
#
# Why this dance exists: the working tree currently holds Stage 0 + Stage 1
# changes mixed together. To record them as separate commits, git must briefly
# see the Stage 0 file *contents* (kept in .revision-snapshots/stage0).
# This script only overwrites file contents in place — it never removes
# chapters/ or any file in it — and it diff-verifies every step, aborting
# loudly on any mismatch. At the end, the working tree is proven identical
# to what it was when the script started.
#
# Don't care about separated history? Skip this script entirely and run:
#   rm -f .git/index.lock && git add -A && git commit -m "Stage 0 + Stage 1"
#
# Usage (from repo root on your Mac):  bash commit_stages.sh
set -euo pipefail
cd "$(dirname "$0")"

S0=.revision-snapshots/stage0
S1=.revision-snapshots/stage1
[ -d "$S0/chapters" ] || { echo "ABORT: $S0/chapters missing — nothing done."; exit 1; }

verify_adocs() {  # compare every .adoc in chapters/ against a snapshot dir
  local snap="$1" f
  for f in chapters/*.adoc; do
    diff -q "$f" "$snap/$(basename "$f")" >/dev/null || return 1
  done
}

# ---- Step 1: snapshot the CURRENT (Stage 1) state, and verify the snapshot
rm -rf "$S1"                      # scratch snapshot dir only — never your real files
mkdir -p "$S1/chapters"
cp -p chapters/*.adoc "$S1/chapters/"
cp -p the-semantic-enterprise.adoc "$S1/"
verify_adocs "$S1/chapters" || { echo "ABORT: stage1 snapshot imperfect — nothing committed."; exit 1; }

# ---- Step 2: sanity — Stage 0 snapshot must contain exactly the same file set
diff <(cd chapters && ls -- *.adoc) <(cd "$S0/chapters" && ls -- *.adoc) >/dev/null \
  || { echo "ABORT: file sets differ between working tree and stage0 snapshot."; exit 1; }

rm -f .git/index.lock

# ---- Commit 1: Stage 0 (contents set back temporarily; files never removed)
cp -p "$S0"/chapters/*.adoc chapters/
cp -p "$S0/the-semantic-enterprise.adoc" the-semantic-enterprise.adoc
git add the-semantic-enterprise.adoc chapters merge_book.py .gitignore
git commit -m "Stage 0: mechanical fixes + chapter split

- Fix 415 malformed em-dashes (em-dash+hyphen artifact), typos
- Split monolith into chapters/01-14; master becomes include-based
  (reconstruction verified byte-identical; anchors travel with chapters;
  all 27 figure refs resolve)
- merge_book.py flattens includes for legacy tooling"

# ---- Commit 2: review + briefs
git add review-2026-06-11-technical-depth-and-style.md revision/ commit_stages.sh
git commit -m "Revision campaign: technical review + agent briefs 00-06

- Full technical-depth & style review (fact-check with sources)
- Briefs: plan, style charter, corrections, governed-joins doctrine,
  de-crypto + GDPR rebuild, multi-agent v2, reflexive loop (new chapter)"

# ---- Commit 3: Stage 1 (restore current contents)
cp -p "$S1"/chapters/*.adoc chapters/
cp -p "$S1/the-semantic-enterprise.adoc" the-semantic-enterprise.adoc
git add chapters the-semantic-enterprise.adoc
git commit -m "Stage 1: corrections + de-crypto (8 chapters, parallel agents)

- dbt-snapshots valid/system-time inversion corrected (Time chapter)
- Benchmarks refreshed (Spider 2.0, BIRD, dbt 2026); fabricated stats cut
  (MIT 34%, \$67B, 84%, 200-400% pods); Gartner wordings made exact
- EU AI Act updated for May 2026 Digital Omnibus
- Crypto/employer references recast as generic trading venue (incl. Bullish ref);
  MiCA -> MiFID II recategorisation / IBOR transition
- 3 TODO(author) markers for items needing author input
- Untouched by design: 300x/joins passages, multi-agent section,
  erasure section (Stage 2 rewrites per briefs 03/04/05)"

# ---- Step 3: PROOF — working tree must be identical to where we started
verify_adocs "$S1/chapters" \
  && diff -q the-semantic-enterprise.adoc "$S1/the-semantic-enterprise.adoc" >/dev/null \
  || { echo "ABORT: final state mismatch — your Stage 1 files are safe in $S1; restore with: cp $S1/chapters/*.adoc chapters/"; exit 1; }

rm -rf .revision-snapshots
echo "=== Done. Working tree verified identical to pre-script state. ==="
git log --oneline -3
