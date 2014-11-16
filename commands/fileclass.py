from command import *
import abc

class File(Command):
	"""Abstract base class to handle files
	Defines :
	NewLine : New line to output to a file"""

	__metaclass__  = abc.ABCMeta

	def __init__(self, name="", newline=""):
		Command.__init__(self, name)
		self._newLine = newline

	def _get_newLine(self):
		return self._newLine

	def _set_newLine(self, newline):
		self._newLine = newline

	@abc.abstractmethod
	def prepareCommand(self):
		"""trying to make File abstract by making prepareCommand abstract"""

	NewLine = property(_get_newLine, _set_newLine)
