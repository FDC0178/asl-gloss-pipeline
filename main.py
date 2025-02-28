"""Main entry point for the pipeline."""
from src.model import train_model
from src.predict import predict
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text-to-ASL Gloss Pipeline")
    parser.add_argument('--train', help="Path to training dataset (CSV)", required=False)
    parser.add_argument('--model', help="Output path for trained model", required=False)
    parser.add_argument('--input', help="Input text for prediction", required=False)

    args = parser.parse_args()

    if args.train and args.model:
        train_model(args.train, args.model)

    if args.input and args.model:
        gloss = predict(args.input, args.model)
        print(f"Input Text: {args.input}\nASL Gloss: {gloss}")
