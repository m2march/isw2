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
	
	def reduceOp(anAccumulator, aFilterResult):
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
	
	def reduceOp(anAccumulator, aFilterResult):
		return anAccumulator and aFilterResult
	
	def __str__(self):
		toString = "AndFilter ["
		for aFilter in self._filters:
			toString += str(aFilter) + " " 
		toString += "]"
		return toString
