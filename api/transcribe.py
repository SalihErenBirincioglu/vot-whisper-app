from fastapi import APIRouter
from models.transcribe_request import TranscribeRequest
from services.transcribe_service import transcribe_episode
from exceptions import TranscribeException
router = APIRouter(prefix="/transcribe", tags=["transcribe"])

@router.post("")
def transcribe(req: TranscribeRequest):
    try:
        result = transcribe_episode(req.url, req.episode_id)
        return {
            "success": True,
            "episodeId": req.episode_id,
            "text": result["text"]
        }
    except TranscribeException as e:
        return {
            "success": False,
            "episodeId": req.episode_id,
            "errorCode": e.code,
            "message": e.message
        }