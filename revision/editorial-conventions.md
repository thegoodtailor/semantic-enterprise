# Editorial markup conventions

How the author flags edits for Claude to work through. Lightweight, drift-proof, invisible to the renderer.

## The marker

A single AsciiDoc line comment, **on its own line, at the start of the line**, directly above the paragraph/block it concerns:

```
//@ TAG: your note
```

`//` is an AsciiDoc comment only when it begins the line — so the marker must be on its own line, not tacked onto the end of a sentence (there it would render as literal text). Comments never appear in the PDF/HTML.

## Tags → how Claude handles each

| Tag | Meaning | Claude's action |
|-----|---------|-----------------|
| `STYLE` | tone / voice / phrasing | applies directly, within the voice rules; shows the diff |
| `CUT` | remove this | removes it |
| `FACT` | check/fix a claim or figure | web-verifies + fixes |
| `EXPAND` | needs more depth | drafts the expansion — **author certifies** (esp. domain claims) |
| `EXAMPLE` | add / improve a worked example | drafts at the rich-semantics altitude — **author certifies the finance** |
| `PROOF` | needs empirical backing / a citation | hunts for a real source/study; **if none exists, flags it — never fabricates evidence** (the one tag that can block) |
| `Q` | a question for Claude | answers inline, no edit |

No tag is fine too — an untagged `//@ make this punchier` still gets caught and classified.

## Workflow (one driver at a time, to avoid save-collisions)

1. **Author** edits the chapter `.adoc` files in VS Code, dropping `//@` lines. They don't show in preview.
2. Save → **commit & push** (VS Code Source Control), or just save and tell Claude "ch1 done".
3. **Claude** pulls, greps every `//@`, and returns a triage report (grouped by tag, with a plan per item) *before* editing.
4. Claude works through them, flips each resolved marker `//@` → `//@DONE — <what changed>` (audit trail), and pushes.
5. **Author** runs **Revert File** in VS Code before reopening that chapter, then reviews — closes or re-annotates.

Recommended cadence: **chapter by chapter**, not all at once — tighter loop, less collision.

## Finding open vs resolved

- Open items:   `grep -rn '//@ ' chapters/`
- Resolved:     `grep -rn '//@DONE' chapters/`

## Which files to edit

The book is `chapters/01-introduction.adoc` … `16-references.adoc`. Edit those, not the merged or HTML build artifacts. Suggested start: `chapters/01-introduction.adoc`.
