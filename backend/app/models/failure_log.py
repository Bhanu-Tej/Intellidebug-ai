from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database.db import Base

class FailureLog(Base):

    __tablename__ = "failure_logs"

    id = Column(Integer, primary_key=True, index=True)

    error_message = Column(String)

    status_code = Column(Integer)

    category = Column(String)

    severity = Column(String)

    retry_count = Column(Integer)

    retry_recommended = Column(Boolean)

    confidence_score = Column(Float)