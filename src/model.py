"""Train a text-to-ASL gloss model."""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
from src.preprocess import preprocess_dataset

def train_model(dataset_csv, output_model):
    data = preprocess_dataset(dataset_csv)
    X_train, X_test, y_train, y_test = train_test_split(data['processed_sentence'], data['asl_gloss'], test_size=0.2, random_state=42)
    vectorizer = CountVectorizer()
    X_train_vect = vectorizer.fit_transform(X_train)
    X_test_vect = vectorizer.transform(X_test)

    model = MultinomialNB()
    model.fit(X_train_vect, y_train)
    y_pred = model.predict(X_test_vect)
    print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

    with open(output_model, 'wb') as f:
        pickle.dump((model, vectorizer), f)
