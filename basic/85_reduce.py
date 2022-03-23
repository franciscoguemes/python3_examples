#!/usr/bin/python3

# Following the previous example of the map function I am going to create an application that returns the sum of the
# square roots of the supplied values.
# See:
#   https://book.pythontips.com/en/latest/map_filter.html#reduce

# To summarize the reduce function works as follows:
#   map(function_to_apply_to_the_partial_result_and_to_each_element_in_the_list, list_of_inputs)

from functools import reduce
import math


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

# Note that the left argument of the reduce function is a lambda expression with 2 parameters "x" and "y". In this
# case x represents the value of the sum of all square roots computed until the current moment and "y" represents the
# current value that is being iterated in the list.
sum_of_square_roots = reduce((lambda x, y: x + calculate_root(y)), list(filter(is_positive, numbers)))
print("The sum of the square roots of the positive numbers is:")
print(sum_of_square_roots)


