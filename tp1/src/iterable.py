class Iterable:
	def __init__(self, aConnectors):
		self.connectors = aConnectors
		self.itconnectors = iter(self.connectors)
		self.currentConnectorit = iter(self.itconnectors.next().getData())
	def __iter__(self):
		return self
	def next(self):
		try:
			next = self.currentConnectorit.next()
			return next
		except StopIteration:
			self.currentConnectorit = iter(self.itconnectors.next().getData())
			return self.next()