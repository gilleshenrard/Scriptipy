from commands.osgear import *
import unittest

class testOSGear(unittest.TestCase):
	"""Test Case to test out OSGear"""
	def setUp(self):
		"""Initialise test variables"""
		self.os=OSGear()
#
#	TEST CONSTRUCTOR
#
	def test_CorrectValues_Contructor_ShouldNotFail(self):
		"""Test correct values for OSGear constructor"""
		try:
			os2=OSGear("Ubuntu", "apt-get", {"update": "update"})
		except:
			self.fail("Test for correct Constructor values assignment failed!")
#
#	TEST NAME PROPERTY
#
	def test_Correct_Name_ShouldNotFail(self):
		"""Test correct name value for Command"""
		try:
			self.os.Name="Fedora Gnome"
		except:
			self.fail("Test for correct Name assignment failed!")
#
#	TEST PACKAGEMANAGER PROPERTY
#
	def test_Correct_PackageManager_ShouldNotFail(self):
		"""Test correct PackageManager value for Command"""
		try:
			self.os.PackageManager="dnf"
		except:
			self.fail("Test for correct PackageManager assignment failed!")
#
#	TEST OPTIONS PROPERTY
#
	def test_Correct_Options_ShouldNotFail(self):
		"""Test correct Options value for Command"""
		try:
			self.os.Features["update"]="update"
		except:
			self.fail("Test for correct Options assignment failed!")

	def test_RemoveWrongKey_Options_RaisesKeyError(self):
		"""Test wrong key removal into Options"""
		with self.assertRaises(KeyError):
			self.os.Features.pop("WrongOption")
