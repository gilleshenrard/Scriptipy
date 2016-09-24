from commands.append import *
import unittest

class testAppend(unittest.TestCase):
	"""Test Case to test out Append"""
	def setUp(self):
		"""Initialise test variables"""
		self.a=Append("FileName", "This is a new line")

    #
    #	TEST CONSTRUCTOR
    #
	def test_Constructor_Correct_ShouldNotFail(self):
		"""Test correct values for constructor (sould not fail)"""
		try:
			a2=Append("fileName", "This is a new line")
			self.assertEqual(a2.NewLine, "This is a new line")
		except:
			self.fail("Correct Constructor values assignment failed!")

    #
    #	TEST NEWLINE PROPERTY
    #
	def test_NewLine_Correct_ShouldNotFail(self):
		"""Test correct values for NewLine (should not fail)"""
		try:
			self.a.NewLine="This other new line"
			self.assertEqual(self.a.NewLine, "This other new line")
		except:
			self.fail("Correct NewLine values assignment failed!")

	#
	# TEST __STR__
	#
	def test_str_Final_ShouldNotFail(self):
		"""Test if final result is the one expected"""
		self.assertEqual(str(self.a), 'echo "This is a new line" >> FileName')
