from sklearn.feature_extraction.text import TfidfVectorizer

class TextVectorizer:
    def __init__(self, stop_words='english', ngram_range=(1,1), max_features=None):
        self.vectorizer = TfidfVectorizer(
            stop_words=stop_words,
            ngram_range=ngram_range,
            max_features=max_features
        )
        self.is_fitted = False  # 用于判断是否已经 fit

    def fit(self, job_descriptions):
        self.vectorizer.fit(job_descriptions)
        self.is_fitted = True

    def transform(self, docs):
        if not self.is_fitted:
            raise ValueError("Vectorizer has not been fitted yet.")
        return self.vectorizer.transform(docs)

    def fit_transform(self, job_descriptions):
        self.is_fitted = True
        return self.vectorizer.fit_transform(job_descriptions)

    def get_feature_names(self):
        return self.vectorizer.get_feature_names_out()
    
    def print_tfidf_scores(self, docs):
        """
        打印每个文档中每个词的 TF-IDF 分数
        """
        vecs = self.transform(docs)
        feature_names = self.vectorizer.get_feature_names_out()

        for doc_index, vec in enumerate(vecs):
            print(f"\n🔍 文档 {doc_index + 1} 的 TF-IDF 分数：")
            dense = vec.todense().tolist()[0]
            scores = [(feature_names[i], score) for i, score in enumerate(dense) if score > 0]
            scores.sort(key=lambda x: x[1], reverse=True)
            for word, score in scores:
                print(f"{word:20s} -> {score:.4f}") 
    
#########################################################################################
#########################################################################################
if __name__ == "__main__":
    job_descriptions = [
        "Looking for a data scientist with Python and machine learning experience.",
        "We need a front-end engineer with React and JavaScript skills."
    ]
    resume = "Experienced Python developer with skills in data analysis and machine learning."

    vec = TextVectorizer()
    vec.fit(job_descriptions)

    # 打印简历中的词权重
    vec.print_tfidf_scores([resume])