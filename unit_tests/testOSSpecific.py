from unit_tests.osspecific_notabstract import *
import unittest

class testOSSpecific(unittest.TestCase):
	"""Test Case to test out OSSpecific"""
#
#	INITIALIZATION
#
	def setUp(self):
		"""Initialise test variables"""
		self.o=OSSpecificNotAbstract(name="test", act="doTest", opt="-l", os=OSSpecifications())
#
#	TEST CONSTRUCTOR
#
	def test_Instanciation_Abstract_RaisesTypeError(self):
		"""Test correct values for Command constructor"""
		with self.assertRaises(TypeError):
			o2=OSSpecific()

	def test_CorrectValuesContructor_ShouldNotFail(self):
		"""Test correct values for Command constructor"""
		try:
			o2=OSSpecificNotAbstract(name="test2", act="doTest2", opt="-la", os=OSSpecifications())
		except:
			self.fail("Test for correct Constructor values assignment failed!")
#
#	TEST OPTIONS PROPERTY
#
	def test_CorrectOptions_ShouldNotFail(self):
		"""Test correct name value for Command"""
		try:
			self.o.Options="ls -l"
		except:
			self.fail("Test for correct Options assignment failed!")
#
#	TEST ACTION PROPERTY
#
	def test_CorrectAction_ShouldNotFail(self):
		"""Test correct comment value for Command"""
		try:
			self.o.Action="Some Action"
		except:
			self.fail("Test for correct Action assignment failed!")
#
#	TEST OS PROPERTY
#
	def test_CorrectOS_ShouldNotFail(self):
		"""Test correct comment value for Command"""
		try:
			self.o.OS=OSSpecifications(name="Ubuntu", pacman="apt-get", opt={"install":"install", "remove":"remove"})
		except:
			self.fail("Test for correct OS assignment failed!")
