# src/title_score.py

TITLE_WEIGHTS = {
    "senior ai engineer": 1.0,
    "staff machine learning engineer": 0.95,
    "principal machine learning engineer": 0.95,
    "recommendation systems engineer": 0.90,
    "search engineer": 0.90,
    "nlp engineer": 0.85,
    "ml engineer": 0.80,
    "machine learning engineer": 0.80,
    "junior ml engineer": 0.30,
    "intern": 0.10
}

def title_score(candidate):

    profile = candidate.get("profile", {})

    title = (
        profile.get("current_title", "")
        .lower()
        .strip()
    )

    for key, score in TITLE_WEIGHTS.items():
        if key in title:
            return score

    return 0.5