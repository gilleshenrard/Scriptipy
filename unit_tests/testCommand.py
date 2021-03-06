from commands.command import *
import unittest

class testCommand(unittest.TestCase):
	"""Test Case to test out raw Commands"""

	#
	#	TEST INITIALISATION
	#
	def setUp(self):
		"""Declare a Command test object with correct values (should not fail).
		Test each given values."""
		self.c=Command("top", "Prints a real time list of processes")

	#
	#	TEST VALUES
	#
	def test_Values_ShouldNotFail(self):
		"""Test correct value set to the values of a command"""
		self.assertEqual(self.c.Name, "top")
		self.assertEqual(self.c.Comment, "Prints a real time list of processes")

    #
    #	TEST NAME PROPERTY
    #
	def test_Name_Correct_ShouldNotFail(self):
		"""Test correct name value for Command (should not fail)"""
		self.c.Name="ls -l"
		self.assertEqual(self.c.Name, "ls -l")

    #
    #	TEST COMMENT PROPERTY
    #
	def test_Comment_Correct_ShouldNotFail(self):
		"""Test correct comment value for Command (should not fail)"""
		self.c.Comment="Some comment"
		self.assertEqual(self.c.Comment, "Some comment")

	#
	# TEST __STR__
	#
	def test_str_Final_ShouldNotFail(self):
		"""Test if final result is the one expected"""
		self.assertEqual(str(self.c), "top")