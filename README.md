# Crypto Sentiment Trading Analysis

**Repository Name:** `crypto-sentiment-trader-analysis`

## Overview

This project analyzes the relationship between Bitcoin market sentiment (Fear & Greed Index) and trader performance using Hyperliquid trading data. The goal is to find patterns that can improve trading strategies in cryptocurrency markets.

## Dataset

- **Bitcoin Market Sentiment**: Fear/Greed classification data
- **Hyperliquid Trading Data**: Real trader execution data with PnL, position sizes, timestamps
- **Time Period**: Historical trading data with sentiment alignment
- **Size**: 200K+ trading records analyzed

## Key Findings

### 💡 Main Insight
**Extreme Fear periods create the best buying opportunities** despite having fewer trades.

### 📊 Results Summary
- **Extreme Fear + Long trades**: Highest profit potential (±$15K range)
- **Fear periods**: Most trading activity (62K trades) with steady returns
- **Greed periods**: Mixed results, some short opportunities
- **Asset concentration**: One coin dominates 70K+ trades

## Analysis Approach

### Data Exploration
1. **Market sentiment distribution** - Trade counts by Fear/Greed levels
2. **PnL analysis** - Profit patterns across sentiment categories  
3. **Correlation analysis** - Relationships between trading metrics
4. **Position sizing** - How sentiment affects trade sizes
5. **Asset distribution** - Trading concentration analysis

### Visualization
- Box plots for PnL distribution by sentiment
- Correlation heatmaps for feature relationships
- Bar charts for trading volume analysis
- Scatter plots for multi-dimensional patterns
- Violin plots for position size distributions

## Trading Strategy

### Simple Rules
```python
# Contrarian approach based on market sentiment
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

## Files Structure

```
crypto-sentiment-trader-analysis/
├── data/
│   ├── fear_greed_index.csv
│   └── hyperliquid_trades.csv
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_sentiment_analysis.ipynb
│   └── 03_trading_strategy.ipynb
├── plots/
│   ├── pnl_sentiment_boxplot.png
│   ├── correlation_heatmap.png
│   ├── trade_volume_analysis.png
│   └── position_size_distribution.png
├── src/
│   ├── data_processing.py
│   ├── sentiment_analysis.py
│   └── visualization.py
├── README.md
└── requirements.txt
```

## Technical Requirements

```python
pandas>=1.5.0
numpy>=1.20.0
matplotlib>=3.5.0
seaborn>=0.11.0
plotly>=5.0.0
jupyter>=1.0.0
```

## Installation & Usage

```bash
# Clone repository
git clone https://github.com/[username]/crypto-sentiment-trader-analysis.git
cd crypto-sentiment-trader-analysis

# Install requirements
pip install -r requirements.txt

# Run analysis
jupyter notebook notebooks/01_data_exploration.ipynb
```

## Results

### Key Metrics
- **Best Strategy**: Extreme Fear + Long positions
- **Risk/Reward**: High volatility but positive expected value
- **Trade Volume**: Fear periods generate 3x more activity
- **Profit Range**: ±$15K in extreme sentiment periods

### Business Value
- Systematic trading approach based on market psychology
- Risk-adjusted position sizing framework
- Contrarian strategy validation with real market data
- Scalable algorithm for automated trading

## Methodology

1. **Data Cleaning**: Handle missing values, align timestamps
2. **Feature Engineering**: Calculate PnL per unit, position metrics
3. **Exploratory Analysis**: Visualize patterns and correlations
4. **Strategy Development**: Define rules based on findings
5. **Validation**: Test approach across different market conditions

## Limitations

- Analysis based on historical data only
- Single exchange (Hyperliquid) data source  
- Market conditions may change over time
- Requires proper risk management implementation

## Future Work

- Real-time sentiment integration
- Multi-exchange analysis
- Machine learning model development
- Backtesting framework implementation
- Risk management optimization

## Contact

For questions about this analysis or collaboration opportunities:
- **Email**: kvrushalimay@gmail.com
- **LinkedIn**: https://www.linkedin.com/in/vrushalikadam14/

---

*This project was created as part of a data science assignment analyzing trader behavior and market sentiment relationships in cryptocurrency markets.*

## License

MIT License - see LICENSE file for details.
