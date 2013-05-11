import cherrypy
from service import RestApi
from validProducts import ValidProductsProvider
from queryProcessing import MultiQueryProcessor, ProductQueryProcessor, StrategyQueryProcessor

#Products
validProductsProvider = ValidProductsProvider()

#Inicializo el procesamiento de querys
productQueryProcessor = ProductQueryProcessor(validProductsProvider)
strategyQueryProcessor = StrategyQueryProcessor()

queryProcessor = MultiQueryProcessor([productQueryProcessor, strategyQueryProcessor])

cherrypy.quickstart(RestApi(queryProcessor, validProductsProvider))
