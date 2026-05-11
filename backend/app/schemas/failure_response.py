from pydantic import BaseModel

class FailureResponse(BaseModel):

    id: int

    error_message: str

    status_code: int

    category: str

    severity: str

    retry_count: int

    retry_recommended: bool

    confidence_score: float

    class Config:
        orm_mode = True