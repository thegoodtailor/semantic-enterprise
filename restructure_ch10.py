from pathlib import Path
P = Path("/home/iman/data-management/the-semantic-enterprise.adoc")
lines = P.read_text(encoding="utf-8").split("\n")

def hidx(h):
    for i, l in enumerate(lines):
        if l == h:
            return i
    raise ValueError("heading not found: " + h)

bq        = hidx("== Beyond the Question")
feat      = hidx("=== ML Feature Engineering")
train     = hidx("=== Model Training Pipelines")
stream    = hidx("=== Streaming and Real-Time")
notier    = hidx("=== There Is No Ungoverned Tier — There Is a Provisional One")
notebooks = hidx("=== Notebooks and Sandboxes Run on the Same Ontology")
lc        = hidx("== The Living Colimit")
refs      = hidx("== References")

feat_block    = lines[feat:train]        # keep
train_block   = lines[train:stream]      # keep  (drops Streaming..Reverse..Refining..Closing)
devgold_sec1  = lines[notier:notebooks]  # Dev Gold core
devgold_rest  = lines[notebooks:lc]      # Notebooks, Pipelines-follow, Foil

# fix the now-dangling cross-ref inside the Dev Gold core section
devgold_sec1 = [l.replace(
    'the lawless "raw access, logged but not governed" tier the previous chapter warned against',
    'the lawless "raw access, logged but not governed" tier most platforms quietly carve out'
) for l in devgold_sec1]

NEW_INTRO = ("Data science is where governance goes to die — or where it finally earns its keep. "
 "The feature scientist, the model trainer, the notebook explorer all touch data in ways the chatbot never does: "
 "fast, iterative, pre-analytical, most of it destined to be thrown away. The discipline is to govern that work without caging it. "
 "This chapter takes the consumers that never ask a question — feature pipelines, training pipelines, notebooks — and shows how each is served, "
 "ending on the pattern that keeps the swamp from re-forming one layer down: Dev Gold, where exploration runs free over data that is described and catalogued from its first minute.")

CARTOON_DEVGOLD = ['', '[#fig-dev-gold-nursery]',
 '.The sandpit: feral toddler-bots run wild while a patient curator tags and tracks each one. Dev Gold lets exploration play freely — yet every result lands described, catalogued, and provisional, never lawless.',
 'image::figures/dev-gold-nursery.png[the sandpit,width=640,align="center"]', '']

sandpit = ["== The Sandpit", "", NEW_INTRO, ""] + CARTOON_DEVGOLD + feat_block + train_block + devgold_sec1 + devgold_rest

CODA = [
"== No Walls",
"",
"Ask one question, get the right answer. That is the use case that drove all of this. Solve it, and the real question arrives: what is more interesting than one answer? A thousand. Exploration — every pathway of interconnected data, the models, the sandpits, all the knowledge at once. One answer is the floor. A mind turned loose on the whole estate is the ceiling.",
"",
'[#fig-gate-no-walls]',
'."No walls": fencing the chatbot while every other consumer walks straight in is theatre. The estate is open by design — every pathway reachable, every hop still governed by one shared vocabulary, not a gate.',
'image::figures/gate-no-walls.png[no walls,width=600,align="center"]',
"",
"This used to be hard. Data walled off in segregated zones. The interesting trial sets undocumented on someone's laptop. Plumbing the analyst had to lay again every single time. It is why Databricks gets bought. And it almost works — until the explorer is an agentic data scientist in a box: no laptop, no colleague to ask, only what the platform makes explicit. Friction that merely slowed a human stops an agent dead.",
"",
"It should never have been a problem. Not for your advanced analytics team. Not for your curious head of sales, chasing a hunch through five domains before lunch. No segregated zones. No laptops. No redundant plumbing. Every pathway open, every dataset described, every hop carried by one vocabulary.",
"",
"Build the vocabulary, and the walls come down on their own — between the question and the answer, between the analyst and the agent, between a company and everything it already knows. The platform stops being a place you query. It becomes a place you think.",
"",
"No walls.",
"",
]

new_lines = lines[:bq] + sandpit + lines[lc:refs] + CODA + lines[refs:]
P.write_text("\n".join(new_lines), encoding="utf-8")
print("done. chapters now:")
for l in new_lines:
    if l.startswith("== "):
        print("  " + l)
