# from twitterSimpleConnector import *
# from defaultMemoryStore import *

class ConnectorObserver:
	def update(self):
		raise NotImplementedError( "Should have implemented this" ) 

class DefaultPulleableConnectorObserver(ConnectorObserver):
	def __init__(self, storeObject):
		self.storeObject = storeObject
		self.observables = []
	
	def addObservable(self, connector):
		self.observables.append(connector)

	def update(self, connectorData):		
		self.storeObject.store(connectorData)
	
	def pull(self):
		for observable in self.observables:
			observable.pull()

# if __name__ == '__main__':	
# 	store = DefaultMemoryStore()
# 	observer = DefaultPulleableConnectorObserver(store)
# 	twitterConnector = TwitterSimpleConnector()
# 	twitterConnector.addObserver(observer)
# 	observer.addObservable(twitterConnector)
# 	observer.pull()
# 	print store.getAll()