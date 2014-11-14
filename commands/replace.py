class Replace(File):
	"""Replaces a line by another in a file"""

	def __init__(self):
		File.__init__(self)
		self._oldLine = ""

	def __init__(self, name):
		File.__init__(self, name)
		self._oldLine = ""

	def __init__(self, name, newline):
		File.__init__(self, name, newline)
		self._oldLine = ""

	def __init__(self, name, oldline, newline):
		File.__init(self, name, newline)
		self._oldLine = oldline

	def _set_oldLine(self, oldline):
		self._oldLine = oldline

	def _get_oldLine(self):
		return self._oldLine

	def __str__(self):
		return "replacing {} by {} in {}".format(self.oldLine, self.newLine, self.Name)

	def prepareCommand(self):
		Command.prepareCommand(self)
		return self.Final += "sed -i 's/{}/{}/g' {}".format(self.oldLine, self.newLine, self.Name)

	oldLine = property(_set_oldLine, _get_oldLine)
	
#Testing class
if __name__ == "__main__"
	test=Replace("testfile", "oldline", "newline")
	print(test.Name)
	print(test.oldLine)
	print(test.newLine)
	print(test.Final)
