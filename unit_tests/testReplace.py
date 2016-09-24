from commands.replace import *
import unittest

class testReplace(unittest.TestCase):
	"""Test Case to test out Replace"""
	def setUp(self):
		"""Initialise test variables"""
		self.r=Replace()

    #
    #	TEST CONSTRUCTOR
    #
	def test_Constructor_Correct_ShouldNotFail(self):
		"""Test correct values for constructor (should not fail)"""
		try:
			r2=Replace("fileName", "This is an old line", "This is a new line")
		except:
			self.fail("Correct Constructor values assignment failed!")

    #
    #	TEST OLDLINE PROPERTY
    #
	def test_OldLine_Correct_ShouldNotFail(self):
		"""Test correct values for OldLine (should not fail)"""
		try:
			self.r.OldLine="This other old line"
		except:
			self.fail("Correct OldLine values assignment failed!")
