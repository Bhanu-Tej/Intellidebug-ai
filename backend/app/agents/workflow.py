from typing import TypedDict

from app.utils.error_patterns import (
    ERROR_CATEGORIES
)

from langgraph.graph import (
    StateGraph,
    END
)

from app.embeddings.embedding_model import (
    generate_embedding
)

from app.retrievers.faiss_store import (

    add_error_embedding,

    search_similar_errors
)

from app.services.context_builder import (
    build_contextual_recommendation
)


# =========================================
# STATE MODEL
# =========================================

class DebugState(TypedDict):

    error_message: str

    status_code: int

    retry_count: int

    category: str

    severity: str

    embedding: list

    similar_errors: list

    contextual_ai_recommendation: str


# =========================================
# CLASSIFICATION NODE
# =========================================

def classify_node(state: DebugState):

    error_message = state["error_message"]

    status_code = state["status_code"]

    severity = "LOW"

    if status_code >= 500:

        severity = "HIGH"

    elif status_code >= 400:

        severity = "MEDIUM"

    category = "UNKNOWN"

    for keyword, detected_category in (
        ERROR_CATEGORIES.items()
    ):

        if keyword.lower() in (
            error_message.lower()
        ):

            category = detected_category

            break

    state["severity"] = severity

    state["category"] = category

    return state


# =========================================
# EMBEDDING NODE
# =========================================

def embedding_node(state: DebugState):

    embedding = generate_embedding(
        state["error_message"]
    )

    state["embedding"] = embedding

    return state


# =========================================
# RETRIEVAL NODE
# =========================================

def retrieval_node(state: DebugState):

    add_error_embedding(

        state["error_message"],

        state["embedding"]
    )

    similar_errors = (
        search_similar_errors(
            state["embedding"]
        )
    )

    state["similar_errors"] = (
        similar_errors
    )

    return state


# =========================================
# CONTEXT NODE
# =========================================

def context_node(state: DebugState):

    recommendation = (
        build_contextual_recommendation(

            state["category"],

            state["similar_errors"]
        )
    )

    state[
        "contextual_ai_recommendation"
    ] = recommendation

    return state

# =========================================
# LANGGRAPH WORKFLOW
# =========================================

workflow = StateGraph(DebugState)


# =========================================
# ADD NODES
# =========================================

workflow.add_node(
    "classifier",
    classify_node
)

workflow.add_node(
    "embedding",
    embedding_node
)

workflow.add_node(
    "retrieval",
    retrieval_node
)

workflow.add_node(
    "context",
    context_node
)


# =========================================
# DEFINE FLOW
# =========================================

workflow.set_entry_point(
    "classifier"
)

workflow.add_edge(
    "classifier",
    "embedding"
)

workflow.add_edge(
    "embedding",
    "retrieval"
)

workflow.add_edge(
    "retrieval",
    "context"
)

workflow.add_edge(
    "context",
    END
)


# =========================================
# COMPILE GRAPH
# =========================================

debug_agent = workflow.compile()