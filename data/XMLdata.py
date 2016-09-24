from .datatype import *
from commands.osgear import *
from os import path
from xml.etree.ElementTree import parse

class XMLdata(DataType):
	"""Command XML data (de)serialisation
	:param source: XML source file name"""

	def __init__(self, source=""):
		"""Create and initialise an XML (de)serialisation process."""
		DataType.__init__(self, source)

	def deserialize(self):
		"""Deserialise data from an XML data file."""
		if path.exists(self.Source):
			#Retrieving XML tree root			
			tree = parse(self.Source)
			root = tree.getroot()

			#Reconstructing OSGear elements
			OSes = []
			for elem in root.findall("OSGear"):
				os = OSGear()
				os.Name = elem.find("Name").text
				os.PackageManager = elem.find("PackageManager").text
				for feature in elem.find("Features"):
					os.Features[feature.attrib['key']]=feature.text
				OSes.append(os)

			#Reconstructing command elements
			commands = []
			for elem in root:
				com = ""
				#Defining object type
				if elem.tag == "Command":
					com = Command()
				elif elem.tag == "Append":
					com = Append()
				elif elem.tag == "Replace":
					com = Replace()
				elif elem.tag == "Package":
					com = Package()
				elif elem.tag == "Repository":
					com = Repository()
				else:
					raise ValueError("{} is an unknown type".format(elem.tag))

				#Retrieving all object variables
				name = elem.find("Name")
				if name != None:
					com.Name = name
				comment = elem.find("Comment")
				if comment != None:
					com.Comment = comment

				if elem.tag in ["Append", "Replace"]:
					nl = elem.find("NewLine")
					if nl != None:
						com.NewLine = nl
				if elem.tag == "Replace":
					ol = elem.find("OldLine")
					if ol != None:
						com.OldLine = ol

				if elem.tag in ["Package", "Repository"]:
					act = elem.get("act")
					if act != None:
						com.Action = act
					opt = elem.find("Options")
					if opt != None:
						com.Options = opt
		else:
			raise ValueError("File {} not found".format(self.Source))

	def serialize(self):
		"""Serialise data from a JSON data file."""
		pass