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
    sma50 = close.rolling(window=50).mean()
    sma20 = close.rolling(window=20).mean()
    priceSma_df = pd.DataFrame({
        'Adj Close' : close,
        'SMA 20': sma20,
        'SMA 50': sma50
    })

    plt.style.use('fivethirtyeight')
    plt.figure(figsize = (12,6))
    plt.plot(priceSma_df[starts:ends]['Adj Close'], label="{0} Adj Close".format(ticker), linewidth = 2)
    plt.plot(priceSma_df[starts:ends]['SMA 20'], label='20 days rolling SMA', linewidth = 1.5)
    plt.plot(priceSma_df[starts:ends]['SMA 50'], label='50 days rolling SMA', linewidth = 1.5)
##    plt.plot(close, label="{0} Adj Close".format(ticker), linewidth = 2)
##    plt.plot(sma50, label='50 day rolling SMA', linewidth = 1.5)
    plt.xlabel('Date')
    plt.ylabel('Adjusted closing price ($)')
    plt.title("{0} Price with a single Simple Moving Average".format(ticker))
    plt.legend()
##    plt.savefig("../../images/{0}.jpg".format(ticker))
##    plt.savefig("/Users/kwood/projects/woodez-invest/app/images/{0}.jpg".format(ticker))
    plt.savefig("../images/{0}.jpg".format(ticker))
## stock_graph(ticker = 'SPLK', starts = '2019-01-01', ends = '2019-10-04')
