from fileclass import *

class Append(File):
	"""Appends a line in a file
	Is described by :
	Name -> File name
	NewLine -> Line to add at the end of the file"""

	def __init__(self, name="", newline=""):
		"""Prepares the file appending"""
		File.__init__(self, name, newline)

	def __str__(self):
		"""Provides a description about which line is added to which file"""
		return "Appending line {} into file {}".format(self._newLine, self._name)

	def prepareCommand(self):
		"""Prepares the UNIX command to be executed"""
		self._finalCommand = "echo {} >> {}".format(self._newLine, self._name)

#Testing the class
if __name__ == "__main__":
	test=Append("Filename", "newline")
	print(test.Name)
	print(test.NewLine)
	print(test.Final)
