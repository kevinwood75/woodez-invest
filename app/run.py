import sys
from datetime import datetime,timedelta
import moveavg.mov_avg as mv_avg


if len(sys.argv) < 2:
    print("not enough aruments provided. exiting")
    exit(1)

ends = str(datetime.today()+ timedelta(days=1).strftime('%Y-%m-%d'))

count = 0
for symbol in sys.argv:
    if count > 0: 
       try:
            mv_avg.stock_graph(ticker = symbol, starts = '2015-01-01', ends = ends)
            ##mv_avg.stock_graph(ticker = symbol, starts = '2015-01-01', ends = '2020-03-17')
       except:
            print("Date does not exist in data. exiting...")
             
    count += 1

