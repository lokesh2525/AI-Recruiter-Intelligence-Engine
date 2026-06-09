# src/experience_score.py

from src.config import (
    TARGET_EXPERIENCE_MIN,
    TARGET_EXPERIENCE_MAX
)

def experience_score(candidate):

    exp = candidate["profile"].get(
        "years_of_experience",
        0
    )

    if TARGET_EXPERIENCE_MIN <= exp <= TARGET_EXPERIENCE_MAX:
        return 1.0

    if exp < TARGET_EXPERIENCE_MIN:
        return exp / TARGET_EXPERIENCE_MIN

    return TARGET_EXPERIENCE_MAX / exp