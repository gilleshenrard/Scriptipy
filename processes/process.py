from datatype import *
from XMLdata import *

class Process:
	"""Defines the module to handle the data recovering"""

	def __init__(self, name=""):
		"""Builds a Process"""

		self._fileName = name
		self._fileType = ""
		assignMethod()

	def assignMethod(self):
		file=self._fileName.rsplit(".")
		if file[1] == "xml":
			self._fileType = XMLdata()

	def _get_fileName(self):
		return self._fileName

	def _set_fileName(self, name=""):
		self._fileName = name

	def _set_fileType(self, type):
		self._fileType = type

	def _get_fileType(self):
		return self._fileType

	FileName = property(_get_fileName, _set_fileName)
	FileType = property(_get_fileType, _set_fileType)

if __name__ == "__main__":
	test = Process("ubuntu.xml")
	
