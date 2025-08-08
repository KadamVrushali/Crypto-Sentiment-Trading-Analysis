---

# ⋆.˚🦋༘⋆ Crypto Sentiment Trading Analysis

**Repository:** `crypto-sentiment-trader-analysis`
**Goal:** Understand how Bitcoin market sentiment (Fear & Greed Index) impacts trader behavior and profitability using real Hyperliquid exchange data.

---

## ⋆.˚🦋༘⋆ Overview

This project analyzes historical **Bitcoin sentiment** and **real trader data** to identify profitable trading patterns. It includes a full pipeline from **data ingestion** to **visual EDA**, **strategy logic**, and **correlation analysis**, enabling insights for sentiment-driven trading strategies.

---

## ⋆.˚🦋༘⋆ Dataset

* **Fear & Greed Index**: Historical sentiment data
* **Hyperliquid Trades**: Real trader executions — PnL, positions, timestamps
* **Time Span**: Historical match-aligned data
* **Volume**: 200K+ trades processed

---

## ⋆.˚🦋༘⋆ Key Insights

* **Extreme Fear + Long positions** → Highest average profits (up to ±\$15K)
* **Fear periods** → Most active, consistent trading (\~62K trades)
* **Extreme Greed** → Risky with mixed shorting results
* **Asset Imbalance** → One asset dominates 70K+ trades

---

## ⋆.˚🦋༘⋆ Analysis Pipeline

### ⋆.˚🦋༘⋆ Main Stages:

1. **Data Cleaning**: Null handling, timestamp alignment
2. **Feature Engineering**: PnL per unit, trade scaling, position metrics
3. **EDA & Correlation**: Heatmaps, scatter plots, distribution analysis
4. **Sentiment-based Strategy Logic**: Rule-based contrarian logic
5. **Validation**: Profitability vs sentiment phase, position size, asset bias

### ⋆.˚🦋༘⋆ Output Visuals:

* `pnl_sentiment_boxplot.png`
* `correlation_heatmap.png`
* `trade_volume_analysis.png`
* `position_size_distribution.png`

---

## ⋆.˚🦋༘⋆ Trading Strategy Logic

```python
if sentiment == "Extreme Fear":
    strategy = "BUY (Long)"
    position_size = "Large"

elif sentiment == "Fear":
    strategy = "BUY (Long)"
    position_size = "Medium"

elif sentiment == "Extreme Greed":
    strategy = "SELL (Short)"
    position_size = "Small"
```

---

## ⋆.˚🦋༘⋆ Installation & Usage

```bash
# 1. Clone the repo
git clone https://github.com/kadamvrushali/crypto-sentiment-trader-analysis.git
cd crypto-sentiment-trader-analysis

# 2. (Optional) Set up a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run full analysis
python main.py

# 5. (Optional) Explore individual notebooks
jupyter notebook notebooks/01_data_exploration.ipynb
```

---

## ⋆.˚🦋༘⋆ Project Structure

```
crypto-sentiment-trader-analysis/
├── data/                    # Raw data (sentiment, trades)
├── notebooks/               # Jupyter EDA, strategy notebooks
├── plots/                   # Saved visualizations
├── src/                     # Core pipeline scripts
│   ├── data_processing.py
│   ├── sentiment_analysis.py
│   ├── eda.py
│   └── visualization.py
├── main.py                  # Main analysis pipeline
├── requirements.txt
└── README.md
```

---

## ⋆.˚🦋༘⋆ Results Summary

* **Best Strategy**: Extreme Fear → Long positions
* **Trade Volume**: Fear periods dominate
* **Profit Range**: ±\$15K in extreme sentiment
* **Strategy Type**: Contrarian, sentiment-aligned

---

---

## ⋆.˚🦋༘⋆ Contact

* **Email**: [kvrushalimay@gmail.com](mailto:kvrushalimay@gmail.com)
* **LinkedIn**: [Vrushali Kadam](https://www.linkedin.com/in/vrushalikadam14/)

---
## ⋆.˚🦋༘⋆ Credits 
**Vrushali Kadam** – Data analysis, pipeline development, visualization

Let me know if you'd like to convert this into Markdown or re-upload it to your repo!
