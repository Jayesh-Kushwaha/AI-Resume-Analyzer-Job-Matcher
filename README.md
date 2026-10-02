# 📄 AI Resume Analyzer & Job Matcher

An NLP-based web application that analyzes a resume against a job description and provides a match score, matched skills, missing skills, and improvement recommendations.

## 🚀 Features

- Upload resume in PDF format
- Extract resume text automatically
- Compare resume with job description
- Calculate resume match score
- Identify matched skills
- Identify missing skills
- Provide resume improvement recommendations
- Display extracted resume text
- Simple and interactive Streamlit interface

## 🛠️ Tech Stack

- Python
- Streamlit
- PyPDF2
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Regular Expressions

## 🧠 How It Works

```text
Resume PDF
    ↓
Text Extraction
    ↓
Skill Extraction
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity
    ↓
Match Score
    ↓
Matched & Missing Skills
    ↓
Recommendations