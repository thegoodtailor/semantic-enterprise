"""Generate the two figures that were referenced in the chapters but never drawn:
  figures/agent-picks-engine-joins.png   (ch02 The Shift, ch04 The Architecture)
  figures/reflexive-loop.png             (ch12 The Reflexive Loop)

Same R2 ("clean flat-vector diagram") style + same model/endpoint as render_full_set.py,
but writes directly to ./figures/<final-name>.png (no draft-numbering / wire step needed —
the image:: references are already in the chapters).

Run where your OpenRouter key lives (the Linux box, or anywhere with httpx + the key):
    pip install httpx           # if needed
    export OPENROUTER_API_KEY=sk-or-...     # or put it in a .env next to this file
    python3 render_missing_figures.py

Idempotent: skips a figure whose PNG already exists and is non-empty.
"""
import base64, os
from pathlib import Path
import httpx

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)
URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "google/gemini-3-pro-image-preview"

KEY = os.environ.get("OPENROUTER_API_KEY") or ""
if not KEY:
    env = Path(__file__).resolve().parent / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.startswith("OPENROUTER_API_KEY="):
                KEY = line.split("=", 1)[1].strip(); break

# --- locked R2 style (verbatim from render_full_set.py) ---
DIAGRAM = (
    "Clean, slick, modern FLAT VECTOR architecture diagram for a serious technology book. "
    "Generous whitespace, restrained palette (black ink + soft teal + soft amber on white), thin confident connector lines, rounded-rectangle nodes, "
    "crisp fully-legible small sans-serif labels, no clutter, no overlapping labels, plenty of air, balanced and textbook-quality. "
    "Use ONLY the labels specified below; invent no extra text and no jargon. "
)

JOBS = [
 ("agent-picks-engine-joins.png", "16:9", DIAGRAM +
  "Title idea conveyed visually, not written: 'the agent picks; the engine joins'. A single wide horizontal bar across the middle labelled 'SEMANTIC LAYER'. "
  "ABOVE the bar: one node labelled 'AGENT' reaching down to the bar and selecting three small chips labelled 'fields', 'filters', 'measure'; a small caption label 'picks'. "
  "BELOW the bar: a declared join graph — three small entity tiles labelled 'executions', 'counterparty', 'instrument' connected by two thin labelled arrows, one arrow labelled 'as-of join' and one labelled 'declared join'; a small caption label 'joins'. "
  "The agent above never connects directly to the entity tiles below — every line from the agent stops at the SEMANTIC LAYER bar. "
  "To the lower right, two governed output surfaces side by side: a wide flat rectangle labelled 'FLAT MARTS' with a small sub-label 'head', and a small four-point star shape labelled 'EXPLORES' with a small sub-label 'tail'. "
  "Clean, balanced, lots of air."),

 ("reflexive-loop.png", "1:1", DIAGRAM +
  "Four concentric circular loops nested around a central rounded bar labelled 'SEMANTIC LAYER'. Each loop is a labelled circular arrow, from innermost to outermost: "
  "'LOOP 1 — structural verification', 'LOOP 2 — usage feedback', 'LOOP 3 — falsification', 'LOOP 4 — calibration'. "
  "A single straight horizontal dashed line runs across the whole figure in the gap between Loop 2 and Loop 3, labelled 'observed / observing'. "
  "Everything inside that line (the SEMANTIC LAYER, Loop 1, Loop 2) is the system being observed; everything outside it (Loop 3, Loop 4) is the system observing itself. "
  "Concentric, symmetric, restrained palette, lots of air, textbook-quality."),
]


def gen(fn, aspect, prompt):
    out = OUT / fn
    if out.exists() and out.stat().st_size > 0:
        return f"  skip {fn} (exists)"
    body = {"model": MODEL, "messages": [{"role": "user", "content": prompt}],
            "modalities": ["image"], "image_config": {"aspect_ratio": aspect}, "prompt_upsampling": True}
    try:
        with httpx.Client(timeout=httpx.Timeout(connect=10, read=300, write=30, pool=10)) as c:
            r = c.post(URL, json=body, headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
        if r.status_code >= 400:
            return f"  !! {fn}: {r.status_code} {r.text[:160]}"
        msg = (r.json().get("choices") or [{}])[0].get("message", {})
        imgs = msg.get("images") or []
        url = (imgs[0].get("image_url") or {}).get("url", "") if imgs and isinstance(imgs[0], dict) else ""
        if "base64," not in url:
            return f"  !! {fn}: no image bytes"
        out.write_bytes(base64.b64decode(url.split("base64,", 1)[1]))
        return f"  ok {fn} ({out.stat().st_size // 1024} KB)"
    except Exception as e:
        return f"  !! {fn}: {e}"


if __name__ == "__main__":
    if not KEY:
        raise SystemExit("No OPENROUTER_API_KEY (set env var or put it in .env next to this script).")
    for j in JOBS:
        print(gen(*j), flush=True)
