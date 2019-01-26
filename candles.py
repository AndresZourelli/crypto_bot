import time
import talib 

class candles_types():
	def __init__ (self,opens,high,low,close):
		self.open = opens[-20:]
		self.high = high[-20:]
		self.low = low[-20:]
		self.close = close[-20:]

	def all_candles(self):
		bullish = [] #uptrending market
		bearish = [] #down trending markets
		fill = 0
		candles =[

		{'candle':'two_crows','count' :(talib.CDL2CROWS(self.open,self.high,self.low,self.close)), 'percent': -54},
		{'candle':'three_blk_crows','count' : (talib.CDL3BLACKCROWS(self.open,self.high,self.low,self.close)), 'percent': -78},
		{'candle':'three_inside_up','count' :( talib.CDL3INSIDE(self.open,self.high,self.low,self.close)), 'percent': 65},
		#fpound both bullish: 84 bearish: 65
		{'candle':'three_line_strike','count'  : (talib.CDL3LINESTRIKE(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'three_outside_up','count'  : (talib.CDL3OUTSIDE(self.open,self.high,self.low,self.close)), 'percent': 75},
		{'candle':'three_starts_in_the_south','count'  : (talib.CDL3STARSINSOUTH(self.open,self.high,self.low,self.close)), 'percent': 86},
		{'candle':'three_white_soldiers','count'  : (talib.CDL3WHITESOLDIERS(self.open,self.high,self.low,self.close)),'percent': 82},
		#found in both bearish = 69 bullish = 70
		{'candle':'abandoned_baby','count'  : (talib.CDLABANDONEDBABY(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'advanced_block','count'  : (talib.CDLADVANCEBLOCK(self.open,self.high,self.low,self.close)), 'percent': 64},
		#found in both bearish = 68 bullish = 71
		{'candle':'belt_hold','count'  : (talib.CDLBELTHOLD(self.open,self.high,self.low,self.close)), 'percent': fill},
		#found in both bearish = 63 bullish = 59
		{'candle':'breakaway','count'  : (talib.CDLBREAKAWAY(self.open,self.high,self.low,self.close)), 'percent': fill},
		#too close to tell, RIP
		{'candle':'closing_marubozu','count'  : (talib.CDLCLOSINGMARUBOZU(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'concealing_baby_swallow','count'  : (talib.CDLCONCEALBABYSWALL(self.open,self.high,self.low,self.close)), 'percent': -75},
		#can't find number
		{'candle':'counterattack','count'  : (talib.CDLCOUNTERATTACK(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'dark_cloud_cover','count'  : (talib.CDLDARKCLOUDCOVER(self.open,self.high,self.low,self.close,penetration=0)), 'percent': -60},
		#too many to be sure
		{'candle':'doji','count'  : (talib.CDLDOJI(self.open,self.high,self.low,self.close)), 'percent': fill},
		#too many to be sure
		{'candle':'doji_star','count'  : (talib.CDLDOJISTAR(self.open,self.high,self.low,self.close)), 'percent': fill},
		#indecision
		{'candle':'dragonfly_doji','count'  : (talib.CDLDRAGONFLYDOJI(self.open,self.high,self.low,self.close)), 'percent': fill},
		#found in both bearish = 79 bullish = 63
		{'candle':'engulfing_pattern','count'  : (talib.CDLENGULFING(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'evening_doji_star','count'  : (talib.CDLEVENINGDOJISTAR(self.open,self.high,self.low,self.close,penetration=0)), 'percent': -71},
		{'candle':'evening_star','count'  : (talib.CDLEVENINGSTAR(self.open,self.high,self.low,self.close,penetration=0)),'trend' : 'bear', 'percent': -72},
		#cannot find
		{'candle':'gap_side_by_side','count'  : (talib.CDLGAPSIDESIDEWHITE(self.open,self.high,self.low,self.close)), 'percent': fill},
		#indecision
		{'candle':'gravestone_doji','count'  : (talib.CDLGRAVESTONEDOJI(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'hammer','count'  : (talib.CDLHAMMER(self.open,self.high,self.low,self.close)),'percent': 60},
		{'candle':'hangning_man','count'  : (talib.CDLHANGINGMAN(self.open,self.high,self.low,self.close)), 'percent': 59},
		{'candle':'harami_pattern','count'  : (talib.CDLHARAMI(self.open,self.high,self.low,self.close)), 'percent': 53},
		#found in both bearish = 55 bullish = 57
		{'candle':'harami_cross_pattern','count'  : (talib.CDLHIGHWAVE(self.open,self.high,self.low,self.close)), 'percent': fill},
		#indecision
		{'candle':'high_wave_candle','count'  : (talib.CDLHIGHWAVE(self.open,self.high,self.low,self.close)),'percent': fill},
		#cannot find, i guess
		{'candle':'hikkake_pattern','count'  : (talib.CDLHIKKAKE(self.open,self.high,self.low,self.close)), 'percent': fill},
		#cannot find, i guess
		{'candle':'modified_hikkake_pattern','count'  : (talib.CDLHIKKAKEMOD(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'homing_pigeon','count'  : (talib.CDLHOMINGPIGEON(self.open,self.high,self.low,self.close)), 'percent': -56},
		{'candle':'indentical_three_crows','count'  : (talib.CDLIDENTICAL3CROWS(self.open,self.high,self.low,self.close)), 'percent': -79},
		{'candle':'in_neck_pattern','count'  : (talib.CDLINNECK(self.open,self.high,self.low,self.close)), 'percent': -53},
		{'candle':'inverted_hammer','count'  : (talib.CDLINVERTEDHAMMER(self.open,self.high,self.low,self.close)), 'percent': -65},
		#found in both bearish = 54 bullish = 53
		{'candle':'kicking','count'  : (talib.CDLKICKING(self.open,self.high,self.low,self.close)), 'percent': fill},
		#cannot find, i guess
		{'candle':'kicking_by_longer','count'  : (talib.CDLKICKINGBYLENGTH(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'ladder_bottom','count'  : (talib.CDLLADDERBOTTOM(self.open,self.high,self.low,self.close)), 'percent': 56},
		{'candle':'long_legged_doji','count'  : (talib.CDLLONGLEGGEDDOJI(self.open,self.high,self.low,self.close)),'percent': 51},
		#cannot find, i guess
		{'candle':'long_line_candle','count'  : (talib.CDLLONGLINE(self.open,self.high,self.low,self.close)), 'percent': fill},
		#too many to be sure
		{'candle':'marubozu','count'  : (talib.CDLMARUBOZU(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'matching_low','count'  : (talib.CDLMATCHINGLOW(self.open,self.high,self.low,self.close)), 'percent': -61},
		{'candle':'mat_hold','count'  : (talib.CDLMATHOLD(self.open,self.high,self.low,self.close,penetration=0)), 'percent': 78},
		{'candle':'morning_doji_star','count'  : (talib.CDLMORNINGDOJISTAR(self.open,self.high,self.low,self.close,penetration=0)), 'percent': fill},
		{'candle':'morning_star','count'  : (talib.CDLMORNINGSTAR(self.open,self.high,self.low,self.close,penetration=0)), 'percent': 76},
		{'candle':'on_neck_pattern','count'  : (talib.CDLONNECK(self.open,self.high,self.low,self.close)), 'percent': -56},
		{'candle':'piercing_pattern','count'  : (talib.CDLPIERCING(self.open,self.high,self.low,self.close)), 'percent': 64},
		#indecision
		{'candle':'rickshaw_man','count'  : (talib.CDLRICKSHAWMAN(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'rise_fall_three_method','count'  : (talib.CDLRISEFALL3METHODS(self.open,self.high,self.low,self.close)), 'percent': 74},
		#found in both bearish = 63 bullish = 72
		{'candle':'separating_lines','count'  : (talib.CDLSEPARATINGLINES(self.open,self.high,self.low,self.close)), 'percent': fill},
		#too many to be sure
		{'candle':'shooting_star','count'  : (talib.CDLSHOOTINGSTAR(self.open,self.high,self.low,self.close)), 'percent': fill},
		#indecision
		{'candle':'short_line_candle','count'  : (talib.CDLSHORTLINE(self.open,self.high,self.low,self.close)), 'percent': fill},
		#indecision
		{'candle':'spinning_top','count'  : (talib.CDLSPINNINGTOP(self.open,self.high,self.low,self.close)), 'percent': fill},
		#cannot find, i guess
		{'candle':'stalled_pattern','count'  : (talib.CDLSTALLEDPATTERN(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'stick_sandwich','count'  : (talib.CDLSTICKSANDWICH(self.open,self.high,self.low,self.close)), 'percent': -62},
		{'candle':'takuri','count'  : (talib.CDLTAKURI(self.open,self.high,self.low,self.close)), 'percent': 66},
		{'candle':'tasuki_gap','count'  : (talib.CDLTASUKIGAP(self.open,self.high,self.low,self.close)), 'percent': 54},
		{'candle':'thrusting_pattern','count'  : (talib.CDLTHRUSTING(self.open,self.high,self.low,self.close)), 'percent': 57},
		#found in both bearish = 52 bullish = 60
		{'candle':'tristar','count'  : (talib.CDLTRISTAR(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'unique_three_river','count'  : (talib.CDLUNIQUE3RIVER(self.open,self.high,self.low,self.close)), 'percent': -60},
		{'candle':'upside_gap_two_crows','count'  : (talib.CDLUPSIDEGAP2CROWS(self.open,self.high,self.low,self.close)), 'percent': 60},
		#found in both bearish = 59 bullish = 62
		{'candle':'gap_three_methods','count'  : (talib.CDLXSIDEGAP3METHODS(self.open,self.high,self.low,self.close)), 'percent': fill}
		]
		i = 0
		candle_exists = 0;
		for item in candles:
			for i in range(len(item['count'])):
				if item['count'][i] > 0:
					candle_exists+=1
				elif item['count'][i] < 0:
					candle_exists-=1
			i=0
			if(candle_exists>0):
				bullish.append({'name': item['candle'], 'percent': item['percent']})
			if(candle_exists<0):
				bearish.append({'name': item['candle'], 'percent': item['percent']})
			candle_exists = 0
		# bullish_2 = bullish[-1:]
		# bearish_2 = bearish[-1:]

		return bullish,bearish

	



