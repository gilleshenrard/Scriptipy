from .osspecific import *

class Package(OSSpecific):
	"""Creates a package"""
	def __init__(self, name="", action="", option="", os=OSSpecifications()):
		OSSpecific.__init__(self, name, action, option, os)

	def __str__(self):
		act=self.OS.Options[self.Action]
		return "{} {} {} {}".format(self.OS.PackageManager, act, self.Options, self.Name)
