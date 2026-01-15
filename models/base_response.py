from pydantic import BaseModel
from typing import Optional

class BaseResponse(BaseModel):
    success: bool
    episodeId: int
    text: Optional[str] = None
    errorCode: Optional[str] = None
    message: Optional[str] = None
