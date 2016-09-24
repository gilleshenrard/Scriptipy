from commands.package import *
import unittest

class testPackage(unittest.TestCase):
	"""Test Case to test out Package"""
	def setUp(self):
		"""Initialise test variables"""
		os = OSGear("ubuntu", "apt-get", {"install" : "install"})
		self.p = Package("python", "Installs python", "install", "-y", os)
		pass

	#
	#	TEST CONSTRUCTOR
	#
	def test_Constructor_Correct_ShouldNotFail(self):
		"""Test correct values for Package constructor (should not fail)"""
		try:
			os = OSGear("ubuntu", "apt-get", {"install" : "install"})
			test = Package("python", "Installs python", "install", "-y", os)
		except:
			self.fail("Test for correct values assignment into Package failed!")

	#
	# TEST __STR__
	#
	def test_str_Final_ShouldNotFail(self):
		"""Test if final result is the one expected"""
		self.assertEqual(str(self.p), "apt-get install -y python")