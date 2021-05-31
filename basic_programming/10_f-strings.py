#!/usr/bin/python3

# This example shows how to format strings by using the traditional ways and the F-String way


currency = "€"
amount = 1000000

# Typical concatenation of strings through the "+" operator
str1 = "I want to make " + str(amount) + " " + currency + " in the following year"
# Using the "str.format()" function of a string
str2 = "I want to make {0} {1} in the following year".format(amount, currency)
# Old Python formatting style --> https://pyformat.info/
str3 = "I want to make %i %s in the following year" % (amount, currency)

# Using Python F-Strings
fstring = F"I want to make {amount} {currency} in the following year"


print(str1)
print(str2)
print(str3)
print(fstring)