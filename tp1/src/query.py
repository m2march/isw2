import filter
import json
from strategy import Strategy

class Query(object):
	pass

class OfferQuery(Query):
	def __init__(self, aFilter, aStrategy):
		self._filter = aFilter 
		self._strategy = aStrategy
	
	def filter(self):
		return self._filter
	
	def strategy(self):
		return self._strategy
