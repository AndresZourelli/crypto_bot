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
from botstrat import BotStrategy

def name(name):
	exchange = ccxt.coinbasepro()
	BotStrategys = BotStrategy()
	current_buy_price = 0
	candlesticks = []
	open_ = []
	high = []
	low  = []
	close = []
	start_time = time.time()
	length_bear = 0
	length_bull = 0
	period = 60
	developingcandle = candle_info(period)
	utility = trading_utilities()
	timer = 0
	count=0
	my_time = []
	fama = []
	mama = []
	hl2 = []
	history = exchange.fetch_ohlcv(name,'1m')
	j = 0
	accounts = account()
	plot = graphing()
	push = push_notification()
	current_high = 0
	bought = 0
	
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
			#print(name,ticks)
			

		except:
			# print("Error Occured")
			# print("Attempting to reconnect...")
			pass

		#Builds the acutal candles	
		developingcandle.candle_tick(ticks)

		#Determines the difference in percent between current price and highest price
		if current_high < ticks:
			current_high = ticks

		#print(round((ticks-current_high)/current_high,4))

		#Once Time period has passed a finished candle is added on to stack
		if developingcandle.isClosed():
			
			#Grabs OHLC values from candle_info class
			o,h,l,c = developingcandle.candle_tick(ticks)

			#Records current time and adds to list
			t = time.time()
			my_time.append(t)
			
			#adds tOHLC to candle list
			candlesticks.append([t,o,h,l,c])

			#Creates ability to access all values individually
			open_.append(o)
			high.append(h)
			low.append(l)
			close.append(c)
			#like an average for candle
			hl2.append((h+l)/2.0)

			#clears candle_info class
			developingcandle = candle_info(period)


			print("Open: "+str(o)+" High: "+str(h)+" Low: "+str(l)+" Close: "+str(c)+" current: "+str(ticks))
			
			#creates arrays to be used with ta-lib indicators in their desired format
			open2 = np.array(open_,dtype=float)
			high2 = np.array(close,dtype=float)
			low2 = np.array(low,dtype=float)
			close2 = np.array(close,dtype=float)
			my_time2 = np.array(my_time,dtype=float)
			hl2_ = np.array(hl2,dtype=float)

			#calls to candles_types class where all candle patterns are and returns list of candles names that are present
			candles_info = candles_types(open2,high2,low2,close2)
			bull,bear = candles_info.all_candles()

			#every 5 candles idealInvestment strategy has a chance to buy or sell
			if(count==0):
				BotStrategys.idealInvested(close, ticks,open2,high2,low2,close2)

			count+=1

			#change 5 to how frenquently buy/sell orders are desired
			if(count>5):
				count=0
			timer = 1
			
		#only keeps 50 candles and deletes extra
		if len(open_)>50:
			del open_[0]
			del high[0]
			del low[0]
			del close[0]
			del my_time[0]
			del candlesticks[0]

		# #
		# if timer == 1 and time.time() > start_time + period:
		# 	open2 = np.array(open_,dtype=float)
		# 	high2 = np.array(close,dtype=float)
		# 	low2 = np.array(low,dtype=float)
		# 	close2 = np.array(close,dtype=float)
		# 	candles_info = candles_types(open2,high2,low2,close2)
		# 	bull,bear = candles_info.all_candles()
		# 	mama1 = np.array(mama,dtype=float)
		# 	fama1 = np.array(fama,dtype=float)
		

		#Put code to sleep to ensure API ping does not exceed rate limit	
		time.sleep(exchange.rateLimit/1000)

		
		

# <------------------------------ Run Actual Function -------------------------->
name('ETC/USD')