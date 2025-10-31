from numbers import Number
from abc import ABC, abstractmethod


class Shapes(ABC):
    """
    Abstract (ABC) Super class for all geometric shapes in the sub-classes.
    The abstract methods enfoce common fuctionality for area, perimeter and representation.
    It provides shared functionality such as position, translation,
    and the comparison operators that can be implemented in the sub-classes.

    Attributes:
    - x (Number): coordnate for x-axis
    - y (Number): coordinate for y-axis

    Properties:
    - x (self, value): Makes sure that 'x' is a number and returns a private value for x. 
    - y (self, value): Makes sure that 'y' is a number and returns a private value for y.

    Methods:
    - translate(): Moves the shape with 'dx' along the x-axis 
        and 'dy' along the y-axis
    - __repr__(): abstract representation method
    - __str__(): abstract representation method
    """

    def __init__(self, x: Number, y: Number):
        """
        Initializes 'x' and 'y', the center position of the shape.
        
        Parameters:
        - x (Number): The x-coordinate
        - y (Number): The y-coordinate 

        Calling self.x and self.y for the property 'setter' to
        ensure type validation
        """
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

    def translate(self, dx: Number, dy: Number):
        if not isinstance(dx, Number) or not isinstance(dy, Number):
            raise TypeError("Both 'dx' and 'dy' must be numbers")
        
        # Updates the position
        self.x += dx
        self.y += dy

        return self 

    """
    Read-only properties for the objects perimeter and area.
    Must be implemented in the subclasses. 
    """
    @property
    @abstractmethod
    def perimeter(self) -> Number:
        pass

    @property
    @abstractmethod
    def area(self) -> Number:
        pass
    
    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    """
    Comparison operators that can be implemented in the subclasses
    for comparing area of shapes are:
    less than: '<', greater than: '>', 
    less or equal to: '<=' and greater or equal to: '>='. 
    Equal to '==' must be implemented in sub-classes. 
    """

    @abstractmethod
    def __eq__(self, other) -> bool:
        pass

    def __lt__(self, other) -> bool:
        if not isinstance(other, Shapes):
            return NotImplemented
        return self.area < other.area

    def __gt__(self, other) -> bool:
        return self.area > other.area

    def __le__(self, other) -> bool:
        return self.area <= other.area

    def __ge__(self, other) -> bool:
        return self.area >= other.area



    

    