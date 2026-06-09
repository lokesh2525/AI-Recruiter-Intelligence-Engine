# src/jd_parser.py

from src.config import AI_SKILLS

def load_jd(path=None):
    return """
    Senior AI Engineer
    embeddings retrieval ranking llm vector database
    python faiss pinecone milvus qdrant
    evaluation framework ndcg mrr map
    """

def extract_required_skills(jd_text):
    jd_lower = jd_text.lower()

    found_skills = []

    for skill in AI_SKILLS:
        if skill.lower() in jd_lower:
            found_skills.append(skill)

    return list(set(found_skills))