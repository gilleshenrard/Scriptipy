from scriptable import *

class Action(Scriptable):
	"""Defines a set of related commands, sorted in pre-action, action and post-action"""

	def __init__(self, name="", comment=""):
		"""Builds an empty action"""

		Scriptable.__init__(self, name, comment)
		self._preAction=[]
		self._actualAction=[]
		self._postAction=[]

	def _get_preAction(self):
		return self._preAction

	def _set_preAction(self, pro=[]):
		self._preAction = pro

	def _get_actualAction(self):
		return self._actualAction

	def _set_actualAction(self, pro=[]):
		self._actualAction = pro

	def _get_postAction(self):
		return self._postAction

	def _set_postAction(self, pro=[]):
		self._postAction = pro

	def __str__(self):
		return "Executing the action for {}".format(self.Name)

	PreAction = property(_get_preAction, _set_preAction)
	ActualAction = property(_get_actualAction, _set_actualAction)
	PostAction = property(_get_postAction, _set_postAction)

if __name__ == "__main__":
	test = Action("git", "Configuring git")
	test.PreAction.append("some stuff")
	test.ActualAction = ["stuff", "otherstuff"]
	print(test)
	print(test.PreAction)
	print(test.ActualAction)
	print(test.PostAction)
	print(test.Comment)
