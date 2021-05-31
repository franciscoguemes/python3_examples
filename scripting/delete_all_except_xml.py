#!/usr/bin/python3

#
# This script deletes all contents of the contents of the child directories except the *.xml files.
#

import os
import shutil
from os.path import abspath

# Resolve current working directory: https://stackoverflow.com/a/32838876
pwd = abspath('.')
#Iterate over the files in the directory: https://stackoverflow.com/a/10378012
for file in os.listdir(pwd):
	# Compose the absolute file name
	child = os.path.join(pwd, file)
	if os.path.isdir(child):
		# Iterate in the child directory
		for whatever in os.listdir(child):
			# Compose the absolute file name
			grand_child = os.path.join(child, whatever)
			# If the file is not an xml file delete it
			if not grand_child.endswith('.xml'):
				print(f"Deleting: {grand_child}")
				if os.path.isdir(grand_child):
					shutil.rmtree(grand_child)
				else:
					os.remove(grand_child)


