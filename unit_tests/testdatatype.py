from data.datatype import *
from .not_abstract.datatype_notabstract import *
import unittest

class testDataType(unittest.TestCase):
	"""Test Case to test out DataType"""

	#
	#	TEST INITIALISATION
	#
	def setUp(self):
		"""Declare a DataTypeNotAbstract test object with correct values (should not fail).
		Test each given values."""
		self.d=DataTypeNotAbstract("test")

	#
	#	TEST VALUES
	#
	def test_Source_ShouldNotFail(self):
		"""Test correct value set to the source file for a generic data type"""
		self.assertEqual(self.d.Source, "test")

	#
	#	TEST CONSTRUCTOR
	#
	def test_Instanciation_Abstract_RaisesTypeError(self):
		"""Test instanciation of abstract DataType (raises TypeError)"""
		with self.assertRaises(TypeError):
			d2=DataType()

	#
	#	TEST SOURCE PROPERTY
	#
	def test_Source_Correct_ShouldNotFail(self):
		"""Test correct Source value (should not fail)"""
		self.d.Source="test2"
		self.assertEqual(self.d.Source, "test2")