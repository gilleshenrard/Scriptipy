from commands.package import *
import unittest

class testPackage(unittest.TestCase):
	"""Test Case to test out Package"""
	def setUp(self):
		"""Initialise test variables"""
		pass

	#
	#	TEST CONSTRUCTOR
	#
	def test_Constructor_Correct_ShouldNotFail(self):
		"""Test correct values for Package constructor (should not fail)"""
		try:
			os = OSGear("ubuntu", "apt-get")
			os.Features["install"]="install"
			test = Package("python", "Installs python", "install", "-y", os)
		except:
			self.fail("Test for correct values assignment into Package failed!")
