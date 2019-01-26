#from candles import candle_types
#from testbot import candle_info
import talib
import math
import time
import csv
from account import account
import numpy as np
from utlilities import trading_utilities
from candles import candles_types
class BotStrategy():
	
	def __init__(self):
		self.utility = trading_utilities()
		self.account = account()

#----------------------------------------------------Talib indicator functions to be used in strategies found below--------------------------------------------------------
	def cycle_indicators(self):
		HT_dom_cycle_period = talib.HT_DCPERIOD(self.close)
		HT_dom_cycle_phase = talib.HT_DCPHASE(self.close)
		inphase, quadrature = talib.HT_PHASOR(self.close)
		sine, leadsine = talib.HT_SINE(self.close)
		HT_trend_mode = talib.HT_TRENDMODE(self.close)
		
	def overlap(self):
		upper, middle, lower = talib.BBANDS(self.close,timeperiod=5,nbdevup=2,nbdevdn=2,matype=0)
		EMA = talib.EMA(self.close,self.period)
		HT_trendline = talib.HT_TRENDLINE(self.close)
		KAMA = talib.KAMA(self.close,self.period)
		MA = talib.MA(self.close,self.period,matype=0)
		mama, fama = talib.MAMA(self.close,fastlimit = 0.5,slowlimit = 0.05)
		mavp = talib.MAVP(self.close, minperiod = 5,maxperiod = 30,matype=0)
		midpoint = talib.MIDPOINT(self.close,self.period)
		midprice = talib.MIDPRICE(self.high,self.low,self.period)
		sar = talib.SAR(self.high,self.low,acceleration = 0, maximum = 0)
		sarext = talib.SAREXT(self.high,self.low,startvalue=0,offsetonreverse=0,accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0)
		sma = talib.SMA(self.close,self.period)
		t3 = talib.T3(self.close, self.period, vfactor = 0)
		tema = talib.TEMA(self.close,self.period)
		trima = talib.TRIMA(self.close,period)
		wma = talib.WMA(self.close, self.period)

	def momentum(self):
		adx = talib.ADX(self.high,self.low,self.close,self.period)
		adxr = talib.ADXR(self.high,self.low,self.close,self.period)
		apo = talib.APO(self.high,self.low,self.close,self.period)
		aroondown, aroonup = talib.AROON(self.high, self.low, period)
		aroonosc = talib.AROONOSC(self.high,self.low,self.period)
		bop  = talib.BOP(self.opens,self.high,self.low,self.close)
		cci = talib.CCI(self.high,self.low,self.close,self.period)
		cmo = talib.CMO(self.close,self.period)
		dx = talib.DX(self.high,self.low,self.close,self.period)
		macd, macdsignal, macdhist = talib.MACD(self.close, fastperiod=period, slowperiod=period*5, signalperiod=period*2)
		macd1, macdsignal1, macdhist1 = talib.MACDEXT(self.close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
		macd2, macdsignal2, macdhist2 = talib.MACDFIX(self.close, signalperiod=9)
		mfi = talib.MFI(self.high, self.low, self.close, self.volume, timeperiod=14)
		minus_di = talib.MINUS_DI(self.high, self.low, self.close, timeperiod=14)
		minus_dm = talib.MINUS_DM(self.high, self.low, timeperiod=14)
		mom = talib.MOM(self.close, timeperiod=10)
		plus_di = talib.PLUS_DI(self.high, self.low, self.close, timeperiod=14)
		plus_dm = talib.PLUS_DM(self.high, self.low, timeperiod=14)
		ppo  = talib.PPO(self.close, fastperiod=12, slowperiod=26, matype=0)
		roc  = talib.ROC(self.close, timeperiod=10)
		rocp = talib.ROCP(self.close, timeperiod=10)
		rocr = talib.ROCR(self.close, timeperiod=10)
		rocr100 = talib.ROCR100(self.close, timeperiod=10)
		rsi =  talib.RSI(self.close, timeperiod=14)
		slowk, slowd = talib.STOCH(self.high, self.low, self.close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
		fastk, fastd = talib.STOCHF(self.high, self.low, self.close, fastk_period=5, fastd_period=3, fastd_matype=0)
		fastk1, fastd1 = talib.STOCHRSI(self.close, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0)
		trix = talib.TRIX(self.close, timeperiod=30)
		ultosc = talib.ULTOSC(self.high, self.low, self.close, timeperiod1=7, timeperiod2=14, timeperiod3=28)
		willr = talib.WILLR(self.high, self.low, self.close, timeperiod=14)

	def volume(self):
		ad  = talib.AD(self.high, self.low, self.close, self.volume)
		adosc = talib.ADOSC(self.high, self.low, self.close, self.volume, fastperiod=3, slowperiod=10)
		obv = talib.OBV(self.close, self.volume)

	def volatility(self):
		atr = talib.ATR(self.high, self.low, self.close, timeperiod=14)
		natr = talib.NATR(self.high, self.low, self.close, timeperiod=14)
		trange = talib.TRANGE(self.high, self.low, self.close)

	def price_transform(self):
		avgprice = talib.AVGPRICE(self.opens, self.high, self.low, self.close)
		medprice = talib.MEDPRICE(self.high, self.low)
		typprice = talib.TYPPRICE(self.high, self.low, self.close)
		wclprice = talib.WCLPRICE(self.high, self.low, self.close)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------Candle operations to determine coefficient-----------------------------------------------------------------
	def candlePressure(self, open2,high2,low2,close2):
		candles_info = candles_types(open2,high2,low2,close2)
		bull,bear = candles_info.all_candles()
		candle_pressure = 0

		for i in range(len(bull)):
			candle_pressure += bull[i]['percent']

		for i in range(len(bear)):
			candle_pressure += bear[i]['percent']

		if 'three_line_strike' in bull:
			candle_pressure += 84

		if 'three_line_strike' in bear:
			candle_pressure += -64

		if 'abandoned_baby' in bull:
			candle_pressure += 70

		if 'abandoned_baby' in bear:
			candle_pressure += -69

		if 'belt_hold' in bull:
			candle_pressure += 71

		if 'belt_hold' in bear:
			candle_pressure += -68

		if 'breakaway' in bull:
			candle_pressure += 59

		if 'breakaway' in bear:
			candle_pressure += -63

		if 'engulfing_pattern' in bull:
			candle_pressure += 63

		if 'engulfing_pattern' in bear:
			candle_pressure += -79

		if 'harami_cross_pattern' in bull:
			candle_pressure += 57

		if 'harami_cross_pattern' in bear:
			candle_pressure += -55

		if 'kicking' in bull:
			candle_pressure += 53

		if 'kicking' in bear:
			candle_pressure += -54

		if 'separating_lines' in bull:
			candle_pressure += 73

		if 'separating_lines' in bear:
			candle_pressure += -63

		if 'tristar' in bull:
			candle_pressure += 60

		if 'tristar' in bear:
			candle_pressure += -52

		if 'gap_three_methods' in bull:
			candle_pressure += 62

		if 'gap_three_methods' in bear:
			candle_pressure += -59

		print("Bull: ", bull)
		print("Bear: ", bear)
		return candle_pressure/500
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------Trading strategy based on determining what persentage of held assets is preffered in ETC------------------------------------------------------------
	def idealInvested(self, close, ticks, open2,high2,low2,close2):
		#determines range looked at to determine percent changed over x minutes
		x_minutes = 10
		#determines how many past orders by other traders will effect buy/sell decision
		x_orders = 10

		#checks account for current holdings
		balance = 19.72#self.account.total_USD(ticks)
		inUSD = self.account.balance_USD()
		inETC = self.account.balance_ETC()

		#determines what effect other traders order will effect buy/sell decision
		order_pressure = self.account.orderTotal(x_orders)/1000

		#determines what effect current trend will effect buy/sell decision
		trend_pressure = ((close[49]-close[49-x_minutes])/close[49])*(1/.015)

		#determines what effect candles will effect buy/sell decision
		candle_pressure = self.candlePressure(open2,high2,low2,close2)

		#determines what effect bolliinger bands will effect buy/sell decision
		band_pressure = self.bollingerBands(close)

		#coefficient to determine what npercent of total in trade is preferable in ETC
		coefficient = trend_pressure + order_pressure + candle_pressure + band_pressure
		if(coefficient>1):
			coefficient=1
		if(coefficient<0):
			coefficient=0

		#ideal USD invested in ETC
		ideal = coefficient*balance
		print("Ideal: " + str(ideal))

		#use ideal invested to determine buy/sell action assuring minimum trade is met
		buy = ideal-inETC*ticks
		sell = inETC*ticks-ideal
		if((buy/close[-1])>.1):
			with open('lists.csv','a') as lists:
				filewriter = csv.writer(lists,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow(["B Ideal$" ,ideal, "Total$", balance,
				 "Price$", close[-1], "Coefficient", coefficient, 'Order Pressure', order_pressure, 'Trend Pressure',
				  trend_pressure, 'Candle Pressure', candle_pressure, "Band Pressure", band_pressure, "Time", time.time()])
			#self.account.buyAmount(buy, ticks)
		elif((sell/close[-1])>.1):
			with open('lists.csv','a') as lists:
				filewriter = csv.writer(lists,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow(["S Ideal$", ideal, "Total$", balance,
				 "Price$", close[-1], "Coefficient", coefficient, 'Order Pressure', order_pressure, 'Trend Pressure',
				  trend_pressure, 'Candle Pressure', candle_pressure, "Band Pressure", band_pressure, "Time", time.time()])
			#self.account.sellAmount(sell, ticks)
		else:
			with open('lists.csv','a') as lists:
				filewriter = csv.writer(lists,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
				filewriter.writerow(["N Ideal$", ideal, "Total$", balance,
				 "Price$", close[-1], "Coefficient", coefficient, 'Order Pressure', order_pressure, 'Trend Pressure',
				  trend_pressure, 'Candle Pressure', candle_pressure, "Band Pressure", band_pressure,"Time", time.time()])
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	def bollingerBands(self, close):
		close2 = np.array(close,dtype=float)
		band_pressure = 0
		up, mid, low = talib.BBANDS(close2, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
		rsi = talib.RSI(close2, timeperiod=14)
		bbp = (close - low) / (up - low)

		if((rsi[-1] < 30) and (bbp[-1] < 0)):
			band_pressure = 1

		if((rsi[-1] > 70) and (bbp[-1] > 1)):
			band_pressure = -1
		return band_pressure