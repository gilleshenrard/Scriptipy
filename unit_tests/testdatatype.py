from data.datatype import *
from .not_abstract.datatype_notabstract import *
import unittest

class testDataType(unittest.TestCase):
	"""Test Case to test out DataType"""

	#
	#	INITIALIZATION
	#
	def setUp(self):
		"""Initialise test variables."""
		self.d=DataTypeNotAbstract("test")

	#
	#	TEST CONSTRUCTOR
	#
	def test_Instanciation_Abstract_RaisesTypeError(self):
		"""Test instanciation of abstract DataType (raises TypeError)"""
		with self.assertRaises(TypeError):
			d2=DataType()

	def test_Contructor_Correct_ShouldNotFail(self):
		"""Test correct values for DataType constructor (abstraction removed, should not fail)"""
		try:
			d2=DataTypeNotAbstract("test2")
		except:
			self.fail("Test for correct Constructor values assignment failed!")

	#
	#	TEST SOURCE PROPERTY
	#
	def test_Source_Correct_ShouldNotFail(self):
		"""Test correct Source value (should not fail)"""
		try:
			self.d.Source="test"
		except:
			self.fail("Test for correct Source assignment failed!")