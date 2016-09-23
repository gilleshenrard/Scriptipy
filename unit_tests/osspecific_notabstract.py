from commands.osspecific import *

class OSSpecificNotAbstract(OSSpecific):
	def __init__(self, name="", act="", opt="", os=OSGear()):
		OSSpecific.__init__(self, name, act, opt, os)

	def __str__(self):
		pass
