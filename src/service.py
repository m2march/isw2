#-*- coding: utf-8 -*-

import cherrypy
import json

from defaultModelManager import *
from query import *
from queryProcessing import OfferQueryInConstruction
from offer import offer_as_dict

class RestApi:
  print "RestApi startup"
  def __init__(self, aQueryProcessor, aValidProductsProvider, aModelManager):
    self.modelManager = aModelManager
    self.queryProcessor = aQueryProcessor
    self.validProductsProvider = aValidProductsProvider

  def service(self):
    return "PrecioJusto v0.0.0.0.0.0.0.0.0.0.0.5"

  def strategies(self):
    cherrypy.response.headers["Content-Type"] =  "text/plain"
    response = self.queryProcessor.processStrategysQuery()
    return response

  def products(self):
    cherrypy.response.headers["Content-Type"] =  "text/plain"
    response = self.queryProcessor.processProductsQuery(self.validProductsProvider)
    return response

  def offerquery(self, Product="", MinPrice="", MaxPrice="", Strategy=""):
    cherrypy.response.headers["Content-Type"] =  "text/plain"

    try:
      offerQuery = OfferQueryInConstruction(Product, MinPrice, MaxPrice, Strategy)
      processedOfferQuery = self.queryProcessor.processOfferQuery(offerQuery)
      inmmutableOfferQuery = processedOfferQuery.makeInmmutable()
      queryResult = self.modelManager.process(inmmutableOfferQuery)
      dictQueryResult = map(lambda e: offer_as_dict(e), queryResult)
      return json.dumps({"result": dictQueryResult})
    except Exception as e:
      return json.dumps({"error":True, "reason":str(e)})

  service.exposed = True
  strategies.exposed = True
  products.exposed = True
  offerquery.exposed = True
