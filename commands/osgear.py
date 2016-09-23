class OSGear:
	"""Defines the characteristics specific to the operating system

	:param name: Name of the OS
	:param pacman: Package manager called by the OS
	:param opt: Dictionnary of the options used by the package manager (install, remove, list, ...)"""

	def __init__(self, name="", pacman="", opt={}):
		"""Define the OS characteristics."""
		self.Name = name
		self.PackageManager = pacman
		self.Features = opt

	def _set_name(self, name):
        """Set the OS name."""
		self._name = name

	def _get_name(self):
        """Return the OS name."""
		return self._name

	def _set_packageManager(self, pacman):
        """Set the package manager OS call."""
		self._packageManager = pacman

	def _get_packageManager(self):
        """Return the package manager OS call."""
		return self._packageManager

	def _set_features(self, opt):
        """Set the specific options used by the package manager (install, remove, list, ...)."""
		self._features = opt

	def _get_features(self):
        """Return the specific options used by the package manager."""
		return self._features

	def __str__(self):
        """Return a short report of the OS as a string."""
		return "OS : {}, package manager : {}, predefined options : {}".format(self._name, self._packageManager, self._features)

	Name = property(_get_name, _set_name)
	PackageManager = property(_get_packageManager, _set_packageManager)
	Features = property(_get_features, _set_features)
