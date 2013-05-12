from defaultDataManager import *
from defaultMemoryStore import *
from offerFactory import *

class DefaultModelManager(ModelManager):
	def __init__(self):				
		memoryStore = DefaultMemoryStore()
		dataManager = DefaultDataManager(memoryStore)
		offerFactory = DefaultOfferFactory()
		super(DefaultOfferFactory,self).__init__(self,dataManager,offerFactory,memoryStore)

	def process(self, anInmmutableOfferQuery):


