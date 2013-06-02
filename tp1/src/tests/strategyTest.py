import unittest
from offer import *
from validProducts import ValidProductsProvider
from location import Location
from strategy import * 

class StrategyTestCase(unittest.TestCase):
	def setUp(self):
		self.aValidProductsProvider = ValidProductsProvider()

		self.aProduct = self.aValidProductsProvider.products()[0] 
		self.otherProduct = self.aValidProductsProvider.products()[1]

		self.aLocation = Location("a road 500")

		self.Offers = [Offer(self.aProduct, 4, self.aLocation), Offer(self.aProduct, 3, self.aLocation),  Offer(self.otherProduct, 5, self.aLocation)] 

		self.aNullStrategy = NullStrategy()
		self.aCheapestStrategy = CheapestStrategy()

	def test_validProducts(self):
		self.assertEquals(self.aNullStrategy.prioritize(self.Offers), self.Offers)

		cheapestOffers = self.aCheapestStrategy.prioritize(self.Offers)
		for i in range(0, len(cheapestOffers) - 1):
			self.assertTrue(cheapestOffers[i].price() < cheapestOffers[i+1].price())
