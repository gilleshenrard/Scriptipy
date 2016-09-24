import abc
from .command import *
from .osgear import *

class OSSpecific(Command, metaclass=abc.ABCMeta):
	"""Base class to handle OS specific commands (packages, repositories, ...)

    :param name: Eventual name of the action pending
    :param comment: Comment about the action pending
    :param act: Action to execute (key into the OS dictionnary)
    :param opt: Additional options of the action pending
    :param os: OS specifications - OSGear object"""

	def __init__(self, name="", comment="", act="", opt="", os=OSGear()):
		"""Declare and initialise an OS specific action to process."""
		Command.__init__(self, name, comment)
		self.Options = opt
		self.OS = os
		self.Action = act

	def _set_options(self, opt=""):
		"""Set the additional options to apply to the action pending."""
		self._options = opt

	def _get_options(self):
		"""Return the additional options to apply to the action pending."""        
		return self._options

	def _set_action(self, act=""):
		"""Set the OS specific command to process.
		Search for the action into the OS dictionnary.
		Translate it to the value found.

		Exception:
		Raise a ValueError if the action is not found."""
		if act == "":
			self._action=""
		elif act in self.OS.Features.keys():
			tmp=self.OS.Features[act]
			self._action = tmp
		else:
			raise ValueError("Action '{}' not found for the operating system {}".format(act, self._OS.Name))

	def _get_action(self):
		"""Return the OS specific action pending (as stated into the OS dictionnary)."""
		return self._action

	def _set_OS(self, osspec):
		"""Set the OS specifications (OSGear object)."""
		self._OS = osspec

	def _get_OS(self):
		"""Return the OS specifications (OSGear object)."""
		return self._OS

	@abc.abstractmethod
	def __str__(self):
		pass

	Options = property(_get_options, _set_options)
	Action = property(_get_action, _set_action)
	OS = property(_get_OS, _set_OS)
