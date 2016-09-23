class Command():
	"""Specific command to execute
	:param name: Item name or command to execute (string)
	:param comment: Eventual comment to provide"""
	
	def __init__(self, name="", comment=""):
		"""Create and initialise a specific command."""
		self.Name = name
		self.Comment = comment

	def _set_name(self, name):
		"""Set the the command."""
		self._name = name

	def _get_name(self):
		"""Return the command."""
		return self._name

	def _set_comment(self, comment=""):
		"""Set the comment of the command."""
		self._comment = comment

	def _get_comment(self):
		"""Return the comment of the command."""
		return self._comment

	def __str__(self):
		"""Return the command as a string."""
		return self.Name

	Name = property(_get_name, _set_name)
	Comment = property(_get_comment, _set_comment)
