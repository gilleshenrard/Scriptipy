from .not_abstract.osspecific_notabstract import *
from commands.osspecific import *
import unittest

class testOSSpecific(unittest.TestCase):
	"""Test Case to test out OSSpecific"""

	#
	#	TEST INITIALISATION
	#
	def setUp(self):
		"""Declare an OSSpecific test object with correct values (should not fail).
		Test each given values."""
		self.o=OSSpecificNotAbstract(name="test", act="", opt="-l", os=OSGear())
		self.assertEqual(self.o.Action, "")
		self.assertEqual(self.o.Options, "-l")

	#
	#	TEST CONSTRUCTOR
	#
	def test_Instanciation_Abstract_RaisesTypeError(self):
		"""Test initialisation of OSSpecific abstract constructor (raises TypeError)"""
		with self.assertRaises(TypeError):
			o2=OSSpecific()

	#
	#	TEST OPTIONS PROPERTY
	#
	def test_Options_Correct_ShouldNotFail(self):
		"""Test correct Options value for OSSpecific (should not fail)"""
		self.o.Options="-l"
		self.assertEqual(self.o.Options, "-l")

	#
	#	TEST ACTION PROPERTY
	#
	def test_Action_Correct_ShouldNotFail(self):
		"""Test correct Action value for OSSpecific (should not fail)"""
		self.o.OS.Features["Some Action"]="test"
		self.o.Action="Some Action"
		self.assertEqual(self.o.Action, "test")

	def test_Action_Wrong_RaisesValueError(self):
		"""Test wrong values for Action setter (raises ValueError)"""
		with self.assertRaises(ValueError):
			self.o.Action="Wrong Action"

	#
	#	TEST OS PROPERTY
	#
	def test_OS_Correct_ShouldNotFail(self):
		"""Test correct OS value for OSSpecific (should not fail)"""
		#Assignment testing. See OSGear testing for further information
		self.o.OS=OSGear(name="Ubuntu", pacman="apt-get", opt={"install":"install", "remove":"remove"})