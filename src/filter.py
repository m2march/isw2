class Filter(object):
	def __init__(self):
		raise NotImplementedError("")

	def __str__(self):
		raise NotImplementedError("")

	def filter(self, aOffer):
		raise NotImplementedError("")

class ProductFilter(Filter):
	def __init__(self, aProduct):
		self._product = aProduct
	
	def __str__(self):
		return "ProductFilter [product="+str(self._product)+"]"
	
	def filter(self, aOffer):
		return aOffer.product() == self._product

class PriceRangeFilter(Filter):
	def __init__(self, rangeMin, rangeMax):
		self._rangeMin = rangeMin
		self._rangeMax = rangeMax
	
	def __str__(self):
		return "PriceRangeFilter [rangeMin="+str(self._rangeMin)+", "+str(self._rangeMax)+"]"
	
	def filter(self, aOffer):
		offerPrice = aOffer.price()
		return self._rangeMin <= offerPrice and offerPrice <= self._rangeMax

class AndFilter(Filter):
	def __init__(self):
		self._filters = []
	
	def __str__(self):
		toString = "AndFilter ["
		for aFilter in self.filters:
			toString = toString + str(aFilter) + " " 
		toString = toString + "]"
		return toString
	
	def filter(self, aOffer):
		for aFilter in self._filters:
			if not aFilter._filter(aOffer):
				return False
		return True

	def addFilter(self, aFilter):
		self._filters.append(aFilter)
		return self
