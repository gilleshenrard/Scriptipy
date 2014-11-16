from scriptable import *

class Command(Scriptable):
	"""Defines specific commands (without formatting)
	Is described by :
	Name : Command to execute
	Comment : Eventual comment to provide
	Final : Command to execute (same as Name, for a specific command)"""
	
	def __init__(self, name="", comment=""):
		"""Creates an empty specific command"""

		Scriptable.__init__(self, name, comment)
		self._finalCommand = ""

	def _set_finalCommand(self, final):
		self._finalCommand = final

	def _get_finalCommand(self):
		self.prepareCommand()
		return self._finalCommand

	def prepareCommand(self):
		"""Prepares the command to be executed"""
		self._finalCommand=self._name
		
	def __str__(self):
		"""Provides some informations on what to execute"""
		return "will execute {}".format(self._name)

	Final = property(_get_finalCommand, _set_finalCommand)

#Test the constructors
if __name__ == "__main__":
	test = Command("Some command", "Just a command")
	print(test.Name)
	print(test.Final)
	test.Comment="This is a comment"
	print(test)
