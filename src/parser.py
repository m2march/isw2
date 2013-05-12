import products
from offer import OfferBuilder
from validProducts import ValidProductsProvider
from location import Location


## Parser error
class ParserError(Exception):
	"""Create offer error"""
	def __init__(self, error):
		self.error = error

	def __str__(self):
		return self.error + " couldn't be parsing in the text data"

class ParserChain(object):
	def __init__(self, parserList):
		self._parserList = parserList
		pass

	def parsing(self, rawText):
		rawText = self._removeHashTag(rawText.lower())
		offerBuilder = OfferBuilder()
		for parser in self._parserList:
			offerBuilder = parser.process(rawText, offerBuilder)
		return offerBuilder

	def addParser(self, parser):
		self._parserList.append(parser)

	def _removeHashTag(self, rawText):
		palabras = rawText.split(" ")
		rawText = []
		for palabra in palabras:
			if palabra.find("#") == -1:
				rawText.append(palabra)
		return " ".join(rawText)

class DefaultParserChain(ParserChain):
	def __init__(self):
		listaParser = [ProductParser(), PriceParser(), LocationParser()]
		super(DefaultParserChain, self).__init__(listaParser)
		

class EspecificParser:
	def __init__(self):
		pass
	def process(self, offerBuilder):
		raise NotImplementedError( "Should have implemented this" )

class ProductParser(EspecificParser):
	def process(self, rawText, offerBuilder):
		resultProduct = None
		for product in ValidProductsProvider().products():
			name = product.name()			 
			if name == rawText[:len(name)]:
				if not(resultProduct) or len(name) > len(resultProduct.name()):
					resultProduct = product

		if not(resultProduct):
			raise ParserError("product")
		offerBuilder.setProduct(resultProduct)
		return offerBuilder
		
class PriceParser(EspecificParser):
	def process(self, rawText, offerBuilder):
		## devuelve el primer numero que encuentra en el texto
		rawText = rawText.replace("$", "")
		rawText = rawText.replace(",", ".")
		for palabra in rawText.split(" "):
			try:
				price = float(palabra)
				offerBuilder.setPrice(price)
				return offerBuilder
			except ValueError:
				pass
		raise ParserError("Price")

class LocationParser(EspecificParser):
	def process(self, rawText, offerBuilder):
		rawText = self._removePriceAndUnit(rawText, offerBuilder.getProduct())
		Address = rawText.strip()	
		
		try:
			location = Location(Address)
			offerBuilder.setLocation(Location)
			return offerBuilder
		except:
			raise ParserError("location")
		
	def _removePriceAndUnit(self, rawText, product):
		for unit_name in product.unit().representations():
			if rawText.find(unit_name) != -1:
				return rawText[rawText.find(unit_name) + len(unit_name):]
		raise ParserError("Unit")

if __name__ == "__main__":
	offerBuilder = DefaultParserChain().parsing("Yerba 5 pesos el kilo av.lafuente 1277 #precioJusto")
	print offerBuilder.build()

		
		
