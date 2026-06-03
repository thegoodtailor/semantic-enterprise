#!/usr/bin/env python3
"""Render a segment manifest to a stitched mp3 via the ElevenLabs API.

Segments JSON = list of blocks: [{"voice","voice_id","text","speed"?}, ...].
In a block's text: blank line = paragraph; a short standalone line = heading (beat);
"[[PAUSE]]" = silent lead-in; "[[DIVIDER]]" = a short musical section-divider sting.

    python scripts/tts.py segments/sample.json out/sample_voice.mp3
"""
from __future__ import annotations
import hashlib, json, re, subprocess, sys, tempfile, urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from voices import MODEL, SETTINGS, load_key  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
MAX_CHARS = 2400
SWITCH_PAUSE = 0.7
SECTION_LEADIN = 0.7
AFTER_NAME = 0.5
DIVIDER_PAD = 0.35                       # silence either side of a divider sting
DIVIDER_ASSET = ROOT / "music-assets" / "divider.mp3"
PRON_PATH = ROOT / "pronunciation.json"
LETTER = r"A-Za-zÀ-ÿĀ-ɏ’'\-"


def load_pron():
    if not PRON_PATH.exists():
        return None, {}
    m = json.loads(PRON_PATH.read_text(encoding="utf-8"))
    keys = sorted(m, key=len, reverse=True)
    pat = re.compile(rf"(?<![{LETTER}])(" + "|".join(re.escape(k) for k in keys) + rf")(?![{LETTER}])")
    return pat, m


def apply_pron(text, pat, m):
    return text if pat is None else pat.sub(lambda mo: m[mo.group(1)], text)


def is_heading(p):
    p = p.strip()
    return 0 < len(p) <= 60 and len(p.split()) <= 8 and not p.endswith((".", "!", "?", ":", ","))


def chunk_block(text):
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    units, buf = [], []

    def flush():
        if buf:
            units.append(("\n\n".join(buf), "body")); buf.clear()

    for p in paras:
        if p == "[[PAUSE]]":
            flush(); units.append((None, "pause"))
        elif p == "[[DIVIDER]]":
            flush(); units.append((None, "divider"))
        elif is_heading(p):
            flush(); units.append((p, "heading"))
        elif len(p) > MAX_CHARS:
            flush()
            for c in split_sentences(p):
                units.append((c, "body"))
        elif sum(len(x) + 2 for x in buf) + len(p) > MAX_CHARS:
            flush(); buf.append(p)
        else:
            buf.append(p)
    flush()
    return units


def split_sentences(text):
    parts = re.split(r"(?<=[.!?])\s+", text.replace("\n", " ").strip())
    chunks, cur = [], ""
    for s in parts:
        if len(cur) + len(s) + 1 <= MAX_CHARS:
            cur = (cur + " " + s).strip()
        else:
            if cur:
                chunks.append(cur)
            cur = s
    if cur:
        chunks.append(cur)
    return chunks


def tts(key, voice_id, text, dest, retries=4):
    import time
    body = {"text": text, "model_id": MODEL, "voice_settings": SETTINGS}
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        data=json.dumps(body).encode(),
        headers={"xi-api-key": key, "Content-Type": "application/json"}, method="POST")
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                data = r.read()
            if len(data) < 1000:
                raise OSError(f"response too small ({len(data)}B): {data[:200]!r}")
            dest.write_bytes(data); return
        except Exception as e:
            if attempt == retries - 1:
                raise
            wait = 2 ** attempt
            print(f"    retry {attempt+1} after {wait}s ({e})"); time.sleep(wait)


def atempo(src, dst, speed):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                    "-filter:a", f"atempo={speed}", "-b:a", "128k", str(dst)], check=True)


def silence(dst, sec):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi",
                    "-i", "anullsrc=r=44100:cl=mono", "-t", str(sec), "-b:a", "128k", str(dst)], check=True)


def reencode(src, dst):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                    "-ac", "1", "-ar", "44100", "-b:a", "128k", str(dst)], check=True)


def concat(parts, out):
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        for p in parts:
            f.write(f"file '{p.resolve()}'\n")
        lf = f.name
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
                    "-i", lf, "-c:a", "libmp3lame", "-b:a", "128k", str(out)], check=True)
    Path(lf).unlink(missing_ok=True)


def main(argv):
    if len(argv) < 2:
        print(__doc__); return 1
    seg = (ROOT / argv[0]) if not Path(argv[0]).is_absolute() else Path(argv[0])
    out = (ROOT / argv[1]) if not Path(argv[1]).is_absolute() else Path(argv[1])
    out.parent.mkdir(parents=True, exist_ok=True)
    key = load_key()
    pat, m = load_pron()
    blocks = json.loads(seg.read_text(encoding="utf-8"))
    wd = out.parent / (out.stem + "_chunks"); wd.mkdir(exist_ok=True)
    sw, lead, after = wd / "_sw.mp3", wd / "_lead.mp3", wd / "_after.mp3"
    silence(sw, SWITCH_PAUSE); silence(lead, SECTION_LEADIN); silence(after, AFTER_NAME)
    div_asset = None
    if DIVIDER_ASSET.exists():
        pad = wd / "_divpad.mp3"; silence(pad, DIVIDER_PAD)
        dre = wd / "_div.mp3"; reencode(DIVIDER_ASSET, dre)
        div_asset = (pad, dre)
    skey = json.dumps(SETTINGS, sort_keys=True)
    ordered, counter, prev_voice = [], [0], None

    def render(chunk, voice, vid, speed):
        n = counter[0]
        h = hashlib.sha1((MODEL + skey + voice + chunk).encode()).hexdigest()[:8]
        raw = wd / f"{voice}-{h}.mp3"
        oc = (wd / f"{voice}-{h}-x{speed}.mp3") if abs(speed - 1) > 1e-6 else raw
        if oc.exists() and oc.stat().st_size > 1000:
            print(f"  [{voice:8s}] unit {n} cached")
        else:
            tts(key, vid, chunk, raw)
            if abs(speed - 1) > 1e-6:
                atempo(raw, oc, speed)
            print(f"  [{voice:8s}] unit {n} ({len(chunk)} chars)")
        counter[0] += 1
        return oc

    for b in blocks:
        voice, vid, speed = b["voice"], b["voice_id"], b.get("speed", 1.0)
        for chunk, kind in chunk_block(apply_pron(b["text"], pat, m)):
            if kind == "pause":
                ordered.append(lead); continue
            if kind == "divider":
                if div_asset:
                    ordered += [div_asset[0], div_asset[1], div_asset[0]]
                else:
                    ordered.append(lead)
                prev_voice = None
                continue
            if kind == "heading":
                ordered += [lead, render(chunk, voice, vid, speed), after]
                prev_voice = voice; continue
            if prev_voice is not None and voice != prev_voice:
                ordered.append(sw)
            ordered.append(render(chunk, voice, vid, speed))
            prev_voice = voice
    concat(ordered, out)
    print(f"\n✓ stitched {counter[0]} chunks -> {out} ({out.stat().st_size} B)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
