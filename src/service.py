#-*- coding: utf-8 -*-

import cherrypy
import json

from queryProcessing import OfferQueryInConstruction 
from query import QueryFactory

class RestApi:
	print "RestApi startup"
	def __init__(self, aQueryProcessor, aValidProductsProvider):
		self.queryProcessor = aQueryProcessor
		self.validProductsProvider = aValidProductsProvider
		self.aQueryFactory = QueryFactory()

	def service(self):
		return "PrecioJusto v0.0.0.0.0.0.0.0.0.0.0.5"

	def strategys(self):
		cherrypy.response.headers["Content-Type"] =  "text/plain"
		response = self.queryProcessor.processStrategysQuery()
		return response 

	def products(self):
		cherrypy.response.headers["Content-Type"] =  "text/plain"
		response = self.queryProcessor.processProductsQuert(self.validProductsProvider)
		return response 

	def offerquery(self, Product="", MinPrice="", MaxPrice="", Strategy=""):
		cherrypy.response.headers["Content-Type"] =  "text/plain"

		try:
			offerQuery = OfferQueryInConstruction(Product, MinPrice, MaxPrice, Strategy)
			processedOfferQuery = self.queryProcessor.processOfferQuery(offerQuery)

			queryResult = ["a", "b", "c"]

			return json.dumps({"result": queryResult}) 
		except Exception as e:
			return json.dumps({"error":True, "reason":str(e)})

	service.exposed = True
	strategys.exposed = True
	products.exposed = True
	offerquery.exposed = True
