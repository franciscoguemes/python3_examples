#!/usr/bin/python3

# Replace characters in a string with the "sub" method

import re



str = "I like programming in Pyhon"
# Split the string on spaces.
x = re.sub("\s", "--", str)
print(x)

# You can control the number of substitutions by giving one more extra parameter.
x = re.sub("\s", "--", str, 1)
print(x)