import whisper
import os
print("FFMPEG PATH CHECK:", os.environ.get("PATH"))
print("FFMPEG_BINARY:", os.environ.get("FFMPEG_BINARY"))

_model = whisper.load_model("base")

def transcribe(audio_path: str) -> str:
    result = _model.transcribe(
    audio_path,
    language="tr",
    beam_size=5,
    temperature=0.0
)
    return result["text"]
