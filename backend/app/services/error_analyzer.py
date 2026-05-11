from sqlalchemy.orm import Session

from app.services.context_builder import (
    build_contextual_recommendation
)

from app.agents.workflow import (
    debug_agent
)

from app.utils.error_patterns import ERROR_CATEGORIES

from app.models.failure_log import FailureLog

from app.embeddings.embedding_model import (
    generate_embedding
)

from app.retrievers.faiss_store import (
    add_error_embedding,
    search_similar_errors
)


def analyze_error(

    error_message,

    status_code,

    retry_count,

    db: Session
):

    initial_state = {

        "error_message": error_message,

        "status_code": status_code,

        "retry_count": retry_count,

        "category": "",

        "severity": "",

        "embedding": [],

        "similar_errors": [],

        "contextual_ai_recommendation": ""
    }

    final_state = debug_agent.invoke(
        initial_state
    )

    retry_recommended = True

    if (
        final_state["severity"] == "HIGH"
        and retry_count >= 3
    ):

        retry_recommended = False

    confidence_score = 0.92

    recommendations = {

        "AUTH": [
            "Verify authentication token",
            "Check user session",
            "Validate API credentials"
        ],

        "SECURITY": [
            "Verify encryption keys",
            "Check token validity",
            "Validate decrypt configuration"
        ]
    }

    recommendation = recommendations.get(

        final_state["category"],

        ["Check application logs"]
    )

    failure_log = FailureLog(

        error_message=error_message,

        status_code=status_code,

        category=final_state["category"],

        severity=final_state["severity"],

        retry_count=retry_count,

        retry_recommended=retry_recommended,

        confidence_score=confidence_score
    )

    db.add(failure_log)

    db.commit()

    db.refresh(failure_log)

    return {

        "severity":
            final_state["severity"],

        "category":
            final_state["category"],

        "root_cause":
            error_message,

        "recommendation":
            recommendation,

        "retry_recommended":
            retry_recommended,

        "confidence_score":
            confidence_score,

        "similar_errors":
            final_state["similar_errors"],

        "contextual_ai_recommendation":

            final_state[
                "contextual_ai_recommendation"
            ]
    }