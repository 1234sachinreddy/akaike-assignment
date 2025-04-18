import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

# Train a simple model (for demonstration)
def train_model():
    X = [
        "I need help with my bill",
        "Why is my credit card charged twice?",
        "Unable to login to my account",
        "Having technical issues with your product",
        "How can I reset my password?",
        "Change my account details",
        "Requesting refund for double payment"
    ]

    y = [
        "Billing Issues",
        "Billing Issues",
        "Account Management",
        "Technical Support",
        "Account Management",
        "Account Management",
        "Billing Issues"
    ]

    model = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', MultinomialNB())
    ])

    model.fit(X, y)
    joblib.dump(model, "email_classifier.pkl")
    print("Model trained and saved.")

# Load and use the trained model
def classify_email(text):
    if not os.path.exists("email_classifier.pkl"):
        train_model()
    model = joblib.load("email_classifier.pkl")
    return model.predict([text])[0]
