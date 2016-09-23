from data.jsondata import *
import unittest

class testJSONData(unittest.TestCase):
	"""Test Case to test out Append"""
	def setUp(self):
		"""Initialise test variables"""
		self.j=JSONData("unit_tests/jsontestdata.txt")
#
#	TEST CONSTRUCTOR
#
	def test_CorrectValues_Constructor_ShouldNotFail(self):
		"""Test correct values for constructor"""
		try:
			j2=JSONData("fileName")
		except:
			self.fail("Correct Constructor values assignment failed!")
#
#	TEST FILENAME PROPERTY
#
	def test_CorrectValues_NewLine_ShouldNotFail(self):
		"""Test correct values for NewLine"""
		try:
			self.j.Source="This other new line"
		except:
			self.fail("Correct FileName values assignment failed!")
#
#	TEST DESERIALIZATION
#
	def test_Deserialization_Correct_ShouldNotFail(self):
		try:
			data=self.j.deserialize()
			self.assertEqual(data, [{"eyes": "blue","name": "John","surname": "Doe"},34,"Test"])
		except:
			self.fail("Correct deserialization values failed!")

	def test_Deserialization_FileDoesNotExist_RaisesValueError(self):
		with self.assertRaises(ValueError):
			self.j.Source="filedoesnotexist.txt"
			self.j.deserialize()
#
#	TEST SERIALIZATION
#
	def test_Serialization_Correct_ShouldNotFail(self):
		try:
			data=[{"eyes": "green","name": "John","surname": "Smith"},35,"Test2"]
			self.j.Source="unit_tests/jsontestdata2.txt"
			self.j.serialize(data)
		except:
			self.fail("Correct serialization values failed!")
