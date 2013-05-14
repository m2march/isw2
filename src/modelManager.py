class ModelManager(object):
	def __init__(self,aDataManager, anOfferFactory):
		self.dataManager = aDataManager
		self.offerFactory = anOfferFactory
	def process(self, anOfferQuery):
		#Get data from outside and create the offers
		offers = self.offerFactory.createOffers(self.dataManager.getOffers())
		#filter by user requirements
		aFilter = anOfferQuery.filter()		
		offersFiltered = filter(lambda anOffer: aFilter.filter(anOffer), offers)
		aStrategy = anOfferQuery.strategy()
		offersFinished = aStrategy.prioritize(offersFiltered)
		return offersFinished


