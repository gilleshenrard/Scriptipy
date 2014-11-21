from datatype import *

class XMLdata(Datatype):
	"""Defines the XML file handling"""

	def __init__(self):
		"""Builds a new XML handling module"""
		
		Filetype.__init__(self)

	def extractFromFile(self):
		"""Extracting procedure"""
