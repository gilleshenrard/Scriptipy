import abc

class DataType(metaclass=abc.ABCMeta):
	"""Defines the interface for data types (XML, plain text files, databases)"""

	def __init__(self, source=""):
		"""Builds a data type"""
		self.Source=source

	def _get_source(self):
		return self._source

	def _set_source(self, source):
		self._source=source

	@abc.abstractmethod
	def deserialize(self):
		"""Defines the method to implement and by which we will recover all the data from the file"""

	@abc.abstractmethod
	def serialize(self, data):
		pass


	Source=property(_get_source, _set_source)