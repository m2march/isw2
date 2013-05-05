class Strategy(object):

	@staticmethod
	def strategy_name():
		raise NotImplementedError("")

	def __init__(self):
		raise NotImplementedError("")

	def	__str__(self): 
		raise NotImplementedError("")

	def prioritize(self, anOfferList):
		raise NotImplementedError("")

class WalkingTheLeastStrategy(Strategy):

	@staticmethod
	def strategy_name():
		return "Nearest"

	def __init__(self, aLocation):
		raise NotImplementedError("")

	def	__str__(self): 
		return "WalkingTheLeastStrategy"

	def prioritize(self, anOfferList):
		raise NotImplementedError("")

class CheapestStrategy(Strategy):

	@staticmethod
	def strategy_name():
		return "Cheapest"

	def __init__(self):
		pass

	def	__str__(self): 
		return "CheapestStrategy"

	def prioritize(self, anOfferList):
		return sorted(anOfferList, key=Offer.price)
