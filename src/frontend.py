import cherrypy

import httplib
import json

def build_option(self, Name, Value):
	return "<option value=\"" + Value + "\">" + Name + "</option>"

def rest_call(aBackendURL, aBackendPort, aResource):
	conn = httplib.HTTPConnection(aBackendURL, aBackendPort)
	conn.request("GET", aBackendURL + aResource)

	response = conn.getresponse()

	assert(response.status == 200)
	
	data = response.read()

	asjson = json.load(data)
	return asjson

class Frontend(object):
	print "Frontend startup"
	def __init__(self, aBackendURL, aBackendPort):
		self._backend_url = aBackendURL
		self._backend_port = aBackendPort

	def index(self):
		return self.index_string()

	def index_string(self):
		headAndBody = self.build_head() + self.build_body()
		return "<html>" + headAndBody + "</html>"

	def build_head(self):
		return "<head><title>El #Precio Justo</title></head>"

	def build_body(self):
		productList = self.get_products()
		strategyList = self.get_strategys()

		return """<body>
					<h1 style="text-align: center;">Precio Justo</h1>
					<p style="text-align: center;">Product - Min price - Max price - Strategy</p>
						<form enctype="text/plain" method="get" name="UserQuery">
							<p style="text-align: center;">
								<select name="Product">""" + self.product_select_box(productList) + """</select>

								<input name="MinPrice" size="6" type="text" />
								<input name="MaxPrice" size="6" type="text" />

								<select name="Strategy">""" + self.strategy_select_box(strategyList) + """</select>

								<input name="Submit" type="submit" value="I'm feeling lucky" />
							</p>
						</form>
					<p style="text-align: center;">Ahorremos Ahora (AA)</p>
				</body>"""

	def product_build_option(self, aProduct):
		product_name = aProduct.name()
		return build_option(product_name, product_name)

	def product_select_box(self, someProducts):
		product_option_list = ""
		for aProductName in someProducts:
			product_option_list = product_option_list + build_option(aProductName, aProductName)
		return product_option_list

	def strategy_select_box(self, someStrategys):
		strategy_option_list = ""
		for aStrategyName in someStrategys:
			strategy_option_list = strategy_option_list + build_option(aStrategyName, aStrategyName)

	def get_products(self):
		products = rest_call(self._backend_url, self._backend_port, "/products")
		return products

	def get_strategys(self):
		strategys = rest_call(self._backend_url, self._backend_port, "/strategys")
		return strategys


	index.exposed = True

if __name__ == '__main__':
	cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': 8081})
	cherrypy.quickstart(Frontend("127.0.0.1", 8080))
