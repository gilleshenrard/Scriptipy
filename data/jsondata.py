from .datatype import *
from json import loads, dumps
from os import path

class JSONData(DataType):
	"""Command JSON data (de)serialisation
	:param source: JSON source file name"""

	def __init__(self, source=""):
		"""Create and initialise a JSON (de)serialisation process."""
		DataType.__init__(self, source)

	def deserialize(self):
		"""Deserialise data from a JSON data file.
		Test if file exists at the source name.

		Exceptions:
		Raises ValueError if the file is not found"""

		if path.exists(self.Source):
			with open(self.Source, "r") as file:
				return loads(file.read())
		else:
			raise ValueError("File {} not found".format(self.Source))

	def serialize(self, data):
		"""Serialise data to a file with JSON formatting.
		If the file exists, erase all the content first."""

		with open(self.Source, "w") as file:
			file.write(dumps(data, sort_keys=True, indent=4))
