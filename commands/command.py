class Command():
	"""Defines specific commands (without formatting)
	Is described by :
	Name : Item name or command to execute
	Comment : Eventual comment to provide"""
	
	def __init__(self, name="", comment=""):
		"""Creates and initialises a new specific command"""
		self.Name = name
		self.Comment = comment

	def _set_name(self, name):
		"""Specifies a value for the Item name or the command"""
		self._name = name

	def _get_name(self):
		"""Returns the Item name or the command"""
		return self._name

	def _set_comment(self, comment=""):
		"""Specifies a comment for the command to execute (wipes it if left blank)"""
		self._comment = comment

	def _get_comment(self):
		"""Returns the specified comment"""
		return self._comment

	def __str__(self):
		"""Provides the command to execute"""
		return self.Name

	Name = property(_get_name, _set_name)
	Comment = property(_get_comment, _set_comment)
