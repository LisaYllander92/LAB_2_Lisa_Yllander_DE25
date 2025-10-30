from pytest import raises
from shapes import Shapes

def test_valid_init():
    shape = Shapes(x = 2, y = 2)
    assert shape.x == 2 and shape.y == 2

def test_invalid_type_str_init_fail():
    with raises(TypeError):
        Shapes(x = "1", y = 1)

def test_invalid_type_bool_init_fail():
    with raises(TypeError):
        Shapes(x = True, y = 2)

def test_perimeter_calculation():
    pass

def test_area_calculation():
    pass



