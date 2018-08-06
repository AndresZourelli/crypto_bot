class Currency:
	reversal = 0 
	continuation = 0 
	indecision = 0

	def __init__ (self, _bearish, _bullish):
		self.bearish = _bearish
		self.bullish = _bullish

	def reversalMutator(self):
		reversal = 0
		if 'three_line_strike' in self.bullish or 'three_line_strike' in self.bearish:
			reversal += 84
		if 'abandoned_baby' in self.bearish:
			reversal -= 69
		if 'two_crows' in self.bearish:
			reversal -= 54
		if 'three_blk_crows' in self.bearish:
			reversal -= 78
		if 'three_inside_up' in self.bullish:
			reversal += 65
		if 'three_outside_up' in self.bullish:
			reversal += 75
		if 'three_starts_in_the_south' in self.bullish:
			reversal += 86
		if 'three_white_soldiers' in self.bullish:
			reversal += 82
		if 'belt_hold' in self.bearish:
			reversal -= 68
		if 'belt_hold' in self.bullish:
			reversal += 71
		if 'breakaway' in self.bearish:
			reversal -= 63
		if 'breakaway' in self.bullish:
			reversal += 69
		if 'dark_cloud_cover' in self.bearish:
			reversal -= 60
		if 'dragonfly_doji' in self.bullish:
			reversal += 50
		if 'engulfing_pattern' in self.bearish:
			reversal -= 79
		if 'engulfing_pattern' in self.bullish:
			reversal += 63
		if 'evening_doji_star' in self.bearish:
			reversal -= 71
		if 'evening_star' in self.bearish:
			reversal -=72
		if 'gravestone_doji' in self.bearish:
			reversal -= 51
		if 'hammer' in self.bullish:
			reversal += 60
		if 'harami_pattern' in self.bullish:
			reversal += 53
		if 'indentical_three_crows' in self.bearish:
			reversal -= 79
		if 'kicking' in self.bearish:
			reversal -= 54
		if 'kicking' in self.bullish:
			reversal += 53
		if 'ladder_bottom' in self.bullish:
			reversal += 56
		if 'morning_doji_star' in self.bullish:
			reversal += 76
		if 'morning_star' in self.bullish:
			reversal += 78
		if 'piercing_pattern' in self.bullish:
			reversal += 64
		if 'takuri' in self.bullish:
			reversal += 66
		if 'tasuki_gap' in self.bearish:
			reversal += 54
		if 'thrusting_pattern' in self.bearish:
			reversal += 57
		if 'tristar' in self.bearish:
			reversal -= 52
		if 'tristar' in self.bullish:
			reversal += 60
		if 'gap_three_methods' in self.bullish:
			reversal -= 59
		if 'gap_three_methods' in self.bearish:
			reversal += 62
		return reversal







	def continuationMutator(self):
		continuation = 0
		if 'advanced_block' in self.bearish:
			continuation += 64
		if 'closing_marubozu' in self.bearish:
			continuation -= 52
		if 'closing_marubozu' in self.bullish:
			continuation += 55
		if 'concealing_baby_swallow' in self.bullish:
			continuation -= 75
		if 'doji_star' in self.bullish or 'doji_star' in self.bearish:
			continuation -= 64
		if 'hangning_man' in self.bearish:
			continuation += 59
		if 'harami_pattern' in self.bearish:
			continuation += 53
		if 'harami_cross_pattern' in self.bearish:
			continuation += 57
		if 'homing_pigeon' in self.bullish:
			continuation -= 56
		if 'in_neck_pattern' in self.bearish:
			continuation -= 53
		if 'inverted_hammer' in self.bullish:
			continuation -= 65
		if 'matching_low' in self.bullish:
			continuation -= 61
		if 'mat_hold' in self.bullish:
			continuation += 78
		if 'on_neck_pattern' in self.bearish:
			continuation -= 56
		if 'rise_fall_three_method' in self.bullish:
			continuation += 74
		if 'rise_fall_three_method' in self.bearish:
			continuation -= 71
		if 'separating_lines' in self.bearish:
			continuation -= 63
		if 'separating_lines' in self.bullish:
			continuation += 72
		if 'stick_sandwich' in self.bullish:
			continuation -= 62
		if 'tasuki_gap' in self.bullish:
			continuation += 57
		if 'unique_three_river' in self.bullish:
			continuation -= 60
		if 'upside_gap_two_crows' in self.bearish:
			continuation += 60
		return continuation

	def indecisionMutator(self):
		pass


		#if etc

	def reversalAccessor():
		return reversal

	def continuationAccessor():
		return continuation

	def indecisionAccessor():
		return indecision

