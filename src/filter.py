from validProducts import ValidProductsProvider
from offer import Offer
from location import Location

class Filter(object):
	def __init__(self):
		raise NotImplementedError("")

	def __str__(self):
		raise NotImplementedError("")

	def filter(self, aOffer):
		raise NotImplementedError("")

class SimpleFilter(Filter):
	pass

class ProductFilter(SimpleFilter):
	def __init__(self, aProduct):
		self._product = aProduct
	
	def __str__(self):
		return "ProductFilter [product="+str(self._product)+"]"
	
	def filter(self, aOffer):
		return aOffer.product() == self._product

class PriceRangeFilter(SimpleFilter):
	def __init__(self, rangeMin, rangeMax):
		self._rangeMin = rangeMin
		self._rangeMax = rangeMax
	
	def __str__(self):
		return "PriceRangeFilter [rangeMin="+str(self._rangeMin)+", rangeMax="+str(self._rangeMax)+"]"
	
	def filter(self, aOffer):
		offerPrice = aOffer.price()
		return self._rangeMin <= offerPrice and offerPrice <= self._rangeMax

class MultiFilter(Filter):
	def __init__(self):
		self._filters = []
	
	def baseCase(self):
		raise NotImplementedError("")	
	
	def reduceOp(self, anAccumulator, aFilterResult):
		raise NotImplementedError("")	
	
	def filter(self, aOffer):
		result = self.baseCase()
		
		for aFilter in self._filters:
			result = self.reduceOp(result, aFilter.filter(aOffer))
		
		return result

	def addFilter(self, aFilter):
		self._filters.append(aFilter)
		return self

class AndFilter(MultiFilter):
	
	def baseCase(self):
		return True
	
	def reduceOp(self, anAccumulator, aFilterResult):
		return anAccumulator and aFilterResult
	
	def __str__(self):
		toString = "AndFilter ["
		for aFilter in self._filters:
			toString += str(aFilter) + " " 
		toString += "]"
		return toString


if __name__ == '__main__':
	#test de los filtros

	print "Testing filters"
	aValidProductsProvider = ValidProductsProvider()
	
	aProduct = aValidProductsProvider.products()[0] 
	otherProduct = aValidProductsProvider.products()[1]
	
	aLocation = Location("a road 500")
	
	Offers = [Offer(aProduct, 3, aLocation), Offer(aProduct, 4, aLocation), Offer(otherProduct, 4, aLocation)] 
	
	aProductFilter = ProductFilter(aProduct)
	aPriceRangeFilter = PriceRangeFilter(3.5, 4.5)
	anAndFilter = AndFilter().addFilter(aProductFilter).addFilter(aPriceRangeFilter)
	
	print "ProductFilter Test"
	assert(aProductFilter.filter(Offers[0]) and aProductFilter.filter(Offers[1]) and not aProductFilter.filter(Offers[2]))
	print "Pass"

	print "PriceRangeFilter Test"
	assert(not aPriceRangeFilter.filter(Offers[0]) and aPriceRangeFilter.filter(Offers[1]) and aPriceRangeFilter.filter(Offers[2]))
	print "Pass"

	print "AndFilter Test"
	assert(not anAndFilter.filter(Offers[0]) and anAndFilter.filter(Offers[1]) and not anAndFilter.filter(Offers[2]))
	print "Pass"
