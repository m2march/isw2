import filter
import json
from strategy import Strategy

class Query(object):
	pass

class OfferQuery(Query):
	def __init__(self, aProduct):
		pass

class QueryFactory(object):
	def createOfferQuery(self, aProcessingQuery):
		return OfferQuery(aProcessingQuery.product)
