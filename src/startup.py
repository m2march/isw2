import cherrypy
from service import RestApi
from validProducts import ValidProductsProvider
from queryProcessing import MultiQueryProcessor, ProductQueryProcessor, StrategyQueryProcessor, RangeQueryProcessor

#Products
validProductsProvider = ValidProductsProvider()

#Inicializo el procesamiento de querys
productQueryProcessor = ProductQueryProcessor(validProductsProvider)
strategyQueryProcessor = StrategyQueryProcessor()
rangeQueryProcessor = RangeQueryProcessor()

queryProcessor = MultiQueryProcessor([productQueryProcessor, rangeQueryProcessor, strategyQueryProcessor])

cherrypy.quickstart(RestApi(queryProcessor, validProductsProvider))
