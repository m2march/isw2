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
