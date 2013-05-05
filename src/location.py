
class Location:
	def __init__(self, rawLocationName):
		self._rawLocationName = rawLocationName
		
	def __str__(self):
		return self._rawLocationName
