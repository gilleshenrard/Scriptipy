from .datatype import *
from os import path
from xml.etree.ElementTree import parse

class XMLdata(DataType):
	"""Command XML data (de)serialisation
	:param source: XML source file name"""

	def __init__(self, source=""):
		"""Create and initialise an XML (de)serialisation process."""
		DataType.__init__(self, source)

	def deserialize(self):
		"""Deserialise data from an XML data file."""
		if path.exists(self.Source):
			#Retrieving XML tree root			
			tree = parse(self.Source)
			root = tree.getroot()
			return root
		else:
			raise ValueError("File {} not found".format(self.Source))

	def serialize(self):
		"""Serialise data from a JSON data file."""
		pass