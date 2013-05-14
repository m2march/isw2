import cherrypy
from service import RestApi
from validProducts import ValidProductsProvider
from queryProcessing import MultiQueryProcessor, ProductQueryProcessor, StrategyQueryProcessor, RangeQueryProcessor
from modelManager import *
from parser import *
from twitterSimpleConnector import *
from dataManager import *
from offerFactory import *

#Products
validProductsProvider = ValidProductsProvider()

#Inicializo el procesamiento de querys
productQueryProcessor = ProductQueryProcessor(validProductsProvider)
strategyQueryProcessor = StrategyQueryProcessor()
rangeQueryProcessor = RangeQueryProcessor()
queryProcessor = MultiQueryProcessor([productQueryProcessor, rangeQueryProcessor, strategyQueryProcessor])

#inicializo el data Manager
connectorEs = TwitterSimpleConnector("#precioJusto","es")
dataManager = DataManager(connectorEs)

#inicializo la cadena de parseo
parserChain = ParserChain([ProductParser(), PriceParser(), LocationParser()])

#inicializo la offer factory
offerFactory = OfferFactory(parserChain)

#inicializo el model manager
modelManager = ModelManager(dataManager,offerFactory)

cherrypy.quickstart(RestApi(queryProcessor, validProductsProvider, modelManager))
