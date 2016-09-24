from data.XMLdata import *
import unittest

class testXMLData(unittest.TestCase):
	"""Test Case to test out XMLdata"""
	def setUp(self):
		"""Initialise test variables"""
		self.x=XMLdata("test")

	#
	#	TEST CONSTRUCTOR
	#
	def test_Constructor_Correct_ShouldNotFail(self):
		"""Test correct values for XMLData constructor (should not fail)."""
		try:
			x2=XMLdata("fileName")
		except:
			self.fail("Correct Constructor values assignment failed!")