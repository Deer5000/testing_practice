import pytest

import math
# def calculate_kinetic_energy(mass, velocity): 
#     """Returns kinetic energy of mass [kg] with velocity [ms]."""
#     return 0.5 * mass * velocity ** 2


# def test_calculate_kinetic_energy():
#     mass = 10 # [kg]
#     velocity = 4 # [m/s]
#     assert calculate_kinetic_energy(mass, velocity) == 80


# def calculate_kinetic_energy(mass, velocity): 
#     """Returns kinetic energy of mass [kg] with velocity [ms]."""
#     return mass * velocity ** 2

############################# EXERCISE 1 #########################


def get_average(li):
    if not li:
            return float('NaN')
    sum = 0
    for num in li:
        sum += num
        mean = sum / len(li)
    return mean

def test_get_average_empty_list():
    assert math.isnan(get_average([]))



##########################################

# test_exception.py
def palindrome(word):
    if not isinstance(word, str):
        raise TypeError('Please provide a string argument')
    return word == word[::-1]

palindrome('44') 


def test_palindrom():
    with pytest.raises(TypeError):
        palindrome('44')