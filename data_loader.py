import pandas as pd

def load_kaggle_data(path):
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} rows from {path}")
    return df
