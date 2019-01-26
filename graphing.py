
import matplotlib.pyplot as plt
from mpl_finance import candlestick2_ohlc
import matplotlib.animation as animation
import matplotlib


class graphing():
	def __init__(self):
		fig, self.ax = plt.subplots(facecolor="#07000d")
		fig.subplots_adjust()


	def update(self,open_,high,low,close,data1,data2):
		self.ax.cla()
		line,candles = candlestick2_ohlc(self.ax,open_,high,low,close,width=0.6,colorup='#53c156',colordown='#ff1717',alpha=1.0)
		candles.set_zorder(5)
		
		
		#quotes = [tuple([float(candles[i][0]),candles[i][1],candles[i][2],candles[i][3],candles[i][4]])for i in range(len(candles))]
		#line,patches=candlestick_ohlc(self.ax,quotes,width=0.2,colorup='#53c156',colordown='#ff1717',alpha=1.0)
		#for lines in line:
		#	lines.set_zorder(0)
		ran = len(data2)
		self.ax.plot(data2,'green')
		self.ax.plot(data1,'red')
		plt.grid()
		self.ax.autoscale_view()
		plt.pause(0.0001)
		
	


