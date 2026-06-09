from src.load_data import load_candidates
from src.jd_parser import load_jd, extract_required_skills
from src.skill_match import skill_score
from src.config import AI_SKILLS

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

jd = load_jd(
    "data/raw/job_description.docx"
)

skills = extract_required_skills(jd)

print("JD Skills:", skills)

candidate = candidates[0]

score = skill_score(
    candidate,
    skills
)

print(
    candidate["candidate_id"],
    score
)