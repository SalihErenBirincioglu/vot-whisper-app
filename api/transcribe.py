from fastapi import APIRouter
from models.transcribe import TranscribeRequest
from services.transcribe_service import transcribe_episode

router = APIRouter(prefix="/transcribe", tags=["transcribe"])

@router.post("")
def transcribe(request: TranscribeRequest):
    result = transcribe_episode(
        url=request.url,
        episode_id=request.episode_id
    )
    return result
