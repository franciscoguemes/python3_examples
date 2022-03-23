#!/usr/bin/python3

#   In continuation with the previous example I will show you how you can add and delete object properties on the fly.
#   Very good explanation of the deletion operators:
#       https://www.geeksforgeeks.org/delattr-del-python/

class Person:
    name = "Francisco"
    surname = "Güemes"
    personal_site = "www.franciscoguemes.com"


me = Person()

# There are 2 ways of deleting properties with delattr and with the del operator.
delattr(Person, "personal_site")
del Person.surname

# To add an attribute on the fly simply use the dot notation
me.phone_number = "99990000"

print("Hi! My name is:", me.name, ". And my phone number is:", me.phone_number)


# Here the application will fail because we deleted the field surname
print("Hi! My name is:", me.name, me.surname, ". And my phone number is:", me.phone_number)



