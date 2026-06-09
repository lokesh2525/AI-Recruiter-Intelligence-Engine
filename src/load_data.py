# src/load_data.py
import json
from tqdm import tqdm


def load_candidates(file_path):
    candidates = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in tqdm(f, desc="Loading Candidates"):
            line = line.strip()

            if not line:
                continue

            candidates.append(json.loads(line))

    return candidates


if __name__ == "__main__":

    candidates = load_candidates(
        "data/raw/candidates.jsonl"
    )

    print(f"Loaded {len(candidates)} candidates")