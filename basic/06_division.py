#!/usr/bin/python3

# Floor division // --> returns 3 because the operators are 2 integers
# and it rounds down the result to the closest integer
integer_result = 7//2
print(f"{integer_result}")

# Floor division // --> returns 3.0 because the first number is a float
# , so it rounds down to the closest integer and return it in float format.
float_result = 7.//2
print(f"{float_result}")

# Floor division // --> returns -4.0 because the floor division rounds the result down to the nearest integer
# in this case rounding down is to -4 because -4 is lower than -3 !!!
integer_result = -7.//2
print(f"{integer_result}")

# Division / --> returns 3.5
float_result = 7/2
print(f"{float_result}")

