# src/generate_submission.py

import pandas as pd

from src.rank_candidates import rank_candidates
from src.reasoning_generator import (
    generate_reasoning
)


def create_submission():

    top100 = rank_candidates()

    rows = []

    rank = 1

    for item in top100:

        candidate = item["candidate"]

        rows.append({
            "candidate_id":
                item["candidate_id"],

            "rank":
                rank,

            "score":
                item["score"],

            "reasoning":
                generate_reasoning(
                    candidate
                )
        })

        rank += 1

    df = pd.DataFrame(rows)

    df.to_csv(
        "output/top100_candidates.csv",
        index=False
    )

    print(
        "Submission Saved:"
    )

    print(
        "output/top100_candidates.csv"
    )


if __name__ == "__main__":

    create_submission()