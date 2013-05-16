from unit import Unit
from offer import *
from validProducts import ValidProductsProvider
from location import Location

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

if __name__ == '__main__':
	#test de los filtros
	
	print "Testing filters"
	aValidProductsProvider = ValidProductsProvider()
	
	aProduct = aValidProductsProvider.products()[0] 
	otherProduct = aValidProductsProvider.products()[1]
	
	aLocation = Location("a road 500")
	
	Offers = [Offer(aProduct, 4, aLocation), Offer(aProduct, 3, aLocation),  Offer(otherProduct, 5, aLocation)] 
	
	aNullStrategy = NullStrategy()
	aCheapestStrategy = CheapestStrategy()

	print "NullStrategy Test"
	assert(aNullStrategy.prioritize(Offers) == Offers)
	print "Pass"
	
	print "CheapestStrategy"
	cheapestOffers = aCheapestStrategy.prioritize(Offers)
	for i in range(0, len(cheapestOffers) - 1):
		assert(cheapestOffers[i].price() < cheapestOffers[i+1].price())
	print "Pass"
