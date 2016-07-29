from libs.osspecifications import *
import unittest

class testOSSpecifications(unittest.TestCase):
	"""Test Case to test out OSSpecifications"""
	def setUp(self):
		"""Initialise test variables"""
		self.os=OSSpecifications()
#
#	TEST CONSTRUCTOR
#
	def test_CorrectValues_Contructor_ShouldNotFail(self):
		"""Test correct values for OSSpecifications constructor"""
		try:
			os2=OSSpecifications("Ubuntu", "apt-get", {"update": "update"})
			print(os2)
			os3=OSSpecifications("arch", "pacman")
			print(os3)
		except:
			self.fail("Test for correct Constructor values assignment failed!")
#
#	TEST NAME PROPERTY
#
	def test_Correct_Name_ShouldNotFail(self):
		"""Test correct name value for Command"""
		try:
			self.os.Name="Fedora Gnome"
			print(self.os.Name)
		except:
			self.fail("Test for correct Name assignment failed!")
#
#	TEST PACKAGEMANAGER PROPERTY
#
	def test_Correct_PackageManager_ShouldNotFail(self):
		"""Test correct PackageManager value for Command"""
		try:
			self.os.PackageManager="dnf"
			print(self.os.PackageManager)
		except:
			self.fail("Test for correct PackageManager assignment failed!")
#
#	TEST OPTIONS PROPERTY
#
	def test_Correct_Options_ShouldNotFail(self):
		"""Test correct Options value for Command"""
		try:
			self.os.Options["update"]="update"
			print(self.os.Options)
		except:
			self.fail("Test for correct Options assignment failed!")

	def test_RemoveWrongKey_Options_RaisesKeyError(self):
		"""Test wrong key removal into Options"""
		with self.assertRaises(KeyError):
			self.os.Options.pop("WrongOption")
