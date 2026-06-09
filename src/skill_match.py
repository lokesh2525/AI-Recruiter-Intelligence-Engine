# src/skill_match.py

def get_candidate_skills(candidate):

    skills = candidate.get("skills", [])

    return {
        skill["name"].lower()
        for skill in skills
    }


def skill_score(candidate, jd_skills):

    candidate_skills = get_candidate_skills(candidate)

    if len(jd_skills) == 0:
        return 0

    matched = 0

    for skill in jd_skills:

        if skill.lower() in candidate_skills:
            matched += 1

    return matched / len(jd_skills)