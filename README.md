# 📊 Resume Screening Bot using NLP and TF-IDF

This project automatically ranks resumes based on their relevance to a given job description using Natural Language Processing (NLP) and cosine similarity with TF-IDF.

## 🔍 Problem Statement

Recruiters face the challenge of manually scanning hundreds of resumes, leading to inefficiencies and subjective shortlisting. There is a need for an automated tool that can screen and rank resumes quickly and objectively based on the job description.

## ✅ Proposed Solution

A Python-based tool that:
- Accepts a job description and multiple resumes (PDFs).
- Cleans and extracts text from each resume.
- Computes similarity scores using the TF-IDF algorithm and cosine similarity.
- Ranks resumes based on relevance scores.

## 🛠️ Technology Stack

- **Frontend**: Streamlit (for interactive web interface)
- **Backend**: Python
- **Libraries Used**: 
  - `nltk` for text preprocessing
  - `scikit-learn` for TF-IDF and similarity
  - `PyPDF2` for reading PDFs

## 🧠 Algorithm

- **TF-IDF Vectorization**: Converts job description and resumes into numerical feature vectors.
- **Cosine Similarity**: Measures textual similarity between job description and resumes.

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/resume-screening-bot.git
cd resume-screening-bot

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
