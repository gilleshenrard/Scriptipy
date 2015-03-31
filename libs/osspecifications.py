#! /usr/bin/python
class OSSpecifications:
	"""Defines specifications for different OSes"""

	def __init__(self, name="", pacman="", opt={}):
		self._name = name
		self._packageManager = pacman
		self._specificOptions = opt

	def _set_name(self, name):
		self._name = name

	def _get_name(self):
		return self._name

	def _set_packageManager(self, pacman):
		self._packageManager = pacman

	def _get_packageManager(self):
		return self._packageManager

	def _set_specificOptions(self, opt):
		self._specificOptions = opt

	def _get_specificOptions(self):
		return self._specificOptions

	def addOption(self, key="", value=""):
		self._specificOptions[key]=value

	def getOption(self, key=""):
		return self._specificOptions[key]

	def delOption(self, key=""):
		removed=self._specificOptions.pop(key)
		return removed

	def __str__(self):
		return "OS : {}, package manager : {}, predefined options : {}".format(self._name, self._packageManager, self._specificOptions)

	Name = property(_get_name, _set_name)
	PackageManager = property(_get_packageManager, _set_packageManager)
	SpecificOptions = property(_get_specificOptions, _set_specificOptions)

if __name__ == "__main__":
	test = OSSpecifications("Ubuntu", "apt-get", {"update": "update"})
	print(test.Name)
	print(test.PackageManager)
	print(test.SpecificOptions)
	print(test.getOption("update"))
	test.addOption("remove", "remove")
	print(test.SpecificOptions)
	test.delOption("update")
	print(test.SpecificOptions)
	print(test)
	test2 = OSSpecifications("arch", "pacman")
	print(test2.SpecificOptions)
