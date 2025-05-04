import streamlit as st
import os
from resume_parser import extract_text_from_pdf, clean_text
from utils import get_resume_scores

st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("📄 AI Resume Screening Bot")

uploaded_jd = st.file_uploader("Upload Job Description (PDF or TXT)", type=["pdf", "txt"])
uploaded_resumes = st.file_uploader("Upload Resumes (Multiple PDFs)", accept_multiple_files=True, type="pdf")

if st.button("Process Resumes") and uploaded_jd and uploaded_resumes:
    # Extract JD
    jd_text = ""
    if uploaded_jd.name.endswith(".pdf"):
        with open("jd.pdf", "wb") as f:
            f.write(uploaded_jd.read())
        jd_text = extract_text_from_pdf("jd.pdf")
    else:
        jd_text = uploaded_jd.read().decode("utf-8")
    
    cleaned_jd = clean_text(jd_text)

    # Extract Resumes
    resume_texts = []
    resume_names = []
    
    for resume in uploaded_resumes:
        with open(f"resumes/{resume.name}", "wb") as f:
            f.write(resume.read())
        raw_text = extract_text_from_pdf(f"resumes/{resume.name}")
        resume_texts.append(clean_text(raw_text))
        resume_names.append(resume.name)

    # Get Results
    scores = get_resume_scores(cleaned_jd, resume_texts, resume_names)

    st.subheader("📊 Resume Ranking")
    for rank, (name, score) in enumerate(scores, 1):
        # Calculate score out of 10 (rounded to 2 decimal places)
        score_out_of_10 = round(score * 10, 2)
        
        # Determine color based on score
        if score_out_of_10 >= 7.5:
            color = "green"
        elif score_out_of_10 >= 5:
            color = "orange"
        else:
            color = "red"
            
        st.markdown(f"**{rank}. {name}** — Relevance Score: <span style='color:{color};font-weight:bold'>{score_out_of_10}/10</span>", unsafe_allow_html=True)

