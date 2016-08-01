from commands.osspecific import *
import unittest

class testOSSpecific(unittest.TestCase):
	"""Test Case to test out OSSpecific"""
#
#	TEST CONSTRUCTOR
#
	def test_Instanciation_Constructor_RaisesTypeError(self):
		"""Test instanciation for constructor"""
		with self.assertRaises(TypeError):
			os=OSSpecific()
