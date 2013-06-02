import unittest
from validProducts import ValidProductsProvider

class ValidProductsProviderTest(unittest.TestCase):

  def setUp(self):
    self.productsList = ValidProductsProvider().products()

  def test_validProducts(self):
    self.assertEquals(
      map(lambda p : (p.name(), p.unit().name()), self.productsList),
      [("yerba", "kilo"), ("azucar", "kilo")]
    )

