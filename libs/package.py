from osspecific import *

class Package(OSSpecific):

	def __init__(self, name="", action="", option=""):
		OSSpecific.__init__(self, name, action, option)

	def prepareCommand(self):
		act=self.OS.getOption(self.Action)
		self.Final = "{} {} {} {}".format(self.OS.PackageManager, act, self.Options, self.Name)

	def __str__(self):
		act=self.OS.getOption(self.Action)
		return "{} {} {} {}".format(self.OS.PackageManager, act, self.Options, self.Name)

if __name__ == "__main__":
	os = OSSpecifications("ubuntu", "apt-get")
	os.addOption("install", "install")
	test = Package("python", "install", "-y")
	test.OS=os
	print(test.Name)
	print(test.Action)
	print(test.OS)
	print(test)

	os = OSSpecifications("archlinux", "pacman")
	os.editOption("install", "-S")
	test = Package("python", "install")
	test.OS=os
	print(test.Name)
	print(test.Action)
	print(test.OS)
	print(test)
