#!/usr/bin/env python3
"""Convert chapters/*.adoc into single-narrator segment manifests for review renders.

Keeps: headings (as beat lines), body prose, list items, sidebar titles + content,
admonition prose. Skips: code blocks (spoken marker), tables (spoken marker),
figures/captions, comments, anchors, attribute lines. Normalizes symbols and
strips inline AsciiDoc markup so the TTS reads clean text.

    python scripts/adoc2segments.py            # all chapters -> segments/review/
    python scripts/adoc2segments.py 03 12      # just chapters 03 and 12
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from voices import VOICES  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT.parent / "chapters"
OUT = ROOT / "segments" / "review"

INLINE = [
    (re.compile(r"image:[^\[]*\[[^\]]*\]"), ""),          # inline images
    (re.compile(r"(?:xref|link):[^\[]*\[([^\]]*)\]"), r"\1"),
    (re.compile(r"https?://\S+\[([^\]]*)\]"), r"\1"),
    (re.compile(r"https?://[^\s\]]+"), ""),               # bare URLs
    (re.compile(r"footnote:\[[^\]]*\]"), ""),
    (re.compile(r"\*\*([^*]+)\*\*"), r"\1"),
    (re.compile(r"\*([^*\n]+)\*"), r"\1"),
    (re.compile(r"__([^_]+)__"), r"\1"),
    (re.compile(r"\b_([^_\n]+)_\b"), r"\1"),
    (re.compile(r"``?([^`\n]+)``?"), r"\1"),
    (re.compile(r"\[\[[^\]]*\]\]"), ""),                  # inline anchors
]
SYMBOLS = [("→", " to "), ("≠", " is not "), ("≥", " at least "), ("≤", " at most "),
           ("×", " times "), ("±", " plus or minus "), ("†", ""), ("‡", ""),
           ("&amp;", " and "), ("&", " and "), ("#", " number ")]


def clean_inline(s: str) -> str:
    for pat, rep in INLINE:
        s = pat.sub(rep, s)
    for a, b in SYMBOLS:
        s = s.replace(a, b)
    s = s.replace("P&L", "P and L")
    return re.sub(r"[ \t]{2,}", " ", s).strip()


def convert(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    i, n = 0, len(lines)
    in_code = in_table = False
    pending_block_title = None

    def emit(par: str):
        par = par.strip()
        if par:
            out.append(par)

    buf: list[str] = []

    def flush():
        if buf:
            emit(clean_inline(" ".join(buf)))
            buf.clear()

    while i < n:
        raw = lines[i]
        line = raw.rstrip()
        i += 1

        if in_code:
            if line.startswith("----"):
                in_code = False
            continue
        if in_table:
            if line.startswith("|==="):
                in_table = False
            continue

        if line.startswith("----"):
            flush()
            in_code = True
            pending_block_title = None
            emit("Code example omitted.")
            continue
        if line.startswith("|==="):
            flush()
            in_table = True
            pending_block_title = None
            emit("Table omitted.")
            continue
        if line.startswith("image::"):
            flush()
            pending_block_title = None      # drop figure caption with the figure
            continue
        if (not line or line.startswith(("//", ":", "[#", "[["))
                or re.fullmatch(r"\[[^\]]*\]", line)):
            flush()
            continue
        if line.startswith("****"):          # sidebar delimiter
            flush()
            if pending_block_title:
                emit(clean_inline(pending_block_title))
                pending_block_title = None
            continue
        m = re.match(r"^(=+)\s+(.*)$", line)
        if m:
            flush()
            emit(clean_inline(m.group(2)))
            continue
        if line.startswith("."):             # block title (figure caption or sidebar title)
            flush()
            pending_block_title = line[1:].strip()
            continue
        m = re.match(r"^(\*+|\.+|-)\s+(.*)$", line)
        if m:
            flush()
            emit(clean_inline(m.group(2)))
            continue
        if pending_block_title:              # title belonged to a plain block: keep it
            emit(clean_inline(pending_block_title))
            pending_block_title = None
        buf.append(line.strip())
    flush()
    return "\n\n".join(out)


def main(argv):
    OUT.mkdir(parents=True, exist_ok=True)
    narrator = VOICES["narrator"]
    picks = argv or None
    files = sorted(CHAPTERS.glob("*.adoc"))
    total = 0
    for f in files:
        num = f.name.split("-", 1)[0]
        if picks and num not in picks:
            continue
        text = convert(f)
        seg = [{"voice": "narrator", "voice_id": narrator["voice_id"],
                "speed": narrator["speed"], "text": text}]
        dest = OUT / (f.stem + ".json")
        dest.write_text(json.dumps(seg, ensure_ascii=False, indent=1), encoding="utf-8")
        total += len(text)
        print(f"{f.stem:45s} {len(text):>7,} chars")
    print(f"{'TOTAL':45s} {total:>7,} chars  (~{total // 2:,} credits on turbo/flash v2.5)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
