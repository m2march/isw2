import cherrypy
from service import RestApi
from validProducts import ValidProductsProvider
from queryProcessing import MultiQueryProcessor, ProductQueryProcessor

#Products
validProductsProvider = ValidProductsProvider()

#Inicializo el procesamiento de querys
productQueryProcessor = ProductQueryProcessor(validProductsProvider)
queryProcessor = MultiQueryProcessor([productQueryProcessor])

cherrypy.quickstart(RestApi(queryProcessor, validProductsProvider))
