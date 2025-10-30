#To structure:
# https://www.w3resource.com/python-exercises/oop/python-oop-exercise-4.php

from numbers import Number

class Rectangle(Shapes):
    def __init__(self, length: float, width: float):
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
    def perimeter(self):
        return 2 * (self.length + self.width)

    @property
    def area(self):
        return self.length * self.width

