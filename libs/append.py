from command import *

class Append(Command):
	"""Appends a line in a file
	Is described by :
	Name -> File name
	NewLine -> Line to add at the end of the file"""

	def __init__(self, name="", newline=""):
		"""Prepares the file appending"""
		Command.__init__(self, name)
		self._newLine = newline

	def _get_newLine(self):
		return self._newLine

	def _set_newLine(self, newline):
		self._newLine = newline

	def __str__(self):
		"""Provides a description about which line is added to which file"""
		return "Appending line {} into file {}".format(self.NewLine, self.Name)

	def prepareCommand(self):
		"""Prepares the UNIX command to be executed"""
		self.Final = "echo {} >> {}".format(self.NewLine, self.Name)

	NewLine = property(_get_newLine, _set_newLine)

#Testing the class
if __name__ == "__main__":
	test=Append("Filename", "newline")
	print(test.Name)
	print(test.NewLine)
	print(test.Final)
