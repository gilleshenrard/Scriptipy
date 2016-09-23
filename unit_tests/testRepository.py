from commands.repository import *
import unittest

class testRepository(unittest.TestCase):
	"""Test Case to test out Repository"""
	def setUp(self):
		"""Initialise test variables"""
		pass
#
#	TEST CONSTRUCTOR
#
	def test_Correct_Constructor_ShouldNotFail(self):
		"""Test correct values for constructor"""
		try:
			os = OSGear("ubuntu", "apt-get", {"Add": "add-apt-repository"})
			self.r=Repository("some PPA", "Add", "-y", os)
		except:
			self.fail("Test for correct values assignment into Repository failed!")
