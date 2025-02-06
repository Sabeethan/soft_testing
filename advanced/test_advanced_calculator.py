"""Module providing test functions for implementing tests"""

import pytest
from advanced_calculator import power, square_root

def test_power():
    """Test for the power function"""
    assert power(2, 3) == 8
    assert power(3, 3) == 27

def test_square_root():
    """Test that function raises exception"""
    with pytest.raises(ValueError):
        square_root(-1)

def test_square_root_exact():
    """Test that function raises exact exception"""
    with pytest.raises(ValueError) as e:
        square_root(-1)
    assert str(e.value) == "Cannot compute square root of negative number yet!"
