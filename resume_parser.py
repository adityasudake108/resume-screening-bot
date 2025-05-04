import os
import fitz  # PyMuPDF
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

stop_words = set(stopwords.words('english'))

def extract_text_from_pdf(file_path):
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def clean_text(text):
    tokens = word_tokenize(text)
    tokens = [w.lower() for w in tokens if w.isalpha()]
    filtered = [w for w in tokens if w not in stop_words and w not in string.punctuation]
    return ' '.join(filtered)
