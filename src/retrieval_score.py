RETRIEVAL_SKILLS = [
    "retrieval",
    "ranking",
    "embeddings",
    "faiss",
    "pinecone",
    "milvus",
    "qdrant",
    "vector database",
    "search",
    "recommendation"
]

def retrieval_score(candidate):

    text = str(candidate).lower()

    matches = 0

    for skill in RETRIEVAL_SKILLS:
        if skill in text:
            matches += 1

    return matches / len(RETRIEVAL_SKILLS)