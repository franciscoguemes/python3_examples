#!/usr/bin/python3

#   In this example I am going to continue with the previous example and I am going to create an encapsulated method
#   that I will use inside the class.


class Person:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def introduce(self):
        print("Hi! My name is:", self.__full_name())

    def __full_name(self):
        return self.__name + " " + self.__surname


# As you can see now in order to instantiate the class I have to use the constructor and pass the parameters.
me = Person("Francisco", "Güemes")
me.introduce()






