#!/usr/bin/python3

#   This example shows how to use multiple inheritance and shows which constructor is executed in case of inherit from
#   multiple classes.

#   Python looks for each attribute in the class's parents as they are listed left to right.
#       More info: https://stackoverflow.com/a/3277407
#   A very good explanation of the multiple inheritance:
#       https://www.python-course.eu/python3_multiple_inheritance.php


class Base1:
    def __init__(self):
        print("Constructor of class: Base1")
        self.__x = 1


class Base2:
    def __init__(self):
        print("Constructor of class: Base2")
        self.__x = 2

    def m(self):
        print("m of Base2 called")


class Base3:
    def __init__(self):
        print("Constructor of class: Base3")
        self.__x = 3

    def m(self):
        print("m of Base2 called")


class Child(Base1, Base2, Base3):
    # With multiple inheritance the keyword super reference only the first class in the inheritance list. Therefore it
    # is more handy to use the class name followed by the method/property to access. In this case all constructors from
    # the parent classes are called in order to initialize the child instance correctly.
    def __init__(self):
        Base1.__init__(self)
        Base2.__init__(self)
        Base3.__init__(self)

    def sum_x(self):
         return self._Base1__x + self._Base2__x + self._Base3__x


c1 = Child()
# This calls the method in Base2 because Base2 has precedence in the inheritance declaration to Base3
c1.m()
print("The sum of all x is", c1.sum_x())