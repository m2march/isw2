import filter
import json
from strategy import Strategy

class StrategyQuery(object):
	def __str__(self):
		subclasses = Strategy.__subclasses__()
		subclassNameList = [] 

		print subclassNameList

		for aSubclass in subclasses:
			subclassNameList.append(aSubclass.strategy_name())

		return json.dumps(subclassNameList)

class QueryFactory(object):
	def createStrategyQuery(self):
		return StrategyQuery()

	def createQuery(self, aProcessingQuery):
		return Query(aProcessingQuery.product)

class Query(object):
	def __init__(self, product):
		self.product = product

	def __str__(self):
		return "Query [product="+str(self.product)+"]"
