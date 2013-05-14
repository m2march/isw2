from products import Product
from unit import Unit

class ValidProductsProvider:
  def products(self):
    kilo = Unit("kilo", ["kilo", "kg", "kilos", "kgs"])
    litro = Unit("litro", ["litro", "litros", "lt", "lts", "l"])
    return [Product("Yerba", kilo), Product("Azucar", kilo),
     Product("Papa",kilo), Product("Leche", litro), 
     Product("Dulce", kilo), Product("Dulce de leche", kilo)]

