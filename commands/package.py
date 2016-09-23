from .osspecific import *

class Package(OSSpecific):
	"""Creates a package"""
	def __init__(self, name="", action="", option="", os=OSSpecifications()):
		OSSpecific.__init__(self, name, action, option, os)

	def __str__(self):
		return "{} {} {} {}".format(self.OS.PackageManager, self.Action, self.Options, self.Name)
