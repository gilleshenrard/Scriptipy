from scriptable import *

class Process(Scriptable):
	"""Defines a set of related commands, sorted in pre-process, process and post-process"""

	def __init__(self, name="", comment=""):
		"""Builds an empty process"""

		Scriptable.__init__(self, name, comment)
		self._preProcess=[]
		self._actualProcess=[]
		self._postProcess=[]

	def _get_preProcess(self):
		return self._preProcess

	def _set_preProcess(self, pro=[]):
		self._preProcess = pro

	def _get_actualProcess(self):
		return self._actualProcess

	def _set_actualProcess(self, pro=[]):
		self._actualProcess = pro

	def _get_postProcess(self):
		return self._postProcess

	def _set_postProcess(self, pro=[]):
		self._postProcess = pro

	def __str__(self):
		return "Executing the process for {}".format(self.Name)

	PreProcess = property(_get_preProcess, _set_preProcess)
	ActualProcess = property(_get_actualProcess, _set_actualProcess)
	PostProcess = property(_get_postProcess, _set_postProcess)

if __name__ == "__main__":
	test = Process("git", "Configuring git")
	test.PreProcess.append("some stuff")
	test.Actualprocess = ["stuff", "otherstuff"]
	print(test)
	print(test.PreProcess)
	print(test.ActualProcess)
	print(test.PostProcess)
	print(test.Comment)
