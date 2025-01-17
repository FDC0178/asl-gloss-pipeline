"""Preprocess the dataset: Tokenize, clean, and vectorize text."""
import spacy

def preprocess_text(text):
    nlp = spacy.load("en_core_web_sm")
    if not isinstance(text, str):
        # Handle non-string or missing values
        return ""
    doc = nlp(text.lower())
    return " ".join([token.text for token in doc if not token.is_stop and not token.is_punct])
