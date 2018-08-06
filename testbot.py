
import ccxt
import time

class candle_info(object):


	def __init__ (self,period,opens=None,high=None,low=None,close=None):
		self.opens = opens
		self.high = high
		self.low = low
		self.close = close
		self.current = None
		self.period = period
		self.startTime = time.time()

	def candle_tick(self, price):
		self.current = price
		if self.opens is None:
			self.opens = self.current
		if self.high is None or self.current > self.high:
			self.high = self.current
		if self.low is None or self.current < self.low:
			self.low = self.current
		if time.time() >= self.startTime + self.period:
			self.close =self.current
			
			return(self.opens,self.high,self.low,self.close)
		
	def isClosed(self):
		if self.close is not None:
			return True

		else:
			return False



