import pandas_datareader as web
import pandas as pd
import numpy as np

#tslaQuote = web.DataReader('TSLA', data_source='yahoo', start='2011-01-01', end='2019-10-31')
#print(tslaQuote)
# stocks =['SPY', 'MSFT', 'SPLK', 'TWLO', 'SNAP', 'NOK', 'BYL.TO', 'CNQ.TO', 'NPI.TO', 'BBD-B.TO']
stocks = ['MSFT']
numAssets = len(stocks)
source = 'yahoo'
start = '2015-01-01'
end = '2019-11-11'

data = pd.DataFrame(columns=stocks)
for symbol in stocks:
    data[symbol] = web.DataReader(symbol, data_source=source, start=start, end=end)['Adj Close']
    
# Calculating log returns
percent_change = data.pct_change()
returns = np.log(1+percent_change)
# print(returns.tail())
meanDailyReturns = returns.mean()
covMatrix = returns.cov()

meanDailyReturns

print(covMatrix)


