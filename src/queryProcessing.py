import json
from strategy import Strategy

class OfferQueryInConstruction(object):
	"""Passed among QueryProcessors to process each part of the query.
	sVariables are strings
	proper variables should be set by the processor."""

	def __init__(self, Product, MinPrice, MaxPrice, Strategy):
		self.sProduct = Product
		self.sRange = (MinPrice, MaxPrice)
		self.sStrategy = Strategy

class QueryProcessor(object):
	"""Abstract class for query processing. processQuery modifies
	the given processingQuery adding proper variables made
	from the sVariables. """

	def processProductsQuert(self, aValidProductsProvider):
		validProducts = aValidProductsProvider.products()
		validProductsName = map(lambda p: p.name(), validProducts)
		return json.dumps(validProductsName, ensure_ascii=False)

	def processStrategysQuery(self):
		subclasses = Strategy.__subclasses__()
		subclassNameList = [] 

		for aSubclass in subclasses:
			subclassNameList.append(aSubclass.strategy_name())

		return json.dumps(subclassNameList, ensure_ascii=False)

	def processOfferQuery(self, aQueryInConstruction):
		raise NotImplementedError()

class ProductQueryProcessor(QueryProcessor):
	def __init__(self, aValidProductsProvider):
		self.validProductsProvider = aValidProductsProvider

	def processOfferQuery(self, aQueryInConstruction):
		productList = self.validProductsProvider.products()
		
		try:
			aProduct = next(p for p in productList if p.name() == aQueryInConstruction.sProduct)
			aQueryInConstruction.product = aProduct
		except Exception as anException:
			raise IllegalProduct(aQueryInConstruction.sProduct)

		return aQueryInConstruction

class RangeQueryProcessor(QueryProcessor):
	def processOfferQuery(self, aQueryInConstruction):
		(sMin, sMax) = aQueryInConstruction.sRange

		raise IllegalRange(aQueryInConstruction.sRange)

		return aQueryInConstruction

class StrategyQueryProcessor(QueryProcessor):
	def processOfferQuery(self, aQueryInConstruction):
		sStrategy = aQueryInConstruction.sStrategy
		try:
			aStrategy = next(sc for sc in Strategy.__subclasses__() if sc.strategy_name() == aQueryInConstruction.sStrategy)
			aQueryInConstruction.Strategy = aStrategy
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
		return self.sRange + " is not a valid range"

class IllegalStrategy(ProcessingError):
	def __init__(self, sStrategy):
		self.sStrategy = sStrategy

	def __str__(self):
		return self.sStrategy + " is not a valid strategy"
