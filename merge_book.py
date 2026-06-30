#!/usr/bin/env python3
"""Flatten the include-based master back into a single AsciiDoc file.

Usage:
  python3 merge_book.py                  # writes the-semantic-enterprise-merged.adoc
  python3 merge_book.py -o out.adoc      # custom output
  python3 merge_book.py --stdout         # print to stdout

For any legacy script that expects the monolith (render_full_set.py etc.),
point it at the merged file, or import flatten() from here.
"""
import argparse, re, sys
from pathlib import Path

MASTER = Path(__file__).parent / "the-semantic-enterprise.adoc"
INCLUDE_RE = re.compile(r"^include::(?P<target>[^\[]+)\[\]\s*$")


def flatten(master: Path = MASTER) -> str:
    out = []
    for line in master.read_text(encoding="utf-8").split("\n"):
        m = INCLUDE_RE.match(line)
        if m:
            out.append((master.parent / m.group("target")).read_text(encoding="utf-8"))
        else:
            out.append(line)
    text = "\n".join(out)
    text = text if text.endswith("\n") else text + "\n"
    return BANNER + text


BANNER = (
    "////\n"
    "=====================================================================\n"
    " GENERATED FILE — DO NOT EDIT.\n"
    " This is a flattened snapshot of the book, rebuilt from chapters/*.adoc\n"
    " for legacy tooling. Edit the REAL source in chapters/*.adoc, then run:\n"
    "     python3 merge_book.py\n"
    " Any edit made directly in this file is LOST on the next regenerate.\n"
    "=====================================================================\n"
    "////\n\n"
)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", default="the-semantic-enterprise-merged.adoc")
    ap.add_argument("--stdout", action="store_true")
    args = ap.parse_args()
    text = flatten()
    if args.stdout:
        sys.stdout.write(text)
    else:
        Path(args.output).write_text(text, encoding="utf-8")
        print(f"wrote {args.output} ({len(text.splitlines())} lines)")
