from twitterStreamingConnector import *
# import offerFactory
from twitterSimpleConnector import *
from iterable import *

class DataManager:
	def __init__(self, aConnector):
		self.connectors = []
		self.connectors.append(aConnector)
	def getOffers(self):
		return Iterable(self.connectors)
	def addConnector(self, aConnector):
		self.connectors.append(aConnector)


if __name__ == '__main__':
	connectorEs = TwitterSimpleConnector("#precioJusto","es")
	connectorEn = TwitterSimpleConnector("#precioJusto", "en")
	dtdm = DataManager(connectorEs)
	dtdm.addConnector(connectorEn)
	for offer in dtdm.getOffers():
		print offer.text.encode("utf-8","ignore")

