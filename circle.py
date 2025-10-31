#https://www.w3resource.com/python-exercises/oop/python-oop-exercise-4.php

from shapes import Shapes
import math # to calculate pi and use isclose
from numbers import Number  # to just make sure the value is a number

class Circle(Shapes):
    def __init__(self, x: Number, y: Number, radius: Number):
        super().__init__(x, y)
        self.radius = radius
        

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
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        
        return self.radius == other.radius
        

    # Check if the circle is a unit-circle (radius 1, center 0,0)
    def is_unit_circle(self) -> bool:
        radius_ok = math.isclose(self.radius, 1,0)
        x_ok = math.isclose(self.x, 0.0)
        y_ok = math.isclose(self.y, 0.0)

        return radius_ok, x_ok and y_ok
         
    def __repr__(self) -> str:
        return f"Circle: x: {self.x}, y: {self.y} and radius: {self.radius}"
    
    def __str__(self) -> str:
        f"The circle at ({self.x}, {self.y}) with radius: {self.radius} \nhas the area of:{self.area:.2f}"