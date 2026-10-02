import streamlit as st
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

.section-title {
    font-size: 24px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================

st.markdown(
    '<div class="main-title">📄 AI Resume Analyzer & Job Matcher</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Analyze your resume against a job description using AI-powered text matching.</div>',
    unsafe_allow_html=True
)


# =========================
# INPUT SECTION
# =========================

col1, col2 = st.columns(2)


with col1:

    st.subheader("📄 Upload Resume")

    resume = st.file_uploader(
        "Upload your Resume PDF",
        type=["pdf"]
    )


with col2:

    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste the Job Description",
        height=180,
        placeholder="Paste the job description here..."
    )


# =========================
# EXTRACT RESUME TEXT
# =========================

def extract_resume_text(pdf_file):

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + " "

    return text


# =========================
# CALCULATE MATCH SCORE
# =========================

def calculate_match(resume_text, job_description):

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )

    score = similarity[0][0] * 100

    return round(score, 2)


# =========================
# FIND SKILLS
# =========================

def find_skills(text):

    skills_list = [
        "python",
        "java",
        "javascript",
        "react",
        "node.js",
        "sql",
        "mysql",
        "mongodb",
        "html",
        "css",
        "power bi",
        "excel",
        "machine learning",
        "data analysis",
        "pandas",
        "numpy",
        "scikit-learn",
        "git",
        "github",
        "aws"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if re.search(
            r"\b" + re.escape(skill.lower()) + r"\b",
            text
        ):
            found_skills.append(skill)

    return found_skills


# =========================
# ANALYZE BUTTON
# =========================

if st.button(
    "🚀 Analyze Resume",
    use_container_width=True
):

    # -------------------------
    # VALIDATION
    # -------------------------

    if resume is None:

        st.warning(
            "⚠️ Please upload your resume PDF."
        )

    elif job_description.strip() == "":

        st.warning(
            "⚠️ Please enter a job description."
        )

    else:

        # -------------------------
        # RESUME TEXT
        # -------------------------

        resume_text = extract_resume_text(
            resume
        )


        # -------------------------
        # MATCH SCORE
        # -------------------------

        score = calculate_match(
            resume_text,
            job_description
        )


        # -------------------------
        # SKILLS
        # -------------------------

        resume_skills = find_skills(
            resume_text
        )

        job_skills = find_skills(
            job_description
        )


        matched_skills = []

        missing_skills = []


        for skill in job_skills:

            if skill in resume_skills:

                matched_skills.append(skill)

            else:

                missing_skills.append(skill)


        # -------------------------
        # SUCCESS MESSAGE
        # -------------------------

        st.success(
            "✅ Resume analyzed successfully!"
        )


        # =========================
        # SCORE SECTION
        # =========================

        st.subheader(
            "📊 Resume Analysis"
        )


        score_col1, score_col2, score_col3 = st.columns(3)


        with score_col1:

            st.metric(
                "Resume Match Score",
                f"{score}%"
            )


        with score_col2:

            st.metric(
                "Matched Skills",
                len(matched_skills)
            )


        with score_col3:

            st.metric(
                "Missing Skills",
                len(missing_skills)
            )


        # Progress bar

        st.progress(
            min(score / 100, 1.0)
        )


        # =========================
        # MATCHED SKILLS
        # =========================

        st.subheader(
            "✅ Matched Skills"
        )


        if matched_skills:

            st.write(
                ", ".join(matched_skills)
            )

        else:

            st.info(
                "No matching skills found."
            )


        # =========================
        # MISSING SKILLS
        # =========================

        st.subheader(
            "❌ Missing Skills"
        )


        if missing_skills:

            st.write(
                ", ".join(missing_skills)
            )

        else:

            st.success(
                "No major missing skills found."
            )


        # =========================
        # RECOMMENDATIONS
        # =========================

        st.subheader(
            "💡 Recommendations"
        )


        if missing_skills:

            st.write(
                "Your resume could be improved by adding or highlighting these skills:"
            )


            for skill in missing_skills:

                st.write(
                    f"• Learn or highlight **{skill}** in your resume."
                )

        else:

            st.success(
                "Your resume covers the main skills mentioned in the job description!"
            )


        # =========================
        # ANALYSIS SUMMARY
        # =========================

        st.subheader(
            "📌 Analysis Summary"
        )


        st.write(
            f"Your resume has a **{score}% similarity** "
            "with the provided job description."
        )


        if score >= 70:

            st.info(
                "🟢 Your resume has a strong textual match "
                "with this job description."
            )

        elif score >= 40:

            st.info(
                "🟡 Your resume has a moderate textual match. "
                "Consider adding relevant keywords."
            )

        else:

            st.info(
                "🔴 Your resume has a low textual match. "
                "Review the job requirements and relevant skills."
            )


        # =========================
        # EXTRACTED RESUME
        # =========================

        st.subheader(
            "📄 Extracted Resume Text"
        )


        st.text_area(
            "Resume Content",
            resume_text,
            height=300
        )