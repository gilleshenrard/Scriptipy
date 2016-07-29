from libs.append import *
import unittest

class testAppend(unittest.TestCase):
	"""Test Case to test out Append"""
	def setUp(self):
		"""Initialise test variables"""
		self.a=Append()
#
#	TEST CONSTRUCTOR
#
	def test_CorrectValues_Constructor_ShouldNotFail(self):
		"""Test correct values for constructor"""
		try:
			a2=Append("fileName", "This is a new line")
			print(a2)
		except:
			self.fail("Correct Constructor values assignment failed!")
#
#	TEST NEWLINE PROPERTY
#
	def test_CorrectValues_NewLine_ShouldNotFail(self):
		"""Test correct values for NewLine"""
		try:
			self.a.NewLine="This other new line"
			print(self.a)
			print(self.a.NewLine)
		except:
			self.fail("Correct NewLine values assignment failed!")
