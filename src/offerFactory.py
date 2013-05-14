import products
from offer import Offer
from offer import OfferBuilder
from parser import *

class OfferFactory(object):
	def __init__(self, parser):
		self.parser = parser
		pass
	
	def createOffers(self, anIterable):
		results = []
		for rawInfo in anIterable:
			try:
				results.append(self.createOffer(rawInfo))
			except ParserError:
				pass
		return results
			
	
	def createOffer(self, rawInfo):
		offerbuilder = self.parser.parsing(rawInfo)
		return offerbuilder.build()

if __name__ == "__main__":
	class TextData:
		def __init__(self, text):
			self.text = text
		def text(self):
			return self.text
	class StoreObject:
		def __init__(self, lista):
			self._info = []
			for text in lista:
				self._info.append(TextData(text))
		def getAll(self):
			return iter(self._info)
	import parser
	parserChain = ParserChain([ProductParser(), PriceParser(), LocationParser()])
	of = OfferFactory(parserChain)
	lista = ["Yerba 5 pesos el kilo av.lafuente 1277 #precioJusto",
			 "aZucar 2 p el kg yatai 50 5toA #precioJusto #lallaa",
			 "dsadsadsadsa sdsad adsa 432 sda #precioJusto",
			 "Papa $12 Kg Cabildo 1000 #PrecioJusto",
			 "leche $5.05 Lt Cabildo 3000 #PrecioJusto",
			 "Dulce de leche $5.05 kg Cabildo 3000 #PrecioJusto"]
	res = of.createOffers(StoreObject(lista).getAll())
	
	for x in res:
		print x
