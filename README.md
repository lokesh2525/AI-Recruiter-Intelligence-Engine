# 🤖 AI Recruiter Intelligence Engine

## Overview

AI Recruiter Intelligence Engine is an AI-powered candidate ranking system developed for the Data & AI Challenge.

Traditional ATS systems rely heavily on keyword matching, often overlooking highly qualified candidates. This project uses a hybrid scoring approach that evaluates candidates based on skills, experience, behavioral signals, production expertise, title relevance, and retrieval/search relevance to identify the best-fit candidates for a given role.

The system processes 100,000 candidate profiles and generates a ranked shortlist of the top 100 candidates.

---

## Problem Statement

Recruiters review hundreds of profiles and often miss strong candidates because traditional filtering systems focus on keyword matching rather than true relevance.

The goal is to build an intelligent ranking system that:

* Understands job requirements
* Evaluates candidate suitability holistically
* Ranks candidates based on multiple factors
* Produces a recruiter-ready shortlist

---

## Solution Architecture

```text
Job Description
        │
        ▼
JD Parser
        │
        ▼
Candidate Dataset
        │
        ▼
Skill Matching
Experience Scoring
Behavioral Scoring
Production Scoring
Title Relevance Scoring
Retrieval Relevance Scoring
        │
        ▼
Hybrid Ranking Engine
        │
        ▼
Top 100 Candidates
        │
        ▼
Submission CSV
```

---

## Features

### Skill Matching

Matches candidate skills against job requirements.

### Experience Analysis

Evaluates total years of relevant experience.

### Behavioral Signals

Incorporates recruiter engagement and profile interaction metrics.

### Production Experience

Rewards candidates with proven production-level expertise.

### Title Relevance

Prioritizes candidates with relevant job titles such as:

* Senior AI Engineer
* Staff Machine Learning Engineer
* Search Engineer
* Recommendation Systems Engineer
* NLP Engineer

### Retrieval & Search Relevance

Boosts candidates with expertise in:

* Retrieval Systems
* Ranking Systems
* Search Engineering
* Recommendation Systems
* Vector Databases
* Embeddings

---

## Ranking Formula

```python
Final Score =

0.25 × Skill Score +
0.15 × Experience Score +
0.15 × Production Score +
0.15 × Behavioral Score +
0.15 × Retrieval Score +
0.15 × Title Score
```

---

## Technology Stack

* Python
* Streamlit
* Pandas
* Matplotlib
* JSONL Processing

---

## Dashboard

The project includes a Streamlit-based dashboard with:

* KPI Cards
* Candidate Analytics
* Score Distribution
* Top Candidate Highlight
* Candidate Search
* Downloadable Ranking Results

### Dashboard Screenshots

Add screenshots inside the `screenshots/` folder:

* dashboard.png
* analytics.png
* ranking_table.png
* top_candidate.png

---

## Project Structure

```text
AI-Recruiter/
│
├── app.py
├── requirements.txt
├── README.md
├── validate_submission.py
│
├── src/
│   ├── load_data.py
│   ├── jd_parser.py
│   ├── skill_match.py
│   ├── experience_score.py
│   ├── behavior_score.py
│   ├── production_score.py
│   ├── title_score.py
│   ├── retrieval_score.py
│   ├── reasoning_generator.py
│   ├── rank_candidates.py
│   └── generate_submission.py
│
├── output/
│   └── top100_candidates.csv
│
├── screenshots/
│
└── ppt/
    └── AI_Recruiter_Presentation.pdf
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd AI-Recruiter
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Dashboard

```bash
streamlit run app.py
```

---

## Generate Submission File

```bash
python -m src.generate_submission
```

Output:

```text
output/top100_candidates.csv
```

---

## Validate Submission

```bash
python validate_submission.py output/top100_candidates.csv
```

Expected Output:

```text
Submission is valid.
```

---

## Results

The system successfully:

* Processed 100,000 candidate profiles
* Generated Top 100 ranked candidates
* Produced a valid submission file
* Delivered a recruiter-friendly dashboard for analysis

---

## Future Improvements

* Semantic Matching using Sentence Transformers
* Vector Search using FAISS
* LLM-based Candidate Reasoning
* Explainable AI Ranking
* Real-time Candidate Recommendations
* Multi-Job Ranking Support

---

## Author

Lokesh Fegade

B.Tech – Artificial Intelligence & Machine Learning

Data Analyst Intern

Data & AI Challenge Submission
