from commands.replace import *
import unittest

class testReplace(unittest.TestCase):
	"""Test Case to test out Replace"""

	#
	#	TEST INITIALISATION
	#
	def setUp(self):
		"""Declare a Replace test object with correct values (should not fail).
		Test each given values."""
		self.r=Replace("fileName", "This is an old line", "This is a new line")

	#
	#	TEST VALUES
	#
	def test_OldLine_ShouldNotFail(self):
		"""Test correct value set to the old line of a replace action"""
		self.assertEqual(self.r.OldLine, "This is an old line")

    #
    #	TEST OLDLINE PROPERTY
    #
	def test_OldLine_Correct_ShouldNotFail(self):
		"""Test correct values for OldLine (should not fail)"""
		self.r.OldLine="This other old line"
		self.assertEqual(self.r.OldLine, "This other old line")

	#
	# TEST __STR__
	#
	def test_str_Final_ShouldNotFail(self):
		"""Test if final result is the one expected"""
		self.assertEqual(str(self.r), "sed -i 's/This is an old line/This is a new line/g' fileName")