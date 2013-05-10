import products
from offer import Offer
from parser import ParserError
from parser import Parser

class OfferFactory:
	def __init__(self, parser=Parser()):
		self.parser = parser
		pass
	
	def createOffers(self, storeObject):
		results = []
		for textData in storeObject.getall():
			try:
				results.append(self.createOffer(textData))
			except ParserError:
				pass
		return results
			
	
	def createOffer(self, textData):
		rawText = textData.text()
		(product, price, location) = self.parser.parsing(rawText)
		return Offer(product, price, location)

##TODO: borrame
if __name__ == "__main__":
	class TextData:
		def __init__(self, text):
			self._text = text
		def text(self):
			return self._text
	class StoreObject:
		def __init__(self, lista):
			self._info = []
			for text in lista:
				self._info.append(TextData(text))
		def getall(self):
			return self._info
	import parser
	of = OfferFactory(parser.Parser())
	lista = ["Yerba 5 pesos el kilo av.lafuente 1277 #precioJusto",
			 "aZucar 2 p el kg yatai 50 5toA #precioJusto #lallaa",
			 "dsadsadsadsa sdsad adsa 432 sda #precioJusto"]
	res = of.createOffers(StoreObject(lista))
	
	for x in res:
		print x
