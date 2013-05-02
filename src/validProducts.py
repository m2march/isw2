import products

class ValidProductsProvider:
	def products(self):
		return [products.Yerba(), products.Azucar()]


if __name__ == "__main__":
	productsList = ValidProductProvider().products()
	assert map(lambda p : p.name(), productsList) == ["Yerba", "Azucar"]
