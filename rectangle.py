#To structure:
# https://www.w3resource.com/python-exercises/oop/python-oop-exercise-4.php

from shapes import Shapes
from numbers import Number # To make sure the value is a number
import math
import matplotlib.pyplot as plt

class Rectangle(Shapes):
    def __init__(self, length: Number, width: Number, x: Number = 0, y: Number = 0):
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
        return f"Rectangle with length: {self.length} and width: {self.width}, has the area of: {self.area}"
        
    def draw(self):
        """
        Vissualizes the rectangle using Matplotlib
        Sources: 
        https://www.geeksforgeeks.org/python/how-to-draw-shapes-in-matplotlib-with-python/
        https://www.statology.org/matplotlib-rectangle/
        """

        # Creating figure (the window) and axes (the plot area) using plt.subplots().
        fig, ax = plt.subplots(1) 

        # Determine starting position (Matplotlib's rectangle patch requiers
        # the coordinates of the bottom-left corner).
        # Calculation: center x - half length, center y - half width
        x_start = self.x - self.length /2
        y_start = self.y - self.width /2

        # plt.Rectangle creates the object based on the 
        # calculated start point and dimensions
        rect_patch = plt.Rectangle(
            (x_start, y_start), # Bottom left corner
            self.length,
            self.width,
            color = 'green',
            alpha = 0.5
        )

        # .add_artist() adds the rectangle shape to the plot.
        ax.add_artist(rect_patch)

        # .plot(..., 'ro') marks the center (self.x, self.y) with a red dot
        ax.plot(self.x, self.y, 'ro') 

        # Setting the plot limits to make sure the entire rectangle is visible.
        margin_x = self.length * 0.2
        margin_y = self.width * 0.2
        ax.set_xlim(self.x - self.length / 2 - margin_x, self.x + self.length / 2 + margin_x)
        ax.set_ylim(self.y - self.width / 2 - margin_y, self.y + self.width / 2 + margin_y)

        # Display settings:
        # ax.set_aspects('equal') controlls the form of the object (rectangle), so a square doesn't look lika a rectangle,
        # making sure that the unit on the x-axis is the same as the unit on the y-axis.
        #(adjustable = 'box') the plotting area will adjust to the dimensions of the figure.
        ax.set_aspect('equal', adjustable = 'box')

        plt.title(f"Rectangle: {self.length} x {self.width}, center = ({self.x}, {self.y})")
        plt.xlabel("x-axis")
        plt.ylabel("y-axis")
        plt.grid(True)
        plt.plot()
