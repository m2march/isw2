
class StoreObject:
	def store(self, data2store):
		raise NotImplementedError( "Should have implemented this" )
	def getAll(self):
		raise NotImplementedError( "Should have implemented this" )

class DefaultMemoryStore(StoreObject):
	def __init__(self):
		self.data = []
	def store(self, data2store):
		if (not self.contains(data2store)):
			self.data.append(data2store)
			print " ".join(["data added", data2store.text])			
	def getAll(self):
		return self.data
	def contains(self, data2check):
		for data in self.data:
			if data.text == data2check.text:
				return True		

# if __name__ == '__main__':
# 	print "test for default storage"
# 	dataStore = DefaultMemoryStore()
# 	data = 2
# 	print "adding data to store"
# 	dataStore.store("soy un test #precioJusto")
# 	if (dataStore.getAll()[0] == "soy un test #precioJusto"):
# 		print "getting element ok from store"
# 	else: 
# 		print "store is wrong"
# 	if (dataStore.contains("soy un test #precioJusto")):
# 		print "checking element ok"
# 	else:
# 		print "checking element fail"

