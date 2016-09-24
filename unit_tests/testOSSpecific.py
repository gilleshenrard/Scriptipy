from .not_abstract.osspecific_notabstract import *
from commands.osspecific import *
import unittest

class testOSSpecific(unittest.TestCase):
	"""Test Case to test out OSSpecific"""

	#
	#	INITIALIZATION
	#
	def setUp(self):
		"""Initialise test variables"""
		self.o=OSSpecificNotAbstract(name="test", act="", opt="-l", os=OSGear())

	#
	#	TEST CONSTRUCTOR
	#
	def test_Instanciation_Abstract_RaisesTypeError(self):
		"""Test correct values for OSSpecific constructor (raises TypeError)"""
		with self.assertRaises(TypeError):
			o2=OSSpecific()

	def test_Contructor_Correct_ShouldNotFail(self):
		"""Test correct values for OSSpecific constructor (should not fail)"""
		try:
			o2=OSSpecificNotAbstract(name="test2", act="", opt="-la", os=OSGear())
			self.assertEqual(o2.Action, "")
			self.assertEqual(o2.Options, "-la")
		except:
			self.fail("Test for correct Constructor values assignment failed!")

	#
	#	TEST OPTIONS PROPERTY
	#
	def test_Options_Correct_ShouldNotFail(self):
		"""Test correct Options value for OSSpecific (should not fail)"""
		try:
			self.o.Options="-l"
			self.assertEqual(self.o.Options, "-l")
		except:
			self.fail("Test for correct Options assignment failed!")

	#
	#	TEST ACTION PROPERTY
	#
	def test_Action_Correct_ShouldNotFail(self):
		"""Test correct Action value for OSSpecific (should not fail)"""
		try:
			self.o.OS.Features["Some Action"]="test"
			self.o.Action="Some Action"
			self.assertEqual(self.o.Action, "test")
		except:
			self.fail("Test for correct Action assignment failed!")

	def test_Action_Wrong_RaisesValueError(self):
		"""Test wrong values for Action setter (raises ValueError)"""
		with self.assertRaises(ValueError):
			self.o.Action="Wrong Action"

	#
	#	TEST OS PROPERTY
	#
	def test_OS_Correct_ShouldNotFail(self):
		"""Test correct OS value for OSSpecific (should not fail)"""
		try:
			#Assignment testing. See OSGear testing for further information
			self.o.OS=OSGear(name="Ubuntu", pacman="apt-get", opt={"install":"install", "remove":"remove"})
		except:
			self.fail("Test for correct OS assignment failed!")
