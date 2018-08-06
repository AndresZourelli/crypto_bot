#from candles import candle_types
#from testbot import candle_info
import talib
import math
import numpy as np
from utilities import trading_utilities
class BotStrategy():
	utility = trading_utilities()
	def __init__(self):
		pass

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


	



		



