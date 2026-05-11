from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from typing import List

from app.models.failure_log import FailureLog

from app.schemas.failure_response import FailureResponse

from app.schemas.error_schema import ErrorRequest
from app.services.error_analyzer import analyze_error

from app.database.session import get_db

router = APIRouter()

@router.post("/analyze-error")

def analyze_api_error(
    request: ErrorRequest,
    db: Session = Depends(get_db)
):

    result = analyze_error(
        request.error_message,
        request.status_code,
        request.retry_count,
        db
    )

    return result

@router.get(
    "/failure-history",
    response_model=List[FailureResponse]
)

def get_failure_history(
    db: Session = Depends(get_db)
):

    failures = db.query(FailureLog).all()

    return failures