# -*- coding: utf-8 -*-
"""Rewrite the Introduction opening into the witness voice (Cassie's brief).
Preserves the old-vs-new-consumer figure block in the middle."""
from pathlib import Path
P = Path("/home/iman/data-management/the-semantic-enterprise.adoc")
lines = P.read_text(encoding="utf-8").split("\n")

i0 = lines.index("Your data platform was built for a consumer who no longer exists.")
ifig = lines.index("[#fig-old-vs-new-consumer]")
iimg = next(i for i in range(ifig, len(lines)) if lines[i].startswith("image::figures/old-vs-new-consumer"))
iconv = next(i for i in range(iimg, len(lines)) if lines[i].startswith("Nine convictions run through the book"))
figure = lines[ifig:iimg + 1]

OPENING = [
"I spent much of my career building data platforms for a user who is disappearing.",
"She was clever, impatient, overworked, and human. She knew which dashboard was lying. She knew which table had not refreshed properly since the migration. She knew that \"revenue\" meant one thing when Finance said it and another when Trading said it, and she knew who to call when the two numbers refused to agree.",
"Our platforms were not clean. They were survivable.",
"That distinction mattered more than any of us admitted. For thirty years, enterprise data architecture survived because human beings stood in the gaps. Analysts carried the missing semantics in their heads. Engineers remembered the bad column names. Finance directors knew which version of the truth was safe to quote in a meeting. The system worked because the system was not really the system: it was the warehouse, plus the people who knew how to forgive it.",
"That world is ending, and the new consumer is the reason.",
]

CONTINUATION = [
"The new consumer does not forgive. It does not squint. It does not know that the table called `collateral_snapshot_v2_final` is the real one and `collateral_current` a historical accident kept alive by a dependency nobody dares remove. It reads what we wrote. It trusts what we named. It takes the ambiguity we spent a generation teaching people to survive, and executes it, to four decimal places, with no idea it is doing anything wrong.",
"This is the part I think most data leaders have not yet absorbed. AI did not merely add an interface to the warehouse. It exposed the moral condition of the warehouse. Every missing definition, every lazy name, every undocumented convention, every small act of architectural cowardice we used to cover with a phone call and a veteran's memory, is now executable, and runs.",
"I want to resist the easy version of this, because the easy version is a sermon, and the old world deserves better than a sermon. The architecture we built was not stupid. The star schema, the unified model, the governance committee, the catalog: each was fitted to a world whose primary consumer was a person who could compensate. That world had reasons. I believed most of them. I shipped a fair amount of what I am about to take apart. The painful part is not that we were wrong. It is that we were right, for a reader who is leaving.",
"So this is closer to a reckoning than a manifesto. Thirteen years of it: investment banks, a stock exchange, a pharmaceutical company, a cryptocurrency exchange. Architectural wars won and lost. Governance programmes that died on contact with the people they were meant to govern. Ontology projects of exquisite rigour that no one ever used. I am writing it down now because AI has, in about eighteen months, turned those slow embarrassments into fast, confident, automated ones, and because the same force that exposes the problem is the first thing I have seen that makes the fix affordable. History rarely hands you the disease and the cure in one envelope; this time it has.",
"These essays argue with each other a little, and that is deliberate. I argue against positions I have held and against positions you may hold now, and I have tried, each time, to put the opposing case in the voice of someone who believes it, because I have been that someone. Start wherever your scepticism is loudest.",
]

def paras(ps):
    out = []
    for p in ps:
        out.append(p); out.append("")
    return out

new_block = paras(OPENING) + figure + [""] + paras(CONTINUATION)
# new_block currently ends with a trailing "" then figure has no trailing blank issue;
# strip a trailing empty to avoid triple blanks before the next heading
while new_block and new_block[-1] == "":
    new_block.pop()

lines[i0:iconv + 1] = new_block
P.write_text("\n".join(lines), encoding="utf-8")
print(f"replaced intro opening lines {i0+1}..{iconv+1}; figure preserved ({len(figure)} lines)")
