from fastapi import FastAPI
from dotenv import load_dotenv

# load .env if present (safe in prod too)
load_dotenv()

from api.transcribe import router as transcribe_router

app = FastAPI(
    title="VoT Whisper Service",
    version="1.0.0"
)

app.include_router(transcribe_router)
