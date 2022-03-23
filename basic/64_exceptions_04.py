#!/usr/bin/python3

#   This example shows how to create your own user-defined exception hierarchy. Like any other class in Python,
#   exceptions can inherit from other exceptions.

import math


class NumberException(Exception):
    """Base class for other exceptions"""
    pass


class EvenNumberException(NumberException):
    """Specific exception which inherits from MyGenericException"""
    pass


class OddNumberException(NumberException):
    """Specific exception which inherits from MyGenericException"""
    pass


def get_number(message):
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("The supplied value is not a number, Try again...")


stay = True
while stay:
    try:
        num = get_number("Introduce any number (0 to exit):")
        if num == 0:
            stay = False
        elif num % 2 == 0:
            raise EvenNumberException
        else:
            raise OddNumberException
    except EvenNumberException:
        print("The number you introduced", num, "is Even!")
    except OddNumberException:
        print("The number you introduced", num, "is Odd!")


# As example you can try to re-write this same application capturing the exception NumberException and using the
# isinstance operator...
