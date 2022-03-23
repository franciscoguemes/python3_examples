#!/usr/bin/python3

# In this example I am going to show how to use the filter function in Python
# See:
#   https://book.pythontips.com/en/latest/map_filter.html#filter
#   https://www.programiz.com/python-programming/methods/built-in/filter


# The filter function accepts a couple of parameters:
#   -the function to apply to each element. The function can be also a lambda.
#   -The collection of items on which the function will be applied.
# The function filter returns a list of elements.

numbers = range(-5, 6)


print("Negative numbers: ")
# Note that after calling to filter it is necessary to call the function "list":
#   https://www.programiz.com/python-programming/methods/built-in/list
for n in list(filter(lambda x: x<0, numbers)):
    print(n, end=" ")

print()
print("Natural numbers: ")
for n in list(filter(lambda x: x>=0, numbers)):
    print(n, end=" ")
print()