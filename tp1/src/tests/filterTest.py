import unittest
from filter import *
from validProducts import ValidProductsProvider
from offer import Offer
from location import Location

class FilterTestCase(unittest.TestCase):

  def setUp(self):
	self.aValidProductsProvider = ValidProductsProvider()
	
	self.aProduct = self.aValidProductsProvider.products()[0] 
	self.otherProduct = self.aValidProductsProvider.products()[1]
	
	self.aLocation = Location("a road 500")
	
	self.Offers = [Offer(self.aProduct, 3, self.aLocation), Offer(self.aProduct, 4, self.aLocation), Offer(self.otherProduct, 4, self.aLocation)] 
	
	self.aProductFilter = ProductFilter(self.aProduct)
	self.aPriceRangeFilter = PriceRangeFilter(3.5, 4.5)
	self.anAndFilter = AndFilter().addFilter(self.aProductFilter).addFilter(self.aPriceRangeFilter)

  def test_validProducts(self):
    self.assertTrue(self.aProductFilter.filter(self.Offers[0]) and self.aProductFilter.filter(self.Offers[1]) and not self.aProductFilter.filter(self.Offers[2]))
	self.assertTrue(not self.aPriceRangeFilter.filter(self.Offers[0]) and self.aPriceRangeFilter.filter(self.Offers[1]) and self.aPriceRangeFilter.filter(self.Offers[2]))

	self.assertTrue(not self.anAndFilter.filter(self.Offers[0]) and self.anAndFilter.filter(self.Offers[1]) and not self.anAndFilter.filter(self.Offers[2]))

