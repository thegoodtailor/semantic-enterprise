#!/usr/bin/env python3
"""Parse one chapter of the adoc into a voiced segments JSON.

    python scripts/segment.py "Exploring the Glued Ontology" segments/05-exploring.json
    python scripts/segment.py "<chapter title>" <out.json> [--flame "Sec A" "Sec B"]

Default voice = narrator (cosmic). Sections whose title is in --flame (or the whole
chapter via --all-flame) go to the maher register. Markup is stripped, figures/listings
skipped, em-dashes -> commas, === sections get a [[DIVIDER]] sting, headings get a beat.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from voices import VOICES  # noqa: E402

BOOK = Path("/home/iman/data-management/the-semantic-enterprise.adoc")


def inline(s: str) -> str:
    s = re.sub(r"<<[^,>]+,([^>]+)>>", r"\1", s)      # xref with text
    s = re.sub(r"<<[^>]+>>", "", s)                  # bare xref
    s = s.replace("`", "")                            # code spans
    s = s.replace("*", "").replace("_", "")           # bold/italic markers
    s = s.replace("—-", ", ").replace("—", ", ").replace("–", ", ")
    s = s.replace("P&L", "P and L").replace("R&R", "R and R").replace("&", " and ")
    s = re.sub(r"\s+,", ",", s)                       # tidy " ,"
    s = re.sub(r",\s*,", ",", s)
    s = re.sub(r"[ \t]{2,}", " ", s).strip()
    return s


def chapter_lines(title: str) -> list[str]:
    lines = BOOK.read_text(encoding="utf-8").split("\n")
    start = next(i for i, l in enumerate(lines) if l == f"== {title}")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("== ")), len(lines))
    return lines[start:end]


def parse(title: str, flame_sections: set[str], all_flame: bool):
    lines = chapter_lines(title)
    blocks: list[dict] = []
    cur_voice = "maher" if all_flame else "narrator"
    paras: list[str] = []

    def push():
        nonlocal paras
        if paras:
            v = VOICES[cur_voice]
            blocks.append({"voice": cur_voice, "voice_id": v["voice_id"],
                           "speed": v.get("speed", 1.0), "text": "\n\n".join(paras)})
            paras = []

    for ln in lines:
        s = ln.rstrip("\n")
        st = s.strip()
        if not st:
            continue
        if st.startswith("// ") or st.startswith("[#") or st.startswith("image::"):
            continue
        if st.startswith(".") and len(st) > 1 and st[1].isalpha() and st[1].isupper():
            continue  # figure/block caption
        if s.startswith("== "):                       # chapter title
            paras.append(inline(s[3:]))
            continue
        if s.startswith("==== "):                     # subsection -> heading beat
            paras.append(inline(s[5:]))
            continue
        if s.startswith("=== "):                       # section -> divider + heading
            sec = s[4:].strip()
            want = "maher" if (all_flame or sec in flame_sections) else "narrator"
            if want != cur_voice:
                push(); cur_voice = want
            paras.append("[[DIVIDER]]")
            paras.append(inline(sec))
            continue
        m = re.match(r"\*Pattern:\s*(.+?)\*$", st)     # *Pattern: X*
        if m:
            paras.append("Pattern. " + inline(m.group(1)))
            continue
        m = re.match(r"_([A-Z][a-z]+):_\s*(.*)$", st)  # _Context:_ ... etc.
        if m:
            paras.append(m.group(1) + ". " + inline(m.group(2)))
            continue
        if st.startswith("* "):                        # bullet -> sentence
            paras.append(inline(st[2:]))
            continue
        paras.append(inline(st))                       # body paragraph
    push()
    return blocks


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 1
    title, out = argv[0], argv[1]
    flame, all_flame = set(), False
    if "--all-flame" in argv:
        all_flame = True
    if "--flame" in argv:
        i = argv.index("--flame")
        flame = set(a for a in argv[i + 1:] if not a.startswith("--"))
    blocks = parse(title, flame, all_flame)
    outp = Path(out) if Path(out).is_absolute() else (Path(__file__).resolve().parent.parent / out)
    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(blocks, ensure_ascii=False, indent=2), encoding="utf-8")
    chars = sum(len(b["text"]) for b in blocks)
    print(f"✓ {outp}  ({len(blocks)} block(s), {chars} chars, voices: "
          f"{', '.join(sorted(set(b['voice'] for b in blocks)))})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
