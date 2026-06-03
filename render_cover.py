"""Cover art for The Semantic Enterprise — Scarfe register, no baked-in text."""
import base64, os
from pathlib import Path
import httpx

OUT = Path("/home/iman/data-management/figures-draft"); OUT.mkdir(parents=True, exist_ok=True)
KEY = os.environ.get("OPENROUTER_API_KEY") or ""
if not KEY:
    for line in Path("/home/iman/cassie-project/.env").read_text().splitlines():
        if line.startswith("OPENROUTER_API_KEY="):
            KEY = line.split("=",1)[1].strip(); break

PROMPT = (
 "BOOK COVER illustration, PORTRAIT orientation. Savage-but-elegant editorial ink in the spirit of GERALD SCARFE and Ronald Searle: "
 "confident slashing pen line, a little ink-spatter, grotesque-wit and menace under control, intelligent and grown-up — never cute, never crosshatch-clutter. "
 "Warm off-white paper, mostly black ink with ONE cool teal spot-colour and small wounds of red. "
 "CENTRAL HERO: CRISP-BOT — a calm, coherent, slightly mischievous boxy vintage robot with a single round head-lamp eye, teal-lit — stands triumphant and in control, "
 "WEAVING with its hands a glowing luminous LATTICE of threads (warp and weft) that glues many small interlinked DOMAIN boxes into ONE coherent whole hovering above it — "
 "a woven web, the integrated 'colimit', the living glued ontology, radiant and ordered. Its expression is a wry subversive half-grin: it has won. "
 "BENEATH AND AROUND, the toppled old orthodoxy in ruin: a collapsing tangled STAR SCHEMA shedding barbed cables, a sinking fetid data-swamp of unlabelled table-cards, "
 "a cracked gilded tombstone half-buried, a snarl of dead wires. A couple of tiny feral toddler robot-bots scamper mischievously at its feet. "
 "The old world crumbles; the coherent woven world rises. "
 "CRITICAL: leave the entire TOP THIRD of the image as CLEAN EMPTY off-white space for a title to be added later. NO text, NO letters, NO words, NO numbers, NO signature, NO gibberish anywhere in the image — none at all. Pure illustration, clean negative space at the top. "
 "Dangerous, witty, hopeful — the rise of coherence after AI."
)

body = {"model":"google/gemini-3-pro-image-preview","messages":[{"role":"user","content":PROMPT}],
        "modalities":["image"],"image_config":{"aspect_ratio":"3:4"},"prompt_upsampling":True}
with httpx.Client(timeout=httpx.Timeout(connect=10,read=300,write=30,pool=10)) as c:
    r = c.post("https://openrouter.ai/api/v1/chat/completions", json=body,
               headers={"Authorization":f"Bearer {KEY}","Content-Type":"application/json"})
if r.status_code>=400:
    raise SystemExit(f"{r.status_code}: {r.text[:300]}")
msg=(r.json().get("choices") or [{}])[0].get("message",{})
url=(msg.get("images") or [{}])[0].get("image_url",{}).get("url","")
out=OUT/"00_cover_art.png"
out.write_bytes(base64.b64decode(url.split("base64,",1)[1]))
print(f"ok {out} ({out.stat().st_size//1024} KB)")
