#!/usr/bin/python3

#   To explain the inheritance I will continue with the example of the class Person, but know I will create a class
#   Employee that will inherit from the class Person.


class Person:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def introduce(self):
        print("Hi! My name is:", self.__full_name())

    def __full_name(self):
        return self.__name + " " + self.__surname


# The class Customer inherits from Person
class Customer(Person):
    pass


# As you can see now I am instantiating a class of type Customer, but it inherits the properties, behaviour and state
# of the class Person.
me = Customer("Francisco", "Güemes")
me.introduce()






