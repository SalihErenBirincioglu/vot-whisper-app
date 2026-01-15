from pathlib import Path
from datetime import datetime, timedelta
from config.settings import ENABLE_AUDIO_CLEANUP, AUDIO_TTL_HOURS

TMP_DIR = Path("/tmp/vot")

def run():
    if not ENABLE_AUDIO_CLEANUP:
        return

    if not TMP_DIR.exists():
        return

    cutoff = datetime.now() - timedelta(hours=AUDIO_TTL_HOURS)

    for file in TMP_DIR.iterdir():
        if not file.is_file():
            continue

        mtime = datetime.fromtimestamp(file.stat().st_mtime)
        if mtime < cutoff:
            file.unlink()

if __name__ == "__main__":
    run()
