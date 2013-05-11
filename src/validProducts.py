from products import Product
from unit import Unit

class ValidProductsProvider:
  def products(self):
    kilo = Unit("kilo", ["kilo", "kg", "kilos", "kgs"])
    return [Product("Yerba", kilo), Product("Azucar", kilo)]

