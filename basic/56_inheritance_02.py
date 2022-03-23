#!/usr/bin/python3

#   In this example I am going to override the added the properties "id" to the class Person and I will override the
#   method introduce


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
    def __init__(self, id, name, surname):
        super().__init__(name, surname)
        self.__id = id

    # I am overriding the method introduce here...
    def introduce(self):
        # Note that in order to call the encapsulated method __full_name of the parent class, I need to use name
        # mangling --> https://stackoverflow.com/questions/20261517/inheritance-of-private-and-protected-methods-in-python
        print("Hi! My customer id is", self.__id, "and my name is", self._Person__full_name())


# As you can see now I am instantiating a class of type Customer, but it inherits the properties, behaviour and state
# of the class Person.
me = Customer("000001", "Francisco", "Güemes")
me.introduce()






