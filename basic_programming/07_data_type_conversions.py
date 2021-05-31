#!/usr/bin/python3

string = "7"
print(f"{string}") # --> 7

number = 7
print(f"{number}") # --> 7

#It is necessary to convert the string to an integer with the int()
addition = number + int(string)
print(f"{addition}") # --> 14

string2 = "7.5"
addition2 = number + float(string2)
print(f"{addition2}") # --> 14.5


addition3 = number + int(string2) # --> Generates error, it is invalid
print(f"{addition2}")