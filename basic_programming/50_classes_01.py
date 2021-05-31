#!/usr/bin/python3

#   This example shows how to define a class. I have defined the class Person which has 2 attributes: name and
#   surname.
#   Later I use create an instance of the class Person in my application to present myself.

class Person:
    name = "Francisco"
    surname = "Güemes"
    personal_site = "www.franciscoguemes.com"

me = Person()
print("Hi! My name is:", me.name, me.surname, ". More info about me in my site:", me.personal_site)



