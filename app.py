import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
btc = pd.read_csv('BTC.csv')
sol = pd.read_csv('SOL.csv')
eth = pd.read_csv('ETH.csv')
usdt = pd.read_csv('USDT.csv')

# Prepare data
btc['date'] = pd.to_datetime(btc['date'])
sol['date'] = pd.to_datetime(sol['date'])
eth['date'] = pd.to_datetime(eth['date'])
usdt['date'] = pd.to_datetime(usdt['date'])

btc['coin'] = 'BTC'
sol['coin'] = 'SOL'
eth['coin'] = 'ETH'
usdt['coin'] = 'USDT'

df = pd.concat([btc, sol, eth, usdt])
df.sort_values(by='date', inplace=True)
df['volatility'] = df['high'] - df['low']

# Sidebar coin selector
coin = st.sidebar.selectbox('💱 Choose a Coin:', ['BTC', 'SOL', 'ETH', 'USDT'])
data = df[df['coin'] == coin].copy()

# Year filter
selected_year = st.sidebar.selectbox('🔄 Select a Year:', sorted(df['date'].dt.year.unique(), reverse=True))
data = data[data['date'].dt.year == selected_year]

st.sidebar.markdown(f"**Period:** {data['date'].min().date()} → {data['date'].max().date()}")
st.sidebar.markdown(f"**Total Records:** {data.shape[0]}")

# Chart 1 - Closing Price
st.subheader(f'📉 Closing Price Over Time - {coin} ({selected_year})')
fig1, ax1 = plt.subplots(figsize=(12, 4))
sns.lineplot(data=data, x='date', y='close', ax=ax1)
ax1.set_ylabel('Closing Price (USD)')
st.pyplot(fig1)

st.markdown("""
*This chart shows how the coin's closing price evolves over time.
It makes upward and downward price trends visible and helps identify periods of higher volatility.*
""")

# Chart 2 - Daily Volatility
st.subheader(f'⚡ Daily Volatility (High - Low) - {coin} ({selected_year})')
fig2, ax2 = plt.subplots(figsize=(12, 4))
sns.lineplot(data=data, x='date', y='volatility', color='orange', ax=ax2)
ax2.set_ylabel('Volatility (USD)')
st.pyplot(fig2)

st.markdown("""
*This chart shows daily volatility, calculated as the difference between the day's highest and lowest price.
High volatility can signal strong uncertainty or a shift in market trends.*
""")

# Chart 3 - Open vs Close Correlation
st.subheader(f'🔗 Open vs Close Correlation - {coin} ({selected_year})')
fig3, ax3 = plt.subplots(figsize=(6, 4))
sns.scatterplot(data=data, x='open', y='close', ax=ax3)
ax3.set_xlabel('Open (USD)')
ax3.set_ylabel('Close (USD)')
st.pyplot(fig3)

st.markdown("""
*This scatter plot shows how the opening price relates to the closing price.
A strong correlation may indicate that the coin tends to keep its direction throughout the day.*
""")

# Chart 4 - 30-Day Moving Average
st.subheader(f'📈 30-Day Moving Average - {coin} ({selected_year})')
data['moving_avg'] = data['close'].rolling(window=30).mean()
fig4, ax4 = plt.subplots(figsize=(12, 4))
sns.lineplot(data=data, x='date', y='close', label='Close', ax=ax4)
sns.lineplot(data=data, x='date', y='moving_avg', label='Moving Average (30d)', ax=ax4)
ax4.set_ylabel('USD')
ax4.legend()
st.pyplot(fig4)

st.markdown("""
*The 30-day moving average smooths out daily fluctuations and reveals the underlying price trend.
It is useful for spotting more gradual changes in the price pattern over time.*
""")

# Chart 5 - Volatility Distribution
st.subheader(f'🎻 Volatility Distribution - {coin} ({selected_year})')
fig5, ax5 = plt.subplots(figsize=(6, 4))
sns.violinplot(data=data, x='coin', y='volatility', ax=ax5)
ax5.set_ylabel('Volatility')
st.pyplot(fig5)

st.markdown("""
*The violin plot is useful for comparing the volatility distribution across coins. It also shows the median,
the quartiles and the overall shape of the distribution.*
""")

# Chart 6 - Price Boxplot
st.subheader(f'📦 Closing Price Boxplot - {coin} ({selected_year})')
fig6, ax6 = plt.subplots(figsize=(6, 4))
sns.boxplot(data=data, y='close', ax=ax6)
ax6.set_ylabel('Close (USD)')
st.pyplot(fig6)

st.markdown("""
*The boxplot shows the spread of closing prices and highlights outliers,
that is, days when prices were unusually high or low.*
""")

# Chart 7 - Price Histogram + KDE
st.subheader(f'📊 Closing Price Distribution - {coin} ({selected_year})')
fig7, ax7 = plt.subplots(figsize=(8, 4))
sns.histplot(data['close'], kde=True, bins=50, ax=ax7)
ax7.set_xlabel('Close (USD)')
st.pyplot(fig7)

st.markdown("""
*This histogram with a density curve shows the distribution of closing prices.
It helps assess the central tendency and the spread of prices.*
""")

# Chart 8 - Correlation Heatmap
st.subheader(f'🧪 Correlation between Variables - {coin} ({selected_year})')
fig8, ax8 = plt.subplots(figsize=(6, 4))
sns.heatmap(
    data[['open', 'high', 'low', 'close', 'volatility']].corr(),
    annot=True, cmap='coolwarm', ax=ax8, fmt=".2f"
)
st.pyplot(fig8)

st.markdown("""
*This heatmap shows the correlation between the main variables, such as opening price, closing price and volatility.
A high correlation between two variables means they are strongly related.*
""")

# Conclusion
st.markdown("---")
st.subheader("🔍 Conclusion")
st.markdown("""
This exploratory analysis shows how BTC, SOL, ETH and USDT behave over time in terms of price, volatility and other key variables.

Interactive charts make it possible to explore trends, identify periods of high volatility and observe the relationship between opening and closing prices.

The **moving average** smooths the data and makes trends clearer, while the **boxplot** and **violin plot** help identify outliers and better understand the data distribution.

Together, these charts give investors and analysts a clear, practical view that supports better-informed decisions about these assets.

With **year selection** and per-coin views, the app becomes a useful tool for comparing different cryptocurrencies side by side.
""")
