#!/usr/bin/python3

import math

# In this example I am going to show how to use the map function in Python by using an overcomplicated example.
# See:
#   https://book.pythontips.com/en/latest/map_filter.html#map

# To summarize the map function works as follows:
#   map(function_to_apply, list_of_inputs)

# To explain the map function I am going to create 2 functions one that acts as a filter in order to get ony the
# positive values and another one that calculates the square root.


def is_positive(num):
    if num >= 0:
        return True
    else:
        return False


def calculate_root(num):
    return math.sqrt(num)


def print_iterable(iterable):
    for n in iterable:
        print(n, end=" ")
    print()


numbers = range(-5, 6)
print("The generated numbers are:")
print_iterable(numbers)
# You could achieve the same result without the lambda expression calling directly to "calculate_root" passing
# directly the function as argument or on the other hand side if you use a lambda expression calculating the square
# root inside the lambda expression.
# Also in the second argument of the function map, I directly applied a filter over the collection. To make it more
# readable you could apply the filter, store the resulting collection in a variable, and pass it as second argument
# to the map function.
square_roots = list(map(lambda x: calculate_root(x), list(filter(is_positive, numbers))))
print("The square roots of the positive numbers are:")
print_iterable(square_roots)