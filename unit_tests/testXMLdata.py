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
		self.x=XMLdata("unit_tests/test_files/xmltestdata.xml")

	#
	#	TEST VALUES
	#
	def test_Source_ShouldNotFail(self):
		"""Test correct value set to the source file for XML data"""
		self.assertEqual(self.x.Source, "unit_tests/test_files/xmltestdata.xml")

	#
	# 	TEST DESERIALIZATION
	#
	def test_Deserialization_Correct_ShouldNotFail(self):
		"""Test correct deserialisation process (should not fail)."""
		self.x.deserialize()