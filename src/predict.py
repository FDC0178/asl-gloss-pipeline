"""Make predictions using the trained model."""
import pickle
from src.preprocess import preprocess_text

def load_model(model_path):
    with open(model_path, 'rb') as f:
        return pickle.load(f)

def predict(input_text, model_path):
    model, vectorizer = load_model(model_path)
    processed_text = preprocess_text(input_text)
    vect_text = vectorizer.transform([processed_text])
    return model.predict(vect_text)[0]