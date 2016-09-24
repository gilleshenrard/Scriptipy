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
	def test_Contructor_Correct_ShouldNotFail(self):
		"""Test correct values for Command constructor (should not fail)"""
		try:
			c2=Command("top", "Prints a real time list of processes")
			self.assertEqual(c2.Name, "top")
			self.assertEqual(c2.Comment, "Prints a real time list of processes")
		except:
			self.fail("Test for correct Constructor values assignment failed!")

    #
    #	TEST NAME PROPERTY
    #
	def test_Name_Correct_ShouldNotFail(self):
		"""Test correct name value for Command (should not fail)"""
		try:
			self.c.Name="ls -l"
			self.assertEqual(self.c.Name, "ls -l")
		except:
			self.fail("Test for correct Name assignment failed!")

    #
    #	TEST COMMENT PROPERTY
    #
	def test_Comment_Correct_ShouldNotFail(self):
		"""Test correct comment value for Command (should not fail)"""
		try:
			self.c.Comment="Some comment"
			self.assertEqual(self.c.Comment, "Some comment")
		except:
			self.fail("Test for correct Comment assignment failed!")
