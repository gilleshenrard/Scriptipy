from data.XMLdata import *
import unittest

class testXMLData(unittest.TestCase):
	"""Test Case to test out XMLdata"""

	#
	#	TEST INITIALISATION
	#
	def setUp(self):
		"""Declare a XMLData test object with correct values (should not fail).
		Test each given values."""
		self.x=XMLdata("filename")
		self.assertEqual(self.x.Source, "filename")