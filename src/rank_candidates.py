# src/rank_candidates.py

from src.load_data import load_candidates

from src.jd_parser import (
    load_jd,
    extract_required_skills
)

from src.skill_match import skill_score
from src.experience_score import experience_score
from src.behavior_score import behavior_score
from src.production_score import production_score
from src.title_score import title_score
from src.retrieval_score import retrieval_score


def rank_candidates():

    print("Loading candidates...")

    candidates = load_candidates(
        "data/raw/candidates.jsonl"
    )

    print("Loading JD...")

    jd = load_jd(
        "data/raw/job_description.docx"
    )

    jd_skills = extract_required_skills(
        jd
    )

    results = []

    for candidate in candidates:

        skill = skill_score(
            candidate,
            jd_skills
        )

        exp = experience_score(
            candidate
        )

        behavior = behavior_score(
            candidate
        )

        production = production_score(
            candidate
        )

        title = title_score(
            candidate
        )

        retrieval = retrieval_score(
            candidate
        )

        final_score = (

            0.25 * skill +

            0.15 * exp +

            0.15 * production +

            0.15 * behavior +

            0.15 * retrieval +

            0.15 * title
        )

        results.append({

            "candidate_id":
                candidate["candidate_id"],

            "score":
                round(
                    final_score,
                    6
                ),

            "candidate":
                candidate
        })

    results.sort(
    key=lambda x: (
        -x["score"],
        x["candidate_id"]
    )
    )
    print(
        f"Processed {len(results)} candidates"
    )

    return results[:100]


if __name__ == "__main__":

    top100 = rank_candidates()

    print("\nTop 10 Candidates\n")

    for idx, candidate in enumerate(
        top100[:10],
        start=1
    ):

        print(
            idx,
            candidate["candidate_id"],
            candidate["score"]
        )