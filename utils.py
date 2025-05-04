from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_resume_scores(jd_text, resumes_texts, filenames):
    documents = [jd_text] + resumes_texts
    vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)

    tfidf_matrix = vectorizer.fit_transform(documents)
    
    jd_vector = tfidf_matrix[0:1]
    resume_vectors = tfidf_matrix[1:]
    
    similarities = cosine_similarity(jd_vector, resume_vectors).flatten()
    
    results = list(zip(filenames, similarities))
    results.sort(key=lambda x: x[1], reverse=True)
    
    return results
