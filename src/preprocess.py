"""Preprocess the dataset: Tokenize, clean, and vectorize text."""
import pandas as pd
import spacy

def preprocess_text(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text.lower())
    return " ".join([token.text for token in doc if not token.is_stop and not token.is_punct])

def preprocess_dataset(input_csv):
    df = pd.read_csv(input_csv)
    df['processed_sentence'] = df['sentence'].apply(preprocess_text)
    return df[['processed_sentence', 'asl_gloss']]