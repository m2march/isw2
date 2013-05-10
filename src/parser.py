import products
from validProducts import ValidProductsProvider
from location import Location


## Parser error
class ParserError(Exception):
	"""Create offer error"""
	def __init__(self, error):
		self.error = error

	def __str__(self):
		return self.error + " couldn't be parsing in the text data"

class Parser:
	def __init__(self):
		pass

	def parsing(self, rawText):
		rawText = self._removeHashTag(rawText.lower())
		product = ProductParser().get(rawText)
		price = PriceParser(product).get(rawText)
		locationName = LocationParser(product, price).get(rawText)
		try:
			location = Location(locationName)
		except:
			raise ParserError("location")
		return (product, price, location)

	def _removeHashTag(self, rawText):
		palabras = rawText.split(" ")
		rawText = []
		for palabra in palabras:
			if palabra.find("#") == -1:
				rawText.append(palabra)
		return " ".join(rawText)


class EspecificParser:
	def __init__(self):
		pass
	def get(self):
		raise NotImplementedError( "Should have implemented this" )

class ProductParser(EspecificParser):
	def get(self, rawText):
		resultProduct = None
		for product in ValidProductsProvider().products():
			name = product.name()			 
			if name == rawText[:len(name)]:
				if not(resultProduct) or len(name) > len(resultProduct.name()):
					resultProduct = product

		if not(resultProduct):
			raise ParserError("product")
		return resultProduct
		
class PriceParser(EspecificParser):
	def __init__(self, product):
		self._product = product

	def get(self, rawText):
		## devuelve el primer numero que encuentra en el texto
		rawText = rawText.replace("$", "")
		rawText = rawText.replace(",", ".")
		for palabra in rawText.split(" "):
			try:
				return float(palabra)
			except ValueError:
				pass
		raise ParserError("Price")

class LocationParser(EspecificParser):
	def __init__(self, product, price):
		self._product = product
		self._price = price

	def get(self, rawText):
		rawText = self._removePriceAndUnit(rawText)
		return rawText.strip()
		
	def _removePriceAndUnit(self, rawText):
		for unit_name in self._product.unit().representations():
			if rawText.find(unit_name) != -1:
				return rawText[rawText.find(unit_name) + len(unit_name):]
		raise ParserError("Unit")

if __name__ == "__main__":
	(product, price, location) = Parser().parsing("Yerba 5 pesos el kilo av.lafuente 1277 #precioJusto")
	print product, price, location

		
		
