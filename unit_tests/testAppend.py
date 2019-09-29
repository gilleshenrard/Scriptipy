from commands.append import *
import unittest

class testAppend(unittest.TestCase):
	"""Test Case to test out Append"""

	#
	#	TEST INITIALISATION
	#
	def setUp(self):
		"""Declare an Append test object with correct values (should not fail).
		Test each given values."""
		self.a=Append("FileName", "This is a new line")

	#
	#	TEST VALUES
	#
	def test_NewLine_ShouldNotFail(self):
		"""Test correct value set to the new line value for an append action"""
		self.assertEqual(self.a.NewLine, "This is a new line")

	#
    #	TEST NEWLINE PROPERTY
    #
	def test_NewLine_Correct_ShouldNotFail(self):
		"""Test correct values for NewLine (should not fail)"""
		self.a.NewLine="This other new line"
		self.assertEqual(self.a.NewLine, "This other new line")

	#
	# TEST __STR__
	#
	def test_str_Final_ShouldNotFail(self):
		"""Test if final result is the one expected"""
		self.assertEqual(str(self.a), 'echo "This is a new line" >> FileName')
