import products

class Offer:
	def __init__(self, product, price, location):
		self._product = product
		self._price = price
		self._location = location

	def product(self):
		return self._product
	
	def price(self):
		return self._price
	
	def location(self):
		return self._location
	
	def __str__(self):
		return "oferta({0}, {1}, {2})".format(self._product, self._price, self._location)

class OfferBuilder:
	def __init__(self, product = None, price = None, location = None):
		self._product = product
		self._price = price
		self._location = location
	def setProduct(self, product):
		self._product = product
	def getProduct(self):
		return self._product
	def setPrice(self, price):
		self._price = price
	def getPrice(self):
		return self._price
	def setLocation(self, location):
		self._location = location
	def getLocation(self):
		return self._location
	def build(self):
		return Offer(self._product, self._price, self._location)
