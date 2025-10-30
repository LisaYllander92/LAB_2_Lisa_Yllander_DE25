#https://www.w3resource.com/python-exercises/oop/python-oop-exercise-4.php

import math #to calculate pi
from numbers import Number

class Circle(Shapes):
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @ radius.setter
    def radius(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"Radius must be a valid number, not {type(value)}")
        self._radius = value

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius

    @property
    def area(self):
        return math.pi * self.radius**2

    def is_unit_circle(self):
        pass