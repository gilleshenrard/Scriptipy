from .datatype import *
from json import loads, dumps
from os import path

class JSONData(DataType):
	def __init__(self, source=""):
		DataType.__init__(self, source)

	def deserialize(self):
		if path.exists(self.Source):
			with open(self.Source, "r") as file:
				return loads(file.read())
		else:
			raise ValueError("File {} not found".format(self.Source))

	def serialize(self, data):
		with open(self.Source, "w") as file:
			file.write(dumps(data, sort_keys=True, indent=4))
