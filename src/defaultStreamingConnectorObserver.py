# from twitterStreamingConnector import *
# from defaultMemoryStore import *

class ConnectorObserver:
	def update(self):
		raise NotImplementedError( "Should have implemented this" ) 

class DefaultStreamingConnectorObserver(ConnectorObserver):
	def __init__(self, storeObject):
		self.storeObject = storeObject
		self.observables = []
	def addObservable(self, connector):
		self.observables.append(connector)
	def update(self, connectorData):		
		self.storeObject.store(connectorData)		

		


# if __name__ == '__main__':
# 	store = DefaultMemoryStore()
# 	observer = DefaultStreamingConnectorObserver(store)
# 	twitterConnector = TwitterStreamingConnector()
# 	twitterConnector.addObserver(observer)
# 	observer.addObservable(twitterConnector)

