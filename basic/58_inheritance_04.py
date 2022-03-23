#!/usr/bin/python3

#   This example shows how to handle an inheritance tree with abstract classes and abstract methods

# I import this library in order to be able to define abstract methods
import math
from abc import abstractmethod, ABC


class Shape:
    def __init__(self, color):
        self.__color = color

    # In Python there are no abstract methods officially defined, so to explicitly create abstract methods you need to
    # decorate them with this extra annotation and import the library abc.
    @abstractmethod
    def calculate_surface(self):
        return

    @abstractmethod
    def calculate_perimeter(self):
        return


class Polygon(Shape, ABC):
    def __init__(self, num_sides):
        self.__num_sides = num_sides


class RegularPolygon(Polygon, ABC):
    def __init__(self, num_sides, side_length):
        super().__init__(num_sides)
        self.__side_length = side_length

    def calculate_perimeter(self):
        return self.__side_length * self._Polygon__num_sides


class Square(RegularPolygon):
    NUM_SIDES = 4

    def __init__(self, side_length):
        super().__init__(self.NUM_SIDES, side_length)

    def calculate_surface(self):
        return math.pow(self._RegularPolygon__side_length, 2)


class EquilateralTriangle(RegularPolygon):
    NUM_SIDES = 3

    def __init__(self, side_length):
        super().__init__(self.NUM_SIDES, side_length)

    def calculate_surface(self):
        return math.sqrt(3) / 4.0 * math.pow(self._RegularPolygon__side_length, 2)


s1 = Square(5)
print("The perimeter of the square is: ", s1.calculate_perimeter(), "and its surface: ", s1.calculate_surface())

t1 = EquilateralTriangle(3)
print("The perimeter of the triangle is: ", t1.calculate_perimeter(), "and its surface: ", t1.calculate_surface())






