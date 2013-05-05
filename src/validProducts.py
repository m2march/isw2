from products import Product
from unit import Unit

class ValidProductsProvider:
	def products(self):
		kilo = Unit("kilo", ["kilo", "kg", "kilos", "kgs"])
		return [Product("Yerba", kilo), Product("Azucar", kilo)]



if __name__ == "__main__":
  productsList = ValidProductsProvider().products()
  assert map(lambda p : p.name(), productsList) == ["YERBA", "AZUCAR"]
