"""Train a text-to-ASL gloss model."""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import pandas as pd
from src.preprocess import preprocess_text

def train_model(dataset_csv, output_model):
    df = pd.read_csv(dataset_csv)

    # Ensure column headers are correctly stripped
    df.columns = df.columns.str.strip()

    # Drop rows with missing or invalid values
    df = df.dropna(subset=['sentence', 'asl_gloss'])

    # Preprocess the 'sentence' column
    df['processed_sentence'] = df['sentence'].apply(preprocess_text)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        df['processed_sentence'], df['asl_gloss'], test_size=0.2, random_state=42
    )

    # Vectorize and train
    vectorizer = CountVectorizer()
    X_train_vect = vectorizer.fit_transform(X_train)
    X_test_vect = vectorizer.transform(X_test)

    model = MultinomialNB()
    model.fit(X_train_vect, y_train)

    # Evaluate and save model
    y_pred = model.predict(X_test_vect)
    print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")
    with open(output_model, 'wb') as f:
        pickle.dump((model, vectorizer), f)
