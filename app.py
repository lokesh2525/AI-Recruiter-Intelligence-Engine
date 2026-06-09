import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.rank_candidates import rank_candidates

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Recruiter Intelligence Engine",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.big-title {
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#2563EB;
    margin-bottom:10px;
}

.subtitle {
    text-align:center;
    color:#6B7280;
    font-size:18px;
    margin-bottom:25px;
}

.metric-card {
    background: linear-gradient(
        135deg,
        #2563EB,
        #3B82F6
    );

    padding:20px;

    border-radius:16px;

    text-align:center;

    color:white;

    box-shadow:
    0px 6px 20px rgba(
        37,
        99,
        235,
        0.20
    );
}

.hero-card {

    background: linear-gradient(
        90deg,
        #2563EB,
        #06B6D4
    );

    padding:25px;

    border-radius:20px;

    color:white;

    box-shadow:
    0px 8px 24px rgba(
        37,
        99,
        235,
        0.25
    );

    margin-top:20px;
    margin-bottom:20px;
}

.section-title{
    color:#1E3A8A;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class='big-title'>
🤖 AI Recruiter Intelligence Engine
</div>

<div class='subtitle'>
AI-Powered Candidate Ranking Platform for Smart Hiring Decisions
</div>
""", unsafe_allow_html=True)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🚀 AI Recruiter")

st.sidebar.success(
    "Data & AI Challenge Submission"
)

st.sidebar.info(
    """
    AI-powered hiring assistant using:

    • Skill Matching

    • Experience Analysis

    • Behavioral Signals

    • Production Experience

    • Retrieval & Search Relevance
    """
)

st.sidebar.markdown("""
### Ranking Pipeline

1️⃣ Load Candidates

2️⃣ Parse Job Description

3️⃣ Skill Matching

4️⃣ Experience Scoring

5️⃣ Behavioral Analysis

6️⃣ Production Scoring

7️⃣ Retrieval Scoring

8️⃣ Final Ranking

9️⃣ Top 100 Selection
""")

# =====================================================
# GENERATE BUTTON
# =====================================================

if st.button("🚀 Generate Top 100 Candidates"):

    with st.spinner(
        "Analyzing 100,000 candidates..."
    ):

        top100 = rank_candidates()

    rows = []

    for idx, item in enumerate(
        top100,
        start=1
    ):

        candidate = item["candidate"]

        profile = candidate.get(
            "profile",
            {}
        )

        rows.append({

            "Rank":
                idx,

            "Candidate ID":
                item["candidate_id"],

            "Title":
                profile.get(
                    "current_title",
                    "NA"
                ),

            "Experience":
                profile.get(
                    "years_of_experience",
                    "NA"
                ),

            "Score":
                item["score"]
        })

    df = pd.DataFrame(rows)

    # =====================================================
    # KPI CARDS
    # =====================================================

    st.markdown(
        "## 📊 Dashboard Overview"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class='metric-card'>
        <h2>100,000</h2>
        <p>Profiles Analyzed</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class='metric-card'>
        <h2>100</h2>
        <p>Top Candidates</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='metric-card'>
        <h2>{round(df['Score'].max(),3)}</h2>
        <p>Top Score</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class='metric-card'>
        <h2>{round(df['Score'].mean(),3)}</h2>
        <p>Average Score</p>
        </div>
        """, unsafe_allow_html=True)

    # =====================================================
    # HERO CARD
    # =====================================================

    best = df.iloc[0]

    st.markdown(
        f"""
        <div class='hero-card'>

        <h2>🏆 Top Ranked Candidate</h2>

        <h3>{best['Candidate ID']}</h3>

        <h3>{best['Title']}</h3>

        <h4>Experience: {best['Experience']} Years</h4>

        <h2>Score: {best['Score']}</h2>

        </div>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # INSIGHTS
    # =====================================================

    st.subheader("📊 Ranking Insights")

    st.write("""
    This ranking engine combines:

    - Skill Matching
    - Experience Scoring
    - Behavioral Signals
    - Production Experience
    - Retrieval/Search Relevance
    - Title Relevance
    """)

    # =====================================================
    # TABS
    # =====================================================

    tab1, tab2, tab3 = st.tabs(
        [
            "📈 Analytics",
            "🏆 Candidates",
            "⬇ Download"
        ]
    )

    # =====================================================
    # ANALYTICS TAB
    # =====================================================

    with tab1:

        st.subheader(
            "Score Distribution"
        )

        fig, ax = plt.subplots(
            figsize=(8,4)
        )

        ax.hist(
            df["Score"],
            bins=15
        )

        ax.set_title(
            "Candidate Score Distribution"
        )

        st.pyplot(fig)

        st.subheader(
            "Top 10 Candidate Scores"
        )

        st.bar_chart(
            df.head(10)
            .set_index(
                "Candidate ID"
            )["Score"]
        )

        st.subheader(
            "🏆 Top Candidates"
        )

        for _, row in (
            df.head(10)
            .iterrows()
        ):

            st.write(
                f"{row['Candidate ID']} | {row['Title']}"
            )

            st.progress(
                min(
                    float(
                        row["Score"]
                    ),
                    1.0
                )
            )

    # =====================================================
    # CANDIDATE TAB
    # =====================================================

    with tab2:

        st.subheader(
            "Top 100 Ranked Candidates"
        )

        search = st.text_input(
            "🔍 Search Candidate ID"
        )

        filtered_df = df

        if search:

            filtered_df = df[
                df["Candidate ID"]
                .str.contains(
                    search,
                    case=False
                )
            ]

        st.dataframe(
            filtered_df,
            use_container_width=True,
            height=600
        )

    # =====================================================
    # DOWNLOAD TAB
    # =====================================================

    with tab3:

        st.subheader(
            "Download Submission"
        )

        csv = (
            df.to_csv(
                index=False
            )
            .encode("utf-8")
        )

        st.download_button(
            label="📥 Download Top100 CSV",
            data=csv,
            file_name="top100_candidates.csv",
            mime="text/csv"
        )

        st.success(
            "Submission File Ready"
        )
