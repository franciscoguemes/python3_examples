#!/usr/bin/python3

#   As it is now, the class Person is pretty much useless so let's add a constructor

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


# As you can see now in order to instantiate the class I have to use the constructor and pass the parameters.
me = Person("Francisco", "Güemes")

# To review the previous example I will add the phone number on the fly
me.phone_number = "99990000"

print("Hi! My name is:", me.name, me.surname, ". And my phone number is:", me.phone_number)




