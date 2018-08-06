import ccxt
import time
import pandas as pd
import csv
import talib
from testbot import candle_info
from talib import abstract 
import numpy as np
from candles import candles_types
from Currency import Currency
from utlilities import trading_utilities
from account import account
import matplotlib.pyplot as plt
from graphing import graphing
from push_notifications import push_notification
#from botstrat import BotStrategy
#import matplotlib.animation as animation
#import matplotlib
#from botstrat import BotStrategy

def name(name):
	print("\033[0;0m")
	exchange = ccxt.gdax()
	current_buy_price = 0
	candlesticks = []
	open_ = []
	high = []
	low  = []
	close = []
	start_time = time.time()
	length_bear = 0
	length_bull = 0
	period = 60*5
	developingcandle = candle_info(period)
	utility = trading_utilities()
	timer = 0
	#strat = BotStrategy()
	my_time = []
	fama = []
	mama = []
	hl2 = []
	history = exchange.fetch_ohlcv(name,'5m')
	j = 0
	accounts = account()
	plot = graphing()
	push = push_notification()
	current_high = 0
	bought = 0
	
	plt.ion()
	
	for i in range(len(history)-1,0,-1):
		my_time.append(history[i][0]/1000.00)
		open_.append(history[i][1])
		high.append(history[i][2])
		low.append(history[i][3])
		close.append(history[i][4])
		
		candlesticks.append([history[i][0]/1000.00,history[i][1],history[i][2],history[i][3],history[i][4]])
		hl2.append((history[i][2]+history[i][3])/2.0)
		j+=1
		



	while True:
		try:
			ticks = float(((exchange.fetchTicker(name)['last'])))
			print(name,ticks)

		except:
			pass
		#take = testbot.candle_info(ticks)
		developingcandle.candle_tick(ticks)

		if current_high < ticks:
			current_high = ticks

		print(round((ticks-current_high)/current_high,4))


		if round((ticks-current_high)/current_high,4) < -.006 and bought == 1:
			current_high = 0
			bought = 0
			print("\033[1;31m"+ 'SELL ')
			with open('lists.csv','a') as lists:
				filewriter = csv.writer(lists,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow(["Sell",c,bull,bear])
				accounts.sell(c)




		if developingcandle.isClosed():
			o,h,l,c = developingcandle.candle_tick(ticks)
			t = time.time()
			my_time.append(t)
			
			candlesticks.append([t,o,h,l,c])
			open_.append(o)
			high.append(h)
			low.append(l)
			close.append(c)
			hl2.append((h+l)/2.0)
			developingcandle = candle_info(period)
			print("Open: "+str(o)+" High: "+str(h)+" Low: "+str(l)+" Close: "+str(c)+" current: "+str(ticks))
			open2 = np.array(open_,dtype=float)
			high2 = np.array(close,dtype=float)
			low2 = np.array(low,dtype=float)
			close2 = np.array(close,dtype=float)
			my_time2 = np.array(my_time,dtype=float)
			hl2_ = np.array(hl2,dtype=float)
			candles_info = candles_types(open2,high2,low2,close2)
			bull,bear = candles_info.all_candles()
			ema8 = talib.EMA(hl2_,8)
			ema3 = talib.EMA(hl2_,3)
			
			mama = np.round_(mama,3)
			fama = np.round_(fama,3)
			plot.update(open_[-40:],high[-40:],low[-40:],close[-40:],ema8[-40:],ema3[-40:])
			
			#plt.plot(my_time[-50:],close[-50:],'r',my_time[-50:],mama[-50:],'b',my_time[-50:],fama[-50:],'g')
			#plt.show()

			

			

			if len(close) > 2:
				

				crossover = utility.crossover(ema3,ema8)
				crossunder = utility.crossunder(ema3,ema8)

				

				if crossover == 1 and bought == 0:
					print( '\033[92m'+'BUY ')
					bought = 1
					with open('lists.csv','a') as lists:
						filewriter = csv.writer(lists,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
						filewriter.writerow(["Buy",-c,bull,bear])
						current_buy_price = c
						accounts.buy(c)
						#push.buy(name,c,c)

			timer = 1
			
		
		if len(open_)>50:
			del open_[0]
			del high[0]
			del low[0]
			del close[0]
			del my_time[0]
			del candlesticks[0]
			#print(open_)

		if timer == 1 and time.time() > start_time + period:
		#if len(candlesticks) > 0:
			open2 = np.array(open_,dtype=float)
			high2 = np.array(close,dtype=float)
			low2 = np.array(low,dtype=float)
			close2 = np.array(close,dtype=float)
			candles_info = candles_types(open2,high2,low2,close2)
			bull,bear = candles_info.all_candles()
			mama1 = np.array(mama,dtype=float)
			fama1 = np.array(fama,dtype=float)

		#if len(candlesticks) > 0 and (len(bull) != length_bull or len(bear) != length_bear):
			
			#print(open2)
			#candle = talib.CDLTRISTAR(open2,high2,low2,close2)
			#print(candle)

			
			length_bear = len(bear)
			length_bull= len(bull)
			Currency2 = Currency(bear,bull)
			reversal = Currency2.reversalMutator()
			continuation = Currency2.continuationMutator()
			print(bull,bear)
			print('reversal %.2f, continuation %.2f' % (reversal,continuation) )
			timer = 0
			if (reversal > 0 or continuation > 0) and not (reversal < 0 or continuation < 0) and crossover:
				with open('reversal.csv','a') as lists:
						filewriter = csv.writer(lists,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
						filewriter.writerow(("Buy", -close[-1]))

						

			if (reversal < 0 or continuation < 0) and not (reversal > 0 or continuation > 0) and crossunder:
				with open('reversal.csv','a') as lists:
						filewriter = csv.writer(lists,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
						filewriter.writerow(("Sell", close[-1]))



		
		
		
		
			
		time.sleep(exchange.rateLimit/1000)

		
		


name('ETH/USD')