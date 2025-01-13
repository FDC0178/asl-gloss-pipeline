"""Evaluate similarity scores between predicted and expected ASL gloss."""
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Initialize pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

def compute_similarity(expected_output, actual_output):
    """Compute cosine similarity between expected and actual outputs."""
    embeddings1 = model.encode([expected_output])
    embeddings2 = model.encode([actual_output])
    return cosine_similarity(embeddings1, embeddings2)[0][0]

def evaluate_similarity(input_file, output_file):
    """Evaluate similarity scores and save results."""
    # Read input Excel file
    df = pd.read_excel(input_file)

    # Ensure required columns exist
    if 'Expected Result' not in df.columns or 'Answer' not in df.columns:
        raise ValueError("File must contain 'Expected Result' and 'Answer' columns.")

    # Compute similarity scores
    df['Similarity Score'] = df.apply(lambda row: compute_similarity(row['Expected Result'], row['Answer']), axis=1)

    # Save results to a new Excel file
    df.to_excel(output_file, index=False, engine='openpyxl')
