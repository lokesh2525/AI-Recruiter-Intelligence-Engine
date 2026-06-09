# src/production_score.py

PRODUCTION_KEYWORDS = [
    "production",
    "deployed",
    "deployment",
    "users",
    "scale",
    "pipeline",
    "retrieval",
    "ranking",
    "inference",
    "serving",
    "real-time",
    "evaluation",
    "a/b testing"
]


def production_score(candidate):

    history = candidate.get(
        "career_history",
        []
    )

    text = ""

    for role in history:
        text += (
            role.get(
                "description",
                ""
            ).lower()
            + " "
        )

    matches = 0

    for keyword in PRODUCTION_KEYWORDS:

        if keyword in text:
            matches += 1

    return min(
        matches /
        len(PRODUCTION_KEYWORDS),
        1
    )