import abc

class DataType(metaclass=abc.ABCMeta):
	"""Defines the interface for data types (XML, plain text files, databases)"""

	def __init__(self):
		"""Builds a data type"""
		pass

	@abc.abstractmethod
	def deserialize(self):
		"""Defines the method to implement and by which we will recover all the data from the file"""

	@abc.abstractmethod
	def serialize(self, data):
		pass
