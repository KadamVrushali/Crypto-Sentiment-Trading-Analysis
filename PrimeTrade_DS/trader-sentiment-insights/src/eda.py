import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def run_eda(df: pd.DataFrame):
    output_dir = "outputs/eda"
    os.makedirs(output_dir, exist_ok=True)
    print("EDA DataFrame columns:", df.columns)

    sns.set(style="whitegrid", palette="Set2")

    # --- 1. Boxplot: pnl_per_unit vs Sentiment ---
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='classification', y='pnl_per_unit')
    plt.title('PnL per Unit vs Market Sentiment')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/boxplot_pnl_vs_sentiment.png")
    plt.close()

    # --- 2. Correlation Heatmap (Numerical Only) ---
    plt.figure(figsize=(12, 8))
    numeric_df = df.select_dtypes(include='number')
    corr = numeric_df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
    plt.title("Correlation Heatmap of Numeric Features")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/correlation_heatmap.png")
    plt.close()

    # --- 3. Pairplot: PnL, Size, Value ---
    pairplot_cols = ['pnl_per_unit', 'Size USD', 'value']
    sns.pairplot(df[pairplot_cols + ['classification']], hue='classification', diag_kind='kde')
    plt.savefig(f"{output_dir}/pairplot_selected_features.png")
    plt.close()

    # --- 4. Violin Plot: Size USD vs Sentiment ---
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=df, x='classification', y='Size USD')
    plt.title('Trade Size vs Market Sentiment')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/violin_size_sentiment.png")
    plt.close()

    # --- 5. Count Plot: Trades by Sentiment ---
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='classification')
    plt.title('Trade Counts by Sentiment')
    plt.tight_layout()
    plt.savefig(f"{output_dir}/count_trades_by_sentiment.png")
    plt.close()

    # --- 6. Count Plot: Coin Distribution ---
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x='Coin', order=df['Coin'].value_counts().index)
    plt.title('Trades by Coin')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"{output_dir}/count_trades_by_coin.png")
    plt.close()

    # --- 7. Heatmap: Sentiment vs Direction vs Profitability ---
    pivot = pd.crosstab([df['classification'], df['Direction']], df['is_profitable'])
    plt.figure(figsize=(8, 6))
    sns.heatmap(pivot, annot=True, fmt="d", cmap='Blues')
    plt.title("Sentiment & Direction vs Profitability")
    plt.tight_layout()
    plt.savefig(f"{output_dir}/heatmap_sentiment_direction_profitability.png")
    plt.close()

    print(f"✅ EDA plots saved to: {output_dir}")
