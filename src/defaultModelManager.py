from defaultDataManager import *
from defaultMemoryStore import *
from offerFactory import *
from modelManager import *

class DefaultModelManager(ModelManager):
	def __init__(self):				
		memoryStore = DefaultMemoryStore()
		dataManager = DefaultDataManager(memoryStore)
		offerFactory = DefaultOfferFactory()
		super(DefaultModelManager,self).__init__(dataManager,offerFactory,memoryStore)


if __name__ == "__main__":
	modelManager = DefaultModelManager()
