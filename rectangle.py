#To structure:
# https://www.w3resource.com/python-exercises/oop/python-oop-exercise-4.php

from shapes import Shapes
from numbers import Number

class Rectangle(Shapes):
    def __init__(self, x: Number, y: Number, length: Number, width: Number):
        super().__init__(x, y)
        self.length = length
        self.width = width
        

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"Length must be a valid number, not {type(value)}")
        self._length = value

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"Width must be a valid number, not {type(value)}")
        self._width = value

    @property
    def perimeter(self) -> Number:
        return 2 * (self.length + self.width)

    @property
    def area(self) -> Number:
        return self.length * self.width

    def is_square(self) -> bool:
        return self.length == self.width

    def __repr__(self) -> None:
        return f"Rectangle ({self.x}, {self.y} with length: {self.length} and width: {self.width})"

    def __str__(self) -> str:
        print(f"Rectangle with length: {self.length} and width: {self.width}, \nhas the area of: {self.area}")
        