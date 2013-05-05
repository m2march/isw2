class Unit:
	def __init__(self, name, listOfRepresentations):
		self._name = name.lower()
		self._listOfRepresentations = listOfRepresentations
	
	def name(self):
		return self._name
	
	def representations(self):
		return self._listOfRepresentations
	
	def __str__(self):
		return self._name
