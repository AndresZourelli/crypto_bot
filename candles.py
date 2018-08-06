import time
import talib 

class candles_types():
	def __init__ (self,opens,high,low,close):
		self.open = opens
		self.high = high
		self.low = low
		self.close = close
	

	def all_candles(self):
		bullish = [] #uptrending market
		bearish = [] #down trending markets
		fill = 0
		candles =[

		{'candle':'two_crows','count' :(talib.CDL2CROWS(self.open,self.high,self.low,self.close)), 'percent': 60},
		{'candle':'three_blk_crows','count' : (talib.CDL3BLACKCROWS(self.open,self.high,self.low,self.close)), 'percent': 0},
		{'candle':'three_inside_up','count' :( talib.CDL3INSIDE(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'three_line_strike','count'  : (talib.CDL3LINESTRIKE(self.open,self.high,self.low,self.close)), 'percent': 84},
		{'candle':'three_outside_up','count'  : (talib.CDL3OUTSIDE(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'three_starts_in_the_south','count'  : (talib.CDL3STARSINSOUTH(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'three_white_soldiers','count'  : (talib.CDL3WHITESOLDIERS(self.open,self.high,self.low,self.close)),'percent': fill},
		{'candle':'abandoned_baby','count'  : (talib.CDLABANDONEDBABY(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'advanced_block','count'  : (talib.CDLADVANCEBLOCK(self.open,self.high,self.low,self.close)), 'percent': 64},
		{'candle':'belt_hold','count'  : (talib.CDLBELTHOLD(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'breakaway','count'  : (talib.CDLBREAKAWAY(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'closing_marubozu','count'  : (talib.CDLCLOSINGMARUBOZU(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'concealing_baby_swallow','count'  : (talib.CDLCONCEALBABYSWALL(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'counterattack','count'  : (talib.CDLCOUNTERATTACK(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'dark_cloud_cover','count'  : (talib.CDLDARKCLOUDCOVER(self.open,self.high,self.low,self.close,penetration=0)), 'percent': fill},
		{'candle':'doji','count'  : (talib.CDLDOJI(self.open,self.high,self.low,self.close)), 'percent': 69},
		{'candle':'doji_star','count'  : (talib.CDLDOJISTAR(self.open,self.high,self.low,self.close)), 'percent': 69},
		{'candle':'dragonfly_doji','count'  : (talib.CDLDRAGONFLYDOJI(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'engulfing_pattern','count'  : (talib.CDLENGULFING(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'evening_doji_star','count'  : (talib.CDLEVENINGDOJISTAR(self.open,self.high,self.low,self.close,penetration=0)), 'percent': fill},
		{'candle':'evening_star','count'  : (talib.CDLEVENINGSTAR(self.open,self.high,self.low,self.close,penetration=0)),'trend' : 'bear', 'percent': fill},
		{'candle':'gap_side_by_side','count'  : (talib.CDLGAPSIDESIDEWHITE(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'gravestone_doji','count'  : (talib.CDLGRAVESTONEDOJI(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'hammer','count'  : (talib.CDLHAMMER(self.open,self.high,self.low,self.close)),'percent': fill},
		{'candle':'hangning_man','count'  : (talib.CDLHANGINGMAN(self.open,self.high,self.low,self.close)), 'percent': 59},
		{'candle':'harami_pattern','count'  : (talib.CDLHARAMI(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'harami_cross_pattern','count'  : (talib.CDLHIGHWAVE(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'high_wave_candle','count'  : (talib.CDLHIGHWAVE(self.open,self.high,self.low,self.close)),'percent': fill},
		{'candle':'hikkake_pattern','count'  : (talib.CDLHIKKAKE(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'modified_hikkake_pattern','count'  : (talib.CDLHIKKAKEMOD(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'homing_pigeon','count'  : (talib.CDLHOMINGPIGEON(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'indentical_three_crows','count'  : (talib.CDLIDENTICAL3CROWS(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'in_neck_pattern','count'  : (talib.CDLINNECK(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'inverted_hammer','count'  : (talib.CDLINVERTEDHAMMER(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'kicking','count'  : (talib.CDLKICKING(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'kicking_by_longer','count'  : (talib.CDLKICKINGBYLENGTH(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'ladder_bottom','count'  : (talib.CDLLADDERBOTTOM(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'long_legged_doji','count'  : (talib.CDLLONGLEGGEDDOJI(self.open,self.high,self.low,self.close)),'percent': fill},
		{'candle':'long_line_candle','count'  : (talib.CDLLONGLINE(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'marubozu','count'  : (talib.CDLMARUBOZU(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'matching_low','count'  : (talib.CDLMATCHINGLOW(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'mat_hold','count'  : (talib.CDLMATHOLD(self.open,self.high,self.low,self.close,penetration=0)), 'percent': fill},
		{'candle':'morning_doji_star','count'  : (talib.CDLMORNINGDOJISTAR(self.open,self.high,self.low,self.close,penetration=0)), 'percent': fill},
		{'candle':'morning_star','count'  : (talib.CDLMORNINGSTAR(self.open,self.high,self.low,self.close,penetration=0)), 'percent': fill},
		{'candle':'on_neck_pattern','count'  : (talib.CDLONNECK(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'piercing_pattern','count'  : (talib.CDLPIERCING(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'rickshaw_man','count'  : (talib.CDLRICKSHAWMAN(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'rise_fall_three_method','count'  : (talib.CDLRISEFALL3METHODS(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'separating_lines','count'  : (talib.CDLSEPARATINGLINES(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'shooting_star','count'  : (talib.CDLSHOOTINGSTAR(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'short_line_candle','count'  : (talib.CDLSHORTLINE(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'spinning_top','count'  : (talib.CDLSPINNINGTOP(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'stalled_pattern','count'  : (talib.CDLSTALLEDPATTERN(self.open,self.high,self.low,self.close)), 'percent': 77},
		{'candle':'stick_sandwich','count'  : (talib.CDLSTICKSANDWICH(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'takuri','count'  : (talib.CDLTAKURI(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'tasuki_gap','count'  : (talib.CDLTASUKIGAP(self.open,self.high,self.low,self.close)), 'percent': 54},
		{'candle':'thrusting_pattern','count'  : (talib.CDLTHRUSTING(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'tristar','count'  : (talib.CDLTRISTAR(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'unique_three_river','count'  : (talib.CDLUNIQUE3RIVER(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'upside_gap_two_crows','count'  : (talib.CDLUPSIDEGAP2CROWS(self.open,self.high,self.low,self.close)), 'percent': fill},
		{'candle':'gap_three_methods','count'  : (talib.CDLXSIDEGAP3METHODS(self.open,self.high,self.low,self.close)), 'percent': fill}
		]
		i = 0

		for item in candles:
			if item['count'][-1:] > 0:
				bullish.append(item['candle'])

			if item['count'][-1] < 0:
				bearish.append(item['candle'])
		bullish_2 = bullish[-1:]
		bearish_2 = bearish[-1:]

		return bullish_2,bearish_2



		#if count > 0;
		#	bullish
		#if count < 0:
		#	bearish


