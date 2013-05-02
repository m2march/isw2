#-*- coding: utf-8 -*-

import cherrypy
from queryProcessing import ProcessingQuery
from query import QueryFactory

class RestApi:
    print "RestApi startup"
    def __init__(self, aQueryProcessor):
        self.queryProcessor = aQueryProcessor

    def service(self):
        return "PrecioJusto v0.0.0.0.0.0.0.0.0.0.0.5"

    def query(self, producto, rango=None):
        cherrypy.response.headers["Content-Type"] =  "text/plain"
        processingQuery = ProcessingQuery(producto)
        processingQuery.setRango(rango)

        self.queryProcessor.processQuery(processingQuery)
        query = QueryFactory().createQuery(processingQuery)
        return str(query)


    service.exposed = True
    query.exposed = True	
