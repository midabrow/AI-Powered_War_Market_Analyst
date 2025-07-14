from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from typing import List

class NewsClassifier:
    """
    Simple text classifier using Naive Bayes for war-related event tagging.
    """

    def __init__(self):
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()

    def train(self, texts: List[str], labels: List[str]) -> None:
        """
        Train the classifier on labeled text data.
        """
        X = self.vectorizer.fit_transform(texts)
        self.model.fit(X, labels)

    def predict(self, text: str) -> str:
        """
        Predict the tag for a given text input.
        """
        X = self.vectorizer.transform([text])
        return self.model.predict(X)[0]