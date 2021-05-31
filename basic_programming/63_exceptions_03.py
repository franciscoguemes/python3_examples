#!/usr/bin/python3

#   In the current example I show how to create our own user-defined exception and how to throw it by using the keyword
#   "raise"

import math


# All user-defined exceptions inherits from Exception.
class InvalidArgumentException(Exception):
    """This exception will be triggered when the argument is considered to be invalid"""
    pass


def get_number(message):
    while True:
        try:
            num1 = int(input(message))
            return num1
        except ValueError:
            print("The supplied value is not a number, Try again...")


print("Welcome to the square root app...")
try:
    num1 = get_number("Introduce the number to calculate the square root:")
    if num1<0:
        raise InvalidArgumentException
    print("The result is:", math.sqrt(num1))
except InvalidArgumentException:
    print("It is not allowed to calculate the square root of a negative number!")
finally:
    # This block will be always executed independently of what happens...
    print("Thanks for using the square root app!")