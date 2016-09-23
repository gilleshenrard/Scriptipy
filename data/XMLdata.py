from .datatype import *

class XMLdata(DataType):
	"""Defines the XML file handling"""

	def __init__(self, source=""):
		"""Builds a new XML handling module"""
		DataType.__init__(self, source)

	def deserialize(self):
		"""Extracting procedure"""

	def serialize(self):
		"""Serializing procedure"""