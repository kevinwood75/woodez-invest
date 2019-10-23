import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters


def stock_graph(**kwargs):
    register_matplotlib_converters()
    ticker = kwargs['ticker'] 
    starts = kwargs['starts']
    ends = kwargs['ends']
    yf.pdr_override()
    data = pdr.get_data_yahoo(ticker, start=starts, end=ends)
    close = data['Adj Close']
    close.index = pd.to_datetime(close.index)
    sma100 = close.rolling(window=100).mean()
    sma50 = close.rolling(window=50).mean()
    sma20 = close.rolling(window=20).mean()
    print(sma20.tail(1).values.pop())
    if float(close[ends]) < float(sma20[ends]):
       pricdiff = float(sma20[ends]) - float(close[ends])
       print("Buy {0} its close is lower then 20 day moving average by {1}({2})".format(ticker,pricdiff,close[ends]))
    if float(close[ends]) > float(sma20[ends]):
       pricdiff = float(close[ends]) - float(sma20[ends])
       print("Sell {0} its close is Higher then 20 day moving average by {1}({2})".format(ticker,pricdiff,close[ends]))
    sma15 = close.rolling(window=15).mean()
    priceSma_df = pd.DataFrame({
        'Adj Close' : close,
        'SMA 15': sma15,
        'SMA 20': sma20,
        'SMA 50': sma50,
        'SMA 100': sma100
    })

    plt.style.use('fivethirtyeight')
    plt.figure(figsize = (12,6))
    plt.plot(priceSma_df[starts:ends]['Adj Close'], label="{0} Adj Close".format(ticker), linewidth = 2)
    plt.plot(priceSma_df[starts:ends]['SMA 15'], label='15 days rolling SMA', linewidth = 1.5)
    plt.plot(priceSma_df[starts:ends]['SMA 20'], label='20 days rolling SMA', linewidth = 1.5)
    plt.plot(priceSma_df[starts:ends]['SMA 50'], label='50 days rolling SMA', linewidth = 1.5)
    plt.plot(priceSma_df[starts:ends]['SMA 100'], label='100 days rolling SMA', linewidth = 1.5)
    plt.xlabel('Date')
    plt.ylabel('Adjusted closing price ($)')
    plt.title("{0} Price with Moving Average".format(ticker))
    plt.legend()
    plt.savefig("/var/www/html/stocks/images/{0}.jpg".format(ticker))

