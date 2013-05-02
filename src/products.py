class Product:
    def name(self):
        raise NotImplementedError()

    def __str__(self):
        return self.name()

class Yerba(Product):
	def name(self):
		return "Yerba"

class Azucar(Product):
	def name(self):
		return "Azucar"
