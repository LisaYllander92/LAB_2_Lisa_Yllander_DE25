#https://www.w3resource.com/python-exercises/oop/python-oop-exercise-4.php

from shapes import Shapes
import math # to calculate pi
from numbers import Number # to just make sure the value is a number

class Circle(Shapes):
    def __init__(self, x: Number, y: Number, radius: Number):
        self.radius = radius
        super().__init__(x, y)

    @property
    def radius(self):
        return self._radius
    
    @ radius.setter
    def radius(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"Radius must be a non-negative number, not {type(value)}")
        self._radius = value

    @property
    def perimeter(self) -> Number:
        return 2 * math.pi * self.radius

    @property
    def area(self) -> Number:
        return math.pi * self.radius**2

    # Check if the circle is a unit-circle (radius 1, center 0,0)
    def is_unit_circle(self) -> bool:
        return self.radius == 1 and self.x == 0 and self.y == 0
    
    def __repr__(self) -> str:
        return f"Circle: x: {self.x}, y: {self.y} and radius: {self.radius}"
    
    def __str__(self) -> str:
        print(f"The circle at ({self.x}, {self.y}) with radius: {self.radius} \nhas the area of:{self.area:.2f}")