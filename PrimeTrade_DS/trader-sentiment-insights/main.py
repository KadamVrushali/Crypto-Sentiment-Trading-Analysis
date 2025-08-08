### main.py
from src.load_data import load_trader_data, load_sentiment_data
from src.preprocess import preprocess_and_merge
from src.feature_engineering import create_features
from src.eda import run_eda
import os

def main():
    print("Starting Trader Behavior vs Market Sentiment Analysis Pipeline...")

    # Load raw data
    trader_df = load_trader_data("data/raw/historical_data.csv")
    #print("Trader data columns:", trader_df.columns.tolist())

    sentiment_df = load_sentiment_data("data/raw/fear_greed_index.csv")

    # Merge & preprocess
    merged_df = preprocess_and_merge(trader_df, sentiment_df)
    print("Merged columns:", merged_df.columns)

    # Feature engineering
    features_df = create_features(merged_df)

    # Run EDA and save plots
    run_eda(features_df)

    # Save processed dataset
    os.makedirs("data/processed", exist_ok=True)
    features_df.to_csv("data/processed/merged_data.csv", index=False)
    print("\n✅ Pipeline complete. Processed data and plots saved.")

if __name__ == "__main__":
    main()
