from commands.command import *
import unittest

class testCommand(unittest.TestCase):
	"""Test Case to test out raw Commands"""
	def setUp(self):
		"""Initialise test variables"""
		self.c=Command()
#
#	TEST CONSTRUCTOR
#
	def test_CorrectValuesContructor_ShouldNotFail(self):
		"""Test correct values for Command constructor"""
		try:
			c2=Command("top", "Prints a real time list of processes")
		except:
			self.fail("Test for correct Constructor values assignment failed!")
#
#	TEST NAME PROPERTY
#
	def test_CorrectName_ShouldNotFail(self):
		"""Test correct name value for Command"""
		try:
			self.c.Name="ls -l"
		except:
			self.fail("Test for correct Name assignment failed!")
#
#	TEST COMMENT PROPERTY
#
	def test_CorrectComment_ShouldNotFail(self):
		"""Test correct comment value for Command"""
		try:
			self.c.Comment="Some comment"
		except:
			self.fail("Test for correct Comment assignment failed!")
