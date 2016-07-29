from command import *

class Append(Command):
	"""Appends a line in a file
	Is described by :
	Name : File name
	NewLine : Line to add at the end of the file"""

	def __init__(self, name="", newline=""):
		"""Creates and initialises a new line appending"""
		Command.__init__(self, name)
		self.NewLine = newline

	def _get_newLine(self):
		"""Returns the new line to append to a file"""
		return self._newLine

	def _set_newLine(self, t_newline):
		"""Sets the new line to append to a file"""
		self._newLine = t_newline

	def __str__(self):
		"""Provides the command which appends the new line to the file"""
		return "echo {} >> {}".format(self.NewLine, self.Name)

	NewLine = property(_get_newLine, _set_newLine)
