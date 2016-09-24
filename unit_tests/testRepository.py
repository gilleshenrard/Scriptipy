from commands.repository import *
import unittest

class testRepository(unittest.TestCase):
	"""Test Case to test out Repository"""
	def setUp(self):
		"""Initialise test variables"""
		os = OSGear("ubuntu", "apt-get", {"Add": "add-apt-repository"})
		self.r=Repository("some PPA", "Adds a PPA", "Add", "-y", os)

	#
	#	TEST CONSTRUCTOR
	#
	def test_Constructor_Correct_ShouldNotFail(self):
		"""Test correct values for constructor (should not fail)"""
		try:
			os = OSGear("ubuntu", "apt-get", {"Add": "add-apt-repository"})
			r=Repository("some PPA", "Adds a PPA", "Add", "-y", os)
		except:
			self.fail("Test for correct values assignment into Repository failed!")

	#
	# TEST __STR__
	#
	def test_str_Final_ShouldNotFail(self):
		"""Test if final result is the one expected"""
		self.assertEqual(str(self.r), "add-apt-repository -y some PPA")