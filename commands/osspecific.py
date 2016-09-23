import abc
from .command import *
from .osspecifications import *

class OSSpecific(Command, metaclass=abc.ABCMeta):
	"""Defines the base class to handle OS specific commands (packages, repos, ...)"""

	def __init__(self, name="", act="", opt="", os=OSSpecifications()):
		Command.__init__(self, name)
		self.Options = opt
		self.OS = os
		self.Action = act

	def _set_options(self, opt=""):
		self._options = opt

	def _get_options(self):
		return self._options

	def _set_action(self, act=""):
		if act in self.OS.Options.keys():
			tmp=self._OS.Options[act]
			self._action = tmp
		else:
			raise ValueError("Action '{}' not found for the operating system {}".format(act, self._OS.Name))

	def _get_action(self):
		return self._action

	def _set_OS(self, osspec):
		self._OS = osspec

	def _get_OS(self):
		return self._OS

	@abc.abstractmethod
	def __str__(self):
		pass

	Options = property(_get_options, _set_options)
	Action = property(_get_action, _set_action)
	OS = property(_get_OS, _set_OS)
