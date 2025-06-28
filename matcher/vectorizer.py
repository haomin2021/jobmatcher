from sklearn.feature_extraction.text import TfidfVectorizer

class TextVectorizer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')

    def fit(self, job_descriptions):
        self.vectorizer.fit(job_descriptions)

    def transform(self, docs):
        return self.vectorizer.transform(docs)