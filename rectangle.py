#To structure:
# https://www.w3resource.com/python-exercises/oop/python-oop-exercise-4.php

from shapes import Shapes
from numbers import Number
import math # needed for isclose()

class Rectangle(Shapes):
    def __init__(self, x: Number, y: Number, length: Number, width: Number):
        self.length = length
        self.width = width

        super().__init__(x, y)

    """Length properties"""
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"Length must be a valid number, not {type(value)}")
        self._length = value

    """Width properties"""

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"Width must be a valid number, not {type(value)}")
        self._width = value

    """Abstract properties"""

    @property
    def perimeter(self) -> Number:
        return 2 * (self.length + self.width)

    @property
    def area(self) -> Number:
        return self.length * self.width
    
    """Comparison operators"""

    def __eq__(self, other) -> bool:
        """
        Checks equality: Two rectangles are equal if they have
        the same dimensions, regardless of order. 
        Using math.isclose() to round numbers.
        """
        if not isinstance(other, Rectangle):
            return NotImplemented

        self_sides = sorted([self.length, self.width])
        other_sides = sorted([other.length, other.width])
        
        # Compares every pair in the sorted lists with math.isclose()
        return all(math.isclose(a, b) for a, b in zip(self_sides, other_sides))


    def is_square(self) -> bool:
        """Checks if the rectangle is a square"""
        return math.isclose(self.length == self.width)

    """Representation"""
    def __repr__(self) -> str:
        return f"Rectangle ({self.x}, {self.y} with length: {self.length} and width: {self.width})"

    def __str__(self) -> str:
        return f"Rectangle with length: {self.length} and width: {self.width}, \nhas the area of: {self.area}"
        