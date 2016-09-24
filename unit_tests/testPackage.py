from commands.package import *
import unittest

class testPackage(unittest.TestCase):
	"""Test Case to test out Package"""

	#
	#	TEST INITIALISATION
	#
	def setUp(self):
		"""Declare a Package test object with correct values (should not fail).
		Test each given values."""
		os = OSGear("ubuntu", "apt-get", {"Installation" : "install"})
		self.p = Package("python", "Installs python", "Installation", "-y", os)

	#
	# TEST __STR__
	#
	def test_str_Final_ShouldNotFail(self):
		"""Test if final result is the one expected"""
		self.assertEqual(str(self.p), "apt-get install -y python")