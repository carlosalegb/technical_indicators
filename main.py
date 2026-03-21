# %% Libraries
import talib as ta
import matplotlib.pyplot as plt
import yfinance as yf

plt.style.use('bmh')
aapl = yf.download('AAPL', '2019-01-01', '2021-04-30')
close_prices = aapl['Close'].values.flatten()

# %% Moving Average
aapl['SMA'] = ta.SMA(close_prices, 21)
aapl['EMA'] = ta.EMA(close_prices, 55)

# Plot
aapl[['Close', 'SMA', 'EMA']].plot(figsize=(15, 15))
plt.show()

# %% Bollinger bands
aapl['upper_band'], aapl['middle_band'], aapl['lower_band'] = ta.BBANDS(close_prices, timeperiod=20)

# Plot
aapl[['Close', 'upper_band', 'middle_band', 'lower_band']].plot(figsize=(15, 15))
plt.show()

# %% RSI
aapl['RSI'] = ta.RSI(close_prices, 14)
aapl[['Close','RSI']].plot(figsize=(15, 15))
plt.show()