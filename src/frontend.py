import cherrypy

import httplib
import json

class UnreachableRestResource(Exception):
	def __init__(self, aReason):
		self.reason = "UnreachableRestResource: " + aReason

	def __str__(self):
		return self.reason

class RestBackend(object):
	def __init__(self, aBackendURL, aBackendPort):
		self.url = aBackendURL
		self.port = aBackendPort

	def ask_for(self, resource):
		conn = httplib.HTTPConnection(self.url, self.port)
		conn.request("GET", resource)

		response = conn.getresponse()

		if response.status != 200:
			errorString = str(aBackendURL) + ":" + str(aBackendPort) + " " + resource  + "\n\tresponse_status = " + str(response.status) + "\n"
			raise UnreachableRestResource(errorString)

		data = json.loads(response.read())

		return data

class OfferRestBackend(object):
	def __init__(self, aBackendURL, aBackendPort):
		self.backend = RestBackend(aBackendURL, aBackendPort)

	@staticmethod
	def map_to_utf8(anUnicodeList):
		return map(lambda elem: elem.encode("utf-8"), anUnicodeList)

	def products(self):
		return OfferRestBackend.map_to_utf8(self.backend.ask_for("/products"))

	def strategys(self):
		return OfferRestBackend.map_to_utf8(self.backend.ask_for("/strategys"))

	def offerQuery(self):
		pass


class Frontend(object):
	print "Frontend startup"
	def __init__(self, aBackendURL, aBackendPort):
		self.backend = OfferRestBackend(aBackendURL, aBackendPort)

	def index(self):
		response = ""

		try:
			response = self.indexString()
		except Exception as anyException:
			response = self.errorString(anyException) 
		return response

	def errorString(self, anError):
		return "<html>\n" + self.buildHead() + "\n<body><h1>Ops!</h1>\n" + str(anError) + "</body>\n</head>"
	
	def indexString(self):
		headAndBody = self.buildHead() + self.buildBody()
		return "<html>" + headAndBody + "</html>"

	def buildHead(self):
		return "<head><title>El #Precio Justo</title></head>"

	def buildBody(self):
		productList = self.backend.products()
		strategyList = self.backend.strategys()

		body = """<body>
					<h1 style="text-align: center;">Precio Justo</h1>
					<p style="text-align: center;">Product - Min price - Max price - Strategy</p>
						<form enctype="text/plain" method="get" name="UserQuery">
							<p style="text-align: center;">
								<select name="Product">""" + self.productSelectBox(productList) + """</select>

								<input name="MinPrice" size="6" type="text" />
								<input name="MaxPrice" size="6" type="text" />

								<select name="Strategy">""" + self.strategySelectBox(strategyList) + """</select>

								<input name="Submit" type="submit" value="I'm feeling lucky" />
							</p>
						</form>
					<p style="text-align: center;">Ahorremos Ahora (AA)</p>
				</body>"""
		return body

	@staticmethod
	def buildOption(Name, Value):
		return "<option value=\"" + Value + "\">" + Name + "</option>"

	@staticmethod
	def buildOptionsFromStringList(aStringList):
		options = map(lambda name: Frontend.buildOption(name, name), aStringList)
		return reduce(lambda s1, s2: s1 + s2, options)

	def productSelectBox(self, someProducts):
		return Frontend.buildOptionsFromStringList(someProducts)

	def strategySelectBox(self, someStrategys):
		return Frontend.buildOptionsFromStringList(someStrategys)

	index.exposed = True

if __name__ == '__main__':
	cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 8081})
	cherrypy.quickstart(Frontend("127.0.0.1", 8080))
