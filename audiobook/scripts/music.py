#!/usr/bin/env python3
"""Lay an ambient bed + sci-fi theme under a rendered mp3 (ElevenLabs Music API).

    python scripts/music.py out/sample_voice.mp3 out/sample.mp3        # mix
    python scripts/music.py --assets                                   # just (re)build assets

Assets (theme, bed, divider) generated once, cached in audiobook/music-assets/.
The divider.mp3 is consumed by tts.py at [[DIVIDER]] markers.
"""
from __future__ import annotations
import json, subprocess, sys, urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from voices import load_key  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "music-assets"

THEME_PROMPT = ("Opening theme for a science-fiction / posthuman audiobook in the BBC Radiophonic "
    "Workshop and 1970s science-documentary palette: analog modular synthesizer, eerie sine-wave "
    "oscillators, tape-loop textures, cosmic shimmer, mysterious and elegant, building to a bright "
    "resolving chord. Instrumental.")
BED_PROMPT = ("Sparse ambient drone bed to sit quietly UNDER spoken-word narration, BBC Radiophonic "
    "Workshop palette: slow evolving analog pads, a deep low hum, distant shimmer, no drums, no "
    "discernible melody, dark and contemplative, seamless. Instrumental.")
DIVIDER_PROMPT = ("A short three-second analog-synth transition sting in the BBC Radiophonic Workshop "
    "palette: a single rising-then-settling shimmer, eerie and elegant, a clean section divider. Instrumental.")
THEME_MS, BED_MS, DIVIDER_MS = 13000, 90000, 3000
BED_VOL = 0.13


def music(key, prompt, ms, out):
    req = urllib.request.Request("https://api.elevenlabs.io/v1/music",
        data=json.dumps({"prompt": prompt, "music_length_ms": ms}).encode(),
        headers={"xi-api-key": key, "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=300) as r:
        data = r.read()
    if len(data) < 2000:
        raise OSError("music response too small: " + data[:200].decode("utf8", "replace"))
    out.write_bytes(data)


def ff(args):
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *args], check=True)


def dur(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
        "format=duration", "-of", "default=nw=1:nk=1", str(p)]).strip() or 0)


def ensure_assets(key):
    ASSETS.mkdir(parents=True, exist_ok=True)
    out = {}
    for name, prompt, ms in (("theme", THEME_PROMPT, THEME_MS),
                             ("bed", BED_PROMPT, BED_MS),
                             ("divider", DIVIDER_PROMPT, DIVIDER_MS)):
        p = ASSETS / f"{name}.mp3"
        if not p.is_file():
            print(f"  generating {name}…", flush=True); music(key, prompt, ms, p)
        out[name] = p
    return out


def mix(inp, out):
    key = load_key()
    a = ensure_assets(key)
    theme, bed = a["theme"], a["bed"]
    work = out.parent / (out.stem + "_mus"); work.mkdir(exist_ok=True)
    nlen = dur(inp)
    bedloop = work / "bedloop.mp3"
    ff(["-stream_loop", "-1", "-i", str(bed), "-t", f"{nlen:.2f}", "-filter:a",
        f"volume={BED_VOL},afade=t=in:st=0:d=3,afade=t=out:st={max(0.0, nlen-4):.2f}:d=4",
        "-c:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", "-ac", "1", str(bedloop)])
    body = work / "body.mp3"
    ff(["-i", str(inp), "-i", str(bedloop), "-filter_complex",
        "[0:a]aresample=44100[v];[1:a]aresample=44100[b];[v][b]amix=inputs=2:duration=first:normalize=0[a]",
        "-map", "[a]", "-ac", "1", "-ar", "44100", "-c:a", "libmp3lame", "-b:a", "128k", str(body)])
    introtheme = work / "introtheme.mp3"
    ff(["-i", str(theme), "-filter:a", "afade=t=out:st=10:d=3",
        "-c:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", "-ac", "1", str(introtheme)])
    tmp = work / "intro_body.mp3"
    ff(["-i", str(introtheme), "-i", str(body), "-filter_complex",
        "[0:a][1:a]acrossfade=d=2:c1=tri:c2=tri[a]", "-map", "[a]",
        "-ac", "1", "-ar", "44100", "-c:a", "libmp3lame", "-b:a", "128k", str(tmp)])
    ff(["-i", str(tmp), "-i", str(theme), "-filter_complex",
        "[0:a][1:a]acrossfade=d=2:c1=tri:c2=tri[a]", "-map", "[a]",
        "-ac", "1", "-ar", "44100", "-c:a", "libmp3lame", "-b:a", "128k", str(out)])
    print(f"✓ {out} ({dur(out)/60:.1f} min)")


def main(argv):
    if argv and argv[0] == "--assets":
        ensure_assets(load_key()); print("assets ready in", ASSETS); return 0
    if len(argv) < 2:
        print(__doc__); return 1
    inp = (ROOT / argv[0]) if not Path(argv[0]).is_absolute() else Path(argv[0])
    out = (ROOT / argv[1]) if not Path(argv[1]).is_absolute() else Path(argv[1])
    out.parent.mkdir(parents=True, exist_ok=True)
    mix(inp, out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
