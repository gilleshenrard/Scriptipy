from .osspecific import *

class Repository(OSSpecific):
	"""Defines the behaviour to handle a repository"""
	def __init__(self, name="", act="", opt="", os=OSSpecifications()):
		"""Defines an action on a repository"""
		OSSpecific.__init__(self, name, act, opt, os)

	def __str__(self):
		act=self.OS.Options[self.Action]
		return "{} {} {}".format(act, self.Options, self.Name)
