from data.datatype import *
import unittest

class testDataType(unittest.TestCase):
	def test_Instanciation_RaisesTypeError(self):
		with self.assertRaises(TypeError):
			self.d=DataType()
