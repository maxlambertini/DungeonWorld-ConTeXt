# -*- coding: utf-8 -*-

import os
import glob
import codecs
from xml.dom.minidom import *

tags_to_div = ["Body","Story","Root"]

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
				domDest.documentElement.appendChild(elem)
		print "processed ", file
			

data= domDest.getElementsByTagName("body")[0].toxml(encoding="utf-8")
for tag in tags_to_div:
	data = data.replace("<"+tag, "<div")
	data = data.replace("</"+tag, "</div")
data=data.replace("aid:pstyle","class")
data=data.replace("aid:cstyle","class")

with open ("dw_full.html", "w") as out:
	out.write(data);
	
	



