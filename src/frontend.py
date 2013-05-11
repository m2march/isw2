import cherrypy

import httplib
import json

class UnreachableRestResource(Exception):
  def __init__(self, aReason):
    self.reason = "UnreachableRestResource: " + aReason

  def __str__(self):
    return self.reason

class QueryError(Exception):
  def __init__(self, aReason):
    self.reason = aReason

  def __str__(self):
    return self.reason


class RestBackend(object):
  def __init__(self, aBackendURL, aBackendPort):
    self.url = aBackendURL
    self.port = aBackendPort

  def ask_for(self, resource, parameter = {}):

    if len(parameter) != 0:
      resource = resource + "?"
      for key, val in parameter.items():
        resource = resource + key + "=" + val + "&"

    conn = httplib.HTTPConnection(self.url, self.port)
    conn.request("GET", resource)

    response = conn.getresponse()

    if response.status != 200:
      errorString = str(self.url) + ":" + str(self.port) + " " + resource  + "\n\tresponse_status = " + str(response.status) + "\n"
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

  def strategies(self):
    return OfferRestBackend.map_to_utf8(self.backend.ask_for("/strategies"))

  def offerQuery(self, Product, MinPrice, MaxPrice, Strategy):
    parameters = {"Product" : Product, "MinPrice" : MinPrice, "MaxPrice" : MaxPrice, "Strategy":Strategy}
    response = self.backend.ask_for("/offerquery", parameters)

    if "error" in response.keys() :
      raise QueryError(response["reason"])

    return response["result"]

class Frontend(object):
  def __init__(self, aBackendURL, aBackendPort):
    self.backend = OfferRestBackend(aBackendURL, aBackendPort)
    print "Frontend startup"

  def offerqueryPage(self, Product, MinPrice, MaxPrice, Strategy):
    query_result = self.backend.offerQuery(Product, MinPrice, MaxPrice, Strategy) #parameter validation must be done on the backend
    response = self.offerQueryResponse(query_result)
    return response

  def offerQueryResponse(self, queryResult):
    response = "<html>"
    response += self.buildHead()
    response += "<body>"

    if len(queryResult) == 0:
      response += "<h1 style=\"text-align: center\";>No offers matching the requested description.</h1>"
    else:
      response += "<h1 style=\"text-align: center\";>Offers matching the requested description</h1>"

      for result in queryResult:
        response += "<p style=\"text-align: center\";>TODO: Print the result in a nice way! " + str(result) + "</p>"
    response += "</body></html>"
    return response

  def index(self, Product = "", MinPrice = "", MaxPrice = "", Submit = "", Strategy = ""):
    response = ""

    try:
      if len(Submit) == 0:
        response = self.indexPage()
      else:
        response = self.offerqueryPage(Product, MinPrice, MaxPrice, Strategy)
    except Exception as anException:
      response = self.errorPage(anException)

    return response

  def errorPage(self, anError):
    return "<html>\n" + self.buildHead() + "\n<body><h1>Ops!</h1>\n" + str(anError) + "</body>\n</head>"

  def indexPage(self):
    headAndBody = self.buildHead() + self.buildIndexBody()
    response = "<html>" + headAndBody + "</html>"
    return response

  def buildHead(self):
    return "<head><title>El #Precio Justo</title></head>"

  def buildIndexBody(self):
    productList = self.backend.products()
    strategyList = self.backend.strategies()

    body = """<body>
          <h1 style="text-align: center;">Precio Justo</h1>
          <p style="text-align: center;">Product - Min price - Max price - Strategy</p>
            <form enctype="text/plain" method="get" name="UserQuery">
              <p style="text-align: center;">
                <select name="Product">""" + self.productSelectBox(productList) + """</select>

                <input name="MinPrice" size="6" type="text" />
                <input name="MaxPrice" size="6" type="text" />

                <select name="Strategy">""" + self.strategySelectBox(strategyList) + """</select>

                <input name="Submit" type="submit" value="I'm feeling lucky" action="index" method="get"/>
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
