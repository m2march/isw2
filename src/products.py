class Product:
    def __init__(self, name):
	self._name = name.upper()

    def name(self):
	return self._name

    def __str__(self):
        return self.name()

    def __eq__(self, other):
	return self.name() == other.name()
