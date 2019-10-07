import sys
from datetime import datetime
import moveavg.mov_avg as mv_avg


if len(sys.argv) < 2:
    print("not enough aruments provided. exiting")
    exit(1)

ends = str(datetime.today().strftime('%Y-%m-%d'))

count = 0
for symbol in sys.argv:
    print("{}".format(str(symbol)))
    if count is not 0:    
       mv_avg.stock_graph(ticker = symbol, starts = '2019-01-01', ends = ends)
       count += 1

