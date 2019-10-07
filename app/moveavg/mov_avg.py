import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt


def stock_graph(**kwargs):
    ticker = kwargs['ticker'] 
    starts = kwargs['starts']
    ends = kwargs['ends']
    yf.pdr_override()
    data = pdr.get_data_yahoo(ticker, start=starts, end=ends)
    close = data['Adj Close']
    close.index = pd.to_datetime(close.index)
    sma50 = close.rolling(window=5).mean()
    plt.style.use('fivethirtyeight')
    plt.figure(figsize = (12,6))
    plt.plot(close, label="{0} Adj Close".format(ticker), linewidth = 2)
    plt.plot(sma50, label='50 day rolling SMA', linewidth = 1.5)
    plt.xlabel('Date')
    plt.ylabel('Adjusted closing price ($)')
    plt.title("{0} Price with a single Simple Moving Average".format(ticker))
    plt.legend()
    plt.savefig("../../images/{0}.jpg".format(ticker))

stock_graph(ticker = 'SPLK', starts = '2019-01-01', ends = '2019-10-04')
