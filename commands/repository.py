from .osspecific import *

class Repository(OSSpecific):
	"""Repository action command, based on the information provided into the OSGear object

    :param name: Name of the repository
    :param action: Action to perform with the repository (into OS dictionnary)
    :param option: Additionnal options of the repository command
    :param os: OS specific characteristics (OSGear object)"""

	def __init__(self, name="", comment="", act="", opt="", os=OSGear()):
		"""Declare and initialise a repository action command."""
		OSSpecific.__init__(self, name, comment, act, opt, os)

	def __str__(self):
		"""Return a repository action command as a string."""
		return "{} {} {}".format(self.Action, self.Options, self.Name)
