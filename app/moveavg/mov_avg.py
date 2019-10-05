import pandas as pd
import matplotlib.pyplot as plt

#datafile = 'SPY.csv'
#datafile = 'MSFT.csv'
datafile = '../../data/SPLK.csv'
#This creates a dataframe from the CSV file:
data = pd.read_csv(datafile, index_col = 'Date')
close = data['Adj Close']
close.index = pd.to_datetime(close.index)
# print("{0}".format(close))
# close.plot()
# plt.show()
sma50 = close.rolling(window=50).mean()
#print("{0}".format(sma50))
plt.style.use('fivethirtyeight')
#The size for our chart:
plt.figure(figsize = (12,6))
#Plotting price and SMA lines:
plt.plot(close, label='MSFT Adj Close', linewidth = 2)
plt.plot(sma50, label='50 day rolling SMA', linewidth = 1.5)
#Adding title and labeles on the axes, making legend visible:
plt.xlabel('Date')
plt.ylabel('Adjusted closing price ($)')
plt.title('Price with a single Simple Moving Average')
plt.legend()
plt.show()