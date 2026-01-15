import requests
from pathlib import Path
from exceptions import TranscribeException
import time

TMP_DIR = Path("/tmp/vot")
MAX_RETRY = 3
TIMEOUT = 30

def download(url: str, episode_id: int) -> str:
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    audio_path = TMP_DIR / f"episode_{episode_id}.audio"

    for attempt in range(1, MAX_RETRY + 1):
        try:
            with requests.get(url, stream=True, timeout=TIMEOUT) as r:
                r.raise_for_status()
                with open(audio_path, "wb") as f:
                    for chunk in r.iter_content(8192):
                        if chunk:
                            f.write(chunk)
            return str(audio_path)

        except Exception as e:
            if attempt == MAX_RETRY:
                raise TranscribeException(
                    code="AUDIO_DOWNLOAD_FAILED",
                    message="Audio download failed"
                )
            time.sleep(1)

