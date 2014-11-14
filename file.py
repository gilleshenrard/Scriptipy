import abc

class File(Command):
	"""Base class to handle files"""
	
	__metaclass__  = abc.ABCMeta

	def __init__(self):
		Command.__init__(self)
		self._newLine = ""

	def __init__(self, name):
		Command.__init__(self, name)
		self._newLine = ""

	def __init__(self, name, newline)
		Command.__init__(self, name, comment)
		self._newLine = newline

	def _get_newLine(self):
		return self.newLine

	def _set_newLine(self, newline):
		self._newLine = newline
		
	@abc.abstractmethod
	def prepareCommand(self):
		"""trying to make File abstract by making prepareCommand abstract"""

	newLine = property(_get_newLine, set_newLine)
	
