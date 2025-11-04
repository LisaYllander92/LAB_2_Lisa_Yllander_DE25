#https://www.w3resource.com/python-exercises/oop/python-oop-exercise-4.php


from shapes import Shapes
import math # to calculate pi and use isclose
from numbers import Number  # to just make sure the value is a number
import matplotlib.pyplot as plt # To plot the shapes

class Circle(Shapes):
    # Changed the standard value of x and y to 0
    def __init__(self, radius: Number, x: Number = 0, y: Number = 0):
        self.radius = radius
        super().__init__(x, y)

    """ Radius properties """
    @property
    def radius(self):
        return self._radius
    
    @ radius.setter
    def radius(self, value):
        if not isinstance(value, Number):
            raise TypeError(f"Radius must be a non-negative number, not {type(value).__name__}")
        if value < 0:
            raise ValueError("Radius can't be negative")
        self._radius = value

    """ Abstract properties """
    @property
    def perimeter(self) -> Number:
        return 2 * math.pi * self.radius

    @property
    def area(self) -> Number:
        return math.pi * self.radius**2
    
    """
    Operator overload for equality (==).
    Two circles are equal if their radius are the same, 
    using math.isclose to handle compaison of float-numbers.
    """
    def __eq__(self, other) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented  
        return math.isclose(self.radius, other.radius)
        
    """ Unique method that checks if the circle is a unit-circle (radius 1, center 0,0)"""
    def is_unit_circle(self) -> bool:
        radius_ok = math.isclose(self.radius, 1.0)
        x_ok = math.isclose(self.x, 0.0)
        y_ok = math.isclose(self.y, 0.0)

        return radius_ok and x_ok and y_ok
         
    """ Representations """     
    def __repr__(self) -> str:
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"
    
    def __str__(self) -> str:
        return f"The circle at ({self.x}, {self.y}) with radius: {self.radius} \nhas the area of:{self.area:.2f}"
    
    def draw(self):
        """
        Visualizes the circle using Matplotlib. 
        Sources: 
        https://www.geeksforgeeks.org/python/how-to-draw-a-circle-using-matplotlib-in-python/
        https://www.geeksforgeeks.org/python/how-to-draw-shapes-in-matplotlib-with-python/
        """

        # Creating figure (the window) and axes (the plot area) using plt.subplots().
        fig, ax = plt.subplots(1)

        # Setting the scale/plot limits to ensure the entire circle is visible.
        # The limits are based on the center (self.x, self.y).
        margin = self.radius * 1.5 # gives the circle some space
        ax.set_xlim(self.x - margin, self.x + margin)
        ax.set_ylim(self.y - margin, self.y + margin)

        # plt.Circle creates the object (circle) to display
        circle_patch = plt.Circle(
            (self.x, self.y), # Center position (coordinates (x,y))
            self.radius, # The radius
            color = 'pink', # filled color
            alpha = 0.5 # sets transparancy
        )

        # add_artist() adds the circle shape to the plot.
        ax.add_artist(circle_patch) 

        # .plot(..., 'ro') adds a red circle ('r') marker ('o') at the center (x, y).
        # This visually confirms the center position set by the 'x' and 'y' attributes.
        ax.plot(self.x, self.y, 'ro') 

        # Display settings: 
        # ax.set_aspects('equal') controlls the form of the object (circle),
        # making sure that the unit on the x-axis is the same as the unit on the y-axis.
        # (adjustable = 'box') the plotting area will adjust to the dimensions of the figure.
        ax.set_aspect('equal', adjustable = 'box')

        plt.title(f"Circle: radius = {self.radius}, center = ({self.x}, {self.y})")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.show()
