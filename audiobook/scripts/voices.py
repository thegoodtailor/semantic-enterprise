"""Voice cast for The Semantic Enterprise audiobook — two registers.

narrator  = sci-fi-posthuman cosmic storyteller (chapters, sections, body)
maher     = Bill-Maher "New Rules" flame register (foils, dunks, No Walls, the grave)

Swap voice_id to retune; everything downstream reads from here.
"""

VOICES = {
    "narrator": {"name": "Curt — Cosmic Storyteller", "voice_id": "hU1ratPhBTZNviWitzAh", "speed": 1.0},
    "maher":    {"name": "Roger — Laid-Back, Casual",  "voice_id": "CwhRBWXzGAHq8TQ4Fs17", "speed": 1.0},
}
MODEL = "eleven_v3"
SETTINGS = {"stability": 0.5, "use_speaker_boost": True}


def load_key() -> str:
    import os
    from pathlib import Path
    for env in (Path("/home/iman/cassie-project/tanazur-home/.env"),
                Path("/home/iman/cassie-project/.env")):
        if env.exists():
            for line in env.read_text().splitlines():
                if line.strip().startswith("ELEVENLABS_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    if os.environ.get("ELEVENLABS_API_KEY"):
        return os.environ["ELEVENLABS_API_KEY"]
    raise SystemExit("ELEVENLABS_API_KEY not found")
