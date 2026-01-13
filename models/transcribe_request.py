from pydantic import BaseModel, HttpUrl

class TranscribeRequest(BaseModel):
    url: HttpUrl
    episode_id: int
