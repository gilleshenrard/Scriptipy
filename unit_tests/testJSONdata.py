from data.jsondata import *
import unittest

class testJSONData(unittest.TestCase):
	"""Test Case to test out JSDONData"""
	def setUp(self):
		"""Initialise test variables"""
		self.j=JSONData("unit_tests/test_files/jsontestdata.txt")

	#
	#	TEST CONSTRUCTOR
	#
	def test_Constructor_Correct_ShouldNotFail(self):
		"""Test correct values for constructor in JSDONData (should not fail)."""
		try:
			j2=JSONData("fileName")
		except:
			self.fail("Correct Constructor values assignment failed!")

	#
	#	TEST DESERIALIZATION
	#
	def test_Deserialization_Correct_ShouldNotFail(self):
		"""Test correct deserialisation process (should not fail)."""
		try:
			data=self.j.deserialize()
			self.assertEqual(data, [{"eyes": "blue","name": "John","surname": "Doe"},34,"Test"])
		except:
			self.fail("Correct deserialization values failed!")

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
		try:
			data=[{"eyes": "green","name": "John","surname": "Smith"},35,"Test2"]
			self.j.Source="unit_tests/test_files/jsontestdata2.txt"
			self.j.serialize(data)
		except:
			self.fail("Correct serialization values failed!")
