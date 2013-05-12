class ModelManager(Object):
	def __init__(self,aDataManager, anOfferFactory, aStoreObject):
		self.dataManager = aDataManager
		self.offerFactory = offerFactory
		self.storeObject = aStoreObject
	def process(self, anInmmutableOfferQuery):
		raise NotImplementedError("Should have implemented this")