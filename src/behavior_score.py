# src/behavior_score.py

def behavior_score(candidate):

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    score = 0

    if signals.get("open_to_work_flag"):
        score += 20

    score += (
        signals.get(
            "recruiter_response_rate",
            0
        ) * 30
    )

    score += (
        signals.get(
            "interview_completion_rate",
            0
        ) * 25
    )

    github = signals.get(
        "github_activity_score",
        -1
    )

    if github > 0:
        score += github * 0.15

    score += min(
        signals.get(
            "saved_by_recruiters_30d",
            0
        ),
        20
    )

    return min(score / 100, 1)