### src/load_data.py
import pandas as pd

def load_trader_data(path):
    print(f"Loading trader data from {path}...")
    return pd.read_csv(path)

def load_sentiment_data(path):
    print(f"Loading sentiment data from {path}...")
    return pd.read_csv(path)
