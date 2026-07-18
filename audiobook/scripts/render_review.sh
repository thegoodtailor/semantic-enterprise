#!/bin/bash
# Cheap review render: all chapters except references, turbo v2.5, narrator voice.
source ~/.zshenv 2>/dev/null
export ELEVEN_MODEL=eleven_turbo_v2_5
cd "$(dirname "$0")/.."
mkdir -p out/review
for seg in segments/review/*.json; do
  base=$(basename "$seg" .json)
  [ "$base" = "16-references" ] && continue
  out="out/review/${base}.mp3"
  if [ -s "$out" ]; then echo "== $base already rendered, skipping"; continue; fi
  echo "== rendering $base"
  python3 scripts/tts.py "$seg" "$out" || echo "!! FAILED: $base"
done
echo "== ALL DONE"
