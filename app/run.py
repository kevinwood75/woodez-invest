from datetime import datetime
import moveavg.mov_avg as mv_avg

ends = str(datetime.today().strftime('%Y-%m-%d'))


mv_avg.stock_graph(ticker = 'SPLK', starts = '2019-01-01', ends = ends)

