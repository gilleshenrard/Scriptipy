class command(scriptable):
	"""Defines specific commands (without formatting)
	Defines the final command for the tree"""
	
	def __init__(self):
		"""Creates an empty specific command"""
		
		scriptable.__init__(self)
		self.finalCommand = ""
	
	def __init__(self, name):
		"""Creates a specific command"""

		scriptable.__init__(self, name)
		self._finalCommand = ""

	def _set_finalCommand(self, final):
		self.finalCommand = final

	def _get_finalCommand(self):
		return self._finalCommand
		
	def __str__(self):
		return self._comment

	Final = property(_set_finalCommand, _get_finalCommand)

#Test the constructors
if __name__ == "__main__":
	test = command("Some command", "Just a command")
	print(test.Name)
	print(test.Final)
	print(test)
