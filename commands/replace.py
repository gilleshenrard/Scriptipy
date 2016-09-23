from .append import *

class Replace(Append):
	"""Command to replace a line by another in a file
	
	:param name : File name
	:param oldLine : Line to replace in the file
	:param newline : New value of the line

	Note:
	Uses built-in 'sed' command, will work on every UNIX based distribution."""

	def __init__(self, name="", oldline="", newline=""):
		"""Create and initialise a line replacement command."""
		Append.__init__(self, name, newline)
		self.OldLine = oldline

	def _set_oldLine(self, oldline):
		"""Set the old line to be replaced."""
		self._oldLine = oldline

	def _get_oldLine(self):
		"""Return the old line to be replaced."""
		return self._oldLine

	def __str__(self):
		"""Return the line replacement command as a string."""
		return "sed -i 's/{}/{}/g' {}".format(self.OldLine, self.NewLine, self.Name)

	OldLine = property(_get_oldLine, _set_oldLine)
