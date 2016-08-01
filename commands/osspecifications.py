class OSSpecifications:
	"""Defines specifications for different OSes"""

	def __init__(self, name="", pacman="", opt={}):
		self.Name = name
		self.PackageManager = pacman
		self.Options = opt

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

	def __str__(self):
		return "OS : {}, package manager : {}, predefined options : {}".format(self._name, self._packageManager, self._specificOptions)

	Name = property(_get_name, _set_name)
	PackageManager = property(_get_packageManager, _set_packageManager)
	Options = property(_get_specificOptions, _set_specificOptions)
