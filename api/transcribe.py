from fastapi import APIRouter
from models.transcribe_request import TranscribeRequest
from models.transcribe_file_request import TranscribeFileRequest
from services.transcribe_service import transcribe_episode
from services.transcribe_service import transcribe_local_file
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
    except Exception as e:
        return {
            "success": False,
            "episodeId": req.episode_id,
            "errorCode": "UNEXPECTED_ERROR",
            "message": str(e)
        }
    

@router.post("/file")
def transcribe_file(req: TranscribeFileRequest):
    try:
        result = transcribe_local_file(req.file_path, req.episode_id)
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

    except Exception as e:
        return {
            "success": False,
            "episodeId": req.episode_id,
            "errorCode": "UNEXPECTED_ERROR",
            "message": str(e)
        }   