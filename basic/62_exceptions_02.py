#!/usr/bin/python3

#   To be fair the previous example was not foolproof since someone could introduce 0 as divisor and then the
#   application would fail so I will fix that by handling the error: ZeroDivisionError:


def get_number(message):
    while True:
        try:
            num1 = int(input(message))
        except ValueError:
            print("The supplied value is not a number, Try again...")
        except:
            # This will catch any other exception
            print("An unexpected error has occur")
        else:
            # else block excecutes if try block "succeeds"
            return num1



print("Welcome to the division app...")
try:
    num1 = get_number("Introduce the dividend:")
    num2 = get_number("Introduce the divisor:")
    print("The result is:", num1 / num2)
except ZeroDivisionError:
    print("It is not allowed to divide by zero!!!!")
finally:
    # This block will be always executed independently of what happens...
    print("Thanks for using the division app!")