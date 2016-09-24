from commands.osgear import *
import unittest

class testOSGear(unittest.TestCase):
	"""Test Case to test out OSGear"""
	
	#
	#	TEST INITIALISATION
	#
	def setUp(self):
		"""Declare an Append test object with correct values (should not fail).
		Test each given values."""
		self.os=OSGear("Ubuntu", "apt-get", {"update": "update"})
		self.assertEqual(self.os.Name, "Ubuntu")
		self.assertEqual(self.os.PackageManager, "apt-get")
		self.assertEqual(self.os.Features, {"update": "update"})

	#
	#	TEST NAME PROPERTY
	#
	def test_Name_Correct_ShouldNotFail(self):
		"""Test correct value for name into OSGear (should not fail)."""
		self.os.Name="Fedora Gnome"
		self.assertEqual(self.os.Name, "Fedora Gnome")

	#
	#	TEST PACKAGEMANAGER PROPERTY
	#
	def test_PackageManager_Correct_ShouldNotFail(self):
		"""Test correct PackageManager value for OSGear (should not fail)."""
		self.os.PackageManager="dnf"
		self.assertEqual(self.os.PackageManager, "dnf")

	#
	#	TEST FEATURES PROPERTY
	#
	def test_Features_Correct_ShouldNotFail(self):
		"""Test correct Features value for OSGear (should not fail)."""
		self.os.Features["Update"]="update"
		self.assertEqual(self.os.Features["Update"], "update")

	def test_Features_WrongKey_Retrieve_RaisesKeyError(self):
		"""Test wrong key retrieval into Features (raises KeyError)."""
		with self.assertRaises(KeyError):
			test = self.os.Features["WrongKey"]