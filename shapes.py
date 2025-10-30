from numbers import Number
from abc import ABC, abstractmethod

"""
Parent class
"""

class Shapes:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"'x' must be a number of an int or float, not {type(value)}")
        self._x = value

    @property
    def y(self):
        return self._y 

    @y.setter
    def y(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"'y' must be a number of an int or float, not {type(value)}")
        self._y = value


    @property
    def perimeter(self):
        pass

    def area(self):
        pass

    def __eq__(self):
        pass

    def __lt__(self):
        pass

    def __gt__(self):
        pass

    def __le__(self):
        pass

    def __ge__(self):
        pass



    

    