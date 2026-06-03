"""Full figure set for The Semantic Enterprise.

R1 = Gerald-Scarfe-biting editorial cartoons (mascots locked via reference image).
R2 = clean slick vector architecture diagrams.
Gemini 3 Pro Image on OpenRouter. Parallel, idempotent.
"""
import base64, os, sys, time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import httpx

OUT = Path("/home/iman/data-management/figures-draft"); OUT.mkdir(parents=True, exist_ok=True)
URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "google/gemini-3-pro-image-preview"
KEY = os.environ.get("OPENROUTER_API_KEY") or ""
if not KEY:
    for line in Path("/home/iman/cassie-project/.env").read_text().splitlines():
        if line.startswith("OPENROUTER_API_KEY="):
            KEY = line.split("=", 1)[1].strip(); break

# --- locked R1 style: Gerald Scarfe bite ---
EDITORIAL = (
    "Savage, biting editorial caricature for a serious business/technology book, in the spirit of GERALD SCARFE and Ralph Steadman: "
    "dangerous slashing pen-and-ink linework, whiplash strokes, splattered and dripping ink, grotesque expressive exaggeration, satirical venom and menace under the wit. "
    "Political-caricature ferocity, NOT cute, NOT poised, never juvenile underground-comix crosshatch — it draws blood but stays intelligent and grown-up. "
    "Black ink with flicked spatter on warm off-white paper, ONE spot-colour accent used like a wound. Confident negative space. "
    "CRITICAL TEXT RULE: the ONLY text anywhere in the image is the single hand-scrawled PUNCH-WORD named below (plus any short labels explicitly listed). "
    "Render NO caption, NO sentence, NO paragraph, NO explanatory line, NO gibberish lettering of any kind. Leave the lower portion as clean EMPTY off-white paper — a real human caption is added later. Empty space is correct; do not fill it with text. "
)
# --- locked R2 style: slick clean diagram ---
DIAGRAM = (
    "Clean, slick, modern FLAT VECTOR architecture diagram for a serious technology book. "
    "Generous whitespace, restrained palette (black ink + soft teal + soft amber on white), thin confident connector lines, rounded-rectangle nodes, "
    "crisp fully-legible small sans-serif labels, no clutter, no overlapping labels, plenty of air, balanced and textbook-quality. "
    "Use ONLY the labels specified below; invent no extra text and no jargon. "
)
MASCOT_REF = (
    "Two recurring robot CHARACTERS, drawn in the same Scarfe ink style. TANGLE-BOT: an anxious boxy vintage robot, single round head-lamp eye that glows red when stressed, "
    "rectangular torso with a little dial, spindly limbs, perpetually snared in cables — the dumb/overwhelmed AI. CRISP-BOT: the SAME robot design but calm, upright, clean, "
    "uncluttered, often teal-lit — the coherent AI. Keep their design consistent across the book. Draw ONLY the scene described below. "
)

REF_IMG = OUT / "01_tax300x_cartoon.png"
_ref_b64 = None  # ref-image conditioning disabled — it bled the anchor's scene; text description holds the mascots

# (filename, register R1|R2, aspect, prompt)  -- 01/02/03 already approved, skipped
JOBS = [
 # ---------- R1 cartoons, one per argument ----------
 ("04_machine_doesnt_squint.png","R1","16:9", EDITORIAL+MASCOT_REF+
  "INTRO contrast (old way vs new way), reading left-to-right. LEFT: a shambolic, sweating human analyst SQUINTS and shrugs helplessly in front of a vast chaotic wall of dozens of conflicting dashboard widgets, handing a smudged muddled result to an UNHAPPY, frowning stakeholder. RIGHT: a cheerful, capable CRISP-BOT instantly hands one clean confident answer-card to a pleased, attractive-but-edgy executive drawn in Ronald-Searle / St-Trinian's style, who beams. The human compensates slowly and badly; the bot answers instantly and well. NO big punch-word — let the contrast carry it. Clean caption space."),
 ("05_context_per_token.png","R1","16:9", EDITORIAL+MASCOT_REF+
  "THE SHIFT (information density): TANGLE-BOT drowning in an avalanche of raw DDL printout / CREATE TABLE scrolls and sample-row confetti, going under. CRISP-BOT calmly reads a single small clean MENU card and gets the answer. Less paper, more meaning. Punch-words allowed: none or 'MEANING'. Caption space."),
 ("06_chatbot_confusion.png","R1","16:9", EDITORIAL+MASCOT_REF+
  "THE SHIFT foil ('just add a chatbot'): a grinning chatbot-bot bolted crudely onto a rotting dashboard, confidently inventing a fake refund policy on a speech-scroll while a customer recoils. Automated confusion delivered fast. Punch-word: 'CONFIDENT.' Caption space."),
 ("07_polysemy_position.png","R1","16:9", EDITORIAL+
  "LANGUAGE IS THE MATERIAL (polysemy): three figures — a trader, an accountant, a risk officer — each shout the same word 'POSITION' meaning three different things; a bewildered warehouse-machine in the middle blends their three meanings into one nonsense number pouring out. Data engineering as applied linguistics. Punch-word: 'POSITION'. Caption space."),
 ("08_restaurant_no_menu.png","R1","16:9", EDITORIAL+MASCOT_REF+
  "THE ARCHITECTURE opener: a data platform drawn as a chaotic restaurant with only a LOADING DOCK and NO menu. Trucks dump crates of RAW INGREDIENTS in a heap — lots of actual tumbling FOOD spilling everywhere: tomatoes, a whole fish, carrots, cabbages, a side of raw red meat, spilled flour, cracking eggs — pouring out of broken crates. TANGLE-BOT rummages waist-deep in the food pile trying to assemble something edible; no kitchen, no chef. Punch-word: 'NO MENU.' Caption space."),
 ("09_bronze_witness.png","R1","16:9", EDITORIAL+MASCOT_REF+
  "BRONZE the faithful witness: a courtroom. TANGLE-BOT sits in the witness box, one hand raised taking the oath, the other resting on a thick stack of raw printouts labelled as the producer's original data. A court-stenographer robot transcribes its words VERBATIM, word for word, changing nothing — warts, typos and all. The whole scene reads clearly as 'the record is taken down exactly as given and never edited.' Punch-word: 'SWORN.' Caption space."),
 ("10_data_swamp.png","R1","16:9", EDITORIAL+MASCOT_REF+
  "GOLD swamp: a fetid swamp of hundreds of half-sunk, unlabelled database-table cards, a confused TANGLE-BOT sinking to its eye-lamp, mislabelled signs, nobody trusts the numbers. The fate of an uncatalogued Gold layer. Punch-word: 'SWAMP.' Caption space."),
 ("11_two_questions_auditor.png","R1","16:9", EDITORIAL+MASCOT_REF+
  "TIME (two questions): CENTRED, balanced composition — a sweating TANGLE-BOT stands squarely in the MIDDLE of the frame, its body bearing TWO clock-faces showing different times, one labelled 'TRUE', one 'REPORTED'. A stern auditor in a long coat leans in from one side and demands an answer. Keep the robot centred and symmetrical in frame. Punch-word: 'WHEN?' Caption space."),
 ("12_bitemporal_overkill.png","R1","16:9", EDITORIAL+MASCOT_REF+
  "TIME (the overkill Iman hates): TANGLE-BOT buried alive under an absurd mountain of identical valid_from / valid_to / system_from / system_to date-columns bolted onto EVERY tiny reference table (even a table of country names), crushed by temporal machinery nobody will ever query. Two clocks on every row = madness. Punch-word: 'OVERKILL.' Caption space."),
 ("13_forty_workbooks.png","R1","16:9", EDITORIAL+
  "DEATH OF THE DASHBOARD (the 40-workbook problem shown as its CAUSE): a frantic open-plan office, a long daisy-chain of analysts each hunched over their own laptop, every screen a 'REVENUE' dashboard showing a DIFFERENT number, each analyst frantically COPYING over the shoulder of the next so the discrepancy multiplies down the line — forty people, forty different 'true' numbers, nobody able to reconcile them. Punch-word: 'REVENUE?' Caption space."),
 ("14_guess_vs_reason.png","R1","16:9", EDITORIAL+MASCOT_REF+
  "AGENTIC INTELLIGENCE: split scene. LEFT, TANGLE-BOT blindfolded, throwing darts wildly at a board of random numbers (guessing). RIGHT, CRISP-BOT reading a clean governed stack and calmly reasoning to the right answer. The difference is infrastructure, not IQ. Punch-words: 'GUESS / REASON.' Caption space."),
 ("15_multiagent_amplify.png","R1","16:9", EDITORIAL+MASCOT_REF+
  "AGENTIC (17x error amplification): a chaotic newsroom of several TANGLE-BOTS shouting different definitions of the same word at each other, each amplifying the others' errors into a screaming feedback loop, the 'house view' coming out as garbage. More agents without shared meaning = multiplied confusion. Punch-word: '17x.' Caption space."),
 ("16_curator_vs_committee.png","R1","16:9", EDITORIAL+MASCOT_REF+
  "BUILDING WITH AI (continuous vs quarterly): RIGHT, a tireless CRISP-BOT curator working every second, glossary kept spotless. LEFT, a dusty governance COMMITTEE of humans asleep around a boardroom table, a 'QUARTERLY REVIEW' calendar thick with cobwebs, the data already changed three times. Punch-word: 'ASLEEP.' Caption space."),
 ("17_gate_no_walls.png","R1","16:9", EDITORIAL+MASCOT_REF+
  "THE CONSUMERS YOU FORGOT: a proud locked SECURITY GATE (the semantic layer) guarding the front of a building that HAS NO WALLS — a crowd of other consumers (pipelines, notebooks, feeds drawn as little bots) stroll in freely around the sides. Governing the chatbot while ignoring everyone else. Punch-word: 'NO WALLS.' Caption space."),
 ("18_dev_gold_no_lawless.png","R1","16:9", EDITORIAL+MASCOT_REF+
  "DATA SCIENCE & DEV GOLD, warm and funny: a NURSERY SANDBOX full of mischievous TODDLER BABY-BOTS — small, round, naughty and a bit feral in the anarchic spirit of Ronald Searle's St Trinian's: one biting another, one flinging sand, one scrawling on the wall, one gnawing a cable with tiny sharp teeth — chaos, but bursting with potential. CRISP-BOT stands among them as a calm, fond teacher/matron, clipboard in hand, tracking each toddler's development and planning a curriculum, gently tagging each little bot with a small 'DEV GOLD' label. Affectionate, hopeful, a little dangerous — the feral toddlers show data science has teeth and promise. Punch-word: 'DEV GOLD.' Caption space."),
 ("19_board_three_sentences.png","R1","16:9", EDITORIAL+
  "THE PLAYBOOK: a bored board of directors buried under an avalanche of a 50-slide strategy deck cascading off the table, while a sharp presenter holds up a SINGLE clean page. If your strategy needs fifty slides, it isn't a strategy. Punch-word: 'ONE PAGE.' Caption space."),
 # ---------- R2 slick diagrams ----------
 ("D1_medallion_layers.png","R2","16:9", DIAGRAM+
  "Three stacked horizontal layers labelled 'BRONZE', 'SILVER', 'GOLD', each with its one-line epistemic question to its right: Bronze 'what did the producer say?', Silver 'what does it mean in our language?', Gold 'what do we know?'. Above all three sits a wide bar 'SEMANTIC LAYER' as the single consumption face, with small consumer icons (analyst, agent, dashboard) reaching it. Clean upward flow arrows."),
 ("D2_silver_vs_gold.png","R2","16:9", DIAGRAM+
  "Side-by-side comparison. LEFT labelled 'SILVER — dimensional': a small star of a central fact tile with a few dimension tiles, tagged 'grain', 'SCD2', 'conformed'. RIGHT labelled 'GOLD — flat': one wide single row of many columns, tagged 'denormalized', 'question-driven', 'no joins'. Same data, two shapes. A small 'semantic layer' bar spanning both."),
 ("D3_colimit_composition.png","R2","16:9", DIAGRAM+
  "The formal centrepiece. Several labelled domain nodes ('Trading','Finance','Compliance','Custody') drawn as small category boxes; curved labelled 'bridge' arrows (morphisms) between the ones that share a concept; converging into one larger node labelled 'the colimit — the integrated view'. Elegant, mathematical-but-friendly, lots of air."),
 ("D4_sole_interface.png","R2","16:9", DIAGRAM+
  "A single governed funnel: many consumer icons (human analyst, AI agent, dashboard, API, regulator) on the left all routed through ONE central bar labelled 'SEMANTIC LAYER' before reaching the governed data store on the right. One faint dotted bypass arrow attempting to go around it is shown crossed out. One funnel, every consumer."),
 ("D5_two_clocks.png","R2","16:9", DIAGRAM+
  "A clean two-axis plot: x-axis 'valid time (when it was true)', y-axis 'system time (when we learned it)'. A single fact plotted as a dot; a correction draws a second dot moved back-and-up with a small arrow; the original dot stays (never overwritten). Minimal, precise, one fact two clocks."),
 ("D6_three_tier_vocab.png","R2","16:9", DIAGRAM+
  "Three stacked tiers with a single downward 'upstream always wins' arrow through them: top 'TIER 1 — Glossary (business definitions)', middle 'TIER 2 — Schema definition (the LDM)', bottom 'TIER 3 — Semantic layer (consumption)'. A term 'revenue' shown inheriting unchanged down the three tiers."),
 ("D7_intelligence_stack.png","R2","9:16", DIAGRAM+
  "Five stacked layers, each depending on the one below, labelled bottom-to-top: '1 Governed data (medallion)', '2 Semantic layer', '3 Conversational interface', '4 Agentic intelligence', '5 Autonomous research'. A side note 'meaning flows up; skip a layer and it collapses'. Clean vertical stack."),
 ("D8_living_colimit_mesh.png","R2","16:9", DIAGRAM+
  "The verification mesh. Several domain nodes each with a small 'verification agent' badge; a central 'coordinator' node; bridges between domains; ONE bridge highlighted amber as a flagged 'witness' on a single span; a side gauge labelled 'colimit health' like an uptime dial. Always-on, self-checking. Clean and confident."),
]

def build_content(reg, prompt):
    if reg == "R1" and _ref_b64:
        return [{"type":"text","text":prompt},
                {"type":"image_url","image_url":{"url":f"data:image/png;base64,{_ref_b64}"}}]
    return prompt

def gen(fn, reg, aspect, prompt):
    out = OUT / fn
    if out.exists() and out.stat().st_size > 0:
        return f"  skip {fn} (exists)"
    body = {"model": MODEL, "messages":[{"role":"user","content":build_content(reg,prompt)}],
            "modalities":["image"], "image_config":{"aspect_ratio":aspect}, "prompt_upsampling": True}
    try:
        with httpx.Client(timeout=httpx.Timeout(connect=10,read=300,write=30,pool=10)) as c:
            r = c.post(URL, json=body, headers={"Authorization":f"Bearer {KEY}","Content-Type":"application/json"})
        if r.status_code >= 400:
            return f"  !! {fn}: {r.status_code} {r.text[:160]}"
        msg = (r.json().get("choices") or [{}])[0].get("message", {})
        imgs = msg.get("images") or []
        url = (imgs[0].get("image_url") or {}).get("url","") if imgs and isinstance(imgs[0],dict) else ""
        if "base64," not in url:
            return f"  !! {fn}: no image bytes"
        out.write_bytes(base64.b64decode(url.split("base64,",1)[1]))
        return f"  ok {fn} ({out.stat().st_size//1024} KB)"
    except Exception as e:
        return f"  !! {fn}: {e}"

if __name__ == "__main__":
    print(f"ref image loaded: {_ref_b64 is not None}  | jobs: {len(JOBS)}")
    with ThreadPoolExecutor(max_workers=5) as ex:
        futs = {ex.submit(gen, *j): j[0] for j in JOBS}
        for f in as_completed(futs):
            print(f.result(), flush=True)
