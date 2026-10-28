# 📈 Crypto Market Explorer | Seaborn + Streamlit

Explores historical daily prices for BTC, ETH, SOL and USDT. A notebook combines the four datasets and runs exploratory charts with Seaborn, and a Streamlit app lets you pick a coin and a year to inspect closing prices, daily volatility, moving averages and correlations.

## Stack
`Python` `pandas` `Seaborn` `Matplotlib` `Streamlit` `Jupyter`

## What it does
- Loads the four coin CSVs, converts dates, tags each row with its coin and concatenates everything into one DataFrame
- Runs exploratory charts in the notebook: closing price over time, price distribution (histogram + KDE) and boxplot by coin
- Streamlit app with sidebar filters for coin and year, plus period and record count
- Eight interactive charts: closing price, daily volatility (high - low), open vs close scatter, 30-day moving average, volatility violin plot, price boxplot, price histogram + KDE and a correlation heatmap

## How to run
```bash
git clone https://github.com/lucas-wall/Seaborn-Streamlit-Crypto-Analysis.git
cd Seaborn-Streamlit-Crypto-Analysis
pip install pandas seaborn matplotlib streamlit
streamlit run app.py
```

To explore the notebook: `pip install jupyter && jupyter notebook crypto_analysis.ipynb` (it was built in Google Colab and reads the CSVs from `/content/`; change those paths to run locally).
