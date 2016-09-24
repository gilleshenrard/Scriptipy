from commands.osspecific import *

class OSSpecificNotAbstract(OSSpecific):
	def __init__(self, name="", comment="", act="", opt="", os=OSGear()):
		OSSpecific.__init__(self, name, comment, act, opt, os)

	def __str__(self):
		pass
