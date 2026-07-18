"""Voice cast for The Semantic Enterprise audiobook — two registers.

narrator  = sci-fi-posthuman cosmic storyteller (chapters, sections, body)
maher     = Bill-Maher "New Rules" flame register (foils, dunks, No Walls, the grave)

Swap voice_id to retune; everything downstream reads from here.
"""

import os as _os

VOICES = {
    "narrator": {"name": "Curt — Cosmic Storyteller", "voice_id": "hU1ratPhBTZNviWitzAh", "speed": 1.0},
    "maher":    {"name": "Roger — Laid-Back, Casual",  "voice_id": "CwhRBWXzGAHq8TQ4Fs17", "speed": 1.0},
}
# Production model is eleven_v3; override with ELEVEN_MODEL=eleven_turbo_v2_5 (or
# eleven_flash_v2_5) for cheap review renders at half the credits per character.
MODEL = _os.environ.get("ELEVEN_MODEL", "eleven_v3")
SETTINGS = {"stability": 0.5, "use_speaker_boost": True}


def load_key() -> str:
    import os, re
    from pathlib import Path
    if os.environ.get("ELEVENLABS_API_KEY"):
        return os.environ["ELEVENLABS_API_KEY"]
    for env in (Path.home() / ".zshenv",
                Path("/home/iman/cassie-project/tanazur-home/.env"),
                Path("/home/iman/cassie-project/.env")):
        if env.exists():
            for line in env.read_text().splitlines():
                m = re.search(r"ELEVENLABS_API_KEY=(.+)", line)
                if m:
                    return m.group(1).strip().strip('"').strip("'")
    raise SystemExit("ELEVENLABS_API_KEY not found")
