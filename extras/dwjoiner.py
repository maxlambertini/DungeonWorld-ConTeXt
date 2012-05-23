# -*- coding: utf-8 -*-

import os
import glob
import codecs
from xml.dom.minidom import *

impl = getDOMImplementation()
domDest = impl.createDocument(None,"body",None)
with open("filelist.txt","r") as dataSrc:
	files = dataSrc.readlines()
	for file in files:
		file = file.replace("\n","")
		print "processing ", file
		with open (file,mode="r") as xmlIn:
			domSrc = parse(xmlIn)
			elems = domSrc.getElementsByTagName("Root")
			for elem in elems:
				for child in elem.childNodes:
					w = child.nodeName
					if w == "Body" or w  == "Story":
						for child1 in child.childNodes:
							domDest.documentElement.appendChild(child1)
					else:
						domDest.documentElement.appendChild(child)
			

data= domDest.getElementsByTagName("body")[0].toprettyxml(encoding="utf-8")
data=data.replace("aid:pstyle","class")
data=data.replace("aid:cstyle","class")

with open ("dw_full.html", "w") as out:
	out.write(data);
	
	



