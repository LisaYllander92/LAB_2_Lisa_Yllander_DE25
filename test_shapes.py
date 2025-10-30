from pytest import raises
from shapes import Shapes

def test_valid_init():
    shapes = Shapes(x = 2, y = 2)
    assert shapes.x == 2 and shapes.y == 2