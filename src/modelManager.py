class ModelManager(object):
	def __init__(self,aDataManager, anOfferFactory, aStoreObject):
		self.dataManager = aDataManager
		self.offerFactory = anOfferFactory
		self.storeObject = aStoreObject
	def process(self, anOfferQuery):
		#Get offers from outside
		self.dataManager.getOffers()
		#Parse and create offers
		offers = self.offerFactory.createOffers(self.storeObject)
		print offers
		#filter by user requirements
		aFilter = anOfferQuery.filter()		
		offersFiltered = filter(lambda anOffer: aFilter.filter(anOffer), offers)
		aStrategy = anOfferQuery.strategy()
		offersFinished = aStrategy.prioritize(offersFiltered)
		return offersFinished
