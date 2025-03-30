import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf

# Download historical Bitcoin data
btc = yf.download('BTC-USD', start='2023-01-01', end='2024-01-01')

# Calculate moving averages
btc['MA50'] = btc['Close'].rolling(window=50).mean()
btc['MA200'] = btc['Close'].rolling(window=200).mean()

# Plot Bitcoin Closing Prices
plt.figure(figsize=(12, 6))
sns.set_style("darkgrid")
plt.plot(btc.index, btc['Close'], label='Closing Price', color='blue')
plt.plot(btc.index, btc['MA50'], label='50-day MA', color='red', linestyle='dashed')
plt.plot(btc.index, btc['MA200'], label='200-day MA', color='green', linestyle='dashed')
plt.title('Bitcoin Price Analysis (2023)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.show()

# Plot daily returns
btc['Daily Return'] = btc['Close'].pct_change()
plt.figure(figsize=(12, 6))
sns.histplot(btc['Daily Return'].dropna(), bins=50, kde=True, color='purple')
plt.title('Bitcoin Daily Returns Distribution')
plt.xlabel('Daily Return')
plt.ylabel('Frequency')
plt.show()

# Correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(btc[['Open', 'High', 'Low', 'Close', 'Volume']].corr(), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Bitcoin Price Correlation Matrix')
plt.show()

# Volatility analysis
btc['Volatility'] = btc['Daily Return'].rolling(window=30).std()
plt.figure(figsize=(12, 6))
plt.plot(btc.index, btc['Volatility'], label='30-day Volatility', color='orange')
plt.title('Bitcoin 30-day Rolling Volatility')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.show()
