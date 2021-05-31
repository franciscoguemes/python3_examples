#!/usr/bin/python3

#   This example shows how to use polymorphism in Python since the show_communication just expects a class that has
#   the method communicate, not necessarily that extends from LifeForm.

#   The example also shows how to use the built-in method isinstance to differentiate between different object types.

from abc import abstractmethod


class LifeForm:
    @abstractmethod
    def communicate(self):
        return


class Person(LifeForm):
    def communicate(self):
        print("Bla bla bla")


class Dog(LifeForm):
    def communicate(self):
        print("wow wow wow")


class Bird(LifeForm):
    def communicate(self):
        print("Pi pi pi")


def show_communication(life_form):
    if isinstance(life_form, Person):
        print("The persons usually talk...")
    elif isinstance(life_form, Dog):
        print("The dogs usually bark...")
    elif isinstance(life_form, Bird):
        print("The birds usually cheep...")
    else:
        print("Other life forms just do...")

    life_form.communicate()


print("In this programm we show how different life forms communicate...")
p1 = Person()
d1 = Dog()
b1 = Bird()

show_communication(p1)
show_communication(d1)
show_communication(b1)

