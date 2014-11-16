import abc

class Scriptable(metaclass=abc.ABCMeta) :
	"""Defines basic characteristics, such as name and comment.
	Can't be instanciated.
	Defined by a name and a comment"""

	def __init__(self, name="", comment=""):
		self._name = name
		self._comment = comment

	def _set_name(self, name):
		self._name = name

	def _get_name(self):
		return self._name

	def _set_comment(self, comment):
		self._comment = comment

	def _get_comment(self):
		return self._comment

	@abc.abstractmethod
	def __str__(self):
		"""will return comment"""

	Name = property(_get_name, _set_name)
	Comment = property(_get_comment, _set_comment)

if __name__ == "__main__":
	test=Scriptable()
