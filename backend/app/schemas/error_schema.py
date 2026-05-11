from pydantic import BaseModel

class ErrorRequest(BaseModel):
    error_message: str
    status_code: int
    retry_count: int