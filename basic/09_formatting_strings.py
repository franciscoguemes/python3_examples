#!/usr/bin/python3

# TODO: Continue the example from: https://pyformat.info/

# There are two ways of formatting strings in Python:
#   With the "str.format()" function
#   Using the Old Python way through the "%" operator


# Formatting strings that contain strings
old_str = "%s %s" % ("Hello", "World")
new_str = "{} {}".format("Hello", "World")

print(old_str)
print(new_str)

# Formatting strings that contain integers
old_str = "%d and %d" % (1, 2)
new_str = "{} and {}".format(1, 2)

print(old_str)
print(new_str)

# Formatting strings that contain float
old_str = "%f" % (3.141592653589793)
new_str = "{:f}".format(3.141592653589793)

print(old_str)
print(new_str)