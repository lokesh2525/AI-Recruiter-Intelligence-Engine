# # src/reasoning_generator.py

# def generate_reasoning(candidate):

#     profile = candidate.get("profile", {})
#     signals = candidate.get("redrob_signals", {})

#     title = profile.get("current_title", "Professional")
#     exp = profile.get("years_of_experience", 0)

#     response_rate = round(
#         signals.get(
#             "recruiter_response_rate",
#             0
#         ) * 100,
#         0
#     )

#     return (
#         f"{title} with {exp} years experience. "
#         f"Recruiter response rate "
#         f"{response_rate}% and strong profile fit."
#     )

# src/reasoning_generator.py

def generate_reasoning(candidate):

    profile = candidate.get("profile", {})
    signals = candidate.get("redrob_signals", {})

    title = profile.get(
        "current_title",
        "Professional"
    )

    exp = profile.get(
        "years_of_experience",
        0
    )

    response_rate = round(
        signals.get(
            "recruiter_response_rate",
            0
        ) * 100,
        0
    )

    title_lower = title.lower()

    if "recommendation" in title_lower:

        fit = (
            "Strong alignment with ranking and "
            "recommendation systems."
        )

    elif "search" in title_lower:

        fit = (
            "Direct search and retrieval "
            "experience relevant to the role."
        )

    elif "ai engineer" in title_lower:

        fit = (
            "Senior AI engineering background "
            "closely matches JD requirements."
        )

    elif "machine learning" in title_lower:

        fit = (
            "Production ML experience and "
            "relevant seniority level."
        )

    elif "nlp" in title_lower:

        fit = (
            "NLP expertise supports retrieval "
            "and LLM-oriented workloads."
        )

    else:

        fit = (
            "Relevant technical background "
            "with transferable AI skills."
        )

    concern = ""

    if exp < 5:

        concern = (
            " Slightly below the preferred "
            "experience range."
        )

    elif response_rate < 50:

        concern = (
            " Lower recruiter engagement than "
            "other top candidates."
        )

    return (
        f"{title} with {exp} years of experience. "
        f"Recruiter response rate {response_rate}%. "
        f"{fit}.{concern}"
    )