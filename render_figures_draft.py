"""First-look figure renders for The Semantic Enterprise.

Grown-up editorial register (NOT Robert Crumb crosshatch) + recurring mascots,
via Gemini 3 Pro Image on OpenRouter. Stills only.
"""
import base64, os, sys, time
from pathlib import Path
import httpx

OUT = Path("/home/iman/data-management/figures-draft"); OUT.mkdir(parents=True, exist_ok=True)
URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "google/gemini-3-pro-image-preview"
KEY = os.environ.get("OPENROUTER_API_KEY") or ""
if not KEY:
    # load from project .env
    for line in Path("/home/iman/cassie-project/.env").read_text().splitlines():
        if line.startswith("OPENROUTER_API_KEY="):
            KEY = line.split("=", 1)[1].strip(); break

# --- The locked style sheet (R1 editorial register) — Gerald Scarfe bite ---
EDITORIAL = (
    "Savage, biting editorial caricature for a serious business/technology book, in the spirit of GERALD SCARFE and Ralph Steadman: "
    "dangerous slashing pen-and-ink linework, whiplash strokes, splattered and dripping ink, grotesque expressive exaggeration, satirical venom and menace under the wit. "
    "This is political-caricature ferocity, NOT cute and NOT poised — it draws blood — but it stays intelligent and grown-up, never juvenile underground-comix crosshatch. "
    "Limited palette: black ink with flicked spatter on warm off-white paper, ONE spot-colour accent used like a wound. Confident negative space. "
    "Keep text in the image to AT MOST one or two large hand-scrawled punch-words; everything precise is carried by the caption, so leave clean space. "
)

# --- The two recurring mascots (describe identically every time for consistency) ---
TANGLEBOT = (
    "TANGLE-BOT, the recurring 'dumb AI' mascot: a small boxy vintage robot with a single round head-lamp eye and a rectangular torso, "
    "anxious posture, overwhelmed, entangled in a snarl of cables and wires, one or two sweat-beads flicked off its head. "
    "Rendered in the same clean elegant line as the rest — endearing and a little pitiable, never ugly. Warm-red spot-colour accent."
)
CRISPBOT = (
    "CRISP-BOT, the recurring 'coherent AI' mascot: the SAME boxy vintage robot design as Tangle-bot (same round head-lamp eye, same rectangular torso) "
    "but upright, calm, confident, uncluttered — one single tidy cable, posture relaxed, reading a clean single card. Cool-teal spot-colour accent."
)

JOBS = [
    # (filename, aspect, prompt)
    ("01_tax300x_cartoon.png", "16:9",
     EDITORIAL + "A single wide editorial cartoon making one savage argument: a STAR SCHEMA is strangling the machine. "
     "LEFT: " + TANGLEBOT + " The tangle around it is explicitly a STAR SCHEMA gone feral — one large central database FACT table, with five or six DIMENSION tables radiating around it like points of a star, and the foreign-key 'join' lines between them have multiplied into barbed, snaking, vicious cables that wrap around Tangle-bot's neck and limbs and STRANGLE it. It is gagging, overtaxed, feeding its last coins into a grotesque mechanical cash register that spits ink. Real menace — the schema is eating it alive. "
     "RIGHT: " + CRISPBOT + " calm, untouched, plugged into ONE single clean flat table-card, reading effortlessly, a single golden bar at its feet. "
     "The one punch-word allowed, large and hand-scrawled between them with an ink-flick: '300x'. Composition reads instantly left-to-right: the star schema devours, the flat table frees. Leave clean margin for a caption."),

    ("02_metadata_graveyard.png", "16:9",
     EDITORIAL + "A biting single editorial cartoon: a windswept graveyard of dead enterprise-data initiatives, tombstones leaning at savage angles, dead ivy clawing over them. "
     "EACH tombstone bears a DIFFERENT epitaph — do NOT repeat words across tombstones — drawn from these and only these, one per stone, legible: "
     "'THE GRAND UNIFIED DATA MODEL' (the largest, central), 'STANDALONE MDR', 'FIBO' (this one ornate and gilded — a beautiful embalmed corpse of a tombstone), 'THE DATA CATALOG', 'MULTI-YEAR ONTOLOGY PROJECT', and a fresh open grave marked 'DATA MESH (no semantic layer)'. "
     "In the foreground " + TANGLEBOT + " stands holding a single wilting flower at the gilded FIBO stone, mock-mourning. "
     "Mordant, dangerous, blackly funny — a mass grave of governance theatre. One small scrawled punch-word at most ('RETIRED'). Clean space for a caption."),

    ("03_cross_ontology_diagram.png", "16:9",
     "Clean, slick, modern vector-style ARCHITECTURE DIAGRAM for a serious technology book — the R2 register. "
     "Flat minimal design, generous whitespace, restrained palette (ink + soft teal + soft amber on white), thin confident connector lines, rounded rectangular nodes, crisp small sans-serif labels that are fully legible. "
     "Show THREE labelled domain blocks — 'Risk', 'Trading', 'Custody' — each drawn as a small stack of dimension tiles (a compact dimensional model). "
     "Curved labelled connectors ('bridge') link the three. One highlighted path traces Risk -> Trading -> Custody to show an analyst exploring across them. "
     "A soft shaded overlap region where the three meet, labelled 'composed view (access = intersection)'. "
     "Elegant, balanced, textbook-quality. No clutter, no overlap of labels, plenty of air."),
]

def gen(fn, aspect, prompt):
    out = OUT / fn
    body = {"model": MODEL, "messages": [{"role": "user", "content": prompt}],
            "modalities": ["image"], "image_config": {"aspect_ratio": aspect}, "prompt_upsampling": True}
    t0 = time.time()
    with httpx.Client(timeout=httpx.Timeout(connect=10, read=240, write=30, pool=10)) as c:
        r = c.post(URL, json=body, headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    if r.status_code >= 400:
        print(f"  !! {fn}: {r.status_code} {r.text[:200]}"); return
    msg = (r.json().get("choices") or [{}])[0].get("message", {})
    imgs = msg.get("images") or []
    url = (imgs[0].get("image_url") or {}).get("url", "") if imgs and isinstance(imgs[0], dict) else ""
    if "base64," not in url:
        print(f"  !! {fn}: no image bytes"); return
    out.write_bytes(base64.b64decode(url.split("base64,", 1)[1]))
    print(f"  ok {fn} ({out.stat().st_size//1024} KB, {time.time()-t0:.0f}s)")

if __name__ == "__main__":
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for fn, aspect, prompt in JOBS:
        if only and only not in fn:
            continue
        print(f"generating {fn} ...")
        gen(fn, aspect, prompt)
