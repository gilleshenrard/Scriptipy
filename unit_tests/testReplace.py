from libs.replace import *
import unittest

class testReplace(unittest.TestCase):
	"""Test Case to test out Replace"""
	def setUp(self):
		"""Initialise test variables"""
		self.r=Replace()
#
#	TEST CONSTRUCTOR
#
	def test_CorrectValues_Constructor_ShouldNotFail(self):
		"""Test correct values for constructor"""
		try:
			r2=Replace("fileName", "This is an old line", "This is a new line")
		except:
			self.fail("Correct Constructor values assignment failed!")
#
#	TEST OLDLINE PROPERTY
#
	def test_CorrectValues_OldLine_ShouldNotFail(self):
		"""Test correct values for OldLine"""
		try:
			self.r.OldLine="This other old line"
		except:
			self.fail("Correct OldLine values assignment failed!")
