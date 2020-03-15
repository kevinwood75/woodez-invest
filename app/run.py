import sys
from datetime import datetime
import moveavg.mov_avg as mv_avg


if len(sys.argv) < 2:
    print("not enough aruments provided. exiting")
    exit(1)

ends = str(datetime.today().strftime('%Y-%m-%d'))

count = 0
for symbol in sys.argv:
    if count > 0: 
       try:
#            mv_avg.stock_graph(ticker = symbol, starts = '2019-01-01', ends = ends)
             mv.avg.stock_graph(ticker = symbol, starts = '2008-01-01', ends = ends)
       except:
            print("Date does not exist in data. exiting...")
             
    count += 1

