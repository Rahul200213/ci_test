import pytest
from src.area import area

def test_calculate_area_sq():
    assert area(2) == 4
    assert area(2.5) == 6.25

def test_calculate_area_sq_negative():
    with pytest.raises(TypeError):
        area(-2)

def test_calculate_area_sq_string():
    with pytest.raises(TypeError):
        area("2")
def test_calculate_area_sq_list():
    with pytest.raises(TypeError):
        area([1])
def test_calculate_area_sq_dict():
    with pytest.raises(TypeError):
        area({'a':1})

