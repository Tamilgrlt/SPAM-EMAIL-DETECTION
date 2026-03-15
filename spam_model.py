# Import libraries
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Create dataset
data = {
    "email": [
        "Win money now",
        "Hello how are you",
        "Claim your free prize",
        "Meeting tomorrow",
        "Free lottery ticket",
        "Project discussion today",
        "Congratulations you won",
        "Let's have lunch",
        "Earn money quickly",
        "See you in class"
    ],
    "label": [
        "spam",
        "ham",
        "spam",
        "ham",
        "spam",
        "ham",
        "spam",
        "ham",
        "spam",
        "ham"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert text to numeric vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["email"])
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# Test with new email
test_email = ["You won free money"]

test_vector = vectorizer.transform(test_email)
prediction = model.predict(test_vector)

print("\nNew Email Prediction:", prediction[0])