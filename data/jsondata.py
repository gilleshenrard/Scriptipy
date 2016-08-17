from libs.datatype import *
from json import loads, dumps
from os import path

class JSONData(DataType):
	def __init__(self, filename=""):
		self.FileName=filename

	def _get_filename(self):
		return self._filename

	def _set_filename(self, filename):
		self._filename=filename

	def deserialize(self):
		if path.exists(self.FileName):
			with open(self.FileName, "r") as file:
				return loads(file.read())
		else:
			raise ValueError("File {} not found".format(self.FileName))

	def serialize(self, data):
		with open(self.FileName, "w") as file:
			file.write(dumps(data, sort_keys=True, indent=4))

	FileName=property(_get_filename, _set_filename)
