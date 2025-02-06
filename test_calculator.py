""" Import the add function so the test can use it """
import pytest
from calculator import add, divide, subtract, Point, Triangle

def test_add():
    """Test add function"""
    # Check that it adds two positive integers
    if add(1, 2) != 3:
        print("Test failed!")
        raise AssertionError("Test failed!")

    # Check that it adds zero
    if add(5, 0) != 5:
        print("Test failed!")
        raise AssertionError("Test failed!")

    # Check that it adds two negative integers
    if add(-1, -2) != -3:
        print("Test failed!")
        raise AssertionError("Test failed!")
    
    assert add(1, 2) == 3

def test_add1():
    """Test add using assert"""
    assert add(1, 2) == 3
    assert add(5, 0) == 5
    assert add(-1, -2) != 3

def test_division():
    """Test that function raises exact exception"""
    with pytest.raises(ZeroDivisionError) as e:
        divide(2, 0)
        assert str(e.value) == "Cannot divide by zero!"

def test_subtract():
    """Test that function raises exact exception"""
    assert subtract(5, 3) == 2

@pytest.mark.parametrize(
   ("p1x, p1y, p2x, p2y, p3x, p3y, expected"),
   [
      pytest.param(0, 0, 2, 0, 1, 1.7320, 1.7320, id="Equilateral triangle"),
      pytest.param(0, 0, 3, 0, 0, 4, 6, id="Right-angled triangle"),
      pytest.param(0, 0, 4, 0, 2, 8, 16, id="Isosceles triangle"),
      pytest.param(0, 0, 3, 0, 1, 4, 6, id="Scalene triangle"),
      pytest.param(0, 0, -3, 0, 0, -4, 6, id="Negative values")
   ]
)
def test_calculate_area(p1x, p1y, p2x, p2y, p3x, p3y, expected):
    p1 = Point(p1x, p1y)
    p2 = Point(p2x, p2y)
    p3 = Point(p3x, p3y)
    t = Triangle(p1, p2, p3)
    assert t.calculate_area() == expected