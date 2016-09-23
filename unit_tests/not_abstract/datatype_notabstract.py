from data.datatype import *

class DataTypeNotAbstract(DataType):
	def __init__(self, source=""):
		DataType.__init__(self, source)

	def deserialize(self):
		pass

	def serialize(self):
		pass