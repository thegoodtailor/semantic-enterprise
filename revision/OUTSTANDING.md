# Outstanding — as of 16 July 2026

The book is submission-ready as it stands: 16 chapters, fact-checked, perishability-hardened,
its own experiments (TradeBench) placed as dated sidebars, its own notation (the creole),
the formal spine self-contained, figures cleaned. Everything below is *improvement*, not blocker.

## Approved in principle, not yet executed (from the digestibility review)

1. **ch01 formalism relocation.** "Intellectual Foundations" (7 dense paragraphs, page 3)
   moves to a new **"Foundations and Sources"** essay placed before References; ch01 keeps one
   confident pointer paragraph ("the math is old and it works; it arrives when you need it").
   While moving: dedupe the Kimball/Inmon/Dehghani positioning against ch04's "Where Serious
   People Disagree."
2. **Ontology pictures (2–3, R2 register)** for the non-relational moments:
   - the pushout, drawn — Trading and Finance gluing along the shared sub-theory S, with the
     naive-union collision beside it (ch03/ch04);
   - the prime-brokerage witness — two bridge paths visibly disagreeing on one concept (ch11);
   - optional: bridge anatomy (what maps / what's lost / what's partial).
   Generate via the existing pipeline (`render_missing_figures.py` pattern). ⚠ OpenRouter
   balance ~$36 — top up first.
3. **Two worked examples for digestibility:**
   - the pushout's everyday analogy, placed *before* the formal treatment: two org charts
     merging after an acquisition — glue along the people both companies agree exist; the
     naive union merges two different "Heads of Risk" because they share a title;
   - the reflexive loop end-to-end: wrong number reaches the board Monday → provenance names
     the definitions it staked → refutation panel kills one → assertion written → the same
     query self-corrects Thursday. One page, one incident, all four loops.

## Author's own actions

4. **Top up OpenRouter** (~$36 remaining of $1,605 lifetime).
5. **Read the fresh PDF cover to cover** — especially ch08 (rebuilt), ch11 (subsumed Formal
   Spine), the four TradeBench sidebars, the creole sections (ch04/ch12/ch15), and the six
   cleaned figures at print size (signed originals archived at `~/Books/figure-backups-signed/`).
6. **O'Reilly submission** — `proposal/oreilly-proposal.md` is complete. Consider adding one
   §5 differentiator line: *"the book's empirical claims ship with a public, reproducible
   experiment harness (TradeBench)"* — and arguably a line about the creole. Then:
   warm intro to an acquisitions editor if the network yields one; else proposals@oreilly.com
   with ch02 "The Shift" as the sample chapter.
7. **Team presentation** (the original second goal) — the Playbook + Laws + Appendix +
   TradeBench repo are the deck. The book is ready to be put into practice.

## Smaller / parked

8. **Creole conversions, remaining:** ch04/ch12/ch15 done; scan other chapters for stray
   conceptual notation on the next pass. Optional: add a `.creole` twin of TradeBench's
   `semantic_layer.yaml` to the public repo (nice proof the notation works as agent context).
9. **Audiobook rig** (`audiobook/`) — untouched through the entire campaign; if the spoken
   edition is still wanted, it needs re-recording against the current text.
10. **Repo housekeeping:** old review docs (`the-semantic-enterprise-review*.md`,
    `pdf-vs-adoc-comparison.md`) could move into `revision/`; `figure-map.md` is slightly
    stale post-cleanup.
11. **PDF weight:** 32 MB (figure PNGs). A compressed sharing copy (~8–10 MB, downscaled
    figures) is a 5-minute job on request.

## Standing editorial rules (apply to all future passes)

- Manifesto voice; intermediate-long phrases; filler/repetition hunt.
- **Antithesis rule:** the Y is the insight — cut the "not X" unless X is a genuinely held
  misconception being corrected.
- **Perishability policy** (`revision/perishability-policy.md`): dated sidebars for volatile
  claims; mechanism-level claims in prose.
- **No draft-self-reference:** the reader's book has no history.
- **Register-match inventions:** the creole is pseudocode, used confidently, fussed over never.
- Em-dashes: settled at the principled-pass level (ch02); leave the rest.
- TradeBench numbers: any new figure entering the book needs a run in the committed harness
  and the author's sign-off.

## Where everything lives

- Book: `github.com/thegoodtailor/semantic-enterprise` (chapters/ is the source; Action
  builds PDF+HTML per push — Actions → newest run → Artifacts).
- Experiments: `github.com/thegoodtailor/semantic-enterprise-experiments` (public, reproducible).
- Companion paper: subsumed into ch11; `enterprise-colimit` repo is archival.
- Proposal: `proposal/oreilly-proposal.md`. Conventions: `revision/editorial-conventions.md`.
