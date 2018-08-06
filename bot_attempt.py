import ccxt
import time


"""def data():
	polo = ccxt.poloniex()
	print(polo.returnTicker('ETH/BTC'))
	lists = polo.markets() 
	#for i in range(len(lists)):
	#	print(lists[i]) 
	#symbol ='ETH/BTC'
	#for symbol in lists:
	#	print(polo.fetch_order_book(symbol))
	#	time.sleep(2)
	


data()"""



exchange = ccxt.kraken()
markets = exchange.load_markets()
#print(exchange.id,markets)

"""while True:
	a = exchange.fetchTicker('ETH/USD')['last']
	b = exchange.fetchTicker('ETH/USD')['symbol']
	print(b,a)
	
	time.sleep(6)"""

"""class BotCandlestick():

	def __int__(self, period =12, opens=None, high=None, low=None, close=None,priceAverage=None):
		self.current = None
		self.opens = opens
		self.close = close
		self.high = high
		self.low = low
		self.start_Time = time.time()
		self.period = period
		self.priceAverage = priceAverage

	def candles(self,price):
		
		self.current = float(price)
		
		if self.opens is None:
			self.opens = self.current
		if self.high == None or self.current > self.high:
			self.high = self.current
		if self.low == None or self.current < self.low:
			self.low = self.current
		if time.time() >= (self.start_Time+self.period):
			self.close = self.current
			self.priceAverage = (self.high + self.low + self.close)/float(3)
			candle_sticks.append((self.opens, self.high, self.low, self.close,priceAverage))

	def isClosed(self):
		if self.close is not None:
			return True
		else:
			return False


			"""







def ETH_Kraken_Ticker():
	i=0
	last=[1]
	period = 60
	start_Time = time.time()
	exchange = ccxt.gdax()
	markets = exchange.load_markets()
	developing_candle_sticks = []
	candle_sticks = [None]
	j = 0
	print('Hello, I am Crypto Bot! \n Starting Trading..... ')
	opens = None
	high = None
	low = None
	close = None
	while True:
		

		coin_name = exchange.fetchTicker('ETH/USD')['symbol']
		current =  float(exchange.fetchTicker('ETH/USD')['last'])
		change = ((current - last[i])/last[i])*100
		
		last.append( current )
		print('%s $%.2f %.2f%%' %(coin_name,current,change))
		
		if candles(current,start_Time,period,candle_sticks,opens, high, low, close) is True:

			start_Time = time.time()
			j+=1
			opens = None
			high = None
			low = None
			close = None
			print('Open: $%.2f, High: $%.2f, Low: $%.2f, Close: $%.2f, Average: $%.2f'%(candle_sticks[j][0],candle_sticks[j][1],candle_sticks[j][2],candle_sticks[j][3],candle_sticks[j][4]))
		else:
			opens,high,low,close = (candles(current,start_Time,period,candle_sticks,opens, high, low, close))	
		
		
		i+=1
		time.sleep(1)

def candles(current,start_Time,period,candle_sticks,opens, high, low, close):
		
		current = float(current)
		
		if opens is None:
			opens = current
		if high == None or current > high:
			high = current
		if low == None or current < low:
			low = current
		if time.time() >= (start_Time+period):
			close = current
			priceAverage = (high + low + close)/float(3)
			candle_sticks.append((opens, high, low, close,priceAverage))
			return True
		return opens, high, low, close



ETH_Kraken_Ticker()






