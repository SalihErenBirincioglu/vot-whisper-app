import requests
from pathlib import Path

TMP_DIR = Path("/tmp/vot")

def download(url: str, episode_id: int) -> str:
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    audio_path = TMP_DIR / f"episode_{episode_id}.audio"

    with requests.get(url, stream=True, timeout=30) as r:
        r.raise_for_status()
        with open(audio_path, "wb") as f:
            for chunk in r.iter_content(8192):
                if chunk:
                    f.write(chunk)

    return str(audio_path)
