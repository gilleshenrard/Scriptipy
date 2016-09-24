from .datatype import *

class XMLdata(DataType):
	"""Command XML data (de)serialisation
	:param source: XML source file name"""

	def __init__(self, source=""):
		"""Create and initialise an XML (de)serialisation process."""
		DataType.__init__(self, source)

	def deserialize(self):
		"""Deserialise data from an XML data file."""
		pass

	def serialize(self):
		"""Serialise data from a JSON data file."""
		pass