from data.jsondata import *
import unittest

class testJSONData(unittest.TestCase):
	"""Test Case to test out JSDONData"""

	#
	#	TEST INITIALISATION
	#
	def setUp(self):
		"""Declare a JSONData test object with correct values (should not fail).
		Test each given values."""
		self.j=JSONData("unit_tests/test_files/jsontestdata.txt")
		self.assertEqual(self.j.Source, "unit_tests/test_files/jsontestdata.txt")

	#
	#	TEST DESERIALIZATION
	#
	def test_Deserialization_Correct_ShouldNotFail(self):
		"""Test correct deserialisation process (should not fail)."""
		data=self.j.deserialize()
		self.assertEqual(data, [{"eyes": "blue","name": "John","surname": "Doe"},34,"Test"])

	def test_Deserialization_FileDoesNotExist_RaisesValueError(self):
		"""Test deserialisation from a file which doesn*t exist (raises ValueError)."""
		with self.assertRaises(ValueError):
			self.j.Source="filedoesnotexist.txt"
			self.j.deserialize()

	#
	#	TEST SERIALIZATION
	#
	def test_Serialization_Correct_ShouldNotFail(self):
		"""Test correct serialisation process (should not fail)."""
		data=[{"eyes": "green","name": "John","surname": "Smith"},35,"Test2"]
		self.j.Source="unit_tests/test_files/jsontestdata2.txt"
		self.j.serialize(data)
