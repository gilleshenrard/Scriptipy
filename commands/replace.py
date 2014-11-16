from fileclass import *

class Replace(File):
	"""Replaces a line by another in a file
	Is defined by :
	Name : File name
	OldLine : Line to replace
	NewLine : Line to replace by"""

	def __init__(self, name="", oldline="", newline=""):
		File.__init__(self, name, newline)
		self._oldLine = oldline

	def _set_oldLine(self, oldline):
		self._oldLine = oldline

	def _get_oldLine(self):
		return self._oldLine

	def __str__(self):
		return "replacing {} by {} in {}".format(self._oldLine, self._newLine, self.Name)

	def prepareCommand(self):
		self._finalCommand = "sed -i 's/{}/{}/g' {}".format(self._oldLine, self._newLine, self.Name)

	OldLine = property(_get_oldLine, _set_oldLine)
	
#Testing class
if __name__ == "__main__":
	test=Replace("testfile", "oldline", "newline")
	print(test.Name)
	print(test.OldLine)
	print(test.NewLine)
	print(test.Final)
	print(test)
