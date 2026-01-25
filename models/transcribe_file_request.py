from pydantic import BaseModel

class TranscribeFileRequest(BaseModel):
    file_path: str
    episode_id: int
