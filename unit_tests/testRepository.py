from commands.repository import *
import unittest

class testRepository(unittest.TestCase):
	"""Test Case to test out Repository"""

	#
	#	TEST INITIALISATION
	#
	def setUp(self):
		"""Declare a Repository test object with correct values (should not fail).
		Test each given values."""
		os = OSGear("ubuntu", "apt-get", {"Add": "add-apt-repository"})
		self.r=Repository("some PPA", "Adds a PPA", "Add", "-y", os)

	#
	# TEST __STR__
	#
	def test_str_Final_ShouldNotFail(self):
		"""Test if final result is the one expected"""
		self.assertEqual(str(self.r), "add-apt-repository -y some PPA")