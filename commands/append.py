class Append(File):
	"""Appends a line in a file"""
	
	def __init__(self):
		File.__init__(self)

	def __init__(self, name)
		File.__init__(self, name)

	def __init__(self, name, newline)
		File.__init__(self, name, newline)

	def __str__(self):
		return "Appending line {} into file {}".format(self.newLine, self.Name)

	def prepareCommand(self):
		Command.prepareCommand(self)
		self.Final += "echo {} >> {}".format(self.newLine, self.Name)
		return self.Final

if __name__=="__main__"
	test=Append("filename", "newline")
	print(test)
	print(test.Final)
