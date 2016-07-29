class OSSpecifications:
	"""Defines specifications for different OSes"""

	def __init__(self, name="", pacman="", opt={}):
		self.Name = name
		self.PackageManager = pacman
		self.Options = opt

	def _set_name(self, t_name):
		self._name = t_name

	def _get_name(self):
		return self._name

	def _set_packageManager(self, t_pacman):
		self._packageManager = t_pacman

	def _get_packageManager(self):
		return self._packageManager

	def _set_specificOptions(self, t_opt):
		self._specificOptions = t_opt

	def _get_specificOptions(self):
		return self._specificOptions

	def __str__(self):
		return "OS : {}, package manager : {}, predefined options : {}".format(self._name, self._packageManager, self._specificOptions)

	Name = property(_get_name, _set_name)
	PackageManager = property(_get_packageManager, _set_packageManager)
	Options = property(_get_specificOptions, _set_specificOptions)
