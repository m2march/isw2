class Product:
	def name(self):
		raise NotImplementedError()

class Yerba(Product):
	def name(self):
		return "Yerba"

class Azucar(Product):
	def name(self):
		return "Azucar"
