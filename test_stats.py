
import random
import numpy as np
import pytest
from stats import *
#sample_participants,filter_participants_by_age, filter_participants_by_height, randomly_sample_and_filter_participants

@pytest.fixture
def participants():
    return [
        {"age": 25, "height": 180},
        {"age": 30, "height": 170},
        {"age": 35, "height": 160},
        {"age": 38, "height": 165},
        {"age": 40, "height": 190},
        {"age": 45, "height": 200},
    ]

@pytest.fixture
def min_height_160():
    return 160

@pytest.fixture
def max_height_170():
    return 170

@pytest.fixture
def sample_size_2():
    return 2

def test_sample_participants(participants):
   # set random seed
   random.seed(0)

   sample_size = 2
   sampled_participants = sample_participants(participants, sample_size)
   expected = [{"age": 38, "height": 165}, {"age": 45, "height": 200}]
   assert sampled_participants == expected

def test_filter_participants_by_age(participants):
   min_age = 30
   max_age = 35
   filtered_participants = filter_participants_by_age(participants, min_age, max_age)
   expected = [{"age": 30, "height": 170}, {"age": 35, "height": 160}]
   assert filtered_participants == expected

def test_filter_participants_by_height(participants):
   min_height = 160
   max_height = 170
   filtered_participants = filter_participants_by_height(participants, min_height, max_height)
   expected = [{"age": 30, "height": 170}, {"age": 35, "height": 160}, {"age": 38, "height": 165}]
   assert filtered_participants == expected

def test_randomly_sample_and_filter_participants(participants):
   # set random seed
   random.seed(0)

   sample_size = 5
   min_age = 28
   max_age = 42
   min_height = 159
   max_height = 172
   filtered_participants = randomly_sample_and_filter_participants(
       participants, sample_size, min_age, max_age, min_height, max_height
   )
   expected = [{"age": 38, "height": 165}, {"age": 30, "height": 170}, {"age": 35, "height": 160}]
   assert filtered_participants == expected

def test_calculate_cumulative_sum():
    """Test calculate_cumulative_sum function"""
    array = np.array([1, 2, 3, 4, 5])
    expected_result = np.array([1, 3, 6, 10, 15])
    np.testing.assert_array_equal(calculate_cumulative_sum(array), expected_result)
