#!/usr/bin/python3

# Use the "split" method to split strings based on regex

import re

str = "I like programming in Pyhon"
# Split the string on spaces.
x = re.split("\s", str)
print(x)

# You can control the number of occurrences by giving a secon parameter (maxsplit)
x = re.split("\s", str,2)
print(x)
