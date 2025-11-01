#To structure:
# https://www.w3resource.com/python-exercises/oop/python-oop-exercise-4.php

from shapes import Shapes
from numbers import Number # To make sure the value is a number
import math

class Rectangle(Shapes):
    def __init__(self, x: Number, y: Number, length: Number, width: Number):
        self.length = length
        self.width = width

        super().__init__(x, y)

    """ Length properties """
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"Length must be a valid number, not {type(value)}")
        self._length = value

    """ Width properties """

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"Width must be a valid number, not {type(value)}")
        self._width = value

    """ Abstract properties """

    @property
    def perimeter(self) -> Number:
        return 2 * (self.length + self.width)

    @property
    def area(self) -> Number:
        return self.length * self.width
    
    """ 
    Operator overload for equality (==).
    Checks equality: Two rectangles are equal if they have
    the same dimensions, regardless of order. 
    """

    def __eq__(self, other) -> bool:
        print(f"Comparing {self.length}x{self.width} with {other.length}x{other.width}")
        if type(other) is not type(self):
        #if not isinstance(other, Rectangle):
            return NotImplemented

        self_sides = sorted([self.length, self.width])
        other_sides = sorted([other.length, other.width])
        
        return self_sides == other_sides

    """ Unique method that checks if the rectangle is a square """
    def is_square(self) -> bool:
        return math.isclose(self.length == self.width)

    """ Representation """
    def __repr__(self) -> str:
        return f"Rectangle ({self.x}, {self.y} with length: {self.length} and width: {self.width})"

    def __str__(self) -> str:
        return f"Rectangle with length: {self.length} and width: {self.width}, \nhas the area of: {self.area}"
        