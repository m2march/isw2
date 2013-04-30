#-*- coding: utf-8 -*-

import cherrypy

class RestApi:
	def query(self, producto, rango=None):
		cherrypy.response.headers["Content-Type"] =  "text/plain"
		result = ["Se consulto el producto: " + producto]
		if (rango!=None):
			result.append("Con el rango: " + rango)

		return "\n".join(result)

	query.exposed = True	

cherrypy.quickstart(RestApi())
