#-*- coding: utf-8 -*-

import cherrypy

from queryProcessing import ProcessingQuery
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

	def query(self, Product, MinPrice, MaxPrice, Submit, Strategy):
		cherrypy.response.headers["Content-Type"] =  "text/plain"
		processingQuery = ProcessingQuery(producto)
		processingQuery.setRango(rango)
		return "ERROR! Not yet implemented!"

	service.exposed = True
	strategys.exposed = True
	products.exposed = True
	query.exposed = True
