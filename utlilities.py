

class trading_utilities():

	def __init__(self, line1 = None, line2 = None):
		self.line1 = line1
		self.line2 = line2

	def crossover(self,line1,line2):
		print("\033[0;0m", line1[-2], "  ", line1[-1])
		print("\033[0;0m", line2[-2], "  ", line2[-1])
		if line1[-2] < line2[-2] and line1[-1] > line2[-1]:
			return 1

		else:
			return 0

	def crossunder(self,line1,line2):
		if line1[-2] > line2[-2] and line1[-1] < line2[-1]:
			return 1
		else:
			return 0

	def negative(self, line):
		print("\033[0;0m", line[-2], "  ", line[-1])
		if line[-2] > line[-1]:
			return 1
		else:
			return 0