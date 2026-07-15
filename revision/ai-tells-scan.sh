#!/bin/bash
# AI-prose tell scanner — mechanical layer.
# Based on Wikipedia's "Signs of AI Writing" + the book's own style charter
# (revision/01-style-charter.md). Regex layer only; cadence/enthusiasm tells
# need a human or LLM read. Run from the repo root: bash revision/ai-tells-scan.sh
# Scans rendered prose only: skips //@ editorial comments and code blocks.
cd "$(dirname "$0")/.." || exit 1

strip() { # drop comment lines and delimited code/listing blocks
  awk '/^(----|\.\.\.\.|====)$/{inblk=!inblk; next} inblk{next} /^\/\//{next} {print}' "$1"
}

count() { local f=$1 label=$2 re=$3
  local n=$(strip "$f" | grep -icE "$re")
  [ "$n" -gt 0 ] && printf "    %-38s %3d\n" "$label" "$n"
}

TOTAL_WORDS=0
for f in chapters/*.adoc; do
  words=$(strip "$f" | wc -w | tr -d ' ')
  TOTAL_WORDS=$((TOTAL_WORDS+words))
  dashes=$(strip "$f" | grep -oE '—' | wc -l | tr -d ' ')
  per1k=$(( words>0 ? dashes*1000/words : 0 ))
  echo "== $(basename $f)  (${words}w, em-dash ${dashes} = ${per1k}/1k words)"
  # --- antithesis / negation-pivot constructions ---
  count "$f" "not just/only/merely X, but Y"   "not (just|only|merely|simply) [^.]{0,60}(, but|; it|— it| but )"
  count "$f" "is not X. It is Y."              "(is|are|was|were) not [^.]{0,60}\. (It|They|That|This) (is|are|was|were) "
  count "$f" "isn't X — it's Y"                "(isn.t|not) [^.]{0,50}— (it.s|it is|they are)"
  count "$f" "not because X but because Y"     "not because [^.]{0,60}(but|;) because"
  # --- slop vocabulary ---
  count "$f" "delve/tapestry/testament"        "\b(delve|delving|tapestry|testament to)\b"
  count "$f" "crucial/pivotal/vital"           "\b(crucial|pivotal)\b"
  count "$f" "seamless/robust/vibrant"         "\b(seamless(ly)?|vibrant)\b"
  count "$f" "leverage/unlock/elevate/foster"  "\b(leverag(e|ing)|unlock(s|ing)?|elevat(e|ing)|foster(s|ing)?)\b"
  count "$f" "landscape/realm/journey"         "\b(landscape|realm|journey)\b"
  count "$f" "game-chang/transformative"       "\b(game.chang|transformative|revolutioniz)"
  # --- breathless / throat-clearing openers ---
  count "$f" "In today's / fast-paced / ever-" "\b(in today.s|fast.paced|ever.(evolving|changing))\b"
  count "$f" "Here's the thing / the reality"  "(here.s the (thing|catch)|the reality is|let.s be (clear|honest)|to be (clear|fair|honest)|make no mistake)"
  count "$f" "simply put / in essence"         "\b(simply put|in essence|at its core, |in short,)\b"
  # --- the user's named suspects ---
  count "$f" "honest/honestly"                 "\bhonest(ly)?\b"
  count "$f" "genuinely/truly/deeply"          "\b(genuinely|truly|deeply)\b"
  count "$f" "actually"                        "\bactually\b"
  # --- self-reflective (writing about the writing) ---
  count "$f" "this chapter/book/essay says"    "(this (chapter|book|essay|section) (argues|shows|makes|is about|has)|as (we|I) (have )?(seen|argued|noted|discussed))"
  # --- hedging the charter bans ---
  count "$f" "arguably/somewhat/perhaps"       "\b(arguably|somewhat|perhaps|quite possibly|it could be argued)\b"
  echo
done
echo "TOTAL WORDS (prose): $TOTAL_WORDS"
echo "Tells regex CANNOT catch (need the LLM/human read): breathless enthusiasm,"
echo "symmetric three-beat cadence, self-satisfied meta-commentary, uniform paragraph"
echo "rhythm, over-signposting. Run the per-chapter LLM pass for those."
