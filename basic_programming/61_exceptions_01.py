#!/usr/bin/python3

#   This example shows how to use a basic exception handling mechanism on which the specific exception ValueError is
#   handled and if any other exception arise during reading the input it is also handled by the block except.


def get_number(message):
    while True:
        try:
            num1 = int(input(message))
            return num1
        except ValueError:
            print("The supplied value is not a number, Try again...")
        except:
            # This will catch any eother exception
            print("An unexpected error has occur")


print("Welcome to the division app...")
num1 = get_number("Introduce the dividend:")
num2 = get_number("Introduce the divisor:")
print("The result is:", num1 / num2)