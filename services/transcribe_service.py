from services.downloader import download
from services.whisper_service import transcribe
from services.writer import write

def transcribe_episode(url: str, episode_id: int) -> dict:
    audio_path = download(url, episode_id)
    text = transcribe(audio_path)
    transcript_path = write(text, episode_id)

    return {
        "episodeId": episode_id,
        "transcriptPath": transcript_path
    }
