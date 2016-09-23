from data.datatype import *
from .not_abstract.datatype_notabstract import *
import unittest

class testDataType(unittest.TestCase):
	"""Test Case to test out DataType"""
#
#	INITIALIZATION
#
	def setUp(self):
		"""Initialise test variables"""
		self.d=DataTypeNotAbstract("test")
#
#	TEST CONSTRUCTOR
#
	def test_Instanciation_Abstract_RaisesTypeError(self):
		"""Test correct values for Command constructor"""
		with self.assertRaises(TypeError):
			d2=DataType()

	def test_CorrectValuesContructor_ShouldNotFail(self):
		"""Test correct values for Command constructor"""
		try:
			d2=DataTypeNotAbstract("test2")
		except:
			self.fail("Test for correct Constructor values assignment failed!")
#
#	TEST SOURCE PROPERTY
#
	def test_CorrectSource_ShouldNotFail(self):
		"""Test correct name value for Source"""
		try:
			self.d.Source="test"
		except:
			self.fail("Test for correct Source assignment failed!")