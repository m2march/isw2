from offer import *

class Strategy(object):
	@staticmethod
	def strategyName():
		raise NotImplementedError("")
	
	def __init__(self):
		raise NotImplementedError("")
	
	def	__str__(self): 
		raise NotImplementedError("")
	
	def prioritize(self, anOfferList):
		raise NotImplementedError("")

class NullStrategy(Strategy):
	@staticmethod
	def strategyName():
		return "None"
	
	def __init__(self):
		pass
	
	def	__str__(self): 
		return "NullStrategy"
	
	def prioritize(self, anOfferList):
		return anOfferList

class WalkingAsLittleStrategy(Strategy):
	@staticmethod
	def strategyName():
		return "Nearest"
	
	def __init__(self, aLocation):
		raise NotImplementedError("")
	
	def	__str__(self): 
		return "WalkingAsLittleStrategy"
	
	def prioritize(self, anOfferList):
		raise NotImplementedError("")

class CheapestStrategy(Strategy):
	@staticmethod
	def strategyName():
		return "Cheapest"
	
	def __init__(self):
		pass
	
	def	__str__(self): 
		return "CheapestStrategy"
	
	def prioritize(self, anOfferList):
		return sorted(anOfferList, key=Offer.price)
