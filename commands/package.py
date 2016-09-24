from .osspecific import *

class Package(OSSpecific):
	"""Package action command, based on the information provided into the OSGear object

    :param name: Name of the package
    :param action: Action to perform with the package (into OS dictionnary)
    :param option: Additionnal options of the package command
    :param os: OS specific characteristics (OSGear object)"""

	def __init__(self, name="", comment="", action="", option="", os=OSGear()):
		"""Declare and initialise a package action command."""
		OSSpecific.__init__(self, name, comment, action, option, os)

	def __str__(self):
		"""Return a package action command as a string."""
		return "{} {} {} {}".format(self.OS.PackageManager, self.Action, self.Options, self.Name)
