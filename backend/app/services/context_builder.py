def build_contextual_recommendation(
    category,
    similar_errors
):

    context_message = (
        f"Detected category: {category}. "
    )

    if similar_errors:

        context_message += (
            "Similar historical failures found: "
        )

        context_message += ", ".join(
            similar_errors
        )

        context_message += ". "

    recommendations = {

        "AUTH": (
            "Verify token expiration, "
            "validate JWT configuration, "
            "and inspect authentication middleware."
        ),

        "SECURITY": (
            "Inspect encryption keys, "
            "validate decrypt payloads, "
            "and review security configurations."
        ),

        "DATABASE": (
            "Verify DB connectivity, "
            "inspect SQL queries, "
            "and validate transaction handling."
        ),

        "NETWORK": (
            "Inspect network latency, "
            "check timeout settings, "
            "and validate API gateway health."
        )
    }

    ai_recommendation = recommendations.get(
        category,
        "Inspect application logs and system traces."
    )

    return context_message + ai_recommendation