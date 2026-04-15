# Assignment (24/03/2026)

# Assignment Name :Word Importance Explorer
# Description : Use TF-IDF on 5 documents and identify top keywords with explanation.

from sklearn.feature_extraction.text import TfidfVectorizer

documents = [
    "Machine learning is amazing",
    "AI and machine learning are related",
    "Deep learning is a part of AI",
    "AI is transforming the world",
    "Machine learning helps in predictions"
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

feature_names = vectorizer.get_feature_names_out()

for i, doc in enumerate(tfidf_matrix.toarray()):
    sorted_indices = doc.argsort()[::-1]
    top_words = [feature_names[j] for j in sorted_indices[:3]]
    print(f"Document {i+1} Top Words:", top_words)
