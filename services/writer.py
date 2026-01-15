from pathlib import Path

OUTPUT_DIR = Path("outputs/transcripts")

def write(text: str, episode_id: int) -> str:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / f"episode_{episode_id}.txt"

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    return str(path)
