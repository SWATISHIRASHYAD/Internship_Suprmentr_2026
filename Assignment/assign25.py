# [7:31 pm, 14/4/2026] S: Assignment (03/04/2026)

# Assignment Name : NLP Mini App
# Description : Build a chatbot, fake news detector, or keyword extractor.

from sklearn.feature_extraction.text import CountVectorizer

text = ["machine learning is powerful and useful"]

vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(text)

keywords = vectorizer.get_feature_names_out()
print(keywords)