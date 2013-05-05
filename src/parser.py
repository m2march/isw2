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
		rawText = rawText.lower()
		rawText = self._removeHashTag(rawText)
		product = self._getProduct(rawText)
		rawText = self._removeProduct(rawText, product)
		price = self._getPrice(rawText)			
		rawText = self._removePriceAndUnit(rawText,product)
		locationName = self._getLocation(rawText)
		location = Location(locationName)
		return (product, price, location)

	def _removeHashTag(self, rawText):
		palabras = rawText.split(" ")
		rawText = []
		for palabra in palabras:
			if palabra.find("#") == -1:
				rawText.append(palabra)
		return " ".join(rawText)

	def _getProduct(self, rawText):
		resultProduct = None
		for product in ValidProductsProvider().products():
			name = product.name()
			 
			if name == rawText[:len(name)]:
				if not(resultProduct) or len(name) > len(resultProduct.name()):
					resultProduct = product
		if not(resultProduct):
			raise ParserError("product")
		return resultProduct
		
	def _removeProduct(self, text, product):
		return text[len(product.name()) + 1:]

	def _getPrice(self, rawText):
		## devuelve el primer numero que encuentra en el texto
		rawText = rawText.replace("$", "")
		rawText = rawText.replace(",", ".")
		for palabra in rawText.split(" "):
			try:
				return float(palabra)
			except ValueError:
				pass
		raise ParserError("Price")
	
	def _removePriceAndUnit(self, rawText, product):
		for unit_name in product.unit().representations():
			if rawText.find(unit_name) != -1:
				return rawText[rawText.find(unit_name) + len(unit_name):]
		raise ParserError("Unit")
	
	def _getLocation(self, rawText):
		return rawText.strip()

if __name__ == "__main__":
	(product, price, location) = Parser().parsing("Yerba 5 pesos el kilo av.lafuente 1277 #precioJusto")
	print product, price, location

		
		
