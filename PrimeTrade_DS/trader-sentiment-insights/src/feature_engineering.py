### src/feature_engineering.py

def create_features(df):
    print("Creating features...")

    df['Side'] = df['Side'].str.capitalize()
    df['position_type'] = df['Side'].map({"Buy": "Long", "Sell": "Short"})

    # PnL per unit size (to normalize for position size)
    df['pnl_per_unit'] = df['Closed PnL'] / df['Size Tokens'].replace(0, 1)

    # Group-level stats (optional)
    df['is_profitable'] = df['Closed PnL'] > 0

    return df
