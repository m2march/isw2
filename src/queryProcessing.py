import json
from strategy import Strategy
from filter import ProductFilter, PriceRangeFilter, AndFilter
from query import OfferQuery

class OfferQueryInConstruction(object):
	"""Passed among QueryProcessors to process each part of the query.
	sVariables are strings
	proper variables should be set by the processor."""
	
	def __init__(self, Product, MinPrice, MaxPrice, Strategy):
		self.filters = []
		self.sProduct = Product
		self.sRange = (MinPrice, MaxPrice)
		self.sStrategy = Strategy
	
	def makeInmmutable(self):
		andfilter = AndFilter()
		
		for aFilter in self.filters:
			andfilter.addFilter(aFilter)
		
		return OfferQuery(andfilter, self.strategy)

class QueryProcessor(object):
	"""Abstract class for query processing. processQuery modifies
	the given processingQuery adding proper variables made
	from the sVariables. """
	
	def processOfferQuery(self, aQueryInConstruction):
		raise NotImplementedError()

class ProductQueryProcessor(QueryProcessor):
	def __init__(self, aValidProductsProvider):
		self.validProductsProvider = aValidProductsProvider
	
	def processOfferQuery(self, aQueryInConstruction):
		productList = self.validProductsProvider.products()
		try:
			aProduct = next(p for p in productList if p.name() == aQueryInConstruction.sProduct)
			aQueryInConstruction.filters.append(ProductFilter(aProduct))
		except Exception as anException:
			raise IllegalProduct(aQueryInConstruction.sProduct)
		return aQueryInConstruction

class RangeQueryProcessor(QueryProcessor):
	def processOfferQuery(self, aQueryInConstruction):
		(sMin, sMax) = aQueryInConstruction.sRange
		if len(sMin) != 0 or len(sMax) != 0:
			try:
				Min = float(sMin)
				Max = float(sMax)
				if not Min < Max :
					raise IllegalRange(aQueryInConstruction.sRange)
				aQueryInConstruction.filters.append(PriceRangeFilter(Min, Max))
			except Exception:
				raise IllegalRange(aQueryInConstruction.sRange)
		return aQueryInConstruction

class StrategyQueryProcessor(QueryProcessor):
	def processOfferQuery(self, aQueryInConstruction):
		sStrategy = aQueryInConstruction.sStrategy
		try:
			aStrategy = next(sc for sc in Strategy.__subclasses__() if sc.strategyName() == aQueryInConstruction.sStrategy)
			aQueryInConstruction.strategy = aStrategy()
		except Exception:
			raise IllegalStrategy(aQueryInConstruction.sStrategy)
		return aQueryInConstruction

class MultiQueryProcessor(QueryProcessor):
	def __init__(self, aQueryProcessorList):
		self.queryProcessorList = aQueryProcessorList
	
	def processOfferQuery(self, aQueryInConstruction):
		for p in self.queryProcessorList:
			p.processOfferQuery(aQueryInConstruction)
		return aQueryInConstruction

## Processing errors
class ProcessingError(Exception):
	"""Processing error"""

class IllegalProduct(ProcessingError):
	def __init__(self, sProduct):
		self.sProduct = sProduct
	
	def __str__(self):
		return self.sProduct + " is not a valid product"

class IllegalRange(ProcessingError):
	def __init__(self, sRange):
		self.sRange = sRange
	
	def __str__(self):
		return str(self.sRange) + " is not a valid range"

class IllegalStrategy(ProcessingError):
	def __init__(self, sStrategy):
		self.sStrategy = sStrategy
	
	def __str__(self):
		return self.sStrategy + " is not a valid strategy"
