from osspecific import *

class Repository(OSSpecific):
	"""Defines the behaviour to handle a repository"""

	def __init__(self, name="", act="", opt=""):
		"""Defines an action on a repository"""

		OSSpecific.__init__(self, name, act, opt)

	def prepareCommand(self):
		act=self.OS.getOption(self.Action)
		self.Final="{} {} {}".format(act, self.Options, self.Name)

	def __str__(self):
		return "Adding repository {}".format(self.Name)

if __name__ == "__main__":
	test = Repository("some PPA", "Add", "-y")
	os = OSSpecifications("ubuntu", "apt-get", {"Add": "add-apt-repository"})
	test.OS = os
	print(test.Name)
	print(test.Action)
	print(test.Final)
	print(test)
