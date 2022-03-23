#!/usr/bin/python3

#   In the previous example we did not have any encapsulation, so in this example I am going to encapsulate the
#   properties inside the class by using the "__" (double underscore) operator to make the properties private to the
#   class and I am going to create a method to introduce the person.
#

class Person:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def introduce(self):
        print("Hi! My name is:", self.__name, self.__surname)


# As you can see now in order to instantiate the class I have to use the constructor and pass the parameters.
me = Person("Francisco", "Güemes")
me.introduce()

# If you uncomment the following line and execute it, it will fail because now the attributes are encapsulated!
# print("Hi! My name is:", me.__name, me.__surname, ". And my phone number is:", me.phone_number)




