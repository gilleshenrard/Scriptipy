from libs.package import *
import unittest

class testPackage(unittest.TestCase):
	"""Test Case to test out Package"""
	def setUp(self):
		"""Initialise test variables"""
		pass
#
#	TEST CONSTRUCTOR
#
	def test_Correct_Constructor_ShouldNotFail(self):
		"""Test correct values for constructor"""
		try:
			os = OSSpecifications("ubuntu", "apt-get")
			os.Options["install"]="install"
			test = Package("python", "install", "-y", os)
		except:
			self.fail("Test for correct values assignment into Package failed!")
