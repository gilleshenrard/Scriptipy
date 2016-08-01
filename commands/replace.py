from .append import *

class Replace(Append):
	"""Replaces a line by another in a file
	Is defined by :
	Name : File name
	OldLine : Line to replace
	NewLine : Line to replace by"""

	def __init__(self, name="", oldline="", newline=""):
		"""Creates and initialises a line replacement"""
		Append.__init__(self, name, newline)
		self.OldLine = oldline

	def _set_oldLine(self, oldline):
		"""Sets the old line to replace with the new line"""
		self._oldLine = oldline

	def _get_oldLine(self):
		"""Returns the old line to replace with the new line"""
		return self._oldLine

	def __str__(self):
		return "sed -i 's/{}/{}/g' {}".format(self.OldLine, self.NewLine, self.Name)

	OldLine = property(_get_oldLine, _set_oldLine)
