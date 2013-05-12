from twitterStreamingConnector import *
# import offerFactory
from defaultStreamingConnectorObserver import *
from defaultPulleableConnectorObserver import *
from defaultMemoryStore import *
from twitterSimpleConnector import *

#TODO DO THE DATA MANAGER ABSTRACTION!

class DefaultDataManager:
	def __init__(self, aStoreObject):		
		#new data storage
		self.dataStorage = aStoreObject		
		#new streaming observer
		self.streamingObserver = DefaultStreamingConnectorObserver(self.dataStorage)
		#creating default twitter streaming connector
		twitterStreamingConnector = TwitterStreamingConnector("#boludoJusto")
		twitterStreamingConnector.addObserver(self.streamingObserver)		
		#do the observer registration
		self.streamingObserver.addObservable(twitterStreamingConnector)

		#new pull observer
		self.pulleableObserver = DefaultPulleableConnectorObserver(self.dataStorage)
		#creating default twitter rest connector
		twitterSimpleConnector = TwitterSimpleConnector("#boludoJusto")
		twitterSimpleConnector.addObserver(self.pulleableObserver)
		self.pulleableObserver.addObservable(twitterSimpleConnector)

		# self.factory = OfferFactory()
	def getOffers(self):
		self.pulleableObserver.pull()
		# return self.factory.createOffers(self.dataStorage)

if __name__ == '__main__':
	store = DefaultMemoryStore()
	dtdm = DefaultDataManager(store)
	dtdm.getOffers()
	print dtdm.dataStorage.data

