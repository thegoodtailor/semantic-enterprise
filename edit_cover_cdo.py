"""Img2img edit: label the cover gravestone 'THE CDO' and make the agent dance on it.
Keeps composition; edits only the tombstone + pose."""
import base64, os
from pathlib import Path
import httpx

D = Path("/home/iman/data-management/figures-draft")
KEY = os.environ.get("OPENROUTER_API_KEY") or ""
if not KEY:
    for line in Path("/home/iman/cassie-project/.env").read_text().splitlines():
        if line.startswith("OPENROUTER_API_KEY="):
            KEY = line.split("=",1)[1].strip(); break

src = D / "00_cover_art_pre-cdo.png"
b64 = base64.b64encode(src.read_bytes()).decode()

PROMPT = (
 "Edit this book-cover illustration. Keep the EXACT same Scarfe ink style, the warm off-white paper, the teal-and-red palette, "
 "the central robot, the glowing woven lattice of domain boxes it holds aloft, and the overall composition and framing — including the clean empty space at the very top for a title. "
 "Make only these changes: "
 "(1) On the cracked tombstone in the lower-right rubble, carve a clearly legible epitaph — the words 'THE CDO' large, with a smaller 'R.I.P.' beneath. Make this tombstone read unmistakably as a grave. "
 "(2) Adjust the central robot so its stance is unmistakably DANCING — joyful, triumphant, one leg kicked up, a jig of victory — planted on top of that grave, dancing on the CDO's tombstone. "
 "Change nothing else. NO other text, NO letters elsewhere, NO signature, NO artist name anywhere. Keep the top area clean and empty."
)

body = {"model":"google/gemini-3-pro-image-preview",
        "messages":[{"role":"user","content":[
            {"type":"text","text":PROMPT},
            {"type":"image_url","image_url":{"url":f"data:image/png;base64,{b64}"}}]}],
        "modalities":["image"],"image_config":{"aspect_ratio":"3:4"},"prompt_upsampling":True}
with httpx.Client(timeout=httpx.Timeout(connect=10,read=300,write=30,pool=10)) as c:
    r = c.post("https://openrouter.ai/api/v1/chat/completions", json=body,
               headers={"Authorization":f"Bearer {KEY}","Content-Type":"application/json"})
if r.status_code>=400:
    raise SystemExit(f"{r.status_code}: {r.text[:300]}")
msg=(r.json().get("choices") or [{}])[0].get("message",{})
url=(msg.get("images") or [{}])[0].get("image_url",{}).get("url","")
out = D / "00_cover_art.png"
out.write_bytes(base64.b64decode(url.split("base64,",1)[1]))
print(f"ok {out} ({out.stat().st_size//1024} KB)")
