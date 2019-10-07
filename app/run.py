import sys
from datetime import datetime
import moveavg.mov_avg as mv_avg


if len(sys.argv) < 2:
    print("not enough aruments provided. exiting")
    exit(1)

ends = str(datetime.today().strftime('%Y-%m-%d'))
symbol = str(sys.argv[1])
mv_avg.stock_graph(ticker = symbol, starts = '2019-01-01', ends = ends)

