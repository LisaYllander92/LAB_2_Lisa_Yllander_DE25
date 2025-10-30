from pytest import raises
from shapes import Shapes

def test_valid_init():
    shapes = Shapes(x = 2, y = 2)
    assert shapes.x == 2 and shapes.y == 2

def test_negative_x_value_fail():
    pass

def test_negative_y_value_fail():
    pass

def test_invalid_type_str_init_fail():
    pass 

def test_invalid_type_bool_init_fail():
    pass


def test_perimeter_calculation():
    pass

def test_area_calculation():
    pass



