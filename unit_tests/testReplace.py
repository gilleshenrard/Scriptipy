from commands.replace import *
import unittest

class testReplace(unittest.TestCase):
	"""Test Case to test out Replace"""
	def setUp(self):
		"""Initialise test variables"""
		self.r=Replace("fileName", "This is an old line", "This is a new line")

    #
    #	TEST CONSTRUCTOR
    #
	def test_Constructor_Correct_ShouldNotFail(self):
		"""Test correct values for constructor (should not fail)"""
		try:
			r2=Replace("fileName", "This is an old line", "This is a new line")
			self.assertEqual(r2.OldLine, "This is an old line")
		except:
			self.fail("Correct Constructor values assignment failed!")

    #
    #	TEST OLDLINE PROPERTY
    #
	def test_OldLine_Correct_ShouldNotFail(self):
		"""Test correct values for OldLine (should not fail)"""
		try:
			self.r.OldLine="This other old line"
			self.assertEqual(self.r.OldLine, "This other old line")
		except:
			self.fail("Correct OldLine values assignment failed!")

	#
	# TEST __STR__
	#
	def test_str_Final_ShouldNotFail(self):
		"""Test if final result is the one expected"""
		self.assertEqual(str(self.r), "sed -i 's/This is an old line/This is a new line/g' fileName")