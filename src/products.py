class Product:
	def __init__(self, name, unit):
		self._name = name.lower()
		self._unit = unit

	def name(self):
		return self._name

	def unit(self):
		return self._unit

	def __str__(self):
		return self.name()

	def __eq__(self, other):
		return self.name() == other.name()
