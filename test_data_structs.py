import numpy as np
import pandas as pd

def test_numpy_arrays():
    """Test that numpy arrays are equal"""
    # Create two numpy arrays
    array1 = np.array([1, 2, 3])
    array2 = np.array([1, 2, 3])
    # Check that the arrays are equal
    np.testing.assert_array_equal(array1, array2)

# Note that np.testing.assert_array_equal even works with nested numpy arrays!

def test_nested_numpy_arrays():
    """Test that nested numpy arrays are equal"""
    # Create two nested numpy arrays
    array1 = np.array([[1, 2], [3, 4]])
    array2 = np.array([[1, 2], [3, 4]])
    # Check that the nested arrays are equal
    np.testing.assert_array_equal(array1, array2)

def test_numpy_arrays_with_tolerance():
    """Test that numpy arrays are equal with tolerance"""
    # Create two numpy arrays
    array1 = np.array([1.0, 2.0, 3.0])
    array2 = np.array([1.00009, 2.0005, 3.0001])
    # Check that the arrays are equal with tolerance
    np.testing.assert_allclose(array1, array2, atol=1e-2)

def test_dictionaries_with_numpy_arrays():
    """Test that dictionaries with numpy arrays are equal"""
    # Doesn't work for all close with tolerances.
    # Create two dictionaries with numpy arrays
    dict1 = {"a": np.array([1, 2, 3]), "b": np.array([4, 5, 6])}
    dict2 = {"a": np.array([1, 2, 3]), "b": np.array([4, 5, 6])}
    # Check that the dictionaries are equal
    np.testing.assert_equal(dict1, dict2)

def test_pandas_dataframes():
    """Test that pandas DataFrames are equal"""
    # Create two pandas DataFrames
    df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df2 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    # Check that the DataFrames are equal
    pd.testing.assert_frame_equal(df1, df2)

def test_pandas_series():
    """Test that pandas Series are equal"""
    # Create two pandas Series
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([1, 2, 3])
    # Check that the Series are equal
    pd.testing.assert_series_equal(s1, s2)
