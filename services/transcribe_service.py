from services.downloader import download
from services.whisper_service import transcribe
from services.nlp_service import normalize
from config.settings import ENABLE_NLP

def transcribe_episode(url: str, episode_id: int) -> dict:
    audio_path = download(url, episode_id)
    text = transcribe(audio_path)

    if ENABLE_NLP:
        text = normalize(text)

    return {
        "episodeId": episode_id,
        "text": text
    }



def transcribe_local_file(file_path: str, episode_id: int) -> dict:
    text = transcribe(file_path)

    if ENABLE_NLP:
        text = normalize(text)

    return {
        "episodeId": episode_id,
        "text": text
    }
