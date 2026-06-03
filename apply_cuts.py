# -*- coding: utf-8 -*-
from pathlib import Path
P = Path("/home/iman/data-management/the-semantic-enterprise.adoc")
t = P.read_text(encoding="utf-8")

R = []

# ---- #3: the "It must be ..." prose-list -> a real bulleted list ----
R.append((
'''If the semantic layer is the only interface through which consumers reach the data, then the obligations on it are correspondingly heavy. A semantic layer that cannot bear those obligations will be bypassed, and a semantic layer that is routinely bypassed is not an interface —- it is a suggestion.

It must be complete enough for the work. A semantic layer that exposes ten dashboards’ worth of canned measures and stops there is not an interface; it is a reporting surface. The semantic layer must expose every entity, every defensible measure, every meaningful join, every temporal contract —- not as a final state, but as a continuously expanding surface where the question "is this available?" has a near-universal "yes" for the questions the business actually asks.

It must be fast enough. If a query that takes ten seconds through direct SQL takes five minutes through the semantic layer, the layer will be bypassed regardless of governance. Performance is the operational precondition for the sole-interface commitment to be honoured. No governance framework survives a five-minute wait time when the alternative is a ten-second query.

It must be capable enough for exploratory work. The most common reason analysts want direct SQL is that they are exploring —- composing questions they have not asked before, iterating on half-formed ideas, sometimes failing and discarding. The semantic layer must support this mode, not only the canned-question mode. If it does not, it has implicitly defined exploration as something that happens outside the architecture, and exploration is exactly where new metric definitions are born and where fragmentation begins. An architecture that forces exploration outside its boundaries is an architecture that generates its own competitors.

It must have a real extension process. "Add it to the semantic layer" must be an intake that returns in days, not quarters. If extending the layer takes longer than building a workaround, the workarounds will accumulate and the layer will atrophy. A semantic-layer team without a working intake is a bottleneck dressed up as governance, and the organization will route around it the way water routes around a rock —- not out of malice, but out of necessity.

It must be well-instrumented. Every request the layer cannot serve is signal. Every workaround that emerges in the wild is signal. The layer’s owners must see this signal in near-real-time, not at a quarterly review. The gaps where consumers reach for bypasses —- whether agentic or human —- must be visible to the team that owns the layer, because those gaps are the layer’s roadmap. A semantic layer that does not know where it is failing is a semantic layer that will fail in the same places indefinitely.''',
'''If the semantic layer is the only interface through which consumers reach the data, the obligations on it are heavy. A layer that cannot bear them gets bypassed — and a layer that is routinely bypassed is not an interface, it is a suggestion. It must clear five bars:

* *Complete enough.* A layer that exposes ten dashboards’ worth of canned measures and stops is a reporting surface, not an interface. It must expose every entity, every defensible measure, every meaningful join, every temporal contract — a continuously expanding surface where "is this available?" is a near-universal yes for the questions the business actually asks.
* *Fast enough.* If a ten-second direct query takes five minutes through the layer, the layer gets bypassed regardless of governance. No framework survives a five-minute wait when the alternative is ten seconds.
* *Capable enough for exploration.* The most common reason analysts reach for direct SQL is that they are exploring — composing questions they have not asked, iterating on half-formed ideas, failing and discarding. The layer must support that mode, not only the canned-question mode. Force exploration outside the architecture and the architecture generates its own competitors — exploration is exactly where new metric definitions are born and where fragmentation begins.
* *Extensible in days, not quarters.* "Add it to the semantic layer" must be an intake that returns in days. If extending the layer is slower than building a workaround, the workarounds accumulate and the layer atrophies. A semantic-layer team without a working intake is a bottleneck dressed up as governance.
* *Well-instrumented.* Every request the layer cannot serve is signal; every workaround in the wild is signal. The owners must see it in near-real-time, not at a quarterly review — those gaps are the layer’s roadmap. A layer that does not know where it is failing fails in the same places indefinitely.'''))

# ---- #4: cut the hand-wringing closer ----
R.append((
'''

These are real costs, not theoretical ones. A team that reads this section and thinks "that won’t happen to us" is the team most likely to discover these costs the hard way.''',
''))

# ---- #5a: drop the dialogue framing ----
R.append((
'As I told a sales team planning their AI roadmap: "Let’s nail phase one. Let’s get everything else out of the way first and then move on to the exciting things, because they depend on the foundation being solid." Fuel before vehicle.',
'Nail phase one before the exciting things; the exciting things depend on the foundation being solid. Fuel before vehicle.'))

# ---- #5b: drop the team-lead anecdote framing ----
R.append((
'One of my team leads said something that stuck with me: "I want to move beyond RAG. I want the warehouse to be the memory. I want smarter ways to interface with our data in an exploratory way."\n\nShe was articulating the architectural endpoint. RAG treats documents as the knowledge base,',
'The architectural endpoint is to move beyond RAG and make the warehouse itself the memory. RAG treats documents as the knowledge base,'))

# ---- #6: keep the barb, cut the throat-clearing ----
R.append((
'Every prescriptive essay risks becoming the thing it critiques. If this playbook becomes a fifty-slide deck presented to a governance committee, it has failed. If it becomes a multi-year program with a steering committee and quarterly reviews, it has failed. If you are reading this in a committee meeting, you are already doing it wrong.',
'If this playbook becomes a fifty-slide deck for a governance committee, or a multi-year program with a steering committee and quarterly reviews, it has failed. If you are reading this in a committee meeting, you are already doing it wrong.'))

# ---- #7: drop the thrice-repeated aphorism (3rd instance) ----
R.append((
'History rarely delivers the disease and the cure in the same package, but here it has. AI demands the architecture, and AI makes it viable.',
'AI demands the architecture, and AI makes it viable.'))

# ---- anything-else: de-dupe the aphorism (2nd instance, now orphaned) ----
R.append((
'History rarely delivers the disease and the cure in the same package.\n\nAI demands: clean definitions,',
'AI demands: clean definitions,'))

applied, missed = 0, []
for o, n in R:
    c = t.count(o)
    if c == 1:
        t = t.replace(o, n); applied += 1
    else:
        missed.append((c, o[:55]))
P.write_text(t, encoding="utf-8")
print(f"applied {applied}/{len(R)}")
for m in missed:
    print("  MISS", m)
print("remaining 'History rarely delivers':", t.count("History rarely delivers the disease and the cure"))
