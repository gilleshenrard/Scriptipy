from libs.datatype import *
from json import loads, dumps

class JSONData(DataType):
	def __init__(self, filename=""):
		self.FileName=filename

	def _get_filename(self):
		return self._filename

	def _set_filename(self, filename):
		self._filename=filename

	def importData(self):
		pass

	def exportData(self, data):
		pass

	FileName=property(_get_filename, _set_filename)
