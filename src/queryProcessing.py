class ProcessingQuery:
	def initialize(self, product):
		self.sProduct = product

	def setRango(self, rango):
		self.sRango = rango

class QueryProcessor:
	def processQuery(aProcessingQuery):
		except NotImplementedError()

class ProductQueryProcessor(QueryProcessor):
	def __init__(self, aValidProductsProvider):
		self.validProductsProvider = aValidProductHolder

	def processQuery(aProcessingQuery):
		productList = self.validProductsProvider.products()
		for p in productList:
			if (p.name == aProcessingQuery.product):
				self.product = p
		return aProcessingQuery

class MultiQueryProcessor(QueryProcessor):
	def __init__(self, aQueryProcessorList):
		self.queryProcessorList = aQueryProcessorList

	def processQuery(aProcessingQuery):
		for p in self.queryProcessorList:
			p.processQuery(aProcessingQuery)	
		return p
		
		
