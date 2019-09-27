#!/usr/bin/python3

# In this example I am going to show how to use lambdas in Python with a very easy example
# If you want to go deeper into lambdas I recommend you the following articles:
#   https://realpython.com/python-lambda/#cryptic-style
#   https://pythonconquerstheuniverse.wordpress.com/2011/08/29/lambda_tutorial/


# This example is a comparator embedded into a lambda. Note that the syntax of the if - else is a bit different in
# the lambda. Note also that the line has a warning (in some Python editors) due to the assignment of a
# lambda expression to a name. See: https://stackoverflow.com/a/25010243
comparator = lambda a, b: str(a) + " is smaller or equals than " + str(b) if a <= b else str(a) + " is bigger than " + str(b)

numbers = [3, 5, 1, 9, 6]

for i in range(len(numbers)-1):
    print(comparator(numbers[i], numbers[i+1]))


