import pandas as pd

def preprocess_and_merge(trader_df, sentiment_df):
    # Use 'Timestamp IST' as datetime in trader_df
    trader_df['time'] = pd.to_datetime(trader_df['Timestamp IST'], format='%d-%m-%Y %H:%M')
    trader_df['date'] = trader_df['time'].dt.date  # for merging

    # Use 'date' column in sentiment_df
    sentiment_df['time'] = pd.to_datetime(sentiment_df['date'], format='%Y-%m-%d')
    sentiment_df['date'] = sentiment_df['time'].dt.date  # for merging

    # Merge on date
    merged_df = pd.merge(trader_df, sentiment_df, on='date', how='inner')

    return merged_df
