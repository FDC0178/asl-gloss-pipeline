"""Markdown file describing project goals, usage, and setup."""
# Text-to-ASL Gloss Pipeline

This project provides a machine learning-based solution for converting English text into American Sign Language (ASL) gloss and evaluating results with similarity scoring.

## Repository Layout

```
.
├── data/
│   ├── simulated_asl_dataset.csv  # Simulated dataset for development and testing
│   ├── test_input.xlsx           # Test data for similarity evaluation
├── src/
│   ├── preprocess.py             # Code for data preprocessing
│   ├── model.py                  # Code for training and evaluating the model
│   ├── predict.py                # Code for making predictions with the model
│   ├── similarity.py             # Code for similarity evaluation
├── notebooks/
│   ├── exploration.ipynb         # Jupyter notebook for initial dataset exploration
├── main.py                       # Main script to orchestrate pipeline
├── requirements.txt              # Required libraries
└── README.md                     # Project description and instructions
```

## Setup

1. Clone the repository:
    ```
    git clone https://github.com/your-repo/asl-gloss-pipeline.git
    cd asl-gloss-pipeline
    ```

2. Install required libraries:
    ```
    pip install -r requirements.txt
    ```

3. Prepare your dataset:
    - Place the `simulated_asl_dataset.csv` file in the `data/` directory.

## Usage

1. **Train the Model:**
    ```
    python main.py --train data/simulated_asl_dataset.csv --model model.pkl
    ```

2. **Make Predictions:**
    ```
    python main.py --model model.pkl --input "I am going to the store"
    ```

3. **Evaluate Similarity:**
    ```
    python main.py --evaluate data/test_input.xlsx --output data/evaluation_results.xlsx
    ```
