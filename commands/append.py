from .command import *

class Append(Command):
	"""Command to append a line in a file
	
	:param name : File name
	:param newline : Line to append to the file

	Note:
	Uses built-in 'echo' command, will work on every UNIX based distribution."""

	def __init__(self, name="", newline=""):
		"""Create and initialise a line appending command."""
		Command.__init__(self, name)
		self.NewLine = newline

	def _get_newLine(self):
		"""Return the line to append."""
		return self._newLine

	def _set_newLine(self, newline):
		"""Set the line to append."""
		self._newLine = newline

	def __str__(self):
		"""Return the line appending command as a string."""
		return "echo {} >> {}".format(self.NewLine, self.Name)

	NewLine = property(_get_newLine, _set_newLine)
