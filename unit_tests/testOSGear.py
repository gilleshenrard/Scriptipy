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
	def test_Contructor_Correct_ShouldNotFail(self):
		"""Test correct values for OSGear constructor (should not fail)."""
		try:
			os2=OSGear("Ubuntu", "apt-get", {"update": "update"})
			self.assertEqual(os2.Name, "Ubuntu")
			self.assertEqual(os2.PackageManager, "apt-get")
			self.assertEqual(os2.Features, {"update": "update"})
		except:
			self.fail("Test for correct Constructor values assignment failed!")

	#
	#	TEST NAME PROPERTY
	#
	def test_Name_Correct_ShouldNotFail(self):
		"""Test correct value for name into OSGear (should not fail)."""
		try:
			self.os.Name="Fedora Gnome"
			self.assertEqual(self.os.Name, "Fedora Gnome")
		except:
			self.fail("Test for correct Name assignment failed!")

	#
	#	TEST PACKAGEMANAGER PROPERTY
	#
	def test_PackageManager_Correct_ShouldNotFail(self):
		"""Test correct PackageManager value for OSGear (should not fail)."""
		try:
			self.os.PackageManager="dnf"
			self.assertEqual(self.os.PackageManager, "dnf")
		except:
			self.fail("Test for correct PackageManager assignment failed!")

	#
	#	TEST FEATURES PROPERTY
	#
	def test_Features_Correct_ShouldNotFail(self):
		"""Test correct Features value for OSGear (should not fail)."""
		try:
			self.os.Features["update"]="update"
			self.assertEqual(self.os.Features["update"], "update")
		except:
			self.fail("Test for correct Features assignment failed!")

	def test_Features_WrongKey_Retrieve_RaisesKeyError(self):
		"""Test wrong key retrieval into Features (raises KeyError)."""
		with self.assertRaises(KeyError):
			test = self.os.Features["WrongKey"]