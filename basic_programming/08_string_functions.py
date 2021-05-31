#!/usr/bin/python3

s1 = 'string defined in single quotes'

s2 = "string defined in double quotes"

s3 = "This is a " + 'valid string'


s4 = """This is a
multi-line string, 
this type of strings are usually used for documenting purposes."""


print("The length of s1 is: " + str(len(s1)))
print(s3.lower())
print(s2.upper())
print(str(3.141592))