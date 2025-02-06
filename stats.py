import random
import numpy as np

def sample_participants(participants, sample_size: int):
    """ Get the sampled participants """
    indexes = random.sample(range(len(participants)), sample_size)
    sampled_participants = []
    for i in indexes:
        sampled_participants.append(participants[i])
    return sampled_participants

def filter_participants_by_age(sampled_participants, min_age, max_age):
    """ Remove participants that are outside the age range """
    filtered_participants = []
    for participant in sampled_participants:
        if participant['age'] >= min_age and participant['age'] <= max_age:
            filtered_participants.append(participant)
    return filtered_participants

def filter_participants_by_height(sampled_participants_age_filtered, min_height, max_height):
    """ Remove participants that are outside the height range """
    sampled_participants_height_filtered = []
    for participant in sampled_participants_age_filtered:
        if participant['height'] >= min_height and participant['height'] <= max_height:
            sampled_participants_height_filtered.append(participant)
    return sampled_participants_height_filtered

def randomly_sample_and_filter_participants(
    participants: list,
    sample_size: int,
    min_age: int,
    max_age: int,
    min_height: int,
    max_height: int
):
    """Participants is a list of tuples, containing the age and height of each participant
    participants = [
                      {age: 25, height: 180}, 
                      {age: 30, height: 170}, 
                      {age: 35, height: 160}, 
    ]
    """    
    # Get the sampled participants
    sampled_participants = sample_participants(participants, sample_size)
    
    # Remove participants that are outside the age range
    sampled_participants_age_filtered = filter_participants_by_age(sampled_participants, min_age, max_age)
    
    # Remove participants that are outside the height range
    sampled_participants_height_filtered = filter_participants_by_height(sampled_participants_age_filtered, min_height, max_height)

    return sampled_participants_height_filtered


def calculate_cumulative_sum(array: np.ndarray) -> np.ndarray:
    """Calculate the cumulative sum of a numpy array"""
    
    # don't use the built-in numpy function
    result = np.zeros(array.shape)
    result[0] = array[0]
    for i in range(1, len(array)):
        result[i] = result[i-1] + array[i]

    return result