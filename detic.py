from pathlib import Path
P = Path("/home/iman/data-management/the-semantic-enterprise.adoc")
t = P.read_text(encoding="utf-8")

# (old, new) -- rhetorical 'honest/honestly' tics only. Technical terms kept:
# Morphism Honesty, Epistemic Honesty, bridge honesty, honest morphisms, honesty data,
# "most honest consumer" theme, "kept honest" (frontier-model idiom), health-metric "honest".
R = [
 # intro: gloss the bare colimit + drop the tic (Iman's instruction)
 ("as long as it maps honestly into the colimit; that AI",
  "as long as it maps into what category theory calls a *colimit* (explored in <<chap-architecture>>); that AI"),
 ("as long as it maps honestly into the colimit. Good governance",
  "as long as it maps into the colimit through bridges that declare their losses. Good governance"),
 ("as long as it maps honestly into the colimit. The architecture distributes",
  "as long as it maps into the colimit through bridges that declare their losses. The architecture distributes"),
 ("The honest claim is therefore not a single leap", "The claim is therefore not a single leap"),
 ("but the honest position is that the measurement has not been done.", "but the measurement has not been done."),
 ("address the organizational reality with honesty and empathy.", "address the organizational reality with candour and empathy."),
 ("is the only honest way to answer", "is the only faithful way to answer"),
 ("Name the exceptions honestly and require", "Name the exceptions and require"),
 ("To train a supervised model honestly, the features", "To train a supervised model correctly, the features"),
 ("The gaps are honest, not failures.", "The gaps are deliberate, not failures."),
 ("Name the cost honestly. Budget for it.", "Name the cost. Budget for it."),
 ("This is the honest reconciliation of", "This is the reconciliation of"),
 ("And then, because you need to be honest, state what this replaces.", "And then state what this replaces."),
 ("The honest response: the policy will be tested", "The response: the policy will be tested"),
 ("Honest position: hallucinations cannot be fully eliminated.", "Hallucinations cannot be fully eliminated."),
 ("Honesty about where this stands: my own platform", "Where this stands: my own platform"),
 ("Here is the honest position: training pipelines are a legitimate consumer",
  "Training pipelines are a legitimate consumer"),
 ("the honest objection", "the fair objection"),
 ("=== Scale, Honestly, As a Build Plan", "=== Scale: A Build Plan"),
 ("a build decision with two honest options.", "a build decision with two real options."),
 ("its vocabulary, kept honest by machines.", "its vocabulary, kept current by machines."),
 ("You need honesty.", "You need candour."),
 ("the honest answer to whether your data", "the answer to whether your data"),
 ("Name the human cost honestly.", "Name the human cost plainly."),
 ("Losses are documented honestly, not hidden", "Losses are documented, not hidden"),
 ("is uncomfortable and honest. Domain ontologies connected by explicit, honest morphisms",
  "is uncomfortable but true. Domain ontologies connected by explicit, honest morphisms"),
]

missing = []
for old, new in R:
    n = t.count(old)
    if n == 1:
        t = t.replace(old, new)
    else:
        missing.append((n, old[:60]))

P.write_text(t, encoding="utf-8")
print(f"applied {len(R)-len(missing)} of {len(R)} replacements")
for n, o in missing:
    print(f"  [{n}x] NOT-1: {o}")
