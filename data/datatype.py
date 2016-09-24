import abc

class DataType(metaclass=abc.ABCMeta):
	"""Base class to handle commands (de)serialisation (JSON, XML, database, ...)

    :param source: Source of data (file/server/...)"""

	def __init__(self, source=""):
		"""Declare and initialise a command (de)serialisation process."""
		self.Source=source

	def _get_source(self):
		"""Get the source of the (de)serialisation."""
		return self._source

	def _set_source(self, source):
		"""Set the source of the (de)serialisation."""
		self._source=source

	@abc.abstractmethod
	def deserialize(self):
		"""Define the base deserialisation method."""
		pass

	@abc.abstractmethod
	def serialize(self, data):
		"""Define the base serialisation method."""
		pass

	Source=property(_get_source, _set_source)