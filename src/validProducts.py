from products import Product

class ValidProductsProvider:
  def products(self):
    return [Product("Yerba"), Product("Azucar")]


if __name__ == "__main__":
  productsList = ValidProductsProvider().products()
  assert map(lambda p : p.name(), productsList) == ["YERBA", "AZUCAR"]
